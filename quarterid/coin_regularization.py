import cv2
import numpy as np


def rotate_image(image, degrees):
    # From: https://stackoverflow.com/questions/9041681/opencv-python-rotate-image-by-x-degrees-around-specific-point
    image_center = tuple(np.array(image.shape[1::-1]) / 2)
    rot_mat = cv2.getRotationMatrix2D(image_center, degrees, 1.0)
    return cv2.warpAffine(image, rot_mat, image.shape[1::-1], flags=cv2.INTER_LINEAR)


def intensity_normalize_image(image):
    (minIntensity, maxIntensity, _, _) = cv2.minMaxLoc(image)
    average_intensity = (maxIntensity - minIntensity) / 2 # cv2.mean(image)[0]
    return abs(image - average_intensity) * 2