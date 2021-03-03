import os
import sys
import logging
from datetime import datetime
import cv2

from quarterid import image_logging
from quarterid.coin_isolation import split_coins
from quarterid.coin_regularization import rotate_image, intensity_normalize_image
from quarterid.coin_read import read_date, read_mint

logger = logging.getLogger(__name__)


def main():
    # Set up logging
    dirname = "results/{:%Y%m%d_%H%M%S}/".format(datetime.now())
    os.mkdir(dirname)
    logging.basicConfig(filename=dirname + "log.log", filemode='w', level=logging.DEBUG)
    logging.getLogger().addHandler(logging.StreamHandler(sys.stdout))

    # Load an image
    image = cv2.imread(
        "data/single/RelativeAngle=90deg_VerticalAngles=30,30deg_Distances=35,35cm,Rotation=0deg.png",
        # "data/mixed/1995.png",
        cv2.IMREAD_GRAYSCALE
    )
    logger.info(f"Loaded image of size {image.shape[0]}x{image.shape[1]}")

    # Search for circular elements in the image
    coins_found = split_coins(image=image, pix_radius=745)

    # Iterate over all the coins that were found
    for index, (coin_image, circle) in enumerate(coins_found):
        (x, y, r) = circle

        # TODO Find coin rotation
        rotated_image = rotate_image(coin_image, 0)
        image_logging.info(rotated_image, f"coin_{index}_({x},{y})")

        print(read_date(rotated_image))
        print(read_mint(rotated_image))

    # Annotate the original image, for debugging
    for _, (x, y, r) in coins_found:
        # Draw a circle which outlines that one
        cv2.circle(image, (x, y), r, (255, 255, 255), 4)
    image_logging.info(image, "annotated")


if __name__ == '__main__':
    main()
