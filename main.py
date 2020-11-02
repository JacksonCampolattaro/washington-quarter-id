import numpy as np
import cv2

if __name__ == '__main__':

    # Load an image
    image = cv2.imread("data/test.jpg")

    # Convert the image to grayscale
    grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Create an output image we can draw on
    output = image.copy()

    # Find the circles in the image
    circles = cv2.HoughCircles(grayscale, cv2.HOUGH_GRADIENT, 1.2, 100)

    # Notify the user if we couldn't find any circles
    if circles is None:
        raise Exception("Couldn't find any circles!")

    # Convert circle data to integers
    circles = np.round(circles[0, :]).astype("int")

    # Iterate over each of the circles found
    for (x, y, r) in circles:

        # Draw a circle which outlines that one
        cv2.circle(output, (x, y), r, (0, 255, 0), 2)

    # Display the image and wait for the user to view it
    cv2.imshow("output", output)
    cv2.waitKey(0)
