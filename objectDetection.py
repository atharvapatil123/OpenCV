# HSV: Hue: 360deg color range, Saturation: 0-100% from center to outer path, Value: from bottom to upper part 0-100%

import cv2
import numpy as np

def nothing(x):
    pass

cap = cv2.VideoCapture(0);

cv2.namedWindow("Tracking")
cv2.createTrackbar("LH", "Tracking", 0, 255, nothing)
cv2.createTrackbar("LS", "Tracking", 0, 255, nothing)
cv2.createTrackbar("LV", "Tracking", 0, 255, nothing)
cv2.createTrackbar("UH", "Tracking", 255, 255, nothing)
cv2.createTrackbar("US", "Tracking", 255, 255, nothing)
cv2.createTrackbar("UV", "Tracking", 255, 255, nothing)

while 1:
    # frame = cv2.imread('smarties.png')

    _, frame = cap.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)#converting bgr to hsv

    l_h = cv2.getTrackbarPos("LH", "Tracking")
    l_s = cv2.getTrackbarPos("LS", "Tracking")
    l_v = cv2.getTrackbarPos("LV", "Tracking")

    u_h = cv2.getTrackbarPos("UH", "Tracking")
    u_s = cv2.getTrackbarPos("US", "Tracking")
    u_v = cv2.getTrackbarPos("UV", "Tracking")

    l_b = np.array([l_h, l_s, l_v])#lower range of blue color, hsv values
    u_b = np.array([u_h, u_s, u_v])#upper range of blue color, hsv values
    # l_b = np.array([95, 116, 50])#lower range of blue color, hsv values
    # u_b = np.array([130, 255, 255])#upper range of blue color, hsv values

    mask = cv2.inRange(hsv, l_b, u_b)
    #hsv is set to 255, if the pixel is within the range else 0
    # Making is filtering  or creating new image, based on given constraints

    res = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow("frame",frame)
    cv2.imshow("hsv",hsv)
    cv2.imshow("mask",mask)
    cv2.imshow("res",res)

    key = cv2.waitKey(1)
    if key ==27:
        break

cap.release()
cv2.destroyAllWindows()