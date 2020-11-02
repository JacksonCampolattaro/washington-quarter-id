import numpy as np
import argparse
import cv2

# construct parser
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path to the image")
args = vars(ap.parse_args())

# load image
image = cv2.imread(args["image"])
output = image.copy()
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# detect circles
circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1.2, 100)

# make sure some circles were found
if circles is not None:
    # convert x,y and radius into integers
    circles = np.round(circles[0, :]).astype("int")
    # loop
    for (x, y, r) in circles:
        # draw circle, then rectangle
        cv2.circle(output, (x, y), r, (0, 255, 0), 4)
        cv2.rectangle(output, (x-5, y-5,), (x+5, y+5), (0, 128, 255), -1)

    # show output
    cv2.imshow("output", np.hstack([image, output]))
    cv2.waitKey(0)
