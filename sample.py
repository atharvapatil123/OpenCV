import cv2
# print(cv2.__version__)
img = cv2.imread('aloeL.jpg',-1)
# print(img)
cv2.imshow('image view',img)
key = cv2.waitKey(0)

if key==27:
    cv2.destroyAllWindows()
elif key==ord('Y'):
    cv2.imwrite('aloeL_my_copy3.jpg',img)
    cv2.destroyAllWindows()
    
# img[0][0]=1
# cv2.imwrite()
# print(img)

