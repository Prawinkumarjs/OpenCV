# draw in the picture

import cv2 as cv
import numpy as np

blank = np.zeros((500, 900, 3), dtype='uint8')
cv.imshow("Blank", blank)


img = cv.imread("Photo/Bike.webp")
cv.imshow("Honda", img)

# 1. Paint the img a certain color

# blank[:] = 0, 255, 0
# blank[200:300, 300:400] = 0, 255, 0

# blank[:} = 0, 0, 255    # for red color
# cv.imshow("green", blank)

# 2. draw a rectangle
cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0, 255, 0), thickness=-1)
cv.imshow('rectangle', blank)
# 3. draw circle
cv.circle(blank,  (blank.shape[1]//2, blank.shape[0]//2), 40,  (0, 0,  255), thickness=3)
cv.imshow("Circle", blank)

# 4. Draw a line
cv.line(blank, (100, 250), (blank.shape[1]//2, blank.shape[0]//2), (255, 255, 255), thickness=3)
cv.imshow('line', blank)
# 5. write a text on image
cv.putText(blank, 'Hello, My Name is PRAWIN KUMAR', (300,300), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0, 255,0), 2)
cv.imshow("Text", blank)



cv.waitKey(0)
