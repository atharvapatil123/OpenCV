import numpy as np
import cv2 
from matplotlib import pyplot as plt

img = cv2.imread("data/lena.jpg",0) 

# img = np.zeros((200, 200), np.uint8)
# cv2.rectangle(img, (10, 10), (100, 100), (255), -1)
# cv2.rectangle(img, (120, 120), (180, 180), (127), -1)

hist = cv2.calcHist([img], [0], None, [256], [0, 256])
# images : it is the source image of type uint8 or float32. it should be given in square brackets, ie, "[img]".
# channels : it is also given in square brackets. It is the index of channel for which we calculate histogram. For example, if input is grayscale image, its value is [0]. For color image, you can pass [0], [1] or [2] to calculate histogram of blue, green or red channel respectively.
# mask : mask image. To find histogram of full image, it is given as "None". But if you want to find histogram of particular region of image, you have to create a mask image for that and give it as mask. (I will show an example later.)
# histSize : this represents our BIN count. Need to be given in square brackets. For full scale, we pass [256].
# ranges : this is our RANGE. Normally, it is [0,256].

# BINS: When need to find the number of pixels lying between 0 to 15, then 16 to 31, ..., 240 to 255. You will need only 16 values to represent the histogram. So, change binsize to 16 rather than individual 256
# DIMS : It is the number of parameters for which we collect the data. In this case, we collect data regarding only one thing, intensity value. So here it is 1.
#RANGE : It is the range of intensity values you want to measure. Normally, it is [0,256], ie all intensity values.

# b, g, r = cv2.split(img)

# cv2.imshow("img", img)
# cv2.imshow("b", b)
# cv2.imshow("g", g)
# cv2.imshow("r", r)

# plt.hist(img.ravel(), 255, [0, 256])#(image, max no. of pixel value, range)
# plt.hist(b.ravel(), 255, [0, 256])
# plt.hist(g.ravel(), 255, [0, 256])
# plt.hist(r.ravel(), 255, [0, 256])

plt.plot(hist)
# Histogram: Intensity distribution of an image
# Calculates histogram of an image :Y-axis - Total no. of pixels, here 200*200=40000, X-axis - Maximum pixel value

plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()