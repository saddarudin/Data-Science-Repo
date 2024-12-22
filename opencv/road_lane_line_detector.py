import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('resources/road.jpeg')
img = cv.cvtColor(img,cv.COLOR_BGR2RGB)
height = img.shape[0]
width = img.shape[1]
roi_vertices = [(0,height),(width/2,height/2),(width,height)]

def roi(img,vertices):
    mask = np.zeros_like(img)
    channel_count = img.shape[2]
    match_mask_color = (255,)*channel_count
    cv.fillPoly(mask,[vertices],match_mask_color)
    masked_image = cv.bitwise_and(img,mask)
    return masked_image

cropped_image = roi(img,np.array([roi_vertices],np.int32))
plt.imshow(cropped_image)
plt.show()
# cv.imshow('Original Image',img)
# cv.waitKey(0)
# cv.destroyAllWindows()