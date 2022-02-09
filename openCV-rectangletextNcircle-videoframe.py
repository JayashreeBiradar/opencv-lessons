import time
import cv2
from cv2 import imshow
from cv2 import waitKey
from cv2 import rectangle
print(cv2.__version__)

width=640
height=320

myText="Hello..."
cam = cv2.VideoCapture(0)

start = time.time()
numberOf_frames=120
frames_p_sec=0

while (numberOf_frames>0):

    ignore, frame=cam.read()
    #frame[rowspt(Hs):rowfpt(Ws),colspt(He):colfpt(We)]
    frame[140:220,250:390]=(0,255,0)

    #rect[frame,(He,Hs),(We,Ws)]
    cv2,rectangle(frame,(250,140),(390,220),(225,0,0),2)

    #circle[frame,(Wdt/2,Ht/2),Radius,color,Thick]
    cv2.circle(frame,(320,180),25,(0,0,0),4)

    cv2.putText(frame,myText,(210,75),(cv2.FONT_HERSHEY_DUPLEX),1,(0,0,255),1)
    cv2.putText(frame,str(int(frames_p_sec)),(0,25),cv2.FONT_HERSHEY_DUPLEX,1,(0,255,255),1)

    imshow('My Frame',frame)
    cv2.resizeWindow('My Frame',width,height)
    numberOf_frames=numberOf_frames-1
    stopTime=time.time()
    timeTaken=stopTime-start
    print("Time taken:",format(timeTaken))
    #Frames/sec
    frames_p_sec=120/timeTaken
    print("FPS:",frames_p_sec)

    if waitKey(1) & 0xFF==ord('q'):
        break

cam.release()
