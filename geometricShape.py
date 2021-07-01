import cv2
import numpy as np

def show(img,name):
    x = f"{name}"
    cv2.imshow(x,img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def border():
    img = cv2.imread('squirrel_cls.jpg',1)
    img = cv2.line(img, (0,1), (530,1), (146,224,43), 15)#1st arg is image itself, 2nd arg is starting point, 3rd ending point, 4th color(bgr) and 5th is thickness, if its -1, then the shape gets filled with that color

    cv2.imshow('Line image',img)
    cv2.waitKey(2000)
    img = cv2.line(img, (530,0), (530,420), (146,224,43), 10)
    cv2.imshow('Line image',img)
    cv2.waitKey(2000)
    img = cv2.line(img, (530,420), (0,420), (146,224,43), 10)
    cv2.imshow('Line image',img)
    cv2.waitKey(2000)
    img = cv2.line(img, (0,420), (0,0), (146,224,43), 15)
    cv2.imshow('Line image',img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


def cross():
    a=False
    img = cv2.imread('squirrel_cls.jpg',1)
    cv2.imshow('Line image',img)
    cv2.waitKey(3)
    img = cv2.line(img, (0,0), (540,430), (146,224,43), 1)
    i=1;
    while(i<=545):
        img = cv2.line(img, (i,0), (540-i,430), (146,224,43), 1)
        cv2.imshow('Line image',img)
        i+=3;
        key = cv2.waitKey(3)
        # key = cv2.waitKey(0)
        if key==ord('q'):
            a=True
            break
    if(a==True):
        cv2.destroyAllWindows()
    else:
        cv2.waitKey(5000)
        cv2.destroyAllWindows()

def arrow():
    img = cv2.imread('squirrel_cls.jpg',1)
    img = cv2.arrowedLine(img, (0,0), (530,400), (146,224,43), 10)
    show(img)

def rectangle():
    img = cv2.imread('squirrel_cls.jpg',1)
    img = cv2.rectangle(img, (132,1), (396,300), (0,255,0), -1)
    name = "Rectangle Image"
    show(img,name)

def chess():
    b=False
    img = cv2.imread('squirrel_cls.jpg',0)
    cv2.imshow('Line image',img)
    cv2.waitKey(3)
    # img = cv2.rectangle(img, (0,0), (45,43), (0,0,0), -1)
    x=0
    y=0
    a=1
    while(y<=430):
        x=0
        while(x<=540):
            if a:
                img = cv2.rectangle(img, (x+0,0+y), (45+x,43+y), (255,255,255), -1)
                a=0
                cv2.imshow('Line image',img)
                key = cv2.waitKey(3)
            else: 
                img = cv2.rectangle(img, (x+0,0+y), (45+x,43+y), (0,0,0), -1)
                a=1
                cv2.imshow('Line image',img)
                key = cv2.waitKey(3)
            if key==ord('q'):
                    b=True
                    break 
            x+=45
        y+=43
    if(b==True):
        cv2.destroyAllWindows()
    else:
        cv2.waitKey(10000)
        cv2.destroyAllWindows()
    

def circle():
    img = cv2.imread('squirrel_cls.jpg',1)
    img = cv2.circle(img, (270,215), 215, (0,255,255), -1 )#2ndarg is center of cirle, 3rd radius, 4th color, 5th thickness=NONE, 6th line typr=NONE, 7th shift=NONE
    name = 'Circle Image'
    show(img,name)


def encircle():
    a=False
    img = cv2.imread('squirrel_cls.jpg',-1)
    cv2.imshow('Line image',img)
    cv2.waitKey(3)
    img = cv2.circle(img, (270,215), 215, (0,0,0), -1 )
    i=1;
    r=215
    while(r>=0 and i<=215):
        r=215-i
        img = cv2.circle(img, (270,215), r, (0+i,0+i,0+i), -1)
        cv2.imshow('Line image',img)
        i+=1;
        key = cv2.waitKey(3)
        # key = cv2.waitKey(0)
        if key==ord('q'):
            a=True
            break
    if(a==True):
        cv2.destroyAllWindows()
    else:
        cv2.waitKey(5000)
        cv2.destroyAllWindows()


def putText():
    img = cv2.imread('squirrel_cls.jpg',1)
    font = cv2.FONT_HERSHEY_COMPLEX_SMALL
    img = cv2.putText(img,'OpenCV',(70,215), font, 4, (255,0,255), 10, cv2.LINE_AA)#2nd arg is text, 3rd is starting pt,  4th is font face, 5th is font size, 6th is color of font, 7th is thickness, 8th is line type
    name = 'PutText Image'
    show(img,name)
    # cv2.imshow('putText',img)
    
def createImg():
    img = np.zeros([512, 512, 1], np.uint8)
    name = "Numpy image"
    show(img,name)


# createImg()
# putText()
# encircle()
chess()
# rectangle()
# arrow()
# border()
# cross()
