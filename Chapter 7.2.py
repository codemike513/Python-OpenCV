# COLOR DETECTION IN WEBCAM
# Same Process as our Color Detection in our Image Just we read the Webcam Video here instead of Image 

import cv2
import numpy as np

def empty(a):
    pass

def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver

cap = cv2.VideoCapture(0)

cv2.namedWindow('TrackBars')
cv2.resizeWindow('TrackBars', 640, 240)

cv2.createTrackbar('Hue Min', 'TrackBars', 102, 179, empty)
cv2.createTrackbar('Hue Max', 'TrackBars', 144, 179, empty)
cv2.createTrackbar('Saturation Min', 'TrackBars', 89, 255, empty)
cv2.createTrackbar('Saturation Max', 'TrackBars', 255, 255, empty)
cv2.createTrackbar('Value Min', 'TrackBars', 0, 255, empty)
cv2.createTrackbar('Value Max', 'TrackBars', 255, 255, empty)

while True:
    success, vid = cap.read()
    imageHSV = cv2.cvtColor(vid, cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos('Hue Min', 'TrackBars')
    h_max = cv2.getTrackbarPos('Hue Max', 'TrackBars')
    s_min = cv2.getTrackbarPos('Saturation Min', 'TrackBars')
    s_max = cv2.getTrackbarPos('Saturation Max', 'TrackBars')
    v_min = cv2.getTrackbarPos('Value Min', 'TrackBars')
    v_max = cv2.getTrackbarPos('Value Max', 'TrackBars')
    print(h_min, h_max, s_min, s_max, v_min, v_max)

    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    # Mask will filter out and give us the Filtered out image of that color
    mask = cv2.inRange(imageHSV, lower, upper)

    imgResult = cv2.bitwise_and(vid, vid, mask=mask)

    imgStack = stackImages(0.6, ([vid, imageHSV], [mask, imgResult]))

    # cv2.imshow('Original Image', img)
    # cv2.imshow('HSV Image', imageHSV)
    # cv2.imshow('Mask Image', mask)
    # cv2.imshow('Result Image', imgResult)

    cv2.imshow('Stacked Images', imgStack)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
