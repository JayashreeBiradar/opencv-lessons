import cv2
import face_recognition as FR
print(cv2.__version__)
import os
from datetime import datetime

font=cv2.FONT_HERSHEY_SIMPLEX
width=640
height=360

path='attendance-system/employee-images'
employeeFaces=[]
employeeNames=[]
empImageList=os.listdir(path)
print(empImageList)

for empImage in empImageList:
    curImage=cv2.imread(f'{path}/{empImage}')
    employeeFaces.append(curImage)
    employeeNames.append(os.path.splitext(empImage)[0])
print(employeeNames)

def encodeEmpImages(employeeFaces):
    empEncodeList=[]
    for empFace in employeeFaces:
        empEncode=FR.face_encodings(empFace)[0]
        empEncodeList.append(empEncode)
    return empEncodeList

encodeListKnown=encodeEmpImages(employeeFaces)
print(len(encodeListKnown))

def markAttendance(name):
    with open('attendance-system/employee-logbook/attendance.csv','r+') as f:
        myDataList=f.readlines()
        nameList=[]
        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])
        if name not in nameList:
            now=datetime.now()
            dtString=now.strftime('%H:%M:%S')
            f.writelines(f'\n{name},{dtString}')


cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

while True:
    ignore,unknownFace=cam.read()
    #unknownFaceSmall=cv2.resize(unknownFace,(0,0),None,0.25,0.25)
    unknownFaceBGR=cv2.cvtColor(unknownFace,cv2.COLOR_RGB2BGR)
    faceLocations=FR.face_locations(unknownFaceBGR)
    unknownEncodings=FR.face_encodings(unknownFaceBGR,faceLocations)

    for faceLocation,unknownEncoding in zip(faceLocations,unknownEncodings):
        top,right,bottom,left=faceLocation
        print(faceLocation)
        cv2.rectangle(unknownFace,(left,top),(right,bottom),(255,0,0),3)
        name='unknown Person'

        match=FR.compare_faces(encodeListKnown,unknownEncoding)
        if True in match:
            matchIndex=match.index(True)
            print(matchIndex)
            name=employeeNames[matchIndex]
            print(name)
            cv2.putText(unknownFace,name,(left,top),font,0.5,(0,0,255),2) 
            markAttendance(name)
       
    cv2.imshow('My Attendance',unknownFace)
    cv2.moveWindow('My Attendance',0,0)
    if cv2.waitKey(1)& 0xFF==ord('q'):
        break
    
cv2.destroyAllWindows()
cam.release()