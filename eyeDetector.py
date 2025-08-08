import cv2

face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_detector = cv2.CascadeClassifier('haarcascade_eye.xml')

webcam = cv2.VideoCapture(0)

while True:
    successful_frame_read, frame = webcam.read()

    if not successful_frame_read:
        break

    frameGrayscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(frameGrayscale)

    for (x, y, w, h) in faces:
        the_faces = frame[y: y+h, x:x+w]
        faceGrayscale = cv2.cvtColor(the_faces, cv2.COLOR_BGR2GRAY)

        eyes = eye_detector.detectMultiScale(faceGrayscale, scaleFactor= 1.1, minNeighbors=10)

        for (x_, y_, w_, h_) in eyes:
            cv2.rectangle(the_faces, (x_, y_), (x_ + w_, y_ + h_), (205, 250, 255), 4)


    cv2.imshow('Eye Detector', frame)
    cv2.waitKey(1)

webcam.release() 
cv2.destroyAllWindows()
print("Hello ING bro")
