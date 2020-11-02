import cv2

if __name__ == '__main__':

    image = cv2.imread("data/test.jpg")
    grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    cv2.imshow("output", grayscale)
    cv2.waitKey(0)
