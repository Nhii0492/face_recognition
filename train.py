import cv2
import numpy as np
import os
from PIL import Image

# Create the LBPH Face Recognizer
recognizer = cv2.face_LBPHFaceRecognizer.create()

path = '/Users/nguyennhi/PycharmProjects/pythonProject4/dataset'

def getImage(path):
    imagePaths = [os.path.join(path, file) for file in os.listdir(path) if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff'))]

    faces = []
    ids = []

    for imagePath in imagePaths:
        try:
            img = Image.open(imagePath).convert('L')
            facenp = np.array(img, 'uint8')
            print(facenp)


            id = int(os.path.split(imagePath)[-1].split(".")[1])

            faces.append(facenp)
            ids.append(id)

            cv2.imshow('Training', facenp)
            cv2.waitKey(10)
        except Exception as e:
            print(f"Error processing {imagePath}: {str(e)}")

    return faces, ids

faces, ids = getImage(path)


recognizer.train(faces, np.array(ids))

if not os.path.exists('recognizer'):
    os.makedirs('recognizer')

recognizer.save('recognizer/training.yml')

cv2.destroyAllWindows()
