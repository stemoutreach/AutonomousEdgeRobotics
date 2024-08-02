import cv2
import time
import numpy as np

print(cv2.__version__)


# Initialize the USB camera (usually the first camera is at 0)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Cannot open camera")
    exit()

fps=0
tPosition=(30,60)
tFont=cv2.FONT_HERSHEY_SIMPLEX
tHeight=1.5
tThick=3
tColor=(0,0,255)


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
    print('Hue Low',valHigh)


cv2.namedWindow('myTracker')

cv2.createTrackbar('Hue Low','myTracker',10,179,onTrack1)
cv2.createTrackbar('Hue High','myTracker',44,179,onTrack2)
cv2.createTrackbar('Sat Low','myTracker',80,255,onTrack3)
cv2.createTrackbar('Sat High','myTracker',255,255,onTrack4)
cv2.createTrackbar('Val Low','myTracker',40,255,onTrack5)
cv2.createTrackbar('Val High','myTracker',255,255,onTrack6)

while True:

    tStart=time.time()
    ret, frame = cap.read()
 
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    frame_height, frame_width, _ = frame.shape
    lowerBound=np.array([hueLow,satLow,valLow])
    upperBound=np.array([hueHigh,satHigh,valHigh])
    frameHSV=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    myMask=cv2.inRange(frameHSV,lowerBound,upperBound)
    myMaskSmall=cv2.resize(myMask,(int(frame_width/2),int(frame_height/2)))
    myObject=cv2.bitwise_and(frame, frame, mask=myMask)
    myObjectSmall=cv2.resize(myObject,(int(frame_width/2),int(frame_height/2)))
    cv2.putText(frame,str(int(fps))+' FPS',tPosition,tFont,tHeight,tColor,tThick)
    cv2.imshow("Camera", frame)
    cv2.imshow('my Mask',myMaskSmall)
    cv2.imshow('My Objest',myObjectSmall)
    if cv2.waitKey(1)==ord('q'):
        break
    tEnd=time.time()
    loopTime=tEnd-tStart
    fps=.9*fps + .1*(1/loopTime)
cv2.destroyAllWindows()