import numpy as np
import cv2
import logging

from quarterid import image_logging, coin_regularization

logger = logging.getLogger(__name__)


def intensity_clamp_image(image, percentile):
    print(np.percentile(image, percentile))
    new_max_intensity = np.percentile(image, percentile)
    return np.clip(image, 0, new_max_intensity).astype(np.uint8)


def clean_binarization_image(image):

    image = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 35, 2)
    image_logging.info(image, f"preprocessing_binary")
    return image


def preprocess(image):
    # image = coin_regularization.intensity_normalize_image(image)
    # image_logging.info(image, f"preprocessing_normalized")

    # Clamp the image to remove extremely bright spots
    image = intensity_clamp_image(image, 90)
    image_logging.info(image, f"preprocessing_clamped")

    # Apply a blur to the image, to help remove remaining noise
    image = cv2.GaussianBlur(image, ksize=(0, 0), sigmaX=5)
    image_logging.info(image, f"preprocessing_blurred")

    # Use an adaptive threshold to convert the image to binary
    image = clean_binarization_image(image)
    image_logging.info(image, f"preprocessing_clean_binary")

    return image
