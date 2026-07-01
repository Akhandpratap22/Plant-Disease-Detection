"""
download_dataset.py — Download PlantVillage Dataset from Kaggle

Requirements:
    pip install kaggle
    Set up Kaggle API credentials:
        1. Go to https://www.kaggle.com/account
        2. Click "Create New API Token"
        3. Place kaggle.json in ~/.kaggle/ (Linux/Mac) or C:\\Users\\<USER>\\.kaggle\\ (Windows)

Usage:
    python download_dataset.py
    python download_dataset.py --subset  (downloads only 10 classes for demo)
"""

import os
import sys
import shutil
import argparse
import zipfile

from config import DATASET_DIR, BASE_DIR

KAGGLE_DATASET = "emmarex/plantdisease"
DOWNLOAD_DIR = os.path.join(BASE_DIR, "dataset")

# Subset of 10 classes for quick demo
DEMO_CLASSES = [
    "Tomato___healthy",
    "Tomato___Early_blight",
    "Tomato___Late_blight",
    "Potato___healthy",
    "Potato___Early_blight",
    "Potato___Late_blight",
    "Apple___healthy",
    "Apple___Black_rot",
    "Corn_(maize)___healthy",
    "Corn_(maize)___Common_rust_",
]


def check_kaggle():
    """Check if Kaggle is installed and configured."""
    try:
        import kaggle  # noqa
        print("✅ Kaggle API is installed.")
    except ImportError:
        print("❌ Kaggle package not found. Install it with:")
        print("   pip install kaggle")
        sys.exit(1)

    kaggle_json_windows = os.path.expanduser("~\\.kaggle\\kaggle.json")
    kaggle_json_unix = os.path.expanduser("~/.kaggle/kaggle.json")
    if not (os.path.exists(kaggle_json_windows) or os.path.exists(kaggle_json_unix)):
        print("❌ Kaggle credentials not found.")
        print("   1. Go to: https://www.kaggle.com/account")
        print("   2. Click 'Create New API Token'")
        print("   3. Place kaggle.json in:")
        print(f"      Windows: {kaggle_json_windows}")
        sys.exit(1)
    print("✅ Kaggle credentials found.")


def download_full_dataset():
    """Download the full PlantVillage dataset from Kaggle."""
    import kaggle

    print(f"\n📥 Downloading dataset: {KAGGLE_DATASET}")
    print(f"   Destination: {DOWNLOAD_DIR}")
    print("   This may take a few minutes (~1.5 GB)...\n")

    os.makedirs(DOWNLOAD_DIR, exist_ok=True)
    kaggle.api.dataset_download_files(
        KAGGLE_DATASET,
        path=DOWNLOAD_DIR,
        unzip=True,
        quiet=False,
    )
    print("\n✅ Dataset downloaded and extracted!")


def filter_subset(subset_classes: list):
    """Keep only the specified subset of classes."""
    pv_dir = os.path.join(DOWNLOAD_DIR, "PlantVillage")
    if not os.path.exists(pv_dir):
        # Try to find the extracted folder
        for item in os.listdir(DOWNLOAD_DIR):
            if os.path.isdir(os.path.join(DOWNLOAD_DIR, item)):
                pv_dir = os.path.join(DOWNLOAD_DIR, item)
                break

    print(f"\n🔍 Filtering dataset to {len(subset_classes)} classes...")
    all_classes = [d for d in os.listdir(pv_dir) if os.path.isdir(os.path.join(pv_dir, d))]

    removed = 0
    for cls in all_classes:
        # Check if this class is in our subset
        keep = any(subset_cls.lower() in cls.lower() for subset_cls in subset_classes)
        if not keep:
            shutil.rmtree(os.path.join(pv_dir, cls))
            removed += 1

    print(f"   Removed {removed} classes. Kept: {len(subset_classes)} classes.")


def count_images(dataset_dir: str):
    """Count total images in the dataset."""
    total = 0
    if not os.path.exists(dataset_dir):
        return 0
    for root, _, files in os.walk(dataset_dir):
        total += sum(1 for f in files if f.lower().endswith((".jpg", ".jpeg", ".png")))
    return total


def main(args):
    print("\n🌿  PlantVillage Dataset Downloader")
    print("─" * 40)

    check_kaggle()
    download_full_dataset()

    if args.subset:
        filter_subset(DEMO_CLASSES)
        print(f"✅ Subset with {len(DEMO_CLASSES)} classes ready.")

    # Find and print dataset stats
    pv_dir = os.path.join(DOWNLOAD_DIR, "PlantVillage")
    if os.path.exists(pv_dir):
        n_classes = len([d for d in os.listdir(pv_dir) if os.path.isdir(os.path.join(pv_dir, d))])
        n_images = count_images(pv_dir)
        print(f"\n📊 Dataset Summary:")
        print(f"   Classes : {n_classes}")
        print(f"   Images  : {n_images:,}")
        print(f"   Path    : {pv_dir}")

    print("\n📌 Next Steps:")
    print("   1. Train the model : python train.py")
    print("   2. Or run web app  : python app.py  (uses demo model)")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Download PlantVillage Dataset")
    parser.add_argument(
        "--subset",
        action="store_true",
        default=False,
        help=f"Download only {len(DEMO_CLASSES)} demo classes instead of all 38",
    )
    args = parser.parse_args()
    main(args)
