import cv2
from cv2 import COLOR_BGR2HSV
print(cv2.__version__)
import numpy as np 

def objTrack1(value):
    global HueLow 
    HueLow=value
    print("HueLow:",HueLow)
def objTrack2(value):
    global HueHigh
    HueHigh=value
    print("HueHigh:",HueHigh)
def objTrack3(value):
    global SatLow
    SatLow=value
    print("SatLow:",SatLow)
def objTrack4(value):
    global SatHigh
    SatHigh=value
    print("SatHigh:",SatHigh)
def objTrack5(value):
    global ValLow
    ValLow=value
    print("ValLow:",ValLow)
def objTrack6(value):
    global ValHigh
    ValHigh=value
    print("ValHigh:",ValLow)
def objTrack7(value):
    global newHueLow 
    newHueLow=value
    print("newHueLow:",newHueLow)
def objTrack8(value):
    global newHueHigh
    newHueHigh=value
    print("newHueHigh:",newHueHigh)

width=360
height=180

cv2.namedWindow('ObjTracker')
cv2.resizeWindow('ObjTracker',320,320)
cv2.moveWindow('ObjTracker',360,0)
cv2.createTrackbar('HueLow','ObjTracker',10,179,objTrack1)
cv2.createTrackbar('HueHigh','ObjTracker',20,179,objTrack2)
cv2.createTrackbar('newHueLow','ObjTracker',10,179,objTrack7)
cv2.createTrackbar('newHueHigh','ObjTracker',20,179,objTrack8)
cv2.createTrackbar('SatLow','ObjTracker',10,255,objTrack3)
cv2.createTrackbar('SatHigh','ObjTracker',250,255,objTrack4)
cv2.createTrackbar('ValLow','ObjTracker',10,255,objTrack5)
cv2.createTrackbar('ValHigh','ObjTracker',250,255,objTrack6)

# creating a video capture object
cam = cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

while True:
    ignore, frame=cam.read()
    frame2=frame[::]

    frameHSV=cv2.cvtColor(frame,COLOR_BGR2HSV)
    #frameHSV2=cv2.cvtColor(frame,COLOR_BGR2HSV)
    frameHSV2=frameHSV[::]

    lowerBound=np.array([HueLow,SatLow,ValLow])
    upperBound=np.array([HueHigh,SatHigh,ValHigh])
    lowerBound2=np.array([newHueLow,SatLow,ValLow])
    upperBound2=np.array([newHueHigh,SatHigh,ValHigh])

    myMask=cv2.inRange(frameHSV,lowerBound,upperBound)
    myMask2=cv2.inRange(frameHSV2,lowerBound2,upperBound2)

    myObject=cv2.bitwise_and(frame,frame,mask=myMask)
    myObject2=cv2.bitwise_and(frame2,frame2,mask=myMask2)

    myObjectsmall=cv2.resize(myObject,(int(width),int(height)))
    cv2.imshow('My Object',myObjectsmall)
    cv2.moveWindow('My Object',int(width/2),int(height/2))
    myObjectsmall2=cv2.resize(myObject2,(int(width),int(height)))
    cv2.imshow('My Object2',myObjectsmall2)
    cv2.moveWindow('My Object2',0,500)

    myMasksmall=cv2.resize(myMask,(int(width/2),int(height/2)))
    myMasksmall2=cv2.resize(myMask2,(int(width/2),int(height/2)))
    #cv2.imshow('my HSV',frameHSV)
    cv2.imshow('my Mask',myMasksmall)
    cv2.imshow('my Mask2',myMasksmall2)

    result= 255*(myMasksmall+myMasksmall2)
    result=result.clip(0,255).astype("uint8")
    cv2.imshow('Result',result)

    result2= (myObjectsmall+myObjectsmall2)
    #result2=cv2.bitwise_and(frame,frame,mask=result)
    result2=result2.clip(0,255).astype("uint8")
    #cv2.resize(result2,(720,360))
    cv2.imshow('Result2',result2)

    cv2.imshow('My Webcam',frame)
    cv2.moveWindow('My Webcam', 0, 0)

    if cv2.waitKey(1)&0xFF==ord('q'):
        break
cam.release()    