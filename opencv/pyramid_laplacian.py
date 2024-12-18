import cv2 as cv

img = cv.imread('resources/hand.jpg')

# Laplacian Pyramid
# A level in Laplacian Pyramid is formed by the difference between 
# that level in Gaussian Pyramid and expanded version of its upper level in Gaussina Pyramid

layer = img.copy()
gp = [layer]

for i in range(6):
    layer = cv.pyrDown(layer)
    gp.append(layer)
    
layer = gp[5]
cv.imshow('Upper Level Gaussian Pyramid',layer)
lp = [layer]

for i in range(5,0,-1):
    gaussian_extended = cv.pyrUp(gp[i])
    laplacian = cv.subtract(gp[i-1],gaussian_extended)
    cv.imshow(str(i),laplacian)
    
cv.imshow('Original',img)
cv.waitKey(0)
cv.destroyAllWindows()