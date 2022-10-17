"""
@Project:bailan_bad
@File:bad_recognition.py
@Author:郑智
@Date:14:11
"""



# pip install pyautogui
# pip install pyperclip
import time
import pyautogui as pg
import pyperclip as pc

class SendMsg(object):


    def __init__(self):
        self.name = input("请输入发送信息的名字：")
        self.msg = input("请输入发送的内容：")


    def send_msg(self):
        # 操作间隔为0.5秒
        pg.PAUSE = 0.5
        pg.hotkey('ctrl', 'alt', 'w')
        pg.hotkey('ctrl', 'f')

        # 找到好友
        pc.copy(self.name)
        pg.hotkey('ctrl', 'v')
        pg.press('enter')

        # 发送消息
        pc.copy(self.msg)
        pg.hotkey('ctrl', 'v')
        pg.press('enter')

        # 隐藏微信
        time.sleep(1)
        pg.hotkey('ctrl', 'alt', 'w')

if __name__ == '__main__':
    s = SendMsg()
    while True:
        s.send_msg()
