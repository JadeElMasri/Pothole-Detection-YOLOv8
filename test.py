from ultralytics import YOLO
import os

model = YOLO(os.path.expanduser("~/Desktop/pothole_detection/runs/detect/train/weights/best.pt"))

results = model.predict(os.path.expanduser("~/Desktop/pothole_detection/Pothole.v1-raw.yolov8/test/images"),save=True,conf=0.5)





