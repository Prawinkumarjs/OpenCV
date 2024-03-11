# image transformation

import cv2 as cv
import numpy as np

img = cv.imread("Photo/images.jpeg")

cv.imshow("IMG", img)

# Translation


def translate(img, x, y):
    transMat = np.float32([[1, 0, x], [0, 1, y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

# -x--> left
# -y--> up
# y-->  right
# x-->  down


translated = translate(img, 100, 100)
cv.imshow("Translated", translated)


# rotation


def rotate(img, angle, rotPoint = None):
    (height,width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2, height//2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)

    return cv.warpAffine(img, rotMat, dimensions)


rotated = rotate(img, 60)
cv.imshow("Rotated", rotated)
rotated_r = rotate(rotated, 90)
cv.imshow("Rotate", rotated_r)


# resizing

resized = cv.resize(img,(500,500), interpolation=cv.INTER_CUBIC)
cv.imshow("RESIZE", resized)


# flipping

flip0 = cv.flip(img, -1)
flip = cv.flip(img, 0)
flip1 = cv.flip(img, 1)
cv.imshow("FLIP", flip)
cv.imshow("Flip", flip1)
cv.imshow("Flip1", flip0)


# cropping


# cropped = img[200: 400, 300: 400]
# cv.imshow("Cropped", cropped)

cv.waitKey(0)
