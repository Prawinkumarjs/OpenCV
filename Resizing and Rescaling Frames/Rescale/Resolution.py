# rescale the video
import cv2 as cv
def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1]*scale)                  # basically denote the width by frame.shape[1]*scale
    height = int(frame.shape[0]*scale)                # basically denote the height by frame.shape[0]*scale
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


# reading the video
def changeRes(width, height):
    # live video
    capture.set(3, width)
    capture.set(4, height)


capture = cv.VideoCapture(0)                        # for capture the video using webcam


while True:                                           # to run the program in loop to capture them all
    #                                                     frame by frame
    isTrue, frame = capture.read()                  # istrue is Boolean function used to run the loop for read capture
    frame_resized = rescaleFrame(frame)
    # frame_resized = rescaleFrame(frame, scale=.2)
    cv.imshow("Video", frame)          # to show the video  frame by frame
    cv.imshow("video resized", frame_resized)

    if cv.waitKey(20) & 0xFF == ord('d'):            # to terminate the loop
        break
capture.release()

# release the capture
cv.destroyAllWindows()                               # close all window
