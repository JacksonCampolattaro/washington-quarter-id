import cv2
import numpy as np
# import pandas as pd
from matplotlib import pyplot as plt

img = cv2.imread('Image/1dilated3it.JPG')
kernel = np.ones((3,3), np.uint8)
erosion = cv2.erode(img, kernel, iterations = 49)

plt.subplot(121), plt.imshow(img), plt.title('Original Image')
plt.subplot(122), plt.imshow(erosion), plt.title('Eroded Image')


#plt.imshow(img)
plt.show()
