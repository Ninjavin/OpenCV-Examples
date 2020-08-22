import numpy as np
from cv2 import cv2

# img = cv2.imread("Screenshot (123).png", 1)

img = np.zeros([512, 512, 3], np.uint8)

img = cv2.line(img, (350,350), (700, 350), (90, 15, 50), 10)
img = cv2.arrowedLine(img, (700, 350), (1050, 350), (50,15,90), 10)

img = cv2.rectangle(img, (350, 355), (700, 700), (150,0,135), -1)

img = cv2.circle(img, (500, 500), 100, (150, 0, 135), -1)
font = cv2.FONT_HERSHEY_SIMPLEX
img = cv2.putText(img, "OpenCV", (500, 350), font, 3, (255, 0, 130), 5, cv2.LINE_AA)

cv2.imshow('Screenshot', img)

cv2.waitKey(0)
cv2.destroyAllWindows()