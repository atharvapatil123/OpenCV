import cv2
import math
cap = cv2.VideoCapture('Dad Video.avi')#default camera index is either 0 or -1

# fourcc = cv2.VideoWriter_fourcc('X','V','I,'D)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc, 30.0, (640,480))#1st arg is name of output file, 2nd arg is fourcc code: 4byte code, use to specify video codec fourcc.org/codecs.php, 3rd arg is no of frames/sec, 4th arg is size

i=1
time=66
while(cap.isOpened()):
    ret, frame = cap.read()#ret is bool varible, frame is actual frame value

    if ret==True:
        # print(cap.get(cv2.CAP_PROP_FPS))
        # print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        # print(cap.get(cv2.CAP_PROP_POS_MSEC))
        # print(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        # if(((cap.get(cv2.CAP_PROP_POS_MSEC)==66.66666666666667) or ((cap.get(cv2.CAP_PROP_POS_MSEC)>=43500) and cap.get(cv2.CAP_PROP_POS_MSEC)<=43500.333333333333)) or (cap.get(cv2.CAP_PROP_POS_MSEC)==86966.66666666666667)):
        #     x = f"{i} copy.jpg"
        #     cv2.imwrite(x,frame)
        #     i+=1

        if(math.floor(cap.get(cv2.CAP_PROP_POS_MSEC))==time):
            print(i)
            x = f"{i} copy.jpg"
            cv2.imwrite(x,frame)
            i+=1
            time+=17000
        # out.write(frame)

        cv2.imshow('frame', frame)

        # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)#1st arg is source, 2nd arg isq conversion
        # img = cv2.imread('cap',0)
        # i+=1
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()