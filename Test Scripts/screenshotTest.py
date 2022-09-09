# This was a test to see if the OCR was working correctly
# Most of the time, it did not 
# You can use this script if something (with the OCR) is not working correctly
# Keep in mind, Pytesseract is just really bad and theres not much you can do about that

import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

symbolImage = cv2.imread('../images/symbol.png')
symbolText = pytesseract.image_to_string(symbolImage, config='--psm 7', lang='eng')
symbol = [*symbolText.lower()]
symbol.remove('\n')
print(symbol)
