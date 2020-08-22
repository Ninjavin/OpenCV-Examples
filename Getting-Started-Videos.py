from cv2 import cv2

capture = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc('X', 'V', 'I', 'D')
out = cv2.VideoWriter('Output.avi', fourcc, 20.0, (640, 480))

while(capture.isOpened()):
    ret, frame = capture.read()
    if ret:
        # print(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
        # print(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
        out.write(frame)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow("Ninjavin", gray)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

capture.release()
out.release()
cv2.destroyAllWindows()