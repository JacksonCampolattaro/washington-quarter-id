import os
import sys
import logging
from datetime import datetime
import numpy as np
import cv2

from quarterid import image_logging
from quarterid.coin_isolation import find_circles, circle_bbox, hole_punch_mask, cut_image

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
    circles_found = find_circles(image=image, pix_radius=750)

    # Display each sub-image sliced using the circle's bounding box
    for index, circle in enumerate(circles_found):
        (x, y, r) = circle
        logger.info(f"Found circle at ({x}, {y}) with radius {r}")
        masked_image = hole_punch_mask(image, circle)
        cropped_image = cut_image(masked_image, circle_bbox(circle))
        rotated_image = rotate_image(cropped_image, 0)
        image_logging.info(rotated_image, f"coin_{index}_({x},{y})")
        normalized_image = intensity_normalize_image(rotated_image)
        image_logging.info(normalized_image, f"coin_{index}_({x},{y})_normalized")
        # cv2.imshow(f"Coin {index}", sub_image)
        # cv2.waitKey(0)

    # Annotate the original image, for debugging
    for (x, y, r) in circles_found:
        # Draw a circle which outlines that one
        cv2.circle(image, (x, y), r, (0, 255, 0), 4)
    image_logging.info(image, "annotated")


if __name__ == '__main__':
    main()
