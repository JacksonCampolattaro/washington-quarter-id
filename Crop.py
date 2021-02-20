# Importing Image class from PIL module
import numpy as np
import cv2
from quarterid.coin_regularization import rotate_image
# Opens a image in RGB mode
#im = Image.open(r"C:\Users\Admin\Pictures\geeks.png")
img = cv2.imread("image/contrast.jpg", 0)
width = int(img.shape[1])
height = int(img.shape[0])
w1 = int(width*.29)
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

wi = int(date.shape[1])
hi = int(date.shape[0])
w5 = int(wi*.02)
w6 = int(wi*.18)
h5 = int(hi*.07)
h6 = int(hi*.80)
num1 = date[h5:h6, w5:w6]
d1 = rotate_image(num1, 20)
cv2.imwrite("image/1.png", d1)

wi = int(date.shape[1])
hi = int(date.shape[0])
w5 = int(wi*.22)
w6 = int(wi*.44)
h5 = int(hi*.24)
h6 = int(hi*.95)
num2 = date[h5:h6, w5:w6]
cv2.imwrite("image/9.png", num2)

wi = int(date.shape[1])
hi = int(date.shape[0])
w5 = int(wi*.50)
w6 = int(wi*.70)
h5 = int(hi*.29)
h6 = int(hi*.99)
num3 = date[h5:h6, w5:w6]
cv2.imwrite("image/7.png", num3)

wi = int(date.shape[1])
hi = int(date.shape[0])
w5 = int(wi*.78)
w6 = int(wi*.98)
h5 = int(hi*.19)
h6 = int(hi*.9)
num3 = date[h5:h6, w5:w6]
d1 = rotate_image(num3, -15)
cv2.imwrite("image/3.png", d1)

cv2.waitKey(0)