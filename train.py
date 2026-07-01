"""
train.py — Plant Disease Detection Model Training
Uses MobileNetV2 Transfer Learning on the PlantVillage Dataset

Usage:
    python train.py
    python train.py --epochs 30 --batch_size 32 --dataset dataset/PlantVillage
"""

import os
import argparse
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras import layers, models, optimizers, callbacks
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from sklearn.utils.class_weight import compute_class_weight
from config import (
    DATASET_DIR, MODEL_DIR, OUTPUT_DIR,
    IMAGE_SIZE, BATCH_SIZE, EPOCHS, FINE_TUNE_EPOCHS,
    LEARNING_RATE, FINE_TUNE_LEARNING_RATE, FINE_TUNE_AT,
    TRAIN_SPLIT, VAL_SPLIT, AUGMENTATION_CONFIG,
    TRAINED_MODEL_PATH, NUM_CLASSES
)

# ─────────────────────────────────────────────────────────────────────────────
# Setup
# ─────────────────────────────────────────────────────────────────────────────

def setup_directories():
    os.makedirs(MODEL_DIR, exist_ok=True)
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    print(f"✅ Model directory: {MODEL_DIR}")
    print(f"✅ Output directory: {OUTPUT_DIR}")


def check_gpu():
    gpus = tf.config.list_physical_devices("GPU")
    if gpus:
        print(f"✅ GPU available: {[g.name for g in gpus]}")
        for gpu in gpus:
            tf.config.experimental.set_memory_growth(gpu, True)
    else:
        print("⚠️  No GPU detected. Training will be slower on CPU.")
        print("   Consider using Google Colab for faster training.")


# ─────────────────────────────────────────────────────────────────────────────
# Data Loading
# ─────────────────────────────────────────────────────────────────────────────

def build_data_generators(dataset_dir: str, batch_size: int):
    """Build train, validation, and test data generators."""

    # Training augmentation
    train_datagen = ImageDataGenerator(
        rescale=1.0 / 255.0,
        validation_split=VAL_SPLIT + (1 - TRAIN_SPLIT - VAL_SPLIT),  # 20% = val + test
        **AUGMENTATION_CONFIG,
    )

    # Validation/Test — only rescale
    val_test_datagen = ImageDataGenerator(
        rescale=1.0 / 255.0,
        validation_split=VAL_SPLIT + (1 - TRAIN_SPLIT - VAL_SPLIT),
    )

    print(f"\n📂 Loading dataset from: {dataset_dir}")

    train_gen = train_datagen.flow_from_directory(
        dataset_dir,
        target_size=IMAGE_SIZE,
        batch_size=batch_size,
        class_mode="categorical",
        subset="training",
        shuffle=True,
        seed=42,
    )

    val_gen = val_test_datagen.flow_from_directory(
        dataset_dir,
        target_size=IMAGE_SIZE,
        batch_size=batch_size,
        class_mode="categorical",
        subset="validation",
        shuffle=False,
        seed=42,
    )

    print(f"\n📊 Dataset Summary:")
    print(f"   Training samples  : {train_gen.samples}")
    print(f"   Validation samples: {val_gen.samples}")
    print(f"   Number of classes : {train_gen.num_classes}")
    print(f"   Class names       : {list(train_gen.class_indices.keys())[:5]}...")

    return train_gen, val_gen


# ─────────────────────────────────────────────────────────────────────────────
# Model Building
# ─────────────────────────────────────────────────────────────────────────────

