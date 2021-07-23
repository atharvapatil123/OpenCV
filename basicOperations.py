import cv2
import numpy as np

def click_event(event,x,y,flag,params):
    if event==cv2.EVENT_LBUTTONDOWN:
        print(x," ",y)
        cv2.imshow("Coordinates of mouseclick on image",img)

# img = cv2.imread('squirrel_cls.jpg')
img = cv2.imread('data\chessboard.png')
img = cv2.rectangle(img,(0,0),(200,200),(0,1,255),-1)
# img2 = cv2.imread('smarties.png')
img2 = np.zeros((512,512,3),np.uint8)
# img2 = cv2.rectangle(img2,(100,200),(400,500),(255,0,255),-1)
img2 = cv2.rectangle(img2,(0,0),(512,512),(1 ,0,0),-1)
# img2 = cv2.rectangle(img2,(10,20),(40,50),(0,255,255),-1)

# print(img.size)#returns total number of pixels in the image
print(img.shape)#returns tuple of number of rows, columns, and channels
# print(img.dtype)#returns dataType of the image

b,g,r = cv2.split(img)
print((b,g,r))
# img = cv2.merge((r,b,g))#Gives a different image
# img = cv2.merge((b,g,r));
# print(img[123,236])
ball = img[289:335, 335:394]
# print(face)
img[294:340, 94:153] =  ball

green = img[284:336, 164:216]
img[289:341 , 335:387] = green
# print(img)

img = cv2.resize(img,(512,512))
img2 = cv2.resize(img2,(512,512))

dst = cv2.add(img,img2)#Adds 2nd image over 1st equally.

dst2 = cv2.addWeighted(img, 0.5, img2, 0.5, 0)# Adds 1st and 2nd images in proportions

bitAnd = cv2.bitwise_and(img,img2)#Ands the pixels at each point, so for (0,0,0) & (255,255,255)=> (0,0,0) i.e black, similarly, for (255,1,200) &(0,255,201) => (0,1,200) i.e. gives lower value

bitOr = cv2.bitwise_or(img,img2)#Gives higher pixel from the two, opposite to bitwise_and

bitXor = cv2.bitwise_xor(img,img2)#Gives high when both are alternate, and low, when both are same i.e for (0,255,195) ^ (201,255,234) => (201,0,234)

bitNot = cv2.bitwise_not(img2)#Gives opposite value to given pixels, i.e 255-currentValue

cv2.imshow("Coordinates of mouseclick on image",img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# cv2.setMouseCallback("Coordinates of mouseclick on image", click_event)

cv2.waitKey(0)
cv2.destroyAllWindows() 

# img = np.zeros((426,535,3),np.uint8)
# cv2.imshow("Image",img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()