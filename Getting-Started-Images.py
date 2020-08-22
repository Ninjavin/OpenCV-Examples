from cv2 import cv2

img = cv2.imread("Screenshot (123).png", 1)

# print(img)

cv2.imshow("Screenshot", img)
k = cv2.waitKey(0) & 0xFF  # Whatever key is pressed its value stored in k

if k==27:
    cv2.destroyAllWindows()
elif k==ord('s'):
    cv2.imwrite("Screenshot-Copy.png", img)
    cv2.destroyAllWindows()