import cv2
import numpy as np
from matplotlib import pyplot as plt

mean = cv2.imread("Image/MeanThr.png",0)
gauss = cv2.imread("Image/GaussThr.png",0)
cont = cv2.imread("image/Contours.png",0)
mint = cv2.imread("image/MintMark.png",0)
img2 = mean.copy()
img3 = gauss.copy()
img4 = mint.copy()
cont2 = cont.copy()
temp = cv2.imread("image/D.png",0)
temp2 = cv2.imread("image/D2.png",0)
tempP = cv2.imread("image/p.png",0)
temp3 = cv2.imread("image/P2.png",0)

w, h = temp.shape[::-1]
w2, h2 = tempP.shape[::-1]
methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
            'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']
string = ''
for meth in methods:
    img = img4.copy()
    method = eval(meth)

    # Apply template Matching
    res = cv2.matchTemplate(img,temp2,method)
    res2 = cv2.matchTemplate(img, temp3, method)
    if np.where(res > res2):
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        string = "D"
    else:
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res2)
        string = "P"
    # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)

    cv2.rectangle(img,top_left, bottom_right, 255, 2)

    plt.subplot(121),plt.imshow(res,cmap = 'gray')
    plt.title('Matching Result '+ string), plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(img,cmap = 'gray')
    plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
    plt.suptitle(meth)

    plt.show()