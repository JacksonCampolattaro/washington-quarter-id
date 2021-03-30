import unittest
import cv2
import os
import glob

from quarterid import coin_read
from quarterid.ocr import hu_moment


class TestHuMoment(unittest.TestCase):

    def setUp(self):
        self.images = []

        # These tests will use all the images with annotated positions
        path = os.path.join(os.path.dirname(__file__), "data/digits")

        # We're going to try every image
        for filename in glob.glob(os.path.join(path, "*.png")):
            # Load the image
            image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)

            # Get the expected digit from the path
            digit = os.path.splitext(os.path.basename(filename))[0][0]

            # Add this pair to the list
            self.images.append((image, digit))

    def test_find_digit(self):
        for (image, known_digit) in self.images:
            with self.subTest(digit=known_digit):

                date, confidence = hu_moment.read_character(image, "0123456789", None)

                self.assertEqual(known_digit, date, "Incorrect digit detected")

                self.assertGreater(confidence, 0.5, "Confidence too low")
