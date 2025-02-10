import cv2 as cv

def nothing(x):
    print(x)

cv.namedWindow('Trackbars')
cv.resizeWindow('Trackbars', 400, 400)

# lower scale will require more computation power but will give better results
# lower neighbors will give more detection but can include false detections as well.
cv.createTrackbar('scale', 'Trackbars', 400, 1000, nothing)
cv.createTrackbar('neigh', 'Trackbars', 8, 20, nothing)
cv.createTrackbar('minArea', 'Trackbars', 0, 100000, nothing)

# Load the image
img = cv.imread('resources/faces.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

cascade = cv.CascadeClassifier('haarcascade/haarcascade_frontalface_default.xml')

while True:
    scaleValue = 1 + (cv.getTrackbarPos('scale', 'Trackbars') / 1000)
    neigh = cv.getTrackbarPos('neigh', 'Trackbars')

    objects = cascade.detectMultiScale(gray, scaleValue, neigh)
    img_copy = img.copy()  

    for (x, y, w, h) in objects:
        area = w * h
        minArea = cv.getTrackbarPos('minArea', 'Trackbars')
        if area > minArea:
            cv.rectangle(img_copy, (x, y), (x + w, y + h), (255, 0, 0), 3)
            cv.putText(img_copy, 'Face', (x, y - 5), cv.FONT_HERSHEY_COMPLEX, 0.7, (0, 0, 255), 2)

    cv.imshow('Result', img_copy)
    
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cv.destroyAllWindows()
