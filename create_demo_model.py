"""
create_demo_model.py — Generate a Lightweight Demo Model

This script creates a MobileNetV2-based model initialized with ImageNet weights.
The model produces predictions immediately (though not accurately trained on plant diseases).
This lets you test the full pipeline — web app, predict.py, etc. — without waiting for training.

For accurate predictions, train the full model using: python train.py

Usage:
    python create_demo_model.py
"""

import os
import json
import numpy as np
import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.applications import MobileNetV2

from config import (
    IMAGE_SIZE, MODEL_DIR, DEMO_MODEL_PATH,
    CLASS_NAMES, NUM_CLASSES
)


def create_demo_model():
    print("\n🌿  Creating Demo Model (MobileNetV2 + ImageNet weights)")
    print("─" * 55)
    print("⚠️  This model uses ImageNet weights — NOT trained on plant diseases.")
    print("   Predictions will not be accurate.")
    print("   For accurate results, run: python train.py")
    print("─" * 55)

    os.makedirs(MODEL_DIR, exist_ok=True)

    # Build MobileNetV2-based model (same architecture as train.py)
    base_model = MobileNetV2(
        input_shape=(*IMAGE_SIZE, 3),
        include_top=False,
        weights="imagenet",
    )
    base_model.trainable = False

    inputs = tf.keras.Input(shape=(*IMAGE_SIZE, 3))
    x = base_model(inputs, training=False)
    x = layers.GlobalAveragePooling2D()(x)
    x = layers.BatchNormalization()(x)
    x = layers.Dense(512, activation="relu")(x)
    x = layers.Dropout(0.4)(x)
    x = layers.Dense(256, activation="relu")(x)
    x = layers.Dropout(0.3)(x)
    outputs = layers.Dense(NUM_CLASSES, activation="softmax")(x)

    model = models.Model(inputs, outputs)
    model.compile(
        optimizer="adam",
        loss="categorical_crossentropy",
        metrics=["accuracy"],
    )

    print(f"\n✅ Model created: {model.count_params():,} total parameters")

    # Save model
    model.save(DEMO_MODEL_PATH)
    print(f"✅ Demo model saved to: {DEMO_MODEL_PATH}")

    # Save class indices
    class_indices = {name: i for i, name in enumerate(CLASS_NAMES)}
    class_indices_path = os.path.join(MODEL_DIR, "class_indices.json")
    with open(class_indices_path, "w") as f:
        json.dump(class_indices, f, indent=2)
    print(f"✅ Class indices saved to: {class_indices_path}")

    # Quick smoke test
    print("\n🧪 Running smoke test...")
    dummy_input = np.random.random((1, *IMAGE_SIZE, 3)).astype(np.float32)
    prediction = model.predict(dummy_input, verbose=0)
    top_class_idx = np.argmax(prediction[0])
    top_class = CLASS_NAMES[top_class_idx]
    top_conf = prediction[0][top_class_idx] * 100

    print(f"   Dummy prediction: {top_class}")
    print(f"   Confidence: {top_conf:.2f}%")
    print("\n✅ Demo model is ready!")
    print("\n📌 Next steps:")
    print("   1. Start the web app : python app.py")
    print("   2. CLI prediction    : python predict.py --image path/to/leaf.jpg")
    print("   3. Train real model  : python train.py  (requires dataset)")


if __name__ == "__main__":
    create_demo_model()
