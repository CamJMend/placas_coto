import cv2
import time
from detect import load_yolo, detect_plates
from ocr import extract_text
from database import save_plate

def main():
    net = load_yolo()  # Cargar modelo YOLO
    cap = cv2.VideoCapture(0)  # Capturar video

    if not cap.isOpened():
        print("Error al abrir la cámara.")
        return

    last_processed_time = time.time()  # Tiempo de la última imagen procesada

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        current_time = time.time()

        # Procesar cada 10 segundos
        if current_time - last_processed_time >= 10:
            plate_roi = detect_plates(frame, net)
            if plate_roi is not None:
                plate_text = extract_text(plate_roi)
                if plate_text:
                    print(f"Placa detectada: {plate_text}")
                    cv2.imshow("Detección de Placas", frame)
                    #save_plate(plate_text)  # Guardar en la base de datos

            # Actualizar el tiempo de la última imagen procesada
            last_processed_time = current_time

        cv2.imshow("Detección de Placas", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):  # Presiona 'q' para salir
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

