import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = '/usr/local/bin/tesseract'

def extract_text(plate_image):
    gray = cv2.cvtColor(plate_image, cv2.COLOR_BGR2GRAY)
    _, binary = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)
    text = pytesseract.image_to_string(binary, config='--psm 8')
    return text.strip()
