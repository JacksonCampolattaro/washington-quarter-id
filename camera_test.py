from capture import capture
import cv2


def main():

    rel_angle = 45
    l1_angle = 30
    l2_angle = 30
    l1_distance = 60
    l2_distance = 60

    # Save the image
    cv2.imwrite("data/RelativeAngle={}deg_VerticalAngles={},{}deg_Distances={},{}cm.png".format(
        rel_angle,
        l1_angle,
        l2_angle,
        l1_distance,
        l2_distance
    ), capture())


if __name__ == '__main__':
    main()
