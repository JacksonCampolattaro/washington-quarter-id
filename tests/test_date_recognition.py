import unittest
import cv2
import os
import glob

from quarterid import coin_read
from quarterid.coin_regularization import rotate_image


class TestDateRecognition(unittest.TestCase):

    def setUp(self):
        self.images = []

        # These tests will use all the images with annotated positions
        path = os.path.join(os.path.dirname(__file__), "data/dates")

        # We're going to try every image
        for filename in glob.glob(os.path.join(path, "*.png")):
            # Load the image
            image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)

            # image = rotate_image(image, -2)

            # Get the expected date from the path
            date = os.path.splitext(os.path.basename(filename))[0]

            # Add this pair to the list
            self.images.append((image, date))

    def test_find_date(self):
        for (image, known_date) in self.images:
            with self.subTest(date=known_date):

                date, confidence = coin_read.read_date(image)

                self.assertEqual(known_date, date, "Incorrect date detected")

                self.assertGreater(confidence, 0.5, "Confidence too low")
