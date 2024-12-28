import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

cap = cv.VideoCapture('F:/Data Science/videos/moving cars.mp4')
ret,frame = cap.read()
frame = cv.resize(frame,(700,500))
x,y,width,height = 388,88,15,16
track_window = (x,y,width,height)
roi = frame[y:y+height,x:x+width]
hsv_roi = cv.cvtColor(roi,cv.COLOR_BGR2HSV)
mask = cv.inRange(hsv_roi,np.array((0.,60.,32.)),np.array((180.,255.,255.)))
roi_hist = cv.calcHist([hsv_roi],[0],mask,[180],[0,180])
cv.normalize(roi_hist,roi_hist,0,255,cv.NORM_MINMAX)
term_crit = (cv.TermCriteria_EPS | cv.TermCriteria_COUNT,10,1)
while cap.isOpened():
    ret,frame = cap.read()
    if ret:
        frame = cv.resize(frame,(700,500))
        hsv = cv.cvtColor(frame,cv.COLOR_BGR2HSV)
        dst = cv.calcBackProject([hsv],[0],roi_hist,[0,180],1)
        ret,track_window = cv.CamShift(dst,track_window,term_crit)
        x,y,w,h = track_window
        final_image = cv.rectangle(frame,(x,y),(x+w,y+h),255,3)
        cv.imshow('Final Image',final_image)
        # cv.imshow('dst',dst)
        if cv.waitKey(10) & 0xFF == ord('q'):
            break
    else:
        break
        
cap.release()
cv.destroyAllWindows()