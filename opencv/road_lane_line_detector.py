import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

def roi(img,vertices):
    mask = np.zeros_like(img)
    match_mask_color = 255
    cv.fillPoly(mask,[vertices],match_mask_color)
    masked_image = cv.bitwise_and(img,mask)
    return masked_image


def draw_lines(img,lines):
    img = np.copy(img)
    blank_img = np.zeros((img.shape[0],img.shape[1],3),dtype=np.uint8)
    for line in lines:
        for x1,y1,x2,y2 in line:
            cv.line(blank_img,(x1,y1),(x2,y2),(0,255,0),5)
    img = cv.addWeighted(img,0.8,blank_img,1,0.0)
    return img
    

img = cv.imread('resources/road.jpeg')
img = cv.cvtColor(img,cv.COLOR_BGR2RGB)
height = img.shape[0]
width = img.shape[1]
roi_vertices = [(0,height),(width/2,height/2),(width,height)]
gray_image = cv.cvtColor(img,cv.COLOR_RGB2GRAY)
canny_image = cv.Canny(gray_image,100,200)
cropped_image = roi(canny_image,np.array([roi_vertices],np.int32))
lines = cv.HoughLinesP(cropped_image,6,np.pi/60,160,np.array([]),minLineLength=40,maxLineGap=25)
img_with_lines = draw_lines(img,lines)


plt.imshow(img_with_lines)
plt.show()
# cv.imshow('Canny Image',canny_image)
# cv.waitKey(0)
# cv.destroyAllWindows()