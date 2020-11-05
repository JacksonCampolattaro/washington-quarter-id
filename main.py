from datetime import datetime
import numpy as np
import cv2


def find_circles(image):
    # Convert the image to grayscale
    grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Smooth the image
    blur = cv2.blur(grayscale, (7, 7))

    # Apply a threshold (binarize the image)
    ret, binary = cv2.threshold(blur, 60, 255, cv2.THRESH_BINARY)

    # # Find the edges in that binarized image
    # edges = cv2.Sobel(binary, cv2.CV_8UC1, 1, 1)
    # cv2.imwrite("edges.jpg", edges)

    # Find the circles based on their edges
    coin_radius = 300
    circles = cv2.HoughCircles(binary, cv2.HOUGH_GRADIENT, 2, coin_radius * 2)

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


if __name__ == '__main__':

    # Load an image
    image = cv2.imread("data/test.jpg")
    print('Loaded image of size {}x{}'.format(image.shape[0], image.shape[1]))

    # Create an output image we can draw on
    output = image.copy()

    # Search for circular elements in the image
    circles_found = find_circles(image)

    # Iterate over each of the circles found
    for (x, y, r) in circles_found:
        # Draw a circle which outlines that one
        cv2.circle(output, (x, y), r, (0, 255, 0), 2)

    # Display each sub-image sliced using the circle's bounding box
    boxes = [circle_bbox(circle) for circle in circles_found]
    for index, box in enumerate(boxes):
        sub = cut_image(output, box)
        cv2.imshow("Coin {}".format(index), sub)

    cv2.waitKey(0)

    # Display the image and wait for the user to view it
    # cv2.imshow("output", output)
    # cv2.waitKey(0)

    # # Save the image to a file named with the current date and time
    # filename = "results/{:%Y%m%d_%H%M%S}.jpg".format(datetime.now())
    # cv2.imwrite(filename, output)
