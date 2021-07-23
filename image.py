import cv2
# print(cv2.__version__)
img = cv2.imread('data/aloeL.jpg',-1)
# print(img)
i=1
while(True):
    cv2.imshow('image view',img)
    key = cv2.waitKey(0)

    if key==27:
        break
    elif key==ord('Y'):
        x = f"aloeL_my_copy{i}.jpg"
        cv2.imwrite(x,img)
        cv2.waitKey(1000)
        cv2.destroyAllWindows()
        # cv2.imshow('image view',img)
        i=i+1
cv2.destroyAllWindows()


# img[0][0]=1
# cv2.imwrite()
# print(img)

