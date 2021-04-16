# WARP PERSPECTIVE

# How to use warp perspective on an image to get its bird eye view

import cv2
import numpy as np

img  = cv2.imread("Resources/Card New.png") 

width, height = 250, 350

pts1 = np.float32([[164, 292],[377,257],[462,568],[218, 620]])
pts2 = np.float32([[0,0],[width, 0],[width, height],[0, height]])

matrix = cv2.getPerspectiveTransform(pts1, pts2)
imgOutput = cv2.warpPerspective(img, matrix, (width, height))


cv2.imshow("Image", img)
cv2.imshow("Output", imgOutput)


cv2.waitKey(0)