# Image pyramid: Multi-scale signal representation in which a signal or an image is subject to repeated smoothing and subsampling
# Example: Level-0:Original image -> Level-1:1/2 resolution -> Level-3:1/4 resolution -> ... like a pyramid
# USE: BLEND AND RECONSTRUCT
import cv2
import numpy as np

img = cv2.imread('data/lena.jpg')

# Gaussian pyramid: Repeat, filtering and subsampling of an image: pyrDown and pyrUp
lr =  cv2.pyrDown(img)
lr2 =  cv2.pyrDown(lr)
# lr3 =  cv2.pyrDown(lr2)
# lr4 =  cv2.pyrDown(lr3)
# lr5 =  cv2.pyrDown(lr4)
layer = img.copy()
gp = [layer]

for i in range(6):
    layer = cv2.pyrDown(layer)
    gp.append(layer)
    # cv2.imshow(str(i), layer)

# Reduces resolution, we loose imformation of the image as well, thus on using pyrUp on that image, we get blurred image

ur =  cv2.pyrUp(lr2)
# Increases resolution


# Laplacian pyramid: Formed from gaussian pyramid, no exclusive function for it:  Difference between that level in Gaussian pyramid and expanded version of its upper level in Gaussian pyramid

layer = gp[5]#Last image of Gaussian pyramid is taken
cv2.imshow('Upper level Gaussian pyramid', layer)
lp = [layer]

for i in range(5, 0, -1):
    gausssian_expanded = cv2.pyrUp(gp[i-1])
    laplacian = cv2.subtract(gp[i-1], gausssian_expanded)
    cv2.imshow(str(i), laplacian)


# cv2.imshow('Original Image', img)
# cv2.imshow('pyrDownImage', lr)
# cv2.imshow('pyrDownImage2', lr2)
# cv2.imshow('3', lr3)
# cv2.imshow('4', lr4)
# cv2.imshow('5', lr5)
# cv2.imshow('pyrUpImage', ur)
cv2.waitKey(0)
cv2.destroyAllWindows()