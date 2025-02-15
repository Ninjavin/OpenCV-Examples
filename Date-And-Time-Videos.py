from cv2 import cv2
import datetime

cap = cv2.VideoCapture(0)

cap.set(3, 1200)
cap.set(4, 1200)

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        font = cv2.FONT_HERSHEY_DUPLEX
        # text = 'Width: ' + str(cap.get(3)) + ' Height: ' + str(cap.get(4))
        date = str(datetime.datetime.now())
        frame = cv2.putText(frame, date, (10, 50), font, 1, (0, 255, 0), 2, cv2.LINE_AA)
        cv2.imshow("Ninjavin", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
