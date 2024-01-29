import cv2

img = cv2.imread("Mihir1.jpeg")
# img = cv2.imread("Camera.jpg")
cv2.imshow("Original", img)

# res = cv2.xphoto.oilPainting(img, 7, 1)
# oilPaint = cv2.resize(res, (970, 545))
# cv2.imshow("Oil Painting", oilPaint)

res1 = cv2.stylization(img, sigma_s=60, sigma_r=0.6)
# waterColour = cv2.resize(res1, (970, 545))
cv2.imshow("Water Coloured", res1)

dst_gray, dst_color = cv2.pencilSketch(img, sigma_s=60, sigma_r=0.07, shade_factor=0.05)
cv2.imshow("Wa", dst_color)
cv2.imshow("red", dst_gray)

cv2.waitKey(0)
cv2.destroyAllWindows()
