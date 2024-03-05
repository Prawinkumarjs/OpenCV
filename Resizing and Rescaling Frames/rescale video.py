# rescale the video
import cv2 as cv

# img = cv.imread('Photo/images1.webp')
# cv.imshow("LINUX", img)

def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1]*scale)                  # basically denote the width by frame.shape[1]*scale
    height = int(frame.shape[0]*scale)                # basically denote the height by frame.shape[0]*scale
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


# reading the video


#                                                       cv.videocapture( )  used to capture or read the video
capture = cv.VideoCapture(0)                        # for capture the video using webcam
# capture = cv.VideoCapture('video/Tiger.mp4')          # for capture the video in the folder
# capture1 = cv.VideoCapture('video/Fire.mp4')

while True:                                           # to run the program in loop to capture them all
    #                                                     frame by frame
    isTrue, frame = capture.read()                  # istrue is Boolean function used to run the loop for read capture
    # isTrue, frame = capture1.read()
    frame_resized = rescaleFrame(frame)
    # frame_resized = rescaleFrame(frame, scale=.2)
    cv.imshow("Video", frame)          # to show the video  frame by frame
    cv.imshow("video resized", frame_resized)

    if cv.waitKey(20) & 0xFF == ord('d'):            # to terminate the loop
        break
capture.release()
# capture1.release()

# release the capture
cv.destroyAllWindows()                               # close all window
