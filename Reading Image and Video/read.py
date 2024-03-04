# read the image

import cv2 as cv    # import the opencv module/ libray as cv2

img = cv.imread('Photo/2.jpg')    # read the image using cv.imread('folder/name.jpg') and save it in a variable
img1 = cv.imread('Photo/images1.webp')
img2 = cv.imread('Photo/images.jpeg')

cv.imshow("Eiffel Tower", img)   # to show the image using cv.imshow(variable)
cv.imshow("LINUX", img2)
cv.imshow("Lady Bird", img1)

# this the wait key function
cv.waitKey(0)
