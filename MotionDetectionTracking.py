# https://learnopencv.com/contour-detection-using-opencv-python-c/
import cv2
import numpy as np 

cap = cv2.VideoCapture('data/vtest.avi')
# cap = cv2.VideoCapture(0)

ret, frame1 =  cap.read()
ret, frame2 =  cap.read()


while cap.isOpened():
    diff = cv2.absdiff(frame1, frame2)
    cv2.imshow("diff",diff)

    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    # cv2.imshow("gray",gray)

    # blur = cv2.GaussianBlur(gray, (5, 5), 0)
    blur = cv2.bilateralFilter(gray, 9, 75, 75)
    # cv2.imshow("blur",blur)

    _, thresh = cv2.threshold(blur, 50, 255, cv2.THRESH_BINARY)
    # cv2.imshow("thresh",thresh)

    dilated = cv2.dilate(thresh, None, iterations=3)

    # dilated = cv2.bilateralFilter(dilated, 9, 75, 75)
    # cv2.imshow("dilated",dilated)

    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # cv2.drawContours(frame1, contours, -1, (0,255,255), 3)

    for contour in contours:
        (x, y, w, h) = cv2.boundingRect(contour)
        # Takes (array) and gives (x, y, width, height)

        if cv2.contourArea(contour) < 500:
            continue
        else:
            cv2.rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 255), 3)
            cv2.putText(frame1, "Status: {}".format("Movement"), (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
        
        approx = cv2.approxPolyDP(contour, 0.01*cv2.arcLength(contour, True), True)#(curve, epsilon: parameter specifying approx. accuracy (acrLength calculates the curve length, closed- True or False), closed-true or False)
        # It approximates a contour shape to another shape with less number of vertices depending upon the precision we specify. It is an implementation of Douglas-Peucker algorithm. 
        cv2.drawContours(frame1, [approx], 0, (0, 0, 0), 5)
        x = approx.ravel()[0]
        y = approx.ravel()[1] - 5


    # cv2.imshow("inter", frame)
    cv2.imshow("new", frame1)

    frame1 = frame2
    ret, frame2 = cap.read()

    if cv2.waitKey(40) == 27:
        break

cv2.destroyAllWindows()
cap.release()