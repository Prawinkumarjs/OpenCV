# reading the video

import cv2 as cv
#                                                       cv.videocapture( )  used to capture or read the video
# capture = cv.VideoCapture(0)                        # for capture the video using webcam
capture = cv.VideoCapture('video/Tiger.mp4')          # for capture the video in the folder
capture1 = cv.VideoCapture('video/Fire.mp4')

while True:                                           # to run the program in loop to capture them all
    #                                                     frame by frame
    # isTrue, frame = capture.read()                  # istrue is Boolean function used to run the loop for read capture
    isTrue, frame = capture1.read()
    cv.imshow("Video",frame)                 # to show the video  frame by frame

    if cv.waitKey(20) & 0xFF == ord('d'):            # to terminate the loop
        break
capture.release()                                    # release the capture
cv.destroyAllWindows()                               # close all window
