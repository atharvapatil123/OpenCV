# Contours: The curve joining all the continuous points along the boundary which are having the same color or intensity
# Shape analysis, object detction eyt

import cv2
import numpy as np

img =  cv2.imread('data/opencv-logo-white.png')
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(imgray, 20, 255, 0)
# ret, thresh = cv2.threshold(imgray, 127, 255, 0)

# threshold must be applied with proper value

contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)#(threshold, contour retrieval mode, method to be applied: Contour approx. method : If you pass cv.CHAIN_APPROX_NONE, all the boundary points are stored. But actually do we need all the points? For eg, you found the contour of a straight line. Do you need all the points on the line to represent that line? No, we need just two end points of that line. This is what cv.CHAIN_APPROX_SIMPLE does. It removes all redundant points and compresses the contour, thereby saving memory.)

#Here, CONTOURS: It is a python list of all contours in the image. Each individual contour is a numpy array of (x,y) coordinates of boundaary points of the object. 

# Hierarchy is an additional value

print("No of contours = " + str(len(contours)))

print(contours[0])

cv2.drawContours(img, contours, -1, (0,255,255), 3)#(original image, contours, contours indexes: -1 for all contours, color, thickness)
# cv2.drawContours(img, contours, 11, (0,255,255), 3)
#Gives contour only for 11th index!

cv2.imshow('Thresh', thresh)
cv2.imshow('Image', img)
cv2.imshow("Image Gray",imgray)
cv2.waitKey(0)
cv2.destroyAllWindows()