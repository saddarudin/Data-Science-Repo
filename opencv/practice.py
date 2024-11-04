import cv2 as cv
import numpy as np

def mouse_event(event,x,y,flags,param):
    if event == cv.EVENT_LBUTTONDOWN:
        b = img[y,x,0]
        g = img[y,x,1]
        r = img[y,x,2]
        cv.putText(img,f'{b},{g},{r}',(x,y),cv.FONT_HERSHEY_DUPLEX,1,(0,0,255),2)
        

cv.namedWindow('window',cv.WINDOW_NORMAL)
img = np.ones((500,500,3),np.uint8)*255


cv.setMouseCallback('window',mouse_event)

while True:
    cv.imshow('window',img)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break 
    
cv.destroyAllWindows() 