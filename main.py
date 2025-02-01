import cv2
import time
from detect import load_yolo, detect_plates
from ocr import extract_text
from database import check_plate, register_visit
#from whatsapp import send_whatsapp_message

def main():
    net = load_yolo()
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error al abrir la cámara.")
        return

    last_processed_time = time.time()
    detected_plates = []

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        current_time = time.time()

        if current_time - last_processed_time >= 10:
            plate_roi = detect_plates(frame, net)
            if plate_roi is not None:
                plate_text = extract_text(plate_roi)
                if plate_text:
                    detected_plates.append(plate_text)
                    
                    if detected_plates.count(plate_text) >= 3:
                        owner_info = check_plate(plate_text)
                        if owner_info:
                            print(f"Acceso permitido para {owner_info['name']}")
                        else:
                            print("Placa no reconocida, solicitando autorización.")
                            register_visit(plate_text)
                    
                    cv2.imshow("Detección de Placas", frame)

            last_processed_time = current_time

        cv2.imshow("Detección de Placas", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()