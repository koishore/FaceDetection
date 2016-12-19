import cv2
import sys
import random

def detect(ImagePath):
    # get cascade path
    cascPath = 'haarcascade_frontalface_default.xml'

    #create the haar cascade
    faceCascade = cv2.CascadeClassifier(cascPath)

    #read image and convert to grayscale
    image = cv2.imread(ImagePath)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    #detect faces in the image
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags = cv2.cv.CV_HAAR_SCALE_IMAGE
    )

    #prints the number of faces in the terminal
    print("Found {0} faces!".format(len(faces)))

    #draw a different coloured rectangle around each face
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (random.randint(0,255), random.randint(0,255), random.randint(0,255)), 2)

    cv2.imwrite(ImagePath, image)
