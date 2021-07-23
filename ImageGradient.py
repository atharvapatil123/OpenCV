# Image gradient is a directional change in the intensity or color in an image, imp in image processing, to find edges inside the image.

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('data/road1.jpg', cv2.IMREAD_GRAYSCALE)

lap = cv2.Laplacian(img, cv2.CV_64F, ksize=3)#(image, data-type: 64-bit Float due to -ve slope induced by tranforming the image from white to black, kernel size (optional))
# Converts the edges to white and remaining black or makes edges more visible

lap = np.uint8(np.absolute(lap))
# REASON: Black-to-White transition is taken as Positive slope (it has a positive value) while White-to-Black transition is taken as a Negative slope (It has negative value). So when you convert data to np.uint8, all negative slopes are made zero. In simple words, you miss that edge.

# If you want to detect both edges, better option is to keep the output datatype to some higher forms, like cv.CV_16S, cv.CV_64F etc, take its absolute value and then convert back to cv.CV_8U. Below code demonstrates this procedure for a horizontal Sobel filter and difference in results.

# Take absolute value of lap and convert it back to the unsigned 8-bit int

sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0)#(img, data-type, Dx=1/0: 1- sobelX 0-sobely, Dy=1/0)
# Change in direction of intensity is in the x direction
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1)
# Change in direction of intensity is in the y direction

sobelx = np.uint8(np.absolute(sobelx))
sobely = np.uint8(np.absolute(sobely))

sobelCombined = cv2.bitwise_or(sobelx, sobely)

bblur = cv2.bilateralFilter(sobelCombined, 9, 75, 75)
def nothing(x):
    print(x)
# Canny Edge Detector: Edge detector operator that uses a multi-stage algorithmn to detect a wide range of edges in images
# Noise reduction
# Gradient calculation
# Non-maximum suppression
# Double threshold
# Edge tracking by hysteresis

cv2.namedWindow('canny')
# canny = cv2.Canny(img, 100, 200)#(image, 1st threshold for hysteresis, 2nd threshold for hysteresis)
cv2.createTrackbar('t1','canny', 0, 255, nothing)
cv2.createTrackbar('t2','canny', 0, 255, nothing)
while 1:
    t1 = cv2.getTrackbarPos('t1','canny')
    t2 = cv2.getTrackbarPos('t2','canny')
    canny = cv2.Canny(img, t1, t2)
    cv2.imshow('canny', canny)
    key = cv2.waitKey(2)
    if(key == 27):
        break

cv2.destroyAllWindows()
# titles = ['image', 'Laplasian', 'sobelX', 'sobelY', 'sobelCombined', 'bblur',  'canny']
# titles = ['image', 'canny']
# images = [img, lap, sobelx, sobely, sobelCombined, bblur, canny]
# images = [img, canny]
# for i in range(7):
#     plt.subplot(2, 4, i+1), plt.imshow(images[i], 'gray')
#     plt.title(titles[i])
#     plt.xticks([])
#     plt.yticks([])

# plt.show()