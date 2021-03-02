import cv2
import numpy as np
# import pandas as pd
from matplotlib import pyplot as plt

img = cv2.imread('Image/Contours.png')
kernel = np.ones((5,5), np.uint8)
#closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
plt.subplot(121), plt.imshow(img), plt.title('Original Image')
#plt.subplot(122), plt.imshow(closing), plt.title('Closing Image')
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
dilation = cv2.dilate(closing, kernel, iterations = 2)
erosion = cv2.erode(dilation,kernel,iterations= 2)
plt.subplot(122), plt.imshow(erosion), plt.title('Dilation Image')
cv2.imwrite("Image/Dilation.png", erosion)
#plt.imshow(img)
plt.show()