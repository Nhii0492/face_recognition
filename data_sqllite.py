import cv2
import os
import sqlite3

def manage_students(id, name):
    with sqlite3.connect("/Users/nguyennhi/PycharmProjects/pythonProject4/data.db") as connection:
        cursor = connection.cursor()

        id = int(id)
        cursor.execute("SELECT * FROM Students WHERE ID=?", (id,))
        existing_student = cursor.fetchone()

        if existing_student is None:
            cursor.execute("INSERT INTO Students (ID, Name) VALUES (?, ?)", (id, name))
        else:
            cursor.execute("UPDATE Students SET Name=? WHERE ID=?", (name, id))

        connection.commit()

cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

id = input("Nhập ID của bạn :")
name = input("Nhập họ và tên của : ")

if id.strip() and name.strip():
    manage_students(id, name)
else:
    print("ID và tên không được để trống")
    exit(1)

index_std = 0

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

        if not os.path.exists('dataset'):
            os.makedirs('dataset')

        index_std += 1
        cv2.imwrite(f'dataset/Student.{id}.{index_std}.jpg', gray[y:y + h, x:x + w])

    cv2.imshow("DETECTING FACE", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    if index_std >= 100:
        break

cap.release()
cv2.destroyAllWindows()
