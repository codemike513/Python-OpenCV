# CHAPTER 1 -> READ IMAGES - VIDEO - WEBCAM
# 1.1 -> READ IMAGES

import cv2

# For reading the image we use imread() function and in its parameter we give the path of image
# img = cv2.imread("Image Location")
img = cv2.imread("Resources/woman1.jpg")

# To display our image we have function imshow() and in this we have to give 2 parameters 1-> Name of Window 2-> The image to be displayed
cv2.imshow("Output", img)

# For delay we have to use function waitkey()
# In the parameter if we put 0 then its infinite delay
# and if we use 1 that means 1 milisecond delay
# and 1000 mean 1 sec delay
cv2.waitKey(0)