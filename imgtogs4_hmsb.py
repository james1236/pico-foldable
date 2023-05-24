import cv2 
import numpy as np

img = cv2.imread('starsbg.png', 0) #grayscale

hex = ["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"]
outputString = ""
even = True

cv2.imshow('image', img)
for y in range(0, 128):
    for x in range(0, 128):
        if (even):
            outputString += "\\x"
        even = not even
    
        col = round((img[y, x] / 256) * 16)
        outputString = outputString + hex[col]

print(outputString)