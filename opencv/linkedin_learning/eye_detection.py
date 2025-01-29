import cv2 as cv

eye_cascade = cv.CascadeClassifier('haarcascade/haarcascade_eye.xml')
img = cv.imread('resources/faces.jpg')
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
eyes = eye_cascade.detectMultiScale(gray,scaleFactor=1.02,minNeighbors=15,minSize=(5,5))
for (x,y,w,h) in eyes:
    xc = (x + x+w)/2
    yc = (y + y+h)/2
    radius = w/2
    cv.circle(img,(int(xc),int(yc)),int(radius),(0,0,0),2)
    # cv.rectangle(img,(x,y),(x+w,y+h),(0,0,0),2)
    
cv.imshow('Detected Eyes',img)
cv.waitKey(0)
cv.destroyAllWindows()  