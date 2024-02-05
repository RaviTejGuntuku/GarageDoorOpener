import cv2
import random

img = cv2.imread('opencv_assets/UTLogo.jpg', 1)
img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)
img = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)

for i in range(img.shape[0] // 3):
    for j in range(img.shape[1]):
        img[i][j] = [random.randint(0, 255), random.randint(0,
                                                            255), random.randint(0, 255)]

cv2.imshow('Image', img)

# print(img.shape)

cv2.imwrite('opencv_assets/new_UTLogo.jpg', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
