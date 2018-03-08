# -*- coding: utf-8 -*-
# Jose Zambudio Bernabeu <zamberjo@gmail.com>

# from picamera.array import PiRGBArray
# from picamera import PiCamera
import time
import cv2
# import telegram

camera = PiCamera()
camera.resolution = (320, 240)
camera.framerate = 30
rawCapture = PiRGBArray(camera, size=(320, 240))
face_cascade = cv2.CascadeClassifier('/home/pi/opencv-3.2.0/data/haarcascades/haarcascade_frontalface_default.xml')
rec = cv2.face.createLBPHFaceRecognizer()
id = 0
font = cv2.FONT_HERSHEY_SIMPLEX
time.sleep(0.1)

for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    image = frame.array
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)


    for(x, y, w, h) in faces:
        image = cv2.rectangle(image,(x, y), (x+w, y+h), (255, 0, 0), 2)
        id, conf = rec.predict(gray[y:y+h, x:x+w])
        if(id == 1):
            id = "negar"

        elif(id == 2):
            id = "professoraerabi"

        cv2.putText(image, str(id), (x,y+h), font, 2, (255,255,255), 3)
              n()




    cv2.imshow("Frame", image)
    key = cv2.waitKey(100) & 0xFF
    rawCapture.truncate(0)
    if key == ord("q"):
         break
