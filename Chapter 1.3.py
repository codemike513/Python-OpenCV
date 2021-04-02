# READ IMAGES - VIDEO - WEBCAM
# 1.3 -> READ WEBCAM

import cv2

# For Reading WebCam we have to create a VideCapture Object
# In its parameter we use 0 for default WebCam
# if we have more than 1 webcam we use its id 0 or 1 etc...
cap = cv2.VideoCapture(0)

# Now to set its width and height

cap.set(3, 640)    # Id 3 for width
cap.set(4, 480)    # Id 4 for height
# Change the brightness
cap.set(10, 100)

# Since Video is a Sequence of images we have to use a loop for display
while True:
    success, img = cap.read()    # The success variable is boolean type it captures the image if true
    cv2.imshow("Video", img)
    # Now we add a delay and wait for 'q' press to break the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break