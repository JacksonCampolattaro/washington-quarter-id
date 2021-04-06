import cv2
import easyocr
import logging

import numpy as np

from quarterid import image_logging, preprocessing

logger = logging.getLogger(__name__)


def read_character(character_image, allowlist, default):
    # Create an EasyOCR reader, if we don't already have one
    if not hasattr(read_character, 'reader'):
        read_character.reader = easyocr.Reader(['en'])

    # Keep track of how many times this is run (for logging)
    read_character.call_count = getattr(read_character, 'call_count', 0) + 1

    # Log the image
    image_logging.info(character_image, f"digit_{read_character.call_count}")

    # Convert our image to binary
    character_image = preprocessing.preprocess(character_image)

    # Remove noise near the margins of our image
    character_image = preprocessing.cover_margins(character_image, int(character_image.shape[0] / 9))

    # Dilate the image TODO Maybe?
    # character_image = cv2.dilate(character_image, np.ones((3, 3), np.uint8), 1)

    # Eliminate all but the largest contour from the binary image
    character_image = preprocessing.largest_contour_only(character_image)

    # Log the image
    image_logging.info(character_image, f"preprocessed_digit_{read_character.call_count}")

    # Try to read the image
    result = read_character.reader.readtext(character_image, allowlist=allowlist)

    # If no characters were found, return the default
    if not result:
        logger.debug(f"Failed to recognize character, defaulting to {default}")
        return default, 0.0

    # Otherwise, interpret the result
    string_detected = result[0][1]
    confidence = result[0][2]

    # If an empty character was found, return the default
    if not string_detected:
        return default, 0.0

    return string_detected[0], confidence
