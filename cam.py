#pip install opencv-contrib-python
#pip install cvzone
#pip install pyautogui

import cv2
from cvzone.HandTrackingModule import HandDetector
import pyautogui

detector = HandDetector(detectionCon=0.5,maxHands=4)

cam = cv2.VideoCapture(0)

cam.set(3,600)
cam.set(4,400)

while True:
    success,frame = cam.read()
    img= cv2.flip(frame,1)
    hand,img = detector.findHands(img)
    
    if hand and hand[0]['type'] == "Left":
        fingers=detector.fingersUp(hand[0])
        totalFingers=fingers.count(1)
        cv2.putText(img, f'Fingers:{totalFingers}',(50,50),cv2.FONT_HERSHEY_PLAIN,2,(0,255,0))
        if totalFingers==5:
            pyautogui.keyDown('right')
            pyautogui.keyUp('left')
        if totalFingers==0:
            pyautogui.keyDown('left')
            pyautogui.keyUp('right')
    cv2.imshow('Livefeed',img)
    cv2.waitKey(1)

      