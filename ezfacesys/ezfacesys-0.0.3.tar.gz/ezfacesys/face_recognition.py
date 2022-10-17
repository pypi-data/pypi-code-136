import cv2
import os

names = []


def upload_data(path):
    recogizer = cv2.face.LBPHFaceRecognizer_create()
    recogizer.read(path)
    return recogizer


def face_detect_demo(path, img, cate_path):
    recogizer = upload_data(path)
    warningtime = 0
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    face_detector = cv2.CascadeClassifier(cate_path)
    face = face_detector.detectMultiScale(gray, 1.1, 5, cv2.CASCADE_SCALE_IMAGE, (100, 100), (300, 300))
    for x, y, w, h in face:
        cv2.rectangle(img, (x, y), (x + w, y + h), color=(0, 0, 255), thickness=2)
        cv2.circle(img, center=(x + w // 2, y + h // 2), radius=w // 2, color=(0, 255, 0), thickness=1)
        ids, confidence = recogizer.predict(gray[y:y + h, x:x + w])
        if confidence > 80:
            warningtime += 1
            if warningtime > 100:
                print("有坏人")
            warningtime = 0
            cv2.putText(img, 'unkonw', (x + 10, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 1)
        else:
            cv2.putText(img, str(names[ids - 1]), (x + 10, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 1)
    cv2.imshow('result', img)


def name(path):
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
    for imagePath in imagePaths:
        name = str(os.path.split(imagePath)[1].split('.', 2)[1])
        names.append(name)


def recognition(path1, path2, cate_path):
    cap = cv2.VideoCapture(0)
    name(path1)
    while True:
        flag, frame = cap.read()
        if not flag:
            break
        face_detect_demo(path2, frame, cate_path)
        if ord(' ') == cv2.waitKey(10):
            break
    cv2.destroyAllWindows()
    cap.release()
