import cv2
import time
import numpy as np
print(cv2.__version__)

dispW=1280
dispH=720

fps=0
tPosition=(30,60)
tFont=cv2.FONT_HERSHEY_SIMPLEX
tHeight=1.5
tThick=3
tColor=(0,0,255)
track=0
# Initialize the USB camera (usually the first camera is at 0)
cap = cv2.VideoCapture(0)
#cap.set(cv2.CAP_PROP_FRAME_WIDTH, dispW)
#cap.set(cv2.CAP_PROP_FRAME_HEIGHT, dispH)
if not cap.isOpened():
    print("Cannot open camera")
    exit()

def onTrack1(val):
    global hueLow
    hueLow=val
    print('Hue Low',hueLow)
def onTrack2(val):
    global hueHigh
    hueHigh=val
    print('Hue High',hueHigh)
def onTrack3(val):
    global satLow
    satLow=val
    print('Sat Low',satLow)
def onTrack4(val):
    global satHigh
    satHigh=val
    print('Sat High',satHigh)
def onTrack5(val):
    global valLow
    valLow=val
    print('Val Low',valLow)
def onTrack6(val):
    global valHigh
    valHigh=val
    print('Val High',valHigh)
def onTrack7(val):
    global track
    track=val
    print('Track Value',track)

cv2.namedWindow('myTracker')

cv2.createTrackbar('Hue Low','myTracker',17,179,onTrack1)
cv2.createTrackbar('Hue High','myTracker',52,179,onTrack2)
cv2.createTrackbar('Sat Low','myTracker',111,255,onTrack3)
cv2.createTrackbar('Sat High','myTracker',255,255,onTrack4)
cv2.createTrackbar('Val Low','myTracker',164,255,onTrack5)
cv2.createTrackbar('Val High','myTracker',255,255,onTrack6)
cv2.createTrackbar('Train-0 Track-1','myTracker',0,1,onTrack7)


while True:

    tStart=time.time()
    # Capture frame-by-frame
    ret, frame = cap.read()
    
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    #cv2.putText(frame,str(int(fps))+' FPS',tPosition,tFont,tHeight,tColor,tThick)
    #cv2.imshow("Camera", frame )



    frameHSV=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    cv2.putText(frame,str(int(fps))+' FPS',tPosition,tFont,tHeight,tColor,tThick)
    lowerBound=np.array([hueLow,satLow,valLow])
    upperBound=np.array([hueHigh,satHigh,valHigh])
    myMask=cv2.inRange(frameHSV,lowerBound,upperBound)
    myMaskSmall=cv2.resize(myMask,(int(dispW/2),int(dispH/2)))
    myObject=cv2.bitwise_and(frame,frame, mask=myMask)
    myObjectSmall=cv2.resize(myObject,(int(dispW/2),int(dispH/2)))
    
    contours,junk=cv2.findContours(myMask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    if len(contours)>0:
        contours=sorted(contours,key=lambda x:cv2.contourArea(x),reverse=True)
        #cv2.drawContours(frame,contours,-1,(255,0,0),3)
        contour=contours[0]
        x,y,w,h=cv2.boundingRect(contour)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),3)
        
    cv2.imshow('Camera',frame)
    cv2.imshow('Mask',myMaskSmall)
    cv2.imshow('My Object',myObjectSmall)
    if cv2.waitKey(1)==ord('q'):
        break
    tEnd=time.time()
    loopTime=tEnd-tStart
    fps=.9*fps + .1*(1/loopTime)
cv2.destroyAllWindows()