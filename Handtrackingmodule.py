import cv2
import time
import mediapipe as mp



class handDetec():
    def __init__(self,mode=False,maxhand=2,detection=0.5,tracking=0.5):
        self.mode=mode
        self.maxhand=maxhand
        self.detection=detection
        self.tracking=tracking
        self.mphand=mp.solutions.hands
        self.hands=self.mphand.Hands(
             self.mode,
             self.maxhand,
             self.detection,
             self.tracking

        )
        self.mpDraw = mp.solutions.drawing_utils


    def findHands(self,img,draw=True):
        imgRgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        self.result=self.hands.process(imgRgb)
    # print(result.multi_hand_landmarks)
        if( self.result.multi_hand_landmarks):
            for handlm in self.result.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img,handlm,self.mphand.HAND_CONNECTIONS)
                

        return img               
    def findPos(self,img,draw=True,HandNo=0):
        lmList=[]
        if( self.result.multi_hand_landmarks):
            myHand=self.result.multi_hand_landmarks[HandNo]
            for id, lm in enumerate(myHand.landmark):
                 h, w, c = img.shape
                 cx, cy = int(lm.x *w), int(lm.y*h)
                 lmList.append([id,cx,cy])
                 if(draw):
                     cv2.circle(img, (cx,cy), 10, (0,255,0), cv2.FILLED)
        return lmList
               
                      





                







# for id, lm in enumerate(handlm.landmark):
#                     # print(id,lm)
#                     h, w, c = img.shape
#                     cx, cy = int(lm.x *w), int(lm.y*h)
               
#                     cv2.circle(img, (cx,cy), 10, (0,255,0), cv2.FILLED)
    
    
    


def main():
    ptime=0
    ctime=0
    cap = cv2.VideoCapture(0)
    detector=handDetec()
    while True:
        success, img = cap.read()
        img=detector.findHands(img)
        marklist=detector.findPos(img)
        if len(marklist) !=0:
            print(marklist[4])
        ctime=time.time()
        fps=1/ (ctime-ptime)
        ptime=ctime
        cv2.putText(img,str(int(fps)),(13,75),cv2.FONT_HERSHEY_PLAIN,2,(0,255,0),2)

        cv2.imshow("Image",img)
        if cv2.waitKey(1) == 13:
            break



if __name__=="__main__":
    main()