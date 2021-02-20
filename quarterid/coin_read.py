import numpy as np
import cv2
import easyocr
import logging

from quarterid import image_logging
from quarterid import coin_regularization, coin_isolation, preprocessing

logger = logging.getLogger(__name__)


def isolate_date(coin_image):

    # We can assume our image is square
    side_length = coin_image.shape[0]

    # These determine the pixel size of the digits
    char_width = int(side_length / 12)
    char_height = int(char_width * 1.25)

    # This determines the gap between the pixels and the bottom of the image
    rim_thickness = int(side_length / 45)

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

    reader = easyocr.Reader(['en'])

    for i, image in enumerate(isolate_date(coin_image)):
        image_logging.info(image, f"digit_{i}")

        image = preprocessing.preprocess(image)
        image = preprocessing.cover_margins(image, 15)
        image_logging.info(image, f"preprocessed_digit_{i}")

        text = reader.readtext(image, allowlist="1234567890", detail=1)
        print(text)

    return "2000"
