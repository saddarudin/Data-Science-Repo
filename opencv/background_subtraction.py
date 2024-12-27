import cv2 as cv

cap = cv.VideoCapture('resources/walking.mp4')
fgbg1 = cv.createBackgroundSubtractorMOG2(detectShadows=False)
fgbg2 = cv.createBackgroundSubtractorKNN(detectShadows=False)


while True:
    ret,frame = cap.read()
    if ret:
        fgmask1 = fgbg1.apply(frame)
        fgmask2 = fgbg2.apply(frame)
        cv.imshow('Original',frame)
        cv.imshow('MOG2',fgmask1)
        cv.imshow('KNN',fgmask2)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
        
cap.release()
cv.destroyAllWindows()