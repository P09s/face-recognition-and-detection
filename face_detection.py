import cv2 as cv

img = cv.imread('Photos/bro.jpg')
cv.imshow('bro', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

haar_cascade = cv.CascadeClassifier('haar_face.xml')
face_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)
print(f'No. of faces detected = {len(face_rect)}')

for (x, y, w, h) in face_rect:
    cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)

cv.imshow('detected faces', img)

cv.waitKey(0)