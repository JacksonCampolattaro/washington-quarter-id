import os
import cv2
import matplotlib.pyplot as plt
import numpy as np

from quarterid import coin_read, coin_regularization


def main():
    # File to load our image from
    filename = "data/dates/1967.png"

    # Load an image
    image = cv2.imread(
        filename,
        cv2.IMREAD_GRAYSCALE
    )
    assert image is not None
    # image = coin_regularization.rotate_image(image, 120)

    # Keep track of the correct date, based on the image name
    correct_date = os.path.splitext(os.path.basename(filename))[0]

    # Create a plot
    plt.style.use('dark_background')
    axis = plt.subplot(projection='polar')
    axis.set_title("Coin-reading confidence as a function of image rotation (1967)")
    axis.set_theta_zero_location("S")
    axis.set_rmax(1.0)

    # Try the image at every angle
    steps = 9000
    for angle in np.linspace(-180, 180, steps):

        # Make a prediction based on a rotated image
        prediction, confidence = coin_read.read_date(coin_regularization.rotate_image(image, angle))
        print(f"\t{angle:.2f}°:\t\t{confidence:.2f}%\t[{prediction}]")

        # If our prediction was right, we'll mark it in green
        color = "green" if prediction == correct_date else "lightblue"

        # Add the confidence to the plot
        radian = angle * np.pi / 180
        step_width = 2 * np.pi / steps
        axis.bar(radian, confidence, width=step_width, bottom=0, color=color)

    # Display the plot
    plt.show()


if __name__ == '__main__':
    main()
