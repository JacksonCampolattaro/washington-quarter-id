from capture import capture
import cv2


def main():
    # Save the image
    cv2.imwrite("test.png", capture())


if __name__ == '__main__':
    main()
