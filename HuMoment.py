import cv2
import math
import numpy as np
from PIL import Image
#def huMoment(image, mode):
#image = input image path
#mode = 0 if date 1 if mint mark
image = 'Image/Dilation.png'
mode = 0
img = cv2.imread(image,0)
img0 = cv2.imread('Image/0.jpg',0)
img1 = cv2.imread('Image/1.jpg',0)
img2 = cv2.imread('Image/2.jpg',0)
img3 = cv2.imread('Image/3.jpg',0)
img4 = cv2.imread('Image/4.jpg',0)
img5 = cv2.imread('Image/5.jpg',0)
img6 = cv2.imread('Image/6.jpg',0)
img7 = cv2.imread('Image/7.jpg',0)
img8 = cv2.imread('Image/8.jpg',0)
img9 = cv2.imread('Image/9.jpg',0)
rect = cv2.imread('Image/Rectangle.png',0)
diff = cv2.imread('Image/D.png',0)
pint = cv2.imread('Image/P.png',0)
#preprocess the templates
ret, thresh = cv2.threshold(img, 127, 255,0)
ret, thresh1 = cv2.threshold(img1, 127, 255,0)#      rect works much better than img1
ret, thresh2 = cv2.threshold(img2, 127, 255,0)
ret, thresh3 = cv2.threshold(img3, 127, 255,0)
ret, thresh4 = cv2.threshold(img4, 127, 255,0)
ret, thresh5 = cv2.threshold(img5, 127, 255,0)
ret, thresh6 = cv2.threshold(img6, 127, 255,0)
ret, thresh7 = cv2.threshold(img7, 127, 255,0)
ret, thresh8 = cv2.threshold(img8, 127, 255,0)
ret, thresh9 = cv2.threshold(img9, 127, 255,0)
ret, thresh0 = cv2.threshold(img0, 127, 255,0)
ret, threshp = cv2.threshold(pint, 127, 255,0)
ret, threshd = cv2.threshold(diff, 127, 255,0)
#default assignment
one = two = three = four = five = six = seven = eight = nine = zero = p = d = 100

#input image
cv2.imwrite('Image/thresh.png', thresh)
cont = np.zeros(thresh.shape)
contours,hierarchy = cv2.findContours(thresh,2,1)
x = 0
cnt0 = contours[0]
cv2.drawContours(cont, cnt0, -1, (255, 255, 255), -1)
try:
    contours[1]
except IndexError:
    x = 1
else:
    x = 2
    cnta = contours[1]
    cv2.drawContours(cont, cnta, -1, (255, 255, 255), -1)
cv2.imwrite('image/C0.png', cont)

