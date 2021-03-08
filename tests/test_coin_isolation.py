import unittest
import cv2

from quarterid import coin_isolation


class TestCoinIsolation(unittest.TestCase):

    def SetUp(self):
        # TODO
        return

    def test_find_circles(self):
        # Open the file containing our image
        image = cv2.imread(
            "data/mixed/1995.png",
            cv2.IMREAD_GRAYSCALE
        )

        # Use our function to find the locations
        locations = coin_isolation.find_circles(image, pix_radius=745)

        # There should only be one coin
        self.assertEqual(1, len(locations))
