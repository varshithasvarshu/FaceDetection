import pickle

import cv2
import numpy as np
import face_recognition
import os

path = 'Imagesof'
images = []
classNames = []
myList = os.listdir(path)
print(myList)
for cls in myList:
    curImg = cv2.imread(f'{path}/{cls}')
    images.append(curImg)
    classNames.append(os.path.splitext(cls)[0])
print(classNames)
def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList
#
encodeListKnown = findEncodings(images)
encodeListKnownWithId=[encodeListKnown,classNames]
print(encodeListKnownWithId)
file=open('encodeFile.p',"wb")
pickle.dump(encodeListKnownWithId,file)
file.close()
print("file saved")
print('encoding complete')

cap = cv2.VideoCapture(0)

while True:
    success,img = cap.read()
    imgS = cv2.resize(img,(0,0),None,0.25,0.25)
    imgS = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    facesCurFrame = face_recognition.face_locations(imgS)[0]
    encodeCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)
    print(encodeCurFrame)
    for encodeFace,faceLoc in zip(encodeCurFrame,facesCurFrame):
            matches = face_recognition.compare_faces(encodeListKnown,encodeFace)
            distance = face_recognition.face_distance(encodeListKnown,encodeFace)
            print(faceDis)

            matchIndex = np.argmin(distance)
            print("matchindex", matchIndex)
            if matches[matchIndex]:
                name = studentId[matchIndex]
                cv2.putText(img, f"{name}", (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 3, (255, 244, 90), 3)
                print("known face was detected", studentId[matchIndex])

    cv2.imshow('picture',img)
    cv2.waitKey(1)
