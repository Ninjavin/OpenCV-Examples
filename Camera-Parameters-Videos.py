from cv2 import cv2

cap = cv2.VideoCapture(0)

cap.set(3, 600)
cap.set(4, 600)

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        cv2.imshow("Ninjavin", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
