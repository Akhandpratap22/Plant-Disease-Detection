"""
app.py — Flask Web Application for Plant Disease Detection

Usage:
    python app.py
    Open: http://localhost:5000
"""

import os
import json
import uuid
import numpy as np
from PIL import Image
from datetime import datetime
import tensorflow as tf
from flask import Flask, request, render_template, jsonify, redirect, url_for, flash

from config import (
    IMAGE_SIZE, TRAINED_MODEL_PATH, DEMO_MODEL_PATH,
    MODEL_DIR, CLASS_NAMES, UPLOAD_FOLDER, ALLOWED_EXTENSIONS,
    MAX_CONTENT_LENGTH, FLASK_HOST, FLASK_PORT, FLASK_DEBUG
)
from disease_info import get_disease_info, get_severity_color

# ─────────────────────────────────────────────────────────────────────────────
# App Initialization
# ─────────────────────────────────────────────────────────────────────────────

app = Flask(__name__)
app.secret_key = os.urandom(24)
app.config["MAX_CONTENT_LENGTH"] = MAX_CONTENT_LENGTH
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# ─────────────────────────────────────────────────────────────────────────────
# Model Loading
# ─────────────────────────────────────────────────────────────────────────────

model = None
class_names = CLASS_NAMES
is_demo_model = False


def load_class_names():
    """Load class names from saved JSON or use defaults."""
    indices_path = os.path.join(MODEL_DIR, "class_indices.json")
    if os.path.exists(indices_path):
        with open(indices_path, "r") as f:
            class_indices = json.load(f)
        return [k for k, _ in sorted(class_indices.items(), key=lambda x: x[1])]
    return CLASS_NAMES


def load_model_on_startup():
    """Load the best available model at startup."""
    global model, class_names, is_demo_model

    if os.path.exists(TRAINED_MODEL_PATH):
        print(f"✅ Loading trained model: {TRAINED_MODEL_PATH}")
        model = tf.keras.models.load_model(TRAINED_MODEL_PATH)
        is_demo_model = False
    elif os.path.exists(DEMO_MODEL_PATH):
        print(f"⚠️  Loading demo model: {DEMO_MODEL_PATH}")
        print("   For accurate results, train the model: python train.py")
        model = tf.keras.models.load_model(DEMO_MODEL_PATH)
        is_demo_model = True
    else:
        print("❌ No model found!")
        print("   Run: python create_demo_model.py")
        print("   Or:  python train.py")
        model = None

    class_names = load_class_names()
    return model is not None


# ─────────────────────────────────────────────────────────────────────────────
# Helper Functions
# ─────────────────────────────────────────────────────────────────────────────

def allowed_file(filename: str) -> bool:
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


def preprocess_image(image_path: str) -> np.ndarray:
    """Load, resize, and normalize an image for model input."""
    img = Image.open(image_path).convert("RGB")
    img = img.resize(IMAGE_SIZE, Image.LANCZOS)
    img_array = np.array(img, dtype=np.float32) / 255.0
    return np.expand_dims(img_array, axis=0)


def run_prediction(image_path: str, top_k: int = 5) -> dict:
    """Run inference and return top-k predictions with disease info."""
    if model is None:
        return {"error": "Model not loaded"}

    img_array = preprocess_image(image_path)
    predictions = model.predict(img_array, verbose=0)[0]
    top_k_indices = np.argsort(predictions)[::-1][:top_k]

    results = []
    for i, idx in enumerate(top_k_indices):
        cls_name = class_names[idx]
        confidence = float(predictions[idx]) * 100
        info = get_disease_info(cls_name)
        results.append({
            "rank": i + 1,
            "class_name": cls_name,
            "confidence": round(confidence, 2),
            "confidence_bar": min(100, round(confidence, 1)),
            "plant": info["plant"],
            "disease": info["disease"],
            "healthy": info["healthy"],
            "severity": info["severity"],
            "severity_class": get_severity_color(info["severity"]),
            "description": info["description"],
            "symptoms": info["symptoms"],
            "treatment": info["treatment"],
            "prevention": info["prevention"],
        })

    return {
        "top_prediction": results[0] if results else None,
        "alternatives": results[1:] if len(results) > 1 else [],
        "all_predictions": results,
        "is_demo_model": is_demo_model,
        "model_type": "Demo Model (Not Trained)" if is_demo_model else "Trained Model",
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }


