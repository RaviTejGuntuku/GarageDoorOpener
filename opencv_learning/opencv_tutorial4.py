import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    width = int(cap.get(3))
    height = int(cap.get(4))

    radius = 100

    img = cv2.line(frame, (0, 0), (width, height), (255, 0, 0), 10)
    img = cv2.line(frame, (0, height), (width, 0), (0, 255, 0), 5)
    img = cv2.rectangle(img, (0, 0), (100, 100), (128, 128, 128), -1)
    img = cv2.circle(img, (width - radius, height - radius),
                     radius, (0, 0, 255), 4)
    img = cv2.putText(img, 'Tej is Great!', (50, height-30),
                      cv2.FONT_HERSHEY_SIMPLEX, 10, (0, 0, 0), 5, cv2.LINE_AA)

    cv2.imshow('frame', img)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
