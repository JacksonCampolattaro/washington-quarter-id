import logging
import cv2
import os

logger = logging.getLogger(__name__)


def get_path_prefix():
    return os.path.dirname(logging.getLogger().handlers[0].baseFilename)


def debug(image, name):
    if logger.isEnabledFor(logging.DEBUG):
        path = f"{get_path_prefix()}/{name}.png"
        logger.debug(f"Saving image to path {path}")
        cv2.imwrite(path, image)


def info(image, name):
    if logger.isEnabledFor(logging.INFO):
        path = f"{get_path_prefix()}/{name}.png"
        logger.info(f"Saving image to path {path}")
        cv2.imwrite(path, image)
