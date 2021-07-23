# Smoothing is blurring images, removing noise, use linear filters in the process as they are fast: Homogeneous, gaussian, bilateral, median filters

import cv2
import numpy as np
from matplotlib import pyplot as plt

# img = cv2.imread('data\opencv-logo-white.png')
# img = cv2.imread('data\\Noise_salt_and_pepper.png')
img = cv2.imread('data\lena.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


kernel = np.ones((4,4), np.float32)/25

# Homogeneous filter is the most simple, each output filter is mean of the kernel neighbour, all pixels contribute equal weight, so homogeneous

# Gaussian filter is using different-weight-kernel in both x and y direction, pixels in the middle have higher wts and goes on decreasing in outward direction. Designed specifically to remove high noise.

#Median Filter: Replaces each pixel's value with the median of it neighbouring pixels. This method is great when dealing with "salt and pepper noise": white + black noise.

#Bilateral Filter: Destroys the noise but not the edges unlike the above filters

# Low Pass Filter: Helps is removing noises, blurring images
# high Pass Filters: Helps in finding edges in the images.

dst = cv2.filter2D(img, -1, kernel)#(image, desired depth of dest. image, kernel)

blur = cv2.blur(img, (5,5))#(image, kernel)
#Averaging algorithmn 

gblur = cv2.GaussianBlur(img, (5,5), 0)#3rd arg is sigma x value, more is sigmax: standard deviation, greater is the spreadness, so less is the blur effect

mblur = cv2.medianBlur(img, 5, 0)#Kernel size must be odd except 1

bblur = cv2.bilateralFilter(img, 9, 75, 75)#2nd arg diameter of neighbouring pixel, sigma color, sigma space

titles = ['images', '2D Convulation', 'blur', 'gblur', 'mblur', 'bblur']
images = [img, dst, blur, gblur, mblur, bblur]

for i in range(6):
    plt.subplot(2, 3, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()

