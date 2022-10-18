import time

from natalie import *

# globals

GLOBAL_STATE=0
max_likes=50
liked=0

loaded_img=False
from PyQt5 import QtCore
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QWidget, QHBoxLayout, \
    QGraphicsDropShadowEffect, QPushButton, QApplication, QComboBox,QSizeGrip
from PyQt5 import QtCore, QtGui, QtWidgets
import cv2

from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import pymongo
import threading

scroll_style_sheet=''' QScrollBar:vertical {
	border: none;
    background: rgb(45, 45, 68);
    width: 14px;
    margin: 15px 0 15px 0;
	border-radius: 0px;
 }

/*  HANDLE BAR VERTICAL */
QScrollBar::handle:vertical {	
	background-color: rgb(80, 80, 122);
	min-height: 30px;
	border-radius: 7px;
}
QScrollBar::handle:vertical:hover{	
	background-color: rgb(255, 0, 127);
}
QScrollBar::handle:vertical:pressed {	
	background-color: rgb(185, 0, 92);
}

/* BTN TOP - SCROLLBAR */
QScrollBar::sub-line:vertical {
	border: none;
	background-color: rgb(59, 59, 90);
	height: 15px;
	border-top-left-radius: 7px;
	border-top-right-radius: 7px;
	subcontrol-position: top;
	subcontrol-origin: margin;
}
QScrollBar::sub-line:vertical:hover {	
	background-color: rgb(255, 0, 127);
}
QScrollBar::sub-line:vertical:pressed {	
	background-color: rgb(185, 0, 92);
}

/* BTN BOTTOM - SCROLLBAR */
QScrollBar::add-line:vertical {
	border: none;
	background-color: rgb(59, 59, 90);
	height: 15px;
	border-bottom-left-radius: 7px;
	border-bottom-right-radius: 7px;
	subcontrol-position: bottom;
	subcontrol-origin: margin;
}
QScrollBar::add-line:vertical:hover {	
	background-color: rgb(255, 0, 127);
}
QScrollBar::add-line:vertical:pressed {	
	background-color: rgb(185, 0, 92);
}

/* RESET ARROW */
QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {
	background: none;
}
QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
	background: none;
}


'''

