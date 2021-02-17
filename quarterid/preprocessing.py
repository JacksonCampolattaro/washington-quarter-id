import numpy as np
import cv2
import logging

from quarterid import image_logging, coin_regularization

logger = logging.getLogger(__name__)


def intensity_clamp(image, percentile):
    print(np.percentile(image, percentile))
    new_max_intensity = np.percentile(image, percentile)
    return np.clip(image, 0, new_max_intensity).astype(np.uint8)


def clean_binary(image):
    image = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 35, 2)
    image_logging.info(image, f"preprocessing_binary")
    return image


def watershed_segment(image):
    # from https://docs.opencv.org/master/d3/db4/tutorial_py_watershed.html

    image = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 35, 2)
    image_logging.info(image, f"debug1")

    # Remove noise using opening
    kernel = np.ones((3, 3), np.uint8)
    image = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel, iterations=1)
    image_logging.info(image, f"debug2")

    # Finding sure background area
    sure_bg = 255 - cv2.dilate(image, kernel, iterations=2)
    image_logging.info(sure_bg, f"debug3")

    # Finding sure foreground area
    dist_transform = cv2.distanceTransform(image, cv2.DIST_L2, 5)
    ret, sure_fg = cv2.threshold(dist_transform, 0.2 * dist_transform.max(), 255, 0)
    sure_fg = np.uint8(sure_fg)
    image_logging.info(sure_fg, f"debug4")

    # Finding unknown region
    unknown = 255 - sure_fg - sure_bg
    # cv2.subtract(sure_bg, sure_fg)
    image_logging.info(unknown, f"debug5")

    # Marker labelling
    ret, markers = cv2.connectedComponents(sure_fg)

    # Add one to all labels so that sure background is not 0, but 1
    markers = markers + 1

    # Now, mark the region of unknown with zero
    color_image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
    markers[unknown == 255] = 0
    markers = cv2.watershed(color_image, markers)
    color_image[markers == -1] = [255, 0, 0]
    return color_image


def blur_threshold(image):

    # Apply a blur to the image, to help remove noise
    image = cv2.GaussianBlur(image, ksize=(0, 0), sigmaX=5)
    image_logging.info(image, f"preprocessing_blurred")

    # Use an adaptive threshold to convert the image to binary
    image = clean_binary(image)
    image_logging.info(image, f"preprocessing_clean_binary")

    return image


def preprocess(image):

    # image = coin_regularization.intensity_normalize_image(image)
    # image_logging.info(image, f"preprocessing_normalized")

    # Clamp the image to remove extremely bright spots
    image = intensity_clamp(image, 90)
    image_logging.info(image, f"preprocessing_clamped")

    image = watershed_segment(image)
    image_logging.info(image, "preprocessing_watershed")

    #image = blur_threshold(image)

    return image
