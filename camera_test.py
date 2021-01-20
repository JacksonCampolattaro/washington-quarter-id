from capture import capture
import cv2


def main():

    rel_angle = 180
    l1_angle = 45
    l2_angle = 45
    l1_distance = 35
    l2_distance = 35

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
