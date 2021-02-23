import cv2
import numpy as np
# import pandas as pd
from matplotlib import pyplot as plt

img = cv2.imread('Image/preprocessed_digit_0.png')
kernel = np.ones((6,6), np.uint8)
dilation = cv2.dilate(img, kernel, iterations = 3)

plt.subplot(121), plt.imshow(img), plt.title('Original Image')
plt.subplot(122), plt.imshow(dilation), plt.title('Dilation Image')


#plt.imshow(img)
plt.show()
