from datetime import datetime
import numpy as np
import cv2


def find_circles(image):
    # Convert the image to grayscale
    grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Smooth the image
    blur = cv2.blur(grayscale, (7, 7))
    cv2.imwrite("blur.jpg", blur)

    # Apply a threshold (binarize the image)
    ret, binary = cv2.threshold(blur, 60, 255, cv2.THRESH_BINARY)
    cv2.imwrite("binary.jpg", binary)

    # Find the circles in the image
    coin_radius = 300
    circles = cv2.HoughCircles(binary, cv2.HOUGH_GRADIENT, 2,
                               coin_radius * 2,
                               # param1=100,
                               # param2=0.8,
                               # minRadius=coinRadius - 100,
                               # maxRadius=coinRadius + 500,
                               )

    # Notify the user if we couldn't find any circles
    if circles is None:
        raise Exception("Couldn't find any circles!")

    # Convert circle data to integers
    circles = np.round(circles[0, :]).astype("int")

    return circles


if __name__ == '__main__':

    # Load an image
    image = cv2.imread("data/test.jpg")
    print('Loaded image of size {}x{}'.format(image.shape[0], image.shape[1]))

    # Create an output image we can draw on
    output = image.copy()

    circles_found = find_circles(image)

    # Iterate over each of the circles found
    for (x, y, r) in circles_found:
        # Draw a circle which outlines that one
        cv2.circle(output, (x, y), r, (0, 255, 0), 2)

    # Display the image and wait for the user to view it
    # cv2.imshow("output", output)
    # cv2.waitKey(0)

    # Save the image to a file named with the current date and time
    filename = "results/{:%Y%m%d_%H%M%S}.jpg".format(datetime.now())
    cv2.imwrite(filename, output)
