# FACE DETECTION
# We will use the method given by VIOLA AND JONES for face detection

import cv2

faceCascade = cv2.CascadeClassifier("Resources/haarcascades/haarcascade_frontalface_default.xml")
img = cv2.imread('Resources/woman1.jpg')
imgNew = cv2.resize(img, (520,640))
imgGray = cv2.cvtColor(imgNew, cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(imgGray, scaleFactor=1.1, minNeighbors=4)

for (x,y,w,h) in faces:
    cv2.rectangle(imgNew,(x,y),(x+w, y+h),(255,0,0),2)


cv2.imshow('Original', imgNew)
cv2.waitKey(0)
