import cv2 as cv
import numpy as np

def draw(event,x,y,flags,param):
    if event == cv.EVENT_LBUTTONDBLCLK:
        cv.circle(img,(x,y),10,(255,0,0),-1)
    elif event ==  cv.EVENT_RBUTTONDBLCLK:
        cv.rectangle(img,(x,y),(x+30,y+10),(0,255,0),2)
        
cv.namedWindow('window',cv.WINDOW_NORMAL)
img = np.zeros((500,500,3),np.uint8)
cv.setMouseCallback('window',draw)

while True:
    cv.imshow('window',img)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cv.destroyAllWindows()