def build_model(num_classes: int) -> tf.keras.Model:
    """
    Build a MobileNetV2-based transfer learning model.
    Phase 1: Train only the top classification head.
    Phase 2: Fine-tune the top layers of MobileNetV2.
    """

    # Load MobileNetV2 pretrained on ImageNet (without top classification layer)
    base_model = MobileNetV2(
        input_shape=(*IMAGE_SIZE, 3),
        include_top=False,
        weights="imagenet",
    )
    base_model.trainable = False  # Freeze base model initially

    # Build the model
    inputs = tf.keras.Input(shape=(*IMAGE_SIZE, 3))
    x = base_model(inputs, training=False)
    x = layers.GlobalAveragePooling2D()(x)
    x = layers.BatchNormalization()(x)
    x = layers.Dense(512, activation="relu")(x)
    x = layers.Dropout(0.4)(x)
    x = layers.Dense(256, activation="relu")(x)
    x = layers.Dropout(0.3)(x)
    outputs = layers.Dense(num_classes, activation="softmax")(x)

    model = models.Model(inputs, outputs)

    print("\n🧠 Model Architecture:")
    print(f"   Base: MobileNetV2 (pretrained on ImageNet)")
    print(f"   Top : GlobalAvgPool → BN → Dense(512) → Dropout → Dense(256) → Dropout → Dense({num_classes})")
    print(f"   Total params: {model.count_params():,}")

    return model, base_model


# ─────────────────────────────────────────────────────────────────────────────
# Training
# ─────────────────────────────────────────────────────────────────────────────

def get_callbacks(model_save_path: str):
    """Define training callbacks."""
    return [
        callbacks.ModelCheckpoint(
            filepath=model_save_path,
            monitor="val_accuracy",
            save_best_only=True,
            verbose=1,
        ),
        callbacks.EarlyStopping(
            monitor="val_loss",
            patience=7,
            restore_best_weights=True,
            verbose=1,
        ),
        callbacks.ReduceLROnPlateau(
            monitor="val_loss",
            factor=0.3,
            patience=3,
            min_lr=1e-7,
            verbose=1,
        ),
        callbacks.TensorBoard(
            log_dir=os.path.join(OUTPUT_DIR, "tensorboard_logs"),
            histogram_freq=1,
        ),
    ]


def train_phase1(model, train_gen, val_gen, epochs: int):
    """Phase 1: Train only the top classification head."""
    print("\n" + "=" * 60)
    print("📚 PHASE 1: Training Classification Head (Base Frozen)")
    print("=" * 60)

    model.compile(
        optimizer=optimizers.Adam(learning_rate=LEARNING_RATE),
        loss="categorical_crossentropy",
        metrics=["accuracy"],
    )

    history = model.fit(
        train_gen,
        epochs=epochs,
        validation_data=val_gen,
        callbacks=get_callbacks(TRAINED_MODEL_PATH),
        verbose=1,
    )
    return history


def train_phase2(model, base_model, train_gen, val_gen, fine_tune_epochs: int):
    """Phase 2: Fine-tune top layers of MobileNetV2."""
    print("\n" + "=" * 60)
    print(f"🔧 PHASE 2: Fine-Tuning (Unfreezing from layer {FINE_TUNE_AT})")
    print("=" * 60)

    base_model.trainable = True
    # Freeze all layers before FINE_TUNE_AT
    for layer in base_model.layers[:FINE_TUNE_AT]:
        layer.trainable = False

    trainable_layers = sum(1 for l in base_model.layers if l.trainable)
    print(f"   Trainable layers in base model: {trainable_layers}")

    model.compile(
        optimizer=optimizers.Adam(learning_rate=FINE_TUNE_LEARNING_RATE),
        loss="categorical_crossentropy",
        metrics=["accuracy"],
    )

    history = model.fit(
        train_gen,
        epochs=fine_tune_epochs,
        validation_data=val_gen,
        callbacks=get_callbacks(TRAINED_MODEL_PATH),
        verbose=1,
    )
    return history


# ─────────────────────────────────────────────────────────────────────────────
# Visualization
# ─────────────────────────────────────────────────────────────────────────────

