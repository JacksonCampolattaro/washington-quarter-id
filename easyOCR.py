import easyocr
import cv2
from matplotlib import pyplot as plt
import numpy as np

IMAGE_PATH = 'Image/Contours.png'

reader = easyocr.Reader(['en'], gpu=False)
result = reader.readtext(IMAGE_PATH,'greedy',5,1,0,"0123456789")
print(result)