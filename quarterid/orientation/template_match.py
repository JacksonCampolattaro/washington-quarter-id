import os

import cv2
import numpy as np

import quarterid.coin_regularization
from quarterid import coin_isolation
from quarterid.coin_regularization import rotate_image


def similarity_to_template(image, template):
    return cv2.matchTemplate(image, template, cv2.TM_CCOEFF).max()


def edges(image):
    # Blur the image
    blur = cv2.GaussianBlur(image, (21, 21), 4, None, 3)  # TODO Document these parameters

    # Find x and y axis edges
    x_edges = cv2.Sobel(blur, cv2.CV_32F, 1, 0, ksize=3)
    y_edges = cv2.Sobel(blur, cv2.CV_32F, 0, 1, ksize=3)

    # Find the combined magnitude of both edge directions
    combined_edges = cv2.magnitude(x_edges, y_edges)

    return np.uint8(255 * combined_edges / np.max(combined_edges))


def without_rim(image, rim_fraction):
    w, h = image.shape
    r = int((w / 2) * (1.0 - rim_fraction))
    return coin_isolation.hole_punch_mask(image, (int(w / 2), int(h / 2), r))


def find_angle(image):
    # Load the template image (if it's not already loaded)
    if not hasattr(find_angle, 'template'):
        template_path = os.path.join(os.path.dirname(__file__), "templates/edges.png")
        find_angle.template = cv2.cv2.imread(template_path, cv2.IMREAD_GRAYSCALE)

    # Preprocess the input image (in the same way the template was preprocessed)
    edge_image = edges(image)

    # Find the similarity for a variety of angles
    similarities = {angle: similarity_to_template(rotate_image(edge_image, angle), find_angle.template)
                    for angle in np.linspace(-180, 180, 100)}

    # Find the angle of highest similarity
    best_angle = max(similarities, key=similarities.get)
    print(best_angle)

    return best_angle
