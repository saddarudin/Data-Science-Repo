import cv2 as cv

face_cascade = cv.CascadeClassifier('haarcascade/haarcascade_frontalface_default.xml')
img = cv.imread('resources/faces2.jpg')
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray,scaleFactor=1.12,minNeighbors=3,minSize=(30,30))
for (x,y,w,h) in faces:
    cv.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
    
cv.imshow('Detected Faces',img)
cv.waitKey(0)
cv.destroyAllWindows()