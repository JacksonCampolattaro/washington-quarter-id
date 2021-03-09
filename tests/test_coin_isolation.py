import unittest
import cv2
import os
import glob

from quarterid import coin_isolation


class TestCoinIsolation(unittest.TestCase):

    def setUp(self):
        self.images = []

        # These tests will use all the images with annotated positions
        path = os.path.join(os.path.dirname(__file__), "data/positions")

        # We're going to try every image
        for filename in glob.glob(os.path.join(path, "*.png")):

            # Load the image
            image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)

            # Get the expected location from the path
            name = os.path.splitext(os.path.basename(filename))[0]
            location = [int(x) for x in name.split(',')]

            # Add this pair to the list
            self.images.append((image, location))

    def test_find_circles(self):

        for (image, known_location) in self.images:
            with self.subTest(location=known_location):

                # Use our function to find the locations
                locations = coin_isolation.find_circles(image, pix_radius=731)

                # There should only be one coin
                self.assertEqual(1, len(locations))

                # The location of the coin should be pretty close to the known correct location
                (x, y, r) = locations[0]
                (known_x, known_y, known_r) = known_location
                self.assertAlmostEqual(known_x, x, delta=10, msg="Incorrect x")
                self.assertAlmostEqual(known_y, y, delta=10, msg="Incorrect y")
                self.assertAlmostEqual(known_r, r, delta=10, msg="Incorrect radius")
