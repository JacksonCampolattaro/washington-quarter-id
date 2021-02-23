import cv2
import numpy as np
# import pandas as pd
from matplotlib import pyplot as plt

img = cv2.imread('Image/preprocessed_digit_0.png')
kernel = np.ones((4,4), np.uint8)
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
plt.subplot(121), plt.imshow(img), plt.title('Original Image')
plt.subplot(122), plt.imshow(closing), plt.title('Closing Image')


#plt.imshow(img)
plt.show()
