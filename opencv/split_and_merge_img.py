import cv2 as cv

img = cv.imread('resources/warp.png')
img = cv.resize(img,(200,200))

b,g,r = cv.split(img)


# cv.imshow('blue',b)
# cv.imshow('green',g)
# cv.imshow('red',r)

merge1 = cv.merge([r,g,b])
merge5 = cv.merge([r,b,g])
merge2 = cv.merge([g,b,r])
merge3 = cv.merge([g,r,b])
merge4 = cv.merge([b,r,g])
merge5 = cv.merge([b,g,r])
cv.imshow('rgb',merge1)
cv.imshow('rbg',merge2)
cv.imshow('gbr',merge3) 
cv.imshow('grb',merge4)
cv.imshow('brg',merge5)
cv.imshow('original',img)
if cv.waitKey(0) & 0xFF == ord('q'):
    cv.destroyAllWindows()