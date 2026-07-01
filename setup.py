"""
setup.py — Project Environment Setup & Verification

Verifies Python version, creates necessary directories,
checks GPU availability, and prints next steps.

Usage:
    python setup.py
"""

import os
import sys
import platform
import subprocess

# ─────────────────────────────────────────────────────────────────────────────
# Color helpers (ANSI — works in most modern terminals)
# ─────────────────────────────────────────────────────────────────────────────

def green(text):  return f"\033[92m{text}\033[0m"
def yellow(text): return f"\033[93m{text}\033[0m"
def red(text):    return f"\033[91m{text}\033[0m"
def bold(text):   return f"\033[1m{text}\033[0m"
def cyan(text):   return f"\033[96m{text}\033[0m"


def banner():
    print(cyan("""
  ╔══════════════════════════════════════════════════╗
  ║   🌿  PLANT DISEASE DETECTION — SETUP CHECKER   ║
  ╚══════════════════════════════════════════════════╝
"""))


def check_python():
    """Check Python version (3.8+ required)."""
    v = sys.version_info
    version_str = f"{v.major}.{v.minor}.{v.micro}"
    if v.major == 3 and v.minor >= 8:
        print(green(f"  ✅ Python {version_str} — OK (3.8+ required)"))
        return True
    else:
        print(red(f"  ❌ Python {version_str} — Requires Python 3.8+"))
        return False


def check_package(package_name, import_name=None):
    """Check if a Python package is installed."""
    import_name = import_name or package_name
    try:
        mod = __import__(import_name)
        version = getattr(mod, "__version__", "unknown")
        print(green(f"  ✅ {package_name:<20} v{version}"))
        return True
    except ImportError:
        print(red(f"  ❌ {package_name:<20} NOT INSTALLED"))
        return False


def check_gpu():
    """Check GPU availability via TensorFlow."""
    try:
        import tensorflow as tf
        gpus = tf.config.list_physical_devices("GPU")
        if gpus:
            print(green(f"  ✅ GPU Available        {[g.name for g in gpus]}"))
            return True
        else:
            print(yellow("  ⚠️  No GPU detected      Training will be slow on CPU"))
            print(yellow("     Consider Google Colab for GPU-accelerated training"))
            return False
    except Exception:
        print(red("  ❌ Could not check GPU  TensorFlow may not be installed"))
        return False


def create_directories():
    """Create all required project directories."""
    dirs = [
        "dataset/PlantVillage",
        "models",
        "outputs",
        "static/uploads",
        "static/css",
        "static/js",
        "templates",
        "notebooks",
    ]
    for d in dirs:
        os.makedirs(d, exist_ok=True)
    print(green(f"  ✅ All directories created ({len(dirs)} folders)"))


def check_dataset():
    """Check if dataset exists."""
    dataset_path = "dataset/PlantVillage"
    if os.path.exists(dataset_path):
        classes = [d for d in os.listdir(dataset_path)
                   if os.path.isdir(os.path.join(dataset_path, d))]
        if classes:
            print(green(f"  ✅ Dataset found        {len(classes)} classes in '{dataset_path}'"))
            return True
    print(yellow(f"  ⚠️  Dataset not found   Run: python download_dataset.py"))
    return False


def check_model():
    """Check if a trained or demo model exists."""
    if os.path.exists("models/plant_disease_model.keras"):
        print(green("  ✅ Trained model found  models/plant_disease_model.keras"))
        return "trained"
    elif os.path.exists("models/demo_model.keras"):
        print(yellow("  ⚠️  Demo model found     Run: python train.py for full accuracy"))
        return "demo"
    else:
        print(red("  ❌ No model found       Run: python create_demo_model.py"))
        return None


# ─────────────────────────────────────────────────────────────────────────────
# Main
# ─────────────────────────────────────────────────────────────────────────────

def main():
    banner()

    print(bold("📋 System Info"))
    print(f"     OS       : {platform.system()} {platform.release()}")
    print(f"     Python   : {sys.version.split()[0]}")
    print(f"     Platform : {platform.machine()}")
    print()

    print(bold("🐍 Python Version"))
    py_ok = check_python()
    print()

    print(bold("📦 Required Packages"))
    packages = [
        ("tensorflow",    "tensorflow"),
        ("flask",         "flask"),
        ("Pillow",        "PIL"),
        ("numpy",         "numpy"),
        ("pandas",        "pandas"),
        ("matplotlib",    "matplotlib"),
        ("seaborn",       "seaborn"),
        ("scikit-learn",  "sklearn"),
        ("opencv-python", "cv2"),
    ]
    missing = []
    for pkg_name, import_name in packages:
        if not check_package(pkg_name, import_name):
            missing.append(pkg_name)
    print()

    print(bold("🖥️  GPU Check"))
    check_gpu()
    print()

    print(bold("📁 Project Directories"))
    create_directories()
    print()

    print(bold("📂 Dataset Status"))
    check_dataset()
    print()

    print(bold("🧠 Model Status"))
    model_status = check_model()
    print()

    # ─── Summary ──────────────────────────────────────────────────────────────
    print("=" * 55)
    if missing:
        print(yellow(f"\n⚠️  Missing packages: {', '.join(missing)}"))
        print(yellow("   Install with:"))
        print(cyan("   pip install -r requirements.txt\n"))
    else:
        print(green("\n✅ All packages are installed!\n"))

    print(bold("📌 Next Steps:"))

    if missing:
        print(f"  1. {cyan('pip install -r requirements.txt')}")

    if model_status is None:
        print(f"  {'2' if missing else '1'}. {cyan('python create_demo_model.py')}  ← Quick demo model")

    if not check_dataset.__doc__:  # always show dataset step
        pass
    print(f"  {'3' if missing and model_status is None else '2' if missing or model_status is None else '1'}. {cyan('python download_dataset.py')}   ← Download PlantVillage dataset (Kaggle)")
    print(f"  {cyan('python train.py')}               ← Train full model (requires dataset)")
    print(f"  {cyan('python app.py')}                 ← Start web app")
    print(f"  {cyan('python predict.py --image leaf.jpg')} ← CLI prediction")
    print()
    print(green("  🌿 Happy farming! Open http://localhost:5000 after starting the app."))
    print("=" * 55 + "\n")


if __name__ == "__main__":
    main()
