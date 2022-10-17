import cv2
import time
import os
import shutil
import numpy as np
from froxiaofeidriver import mysound

class Facecollect:
    xf=mysound.Sound()
    index_photo=0
    
    def __init__(self):
        pass
    # 获取所有文件（人脸id）
    def get_face_list(self,path):
        for root,dirs,files in os.walk(path):
            if root == path:
                return dirs
    def face(self,str_face_id):
        
        os.chdir("/home/pi/AiCar/face")
        # 加载训练好的人脸检测器
        faceCascade = cv2.CascadeClassifier('/home/pi/AiCar/face/haarface.xml')
        if(os.path.exists("/home/pi/AiCar/face/face-collect")):
            shutil.rmtree("/home/pi/AiCar/face/face-collect")
            os.mkdir("/home/pi/AiCar/face/face-collect")
        else:
            os.mkdir("/home/pi/AiCar/face/face-collect")
        os.chdir("/home/pi/AiCar/face/face-collect")
        os.makedirs(str_face_id)
        os.makedirs("quan")
        self.xf.faceStartCollect()
        time.sleep(4)
        # 打开摄像头
        cap = cv2.VideoCapture(0)
#         self.mtts.my_say("开始")
        while True:
          
            # 读取一帧图像
            success, img = cap.read()
        
            if not success:
                continue
            
            # 转换为灰度
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            
            # 进行人脸检测
            faces = faceCascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5,minSize=(50, 50),flags=cv2.CASCADE_SCALE_IMAGE)
            
            # 画框
            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 3)
            
            # 显示检测结果
            
#             os.chdir("/home/pi/AiCar/run")
#             cv2.imshow('FACE',img)
#             self.mtts.my_say("图像")
            
            # 保存人脸
            for (x, y, w, h) in faces:
                roi = img[y:y+h,x:x+w]
                cv2.imwrite("/home/pi/AiCar/face/face-collect/%s/%d.jpg"%(str_face_id,self.index_photo),roi)
                self.index_photo = self.index_photo+1
            if self.index_photo == 20:
                self.xf.faceFirstTwenty()
                time.sleep(3)
            if self.index_photo == 40:
                self.xf.faceMiddleTwenty()
                time.sleep(3)
            if self.index_photo == 60:
                self.xf.faceCollectEnd()
                time.sleep(4)
                break
    
        cv2.destroyAllWindows()
        cap.release()
        os.chdir("../..")
        print(os.getcwd())

        # 创建人脸识别器
        recognizer = cv2.face.LBPHFaceRecognizer_create()

        # 用来存放人脸id的字典
        # 构建人脸编号 和 人脸id 的关系
        dic_face = {}

        # 人脸存储路径
        base_path = "/home/pi/AiCar/face/face-collect"
    
        # 获取人脸id
        face_ids = self.get_face_list(base_path)
        print(face_ids)
        # 用来存放人脸数据与id号的列表
        faceSamples=[]
        ids = []
    
        # 遍历人脸id命名的文件夹
        for i, face_id in enumerate(face_ids):
        
            # 人脸字典更新
            dic_face[i] = face_id
            
            # 获取人脸图片存放路径
            path_img_face = os.path.join(base_path,face_id)
        
            for face_img in os.listdir(path_img_face):
                # 读取以.jpg为后缀的文件
                if face_img.endswith(".jpg"):
                    file_face_img = os.path.join(path_img_face,face_img)
                
                    # 读取图像并转换为灰度图
                    img = cv2.imread(file_face_img)
                    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                
                    # 保存图像和人脸ID
                    faceSamples.append(img)
                    ids.append(i)
    
        print(dic_face)
    
        # 进行模型训练    
        recognizer.train(faceSamples, np.array(ids))

        # 模型保存 
        recognizer.save('/home/pi/AiCar/face/trainer.yml')                
    
        # 进行字典保存
        with open("/home/pi/AiCar/face/face_list.txt",'w') as f:
            for face_id in dic_face:
                f.write("%d %s\n"%(face_id,dic_face[face_id]))
        self.xf.faceTrainEnd()
        time.sleep(3)
    