# -*- coding: utf-8 -*- 
'''
读取手机摄像头的视频流


1. 手机与电脑链接同一个WIFI热点

2. 需要sudo权限：
sudo python  ipcam-cap.py
'''
import cv2
import time

ip_camera_url = 'http://admin:admin@192.168.120.102:8081/'
# 创建一个窗口
cv2.namedWindow('ip_camera', flags=cv2.WINDOW_NORMAL | cv2.WINDOW_FREERATIO)

cap = cv2.VideoCapture(ip_camera_url)

if not cap.isOpened():
    print('请检查IP地址还有端口号，或者查看IP摄像头是否开启，另外记得使用sudo权限运行脚本')

while cap.isOpened():
    ret, frame = cap.read()
    cv2.imshow('ip_camera', frame)


    if cv2.waitKey(1) == ord('q'):
        # 退出程序
        break

cv2.destroyWindow('ip_camera')
cap.release()
