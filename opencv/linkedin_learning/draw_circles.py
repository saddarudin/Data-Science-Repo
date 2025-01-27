import cv2 as cv
import numpy as np

canvas = np.ones((400,400,3),'uint8')*255
color = (0,255,0)
pressed=False

def draw_circle(event,x,y,flags,params):
    
    global canvas, color, pressed
    if event==cv.EVENT_LBUTTONDOWN:
        cv.circle(canvas,(x,y),3,color,-1)
        pressed=True
    elif event==cv.EVENT_MOUSEMOVE and pressed==True:
        cv.circle(canvas,(x,y),3,color,-1)
    elif event==cv.EVENT_RBUTTONDOWN:
        if color == (255,0,0):
            color=(0,255,0)
        else:
            color=(255,0,0)
        pressed=False
        

cv.namedWindow('canvas')
cv.setMouseCallback('canvas',draw_circle)

while True:
    cv.imshow('canvas',canvas)
    if cv.waitKey(1) & 0xFF==ord('q'):
        break


cv.destroyAllWindows()        
    