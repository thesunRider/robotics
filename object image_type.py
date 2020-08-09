
import cv2
import numpy as np
import matplotlib.pyplot as plt

object_classifier = cv2.CascadeClassifier('Haarcascades/haarcascade_shape.xml')

# Open Image
image = cv2.imread('object.jpg')
fix_img = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
plt.imshow(fix_img)


# Detect objects
objects = object_classifier.detectMultiScale(image,1.3,5)


# No objects Detected
if objects is ():
    print('No objects found')
#function declaration
def detect_face(fix_img):
    face_rects = face_classifier.detectMultiScale(fix_img)

    for (x,y,w,h) in face_rects:
        cv2.rectangle(fix_img,
                     (x,y),
                     (x+w,y+h),
                     (255,0,0),
                     10)
    return fix_img

result = detect_face(fix_img)
plt.imshow(result)
