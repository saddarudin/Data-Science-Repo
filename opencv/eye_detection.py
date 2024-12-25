import cv2 as cv
import numpy as np

face_cascade = cv.CascadeClassifier('haarcascade/haarcascade_frontalface_default.xml')
eye_cascade = cv.CascadeClassifier('haarcascade/haarcascade_eye.xml')

img = cv.imread('resources/my face.jpg')
img = cv.resize(img,(500,500))
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray,1.3,5)

for (x,y,w,h) in faces:
    roi_gray = gray[y:y+h,x:x+w]
    cv.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    roi_color = img[y:y+h,x:x+w]
    eyes = eye_cascade.detectMultiScale(roi_gray)
    for (ex,ey,ew,eh) in eyes:
        cv.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
        
cv.imshow('img',roi_color)
cv.waitKey(0)
cv.destroyAllWindows()