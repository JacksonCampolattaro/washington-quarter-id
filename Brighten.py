
from builtins import input
import cv2
import numpy as np
import argparse
# Read image given by user
simg = cv2.imread("image/SingleCoinTest.png", 0)
img = simg.copy()
alpha = 3.0 # Simple contrast control
beta = -127    # Simple brightness control
out = cv2.addWeighted(simg, alpha, simg, 0, beta)
output = cv2.addWeighted
#cv2.imshow('Original Image', img)
cv2.imshow('New Image', out)
cv2.imwrite("image/contrast.jpg", out)
# Wait until user press some key
cv2.waitKey()