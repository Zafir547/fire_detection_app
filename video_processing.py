import cv2
from ultralytics import YOLO

# Load the trained YOLOv8 model
model = YOLO(" models directory path models.pt")

def process_video(video_path):
    """Process video and detect fire events."""
    cap = cv2.VideoCapture(video_path)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Perform detection
        results = model(frame)

        # Annotate frame with detections
        for box in results[0].boxes.xyxy:
            x1, y1, x2, y2 = map(int, box)
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

        # cv2.putText(frame, "Fire", (x1, y1 - 10), cv
        cv2.imshow('Fire Detection', frame)
    
        # Stop with ESC key
        if cv2.waitKey(1) & 0xFF == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

      