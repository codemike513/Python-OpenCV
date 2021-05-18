# COLOR DETECTION IN IMAGE

import cv2
import numpy as np

# Just an empty Function to use in creating TrackBars
def empty(a):
    pass

# Stack image function used in previous chapter to join images horizontally as well as vertically
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

# Path of our Image
path = 'Resources/woman1.jpg'

# We do not know the actual range of color which we have to detect so we use the concept of TrackBars to work with values in real time
# So we created a window named TrackBars with its size
cv2.namedWindow('TrackBars')
cv2.resizeWindow('TrackBars', 640, 240)

# Now we are creeating TrackBar with createTrackbar() function
# in its parameters we have to specify (for what the trackbar is, the name of window(same name), min range, max range, a function(we have used empty here))
# We have created trackbars for hue, saturation and value with max and min
# Minimum and Maximum range for HUE -> 0 and 179 resp (for hue max is 360 but here in open CV its 179)
# Minimum and Maximum range for Saturation -> 0 and 255 resp
# Minimum and Maximum range for Value -> 0 and 255 resp
# Here we have written the minimum range of our image after our trial for execution
cv2.createTrackbar('Hue Min', 'TrackBars', 102, 179, empty)
cv2.createTrackbar('Hue Max', 'TrackBars', 144, 179, empty)
cv2.createTrackbar('Saturation Min', 'TrackBars', 89, 255, empty)
cv2.createTrackbar('Saturation Max', 'TrackBars', 255, 255, empty)
cv2.createTrackbar('Value Min', 'TrackBars', 0, 255, empty)
cv2.createTrackbar('Value Max', 'TrackBars', 255, 255, empty)

while True:
    # Reading the image 
    img = cv2.imread(path)
    # Changing image to HSV 
    imageHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Now here we are printing our Trackbar Values
    # We used getTrackbarPos() function to get our Trackbar values 
    # in its parameter we have to give the same name of what tracbar is for and the same name of our window
    h_min = cv2.getTrackbarPos('Hue Min', 'TrackBars')
    h_max = cv2.getTrackbarPos('Hue Max', 'TrackBars')
    s_min = cv2.getTrackbarPos('Saturation Min', 'TrackBars')
    s_max = cv2.getTrackbarPos('Saturation Max', 'TrackBars')
    v_min = cv2.getTrackbarPos('Value Min', 'TrackBars')
    v_max = cv2.getTrackbarPos('Value Max', 'TrackBars')
    print(h_min, h_max, s_min, s_max, v_min, v_max)

    # Now we are creating mask using array by use of numpy library 
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    # Mask will filter out and give us the Filtered out image of that color
    mask = cv2.inRange(imageHSV, lower, upper)

    # To get the original color on the mask we use bitwise_and function 
    # The and function checks the same pixels in 2 images and then gives the value 1 and gives the color on the required mask
    # In its parameter we give the original image and our mask 
    imgResult = cv2.bitwise_and(img, img, mask=mask)

    # ******* Here our required Color is Detected *******

    # Here we used the stackImages function to join our all images 
    imgStack = stackImages(0.6, ([img, imageHSV], [mask, imgResult]))

    # cv2.imshow('Original Image', img)
    # cv2.imshow('HSV Image', imageHSV)
    # cv2.imshow('Mask Image', mask)
    # cv2.imshow('Result Image', imgResult)

    cv2.imshow('Stacked Images', imgStack)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
