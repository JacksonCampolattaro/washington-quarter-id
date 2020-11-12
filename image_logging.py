import logging


def debug_image(logger, image, path):
    logger.debug(f"logging image at path {path}")


setattr(logging.Logger, "debug_image", debug_image)
