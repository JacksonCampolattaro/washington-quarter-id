import os
import cv2
import matplotlib.pyplot as plt
import numpy as np

from quarterid import coin_read, coin_regularization

def try_range(image, angles):

    results = []

    for angle in angles:

        # Make a prediction based on a rotated image
        prediction, confidence = coin_read.read_date(coin_regularization.rotate_image(image, angle))
        print(f"\t{angle:.2f}°:\t\t{confidence:.2f}%\t[{prediction}]")

        results.append((prediction, confidence))

    return results


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
    fig, axes = plt.subplots(3)
    fig.suptitle("Progressive Coin-reading confidence as a function of image rotation (1967)")

    # Perform a search across the entire range
    angles = np.linspace(-180, 180, 40)
    predictions, confidences = zip(*try_range(image, angles))
    colors = ["green" if prediction == correct_date else "lightblue" for prediction in predictions]

    # Plot the results of the first iteration
    axes[0].bar(angles, confidences, color=colors, width=angles[1] - angles[0])

    # Find the angle with the highest confidence
    best_angle = angles[confidences.index(max(confidences))]

    # Repeat for a range centered around the best angle
    angles = np.linspace(best_angle - 20, best_angle + 20, 40)
    predictions, confidences = zip(*try_range(image, angles))
    colors = ["green" if prediction == correct_date else "lightblue" for prediction in predictions]

    # Plot the results of the first iteration
    axes[1].bar(angles, confidences, color=colors, width=angles[1] - angles[0])

    # Find the angle with the highest confidence
    best_angle = angles[confidences.index(max(confidences))]

    # Repeat for a range centered around the best angle
    angles = np.linspace(best_angle - 3, best_angle + 3, 40)
    predictions, confidences = zip(*try_range(image, angles))
    colors = ["green" if prediction == correct_date else "lightblue" for prediction in predictions]

    # Plot the results of the first iteration
    axes[2].bar(angles, confidences, color=colors, width=angles[1] - angles[0])

    # Display the plot
    plt.show()


if __name__ == '__main__':
    main()
