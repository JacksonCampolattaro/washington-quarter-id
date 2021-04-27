from quarterid.capture import capture
import cv2


def batch_capture():
    rel_angle = 45
    l1_angle = 30
    l2_angle = 30
    l1_distance = 60
    l2_distance = 60

    # Save the image
    cv2.imwrite("data/batch/RelativeAngle={}deg_VerticalAngles={},{}deg_Distances={},{}cm.png".format(
        rel_angle,
        l1_angle,
        l2_angle,
        l1_distance,
        l2_distance
    ), capture())


def single_capture():
    rel_angle = 90
    l1_angle = 35
    l2_angle = 35
    l1_distance = 28
    l2_distance = 28
    coin_rotation = 0

    # Save the image
    cv2.imwrite(
        "data/single/RelativeAngle={}deg_VerticalAngles={},{}deg_Distances={},{}cm,Rotation={}deg.png".format(
            rel_angle,
            l1_angle,
            l2_angle,
            l1_distance,
            l2_distance,
            coin_rotation
        ), capture())



def main():
    # single_capture()
    cv2.imwrite("data/test.png", capture())


if __name__ == '__main__':
    main()
