"""
evaluate.py — Model Evaluation for Plant Disease Detection

Generates:
  - Classification report (Accuracy, Precision, Recall, F1 per class)
  - Confusion matrix heatmap
  - Per-class performance bar chart

Usage:
    python evaluate.py
    python evaluate.py --model models/plant_disease_model.keras --dataset dataset/PlantVillage
"""

import os
import json
import argparse
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import seaborn as sns
import tensorflow as tf
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from tensorflow.keras.preprocessing.image import ImageDataGenerator

from config import (
    DATASET_DIR, MODEL_DIR, OUTPUT_DIR,
    TRAINED_MODEL_PATH, DEMO_MODEL_PATH,
    IMAGE_SIZE, BATCH_SIZE, CLASS_NAMES, VAL_SPLIT, TRAIN_SPLIT
)


def load_model(model_path: str) -> tf.keras.Model:
    if not os.path.exists(model_path):
        print(f"❌ Model not found at: {model_path}")
        raise FileNotFoundError(f"Model not found: {model_path}")
    print(f"✅ Loading model from: {model_path}")
    return tf.keras.models.load_model(model_path)


def build_test_generator(dataset_dir: str):
    datagen = ImageDataGenerator(
        rescale=1.0 / 255.0,
        validation_split=VAL_SPLIT + (1 - TRAIN_SPLIT - VAL_SPLIT),
    )
    gen = datagen.flow_from_directory(
        dataset_dir,
        target_size=IMAGE_SIZE,
        batch_size=BATCH_SIZE,
        class_mode="categorical",
        subset="validation",
        shuffle=False,
    )
    return gen


def evaluate_model(model, test_gen):
    print("\n🔍 Running evaluation on test set...")
    predictions = model.predict(test_gen, verbose=1)
    y_pred = np.argmax(predictions, axis=1)
    y_true = test_gen.classes

    # Load class names from generator
    class_names = list(test_gen.class_indices.keys())

    acc = accuracy_score(y_true, y_pred)
    print(f"\n✅ Overall Accuracy: {acc * 100:.2f}%")

    report = classification_report(y_true, y_pred, target_names=class_names, digits=4)
    print("\n📊 Classification Report:")
    print(report)

    return y_true, y_pred, class_names, report


def plot_confusion_matrix(y_true, y_pred, class_names: list):
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    cm = confusion_matrix(y_true, y_pred)
    cm_normalized = cm.astype("float") / cm.sum(axis=1)[:, np.newaxis]

    n = len(class_names)
    fig_size = max(16, n // 2)
    fig, ax = plt.subplots(figsize=(fig_size, fig_size - 2))

    sns.heatmap(
        cm_normalized,
        annot=True,
        fmt=".2f",
        cmap="Greens",
        xticklabels=[c.split("___")[-1].replace("_", " ") for c in class_names],
        yticklabels=[c.split("___")[-1].replace("_", " ") for c in class_names],
        ax=ax,
        linewidths=0.5,
    )

    ax.set_title("Confusion Matrix (Normalized)", fontsize=16, fontweight="bold", pad=20)
    ax.set_xlabel("Predicted Label", fontsize=12)
    ax.set_ylabel("True Label", fontsize=12)
    plt.xticks(rotation=45, ha="right", fontsize=8)
    plt.yticks(rotation=0, fontsize=8)
    plt.tight_layout()

    save_path = os.path.join(OUTPUT_DIR, "confusion_matrix.png")
    plt.savefig(save_path, dpi=150, bbox_inches="tight")
    print(f"\n📊 Confusion matrix saved to: {save_path}")
    plt.show()


def plot_per_class_accuracy(y_true, y_pred, class_names: list):
    cm = confusion_matrix(y_true, y_pred)
    per_class_acc = cm.diagonal() / cm.sum(axis=1)
    short_names = [c.split("___")[-1].replace("_", " ")[:20] for c in class_names]

    fig, ax = plt.subplots(figsize=(16, 6))
    colors = ["#4CAF50" if acc >= 0.9 else "#FF9800" if acc >= 0.7 else "#F44336"
              for acc in per_class_acc]
    bars = ax.barh(short_names, per_class_acc * 100, color=colors, edgecolor="white", height=0.7)

    ax.set_xlabel("Accuracy (%)", fontsize=12)
    ax.set_title("Per-Class Accuracy", fontsize=14, fontweight="bold")
    ax.axvline(90, color="gray", linestyle="--", alpha=0.5, label="90% threshold")
    ax.set_xlim(0, 105)

    for bar, acc in zip(bars, per_class_acc):
        ax.text(bar.get_width() + 0.5, bar.get_y() + bar.get_height() / 2,
                f"{acc * 100:.1f}%", va="center", fontsize=8)

    ax.legend()
    plt.tight_layout()

    save_path = os.path.join(OUTPUT_DIR, "per_class_accuracy.png")
    plt.savefig(save_path, dpi=150, bbox_inches="tight")
    print(f"📊 Per-class accuracy chart saved to: {save_path}")
    plt.show()


def save_report(report: str, accuracy: float):
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    report_path = os.path.join(OUTPUT_DIR, "evaluation_report.txt")
    with open(report_path, "w") as f:
        f.write(f"Plant Disease Detection — Evaluation Report\n")
        f.write("=" * 60 + "\n\n")
        f.write(f"Overall Accuracy: {accuracy * 100:.2f}%\n\n")
        f.write("Classification Report:\n")
        f.write(report)
    print(f"📄 Report saved to: {report_path}")


def main(args):
    print("\n" + "🌿 " * 15)
    print("   PLANT DISEASE DETECTION — MODEL EVALUATION")
    print("🌿 " * 15 + "\n")

    model_path = args.model or (
        TRAINED_MODEL_PATH if os.path.exists(TRAINED_MODEL_PATH) else DEMO_MODEL_PATH
    )
    dataset_dir = args.dataset or DATASET_DIR

    if not os.path.exists(dataset_dir):
        print(f"❌ Dataset not found at: {dataset_dir}")
        print("   Run: python download_dataset.py")
        return

    model = load_model(model_path)
    test_gen = build_test_generator(dataset_dir)
    y_true, y_pred, class_names, report = evaluate_model(model, test_gen)
    acc = accuracy_score(y_true, y_pred)

    plot_confusion_matrix(y_true, y_pred, class_names)
    plot_per_class_accuracy(y_true, y_pred, class_names)
    save_report(report, acc)

    print("\n🎉 Evaluation complete! Check the 'outputs/' directory for plots.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Evaluate Plant Disease Detection Model")
    parser.add_argument("--model", type=str, default=None, help="Path to model file")
    parser.add_argument("--dataset", type=str, default=None, help="Path to dataset directory")
    args = parser.parse_args()
    main(args)
