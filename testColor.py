from PIL import Image

textBoxImg = Image.open('images/turn.png') 
pix = textBoxImg.load()

print(pix[0,0])
