# Alright so i really hate that I had to make this script because technically the color should be the same every time
# But for some reason, while switching between my laptop and PC, the resulting color from the screenshots was different

# First, get a screenshot that has the color of the textbox
# Then all you need to do is run this program (make sure to change line 9 to the correct image name) 
# Take the resulting tuple from the output and put it in main.py, around line 19 (youll see a comment)

from PIL import Image

textBoxImg = Image.open('../images/turn.png') 
pix = textBoxImg.load()

print(pix[0,0])
