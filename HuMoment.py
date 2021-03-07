import cv2
import math

img = cv2.imread('Image/Dilation.png',0)
img1 = cv2.imread('Image/line.png',0)
img2 = cv2.imread('Image/2.jpg',0)
rect = cv2.imread('Image/Rectangle.png',0)
diff = cv2.imread('Image/D.png',0)
pint = cv2.imread('Image/P.png',0)


ret, thresh = cv2.threshold(img, 127, 255,0)
ret, thresh2 = cv2.threshold(rect, 127, 255,0)
ret, thresh3 = cv2.threshold(img2, 127, 255,0)
ret, thresh4 = cv2.threshold(diff, 127, 255,0)

cv2.imwrite('Image/thresh.png', thresh)

contours,hierarchy = cv2.findContours(thresh,2,1)
cnt1 = contours[0]
contours,hierarchy = cv2.findContours(thresh2,2,1)
cnt2 = contours[0]
contours,hierarchy = cv2.findContours(thresh3,2,1)
cnt3 = contours[0]
contours,hierarchy = cv2.findContours(thresh4,2,1)
cnt4 = contours[0]

r = cv2.matchShapes(cnt1,cnt2,3,0.0)
d = cv2.matchShapes(cnt1,cnt3,3,0.0)
p = cv2.matchShapes(cnt1,cnt4,3,0.0)
#test = cv2.matchShapes(cnt2,cnt4,3,0.0)

print(r)
print(d)
print(p)
#print(test)

if ret == min(r,d,p):
    print('its a 1')
if d == min(r,d,p):
    print('its a 2')
if p == min(r,d,p):
    print('its a d')


