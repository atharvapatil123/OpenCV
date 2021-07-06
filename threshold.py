# It is a segnmentation tech used for separating an object from its backgroud. Comparing each pixel of an image with a fixed threshold value, yields in 2 parts: one with intensity less than or equal to threshold and second greater than threshold .

import cv2 
import numpy as np

# img = cv2.imread('data\gradient.png',0)
img = cv2.imread('data\sudoku.png',0)

_, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)#(source :COMPULASARILY GRAY-SCALE IMAGE, threshold_min, max_pixel, threshold_type)

_, th2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
_, th3 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
_, th4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
_, th5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)


th6 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)#(source, max_value, adaptiveMethod, thresh_type, blockSize: size of neighbourhood area, value of c: constant)

th7 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

# _ is nothing but ret value, which is a bool 

# Types of thresholding:
# 1.) THRESH_BINARY: If pixel<=thresh_min, pixel=0 else 255
# 2.) THRESH_BINARY_INV: If pixel<=thresh_min, pixel=255 else 0
# 3.) THRESH_TRUNC: If pixel<=thresh_min, pixel=pixel else thresh
# 4.) THRESH_TOZERO: If pixel<=thresh_min, pixel=0 else thresh
# 5.) THRESH_TOZERO_INV: If pixel<=thresh_min, pixel=thresh else 0

# Adaptive thresholding:
# Provide different thresholding to different regions
# The algorithm determines the threshold for a pixel based on a small region around it. So we get different thresholds for different regions of the same image which gives better results for images with varying illumination.

# cv.ADAPTIVE_THRESH_MEAN_C: The threshold value is the mean of the neighbourhood area minus the constant C.
# cv.ADAPTIVE_THRESH_GAUSSIAN_C: The threshold value is a gaussian-weighted sum of the neighbourhood values minus the constant C.

cv2.imshow('gradient', img)
# cv2.imshow('th1', th1)
# cv2.imshow('th2', th2)
# cv2.imshow('th3', th3)
# cv2.imshow('th4', th4)
# cv2.imshow('th5', th5)
cv2.imshow('th6', th6)
cv2.imshow('th7', th7)

cv2.waitKey(0)
cv2.destroyAllWindows()