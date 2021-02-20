import numpy as np
import cv2
import pytesseract
import logging

from quarterid import image_logging
from quarterid import coin_regularization, coin_isolation

logger = logging.getLogger(__name__)


def isolate_date(coin_image):

    # We can assume our image is square
    side_length = coin_image.shape[0]

    # These determine the pixel size of the digits
    char_width = int(side_length / 13)
    char_height = int(char_width * 1.25)

    # This determines the gap between the pixels and the bottom of the image
    rim_thickness = int(side_length / 40)

    # These are the bounds of the region we need to take
    char_start_x = int((side_length - char_width) / 2)
    char_start_y = int(side_length - char_height - rim_thickness)
    char_end_x = char_start_x + char_width
    char_end_y = char_start_y + char_height
    char_box = (char_start_x, char_start_y, char_end_x, char_end_y)

    # Start by rotating the image to center the first digit
    rotated_image = coin_regularization.rotate_image(coin_image, 25)

    # We can *probably* trust that our dates will have 4 digits
    digits = []
    for _ in range(4):

        # Cut out this digit
        digits.append(coin_isolation.cut_image(rotated_image, char_box))

        # Rotate the image to the next digit
        rotated_image = coin_regularization.rotate_image(rotated_image, -14)

    return digits


def isolate_mint_mark(coin_image):
    return coin_image


def read_date(coin_image):

    for i, image in enumerate(isolate_date(coin_image)):
        image_logging.info(image, f"{i}")

    # Find the locations of each character
    data = pytesseract.image_to_data(coin_image, output_type=pytesseract.Output.DICT)

    # Create a color image that we can mark up
    color_image = coin_image  # cv2.cvtColor(coin_image, cv2.COLOR_GRAY2RGB)
    logger.info(f"Image shape {coin_image.shape}")

    # Draw green boxes around each character that was found
    for x, y, w, h in zip(data['left'], data['top'], data['width'], data['height']):
        logger.info(f"Found character on coin at (x, y, w, h) = ({x}, {y}, {w}, {h})")
        cv2.rectangle(color_image, (x, y), (w, h), (0, 255, 0), 3)

    image_logging.info(color_image, "date_reading_boxes")

    return "2000"
