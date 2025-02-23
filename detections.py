import cv2
import face_recognition
import numpy as np

imgPath = r'C:\Users\varsh\PycharmProjects\facedetection\images\ramya.jpeg'
imgRamya = face_recognition.load_image_file(imgPath)
imgRamya=cv2.cvtColor(imgRamya, cv2.COLOR_BGR2RGB)

imgPath = r'C:\Users\varsh\PycharmProjects\facedetection\images\ramyatest.jpeg'
imgtest = face_recognition.load_image_file(imgPath)
imgtest=cv2.cvtColor(imgtest, cv2.COLOR_BGR2RGB)

fLoc = face_recognition.face_locations(imgRamya)[0]
encodeRamya = face_recognition.face_encodings(imgRamya)[0]
cv2.rectangle(imgRamya,(fLoc[3],fLoc[1]),(fLoc[1],fLoc[2]),(255,0,255),2)

fLoc = face_recognition.face_locations(imgtest)[0]
encodetest = face_recognition.face_encodings(imgtest)[0]
cv2.rectangle(imgtest,(fLoc[3],fLoc[1]),(fLoc[1],fLoc[2]),(255,0,255),2)

results = face_recognition.compare_faces([encodeRamya],encodetest)
facDis = face_recognition.face_distance([encodeRamya],encodetest)
print(results,facDis)

cv2.imshow('ramya',imgRamya)
cv2.imshow('ramyaaa',imgtest)
cv2.waitKey(0)
