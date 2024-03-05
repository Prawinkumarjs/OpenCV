# resize the image

import cv2 as cv

img = cv.imread('Photo/images1.webp')
cv.imshow("LINUX", img)

def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1]*scale)                  # basically denote the width by frame.shape[1]*scale
    height = int(frame.shape[0]*scale)                # basically denote the height by frame.shape[0]*scale
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


frame_resized = rescaleFrame(img)
cv.imshow("img", frame_resized)
cv.waitKey(0)
