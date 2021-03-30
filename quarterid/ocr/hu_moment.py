import cv2
import logging

from quarterid import image_logging, preprocessing

logger = logging.getLogger(__name__)


def read_character(character_image, allowlist, default):

    # Load our templates, if we don't already have them
    if not hasattr(read_character, 'templates'):
        # TODO

        # Read our template images into a map (key is the character they represent)

        return

    # Compare the contour of the input image to that of each template

    # Chosen character is the one with the least "distance"

    # Smaller distances indicate lower confidence

    # Return the character, and the confidence
    return '9', 0.1
