import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = '/usr/local/bin/tesseract'

def extract_text(plate_image):
    image = imutils.resize(plate_image, width=1000)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Gray", gray)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    cv2.imshow("Blurred", blurred)
    binary = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
    cv2.imshow("Binary", binary)
    text = pytesseract.image_to_string(binary, config=f'--psm 8 --oem 3 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
    print(text)
    return text.strip()
