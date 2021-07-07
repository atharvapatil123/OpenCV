# Erosion, dilation, opening, and closing
# Simple operations based on image shape, normally performed on binary image, 1st original image, 2nd structuring elemnt or kernel.

import cv2
import numpy as np

from matplotlib import pyplot as plt

img = cv2.imread('data\smarties.png', cv2.IMREAD_GRAYSCALE)
_, mask = cv2.threshold(img, 220, 255, cv2.THRESH_BINARY_INV)

kernel =  np.ones((5,5), np.uint8)#4x4 square shape, to be applied on our image, on the dots
# kernel is a shape we want to apply on a image
# To get kernel manually, of our own shape, we use getStructuringElement()

# kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
# kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
# kernel = cv2.getStructuringElement(cv2.MORPH_CROSS,(5,5))

dilation = cv2.dilate(mask, kernel, iterations=2)
#Dilation is dilating the black dots, the pixel is 1 if atleast one pixel on kernel is 1

erosion  = cv2.erode(mask, kernel, iterations=1)#1 iteration by default
#The pixel is 1 if all the pixels of kernel are 1

opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
#First erosion then dilation

closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
#First dilation then erosion

mg = cv2.morphologyEx(mask, cv2.MORPH_GRADIENT, kernel)
# Difference between dilation and erosion of an image

th = cv2.morphologyEx(mask, cv2.MORPH_TOPHAT, kernel)
# Difference between opening an input image

bh = cv2.morphologyEx(mask, cv2.MORPH_BLACKHAT, kernel)
# Difference between closing an input image

# opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

titles = ['image', 'mask', 'dilation', 'erosion', 'opening', 'closing', 'mg', 'th', 'bh']
images=[img, mask, dilation, erosion, opening, closing, mg, th, bh]

for i in range(9):
    plt.subplot(2, 5, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()