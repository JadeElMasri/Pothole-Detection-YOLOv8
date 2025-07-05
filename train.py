from ultralytics import YOLO

model = YOLO("yolov8n.pt")
model.train(data="/home/jade/Desktop/pothole_detection/Pothole.v1-raw.yolov8/data.yaml", epochs=50, imgsz=640)
