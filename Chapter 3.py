# RESIZING AND CROPPING

# In Mathematics convention x-axis is on right side and y-axis is on upper side
# In Open CV convention x-axis is on right side and y-axis is on downward side

import cv2
import numpy as np

img = cv2.imread("Resources/woman1.jpg")
# Prints the Size of Image....In this Case (640, 640, 3) -> (Height, Width, No. of channels whic is BGR)
print(img.shape)

# RESIZING

# For Resizing We will use resizing Function
# In Parameter we will give the image to be resized and the dimensions
# In Dimensions First the width and then height (width, height)
imgResize = cv2.resize(img, (300, 200))
print(imgResize.shape)

# CROPPING

# Since image is an array of pixels(matrix) so we can dirctly use the functionality of arrays(matrix functionality)
# No need to use the Open CV function
# In its parameter we have to give height first and then width
# and we have to give starting and ending point of our image (matrix)
imgCropped = img[0:200, 200:500]

cv2.imshow('Image', img)
cv2.imshow('Resized Image', imgResize)
cv2.imshow('Cropped Image', imgCropped)

cv2.waitKey(0)
