from ultralytics import YOLO
import cv2

def load_yolo():
    model = YOLO("yolov5s.pt")
    return model

def detect_plates(frame, model):
    results = model(frame)  # Ejecutar detección

    for result in results:
        for box in result.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])  # Obtener coordenadas de la caja
            confidence = box.conf[0].item()

            if confidence > 0.5:
                plate_roi = frame[y1:y2, x1:x2]  # Recortar la placa detectada
                return plate_roi

    return None
