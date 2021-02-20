import numpy as np
# import argparse
import cv2

img = cv2.imread("Image/TestQuarters.jpg", 0)

yimg = img.copy()
img = cv2.medianBlur(img, 25)
width = int(img.shape[1] * 0.2)
height = int(img.shape[0] * 0.2)
dim = (width, height)
zimg = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
yimg = cv2.resize(yimg, dim, interpolation = cv2.INTER_AREA)
cimg = cv2.cvtColor(yimg, cv2.COLOR_GRAY2BGR)


circles = cv2.HoughCircles(zimg, cv2.HOUGH_GRADIENT, 1, 50)

circles = np.uint16(np.around(circles))
for i in circles[0, :]:
    # draw the outer circle
    cv2.circle(cimg, (i[0], i[1]), i[2], (0, 255, 0), 2)
    # draw the center of the circle
    # cv2.circle(cimg, (i[0], i[1]), 2, (0, 0, 255), 3)

cv2.imshow('detected circles', cimg)
cv2.waitKey(0)
# cv2.destroyAllWindows()
print("done")