class UIFunctions(MainWindow):
    ## ==> MAXIMIZE RESTORE FUNCTION

    def maximize_restore(self):
        global GLOBAL_STATE

        status = GLOBAL_STATE

        self.ui.close_button.setToolTip("close")
        self.ui.close_button_4.setToolTip("close")

        # IF NOT MAXIMIZED
        if status == 0:
            self.showMaximized()

            # SET GLOBAL TO 1
            GLOBAL_STATE = 1

            # IF MAXIMIZED REMOVE MARGINS AND BORDER RADIUS
            # self.ui.main_frame.setContentsMargins(0, 0, 0, 0)
            # self.ui.main_frame.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(42, 44, 111, 255), stop:0.521368 rgba(28, 29, 73, 255)); border-radius: 0px;")
            self.ui.restore_button.setToolTip("Restore")

        else:
            GLOBAL_STATE = 0
            self.showNormal()
            self.resize(self.width()+1, self.height()+1)
            # self.ui.main_frame.setContentsMargins(10, 10, 10, 10)
            # self.ui.main_frame.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(42, 44, 111, 255), stop:0.521368 rgba(28, 29, 73, 255)); border-radius: 10px;")

            self.ui.minimize_button.setToolTip("minimize")

            self.ui.minimize_button_4.setToolTip("minimize")

    ## ==> UI DEFINITIONS
    def uiDefinitions(self):

        # REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # SET DROPSHADOW WINDOW
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 100))

        # APPLY DROPSHADOW TO FRAME
        self.ui.main_frame.setGraphicsEffect(self.shadow)

        self.ui.login_header_frame.setGraphicsEffect(self.shadow)

        # # MAXIMIZE / RESTORE
        self.ui.restore_button.clicked.connect(lambda: UIFunctions.maximize_restore(self))
        #
        # # MINIMIZE
        self.ui.minimize_button.clicked.connect(lambda: self.showMinimized())
        #
        # # CLOSE
        self.ui.close_button.clicked.connect(lambda: self.close())

        '''login page'''

        # # MAXIMIZE / RESTORE
        # self.ui.restore_button_4.clicked.connect(lambda: UIFunctions.maximize_restore(self))
        #
        # # MINIMIZE
        self.ui.minimize_button_4.clicked.connect(lambda: self.showMinimized())
        #
        # # CLOSE
        self.ui.close_button_4.clicked.connect(lambda: self.close())

        # ==> CREATE SIZE GRIP TO RESIZE WINDOW
        self.sizegrip = QSizeGrip(self.ui.footer_frame)
        self.sizegrip.setStyleSheet("QSizeGrip { width: 10px; height: 10px; margin: 5px } QSizeGrip:hover { background-color: rgb(50, 42, 94) }")
        self.sizegrip.setToolTip("Resize Window")

    def change_avatar(self):

        self.ui.user_avatar.setStyleSheet('''*{border:2px solid  rgb(17, 120, 255);}\n
                                            *:hover{border:3px solid rgb(255, 23, 96);}''')

    def loading_page(self):
        self.setStyleSheet("\n"
"background-color: rgba(59, 59, 59,0);\n"
"border-radius:5px;")

        self.resize(670, 331)

        self.ui.loading_image.setGeometry(QtCore.QRect(30,10, 651, 331))

        self.ui.loading_bar.setGeometry(QtCore.QRect(180,150, 343, 24))

        self.ui.connection_label.setGeometry(QtCore.QRect(240,240, 241, 61))

    def set_current_win(self,win):
        self.ui.stackedWidget.setCurrentIndex(win)

    def login_page(self):
        self.move(500,100)

        self.setStyleSheet("\n"
                           "background-color: rgba(59, 59, 59,0);\n"
                           "border-radius:5px;")

        self.ui.login_header_frame.setStyleSheet("\n"
                           "background-color: rgba(59, 59, 59,255);\n"
                           "border-radius:5px;")

        self.resize(451,737)

        self.ui.login_body_frame.setMaximumSize(QtCore.QSize(451,737))

    def main_page(self):
        self.move(500, 100)

        self.ui.hashtag_title.setStyleSheet("border:none;")
        self.ui.commented_title_2.setStyleSheet("border:none;")

        self.setStyleSheet("\n"
                           "background-color: rgba(59, 59, 59,35);\n"
                           "border-radius:5px;")

        self.ui.header_frame.setStyleSheet("\n"
                                           "background-color: rgba(59, 59, 59,255);\n"
                                           "border-radius:5px;")

        self.resize(542,614)
        self.setMaximumSize(QtCore.QSize(16777215, 16777215))

    def set_blur(self):
        self.blur_effect = QGraphicsBlurEffect()

        # setting blur radius
        self.blur_effect.setBlurRadius(4)

        self.ui.hashtag_frame.setGraphicsEffect(self.blur_effect)

    def edit_verical_scrollbar(self):

        scroll_bar = QScrollBar(self)

        # setting style sheet to the scroll bar
        scroll_bar.setStyleSheet(scroll_style_sheet)

        # setting vertical scroll bar to it
        self.ui.hashtag_input.setVerticalScrollBar(scroll_bar)

        scroll_bar = QScrollBar(self)

        # setting style sheet to the scroll bar
        scroll_bar.setStyleSheet(scroll_style_sheet)

        self.ui.add_comments_input.setVerticalScrollBar(scroll_bar)

        scroll_bar = QScrollBar(self)

        # setting style sheet to the scroll bar
        scroll_bar.setStyleSheet(scroll_style_sheet)

        self.ui.targetusernames_input.setVerticalScrollBar(scroll_bar)

        scroll_bar = QScrollBar(self)

        # setting style sheet to the scroll bar
        scroll_bar.setStyleSheet(scroll_style_sheet)

        self.ui.like_listWidget.setVerticalScrollBar(scroll_bar)

        scroll_bar = QScrollBar(self)

        # setting style sheet to the scroll bar
        scroll_bar.setStyleSheet(scroll_style_sheet)

        self.ui.comment_listwidget.setVerticalScrollBar(scroll_bar)

        scroll_bar = QScrollBar(self)

        # setting style sheet to the scroll bar
        scroll_bar.setStyleSheet(scroll_style_sheet)

        self.ui.status_listwidget.setVerticalScrollBar(scroll_bar)

    def add_scroll_status(self,value):

        print('''      .'\   /`.
         .'.-.`-'.-.`.
    ..._:   .-. .-.   :_...
  .'    '-.(o ) (o ).-'    `.
 :  _    _ _`~(_)~`_ _    _  :
:  /:   ' .-=_   _=-. `   ;\  :
:   :|-.._  '     `  _..-|:   :
 :   `:| |`:-:-.-:-:'| |:'   :
  `.   `.| | | | | | |.'   .'
    `.   `-:_| | |_:-'   .'
 jgs  `-._   ````    _.-'
          ``-------''''')

        self.ui.status_listwidget.setStyleSheet("color: rgb(0,170,255)")
        self.ui.status_listwidget.addItem(value)
        self.ui.status_listwidget.scrollToBottom()

        if "successfully liked" in value:
            print(f"found liking in value {value}")
            value=value.split("|")
            bar_val=int(value[1])

            self.ui.liked_progressBar.setValue(bar_val)

            self.ui.like_listWidget.addItem(value[0])
            self.ui.like_listWidget.scrollToBottom()

        if "maximum limit of 1000 likes" in value:
            bar_val=round(float(value.split("[")[1].split("]")[0].replace("%","")))

            self.ui.liked_progressBar.setValue(bar_val)

            self.ui.like_listWidget.addItem(value)
            self.ui.like_listWidget.scrollToBottom()

        if "like function" in value:
            value=value.split("sleep")[0]

            self.ui.like_listWidget.addItem(value)
            self.ui.like_listWidget.scrollToBottom()

        if "successfully commented" in value:
            value =value.split("|")
            bar_val=int(value[1])
            self.ui.comments_progressbar.setValue(bar_val)

            self.ui.comment_listwidget.addItem(value[0])

            self.ui.comment_listwidget.scrollToBottom()

        if "maximum limit of 200 comments" in value:
            bar_val = round(float(value.split("[")[1].split("]")[0].replace("%", "")))

            self.ui.comments_progressbar.setValue(bar_val)

            self.ui.comment_listwidget.addItem(value)

            self.ui.comment_listwidget.scrollToBottom()

    ## RETURN STATUS IF WINDOWS IS MAXIMIZE OR RESTAURED
    def returnStatus():
        return GLOBAL_STATE





