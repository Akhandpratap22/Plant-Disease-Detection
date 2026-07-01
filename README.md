# 🌿 Plant Disease Detection using Deep Learning

> An AI-powered web application that detects plant diseases from leaf images using **TensorFlow**, **MobileNetV2**, **Computer Vision**, and **Flask**.

---

## 🚀 Overview

Plant diseases can significantly impact agricultural productivity. This project leverages Deep Learning and Transfer Learning to automatically identify diseases from images of plant leaves.

Users simply upload a leaf image, and the model predicts the disease along with its confidence score.

---

## ✨ Features

- 🌱 Detects healthy and diseased plant leaves
- 📷 Upload images through a web interface
- 🧠 Deep Learning model using MobileNetV2
- 📊 Displays prediction confidence
- ⚡ Fast inference
- 💻 Responsive Flask web application

---

## 🛠️ Tech Stack

| Category | Technology |
|----------|------------|
| Language | Python |
| Deep Learning | TensorFlow, Keras |
| Model | MobileNetV2 |
| Computer Vision | OpenCV |
| Backend | Flask |
| Frontend | HTML, CSS |
| Version Control | Git, GitHub |

---

## 📁 Project Structure

```
Plant-Disease-Detection/
│
├── app.py
├── train.py
├── requirements.txt
├── README.md
│
├── dataset/
├── models/
│   └── plant_disease_model.keras
│
├── outputs/
│   └── training_history.png
│
├── static/
│
├── templates/
│
└── screenshots/
```

---

## 📂 Dataset

**Dataset Used:** PlantVillage

The dataset contains thousands of labeled images of healthy and diseased plant leaves.

Supported crops include:

- Tomato
- Potato
- Apple
- Corn
- Grape
- Pepper

Total Classes: **38**

---

## 🧠 Model Architecture

```
Leaf Image
      │
      ▼
Image Preprocessing
      │
      ▼
MobileNetV2
(Transfer Learning)
      │
      ▼
Global Average Pooling
      │
      ▼
Dense Layer
      │
      ▼
Dropout
      │
      ▼
Softmax (38 Classes)
```

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/Akhandpratap22/Plant-Disease-Detection.git
```

Go to project folder

```bash
cd Plant-Disease-Detection
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
python app.py
```

Open

```
http://localhost:5000
```

---

## 🏋️ Training

Train the model using

```bash
python train.py
```

The trained model is saved inside

```
models/
```

Training graph

```
outputs/training_history.png
```

---

## 📈 Results

- Model: MobileNetV2
- Classes: 38
- Framework: TensorFlow
- Deployment: Flask
- Image Size: 224 × 224

The application predicts:

- Plant Name
- Disease Name
- Confidence Score

---

## 📸 Screenshots

### Home Page

Add image here

---

### Upload Image

Add image here

---

### Prediction Result

Add image here

---

### Training Accuracy Graph

Add image here

---

## 🔮 Future Improvements

- Mobile App
- TensorFlow Lite
- Live Camera Detection
- Disease Severity Detection
- Treatment Recommendation
- Multi-language Support
- Cloud Deployment
- Farmer Dashboard

---

## 💡 Applications

- Precision Agriculture
- Smart Farming
- Agriculture Research
- Greenhouse Monitoring

---

## 👨‍💻 Author

**Akhand Pratap Singh**

Machine Learning Student

GitHub:
https://github.com/Akhandpratap22

---

## ⭐ Support

If you found this project helpful, please give it a ⭐ on GitHub.
