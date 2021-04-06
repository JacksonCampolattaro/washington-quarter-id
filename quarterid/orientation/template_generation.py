import glob
import os

import cv2
import numpy as np

from quarterid.orientation.template_match import edges, without_rim


def center_crop(image, edge_fraction):
    w, h = image.shape
    edge_thickness = int(w * edge_fraction / 2)
    return image[edge_thickness: h - edge_thickness, edge_thickness: w - edge_thickness]


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
