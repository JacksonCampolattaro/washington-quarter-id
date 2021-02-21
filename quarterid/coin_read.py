import numpy as np
import cv2
import easyocr
import logging

from quarterid import image_logging
from quarterid import coin_regularization, coin_isolation
from quarterid.preprocessing import preprocess, largest_contour_only, cover_margins

logger = logging.getLogger(__name__)


def isolate_date(coin_image):
    # We can assume our image is square
    side_length = coin_image.shape[0]

    # These determine the pixel size of the digits
    char_width = int(side_length / 12)
    char_height = int(char_width * 1.25)

    # This determines the gap between the pixels and the bottom of the image
    rim_thickness = int(side_length / 60)

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
    # Create an EasyOCR reader set to english
    reader = easyocr.Reader(['en'])

    # Split the coin into digit images
    digits = isolate_date(coin_image)
    [image_logging.info(d, f"digit_{i}") for i, d in enumerate(digits)]

    # Convert our digit images to binary
    digits = [preprocess(digit) for digit in digits]

    # Remove noise near the margins of our images
    digits = [cover_margins(digit, int(digit.shape[0] / 7)) for digit in digits]

    # Eliminate all but the largest contour from each digit
    digits = [largest_contour_only(digit) for digit in digits]

    [image_logging.info(d, f"preprocessed_digit_{i}") for i, d in enumerate(digits)]

    # Split the digits up, because we'll be treating parts of the date separately
    millennium, century, decade, year = digits

    # Each digit is allowed to have different possible values
    millennium_result = reader.readtext(millennium, allowlist="12", detail=1)
    print(millennium_result)
    century_result = reader.readtext(century, allowlist="890", detail=1)
    print(century_result)
    decade_result = reader.readtext(decade, allowlist="1234567890", detail=1)
    print(decade_result)
    year_result = reader.readtext(year, allowlist="1234567890", detail=1)
    print(year_result)

    # TODO
    return "2000"
