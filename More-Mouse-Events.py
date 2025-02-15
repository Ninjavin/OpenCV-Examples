from cv2 import cv2
import numpy as np

# events = [i for i in dir(cv2) if 'EVENT' in i]

# print(events)

def clickEvent(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        blue = img[x, y, 0]
        green = img[x, y, 1]
        red = img[x, y, 2]

        cv2.circle(img, (x, y), 3, (0, 0, 255), -1)
        mycolorImage = np.zeros((1024, 1024, 3), np.uint8)

        mycolorImage[:] = [blue, green, red]

        cv2.imshow('Color', mycolorImage)
    
# img = np.zeros([512, 512, 3], np.uint8)
img = cv2.imread('Screenshot (123).png')
cv2.imshow("Ninjavin", img)
points = []

cv2.setMouseCallback("Ninjavin", clickEvent)

cv2.waitKey(0)
cv2.destroyAllWindows()