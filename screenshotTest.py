import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

symbolImage = cv2.imread('images/symbol.png')
symbolText = pytesseract.image_to_string(symbolImage, config='--psm 7', lang='eng')
symbol = [*symbolText.lower()]
symbol.remove('\n')
print(symbol)
