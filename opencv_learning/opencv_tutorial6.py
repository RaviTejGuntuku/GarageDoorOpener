import numpy as np
import cv2
import random

img = cv2.imread('opencv_assets/chessboard.png')
img = cv2.resize(img, (0, 0), fx=0.75, fy=0.75)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

corners = cv2.goodFeaturesToTrack(gray, 100, 0.01, 10)
corners = np.int0(corners)

print(corners)

for corner in corners:
    x, y = corner.ravel()
    cv2.circle(img, (x, y), 10, (255, 0, 0), -1)

for i in range(len(corners)):
    for j in range(i + 1, len(corners)):
        corner1 = tuple(corners[i][0])
        corner2 = tuple(corners[j][0])

        cv2.line(img, pt1=corner1, pt2=corner2, color=(random.randint(
            0, 255), random.randint(0, 255), random.randint(0, 255)), thickness=1)

cv2.imshow('Frame', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
