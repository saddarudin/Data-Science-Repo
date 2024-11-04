import cv2 as cv
import datetime

cap = cv.VideoCapture('resources/screen_recording.mp4')

while cap.isOpened():
    ret,frame = cap.read()
    if ret:
        frame = cv.resize(frame,(500,500))
        frame = cv.putText(frame,str(datetime.datetime.now()),(20,50),cv.FONT_HERSHEY_DUPLEX,1,(0,0,255),2)
        cv.imshow('video',frame)
        if cv.waitKey(30) & 0xFF == ord('q'):
            break
    else:
        print('video ended or there occured an error')
        break
cap.release()
cv.destroyAllWindows()
