import cv2 as cv

img = cv.imread('resources/geometry.jpg')
cv.imshow('objects',img)

def mouse_event(event,x,y,flags,param):
    global i,roi,coordinates
    if event == cv.EVENT_LBUTTONDOWN:
        coordinates.append((x,y))
        i = i+1
    
    if i==2:
        roi = img[coordinates[0][1]:coordinates[1][1],coordinates[0][0]:coordinates[1][0]]
        cv.imshow('ROI',roi)
        print(coordinates)
        i = 0
    
    if event == cv.EVENT_RBUTTONDOWN:
        img[y:y+(coordinates[1][1]-coordinates[0][1]),x:x+(coordinates[1][0]-coordinates[0][0])] = roi
        cv.imshow('objects',img)
        coordinates.clear()
    
    
    
i = 0
roi = None
coordinates = []
cv.setMouseCallback('objects',mouse_event)
cv.waitKey(0)
cv.destroyAllWindows()