# Template Matching: searching image based on the template provided,  from large image
import numpy as np
import cv2 

img = cv2.imread("data/messi5.jpg")
# img = cv2.imread("data/smarties.png")
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
template = cv2.imread("data/messi5_face.jpg", 0)
# template = cv2.imread("data/smarties_blue.png", 0)
# w, h = template.shape[::-1]
# Gives cols and rows value in reverse order
w, h = template.shape
print(template.shape)
# returns tuple of number of rows, columns, and channels
# Here channel is absent as image is gray

res = cv2.matchTemplate(gray_img, template, cv2.TM_CCOEFF_NORMED)
# (image, template, method)
# print(res)
# Brightest point when template matches the image

threshold = 0.92
loc = np.where(res >= threshold)
print(loc)
print(*loc)
print(*loc[::-1])
# print(loc[0][0], loc[1][0])
# loc[0][0]=216 and loc[1][0]=81
# Gives the coordinates for the template-similar part of original image
# Filters the result
# cv2.line(img, (216, 81), (268, 129), (0, 0, 0), 5 )

for pt in zip(*loc[::-1]):
    # loc = [((y_pos, x_pos))]
    # loc[::-1] = [((x_pos, y_pos))]
    # *loc = ((x_pos, y_pos))
    # The -1 at the end reverses this list to [(column, row)] to obtain (x_pos, y_pos).
    print(pt)
    # print((pt[0] + w, pt[1] + h))
    cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0, 255, 255), 2)

cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()