from cv2 import cv2
import numpy as np

def nothing(x):
    print(x)

img = np.zeros((300, 512, 3), np.uint8)

cv2.namedWindow("Image")

cv2.createTrackbar('B', "Image", 0, 255, nothing)
cv2.createTrackbar('G', "Image", 0, 255, nothing)
cv2.createTrackbar('R', "Image", 0, 255, nothing)

while(1):
    cv2.imshow("Image", img)
    k = cv2.waitKey(1) & 0xFF
    if k==27:
        break

cv2.destroyAllWindows()
