# Importing Image class from PIL module
import numpy as np
import cv2
# Opens a image in RGB mode
#im = Image.open(r"C:\Users\Admin\Pictures\geeks.png")
img = cv2.imread("image/SingleCoinTest.png", 0)
width = int(img.shape[1])
height = int(img.shape[0])
w1 = int(width*.30)
w2 = int(width*.68)
h1 = int(height*.83)
h2 = int(height*.96)

w3 = int(width*.80)
w4 = int(width*.90)
h3 = int(height*.65)
h4 = int(height*.75)

date = img[h1:h2, w1:w2]
mint = img[h3:h4, w3:w4]
cv2.imwrite("image/Date.png", date)
cv2.imwrite("image/MintMark.png", mint)
cv2.waitKey(0)