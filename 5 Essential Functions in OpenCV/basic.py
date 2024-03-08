# 5 Essential Functions in OpenCV

import cv2 as cv

img = cv.imread('Photo/2.jpg')
img1 = cv.imread('Photo/images1.webp')

cv.imshow('Eiffel Tower', img)
cv.imshow("Lady Bird", img1)

# converting to grayscale

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)          # it converts the color img into grayscale image
gray1 = cv.cvtColor(img1, cv.COLOR_BGR2GRAY)

cv.imshow(' Gray Eiffel Tower', gray)
cv.imshow("Gray Lady Bird", gray1)

# blur an image

blur = cv.GaussianBlur(img, (3, 3), cv.BORDER_DEFAULT)       # it converts the color img into blur image
blur1 = cv.GaussianBlur(img1, (9, 9), cv.BORDER_DEFAULT)

cv.imshow("Blur Eiffel Tower", blur)
cv.imshow("Blur Lady Bird", blur1)

# edge cascade

canny = cv.Canny(img, 125, 175)                      # it converts the color image into canny image
canny1 = cv.Canny(img1, 100, 175)
Canny = cv.Canny(blur, 125, 175)                     # it converts the blur image into canny image
Canny1 = cv.Canny(blur1, 100, 175)


cv.imshow("Canny Eiffel Tower", canny)
cv.imshow("Canny Lady Bird", canny1)
cv.imshow("Canny EiffelTower", Canny)
cv.imshow("Canny LadyBird", Canny1)

# dilating the image

dilated = cv.dilate(Canny, (7, 7), iterations=3)
cv.imshow("Dilated", dilated)

# Eroding
eroded = cv.erode(dilated, (3,3), iterations=1)
cv.imshow("Eroded", eroded)

# resize
resize = cv.resize(img, (500, 500), interpolation=cv.INTER_AREA)
cv.imshow("Resized", resize)

# cropping
cropped = img[50:200, 200:400]
cv.imshow("Crop", cropped)


cv.waitKey(0)
