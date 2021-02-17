import os
import sys
import logging
from datetime import datetime
import numpy as np
import cv2

from quarterid import image_logging
from quarterid.coin_isolation import split_coins

logger = logging.getLogger(__name__)


def rotate_image(image, degrees):
    # From: https://stackoverflow.com/questions/9041681/opencv-python-rotate-image-by-x-degrees-around-specific-point
    image_center = tuple(np.array(image.shape[1::-1]) / 2)
    rot_mat = cv2.getRotationMatrix2D(image_center, degrees, 1.0)
    return cv2.warpAffine(image, rot_mat, image.shape[1::-1], flags=cv2.INTER_LINEAR)


def intensity_normalize_image(image):
    (minIntensity, maxIntensity, _, _) = cv2.minMaxLoc(image)
    average_intensity = (maxIntensity - minIntensity) / 2 # cv2.mean(image)[0]
    return abs(image - average_intensity) * 2


def main():
    # Set up logging
    dirname = "results/{:%Y%m%d_%H%M%S}/".format(datetime.now())
    os.mkdir(dirname)
    logging.basicConfig(filename=dirname + "log.log", filemode='w', level=logging.DEBUG)
    logging.getLogger().addHandler(logging.StreamHandler(sys.stdout))

    # Load an image
    image = cv2.imread("data/single/RelativeAngle=90deg_VerticalAngles=30,30deg_Distances=35,35cm,Rotation=0deg.png",
                       0)
    logger.info(f"Loaded image of size {image.shape[0]}x{image.shape[1]}")

    # Search for circular elements in the image
    coins_found = split_coins(image=image, pix_radius=750)

    # Iterate over all the coins that were found
    for index, (coin_image, circle) in enumerate(coins_found):
        (x, y, r) = circle
        rotated_image = rotate_image(coin_image, 0)
        image_logging.info(rotated_image, f"coin_{index}_({x},{y})")
        normalized_image = intensity_normalize_image(rotated_image)
        image_logging.info(normalized_image, f"coin_{index}_({x},{y})_normalized")

    # Annotate the original image, for debugging
    for _, (x, y, r) in coins_found:
        # Draw a circle which outlines that one
        cv2.circle(image, (x, y), r, (255, 255, 255), 4)
    image_logging.info(image, "annotated")


if __name__ == '__main__':
    main()