def cleanup_old_uploads(max_files: int = 50):
    """Remove old uploaded files to save disk space."""
    try:
        files = sorted(
            [os.path.join(UPLOAD_FOLDER, f) for f in os.listdir(UPLOAD_FOLDER)],
            key=os.path.getctime,
        )
        while len(files) > max_files:
            os.remove(files.pop(0))
    except Exception:
        pass


# ─────────────────────────────────────────────────────────────────────────────
# Routes
# ─────────────────────────────────────────────────────────────────────────────

@app.route("/")
def index():
    """Home page — image upload form."""
    return render_template(
        "index.html",
        model_loaded=(model is not None),
        is_demo_model=is_demo_model,
    )


@app.route("/predict", methods=["POST"])
def predict():
    """Handle image upload and return prediction results."""
    if model is None:
        flash("❌ Model not loaded. Run: python create_demo_model.py", "error")
        return redirect(url_for("index"))

    if "file" not in request.files:
        flash("No file uploaded.", "error")
        return redirect(url_for("index"))

    file = request.files["file"]

    if file.filename == "":
        flash("No file selected.", "error")
        return redirect(url_for("index"))

    if not allowed_file(file.filename):
        flash(f"Invalid file type. Allowed: {', '.join(ALLOWED_EXTENSIONS)}", "error")
        return redirect(url_for("index"))

    # Save uploaded file with a unique name
    ext = file.filename.rsplit(".", 1)[1].lower()
    unique_filename = f"{uuid.uuid4().hex}.{ext}"
    save_path = os.path.join(UPLOAD_FOLDER, unique_filename)
    file.save(save_path)

    cleanup_old_uploads()

    # Run prediction
    result = run_prediction(save_path)
    if "error" in result:
        flash(result["error"], "error")
        return redirect(url_for("index"))

    # Relative path for displaying in HTML
    image_url = f"/static/uploads/{unique_filename}"

    return render_template(
        "result.html",
        image_url=image_url,
        result=result,
        top=result["top_prediction"],
        alternatives=result["alternatives"],
        is_demo_model=is_demo_model,
    )


@app.route("/api/predict", methods=["POST"])
def api_predict():
    """JSON API endpoint for prediction (for future mobile/integration use)."""
    if model is None:
        return jsonify({"error": "Model not loaded"}), 503

    if "file" not in request.files:
        return jsonify({"error": "No file provided"}), 400

    file = request.files["file"]
    if not allowed_file(file.filename):
        return jsonify({"error": "Invalid file type"}), 400

    ext = file.filename.rsplit(".", 1)[1].lower()
    unique_filename = f"{uuid.uuid4().hex}.{ext}"
    save_path = os.path.join(UPLOAD_FOLDER, unique_filename)
    file.save(save_path)

    result = run_prediction(save_path, top_k=5)
    return jsonify(result)


@app.route("/about")
def about():
    return render_template("index.html", show_about=True, model_loaded=(model is not None))


@app.route("/health")
def health():
    return jsonify({
        "status": "ok",
        "model_loaded": model is not None,
        "is_demo_model": is_demo_model,
        "num_classes": len(class_names),
    })


# ─────────────────────────────────────────────────────────────────────────────
# Error Handlers
# ─────────────────────────────────────────────────────────────────────────────

@app.errorhandler(413)
def too_large(e):
    flash("File too large. Maximum size is 16 MB.", "error")
    return redirect(url_for("index"))


@app.errorhandler(404)
def not_found(e):
    return render_template("index.html", model_loaded=(model is not None)), 404


# ─────────────────────────────────────────────────────────────────────────────
# Main
# ─────────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("\n" + "🌿 " * 15)
    print("   PLANT DISEASE DETECTION — WEB APPLICATION")
    print("🌿 " * 15)

    model_ok = load_model_on_startup()

    if model_ok:
        print(f"\n✅ Ready! Open your browser at: http://localhost:{FLASK_PORT}")
    else:
        print(f"\n⚠️  Starting without model. Run: python create_demo_model.py")
        print(f"   Then restart: python app.py")

    print(f"   Classes: {len(class_names)}")
    print(f"   Upload folder: {UPLOAD_FOLDER}")
    print("─" * 50)

    app.run(
        host=FLASK_HOST,
        port=FLASK_PORT,
        debug=FLASK_DEBUG,
    )
