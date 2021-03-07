import cv2
import math
import numpy as np

img = cv2.imread('Image/Dilation.png',0)
img1 = cv2.imread('Image/line.png',0)
img2 = cv2.imread('Image/2.jpg',0)
rect = cv2.imread('Image/Rectangle.png',0)
diff = cv2.imread('Image/D.png',0)
pint = cv2.imread('Image/P.png',0)


ret, thresh = cv2.threshold(img, 127, 255,0)
ret, thresh2 = cv2.threshold(img2, 127, 255,0)
ret, thresh3 = cv2.threshold(pint, 127, 255,0)
ret, thresh4 = cv2.threshold(diff, 127, 255,0)

cv2.imwrite('Image/thresh.png', thresh)
cont = np.zeros(thresh.shape)
contours,hierarchy = cv2.findContours(thresh,2,1)

cnt1 = contours[0]
cnta = contours[1]
cv2.drawContours(cont, cnt1, -1, (255, 255, 255), -1)
cv2.drawContours(cont, cnta, -1, (255, 255, 255), -1)
cv2.imwrite('image/C1.png', cont)

cont = np.zeros(thresh2.shape)
contours,hierarchy = cv2.findContours(thresh2,2,1)
cnt2 = contours[3]
cntb = contours[2]
cv2.drawContours(cont, cnt2, -1, (255, 255, 255), -1)
cv2.drawContours(cont, cntb, -1, (255, 255, 255), -1)
cv2.imwrite('image/C2.png', cont)

contours,hierarchy = cv2.findContours(thresh3,2,1)
cnt3 = contours[3]
cntc = contours[2]
cont = np.zeros(thresh3.shape)
cv2.drawContours(cont, cnt3, -1, (255, 255, 255), -1)
cv2.drawContours(cont, cntc, -1, (255, 255, 255), -1)
cv2.imwrite('image/C3.png', cont)

contours,hierarchy = cv2.findContours(thresh4,2,1)
cnt4 = contours[3]
cntd = contours[2]
cont = np.zeros(thresh4.shape)
cv2.drawContours(cont, cnt4, -1, (255, 255, 255), -1)
cv2.drawContours(cont, cntd, -1, (255, 255, 255), -1)
cv2.imwrite('image/C4.png', cont)

r = cv2.matchShapes(cnt1,cnt2,3,0.0)

d = (cv2.matchShapes(cnt1,cnt3,3,0.0) + cv2.matchShapes(cnta,cntc,3,0.0))/2
p = (cv2.matchShapes(cnt1,cnt4,3,0.0) + cv2.matchShapes(cnta,cntd,3,0.0))/2
#test = cv2.matchShapes(cnt2,cnt4,3,0.0)

print(r)
print(d)
print(p)
#print(test)

if r == min(r,d,p):
    print('its a 2')
if d == min(r,d,p):
    print('its a p')
if p == min(r,d,p):
    print('its a d')


