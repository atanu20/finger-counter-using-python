import cv2
import os
import Handtrackingmodule as htm
import time

wcam=688
hcam=488

cap=cv2.VideoCapture(0)
cap.set(3,wcam)
cap.set(4,hcam)

path="img"
finger=[]

listfig=os.listdir(path)
detector=htm.handDetec(detection=0.75)

for im in listfig:
    finger.append(cv2.imread(f'{path}/{im}'))
# print(len(finger))

ptime=0
tipid=[4,8,12,16,20]

while True:
    success, img = cap.read()
    img=detector.findHands(img)
    pointmark=detector.findPos(img,draw=False)
    if( len(pointmark)) !=0:
        fign=[]
         
         
        if(pointmark[tipid[0]][1] > pointmark[tipid[0]-1][1]):
            fign.append(1)
            
        else:
            fign.append(0)


        for id in range(1,5):
            if(pointmark[tipid[id]][2] < pointmark[tipid[id]-2][2]):
               fign.append(1)
            else:
                fign.append(0)
            
        # print(fign.count(1))

        h, w, c =finger[fign.count(1)].shape
        img[30:h+30,30:w+30]=finger[fign.count(1)]

        ctime=time.time()
        fps=1/(ctime-ptime)
        ptime=ctime
        cv2.putText(img,str(int(fps)),(450,50),cv2.FONT_HERSHEY_PLAIN,2,(0,255,0),2)
        cv2.putText(img,"Count: "+str(fign.count(1)),(50,350),cv2.FONT_HERSHEY_PLAIN,2,(0,255,0),2)

                
               
   
    



    cv2.imshow("Image",img)
    if cv2.waitKey(1) == 13:
        break