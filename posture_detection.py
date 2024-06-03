import cv2 as cv
import numpy as np
import mediapipe as mp
import time
from mediapipe.python.solutions.drawing_utils import DrawingSpec

landmark_drawing_spec = DrawingSpec(color=(0, 0, 255), thickness=2, circle_radius=2)  # Green color for landmarks
connection_drawing_spec = DrawingSpec(color=(0, 255, 0), thickness=2)  # Red color for connections

class poseDetector():
    def __init__(self, mode=False, complexity =1, upBody = True, smooth = True, detectioncon = 0.5, trackcon = 0.5):
        self.mode = mode
        self.complexity = complexity
        self.upBody = upBody
        self.smooth = smooth
        self.detectioncon = detectioncon
        self.trackcon = trackcon
        self.mpDraw = mp.solutions.drawing_utils
        self.mpPose = mp.solutions.pose
        self.pose = self.mpPose.Pose(self.mode,self.complexity,self.upBody,self.smooth,self.detectioncon ,self.trackcon)

    def findPose(self , img, draw=True):
        
        imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        self.results = self.pose.process(imgRGB)
    
        if self.results.pose_landmarks:
            if draw:
                self.mpDraw.draw_landmarks(img, self.results.pose_landmarks,self.mpPose.POSE_CONNECTIONS,landmark_drawing_spec,connection_drawing_spec)

        return img

        
    def findPosition(self,img,draw=True):
        lmList=[]
        if self.results.pose_landmarks:
            for id, lm in enumerate(self.results.pose_landmarks.landmark):
                h,w,c = img.shape
                
                cx, cy = int(lm.x*w), int(lm.y*h)
                lmList.append([id,cx,cy])
                if draw:
                    cv.circle(img,(cx,cy),8,(255,0,0),cv.FILLED)

        return lmList


def main():
    pTime = 0


    cap = cv.VideoCapture('Posture_detection/videos/sample-3.mp4')

    detector = poseDetector()
    while True:
        success, img = cap.read()
        img = detector.findPose(img)
        lmList = detector.findPosition(img)
        print(lmList)
        #FPS
        cTime = time.time()
        fps = 1/(cTime-pTime)
        pTime = cTime
        cv.putText(img, str(int(fps)),(70,50),cv.FONT_HERSHEY_PLAIN,3,(0,255,0), 3)
        cv.imshow("Image",img)
        cv.waitKey(20)


if __name__ == "__main__":
    main()