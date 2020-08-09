import cv2
import numpy as np
# Create Classifier
body_classifier = cv2.CascadeClassifier('shapes.xml')
# Capture Video
cap = cv2.VideoCapture(0)
# While Loop
while cap.isOpened():
# Read the capture
    ret,frame = cap.read()

    # Pass the Frame to the Classifier
    bodies = body_classifier.detectMultiScale(frame,1.2,3)

    # if Statement
    if ret ==True:

        # Bound Boxes to Identified Bodies
        for (x,y,w,h) in bodies:
            cv2.rectangle(frame,
                         (x,y),
                         (x+w,y+h),
                         (25,125,255),
                         5)
            cv2.imshow('Pedestrians',frame)

        # Exit with Esc button
        if cv2.waitKey(1) == 27:
            break

    # else Statement
    else:
        break

# Release the Capture & Destroy All Windows
cap.release()
cv2.destroyAllWindows()


# In[ ]:
