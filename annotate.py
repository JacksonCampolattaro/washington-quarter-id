import cv2


file = "Data/mixed/1967.png"
img = cv2.imread(file)
txt = "1967"
height = int(img.shape[0]*.7)
width = int(img.shape[1]*.37)
print("dimensions read")
cv2.putText(img, txt, (width, height), cv2.FONT_HERSHEY_SIMPLEX, 18, (0, 255, 0), 5)
print("text placed")
cv2.imwrite("Image/1967_annotated.png", img)