# Python-opencv-face-recognition
Python+Opencv识别视频统计人数
如需远程调试，可加QQ905733049由专业技术人员远程协助！
运行代码如下：
#!/usr/bin/python
# -*- coding: utf-8 -*-
import cv2
import numpy as np
face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
eye_cascade=cv2.CascadeClassifier("haarcascade_eye.xml")
cap=cv.VideoCapture('1.mp4')
while True:
    ret,frame=cap.read()
    i=frame
       # print i.shape
    gray=cv2.cvtColor(i,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray,1.3,5)
    eyes=eye_cascade.detectMultiScale(gray,1.3,5)
    l=len(faces)
    print(l)
    for (x,y,w,h) in faces:
        cv2.rectangle(i,(x,y),(x+w,y+h),(255,0,0),2)
        cv2.putText(i,'face',(w//2+x,y-h//5),cv2.FONT_HERSHEY_PLAIN,2.0,(255,255,255),2,1)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = i[y:y+h, x:x+w]
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
            cv2.putText(i,face count",(20,20),cv2.FONT_HERSHEY_PLAIN,2.0,(255,255,255),2,1)
            cv2.putText(i,str(l),(230,20),cv2.FONT_HERSHEY_PLAIN,.0,(255,255,255),2,1)
    cv2.imshow("rstp",i)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        exit(0)


