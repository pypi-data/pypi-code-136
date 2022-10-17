"""
@Project:eaface_package
@File:face_recognition.py
@Author:韩晓雷
@Date:10:33
"""


# 模拟数据
faces_list = ["周深", "白敬亭", "银河系"]

# 获取识别到的所有人脸信息
def get_faces():
    print(f"------识别到{len(faces_list)}个人,分别为------")
    for i, index in enumerate(faces_list):
        print(f"第{i+1}张为：{index}")
    print("------识别完成，程序结束------")


if __name__ == '__main__':
    get_faces()


