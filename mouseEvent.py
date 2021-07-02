import numpy as np
import cv2
import math

# events = [i for i in dir(cv2) if 'EVENT' in i]
# print(events)#printitng all mouseEvents present in cv2 library


# ['EVENT_FLAG_ALTKEY', 'EVENT_FLAG_CTRLKEY', 'EVENT_FLAG_LBUTTON', 'EVENT_FLAG_MBUTTON', 
# 'EVENT_FLAG_RBUTTON', 'EVENT_FLAG_SHIFTKEY', 'EVENT_LBUTTONDBLCLK', 'EVENT_LBUTTONDOWN', 'EVENT_LBUTTONUP', 'EVENT_MBUTTONDBLCLK', 'EVENT_MBUTTONDOWN', 'EVENT_MBUTTONUP', 'EVENT_MOUSEHWHEEL', 'EVENT_MOUSEMOVE', 'EVENT_MOUSEWHEEL', 'EVENT_RBUTTONDBLCLK', 'EVENT_RBUTTONDOWN', 'EVENT_RBUTTONUP']

def click_event(event, x, y, flags, params):
    # def showCoordinates():
        # if event == cv2.EVENT_LBUTTONDOWN:
        #     print(x,", ",y)
        #     font = cv2.FONT_HERSHEY_SIMPLEX
        #     text = str(x) + ", " +str(y)
        #     cv2.putText(img1,text, (x,y), font, 1, (0,255,255), 2, cv2.LINE_AA)
        #     cv2.imshow("Coordinates of mouseclick on image",img1)

    # def BGRchannel():
        if event == cv2.EVENT_RBUTTONDOWN:
            blue = img2[y, x, 0]
            green = img2[y, x, 1]
            red = img2[y, x, 2]
            font = cv2.FONT_HERSHEY_SIMPLEX
            text = str(blue) + ", " + str(green) + ', ' + str(red)
            cv2.putText(img2, text, (x,y), font, 1, (255,255,255), 2, cv2.LINE_AA)
            cv2.imshow("BGR channel on image",img2)

    # def MouseMove():
        # if event == cv2.EVENT_MOUSEMOVE:
        #     font = cv2.FONT_HERSHEY_SIMPLEX
        #     text = "~"
        #     cv2.putText(img, text, (x,y), font, 1, (255,255,255), 1, cv2.LINE_AA)
        #     cv2.imshow("MouseMove on image",img)

    # def drawLine():
        # if event == cv2.EVENT_LBUTTONDOWN:
        #     cv2.circle(img1, (x,y), 3, (0,255,0), -1)
        # points.append((x,y))
        # if len(points)>=2:
        #     cv2.line(img1, points[-1], points[-2], (0,255,0), 2)
        # cv2.imshow("Coordinates of mouseclick on image",img1)

    # def drawCircle():
        # if event == cv2.EVENT_LBUTTONDOWN:
        #     cv2.circle(img1, (x,y), 3, (0,255,0), -1)
        # points.append((x,y))
        # if len(points)>=2:
        #     # cv2.line(img1, points[-1], points[-2], (0,255,0), 2)
        #     cv2.circle(img1, points[-2], dist(points[-2],points[-1]), (0,255,0), 1)
        # cv2.imshow("Coordinates of mouseclick on image",img1)
        
    #def myColorImage():
        if event ==cv2.EVENT_LBUTTONDOWN:
            blue = img1[y, x, 0]
            green = img1[y, x, 1]
            red = img1[y, x, 2]
            cv2.circle(img1, (x,y), 3, (0,0,225), -1)
            myColorImage = np.zeros((512,512,3), np.uint8)

            myColorImage[:] = [blue, green, red]

            cv2.imshow("My Color Image", myColorImage)


def dist(center, point):
    x,y = center
    x1,y1 = point
    return int( math.sqrt( ((x-x1)*(x-x1)) + ((y-y1)*(y-y1)) ) )

points = []
# img1 = np.zeros((512,512,3),np.uint8)
img1 = cv2.imread('lena.jpg')
# img2 = cv2.imread('aloeL.jpg')

# cv2.imshow('MouseMove on image', img)
cv2.imshow('Coordinates of mouseclick on image',img1)
# cv2.imshow('BGR channel on image',img2)

# cv2.setMouseCallback("MouseMove on image", click_event)
cv2.setMouseCallback("Coordinates of mouseclick on image", click_event)
# cv2.setMouseCallback("BGR channel on image", click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()