# 🌿 Plant Disease Detection using Machine Learning

> An end-to-end AI system that detects plant diseases from leaf images using deep learning (MobileNetV2 Transfer Learning), with a Flask web application for deployment.

---

## 📋 Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Quick Start](#quick-start)
- [Dataset Setup](#dataset-setup)
- [Training the Model](#training-the-model)
- [Running the Web App](#running-the-web-app)
- [CLI Prediction Tool](#cli-prediction-tool)
- [Model Evaluation](#model-evaluation)
- [Technologies Used](#technologies-used)
- [Supported Crops & Diseases](#supported-crops--diseases)

---

## 🎯 Overview

This project implements a **Plant Disease Detection** system using:
- **MobileNetV2** Transfer Learning (pretrained on ImageNet)
- **PlantVillage Dataset** (38 disease classes, 54,000+ leaf images)
- **Flask Web Application** with premium UI for real-time predictions
- Full ML pipeline: data augmentation → training → evaluation → deployment

---

## ✨ Features

| Feature | Details |
|---------|---------|
| 🧠 Model | MobileNetV2 Transfer Learning |
| 🌿 Classes | 38 (14 crops × healthy + diseased) |
| 📊 Dataset | PlantVillage (54K+ images) |
| 🎯 Input | 224 × 224 RGB leaf images |
| 🌐 Deployment | Flask Web App |
| 💊 Output | Disease name + confidence + treatment |
| 📱 API | REST JSON endpoint (`/api/predict`) |

---

## 📁 Project Structure

```
Plant Disease Detection/
│
├── 📂 dataset/
│   └── PlantVillage/          # Downloaded dataset (38 class folders)
│
├── 📂 models/
│   ├── plant_disease_model.keras  # Trained model (after training)
│   ├── demo_model.keras           # Demo model (generated immediately)
│   └── class_indices.json         # Class name → index mapping
│
├── 📂 static/
│   ├── css/style.css          # Premium dark-green UI
│   ├── js/main.js             # Drag-and-drop, animations
│   └── uploads/               # Temporary uploaded images
│
├── 📂 templates/
│   ├── index.html             # Upload page
│   └── result.html            # Prediction results page
│
├── 📂 outputs/                # Evaluation plots & reports
│   ├── confusion_matrix.png
│   ├── per_class_accuracy.png
│   ├── training_history.png
│   └── evaluation_report.txt
│
├── 📂 notebooks/              # Google Colab training notebook
│
├── app.py                     # Flask web application
├── train.py                   # Model training script
├── evaluate.py                # Evaluation + confusion matrix
├── predict.py                 # CLI prediction tool
├── create_demo_model.py       # Generate demo model instantly
├── download_dataset.py        # Kaggle dataset downloader
├── config.py                  # Project configuration
├── disease_info.py            # Disease descriptions + treatments
├── setup.py                   # Environment setup checker
├── requirements.txt           # Python dependencies
└── README.md
```

---

## 🚀 Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Verify Setup

```bash
python setup.py
```

### 3. Create Demo Model (No Dataset Needed)

```bash
python create_demo_model.py
```

### 4. Start the Web App

```bash
python app.py
```

Open your browser at **http://localhost:5000** 🎉

---

## 📥 Dataset Setup

### Option A: Download from Kaggle (Recommended)

1. Create a Kaggle account at [kaggle.com](https://www.kaggle.com)
2. Go to **Account → Create New API Token** — this downloads `kaggle.json`
3. Place `kaggle.json` in `C:\Users\<YourName>\.kaggle\` (Windows)
4. Run:

```bash
python download_dataset.py
```

For a smaller **demo subset** (10 classes, faster download):
```bash
python download_dataset.py --subset
```

### Option B: Manual Download

1. Go to [PlantVillage on Kaggle](https://www.kaggle.com/datasets/emmarex/plantdisease)
2. Download and extract into `dataset/PlantVillage/`

### Expected Structure After Download
```
dataset/PlantVillage/
├── Apple___Apple_scab/
├── Apple___Black_rot/
├── Apple___healthy/
├── Tomato___Early_blight/
├── Tomato___healthy/
└── ... (38 folders total)
```

---

## 🏋️ Training the Model

### Local Training (GPU Recommended)

```bash
python train.py
```

**With options:**
```bash
python train.py --epochs 30 --batch_size 32 --dataset dataset/PlantVillage
python train.py --no_fine_tune   # Skip Phase 2 fine-tuning
```

### Google Colab (Free GPU)

1. Upload the project to Google Drive
2. Open a new Colab notebook
3. Mount Drive:
```python
from google.colab import drive
drive.mount('/content/drive')
```
4. Install and run:
```python
!pip install tensorflow keras pillow
!python train.py --dataset /content/drive/MyDrive/PlantDisease/dataset/PlantVillage
```
5. Download the trained `.keras` model to `models/` folder

### Training Pipeline

| Phase | Description | Duration |
|-------|-------------|----------|
| Phase 1 | Train classification head (base frozen) | ~30 min (GPU) |
| Phase 2 | Fine-tune top layers of MobileNetV2 | ~20 min (GPU) |

---

## 🌐 Running the Web App

```bash
python app.py
```

- **Home**: http://localhost:5000 — Upload a leaf image
- **API**: http://localhost:5000/api/predict — JSON REST endpoint
- **Health**: http://localhost:5000/health — Service status check

### API Usage

```bash
curl -X POST http://localhost:5000/api/predict \
  -F "file=@path/to/leaf.jpg"
```

**Response:**
```json
{
  "top_prediction": {
    "class_name": "Tomato___Early_blight",
    "disease": "Early Blight",
    "plant": "Tomato",
    "confidence": 94.72,
    "healthy": false,
    "severity": "Moderate",
    "treatment": ["Apply chlorothalonil fungicide", "..."],
    "symptoms": ["Dark brown lesions with rings", "..."]
  },
  "alternatives": [...],
  "model_type": "Trained Model"
}
```

---

## 🔍 CLI Prediction Tool

```bash
# Predict a single image (top-3 results)
python predict.py --image path/to/leaf.jpg

# Show top-5 predictions
python predict.py --image leaf.jpg --top_k 5

# Use a specific model
python predict.py --image leaf.jpg --model models/plant_disease_model.keras
```

---

## 📊 Model Evaluation

After training, evaluate performance:

```bash
python evaluate.py
```

**Outputs in `outputs/`:**
- `confusion_matrix.png` — Normalized confusion matrix heatmap
- `per_class_accuracy.png` — Per-class accuracy bar chart
- `training_history.png` — Training/validation accuracy & loss curves
- `evaluation_report.txt` — Precision, Recall, F1 per class

---

## 🛠️ Technologies Used

| Component | Technology |
|-----------|-----------|
| Programming | Python 3.8+ |
| Deep Learning | TensorFlow 2.x / Keras |
| Model | MobileNetV2 (Transfer Learning) |
| Image Processing | Pillow, OpenCV |
| Data Processing | NumPy, Pandas |
| Visualization | Matplotlib, Seaborn |
| Web Framework | Flask |
| Frontend | HTML5, CSS3, Vanilla JavaScript |
| Dataset | PlantVillage (Kaggle) |

---

## 🌿 Supported Crops & Diseases

| Crop | Conditions |
|------|-----------|
| 🍎 Apple | Apple Scab, Black Rot, Cedar Apple Rust, Healthy |
| 🫐 Blueberry | Healthy |
| 🍒 Cherry | Powdery Mildew, Healthy |
| 🌽 Corn | Gray Leaf Spot, Common Rust, Northern Leaf Blight, Healthy |
| 🍇 Grape | Black Rot, Esca, Leaf Blight, Healthy |
| 🍊 Orange | Citrus Greening (HLB) |
| 🍑 Peach | Bacterial Spot, Healthy |
| 🫑 Bell Pepper | Bacterial Spot, Healthy |
| 🥔 Potato | Early Blight, Late Blight, Healthy |
| 🫐 Raspberry | Healthy |
| 🫘 Soybean | Healthy |
| 🎃 Squash | Powdery Mildew |
| 🍓 Strawberry | Leaf Scorch, Healthy |
| 🍅 Tomato | 9 conditions including Bacterial Spot, Early/Late Blight, TYLCV, Mosaic Virus |

---

## 🔮 Future Enhancements

- [ ] Live camera feed disease detection
- [ ] Disease severity estimation (mild/moderate/severe)
- [ ] Multi-language support for farmers
- [ ] Prediction history with database storage
- [ ] GPS-based disease outbreak mapping
- [ ] TensorFlow Lite conversion for mobile apps
- [ ] Disease spread heatmaps for field monitoring

---

## 📖 Skills Demonstrated

- ✅ Computer Vision & Image Processing
- ✅ Convolutional Neural Networks (CNNs)
- ✅ Transfer Learning (MobileNetV2)
- ✅ Data Augmentation
- ✅ Model Evaluation (Confusion Matrix, F1, Recall)
- ✅ Web Application Development (Flask)
- ✅ REST API Design
- ✅ Full End-to-End ML Pipeline

---

> 🌿 **PlantGuard AI** — Built with ❤️ for smarter agriculture
