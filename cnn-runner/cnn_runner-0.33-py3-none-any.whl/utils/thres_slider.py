#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import (QWidget, QSlider,
    QLabel, QApplication)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import pyqtSignal

def make_slider(slot=None):
    slider = QSlider(Qt.Horizontal)
    slider.setMaximumWidth(200)
    slider.setTracking(False)
    if slot:
        slider.valueChanged.connect(slot)
    # slider.setStyleSheet("""
    #             QSlider::groove:horizontal {
    #                 border: 1px solid #999999;
    #                 height: 8px; /* the groove expands to the size of the slider by default. by giving it a height, it has a fixed size */
    #                 background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #B1B1B1, stop:1 #c4c4c4);
    #                 margin: 2px 0;
    #             }
    #
    #             QSlider::handle:horizontal {
    #                 background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #b4b4b4, stop:1 #8f8f8f);
    #                 border: 1px solid #5c5c5c;
    #                 width: 18px;
    #                 margin: -2px 0; /* handle is placed by default on the contents rect of the groove. Expand outside the groove */
    #                 border-radius: 3px;
    #             }
    #
    #             QSlider::add-page:horizontal {
    #                 background: #747d8c;
    #             }
    #
    #             QSlider::sub-page:horizontal {
    #                 background: #2f3542;
    #             }
    #         """)
    return slider