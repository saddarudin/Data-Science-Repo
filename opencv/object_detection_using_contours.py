import cv2 as cv

cap = cv.VideoCapture('F:/Data Science/videos/people walking.mp4')

ret,frame1 = cap.read()
ret,frame2 = cap.read()

while cap.isOpened():
    if ret:
        diff = cv.absdiff(frame1,frame2)
        gray = cv.cvtColor(diff,cv.COLOR_BGR2GRAY)
        blur = cv.GaussianBlur(gray,(5,5),0)
        _,thresh = cv.threshold(blur,20,255,cv.THRESH_BINARY)
        dilated = cv.dilate(thresh,None,iterations=3)
        contours,_ = cv.findContours(dilated,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
        # cv.drawContours(frame1,contours,-1,(0,255,0),2)
        for contour in contours:
            (x,y,w,h) = cv.boundingRect(contour)
            
            if cv.contourArea(contour) < 900:
                continue
            cv.rectangle(frame1,(x,y),(x+w,y+h),(0,255,0),2)
            cv.putText(frame1,'Status: Movement',(10,20),cv.FONT_HERSHEY_SIMPLEX,1,(0,0,255),3)
                
                
        cv.imshow('Video',frame1)
        frame1 = frame2
        ret,frame2 = cap.read()
        if cv.waitKey(11) & 0xFF == ord('q'):
            break
    else:
        print('Video ended')
        break

cap.release()
cv.destroyAllWindows()