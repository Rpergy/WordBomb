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
    textboxScreenshot = pyautogui.screenshot(region=(306,1012,100,100))
    textboxScreenshot.save(r'images/turn.png')
    textBoxImg = Image.open('images/turn.png') 
    pix = textBoxImg.load() 
    if pix[0,0] == (21, 18, 16):
        return True
    else:
        return False

def captureSymbol():
    symbolScreenshot = pyautogui.screenshot(region=(700,600,70,30))
    symbolScreenshot.save(r'images/symbol.png')
    symbolImage = cv2.imread('images/symbol.png')
    symbolText = pytesseract.image_to_string(symbolImage, config='--psm 7', lang='eng')
    symbol = [*symbolText.lower()]
    symbol.remove('\n')
    for i in range(len(symbol)):
        if symbol[i] == '0':
            symbol[i] = 'o'
        elif symbol[i] == '1':
            symbol[i] = 'l'
    return symbol


wordsFile = open('shortWords.txt', 'r')
wordsFileList = wordsFile.readlines()
while True:
    if checkforturn():
        symbol = captureSymbol()
        print(symbol)

        for i in range(56390):
            currentWord = wordsFileList[i].replace('\n', '')
            if usedWords.count(currentWord) == 0:
                if foundWord == 1:
                    foundWord = 0;
                    break

                splitWord = [*currentWord.lower()]
                for c in range(len(currentWord)):
                    if c > len(currentWord) - len(symbol):
                        break

                    if splitWord[c] == symbol[0]:
                        if(splitWord[c + 1] == symbol[1]):
                            if len(symbol) == 2:
                                print("Found Word:", currentWord)
                                pyautogui.write(currentWord, interval=0.09)
                                keyboard.press(Key.enter)
                                usedWords.append(currentWord)
                                foundWord = 1
                                break
                            else:
                                if(splitWord[c + 2] == symbol[2]):
                                    print("Found Word:", currentWord)
                                    pyautogui.write(currentWord, interval=0.09)
                                    keyboard.press(Key.enter)
                                    usedWords.append(currentWord)
                                    foundWord = 1
                                    break
    sleep(1)
