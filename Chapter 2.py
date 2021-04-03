# BASIC FUNCTIONS

import cv2
import numpy as np

img = cv2.imread("Resources/woman1.jpg")

# In the case of dialation case we have to define a kernel using numpy
# ones is used to set all values to one 
# in its parameter we give size of matrix and then we define the type of object
# which is unsigned integer of 8 bits that means values range from 0 to 255
kernel = np.ones((5,5), np.uint8)


# FUNCTIONS 

# Converting to GrayScale
# For this we will use cvtColor() function which is used to convert into various colors
# In the parameters first we have give to give the image which is to be converted
# and then in which color it has to be converted
# We use RGB but in Open CV the image convention is BGR 
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Creating Blurred image 
# For this we will use GaussianBlur() function
# in its parameters we have to give image then the kernel size(odd number), and then sigmax
imgBlur = cv2.GaussianBlur(imgGray, (7,7), 0)

# To find the edges in our image use an edge detector
# Here we have Canny edge Detector
# In its parameter we have to give image then 2 threshold values
# For simplicity both threshold are 100,100
imgCanny = cv2.Canny(img, 150, 200)

# While detecting edges sometimes there is a gap or because its not joined properly
# it does not detect it as a proper line so what we can do is increase the thickness of our edge
# So in order to that we used Dialation
# in its parameters we will give Canny Image and a kernel
# A kernel is just a matrix that we have to define the size of and value of
# So the matrix has values and size
# To deal with matrices we use the numpy Library
# After kernel we add How many iterations the kernel need to move around that means the thickness we need
# If we increase iterations the edges get more thicker
imgDialation = cv2.dilate(imgCanny, kernel, iterations=1)

# Now we will see the erosion which means we will decrease the thickness
# and make the edges thinner
# in its parameters we will give Dialation Image and a kernel
# A kernel is just a matrix that we have to define the size of and value of
# So the matrix has values and size
# To deal with matrices we use the numpy Library
# After kernel we add How many iterations the kernel need to move around that means the thinness we need
# If we increase iterations the edges get more thinner
imgEroded = cv2.erode(imgDialation, kernel, iterations=1)


cv2.imshow("Gray Image", imgGray)
cv2.imshow("Blurred Image", imgBlur)
cv2.imshow("Canny Image", imgCanny)
cv2.imshow("Dialation Image", imgDialation)
cv2.imshow("Eroded Image", imgEroded)

cv2.waitKey(0)