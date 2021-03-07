import easyocr
import cv2
from matplotlib import pyplot as plt
import numpy as np

IMAGE_PATH = 'Image/Dilation.png'
reader = easyocr.Reader(['en'], gpu=False)
result = reader.readtext(IMAGE_PATH)#,'greedy',5,1,0,"PD")

if result == []:
    result = [1]
print(result)