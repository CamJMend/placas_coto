import cv2
from detect import load_yolo, detect_plates
from ocr import extract_text
from database import save_plate

def main():
    net = load_yolo()  # Cargar modelo YOLO
    cap = cv2.VideoCapture(0)  # Capturar video

    if not cap.isOpened():
        print("Error al abrir la cámara.")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        plate_roi = detect_plates(frame, net)
        if plate_roi is not None:
            plate_text = extract_text(plate_roi)
            if plate_text:
                print(f"Placa detectada: {plate_text}")
                save_plate(plate_text)  # Guardar en la base de datos

        cv2.imshow("Det de Placas", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):  # Presiona 'q' para salir
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
