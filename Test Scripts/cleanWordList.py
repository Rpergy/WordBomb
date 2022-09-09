# This file was used to "clean" a much larger list of words. 
# I mainly removed short words, as they would be pretty unimpressive if they were used in game. 

from hashlib import new


oldList = open("../words.txt", "r")
newList = open("shortWords.txt", "w")

old = oldList.readlines()

for i in range(58109):
    if len(old[i]) > 7:
        newList.write(old[i])

oldList.close()
newList.close()
