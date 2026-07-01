"""
config.py — Central Configuration for Plant Disease Detection Project
"""

import os

# ─────────────────────────────────────────────
# Paths
# ─────────────────────────────────────────────
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATASET_DIR = os.path.join(BASE_DIR, "dataset", "PlantVillage")
if os.path.exists(os.path.join(DATASET_DIR, "dataset", "train")):
    DATASET_DIR = os.path.join(DATASET_DIR, "dataset", "train")
MODEL_DIR = os.path.join(BASE_DIR, "models")
DEMO_MODEL_PATH = os.path.join(MODEL_DIR, "demo_model.keras")
TRAINED_MODEL_PATH = os.path.join(MODEL_DIR, "plant_disease_model.keras")
UPLOAD_FOLDER = os.path.join(BASE_DIR, "static", "uploads")
OUTPUT_DIR = os.path.join(BASE_DIR, "outputs")

# ─────────────────────────────────────────────
# Image Settings
# ─────────────────────────────────────────────
IMAGE_SIZE = (224, 224)
IMAGE_SHAPE = (224, 224, 3)

# ─────────────────────────────────────────────
# Training Hyperparameters
# ─────────────────────────────────────────────
BATCH_SIZE = 32
EPOCHS = 25
FINE_TUNE_EPOCHS = 10
LEARNING_RATE = 1e-4
FINE_TUNE_LEARNING_RATE = 1e-5
FINE_TUNE_AT = 100           # Layer index from which to fine-tune in MobileNetV2

# ─────────────────────────────────────────────
# Dataset Split Ratios
# ─────────────────────────────────────────────
TRAIN_SPLIT = 0.80
VAL_SPLIT = 0.10
TEST_SPLIT = 0.10

# ─────────────────────────────────────────────
# Flask Settings
# ─────────────────────────────────────────────
FLASK_HOST = "0.0.0.0"
FLASK_PORT = 5000
FLASK_DEBUG = False
MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16 MB max upload
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "webp", "bmp"}

# ─────────────────────────────────────────────
# PlantVillage — 38 Disease Classes
# ─────────────────────────────────────────────
CLASS_NAMES = [
    "Apple___Apple_scab",
    "Apple___Black_rot",
    "Apple___Cedar_apple_rust",
    "Apple___healthy",
    "Blueberry___healthy",
    "Cherry_(including_sour)___Powdery_mildew",
    "Cherry_(including_sour)___healthy",
    "Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot",
    "Corn_(maize)___Common_rust_",
    "Corn_(maize)___Northern_Leaf_Blight",
    "Corn_(maize)___healthy",
    "Grape___Black_rot",
    "Grape___Esca_(Black_Measles)",
    "Grape___Leaf_blight_(Isariopsis_Leaf_Spot)",
    "Grape___healthy",
    "Orange___Haunglongbing_(Citrus_greening)",
    "Peach___Bacterial_spot",
    "Peach___healthy",
    "Pepper,_bell___Bacterial_spot",
    "Pepper,_bell___healthy",
    "Potato___Early_blight",
    "Potato___Late_blight",
    "Potato___healthy",
    "Raspberry___healthy",
    "Soybean___healthy",
    "Squash___Powdery_mildew",
    "Strawberry___Leaf_scorch",
    "Strawberry___healthy",
    "Tomato___Bacterial_spot",
    "Tomato___Early_blight",
    "Tomato___Late_blight",
    "Tomato___Leaf_Mold",
    "Tomato___Septoria_leaf_spot",
    "Tomato___Spider_mites Two-spotted_spider_mite",
    "Tomato___Target_Spot",
    "Tomato___Tomato_Yellow_Leaf_Curl_Virus",
    "Tomato___Tomato_mosaic_virus",
    "Tomato___healthy",
]

def get_num_classes():
    if os.path.exists(DATASET_DIR):
        dirs = [d for d in os.listdir(DATASET_DIR) if os.path.isdir(os.path.join(DATASET_DIR, d))]
        if len(dirs) > 0:
            return len(dirs)
    return len(CLASS_NAMES)

NUM_CLASSES = get_num_classes()

# ─────────────────────────────────────────────
# Data Augmentation
# ─────────────────────────────────────────────
AUGMENTATION_CONFIG = {
    "rotation_range": 40,
    "width_shift_range": 0.2,
    "height_shift_range": 0.2,
    "shear_range": 0.2,
    "zoom_range": 0.2,
    "horizontal_flip": True,
    "brightness_range": [0.8, 1.2],
    "fill_mode": "nearest",
}
