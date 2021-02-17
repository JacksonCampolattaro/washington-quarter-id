import numpy as np
import cv2
import pytesseract
import logging

from quarterid import image_logging

logger = logging.getLogger(__name__)


def read_date(coin_image):
    # Find the locations of each character
    data = pytesseract.image_to_data(coin_image, output_type=pytesseract.Output.DICT)

    # Create a color image that we can mark up
    color_image = cv2.cvtColor(coin_image, cv2.COLOR_GRAY2RGB)
    logger.info(f"Image shape {coin_image.shape}")

    # Draw green boxes around each character that was found
    for x, y, w, h in zip(data['left'], data['top'], data['width'], data['height']):
        logger.info(f"Found character on coin at (x, y, w, h) = ({x}, {y}, {w}, {h})")
        cv2.rectangle(color_image, (x, y), (w, h), (0, 255, 0), 3)

    image_logging.info(color_image, "date_reading_boxes")

    return "2000"
