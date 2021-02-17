import cv2
import numpy as np

from quarterid import image_logging


def find_circles(image, pix_radius):
    # Convert the image to grayscale
    grayscale = image  # cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Smooth the image
    blur = cv2.GaussianBlur(
        src=grayscale,
        ksize=(5, 5),
        sigmaX=0
    )
    image_logging.debug(blur, "blur")

    # Find the circles based on their edges
    tolerance = 15
    circles = cv2.HoughCircles(
        image=blur,
        method=cv2.HOUGH_GRADIENT,
        dp=2,
        minDist=(pix_radius * 2) - (tolerance * 4),
        param1=100,
        param2=100,
        minRadius=pix_radius - tolerance,
        maxRadius=pix_radius + tolerance
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
