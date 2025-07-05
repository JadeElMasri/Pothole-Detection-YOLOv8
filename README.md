# Pothole Detection Using YOLOv8


This repository represents a trained YOLOv8 object detection model on an Ubuntu 22 Core i9 PC

The model uses **Ultralytics YOLOv8**

![Ultralytics](ultralytics_yolo.png)




and was trained entirely on the CPU using **YOLOV8n**, for **50 epochs** and a custom dataset from [Roboflow](https://public.roboflow.com/object-detection/pothole) + manually added background-only samples.   

The outcome of this project could be useful in a diversity of research or engineering fields such as **Autonomous Vehicles**, **Smart City Initiatives**, **Traffic Monitoring** etc...





**Results**


### Confusion Matrix

![Confusion Matrix](runs/detect/train2/confusion_matrix_normalized.png)




The model correctly predicted **77%** of the potholes while **23%** were predicted as background. 

In addition to that, All background-only images were misclassified as potholes, highlighting the model's bias due to limited clean road data.




**Limitations**:
  The trained dataset had numerous pothole images with very limited clean road images. This explains the wrong predictions of the model.


**Future Work**:
  - Add more clean road images to improve the model's robustness and predictions.
  - Retrain the model and assess performance


    


  
  
