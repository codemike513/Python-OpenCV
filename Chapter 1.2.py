# READ IMAGES - VIDEO - WEBCAM
# 1.2 -> READ VIDEO

import cv2

# For Reading Video we have to create a VideCapture Object in its parameter we give the path of video
# cap = cv2.VideoCapture("Video Location")
cap = cv2.VideoCapture("Resources/abc.mp4")

# Since Video is a Sequence of images we have to use a loop for display
while True:
    # The success variable is boolean type it captures the image if true
    success, img = cap.read()
    cv2.imshow("Video", img)
    # Now we add a delay and wait for 'q' press to break the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
