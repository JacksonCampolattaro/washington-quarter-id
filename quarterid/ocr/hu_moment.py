import cv2
import easyocr
import logging

import numpy as np

from quarterid import image_logging, preprocessing

logger = logging.getLogger(__name__)


def read_character(character_image, allowlist, default):
    return '9', 1
