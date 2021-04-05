# SHAPES AND TEXTS 

import cv2 
import numpy as np

# Now we will create a matrix filled with zeroes using Numpy Library
# Zeroes means black

# img = np.zeros((512, 512))   # size of matrix in parameter......(512, 512) means GrayScale Image
img = np.zeros((512, 512, 3), np.uint8)   # size of matrix in parameter   (512, 512, 3) means Coloured Image

# print(img.shape)   # Print Shape of Image
# img[:] = 255, 0, 0   # For Background Color for full image
# img[100:300, 200:400] = 255, 0, 0   # For Background Color with particular size area


# DRAWING SHAPES ON IMAGE

# DRAWING A LINE 

# We use line function with parameters 
# First the image on which to Draw then the starting Point dimensions and then Ending Point Dimensions
# then the colour of line and then the thickness 
# line(image, start point, end point, color, thickness)
# Start Point and End Point have Priority as (width, height)
cv2.line(img, (0,0), (300,200), (0, 255, 0), 3)

# In this if we want the end point till last so we use the shape of image as index [1] for Width and index [0] for Height
cv2.line(img, (0,0), (img.shape[1], img.shape[0]), (255, 0, 255), 3)



# DRAWING A RECTANGLE 

# We use rectangle function with parameters 
# First the image on which to Draw then the starting Point dimensions and then Ending Point Dimensions
# then the colour of line and then the thickness 
# line(image, start point, end point, color, thickness)
# Start Point and End Point have Priority as (width, height)

cv2.rectangle(img, (0,0), (250, 350), (0, 0 , 255), 2)

# In this if we have to fill the whole rectangle so we have to remove the thickness and use function cv2.FILLED
cv2.rectangle(img, (0,450), (430, 500), (0, 255, 255), cv2.FILLED)



# DRAWING A CIRCLE 

# We use circle function with parameters 
# First the image on which to Draw then the Position where to Form Circle 
# then the Radius of The Circle 
# then the colour of line and then the thickness 
# line(image, Position, Radius, color, thickness)
# Start Point and End Point have Priority as (width, height)
cv2.circle(img, (450,50), 30, (255, 255, 0), 5)



# WRITING TEXT ON IMAGE 

# We use putText function with parameters 
# First the image on which Text is to be Written
# Then the Text in String and then the Position where to Display Text 
# then the Font of the Text using cv2 module (pre defined Fonts) 
# then the Scale of the Text (Big or Small)
# then the colour of Text and then the thickness 
# line(image, Text To Display, Position, Font Style, Scale, color, thickness)
cv2.putText(img, "HELLO", (320,200), cv2.FONT_HERSHEY_COMPLEX, 0.9, (175, 131, 237), 2)


cv2.imshow("Image", img)

cv2.waitKey(0)