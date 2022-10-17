import cv2
import os
import time
import numpy as np
from froxiaofeidriver import mysound

class RecognizeLBP:
    xf=mysound.Sound()
    str_face = 0
    
    def __init__(self):
        pass
    
    def read_dic_face(self,file_list):
        data = np.loadtxt(file_list,dtype='str')
        dic_face = {}
        for i in range(len(data)):
            dic_face[int(data[i][0])] = data[i][1]
        return dic_face
    def recognize(self):
        # 加载人脸字典
        dic_face = self.read_dic_face("/home/pi/AiCar/face/face_list.txt")
    
        # 加载Opencv人脸检测器
        faceCascade = cv2.CascadeClassifier('/home/pi/AiCar/face/haarface.xml')

        # 加载训练好的人脸识别器
        recognizer = cv2.face.LBPHFaceRecognizer_create()
        recognizer.read('/home/pi/AiCar/face/trainer.yml')

        # 打开摄像头
        cap = cv2.VideoCapture(0)
        self.xf.faceStartRecognize()
        time.sleep(3)
        while True:
        
            # 读取一帧图像
            success, img = cap.read()
        
            if not success:
                continue
        
            # 转换为灰度
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
            # 进行人脸检测
            faces = faceCascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5,minSize=(50, 50),flags=cv2.CASCADE_SCALE_IMAGE)
        
            # 遍历检测到的人脸
            for (x, y, w, h) in faces:
                # 画框
                cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 3)
            
                # 进行人脸识别 
                id_face, confidence = recognizer.predict(gray[y:y+h,x:x+w])
            
                # 检测可信度，这里是通过计算距离来计算可信度，confidence越小说明越近似 
                if (confidence < 35):
                    str_face = dic_face[id_face]
                    return str_face
                    
            # 显示检测结果
#             cv2.imshow("FACE",img)
        
        cap.release()
        
    
    
    
    
    