import cv2
import time

print(cv2.__version__)

fps=0
tPosition=(30,60)
tFont=cv2.FONT_HERSHEY_SIMPLEX
tHeight=1.5
tThick=3
tColor=(0,0,255)

# Initialize the USB camera (usually the first camera is at 0)
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()


try:
    while True:
        tStart=time.time()
        # Capture frame-by-frame
        ret, frame = cap.read()
        
        # if frame is read correctly ret is True
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        
        #cv2.putText(frame,str(int(fps))+' FPS',tPosition,tFont,tHeight,tColor,tThick)
        cv2.imshow("Camera", frame )
        
        # Break the loop when 'q' is pressed
        if cv2.waitKey(1) == ord('q'):
            break

        tEnd=time.time()
        loopTime=tEnd-tStart
        fps=.9*fps + .1*(1/loopTime)


finally:
    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()