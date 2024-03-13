# contour in opencv
# contour are used for shape recognition and object detection and recognition


import cv2 as cv
import numpy as np

img = cv.imread('Photo/images1.webp')

cv.imshow("IMG", img)

blank = np.zeros(img.shape, dtype='uint8')
cv.imshow("blank", blank)


# gray img

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

# blur

blur = cv.blur(gray, (5, 5), cv.BORDER_DEFAULT)
cv.imshow("Blur", blur)

# canny

canny = cv.Canny(blur, 125, 175,)
cv.imshow("Canny Edges", canny)


# Contour


# threshold
ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow("Thresh", thresh)

contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contour(s) found!')


cv.drawContours(blank, contours, -1, (0, 0, 255), 1)
cv.imshow("Contours blank", blank)

cv.waitKey(0)
