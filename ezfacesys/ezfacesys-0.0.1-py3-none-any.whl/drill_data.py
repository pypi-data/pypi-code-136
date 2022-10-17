import os
import cv2
from PIL import Image
import numpy as np


def getImageAndLabels(path):
    facesSamples = []
    ids = []
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
    face_detector = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')

    for imagePath in imagePaths:
        PIL_img = Image.open(imagePath).convert('L')
        img_numpy = np.array(PIL_img, 'uint8')
        faces = face_detector.detectMultiScale(img_numpy)
        id = int(os.path.split(imagePath)[1].split('.')[0])
        for x, y, w, h in faces:
            ids.append(id)
            facesSamples.append(img_numpy[y:y + h, x:x + w])

    return facesSamples, ids


def drill(path1, path2):
    faces, ids = getImageAndLabels(path1)
    try:
        recognizer = cv2.face.LBPHFaceRecognizer_create()
        recognizer.train(faces, np.array(ids))
        recognizer.write(path2)
    except Exception as e:
        return f'保存错误：{e}'
