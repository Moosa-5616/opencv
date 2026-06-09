from ultralytics import YOLO
import cv2

# Load YOLOv8 nano model (lightweight & fast)
model = YOLO("yolov8n.pt")

# Open webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Run YOLO on the frame
    results = model(frame)

    # Draw results (bounding boxes, labels)
    annotated_frame = results[0].plot()

    # Show output
    cv2.imshow("YOLOv8 Live", annotated_frame)

    # Press ESC to exit
    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()