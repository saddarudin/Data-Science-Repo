import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread('resources/colours.jpg',0)
ret,mask = cv.threshold(img,220,255,cv.THRESH_BINARY_INV)

kernel = np.ones((3,3),np.uint8)
dilation = cv.dilate(mask,kernel,iterations=3)
erosion = cv.erode(mask,kernel,iterations=2)
# opening means erosion followed by dilation
# closing means dilation followed by erosion
opening = cv.morphologyEx(mask,cv.MORPH_OPEN,kernel,iterations=2)
closing = cv.morphologyEx(mask,cv.MORPH_CLOSE,kernel,iterations=2)

images = [img,mask,dilation,erosion,opening,closing]
titles = ['Original','Mask','Dilation','Erosion','Opening','Closing']



for i in range(len(images)):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.axis('off')
    
plt.show()