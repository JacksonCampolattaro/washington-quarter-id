import glob
import os

import cv2
import numpy as np

import quarterid.coin_isolation
from quarterid import coin_isolation, coin_regularization


def similarity_to_template(image, template):
    return cv2.matchTemplate(image, template, cv2.TM_CCOEFF).max()


def without_rim(image, rim_fraction):
    w, h = image.shape
    r = int((w / 2) * (1.0 - rim_fraction))
    return quarterid.coin_isolation.hole_punch_mask(image, (int(w / 2), int(h / 2), r))


def center_crop(image, edge_fraction):
    w, h = image.shape
    edge_thickness = int(w * edge_fraction / 2)
    return image[edge_thickness: h - edge_thickness, edge_thickness: w - edge_thickness]


def edges(image):
    # Blur the image
    blur = cv2.GaussianBlur(image, (21, 21), 4, None, 3)  # TODO Document these parameters

    # Find x and y axis edges
    x_edges = cv2.Sobel(blur, cv2.CV_32F, 1, 0, ksize=3)
    y_edges = cv2.Sobel(blur, cv2.CV_32F, 0, 1, ksize=3)

    # Find the combined magnitude of both edge directions
    combined_edges = cv2.magnitude(x_edges, y_edges)

    return np.uint8(255 * combined_edges / np.max(combined_edges))


def main():
    # Load all the example images
    path = os.path.join(os.path.dirname(__file__), "../../tests/data/dates")
    images = [cv2.imread(filename, cv2.IMREAD_GRAYSCALE) for filename in glob.glob(os.path.join(path, "*.png"))]

    # Produce a set of edge images
    edge_images = [edges(image) for image in images]

    # Combine edge images into an average
    average_edge = np.uint8(sum(image / len(edge_images) for image in edge_images))

    # cv2.imshow("test", average_edge)
    # cv2.waitKey()

    # Remove rims from the edges
    rim_thickness = 0.07
    template_image = without_rim(average_edge, rim_thickness)
    template_image = center_crop(template_image, rim_thickness)

    # cv2.imshow("test", template_image)
    # cv2.waitKey()

    # Save the average
    cv2.imwrite("templates/edges.png", template_image)


if __name__ == '__main__':
    main()
