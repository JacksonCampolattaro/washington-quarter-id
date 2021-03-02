# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 09:03:00 2020
@author: crjones4
"""
import numpy as np
import cv2
import sklearn.cluster as cl

def imageClamp(img, factor=0.9):
    # for now, clamp the image at its "factor" point
    hist = np.histogram(img.ravel(), 256, [0, 256])
    cumsum = np.cumsum(hist[0])
    keypoint = factor*max(cumsum)
    greater = np.argmax(cumsum > keypoint)*np.ones(img.shape)
    newImg = np.minimum(img, greater).astype(np.uint8)
    return newImg

def watershedSeg(img):
    # from https://docs.opencv.org/master/d3/db4/tutorial_py_watershed.html
    thresh = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 35, 2)
    cv2.imwrite('C:\\Data\\ColorSeg\\STEP1.png', thresh)
    # noise removal
    kernel = np.ones((3, 3), np.uint8)
    opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=1)
    cv2.imwrite('C:\\Data\\ColorSeg\\STEP2.png', opening)
    # sure background area
    sure_bg = cv2.dilate(opening, kernel, iterations=1)
    cv2.imwrite('C:\\Data\\ColorSeg\\STEP3.png', sure_bg)
    # Finding sure foreground area
    dist_transform = cv2.distanceTransform(opening, cv2.DIST_L2, 5)
    cv2.imwrite('C:\\Data\\ColorSeg\\STEP4.png', cv2.equalizeHist(dist_transform.astype(np.uint8)))
    ret, sure_fg = cv2.threshold(dist_transform, 0.2 * dist_transform.max(), 255, 0)
    cv2.imwrite('C:\\Data\\ColorSeg\\STEP5.png', sure_fg)
    # Finding unknown region
    sure_fg = np.uint8(sure_fg)
    unknown = cv2.subtract(sure_bg, sure_fg)
    cv2.imwrite('C:\\Data\\ColorSeg\\STEP6.png', unknown)
    # Marker labelling
    ret, markers = cv2.connectedComponents(sure_fg)
    # Add one to all labels so that sure background is not 0, but 1
    cv2.imwrite('C:\\Data\\ColorSeg\\STEP7.png', markers)
    markers = markers + 1
    # Now, mark the region of unknown with zero
    colorimg = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
    markers[unknown == 255] = 0
    markers = cv2.watershed(colorimg, markers)
    colorimg[markers == -1] = [255, 0, 0]
    return colorimg


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Load an image and segment
    rawimg = cv2.cvtColor(cv2.imread('image/MintMark.png'), cv2.COLOR_BGR2GRAY)
    img = imageClamp(rawimg, 0.75)
    cv2.imwrite('image/CLAMPED.png', img)
    (ROWS, COLS) = img.shape
    print("Image shape is" + str(img.shape))
    watershedImg = watershedSeg(img)
    cv2.imwrite('image/WATERSHED.png', watershedImg)

    # smoothed = cv2.medianBlur(img, 3)
    smoothed = cv2.GaussianBlur(img, ksize=(0, 0), sigmaX=2.5)

    meanThrImg = cv2.adaptiveThreshold(smoothed, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 65, 2)
    cv2.imwrite('image/MeanThr.png', meanThrImg)

    gaussThrImg = cv2.adaptiveThreshold(smoothed, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 12, 2)
    cv2.imwrite('image/GaussThr.png', gaussThrImg)

    contours, hierarchy = cv2.findContours(gaussThrImg, 2, 2)
    contoursImg = gaussThrImg.copy()
    cont = np.zeros(gaussThrImg.shape)
    for c in contours:
        x = 1000
        y = 1200
        if cv2.contourArea(c) > x:
            if cv2.contourArea(c) < y:
                l,m,n,o = cv2.boundingRect(c)
                #cv2.drawContours(cont, [c], -1, (0, 0, 0), 2)
                cv2.drawContours(cont, [c], -1, (255, 255, 255), 6)

    cv2.imwrite('image/Contours.png', cont)