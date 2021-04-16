# JOINING VIDEOS

import cv2
import numpy as np 

cap = cv2.VideoCapture(0)

while True:
    success, vid = cap.read()
    Hor = np.hstack((vid, vid))
    Ver = np.vstack((vid, vid))
    cv2.imshow("Horizontal Video", Hor)
    cv2.imshow("Vertical Video", Ver)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break