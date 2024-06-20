import cv2
import time

print(cv2.__version__)

dispW=1280
dispH=720

fps=0
tPosition=(30,60)
tFont=cv2.FONT_HERSHEY_SIMPLEX
tHeight=1.5
tThick=3
tColor=(0,0,255)

rUpperLeftCol=250
rUpperLeftRow=140
rLowerRightCol=390
rLowerRightRow=220

rUpperLeft=(rUpperLeftCol,rUpperLeftRow)
rLowerRight=(rLowerRightCol,rLowerRightRow)

rColor=(255,255,255)
rThick=4
 
cCenter=(640,360)
cRadius=30
cColor=(255,255,0)
cThick=8

boxW=250
boxH=125
tlC=50
tlR=75
lrC=tlC+boxW
lrR=tlR+boxH
deltaC=2
deltaR=2
thickness=-1
Rcolor=(0,125,255)
# Initialize the USB camera (usually the first camera is at 0)
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, dispW)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, dispH)
if not cap.isOpened():
    print("Cannot open camera")
    exit()


while True:
    tStart=time.time()
    ret, frame = cap.read()
 
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
 
 
    cv2.putText(frame,str(int(fps))+' FPS',tPosition,tFont,tHeight,tColor,tThick)
    #cv2.rectangle(im,rUpperLeft,rLowerRight,rColor,rThick)
    #cv2.circle(im,cCenter,cRadius,cColor,cThick)
    
    if tlC+deltaC<0 or lrC+deltaC>dispW-1:
        deltaC=deltaC*(-1)
    if tlR+deltaR<0 or lrR+deltaR>dispH-1:
        deltaR=deltaR*(-1)
    tlC=tlC+deltaC
    tlR=tlR+deltaR
    lrC=lrC+deltaC
    lrR=lrR+deltaR
    cv2.rectangle(frame,(tlC,tlR),(lrC,lrR),Rcolor,thickness)

    cv2.imshow("Camera", frame)
    if cv2.waitKey(1)==ord('q'):
        break
    tEnd=time.time()
    loopTime=tEnd-tStart
    fps=.9*fps + .1*(1/loopTime)
cv2.destroyAllWindows()
