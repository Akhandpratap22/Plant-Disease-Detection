"""
predict.py — CLI Prediction Tool for Plant Disease Detection

Usage:
    python predict.py --image path/to/leaf.jpg
    python predict.py --image leaf.jpg --model models/plant_disease_model.keras
    python predict.py --image leaf.jpg --top_k 3
"""

import os
import sys
import json
import argparse
import numpy as np
from PIL import Image
import tensorflow as tf

from config import (
    IMAGE_SIZE, TRAINED_MODEL_PATH, DEMO_MODEL_PATH,
    MODEL_DIR, CLASS_NAMES
)
from disease_info import get_disease_info


def load_model(model_path: str) -> tf.keras.Model:
    """Load a saved Keras model."""
    if not os.path.exists(model_path):
        print(f"❌ Model not found: {model_path}")
        sys.exit(1)
    print(f"✅ Model loaded: {model_path}")
    return tf.keras.models.load_model(model_path)


def load_class_names(model_dir: str) -> list:
    """Load class names from saved class_indices.json or use defaults."""
    indices_path = os.path.join(model_dir, "class_indices.json")
    if os.path.exists(indices_path):
        with open(indices_path, "r") as f:
            class_indices = json.load(f)
        # Invert: index → class name
        return [k for k, _ in sorted(class_indices.items(), key=lambda x: x[1])]
    return CLASS_NAMES


def preprocess_image(image_path: str) -> np.ndarray:
    """Load and preprocess a single image for prediction."""
    if not os.path.exists(image_path):
        print(f"❌ Image not found: {image_path}")
        sys.exit(1)

    img = Image.open(image_path).convert("RGB")
    img = img.resize(IMAGE_SIZE, Image.LANCZOS)
    img_array = np.array(img, dtype=np.float32) / 255.0
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
    return img_array


def predict(model, img_array: np.ndarray, class_names: list, top_k: int = 1):
    """Run prediction and return top-k results."""
    predictions = model.predict(img_array, verbose=0)[0]
    top_k_indices = np.argsort(predictions)[::-1][:top_k]

    results = []
    for idx in top_k_indices:
        results.append({
            "rank": len(results) + 1,
            "class_name": class_names[idx],
            "confidence": float(predictions[idx]) * 100,
        })
    return results


def display_results(results: list):
    """Pretty-print prediction results in the terminal."""
    print("\n" + "─" * 60)
    print("🌿  PLANT DISEASE DETECTION — PREDICTION RESULTS")
    print("─" * 60)

    for result in results:
        class_name = result["class_name"]
        confidence = result["confidence"]
        info = get_disease_info(class_name)

        rank_emoji = ["🥇", "🥈", "🥉"][result["rank"] - 1] if result["rank"] <= 3 else f"#{result['rank']}"
        status_emoji = "✅ HEALTHY" if info["healthy"] else "🚨 DISEASED"

        print(f"\n{rank_emoji} Prediction #{result['rank']}")
        print(f"   Plant      : {info['plant']}")
        print(f"   Disease    : {info['disease']}")
        print(f"   Status     : {status_emoji}")
        print(f"   Confidence : {confidence:.2f}%")
        print(f"   Severity   : {info['severity']}")

        if not info["healthy"]:
            print(f"\n   📋 Description:")
            print(f"      {info['description'][:100]}...")

            if info["symptoms"]:
                print(f"\n   🔍 Symptoms:")
                for s in info["symptoms"][:2]:
                    print(f"      • {s}")

            if info["treatment"]:
                print(f"\n   💊 Treatment:")
                for t in info["treatment"][:2]:
                    print(f"      • {t}")
        else:
            print(f"\n   ℹ️  {info['prevention']}")

    print("\n" + "─" * 60)


def main(args):
    print("\n🌿  Plant Disease Detection — CLI Prediction Tool")

    # Determine model path
    if args.model:
        model_path = args.model
    elif os.path.exists(TRAINED_MODEL_PATH):
        model_path = TRAINED_MODEL_PATH
    elif os.path.exists(DEMO_MODEL_PATH):
        model_path = DEMO_MODEL_PATH
        print("⚠️  Using demo model. For accurate results, train with: python train.py")
    else:
        print("❌ No model found. Run: python create_demo_model.py  or  python train.py")
        sys.exit(1)

    model = load_model(model_path)
    class_names = load_class_names(MODEL_DIR)
    img_array = preprocess_image(args.image)

    print(f"🖼️  Processing: {args.image}")
    results = predict(model, img_array, class_names, args.top_k)
    display_results(results)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Predict plant disease from a leaf image")
    parser.add_argument("--image", type=str, required=True, help="Path to the leaf image")
    parser.add_argument("--model", type=str, default=None, help="Path to the model file (optional)")
    parser.add_argument("--top_k", type=int, default=3, help="Show top K predictions (default: 3)")
    args = parser.parse_args()
    main(args)
