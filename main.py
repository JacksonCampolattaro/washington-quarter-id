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

    # Find the circles based on their edges
    circles = cv2.HoughCircles(
        image=blur,
        method=cv2.HOUGH_GRADIENT,
        dp=2,
        minDist=pix_radius * 2,
        param1=100,
        param2=100,
        minRadius=pix_radius - 10,
        maxRadius=pix_radius + 20
    )

    # Notify the user if we couldn't find any circles
    if circles is None:
        raise Exception("Couldn't find any circles!")

    # Return the circle locations, converted to integers
    return np.round(circles[0, :]).astype("int")


def circle_bbox(circle):
    x, y, r = circle
    return x - r, y - r, x + r, y + r


def cut_image(image, box):
    x1, y1, x2, y2 = box
    return image[y1:y2, x1:x2]


def main():
    # Set up logging
    dirname = "results/{:%Y%m%d_%H%M%S}/".format(datetime.now())
    os.mkdir(dirname)
    logging.basicConfig(filename=dirname + "log.log", filemode='w', level=logging.DEBUG)
    logging.getLogger().addHandler(logging.StreamHandler(sys.stdout))

    # Load an image
    image = cv2.imread("data/test.jpg")
    logger.info(f"Loaded image of size {image.shape[0]}x{image.shape[1]}")

    # Search for circular elements in the image
    circles_found = find_circles(image=image, pix_radius=320)

    # Create an output image we can draw on
    output = image.copy()

    # Iterate over each of the circles found
    for (x, y, r) in circles_found:
        # Draw a circle which outlines that one
        cv2.circle(output, (x, y), r, (0, 255, 0), 2)

    # Display each sub-image sliced using the circle's bounding box
    # sub_images = [cut_image(output, circle_bbox(circle)) for circle in circles_found]
    # for index, sub_image in enumerate(sub_images):
    #     cv2.imshow(f"Coin {index}", sub_image)
    #
    # cv2.waitKey(0)

    # Display the image and wait for the user to view it
    # cv2.imshow("output", output)
    # cv2.waitKey(0)

    # # Save the image to a file named with the current date and time
    image_logging.info(output, "test")


if __name__ == '__main__':
    main()
