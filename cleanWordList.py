from hashlib import new


oldList = open("words.txt", "r")
newList = open("shortWords.txt", "w")

old = oldList.readlines()

for i in range(58109):
    if len(old[i]) < 14:
        newList.write(old[i])

oldList.close()
newList.close()
