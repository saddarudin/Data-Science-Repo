import cv2 as cv

# F:\Data Science\Data-Science-Repo\opencv\haarcascade\haarcascade_frontalface_default.xml
face_cascade = cv.CascadeClassifier('haarcascade/haarcascade_frontalface_default.xml')
img = cv.imread('resources/faces.jpg')
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray,1.1,4)

for (x,y,w,h) in faces:
    cv.rectangle(img,(x,y),(x+w,y+h),(255,0,0),3)

cv.imshow('Image',img)
cv.waitKey(0)
cv.destroyAllWindows()