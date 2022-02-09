from tkinter import EventType
import cv2
from cv2 import EVENT_LBUTTONDOWN
from cv2 import EVENT_RBUTTONUP
print(cv2.__version__)

import numpy as np

width=1280
height=720

frame=np.zeros((256,720,3), dtype=np.uint8)
frame[::]=(0,0,0)

for rows in range(0,256,1):
    for columns in range(0,720,1):
        frame[rows, columns]=(int(columns/4),rows,255)
x=cv2.cvtColor(frame,cv2.COLOR_HSV2BGR)

for rows in range(0,256,1):
    for columns in range(0,720,1):
        frame[rows, columns]=(int(columns/4),255,rows)
y=cv2.cvtColor(frame,cv2.COLOR_HSV2BGR)

while True:   

    cv2.imshow('my HSV',x)
    cv2.moveWindow('my HSV',0,0)

    cv2.imshow('my HSV2',y)
    cv2.moveWindow('my HSV2',0,300)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()
