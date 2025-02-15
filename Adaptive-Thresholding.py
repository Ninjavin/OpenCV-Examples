# Threshold calculated for specific areas/regions of image

from cv2 import cv2

img = cv2.imread("sudoku-original.jpg", 0)
_, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
th3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

cv2.imshow("Image", img)
# cv2.imshow("Thresh", th1)
cv2.imshow("Mean", th2)
cv2.imshow("Gaussian", th3)

cv2.waitKey(0)
cv2.destroyAllWindows()