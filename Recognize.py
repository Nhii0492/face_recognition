import cv2
import numpy as np
import os
import sqlite3
from PIL import Image

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
recognizer = cv2.face_LBPHFaceRecognizer.create()

recognizer.read('/Users/nguyennhi/PycharmProjects/pythonProject4/recognizer/training.yml')

def profile_students(id):
    with sqlite3.connect("/Users/nguyennhi/PycharmProjects/pythonProject4/data.db") as connection:
        cursor = connection.cursor()

        id = int(id)
        cursor.execute("SELECT * FROM Students WHERE ID=?", (id,))

    inf = None
    for row in cursor:
        inf = row
    connection.close()
    return inf


cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
        roi_gray = gray[y:y + h, x:x + w]
        id, confidence = recognizer.predict(roi_gray)
        if confidence < 50:
            info = profile_students(id)
            if info is not None:
                cv2.putText(frame, f"ID: {id}, Name: {info[1]}", (x + 10, y + h + 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                            (0, 255, 0), 2)
            else:
                cv2.putText(frame, 'Unknown', (x + 10, y + h + 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    cv2.imshow('image', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
