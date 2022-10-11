import requests
from PyQt5.QtWidgets import QLabel, QDesktopWidget
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import QUrl, QEvent, Qt, QTimer,QTime
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
import os
import sys


class TeraAppWIcon:
  def __init__(self, title, width,height, icon, colorbg, resizeable):
    self.app = QtWidgets.QApplication(sys.argv)
    self.win = QtWidgets.QMainWindow()
    self.win.setGeometry(500, 200, width,height)
    self.win.setWindowIcon(QIcon(icon))
    self.win.setStyleSheet(f"background-color: {colorbg};")
    if resizeable == "False" or resizeable == "false" or resizeable == "FALSE":
      self.win.setFixedSize(width, height)
    else:
      pass
    if title == "False":
      self.win.setWindowFlags(Qt.Tool|Qt.CustomizeWindowHint)
    elif title == "FullFalse":
      self.win.setStyleSheet(Qt.FramelessWindowHint)
    else:
      self.win.setWindowTitle(title)
    qtRectangle = self.win.frameGeometry()
    centerPoint = QDesktopWidget().availableGeometry().center()
    qtRectangle.moveCenter(centerPoint)
    self.win.move(qtRectangle.topLeft())
    self.win.show()


  def txt(self,txt, x, y, size):
    self.txt_name = QtWidgets.QLabel(self.win)
    self.txt_name.setSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
    self.txt_name.resize(20000,70)
    self.txt_name.setText(txt)
    self.txt_name.move(x, y)
    self.txt_name.setFont(QFont(f'Arial', size))
    self.txt_name.setStyleSheet(f"background-color: none")
    self.txt_name.show()

  def txtc(self,txt, x, y, size, color):
    self.txtc_name = QtWidgets.QLabel(self.win)
    self.txtc_name.setSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
    self.txtc_name.resize(20000,70)
    self.txtc_name.setText(txt)
    self.txtc_name.move(x, y)
    self.txtc_name.setFont(QFont(f'Arial', size))
    self.txtc_name.setStyleSheet(f"color: {color}; background-color: none")
    self.txtc_name.show()

  def button(self, txt, x, y, colorbg):
    self.button_name = QtWidgets.QPushButton(self.win)
    self.button_name.setText(txt)
    self.button_name.move(x,y)
    self.button_name.setStyleSheet(f"background-color: {colorbg};")
    self.button_name.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    self.button_name.show()

  def buttonf(self, txt, x, y, colorbg, function):
    self.buttonf_name = QtWidgets.QPushButton(self.win)
    self.buttonf_name.setText(txt)
    self.buttonf_name.move(x, y)
    self.buttonf_name.setStyleSheet(f"background-color: {colorbg};")
    self.buttonf_name.clicked.connect(function)
    self.buttonf_name.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    self.buttonf_name.show()

  def buttonfri(self, x, y, image, function, width,height, border_radius):
    self.buttonfri_name = QtWidgets.QPushButton(self.win)
    self.buttonfri_name.setSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
    self.buttonfri_name.resize(width,height)
    self.buttonfri_name.move(x, y)
    self.buttonfri_name.setStyleSheet(f"background-image : url({image}); border-radius: {border_radius};")
    self.buttonfri_name.clicked.connect(function)
    self.buttonfri_name.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    self.buttonfri_name.show()

  def buttonfr(self, txt, x, y, colorbg, function, width,height):
    self.buttonfr_name = QtWidgets.QPushButton(self.win)
    self.buttonfr_name.setSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
    self.buttonfr_name.resize(width,height)
    self.buttonfr_name.setText(txt)
    self.buttonfr_name.move(x, y)
    self.buttonfr_name.setStyleSheet(f"background-color: {colorbg};")
    self.buttonfr_name.clicked.connect(function)
    self.buttonfr_name.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    self.buttonfr_name.show()

  def img(self, img, x, y, width,height):
    self.img_name = QtWidgets.QLabel(self.win)
    self.img_name.setSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
    self.img_name.resize(width,height)
    self.img_name.setContentsMargins(0,0,0,0)
    self.pixmap = QtGui.QPixmap(f'{img}')
    self.img_name.setPixmap(self.pixmap)
    self.img_name.setMinimumSize(1,1)
    self.layout_name = QtWidgets.QVBoxLayout()
    self.layout_name.addWidget(self.img_name)
    self.img_name.move(x, y)
    self.img_name.show()

  def splashscreen(self,time):
    QTimer.singleShot(time,self.app.quit)

  def gif(self, gif, x, y, width,height):
    self.gif_name = QtWidgets.QLabel(self.win)
    self.gif_name.setSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
    self.gif_name.resize(width,height)
    self.gif_name.setContentsMargins(0,0,0,0)
    self.gif_name.move(x, y)
    self.movie = QMovie(f"{gif}")
    self.gif_name.setMovie(self.movie)
    self.movie.start()
    self.gif_name.show()

  def sound(self, file):
      full_file_path = f'{file}'
      url = QUrl.fromLocalFile(full_file_path)
      content = QMediaContent(url)
      self.sound_name = QMediaPlayer()
      self.sound_name.setMedia(content)
      self.sound_name.play()

  def imgl(self, img, x, y, width,height):
    self.imgl_name = QImage()
    self.imgl_name.loadFromData(requests.get(img).content)
    self.imgl_name2 = QtWidgets.QLabel(self.win)
    self.imgl_name2.setPixmap(QtGui.QPixmap(self.imgl_name))
    self.imgl_name2.resize(width,height)
    self.imgl_name2.move(x, y)
    self.imgl_name2.show()

  def icon(self, img, x, y):
    im = QPixmap(f"{img}").scaledToHeight(36)
    self.icon_name = QLabel(self.win)
    self.icon_name.setPixmap(im)
    self.icon_name.move(x, y)
    self.icon_name.show()

  def input(self, x, y, colorbg):
    self.input_name = QtWidgets.QLineEdit(self.win)
    self.input_name.move(x, y)
    self.input_name.setStyleSheet(f"background-color: {colorbg}; border: none; border-radius: 5;")
    self.input_name.show()

  def inputr(self, x, y, colorbg, width,height):
    self.inputr_name = QtWidgets.QLineEdit(self.win)
    self.inputr_name.setSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
    self.inputr_name.resize(width,height)
    self.inputr_name.move(x, y)
    self.inputr_name.setStyleSheet(f"background-color: {colorbg}; border: none; border-radius: 5; font-size: 20px;")
    self.inputr_name.show()

  def inputr2(self, x, y, colorbg, width,height):
    self.inputr2_name = QtWidgets.QLineEdit(self.win)
    self.inputr2_name.setSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
    self.inputr2_name.resize(width,height)
    self.inputr2_name.move(x, y)
    self.inputr2_name.setStyleSheet(f"background-color: {colorbg}; border: none; border-radius: 5; font-size: 20px;")
    self.inputr2_name.show()

  def textarea(self,x,y,colorbg,width,height,txtcolor,border):
    self.textarea_name = QtWidgets.QTextEdit(self.win)
    self.textarea_name.setSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
    self.textarea_name.move(x,y)
    self.textarea_name.setStyleSheet(f"background-color: {colorbg}; border: none; border-radius: {border}; color:{txtcolor}; font-weight:700;")
    self.textarea_name.resize(width,height)
    self.textarea_name.acceptRichText = True
    self.textarea_name.show()

  def sidebar(self,colorbg, width):
    self.sidebar_name = QtWidgets.QLabel(self.win)
    self.sidebar_name.setSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
    self.sidebar_name.resize(width, 5500)
    self.sidebar_name.setStyleSheet(f"background-color: {colorbg};")
    self.sidebar_name.show()


  def appbar(self,colorbg, height):
    self.appbar_name = QtWidgets.QLabel(self.win)
    self.appbar_name.setSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
    self.appbar_name.resize(5500, height)
    self.appbar_name.setStyleSheet(f"background-color: {colorbg};")
    self.appbar_name.show()






















