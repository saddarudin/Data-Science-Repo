import cv2 as cv
import numpy as np

img = cv.imread('resources/my pic1.jpg')
img = cv.resize(img,(500,500))
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
face = cv.CascadeClassifier('haarcascade/haarcascade_frontalface_default.xml')
eye = cv.CascadeClassifier('haarcascade/haarcascade_eye.xml')
faces = face.detectMultiScale(gray,1.1,4)
eyes = eye.detectMultiScale(gray,1.1,4)
for (x,y,w,h) in faces:
    cv.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
for (x,y,w,h) in eyes:
    cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
cv.imshow('gray scaled image',img)
cv.waitKey(0)
cv.destroyAllWindows()