import cv2 as cv

img = cv.imread('resources/dog.jpg')

count = 1
def get_coordinates(event,x,y,flags,param):
    if event == cv.EVENT_LBUTTONDOWN:
        global count, x1,x2,y1,y2
        if count==1:
            x1,y1 = x,y
            count = 2
        else:
            x2,y2 = x,y
            cv.rectangle(img,(x1,y1),(x2,y2),(0,255,0),1)
            count = 1
        print(x1,y1,x2,y2)
        


x1,y1,x2,y2 = 0,0,0,0
cv.namedWindow('image',cv.WINDOW_NORMAL)

while True:
    cv.imshow('image',img)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
    cv.setMouseCallback('image',get_coordinates)
cv.destroyAllWindows()

#now to get roi from image we can use slicing
# img[y1:y2,x1:x2] will give us the roi
roi = img[y1:y2,x1:x2]
cv.imshow('roi',roi)
cv.imwrite('resources/dog_head.jpg',roi)
cv.waitKey(0)
cv.destroyAllWindows()

    