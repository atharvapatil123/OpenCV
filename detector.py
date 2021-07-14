import matplotlib.pylab as plt
import cv2
import numpy as np

image = cv2.imread('data/road1.jpg')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

print(image.shape)
height = image.shape[0]
weight = image.shape[1]

region_of_interest_vertices = [
    (0, height),
    (weight/2, height/2),
    (weight,height)
]

# mask = np.zeros_like(image)
# match_mask_color = (255,)* 3
# cv2.imshow("mask",mask)
# print(match_mask_color)


# To mask remaining things other than ROI
def region_of_interest(img, vertices):
    mask = np.zeros_like(img)
    # Takes array as input
    # Return an array of zeros with shape and type of input.
    # While np.zeros() return a new array of given shape and type
    channel_count = img.shape[2]
    match_mask_color = (255,)* channel_count
    # Here, gives (255, 255, 255)
    cv2.fillPoly(mask, vertices, match_mask_color)
    # Fills the area bounded by one or more polygons.
    # The function cv::fillPoly fills an area bounded by several polygonal contours. The function can fill complex areas, for example, areas with holes, contours with self-intersections (some of their parts), and so forth.
    masked_image = cv2.bitwise_and(img, mask)
    return masked_image



masked_image = region_of_interest(image,
               np.array([region_of_interest_vertices], np.int32))
plt.imshow(masked_image)
plt.show()