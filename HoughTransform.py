# Detect any shape, if we can represent that shape in mathematical form. It can detect the shape even if it is broken or distorted

# A line in the image can be represented with 2 variable: using cartesian coordinate system: y = mx + c, represented in a m-c space where we need to manage a single point instead of the entire line, when x and y are given, else when m and c are given m-c space is better: c = xm + y
#  and polar coordinate system: r = x*cos(t) + y*sin(t)
# We use polar coordinate system

# Edge detection
# Mapping of edge points to the Hough space and storage in an accumulator
# Interpretation of accumulator to yield lines of infinite length, done by thresholding
# Conversion of infinite lines to finite lines

# https://learnopencv.com/hough-transform-with-opencv-c-python/

import cv2
import numpy as np

# img = cv2.imread('data/sudoku.png')
img = cv2.imread('data/road1.jpg')
# print(img.shape)
print("\n")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 51, 105, apertureSize=3)
cv2.imshow('canny', edges)
def HoughLinePmethod(): 
    lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 130, minLineLength=100, maxLineGap=10)#(image, rho, theta, threshold, minLineLength: Line segments shorter than this value are rejected, maxLineGap: Max allowed gap between line segments to treat them as single lines)

    print(lines)
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)

    cv2.imshow('image', img)
    k = cv2.waitKey(0)
    cv2.destroyAllWindows()


def HoughLinesMethod():
    lines = cv2.HoughLines(edges, 1, np.pi / 180, threshold=130)#(image, rho value, theta(radians), threshold)
    # Gives lines but are of infinite length, thus comes the use of HoughLinesP() method
    # print(lines)

    for line in lines:
        rho, theta = line[0]
        a = np.cos(theta)
        b = np.sin(theta)
        #origin or top left corner of the image
        x0 = a*rho
        y0 = b*rho
        X=int(x0)
        Y=int(y0)
        print(X," ",Y)
        # x1 stores the rounded off value of (rho*cos(theta) - 1000*sin(theta))
        x1 = int(x0 + 1000 *(-b))
        # y1 stores the rounded off value of (rho*sin(theta) + 1000*cos(theta))
        y1 = int(y0 + 1000 *(a))
        # x2 stores the rounded off value of (rho*cos(theta) + 1000*sin(theta))
        x2 = int(x0 - 1000 *(-b))
        # y2 stores the rounded off value of (rho*sin(theta) - 1000*cos(theta))
        y2 = int(y0 - 1000 *(a))

        cv2.line(img, (X, Y), (x1, y1), (0, 0, 255), 2)

    cv2.imshow('image', img)
    k = cv2.waitKey(0)
    cv2.destroyAllWindows()


HoughLinePmethod()