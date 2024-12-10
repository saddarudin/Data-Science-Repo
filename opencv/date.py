import cv2 as cv
import datetime

cap = cv.VideoCapture(0)

cap.set(3,500)
cap.set(4,500)

while True:
    success,frame = cap.read()
    if success:
        date = str(datetime.datetime.now())
        cv.putText(frame,date,(400,50),cv.FONT_HERSHEY_SIMPLEX,0.5,(0,255,255),1)
        cv.imshow('Video',frame)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        print("Either video ended or an error occured!")
        break
cap.release()
cv.destroyAllWindows()