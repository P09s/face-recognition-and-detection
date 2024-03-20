import cv2 as cv
import numpy as np

haar_cascade = cv.CascadeClassifier('haar_face.xml')

things = ['apple', 'book', 'chair']
# features = np.load('features.npy')
# labels = np.load('labels.npy')

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('face_trained.yml')

img = cv.imread(r'C:\Users\Administrator\Downloads\train\chair\depositphotos_8346493-stock-photo-wooden-chair-over-white-with')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('chair', gray)

face_rect = haar_cascade.detectMultiScale(gray, 1.1, 4)

for (x, y, h, w) in face_rect:
    face_roi = gray[y:y+h, x:x+w]

    label, confidence = face_recognizer.predict(face_roi)
    print(f'Label = {things[label]} with a confidence of {confidence}')

    cv.putText(img, str(things[label]), (20,20), cv.FONT_HERSHEY_COMPLEX, 1.0, (0,255,0), thickness=2)
    cv.rectangle(img, (x,y), (x+w, y+h), (0,255,0), thickness=2)

cv.imshow('detected face', img)
cv.waitKey(0)