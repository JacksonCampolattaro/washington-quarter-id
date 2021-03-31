import numpy as np
import cv2
import logging

from quarterid import coin_regularization, coin_isolation
from quarterid.ocr import easy, hu_moment

logger = logging.getLogger(__name__)


def isolate_date(coin_image):
    # We can assume our image is square
    side_length = coin_image.shape[0]

    # These determine the pixel size of the digits
    char_width = int(side_length / 10)
    char_height = int(char_width * 1.40)

    # This determines the gap between the pixels and the bottom of the image
    rim_thickness = int(side_length * 0.015)

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
    # We can assume our image is square
    side_length = coin_image.shape[0]

    # These determine the pixel size of the mint mark
    mint_width = int(side_length / 20)
    mint_height = mint_width

    # Find the coordinates defining the mint mark's location
    mint_start_x = int(side_length * 0.81)
    mint_start_y = int(side_length * 0.69)
    mint_end_x = mint_start_x + mint_width
    mint_end_y = mint_start_y + mint_height
    mint_box = (mint_start_x, mint_start_y, mint_end_x, mint_end_y)

    return coin_isolation.cut_image(coin_image, mint_box)


def read_character(character_image, allowlist, default):
    return easy.read_character(character_image, allowlist, default)


def read_date(coin_image):
    digits = isolate_date(coin_image)

    # Split the digits up, because we'll be treating parts of the date separately
    millennium, century, decade, year = digits

    # Each digit is allowed to have different possible values
    millennium, millennium_confidence = read_character(millennium, "12", '1')
    century, century_confidence = read_character(century, "90", '9')
    decade, decade_confidence = read_character(decade, "34567890", '9')
    year, year_confidence = read_character(year, "1234567890", '1')

    combined_confidence = sum([millennium_confidence, century_confidence, decade_confidence, year_confidence]) / 4

    return millennium + century + decade + year, combined_confidence


def read_mint(coin_image):
    mint_image = isolate_mint_mark(coin_image)

    return read_character(mint_image, "DP", 'D')
