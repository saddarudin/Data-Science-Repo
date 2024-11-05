import cv2 as cv

img = cv.imread('resources/warp.png')

# let us access the pixel at 100,200

px = img[100,200]
print(px)

# accessing color channel of the pixel

blue = img[100,200,0]
green = img[100,200,1]
red = img[100,200,2]
print(blue,green,red)