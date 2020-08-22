from cv2 import cv2
import numpy as np

img1 = np.zeros((500, 500, 3), np.uint8)
img1 = cv2.rectangle(img1, (150, 0), (350, 250), (255, 0, 255), -1)
img2 = cv2.imread("reddit-alien-png-3.png")
img2 = cv2.resize(img2, (500, 500))

bitAnd = cv2.bitwise_and(img2, img1)
bitOr = cv2.bitwise_or(img2, img1)
bitNot1 = cv2.bitwise_not(img2)
bitNot2 = cv2.bitwise_not(img1)
bitXor = cv2.bitwise_xor(img2, img1)

# cv2.imshow("img1", img1)
# cv2.imshow("img2", img2)
cv2.imshow("And", bitAnd)
cv2.imshow("Or", bitOr)
cv2.imshow("Not", bitNot1)
cv2.imshow("Not2", bitNot2)
cv2.imshow("Xor", bitXor)

cv2.waitKey(0)
cv2.destroyAllWindows()