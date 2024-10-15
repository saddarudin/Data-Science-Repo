import cv2 as cv

cap = cv.VideoCapture(0)

while cap.isOpened():
    ret,frame = cap.read()
    if not ret:
        print("Webcam stopped")
        break
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
    cv.imshow('webcam',frame)
    
cap.release()
cv.destroyAllWindows()
