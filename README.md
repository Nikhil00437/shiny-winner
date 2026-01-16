# Emotion Detection System 😐🙂😠

Let’s be honest: this is not magic, it’s just computer vision + a pre-trained model doing its job. Still, it works — and that’s already better than half the GitHub repos out there.

---

## 📌 Project Overview

This project is a **real-time facial emotion detection system** built using **Python**, **OpenCV**, and **DeepFace**. It captures live video from a webcam, detects faces, and predicts the dominant emotion for each detected face.

Emotions detected typically include:

* Happy
* Sad
* Angry
* Neutral
* Fear
* Surprise
* Disgust

No, it doesn’t read minds. It reads pixels.

---

## 🛠️ Tech Stack

* **Python 3.8+** (older versions? Don’t bother.)
* **OpenCV** – Face detection & video capture
* **DeepFace** – Emotion analysis (pre-trained deep learning models)
* **NumPy** – Because everything needs NumPy

---

## ⚙️ How It Works (Simplified)

1. Webcam captures frames in real time.
2. OpenCV detects faces using Haar Cascades.
3. Each face region is passed to DeepFace.
4. DeepFace predicts the dominant emotion.
5. Emotion label is rendered on the video stream.

That’s it. No blockchain. No overengineering.

---

## 📂 Project Structure

```
Emotion-Detection/
│
├── emotionsdetector.ipynb   # Main notebook
├── haarcascade_frontalface_default.xml
├── README.md
```

If your folder looks messier than this, that’s on you.

---

## 🚀 Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/emotion-detection.git
cd emotion-detection
```

### 2️⃣ Install Dependencies

```bash
pip install opencv-python deepface numpy
```

If this fails, update `pip` instead of crying.

---

## ▶️ Running the Project

### Option 1: Jupyter Notebook

```bash
jupyter notebook emotionsdetector.ipynb
```

Run all cells and make sure your webcam isn’t being used by 10 other apps.

### Option 2: Convert to Script (Recommended if you’re serious)

```bash
jupyter nbconvert --to script emotionsdetector.ipynb
python emotionsdetector.py
```

---

## 📸 Sample Output

* Face detected → bounding box drawn
* Emotion displayed above the face in real time

If lighting is bad or your face is half-visible, don’t blame the model — blame physics.

---

## ⚠️ Limitations (Read This Before Flexing)

* Accuracy drops with poor lighting
* Multiple faces = slower performance
* Emotion prediction is probabilistic, not absolute truth
* Webcam-only (no video file input yet)

Yes, improvements are possible. No, they won’t happen automatically.

---

## 🔧 Possible Improvements

* Switch from Haar Cascade to **DNN-based face detection**
* Add **video file input support**
* Optimize FPS using threading
* Deploy as a **FastAPI / Flask web app**
* Convert into an **Android app** (camera + on-device inference)

---

## 🧠 Use Cases

* Human-computer interaction
* Behavioral analysis (basic level)
* AI demos & college projects
* Interview flex (just don’t oversell it)

---

## 📜 License

This project is for **educational and experimental purposes**.
Use it responsibly — especially if humans are involved.

