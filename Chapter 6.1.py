# JOINING IMAGES

import cv2
import numpy as np 

img = cv2.imread("Resources/woman1.jpg")

# For joining images we are using numpy library functions

# for horizontal join we use hstack function and in prameter we give the images to join
imgHor = np.hstack((img, img))
# for vertical join we use vstack function and in prameter we give the images to join 
imgVer = np.vstack((img, img))

# We can give any number of images to join

cv2.imshow("Horizontal Join", imgHor)
cv2.imshow("Vertical Join", imgVer)

cv2.waitKey(0)