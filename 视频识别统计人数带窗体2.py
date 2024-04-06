# _*_ coding:utf-8 _*_

from tkinter import filedialog
import tkinter.messagebox

from PIL import Image
from PIL import ImageTk
import cv2
import numpy as np

def select_vedio():
    # grab a reference to the image panels

    path = filedialog.askopenfilename(title='打开', filetypes=[('S2out', '*.*'), ('All Files', '*')])
    print(path)


    if len(path) > 0:
        # 视频人数统计
        face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        eye_cascade=cv2.CascadeClassifier("haarcascade_eye.xml")
        cap=cv2.VideoCapture(path)
        while True:
            ret,frame=cap.read()
            i=frame
               # print i.shape

            for (x,y,w,h) in faces:
                cv2.rectangle(i,(x,y),(x+w,y+h),(255,0,0),2)
                cv2.putText(i,'face',(w//2+x,y-h//5),cv2.FONT_HERSHEY_PLAIN,2.0,(255,255,255),2,1)
                roi_gray = gray[y:y+h, x:x+w]


        # if the panels are None, initialize them
        if panelA is None or panelB is None:
            # the first panel will store our original image
            panelA = Label(image=image)



        # otherwise, update the image panels
        else:
            # update the pannels
            panelA.configure(image=image)
            panelB.configure(image=edged)

            panelB.image = edged


 
root = tkinter.Tk()
panelA = None
panelB = None
root.title("视频人数统计")  
root.geometry('500x300+500+200')

btn2 = tkinter.Button(root, text='视频人数统计',font = ('microsoft yahei',14,''),width=10,height=2, command=select_vedio)
btn3 = tkinter.Button(root, text='退出',font = ('microsoft yahei',14,''),width=10,height=2, command=root.quit)


btn2.place(x=80,y=112)
btn3.place(x=240,y=112)



root.mainloop()


