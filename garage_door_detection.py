import cv2
from numpy import *

imgFile = 'garage_current_image.jpg'

img = cv2.imread(imgFile)
height, width, channels = img.shape
mask = zeros((height+2, width+2), uint8)

start_pixel = (360, 200)
diff = (5, 5, 5)

retval, rect, rect2, _ = cv2.floodFill(
    img, mask, start_pixel, (0, 255, 0), diff, diff)

print(retval)

if retval > 50000:
    print(imgFile + ": garage door open")
else:
    print(imgFile + ": garage door closed")

cv2.imwrite(imgFile.replace(".jpg", "") + "_result.jpg", img)

# print("Width: ", w)
# print("Height: ", h)

# img = cv2.circle(img, center=(360, 200), radius=5,
#                  color=(255, 0, 0), thickness=-1)

# cv2.imshow('Image', img)

# cv2.waitKey(0)
# cv2.destroyAllWindows()
