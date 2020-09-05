import os
import time
import threading

#This is in seconds
amountOfTimeToWait = 10


#This part opens the file that is being read from.
#The file being read from should be filled with text before running.

try:
    readFile = open("ReadingFile.txt", 'r')
except:
    readFile = open("ReadingFile.txt", 'w')
    readFile.write("This file didn't exist, please replace this text and rerun the program\nSeparate the lines of text with a semicolon ';'.")
    readFile.close()
    exit()

#This separates the readFile into sentences/chunks whenever it encounters a semicolon (the semicolon can be replaced with any character(s)).
text = readFile.read().split(';')


#This keeps track of which sentence we're writing this time, so we start at 0
sentenceCounter = 0


#This gets called by itself after the amount of time set, on a loop
def updateText():   
    #Let this method know we need that variable between calls
    global sentenceCounter

    if sentenceCounter > (len(text) - 1):
        sentenceCounter = 0

    #open the write file, this will create it if it doesn't exist
    writeFile = open("WritingFile.txt", 'w')  
    print(text[sentenceCounter].strip())
    #Write the next line out, overwriting what's already there
    writeFile.write(text[sentenceCounter].strip())

    #this closes the file so it updates
    writeFile.close()

    #Increment the counter so next time we write a new sentence
    sentenceCounter += 1

    #Wait a certain amount of time and then call this again
    time.sleep(amountOfTimeToWait)
    updateText()

#Actually run the program
updateText()


