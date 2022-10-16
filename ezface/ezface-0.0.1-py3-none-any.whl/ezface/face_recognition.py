#模拟数据
faces_list = ['何胜利','柴奇峰','冯佳秋']


# 获取识别到的所有人脸信息
def get_faces():
    print(f"--------识别到{len(faces_list)}个人，分别如下--------")
    for index,face in enumerate(faces_list):
        print(f"第{index+1}张人脸是：{face}")
    print("--------识别完成，程序结束--------")
    return faces_list


if __name__ == '__main__':
    get_faces()