#number templates
if mode == 0:
    #1
    contours, hierarchy = cv2.findContours(thresh1, 2, 1)
    cnt1 = contours[0]
    cont = np.zeros(thresh1.shape)
    cv2.drawContours(cont, cnt1, -1, (255, 255, 255), -1)
    cv2.imwrite('image/C1.png', cont)
    #2
    cont = np.zeros(thresh2.shape)
    contours,hierarchy = cv2.findContours(thresh2,2,1)
    cnt2 = contours[0]
    cv2.drawContours(cont, cnt2, -1, (255, 255, 255), -1)
    #cv2.drawContours(cont, cntb, -1, (255, 255, 255), -1)
    cv2.imwrite('image/C2.png', cont)

    #3
    contours,hierarchy = cv2.findContours(thresh3,2,1)
    cnt3 = contours[0]
    cont = np.zeros(thresh3.shape)
    cv2.drawContours(cont, cnt3, -1, (255, 255, 255), -1)
    cv2.imwrite('image/C3.png', cont)
    #4
    contours,hierarchy = cv2.findContours(thresh4,2,1)
    cnt4 = contours[0]
    cntf = contours[1]
    cont = np.zeros(thresh4.shape)
    cv2.drawContours(cont, cnt4, -1, (255, 255, 255), -1)
    cv2.drawContours(cont, cntf, -1, (255, 255, 255), -1)
    cv2.imwrite('image/C4.png', cont)
    #5
    contours,hierarchy = cv2.findContours(thresh5,2,1)
    cnt5 = contours[0]
    cont = np.zeros(thresh5.shape)
    cv2.drawContours(cont, cnt5, -1, (255, 255, 255), -1)
    cv2.imwrite('image/C5.png', cont)
    #6
    contours,hierarchy = cv2.findContours(thresh6,2,1)
    cnt6 = contours[0]
    cntg = contours[1]
    cont = np.zeros(thresh6.shape)
    cv2.drawContours(cont, cnt6, -1, (255, 255, 255), -1)
    cv2.drawContours(cont, cntg, -1, (255, 255, 255), -1)
    cv2.imwrite('image/C6.png', cont)
    #7
    contours,hierarchy = cv2.findContours(thresh7,2,1)
    cnt7 = contours[0]
    cont = np.zeros(thresh7.shape)
    cv2.drawContours(cont, cnt7, -1, (255, 255, 255), -1)
    cv2.imwrite('image/C7.png', cont)
    #8
    contours,hierarchy = cv2.findContours(thresh8,2,1)
    cnt8 = contours[0]
    cnth = contours[1]
    cnti = contours[2]
    cont = np.zeros(thresh8.shape)
    cv2.drawContours(cont, cnt8, -1, (255, 255, 255), -1)
    cv2.drawContours(cont, cnth, -1, (255, 255, 255), -1)
    cv2.drawContours(cont, cnti, -1, (255, 255, 255), -1)
    cv2.imwrite('image/C8.png', cont)
    #9
    contours,hierarchy = cv2.findContours(thresh9,2,1)
    cnt9 = contours[0]
    cntj = contours[1]
    cont = np.zeros(thresh9.shape)
    cv2.drawContours(cont, cnt9, -1, (255, 255, 255), -1)
    cv2.drawContours(cont, cntj, -1, (255, 255, 255), -1)
    cv2.imwrite('image/C9.png', cont)
    #0
    contours, hierarchy = cv2.findContours(thresh0, 2, 1)
    cnt10 = contours[0]
    cntk = contours[1]
    cont = np.zeros(thresh0.shape)
    cv2.drawContours(cont, cnt10, -1, (255, 255, 255), -1)
    cv2.drawContours(cont, cntk, -1, (255, 255, 255), -1)
    cv2.imwrite('image/C10.png', cont)
    # testing number of contours found off the input image
    if x == 1:
        one = cv2.matchShapes(cnt0, cnt1, 3, 0.0)-.005
        two = cv2.matchShapes(cnt0, cnt2, 3, 0.0)
        three = cv2.matchShapes(cnt0, cnt3, 3, 0.0)
        four = cv2.matchShapes(cnt0, cnt4, 3, 0.0)
        five = cv2.matchShapes(cnt0, cnt5, 3, 0.0)
        six = cv2.matchShapes(cnt0, cnt6, 3, 0.0)
        seven = cv2.matchShapes(cnt0, cnt7, 3, 0.0)
        eight = cv2.matchShapes(cnt0, cnt8, 3, 0.0)
        nine = cv2.matchShapes(cnt0, cnt9, 3, 0.0)
        zero = cv2.matchShapes(cnt0, cnt10, 3, 0.0)
    if x == 2:
        four = (cv2.matchShapes(cnt0, cnt4, 3, 0.0)  + cv2.matchShapes(cnta,cntf,3,0.0))/2
        six = (cv2.matchShapes(cnt0, cnt6, 3, 0.0)  + cv2.matchShapes(cnta,cntg,3,0.0))/2
        eight = (cv2.matchShapes(cnt0, cnt8, 3, 0.0)  + cv2.matchShapes(cnta,cnth,3,0.0))/2
        nine = (cv2.matchShapes(cnt0, cnt9, 3, 0.0)  + cv2.matchShapes(cnta,cntj,3,0.0))/2
        zero = (cv2.matchShapes(cnt0, cnt10, 3, 0.0)  + cv2.matchShapes(cnta,cntk,3,0.0))/2
#Letters for the mint mark
if mode == 1:
    #P
    contours,hierarchy = cv2.findContours(threshp,2,1)
    cntp = contours[3]
    cntc = contours[2]
    cont = np.zeros(thresh3.shape)
    cv2.drawContours(cont, cntp, -1, (255, 255, 255), -1)
    cv2.drawContours(cont, cntc, -1, (255, 255, 255), -1)
    cv2.imwrite('image/CP.png', cont)
    #D
    contours,hierarchy = cv2.findContours(threshd,2,1)
    cnte = contours[3]
    cntd = contours[2]
    cont = np.zeros(threshd.shape)
    cv2.drawContours(cont, cnte, -1, (255, 255, 255), -1)
    cv2.drawContours(cont, cntd, -1, (255, 255, 255), -1)
    cv2.imwrite('image/CD.png', cont)

    if x == 2:
        p = (cv2.matchShapes(cnt0, cntp, 3, 0.0)  + cv2.matchShapes(cnta,cntc,3,0.0))/2
        d = (cv2.matchShapes(cnt0, cnte, 3, 0.0)  + cv2.matchShapes(cnta,cntd,3,0.0))/2

    else:
        p = cv2.matchShapes(cnt0, cntp, 3, 0.0)
        d = cv2.matchShapes(cnt0, cnte, 3, 0.0)


#confirm output
z = [one,two,three,four,five,six,seven,eight,nine,zero,d,p]
a = 0
b = min(z)
c = 1 - b
y = 0
while z[y] != b:
    y = y+1
a = y+1
if a == 10:
    a = 0
if a == 11:
    a = 'p'
if a == 12:
    a = 'd'
print(z)
print(a)
print(c)
#return a,c

