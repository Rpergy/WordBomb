# WordBomb
Pytesseract is bad

Note: Coordinates will probably not work on your computer, as they change based on display resolution

  You can fix this by screenshotting the Bomb Party screen, and opening the screenshot in mspaint.
  
  from there, choose the select tool and in the bottom left you should see the location of your cursor
  
  use those coordinates on the line that has the "Replace Coords Here" comment, and it should work
  
  <bold>MAKE SURE TO DO THIS FOR BOTH THE SYMBOL DETECTION AND THE TEXTBOX DETECTION</bold>
  
  
  Here is an example of what the box for the symbol should look like
  
  ![An example of the proper symbol screenshot](images/readme_symbol.png)

if the program isn't recognizing the input box, visit "testColor.py" and read the instructions on there.


Hopefully i can make this project better by implementing a better OCR (i hate you pytesseract) and writing some sort of algorithm that will favor words with characters that havent been used yet. 

this way, i can maximize how many lives im earning by focusing on using the most individual letters i can
