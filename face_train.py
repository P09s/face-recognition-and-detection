import os
import cv2 as cv
import numpy as np

things = ['apple', 'book', 'chair']
DIR = r'C:\Users\Administrator\Downloads\train'


haar_cascade = cv.CascadeClassifier('haar_face.xml')

features = []
labels = []
def create_train():
    for object in things: 
        path = os.path.join(DIR, object)
        label = things.index(object)

        for img in os.listdir(path):
            img_path = os.path.join(path, img)


            img_array = cv.imread(img_path)
            grey = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)

            faces_rect = haar_cascade.detectMultiScale(grey, scaleFactor=1.1, minNeighbors = 4 )

            for (x, y, w, h) in faces_rect:
                faces_roi = grey[y:y+h, x:x+w]
                features.append(faces_roi)
                labels.append(label)
create_train()

print('Training done !')
# print(f'Length of the features = {len(features)}')
# print(f'Length of the labels = {len(labels)}')

features = np.array(features, dtype=object)
labels = np.array(labels)

face_recognizer = cv.face.LBPHFaceRecognizer_create()

face_recognizer.train(features,labels)

face_recognizer.save('face_trained.yml')
np.save('features.npy', features)
np.save('labels.npy', labels)