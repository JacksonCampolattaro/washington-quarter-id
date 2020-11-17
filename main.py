import os
import sys
import logging
from datetime import datetime
import numpy as np
import cv2

import image_logging

logger = logging.getLogger(__name__)


def find_circles(image, pix_radius):
    # Convert the image to grayscale
    grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Smooth the image
    blur = cv2.GaussianBlur(
        src=grayscale,
        ksize=(5, 5),
        sigmaX=0
    )
    image_logging.debug(blur, "blur")

    # Find the circles based on their edges
    circles = cv2.HoughCircles(
        image=blur,
        method=cv2.HOUGH_GRADIENT,
        dp=2,
        minDist=pix_radius * 2,
        param1=100,
        param2=100,
        minRadius=pix_radius - 20,
        maxRadius=pix_radius + 10
    )

    # Notify the user if we couldn't find any circles
    if circles is None:
        raise Exception("Couldn't find any circles!")

    # Return the circle locations, converted to integers
    return np.round(circles[0, :]).astype("int")


def circle_bbox(circle):
    x, y, r = circle
    return x - r, y - r, x + r, y + r


def hole_punch_mask(image, circle):
    # From: https://stackoverflow.com/questions/31519197/python-opencv-how-to-crop-circle/47629313
    (x, y, r) = circle
    mask = np.zeros(image.shape, dtype=np.uint8)
    cv2.circle(mask, (x, y), r, (255, 255, 255), thickness=-1)
    return cv2.bitwise_and(image, mask)


def cut_image(image, box):
    x1, y1, x2, y2 = box
    return image[y1:y2, x1:x2]


def rotate_image(image, degrees):
    # From: https://stackoverflow.com/questions/9041681/opencv-python-rotate-image-by-x-degrees-around-specific-point
    image_center = tuple(np.array(image.shape[1::-1]) / 2)
    rot_mat = cv2.getRotationMatrix2D(image_center, degrees, 1.0)
    return cv2.warpAffine(image, rot_mat, image.shape[1::-1], flags=cv2.INTER_LINEAR)


def main():
    # Set up logging
    dirname = "results/{:%Y%m%d_%H%M%S}/".format(datetime.now())
    os.mkdir(dirname)
    logging.basicConfig(filename=dirname + "log.log", filemode='w', level=logging.DEBUG)
    logging.getLogger().addHandler(logging.StreamHandler(sys.stdout))

    # Load an image
    image = cv2.imread("data/sample.bmp")
    logger.info(f"Loaded image of size {image.shape[0]}x{image.shape[1]}")

    # Search for circular elements in the image
    circles_found = find_circles(image=image, pix_radius=305)

    # Create an output image we can draw on
    output = image.copy()

    # Iterate over each of the circles found
    # for (x, y, r) in circles_found:
    #     # Draw a circle which outlines that one
    #     cv2.circle(output, (x, y), r, (0, 255, 0), 4)
    # image_logging.info(output, "test")

    # Display each sub-image sliced using the circle's bounding box
    for index, circle in enumerate(circles_found):
        masked_image = hole_punch_mask(image, circle)
        cropped_image = cut_image(masked_image, circle_bbox(circle))
        image_logging.info(cropped_image, f"coin_{index}")
        # cv2.imshow(f"Coin {index}", sub_image)
        # cv2.waitKey(0)

    # Display the image and wait for the user to view it
    # cv2.imshow("output", output)
    # cv2.waitKey(0)


if __name__ == '__main__':
    main()
