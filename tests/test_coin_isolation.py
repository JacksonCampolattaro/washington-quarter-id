import unittest
import cv2
import os
import glob

from quarterid import coin_isolation


class TestCoinIsolation(unittest.TestCase):

    def SetUp(self):

        images = []

        # These tests will use all the images with annotated positions
        path = os.path.join(os.path.dirname(__file__), "data/positions")

        # We're going to try every image
        for filename in glob.glob(os.path.join(path, "*.png")):
            with cv2.imread(filename, cv2.IMREAD_GRAYSCALE) as image:
                images.append(image)
                # TODO set image position

        return

    def test_find_circles(self):

        # Open the file containing our image
        image = cv2.imread(
            "data/positions/2147,1121,730.png",
            cv2.IMREAD_GRAYSCALE
        )

        # Use our function to find the locations
        locations = coin_isolation.find_circles(image, pix_radius=745)

        # There should only be one coin
        self.assertEqual(1, len(locations))

        # The location of the coin should be pretty close to a known correct location
        (x, y, r) = locations[0]
        self.assertAlmostEqual(2161, x, delta=5)
        self.assertAlmostEqual(1131, y, delta=5)
        self.assertAlmostEqual(745, r, delta=10, msg="Incorrect radius!")
