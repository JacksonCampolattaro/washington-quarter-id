import easyocr
import cv2
from matplotlib import pyplot as plt
import numpy as np

IMAGE_PATH = 'Image/7.png'

reader = easyocr.Reader(['en'], gpu=False)
result = reader.readtext(IMAGE_PATH)
print(result)