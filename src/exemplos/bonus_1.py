# coding: windows-1252
import os
import cv2

cv2path = os.path.join(os.path.dirname(cv2.__file__), 'data')

face_cascade = cv2.CascadeClassifier(os.path.join(cv2path, 'haarcascade_frontalface_default.xml'))
eye_cascade = cv2.CascadeClassifier(os.path.join(cv2path, 'haarcascade_eye.xml'))

img_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'img')

img = cv2.imread(os.path.join(img_dir, 'rosto1.jpg'))

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
 
faces = face_cascade.detectMultiScale(gray, 1.1, 5, minSize=(30,30))
 
for (x,y,w,h) in faces:
  cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

  roi_gray = gray[y:y+h, x:x+w]
  roi_color = img[y:y+h, x:x+w]
  
  eyes = eye_cascade.detectMultiScale(roi_gray)

  for (ex,ey,ew,eh) in eyes:
    cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)


cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()