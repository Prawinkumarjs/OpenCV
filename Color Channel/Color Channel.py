import cv2 as cv
import numpy as np

img = cv.imread("Photo/2.jpg")
cv.imshow("Image", img)

blank = np.zeros(img.shape[:2], dtype="uint8")

b, g, r = cv.split(img)

blue = cv.merge([b, blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])


cv.imshow("blue", blue)
cv.imshow("red", red)
cv.imshow("green", green)
cv.imshow("blu", b)
cv.imshow("re", r)
cv.imshow("gree", g)

print(img.shape)
print(b.shape)
print(r.shape)
print(g.shape)

merged = cv.merge([b, g, r])
cv.imshow("Merged Image", merged)


cv.waitKey(0)
