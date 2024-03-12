# contour in opencv
# contour are used for shape recognition and object detection and recognition


import cv2 as cv

img = cv.imread('Photo/images1.webp')

cv.imshow("IMG", img)


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


cv.waitKey(0)