def plot_training_history(history1, history2=None):
    """Plot training and validation accuracy/loss curves."""
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    fig.suptitle("Plant Disease Detection — Training History", fontsize=14, fontweight="bold")

    # Combine histories
    acc = history1.history["accuracy"]
    val_acc = history1.history["val_accuracy"]
    loss = history1.history["loss"]
    val_loss = history1.history["val_loss"]

    if history2:
        acc += history2.history["accuracy"]
        val_acc += history2.history["val_accuracy"]
        loss += history2.history["loss"]
        val_loss += history2.history["val_loss"]

    epochs_range = range(len(acc))

    # Accuracy
    axes[0].plot(epochs_range, acc, label="Training Accuracy", color="#4CAF50", linewidth=2)
    axes[0].plot(epochs_range, val_acc, label="Validation Accuracy", color="#FF9800", linewidth=2)
    axes[0].set_title("Accuracy")
    axes[0].set_xlabel("Epoch")
    axes[0].set_ylabel("Accuracy")
    axes[0].legend()
    axes[0].grid(True, alpha=0.3)

    # Loss
    axes[1].plot(epochs_range, loss, label="Training Loss", color="#4CAF50", linewidth=2)
    axes[1].plot(epochs_range, val_loss, label="Validation Loss", color="#FF9800", linewidth=2)
    axes[1].set_title("Loss")
    axes[1].set_xlabel("Epoch")
    axes[1].set_ylabel("Loss")
    axes[1].legend()
    axes[1].grid(True, alpha=0.3)

    if history2:
        split = len(history1.history["accuracy"])
        for ax in axes:
            ax.axvline(split, color="red", linestyle="--", alpha=0.7, label="Fine-tuning start")

    plt.tight_layout()
    save_path = os.path.join(OUTPUT_DIR, "training_history.png")
    plt.savefig(save_path, dpi=150, bbox_inches="tight")
    print(f"\n📊 Training history plot saved to: {save_path}")
    plt.show()


# ─────────────────────────────────────────────────────────────────────────────
# Main
# ─────────────────────────────────────────────────────────────────────────────

def main(args):
    print("\n" + "🌿 " * 15)
    print("   PLANT DISEASE DETECTION — MODEL TRAINING")
    print("🌿 " * 15 + "\n")

    setup_directories()
    check_gpu()

    dataset_dir = args.dataset or DATASET_DIR
    if not os.path.exists(dataset_dir):
        print(f"\n❌ Dataset not found at: {dataset_dir}")
        print("   Please download the PlantVillage dataset first:")
        print("   python download_dataset.py")
        return

    # Load data
    train_gen, val_gen = build_data_generators(dataset_dir, args.batch_size)
    num_classes = train_gen.num_classes

    # Build model
    model, base_model = build_model(num_classes)

    # Phase 1: Train classification head
    history1 = train_phase1(model, train_gen, val_gen, args.epochs)

    # Phase 2: Fine-tuning
    history2 = None
    if args.fine_tune:
        history2 = train_phase2(model, base_model, train_gen, val_gen, args.fine_tune_epochs)

    # Plot results
    plot_training_history(history1, history2)

    # Save class indices
    import json
    class_indices_path = os.path.join(MODEL_DIR, "class_indices.json")
    with open(class_indices_path, "w") as f:
        json.dump(train_gen.class_indices, f, indent=2)
    print(f"\n✅ Class indices saved to: {class_indices_path}")

    print(f"\n🎉 Training complete!")
    print(f"   Best model saved to: {TRAINED_MODEL_PATH}")
    print(f"   Run evaluation: python evaluate.py")
    print(f"   Start web app:  python app.py")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Train Plant Disease Detection Model")
    parser.add_argument("--dataset", type=str, default=None, help="Path to dataset directory")
    parser.add_argument("--epochs", type=int, default=EPOCHS, help="Number of training epochs (Phase 1)")
    parser.add_argument("--fine_tune_epochs", type=int, default=FINE_TUNE_EPOCHS, help="Fine-tuning epochs (Phase 2)")
    parser.add_argument("--batch_size", type=int, default=BATCH_SIZE, help="Batch size")
    parser.add_argument("--fine_tune", action="store_true", default=True, help="Enable Phase 2 fine-tuning")
    parser.add_argument("--no_fine_tune", dest="fine_tune", action="store_false", help="Disable fine-tuning")
    args = parser.parse_args()
    main(args)
