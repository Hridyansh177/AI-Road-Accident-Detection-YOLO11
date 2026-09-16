# 🚨 AI Road Accident Detection — YOLO11

A computer vision model for detecting road accidents in images and videos using YOLO11s.

## 🧠 Model

- Architecture: YOLO11s
- Task: Object Detection
- Class: Accident

The trained model is located at:

`models/accident_detector_V1_best.pt`

## 📊 Dataset

The dataset contains approximately 9,000 road accident images.

| Split | Images |
|---|---:|
| Train | 6,308 |
| Validation | 1,801 |
| Test | 893 |

The dataset uses YOLO-format bounding-box annotations.

## 📈 Test Results

The model was evaluated on 893 held-out test images containing 991 ground-truth objects.

| Metric | Result |
|---|---:|
| Precision | 90.9% |
| Recall | 88.4% |
| mAP@0.5 | 94.7% |
| mAP@0.5:0.95 | 71.6% |

## ⚙️ Installation

Clone the repository:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd Accident_Detector_V1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## 🚀 Image Detection

```bash
python predict.py --source image.jpg
```

You can change the confidence threshold:

```bash
python predict.py --source image.jpg --conf 0.60
```

Results are saved under:

`runs/detect/prediction/`

## 🎥 Video Detection

```bash
python predict.py --source video.mp4
```

## 📁 Project Structure

```text
Accident_Detector_V1/
├── models/
│   └── accident_detector_V1_best.pt
├── predict.py
├── requirements.txt
└── README.md
```

## 🔔 Persistent Accident Detection

The detector can be combined with temporal logic so that an accident must be detected across multiple consecutive frames before an alert is triggered.

This can help reduce alerts caused by isolated false detections.

## ⚠️ Limitations

This project is a computer-vision prototype and should not be considered a production-grade emergency-response system.

Performance may vary depending on:
- Camera viewpoint
- Lighting conditions
- Weather
- Image quality
- Distance from the accident
- Occlusion
- Unusual accident scenarios
- Differences between training data and real-world environments

The reported metrics are based on the project's held-out test set.

## 🔬 Future Improvements

- Add more diverse accident scenes
- Increase small and distant accident examples
- Add night, rain and fog scenarios
- Add motorcycle and multi-vehicle accidents
- Add hard-negative normal traffic images
- Improve temporal accident confirmation
- Test on larger real-world video datasets
- Deploy through a web or edge application

## 🛠️ Technologies

- Python
- YOLO11
- Ultralytics
- OpenCV
- Computer Vision
- Object Detection

## 📜 License

Add an appropriate license after verifying that the dataset and trained weights can be redistributed under that license.

## 👨‍💻 Project

**AI Road Accident Detection using YOLO11**
