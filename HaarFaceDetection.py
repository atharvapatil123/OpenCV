import cv2

def Face(): 
    # File taken from https://github.com/opencv/opencv/tree/master/data/haarcascades
    # Starred by me :)
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    Video(face_cascade)

def Smile(): 
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')   
    smile_cascade = cv2.CascadeClassifier('haarcascade_smile.xml')
    # Video(face_cascade)

    cap = cv2.VideoCapture(0)

    while cap.isOpened():
        _, img = cap.read()
        gray =  cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(img, 1.1, 50)
        # (Image, scaleFactor – Parameter specifying how much the image size is reduced at each image scale, minNeighbors - This parameter will affect the quality of the detected faces. Higher value results in fewer detections but with higher quality. 3~6 is a good value for it, minSize, maxSize)

        # It returns coordiantes, with width and height as a box

        # HERE FACE IS OUR ROI

        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 3)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = img[y:y+h, x:x+w]
            smile = smile_cascade.detectMultiScale(roi_gray)
            for (sx, sy, sw, sh) in smile:
                cv2.rectangle(roi_color, (sx, sy), (sx+sw, sy+sh), (0, 255, 0), 5)
        
        cv2.imshow('img', img)
        if cv2.waitKey(1) == 27:
            break

def Eyes():
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')

    cap = cv2.VideoCapture(0)

    while cap.isOpened():
        _, img = cap.read()
        gray =  cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(img, 1.1, 4)
        # HERE FACE IS OUR ROI

        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 3)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = img[y:y+h, x:x+w]
            eyes = eye_cascade.detectMultiScale(roi_gray)
            for (ex, ey, ew, eh) in eyes:
                cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 5)
        
        cv2.imshow('img', img)
        if cv2.waitKey(1) == 27:
            break


def image(face_cascade):
    img = cv2.imread('data/Atharva.jpg')
    img = cv2.pyrDown(img)
    img = cv2.pyrDown(img)
    img = cv2.pyrDown(img)
    gray =  cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(img, 1.1, 50)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 3)


    cv2.imshow('img', img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

def Video(face_cascade):
    cap = cv2.VideoCapture(0)

    while cap.isOpened():
        _, img = cap.read()
        gray =  cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(img, 1.1, 200)

        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 3)

        cv2.imshow('img', img)
        if cv2.waitKey(1) == 27:
            break

    cap.release()
    cv2.destroyAllWindows()


# Eyes()
Smile()