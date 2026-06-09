from ultralytics import YOLO

model=YOLO("yolov8n.pt")
model("bus.jpg", save=True)