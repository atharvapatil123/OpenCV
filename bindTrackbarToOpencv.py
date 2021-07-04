import cv2
import numpy as np

def nothing(x):
    print(x)

def grayColor():
    cv2.namedWindow('image1')#Create a window with a name

    cv2.createTrackbar('B','image1',0, 255, nothing)#(Trackbar name, name of window, initial value at which trackbar is set, final value, callback function)
    cv2.createTrackbar('G','image1',0, 255, nothing)
    cv2.createTrackbar('R','image1',0, 255, nothing)

    switch = 'color/gray'
    cv2.createTrackbar(switch, 'image1', 0 ,1, nothing)

    while(1):
        img = cv2.imread('lena.jpg')
        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            break
        b = cv2.getTrackbarPos('B', 'image1')
        g = cv2.getTrackbarPos('G', 'image1')
        r = cv2.getTrackbarPos('R', 'image1')
        s = cv2.getTrackbarPos(switch, 'image1')

        if s == 0:
            pos = str(b)+" "+str(g)+" "+str(r)
            cv2.putText(img, pos, (50,50), (cv2.FONT_HERSHEY_COMPLEX_SMALL), 2, (0,255,255),5)         
        else:
            img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        
        # img[:] = [b, g, r]
        cv2.imshow('image1',img)


    cv2.destroyAllWindows()

def switchForColor():
    img = np.zeros((300,512,3), np.uint8)
    cv2.namedWindow('image')#Create a window with a name

    cv2.createTrackbar('B','image',0, 255, nothing)#(Trackbar name, name of window, initial value at which trackbar is set, final value, callback function)
    cv2.createTrackbar('G','image',0, 255, nothing)
    cv2.createTrackbar('R','image',0, 255, nothing)

    switch = '0 : OFF\n 1: ON'
    cv2.createTrackbar(switch, 'image', 0 ,1, nothing)

    while(1):
        cv2.imshow('image',img)
        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            break
        b = cv2.getTrackbarPos('B', 'image')
        g = cv2.getTrackbarPos('G', 'image')
        r = cv2.getTrackbarPos('R', 'image')
        s = cv2.getTrackbarPos(switch, 'image')

        if s == 0:
            img[:] = 0
        else:
            img[:] =  [b,g,r]
        
        # img[:] = [b, g, r]

    cv2.destroyAllWindows()

# switchForColor()
grayColor()


