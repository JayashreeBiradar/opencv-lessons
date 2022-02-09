import cv2
from cv2 import VideoCapture 

print(cv2.__version__)

rows = int(input("Boss, enter the rows number:"))
columns =int(input("Enter the columns number:"))

width=1280 
height=720

cam = cv2.VideoCapture(0)

cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

while True:
    ignore, frame=cam.read()
    frame =cv2.resize(frame,(int(width/columns),int(height/columns)))

    for i in range(0,rows):
        for j in range(0,columns):
            windName = "Window"+str(i)+"x"+str(j)
            cv2.imshow(windName, frame)
            cv2.setWindowProperty(windName, cv2.WND_PROP_TOPMOST, 1)
            cv2.moveWindow(windName, int(width/columns)*j, int(height/columns)*i)  

    #cv2.setWindowProperty(windName, cv2.WND_PROP_TOPMOST, 0)
    if cv2.waitKey(1)&0xFF==ord('q'):
        cv2.destroyAllWindows()
        break

cam.release()
