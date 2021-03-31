import glob
import itertools
import os

import cv2
import logging

import numpy as np

from quarterid import image_logging, preprocessing

logger = logging.getLogger(__name__)


def compare(image, template):
    # Binarize both images
    _, template = cv2.threshold(template, 127, 255, cv2.THRESH_BINARY)
    image = preprocessing.preprocess(image)
    image = preprocessing.cover_margins(image, int(image.shape[0] / 9))
    image = preprocessing.largest_contour_only(image)

    # cv2.imshow("image", image)
    # cv2.waitKey()

    # cv2.imshow("template", template)
    # cv2.waitKey()

    # Get the contours of both images
    template_contours, _ = cv2.findContours(template, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    image_contours, _ = cv2.findContours(image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Get only the largest few image contours
    image_contours = sorted(image_contours, key=cv2.contourArea)[-len(template_contours):]

    # demo = np.zeros(image.shape)
    # cv2.drawContours(demo, image_contours, -1, (255, 255, 255), 1)
    # cv2.imshow("contours", demo)
    # cv2.waitKey()

    # Try every combination of contours
    return sum([cv2.matchShapes(template_contour, image_contour, 3, 0.0) / len(template_contours) ** 2
                for (template_contour, image_contour) in itertools.product(template_contours, image_contours)])


def read_character(character_image, allowlist, default):
    # Load our templates, if we don't already have them
    if not hasattr(read_character, 'templates'):
        # Get the path of the template images
        templates_path = os.path.join(os.path.dirname(__file__), "templates")

        # Read our template images into a map (key is the character they represent)
        read_character.templates = {
            filename[0]: cv2.imread(os.path.join(templates_path, filename), cv2.IMREAD_GRAYSCALE)
            for filename in os.listdir(templates_path)
        }

    # Get the list of relevant templates (based on the allowlist)
    relevant_templates = [(character, read_character.templates[character]) for character in allowlist]

    # Compare the contour of the input image to that of each template
    distances = {
        character: compare(character_image, template)
        for (character, template) in relevant_templates
    }
    print(distances)

    # Chosen character is the one with the most weight
    most_likely_value = min(distances, key=distances.get)

    # Return the character, and the confidence (based on a logistic function of the input
    return most_likely_value, 1 / (1 + np.exp(- distances[most_likely_value]))
