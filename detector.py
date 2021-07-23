import matplotlib.pylab as plt
import cv2
import numpy as np

# To mask remaining things other than ROI
def region_of_interest(img, vertices):
    mask = np.zeros_like(img)
    # Takes array as input
    # Return an array of zeros with shape and type of input.
    # While np.zeros() return a new array of given shape and type
    # channel_count = img.shape[2]
    # match_mask_color = (255,)* channel_count
    match_mask_color = 255
    # Here, gives (255, 255, 255)
    cv2.fillPoly(mask, vertices, match_mask_color)

    cv2.imshow("mask", mask)
    # Fills the area bounded by one or more polygons.
    # The function cv::fillPoly fills an area bounded by several polygonal contours. The function can fill complex areas, for example, areas with holes, contours with self-intersections (some of their parts), and so forth.
    masked_image = cv2.bitwise_and(img, mask)
    return masked_image


def draw_the_lines(img, lines):
    img = np.copy(img)
    blank_image = np.zeros((img.shape[0], img.shape[1], 3), dtype=np.uint8)

    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv2.line(blank_image, (x1, y1), (x2, y2), (0, 0, 255), 10)

    img = cv2.addWeighted(img, 0.6, blank_image, 1, 0.0)
    return img


image = cv2.imread('data/road1.jpg')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

print(image.shape)
height = image.shape[0]
weight = image.shape[1]

#Here Y-axis is reverse 
region_of_interest_vertices = [
    (0, height),
    (weight/2, height/2),
    (weight,height)
]

# mask = np.zeros_like(image)
# match_mask_color = (255,)* 3
# cv2.imshow("mask",mask)
# print(match_mask_color)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
canny_image = cv2.Canny(gray, 100, 150)

cv2.imshow("canny_image",canny_image)

masked_image = region_of_interest(canny_image,
               np.array([region_of_interest_vertices], np.int32))
cv2.imshow("masked_image",masked_image)
# plt.imshow(canny_image)

lines = cv2.HoughLinesP(masked_image, 
                        6, 
                        np.pi/60, 
                        160, 
                        np.array([]),
                        minLineLength=40, 
                        maxLineGap=25)

# print(lines)
img = draw_the_lines(image, lines)


plt.imshow(img)
plt.show()

k = cv2.waitKey(0)
cv2.destroyAllWindows()