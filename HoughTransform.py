import numpy as np
# import argparse
import cv2


img = cv2.imread("image/TestQuarters.jpg", 0)
img = cv2.medianBlur(img, 7)
width = int(img.shape[1] * 0.2)
height = int(img.shape[0] * 0.2)
dim = (width, height)
zimg = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
cimg = cv2.cvtColor(zimg, cv2.COLOR_GRAY2BGR)

circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 2, 300, param1=30, param2=30, minRadius=0, maxRadius=0)

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
# construct parser
# ap = argparse.ArgumentParser()
# ap.add_argument("-i", "--image", required=True, help="Path")
# args = vars(ap.parse_args())

# load image
# image = cv2.imread("image/TestQuarters.jpg")
# image = cv2.imread(args["image"])
# output = image.copy()
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# detect circles
# circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1.2, 100)

# make sure some circles were found
# if circles is not None:
# convert x,y and radius into integers
 #   circles = np.round(circles[0, :]).astype("int")
    # loop
  #  for (x, y, r) in circles:
        # draw circle, then rectangle
   #     cv2.circle(output, (x, y), r, (0, 255, 0), 4)
    #    cv2.rectangle(output, (x-5, y-5,), (x+5, y+5), (0, 128, 255), -1)

    # show output
   # cv2.imshow("output", np.hstack([image, output]))
    # cv2.waitKey(0)
