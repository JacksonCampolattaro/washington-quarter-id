import os
import cv2
import matplotlib.pyplot as plt
import numpy as np

from quarterid import coin_regularization
from quarterid.orientation import template_match


def main():
    # Load an image
    image_path = "data/dates/1967.png"
    image = cv2.imread(
        image_path,
        cv2.IMREAD_GRAYSCALE
    )
    assert image is not None
    # image = coin_regularization.rotate_image(image, 120)

    # File to load our template from
    template_path = "../quarterid/orientation/templates/edges.png"
    template = cv2.imread(
        template_path,
        cv2.IMREAD_GRAYSCALE
    )
    assert template is not None

    # Create a plot
    plt.style.use('dark_background')
    axis = plt.subplot(projection='polar')
    axis.set_title("Template similarity as a function of image rotation (1967)")
    axis.set_theta_zero_location("S")
    axis.set_rmax(1.0)

    # Try the image at every angle
    steps = 100
    for angle in np.linspace(-180, 180, steps):

        similarity = template_match.similarity_to_template(coin_regularization.rotate_image(image, angle), template)
        print(similarity)

        # Add the similarity to the plot
        radian = angle * np.pi / 180
        step_width = 2 * np.pi / steps
        axis.bar(radian, similarity, width=step_width, bottom=0, color="lightblue")

    # Display the plot
    plt.show()


if __name__ == '__main__':
    main()
