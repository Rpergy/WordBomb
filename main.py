from time import sleep
import pyautogui
from pynput.keyboard import Key, Controller
import cv2
import pytesseract

from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
keyboard = Controller()
foundWord = 0
usedWords = []

def checkforturn():
    textboxScreenshot = pyautogui.screenshot(region=(535,994,100,100)) # Here is where the coordinates for the textbox should go (replace the first two numbers)
    textboxScreenshot.save(r'images/turn.png')
    textBoxImg = Image.open('images/turn.png') 
    pix = textBoxImg.load() 
    if pix[0,0] == (24, 20, 18): #Replace this tuple with the result from testColor.py
        return True
    else:
        return False

def captureSymbol():
    symbolScreenshot = pyautogui.screenshot(region=(775,540,70,30)) # Here is where the coordinates for the symbol should go (replace the first two numbers)
    symbolScreenshot.save(r'images/symbol.png')
    symbolImage = cv2.imread('images/symbol.png')
    symbolText = pytesseract.image_to_string(symbolImage, config='--psm 7', lang='eng')
    symbolText.replace('0', 'o')
    symbolText.replace('1', 'i')
    symbolText.replace('\n', '')
    return symbolText.lower()


wordsFile = open('words.txt', 'r')
wordsFileList = wordsFile.readlines()
while True:
    if checkforturn():
        symbol = captureSymbol().replace('\n', '')
        print(symbol)

        for i in range(56390):
            currentWord = wordsFileList[i].replace('\n', '')
            if usedWords.count(currentWord) == 0:
                if foundWord == 1:
                    foundWord = 0;
                    break
                
                if symbol in currentWord:
                    print("Found Word:", currentWord)
                    pyautogui.write(currentWord, interval=0.01)
                    keyboard.press(Key.enter)
                    usedWords.append(currentWord)
                    foundWord = 1
                    break
    sleep(1)
