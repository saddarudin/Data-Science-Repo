import cv2 as cv
from tkinter import Tk, filedialog
from PIL import Image

def find_coords(event,x,y,flags,params):
    if event == cv.EVENT_RBUTTONDOWN:
        b = img[y,x,0]
        g = img[y,x,1]
        r = img[y,x,2]
        colorCode = 'rgb=('+str(r)+','+str(g)+','+str(b)+')'
        cv.putText(img,colorCode,(x,y),cv.FONT_HERSHEY_DUPLEX,0.5,(0,0,0),1)
        cv.imshow('image',img)



root = Tk()
root.withdraw() 
file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.png;*.jpeg")])

if file_path:
    img = Image.open(file_path)
    img = cv.imread(file_path)
    cv.imshow('image',img)
    cv.setMouseCallback('image',find_coords)
    cv.waitKey(0)
    cv.destroyAllWindows()
else:
    print("No image selected.")
