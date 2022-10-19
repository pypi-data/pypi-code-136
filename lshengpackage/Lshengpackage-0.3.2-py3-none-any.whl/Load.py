# !/usr/bin/env python
# -*- coding: UTF-8 -*-
import os

import pyautogui

from Lshengpackage.simulate.pc.find_pic import screen_shot, find_image

# 加载
def load(img):
    while True:
        screen_shot()
        iocn = find_image(img)
        if iocn is not None:
            return iocn
        x, y = pyautogui.position()
        if x & y == 1:
            return 'out'


def load_click(img):
    while True:
        screen_shot()
        iocn = find_image(img)
        if iocn is not None:
            print(iocn)
            pyautogui.click(iocn[0], iocn[1])
            break
