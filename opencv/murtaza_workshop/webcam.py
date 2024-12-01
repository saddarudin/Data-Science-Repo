import cv2 as cv

cap = cv.VideoCapture(0)

while True:
    ret,frame = cap.read()
    if ret:
        cv.imshow('webcam',frame)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        print('camera not working')
        break
    
cap.release()
cv.destroyAllWindows()