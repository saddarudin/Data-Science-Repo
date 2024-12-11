import cv2 as cv

def mouse_event(event,x,y,flags,param):
    if event == cv.EVENT_LBUTTONDOWN:
        print(x,y)
        cv.putText(img,str(x)+' '+str(y),(x,y),cv.FONT_HERSHEY_COMPLEX,0.5,(0,0,255),1)
        cv.imshow('Image',img)
        
    if event == cv.EVENT_RBUTTONDOWN:
        b = img[y,x,0]
        g = img[y,x,1]
        r = img[y,x,2]
        bgr = str(b)+','+str(g)+','+str(r)
        cv.putText(img,bgr,(x,y),cv.FONT_HERSHEY_PLAIN,1,(255,0,0),1)
        cv.imshow('Image',img)
        
        
img = cv.imread('resources/dog.jpg')
cv.imshow('Image',img)

cv.setMouseCallback('Image',mouse_event)

cv.waitKey(0)
cv.destroyAllWindows()

