import cv2
import time
import numpy as np
print(cv2.__version__)


# Initialize the USB camera (usually the first camera is at 0)
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()


while True:

    # Capture frame-by-frame
    ret, frame = cap.read()
    
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    frame_height, frame_width, _ = frame.shape
    frameHSV=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    lowerBound=np.array([10,80,40])
    upperBound=np.array([44,255,255])
    myMask=cv2.inRange(frameHSV,lowerBound,upperBound)
   
    contours,junk=cv2.findContours(myMask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    #Yellow=len(contours)
    #cv2.putText(frame,str(Yellow) + ' yellow blocks',(30,60),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)
    if len(contours)>0:
        contours=sorted(contours,key=lambda x:cv2.contourArea(x),reverse=True)
        #cv2.drawContours(frame,contours,-1,(255,0,0),3)
        contour=contours[0]
        x,y,w,h=cv2.boundingRect(contour)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),3)
        
    cv2.imshow('Camera',frame)
    if cv2.waitKey(1)==ord('q'):
        break

cv2.destroyAllWindows()