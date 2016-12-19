import time
import cv2
import face_detect
import os

camera = cv2.VideoCapture(0)
cv2.namedWindow("Face Detection")
count = 1

while 1:
    return_value, frame = camera.read()
    cv2.imshow("Face Detection", frame)
    if not return_value:
        break
    k = cv2.waitKey(1)

    if k%256 == 27:
    # ESC pressed
        print("You have pressed Escape. Program terminating...")
        break
    elif k%256 == 32:
    # SPACE pressed
        while os.path.exists("images/detected{}.png".format(count)):
            count += 1
        img_name = "images/facedetect{}.png".format(count)
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        count += 1
        face_detect.detect("{}".format(img_name))

camera.release()

cv2.destroyAllWindows()
