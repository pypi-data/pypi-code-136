#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5.QtGui import QImage, QPixmap, QPainter, QMovie
from PyQt5.QtPrintSupport import QPrintDialog, QPrinter
from PyQt5.QtWidgets import QLabel, QSizePolicy, QScrollArea, QMessageBox, QVBoxLayout, QHBoxLayout, QMainWindow, QMenu, \
    QAction, \
    QFileDialog, QRubberBand, QToolBar, QSlider, QFormLayout, QWidget, QProgressBar, QSplashScreen, QComboBox
from PyQt5.QtCore import Qt, QPointF, QRect, QTimer
from PyQt5 import QtCore
from PyQt5.QtGui import QIcon, QPalette, QColor
from PIL import ImageGrab
import numpy as np
import cv2
import PySide2 as ps2
import os
import qdarkstyle
from skimage.filters import threshold_otsu

from cnn_runner.utils.settings_window import SettingsWindow
from cnn_runner.utils.show_img_window import ShowImgWindow
from cnn_runner.utils.thres_slider import make_slider
from cnn_runner.utils.splash_screen import MovieSplashScreen
# Display image
from cnn_runner.utils.cnn_worker import CNN_worker
from PyQt5.QtCore import pyqtSignal
from cnn_runner.utils.img_hist_norm import read_process_and_save
from cnn_runner.utils.seg_learning import Segmentator, StartML
from cnn_runner.utils.what_class_window import WhatClassWindow
from PyQt5.QtWidgets import qApp
from cnn_runner.utils.canny_edge import start_add_mask

qApp.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)


class ObjectDetectionWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.resize(1200, 800)

        # Установка темы оформления
        self.theme_str = 'dark_blue.xml'
        self.is_dark_theme = True

        # заставка
        self.start_gif(is_prog_load=True)

        # Принтер
        self.printer = QPrinter()

        # Иконка
        self.setWindowIcon(QIcon("icons/planet-earth.png"))

        # настройка области отображения картинки
        self.scaleFactor = 0.0
        self.imageLabel = QLabel()
        self.imageLabel.setBackgroundRole(QPalette.Base)
        self.imageLabel.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self.imageLabel.setScaledContents(True)

        self.scrollArea = QScrollArea()
        self.scrollArea.setBackgroundRole(QPalette.Dark)
        self.scrollArea.setWidget(self.imageLabel)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setVisible(False)

        # режим выбора области на изображении
        self.isAreaSelectMode = False
        self.isGetPixelsMode = False

        # сохранена ли область
        self.isAreaSaved = False
        # настройка области выбора изображения
        self.selection = QRubberBand(QRubberBand.Rectangle, self)
        # начальная и конечная точка выбора области
        self.start = QPointF()
        self.end = QPointF()
        # путь к файлу с выбранной областью
        self.selectedImgPath = ""
        # применена ли нормализация к изображению
        self.is_selection_normalized = False

        # произведена ли инициализация настроек
        self.cnn_settings_set = False

        # имена классов
        self.yolo_classes_names = ['реактор', 'машинный зал', 'БСС', 'парковка', 'ВНС',
                                   'градирня', 'РУ', 'турбина', 'градирня вент кв', 'градирня вент', 'реактор кв']
        self.mask_classes_names = ['реактор', 'реактор кв', 'градирня', 'градирня вент кв', 'градирня вент', 'РУ',
                                   'ВНС', 'турбина', 'БСС', 'машинный зал', 'парковка']

        self.mask_colors = [(252, 66, 123),  # 'RO'
                            (192, 57, 43),  # 'RO sq'
                            (52, 152, 219),  # 'CT':
                            (52, 152, 219),  # 'CT sq
                            (52, 152, 219),  # 'CT vent
                            (39, 174, 96),  # 'Switch
                            (155, 89, 182),  # 'WPS'
                            (252, 66, 123),  # 'Turb'
                            (155, 89, 182),  # 'Spill'
                            (58, 53, 117),  # ER'
                            (255, 221, 89)]  # 'Parking'

        self.setCentralWidget(self.scrollArea)

        # создаем меню и тулбар
        self.createActions()
        self.createMenus()
        self.createToolbar()
        self.fitToWindowAct.setChecked(True)
        self.updateActions()

        # запущены ли воркеры детектирования и сегментации
        self.is_worker_created = False
        self.is_seg_worker_created = False
        self.is_mask_saved = False
        self.is_map = False
        self.map_path = None
        # заголовок главного окна
        self.setWindowTitle("Модуль обнаружения объектов")

        # инициализация настроек приложения
        self.init_cnn_settings()

        self.splash.finish(self)

    def set_movie_gif(self):
        """
        Установка гифки на заставку
        """
        theme_type = self.theme_str.split('.')[0].split('_')[1]
        if theme_type == "cyan_500":
            theme_type = "cyan"
        if theme_type == "cyan" or theme_type == "blue":
            self.movie_gif = "icons/loading-63.gif"
        elif theme_type == "red" or theme_type == "yellow" or theme_type == "amber":
            self.movie_gif = "icons/loading-64.gif"
        elif theme_type == "teal" or theme_type == "lightgreen":
            self.movie_gif = "icons/loading-65.gif"
        else:
            # purple
            self.movie_gif = "icons/loading-66.gif"

    def start_gif(self, is_prog_load=False):
        self.set_movie_gif()
        self.movie = QMovie(self.movie_gif)
        if is_prog_load:
            self.splash = MovieSplashScreen(self.movie)
        else:
            self.splash = MovieSplashScreen(self.movie, parent_geo=self.geometry())

        self.splash.setWindowFlags(
            QtCore.Qt.WindowStaysOnTopHint | QtCore.Qt.FramelessWindowHint
        )

        self.splash.showMessage(
            "<h1><font color='red'></font></h1>",
            QtCore.Qt.AlignTop | QtCore.Qt.AlignCenter,
            QtCore.Qt.white,
        )

        self.splash.show()

    def display(self, img, frameName="OpenCV Image", width=800):
        """
        Отображение картинки (depricated - сейчас вместо этого модуль ShowImgWindow)
        """
        h, w = img.shape[0:2]
        neww = width
        newh = int(neww * (h / w))
        cv2.namedWindow(frameName)
        img = cv2.resize(img, (neww, newh))

        cv2.imshow(frameName, img)
        cv2.waitKey(0)

    def display_img_by_name(self, img_file_path, title=""):
        """
        Отобразить картинку в отдельном окне со своим тулбаром и меню
        img_file_path - путь к картинке
        title - заголовок окна
        """
        if title == "":
            title = img_file_path

        cnn_type = self.cnn_settings['CNN']
        # if cnn_type == "YOLOR":
        #     classes_names = self.yolo_classes_names
        # else:
        classes_names = self.mask_classes_names
        ShowImgWindow(self, title=title, img_file=img_file_path, icon_folder=self.icon_folder, is_table=True,
                      cls_names=classes_names, cnn_type=cnn_type, parent_geo=self.geometry())

    def open(self):
        """
        Открыть картинку
        """
        options = QFileDialog.Options()
        # fileName = QFileDialog.getOpenFileName(self, "Open File", QDir.currentPath())
        fileName, _ = QFileDialog.getOpenFileName(self, 'QFileDialog.getOpenFileName()', 'aes_imgs/val',
                                                  'Images (*.png *.jpeg *.jpg *.bmp *.gif)', options=options)
        if fileName:
            image = QImage(fileName)
            if image.isNull():
                QMessageBox.information(self, "Модуль обнаружения объектов",
                                        "Не могу загрузить изображение %s." % fileName)
                return

            self.opened_img_filename = fileName
            self.imageLabel.setPixmap(QPixmap.fromImage(image))
            self.scaleFactor = 1.0

            self.scrollArea.setVisible(True)
            self.printAct.setEnabled(True)
            self.fitToWindowAct.setEnabled(True)
            self.detectAllAct.setEnabled(True)
            self.detectScanAct.setEnabled(True)
            self.detectAreaAct.setEnabled(False)
            self.startSegAct.setEnabled(True)
            self.getPixelsAct.setEnabled(True)
            self.createMapAct.setEnabled(True)

            self.is_selection_normalized = False
            self.isAreaSaved = False
            if self.isAreaSelectMode:
                self.selection.hide()
                self.isAreaSelectMode = False

            if self.isGetPixelsMode:
                self.isGetPixelsMode = False

            self.updateActions()

            if not self.fitToWindowAct.isChecked():
                self.imageLabel.adjustSize()

            self.fitToWindowAct.setChecked(True)
            self.fitToWindow()

            self.selectAreaAct.setEnabled(True)

            if (self.cnn_settings['is_fit_window'] == True):
                # if image.width() > image.height():
                #     width = 1400
                #     img_width_to_height = image.width() / image.height()
                #     height = width / img_width_to_height
                #     print(width, height)
                #     self.resize(width, height)
                # else:
                height = self.height()
                img_width_to_height = image.width() / image.height()
                width = height * img_width_to_height
                print(width, height)
                self.resize(width, height)

    def print_(self):
        """
        Вывод изображения на печать
        """
        dialog = QPrintDialog(self.printer, self)
        if dialog.exec_():
            painter = QPainter(self.printer)
            rect = painter.viewport()
            size = self.imageLabel.pixmap().size()
            size.scale(rect.size(), Qt.KeepAspectRatio)
            painter.setViewport(rect.x(), rect.y(), size.width(), size.height())
            painter.setWindow(self.imageLabel.pixmap().rect())
            painter.drawPixmap(0, 0, self.imageLabel.pixmap())

    def zoomIn(self):
        """
        Увеличить на 25%
        """
        self.scaleImage(1.25)

    def zoomOut(self):
        """
        Уменьшить
        """
        self.scaleImage(0.8)

    def normalSize(self):
        """
        Вернуть исходный масштаб
        """
        self.imageLabel.adjustSize()
        self.scaleFactor = 1.0

    def fitToWindow(self):
        """
        Подогнать под экран
        """
        fitToWindow = self.fitToWindowAct.isChecked()
        self.scrollArea.setWidgetResizable(fitToWindow)
        if not fitToWindow:
            self.normalSize()

        self.updateActions()

    def about(self):
        """
        Окно о приложении
        """
        QMessageBox.about(self, "О модуле обнаружения объектов",
                          "<p><b>Модуль обнаружения объектов</b></p>"
                          "<p>Тест описания модуля</p>")

    def set_icons(self):
        """
        Задать иконки
        """

        theme_type = self.theme_str.split('.')[0]

        self.icon_folder = "icons/" + theme_type

        self.openAct.setIcon(QIcon(self.icon_folder + "/folder.png"))
        self.printAct.setIcon(QIcon(self.icon_folder + "/printer.png"))
        self.exitAct.setIcon(QIcon(self.icon_folder + "/logout.png"))
        self.zoomInAct.setIcon(QIcon(self.icon_folder + "/zoom-in.png"))
        self.zoomOutAct.setIcon(QIcon(self.icon_folder + "/zoom-out.png"))
        self.normalSizeAct.setIcon(QIcon(self.icon_folder + "/reset.png"))
        self.fitToWindowAct.setIcon(QIcon(self.icon_folder + "/fit.png"))
        self.aboutAct.setIcon(QIcon(self.icon_folder + "/info.png"))
        self.selectAreaAct.setIcon(QIcon(self.icon_folder + "/select.png"))
        self.detectAreaAct.setIcon(QIcon(self.icon_folder + "/detect.png"))
        self.detectAllAct.setIcon(QIcon(self.icon_folder + "/detect_all.png"))
        self.detectScanAct.setIcon(QIcon(self.icon_folder + "/detect_all.png"))

        self.startSegAct.setIcon(QIcon(self.icon_folder + "/segment.png"))
        self.startSegAreaAct.setIcon(QIcon(self.icon_folder + "/segment_area.png"))
        self.normImgAct.setIcon(QIcon(self.icon_folder + "/gaussian-function.png"))
        self.settingsCNNAct.setIcon(QIcon(self.icon_folder + "/settings.png"))

        self.startMLAct.setIcon(QIcon(self.icon_folder + "/neural.png"))
        self.getPixelsAct.setIcon(QIcon(self.icon_folder + "/pipette.png"))
        self.createMapAct.setIcon(QIcon(self.icon_folder + "/map.png"))

    def createActions(self):

        """
        Задать действия
        """

        self.openAct = QAction("Загрузить изображение...", self, shortcut="Ctrl+O", triggered=self.open)
        self.printAct = QAction("Печать...", self, shortcut="Ctrl+P", enabled=False, triggered=self.print_)
        self.exitAct = QAction("Выход", self, shortcut="Ctrl+Q", triggered=self.close)
        self.zoomInAct = QAction("Увеличить на (25%)", self, shortcut="Ctrl++", enabled=False, triggered=self.zoomIn)
        self.zoomOutAct = QAction("Уменьшить на (25%)", self, shortcut="Ctrl+-", enabled=False, triggered=self.zoomOut)
        self.normalSizeAct = QAction("Исходный размер", self, shortcut="Ctrl+S", enabled=False,
                                     triggered=self.normalSize)
        self.fitToWindowAct = QAction("Подогнать под размер окна", self, enabled=False, checkable=True,
                                      shortcut="Ctrl+F",
                                      triggered=self.fitToWindow)
        self.aboutAct = QAction("О модуле", self, triggered=self.about)
        self.selectAreaAct = QAction("Выделить область", self, shortcut="Ctrl+I", enabled=False, triggered=self.getArea)
        self.detectAreaAct = QAction("Обнаружить объекты в выделенной области", self, shortcut="Ctrl+K", enabled=False,
                                     triggered=self.classCNNArea)
        self.detectAllAct = QAction("Обнаружить объекты на всем изображении", self, shortcut="Ctrl+A", enabled=False,
                                    triggered=self.classCNNAll)
        self.detectScanAct = QAction("Обнаружить объекты сканированием", self, enabled=False,
                                    triggered=self.classCNNscan)

        self.normImgAct = QAction("Нормализовать выделенную область", self, shortcut="Ctrl+N", enabled=False,
                                  triggered=self.normImg)
        self.settingsCNNAct = QAction("Настройки приложения", self, enabled=True, triggered=self.showCNNSettings)

        self.startSegAct = QAction("Сегментировать изображение", self, enabled=False,
                                   triggered=self.segImg)
        self.startSegAreaAct = QAction("Сегментировать выделенную область", self, enabled=False,
                                       triggered=self.segArea)

        self.getPixelsAct = QAction("Взять пиксели для датасета", self, enabled=False,
                                    triggered=self.on_get_pixels_press)

        self.startMLAct = QAction("Переобучить модели ML", self, enabled=True,
                                  triggered=self.on_start_ml_press)

        self.createMapAct = QAction("Создать план-схему", self, enabled=False,
                                    triggered=self.on_create_map_press)

        self.set_icons()

    def createMenus(self):

        """
        Создание меню
        """

        self.fileMenu = QMenu("&Файл", self)
        self.fileMenu.addAction(self.openAct)
        self.fileMenu.addAction(self.printAct)
        self.fileMenu.addSeparator()
        self.fileMenu.addAction(self.exitAct)

        self.viewMenu = QMenu("&Изображение", self)
        self.viewMenu.addAction(self.zoomInAct)
        self.viewMenu.addAction(self.zoomOutAct)
        self.viewMenu.addSeparator()
        self.viewMenu.addAction(self.selectAreaAct)
        self.viewMenu.addAction(self.normImgAct)
        self.viewMenu.addSeparator()
        self.viewMenu.addAction(self.normalSizeAct)
        self.viewMenu.addSeparator()
        self.viewMenu.addAction(self.fitToWindowAct)

        self.classifierMenu = QMenu("Классификатор", self)
        self.classifierMenu.addAction(self.detectAreaAct)
        self.classifierMenu.addAction(self.detectAllAct)
        self.classifierMenu.addAction(self.detectScanAct)
        self.classifierMenu.addSeparator()
        self.classifierMenu.addAction(self.createMapAct)

        self.segMenu = QMenu("Сегментация", self)
        self.segMenu.addAction(self.getPixelsAct)
        self.segMenu.addAction(self.startMLAct)
        self.segMenu.addSeparator()
        self.segMenu.addAction(self.startSegAct)
        self.segMenu.addAction(self.startSegAreaAct)

        self.settingsMenu = QMenu("Настройки", self)
        self.settingsMenu.addAction(self.settingsCNNAct)

        self.helpMenu = QMenu("&Помощь", self)
        self.helpMenu.addAction(self.aboutAct)

        self.menuBar().addMenu(self.fileMenu)
        self.menuBar().addMenu(self.viewMenu)
        self.menuBar().addMenu(self.classifierMenu)
        self.menuBar().addMenu(self.segMenu)
        self.menuBar().addMenu(self.settingsMenu)
        self.menuBar().addMenu(self.helpMenu)

    def createToolbar(self):

        """
        Создание тулбаров
        """

        # Слева

        toolBar = QToolBar("Панель инструментов", self)
        toolBar.addAction(self.openAct)
        toolBar.addSeparator()
        toolBar.addAction(self.zoomInAct)
        toolBar.addAction(self.zoomOutAct)
        toolBar.addAction(self.fitToWindowAct)
        toolBar.addAction(self.normalSizeAct)
        toolBar.addAction(self.selectAreaAct)
        toolBar.addAction(self.normImgAct)
        toolBar.addSeparator()
        toolBar.addAction(self.detectAreaAct)
        toolBar.addAction(self.detectAllAct)
        toolBar.addSeparator()
        toolBar.addAction(self.startSegAreaAct)
        toolBar.addAction(self.startSegAct)
        toolBar.addSeparator()
        toolBar.addAction(self.settingsCNNAct)
        toolBar.addSeparator()
        toolBar.addAction(self.printAct)
        toolBar.addAction(self.exitAct)

        self.toolBarLeft = toolBar
        self.addToolBar(Qt.LeftToolBarArea, self.toolBarLeft)

        # Сверху

        toolBar2 = QToolBar("Панель СНС", self)
        conf_label = QLabel("  Порог уверенности СНС:   ")
        toolBar2.addWidget(conf_label)
        self.thres_conf_slider = make_slider(self.on_conf_thres_slider_change)
        toolBar2.addWidget(self.thres_conf_slider)
        iou_label = QLabel("  Порог IOU СНС:   ")
        toolBar2.addWidget(iou_label)
        self.thres_iou_slider = make_slider(self.on_iou_thres_slider_change)
        toolBar2.addWidget(self.thres_iou_slider)
        toolBar2.setMinimumWidth(400)

        self.toolBarTop = toolBar2
        self.addToolBar(Qt.TopToolBarArea, self.toolBarTop)

    def updateActions(self):
        """
        Обновить состояние действий
        """
        self.zoomInAct.setEnabled(not self.fitToWindowAct.isChecked())
        self.zoomOutAct.setEnabled(not self.fitToWindowAct.isChecked())
        self.normalSizeAct.setEnabled(not self.fitToWindowAct.isChecked())

        self.zoomInAct.setVisible(not self.fitToWindowAct.isChecked())
        self.zoomOutAct.setVisible(not self.fitToWindowAct.isChecked())
        self.normalSizeAct.setVisible(not self.fitToWindowAct.isChecked())

        self.normImgAct.setEnabled(self.isAreaSaved)
        self.normImgAct.setVisible(self.isAreaSaved)
        # self.getPixelsAct.setEnabled(not self.isGetPixelsMode)

    def classCNNscan(self):
        """
        Начать классификацию скользящим окном
        """
        self._cnn_name = self.cnn_settings["CNN"]

        if self._cnn_name == 'YOLOv5l6':
            # 1280 * 1280
            pass
        elif self._cnn_name == 'YOLOv5x6':
            # 640 * 640
            pass


        # спрятать выделение области
        if self.selection.isVisible():
            self.selection.hide()

        # запуск заставки
        self.start_gif()

        # на вход воркера - исходное изображение

        img_path = os.path.dirname(self.opened_img_filename)
        img_name = os.path.basename(self.opened_img_filename)

        self.goCNN(img_name=img_name, img_path=img_path, scanning=True)

    def on_start_ml_press(self):
        print("Start ML pressed")
        self.ml = StartML()

        self.ml.started.connect(self.on_ml_started)
        self.ml.finished.connect(self.on_ml_finished)

        self.is_ml_worker_created = True
        if not self.ml.isRunning():
            self.ml.start()

    def on_create_map_press(self):
        print("Create map pressed")
        self.is_map = True

        tek_path = os.getcwd()
        self.map_path = os.path.join(tek_path, "detection")
        self.map_path = os.path.join(self.map_path, "Cascade R-CNN")

        self._cnn_name = self.cnn_settings["CNN"]
        self._is_mask = self.is_mask_saved

        self.cnn_settings["CNN"] = 'Cascade R-CNN'
        self.is_mask_saved = True

        # запуск заставки
        self.start_gif()

        # на вход воркера - исходное изображение

        img_path = os.path.dirname(self.opened_img_filename)
        img_name = os.path.basename(self.opened_img_filename)

        self.goCNN(img_name=img_name, img_path=img_path)

    def on_ml_started(self):
        # запустить заставку
        print("Start ML")
        self.start_gif()

    def on_ml_finished(self):
        print("End ML")
        self.splash.finish(self)

        self.splash.showMessage(
            'Обучение модели завершено',
            Qt.AlignHCenter | Qt.AlignBottom, Qt.white
        )

        QMessageBox.about(self, "Обучение модели Random Forest",
                          "Обучение модели успешно завершено")

    def on_get_pixels_press(self):
        print("Get pixels pressed")
        self.isGetPixelsMode = True

    def goSeg(self, img_path):
        """
        Начать сегментацию
        img_path - путь к файлу,
        результат будет сохранен с этим же именем в папке segmentation/seg_results
        """
        # скрыть выделение области
        if self.selection.isVisible():
            self.selection.hide()

        # запустить заставку
        self.start_gif()

        # заданы ли настройки сегментации

        if self.cnn_settings_set:
            self.seg_method = self.cnn_settings['Seg model']
            self.clusters_num = self.cnn_settings['k_means_clusters']
            iou_thres_set = self.cnn_settings['iou_thres']

            str_text = "Начинаю сегментацию методом {0:s}".format(self.seg_method)
            print(str_text)

        else:

            self.seg_method = "CNN SemSeg"
            self.clusters_num = 2
            iou_thres_set = 0.5

        # установливаем путь к результатам сегментации
        save_path = os.path.join(os.getcwd(), "segmentation")
        save_path = os.path.join(save_path, self.seg_method)

        if not os.path.exists(save_path):
            os.makedirs(save_path)

        selected_labels = []
        for i, key in enumerate(self.cnn_settings["cnn_semseg_classes"]):
            if self.cnn_settings["cnn_semseg_classes"][key] == True:
                selected_labels.append(i)

        print(selected_labels)
        # создаем воркер-сегментатор и запускаем
        self.segmentator = Segmentator(img_path=img_path, seg_method=self.seg_method, clusters_num=self.clusters_num,
                                       iou_thres=iou_thres_set,
                                       selected_labels=selected_labels,
                                       k_means_attempts=10, save_path=save_path)

        self.segmentator.started.connect(self.on_seg_started)
        self.segmentator.finished.connect(self.on_seg_finished)

        self.is_seg_worker_created = True
        if not self.segmentator.isRunning():
            self.segmentator.start()

    def on_seg_started(self):
        """
        При начале сегментации сегментации
        """
        str_text = "{0:s} started segmentation...".format(self.seg_method)
        print(str_text)

    def on_seg_finished(self):
        """
        При завершении сегментации
        """
        # показываем окно и завершаем заставку
        str_text = "{0:s} finished segmentation".format(self.seg_method)
        print(str_text)

        img_view_window_title = "Результаты сегментации методом {0:s}".format(self.seg_method)

        # читаем путь куда сохранилась картинка
        img_save_path = self.segmentator._img_save_path

        if img_save_path:

            ShowImgWindow(self, title=img_view_window_title, img_file=img_save_path, icon_folder=self.icon_folder,
                          is_table=False, parent_geo=self.geometry())

        else:
            print("Can't read segmented image. Maybe file doesn't exist")

        self.segmentator = None

        self.splash.showMessage(
            'Обнаружение объектов завершено',
            Qt.AlignHCenter | Qt.AlignBottom, Qt.white
        )

        self.splash.finish(self)
        self.isAreaSelectMode = False

    def segImg(self):
        """
        Начать сегментацию всего изображения
        """
        # в opened_img_filename - путь к исходному изображению
        img_path = self.opened_img_filename
        self.goSeg(img_path)

    def segArea(self):
        """
        Начать сегментацию выделенной области
        """
        # Определяем путь к сохраненной выделенной области и запускаем сегментацию
        proj_path = os.getcwd()
        img_path = os.path.join(proj_path, "selected_areas")
        if self.is_selection_normalized:
            img_name = "selected_area-normalized1.jpg"
        else:
            img_name = "selected_area.png"

        img_full_name = os.path.join(img_path, img_name)

        self.goSeg(img_full_name)

    def normImg(self):
        """
        Нормировка области изображения
        """
        if self.isAreaSaved:
            proj_path = os.getcwd()
            img_path = os.path.join(proj_path, "selected_areas")
            img_name = "selected_area.png"
            read_process_and_save(img_name, img_path)
            self.is_selection_normalized = True

            QMessageBox.about(self, "Нормализация выделенной области",
                              "Процесс нормализации выделенной области завершен успешно")

    def on_conf_thres_slider_change(self, value):
        """
        При изменении слайдера порог уверенности СНС
        """
        if not self.cnn_settings_set:
            self.cnn_settings = {}
            self.cnn_settings['CNN'] = 'YOLOv5x6'
            self.cnn_settings['iou_thres'] = 0.7

        self.cnn_settings['conf_thres'] = value / 100

        self.cnn_settings_set = True

    def on_iou_thres_slider_change(self, value):
        """
        При изменении слайдера порог IOU СНС
        """
        if not self.cnn_settings_set:
            self.cnn_settings = {}
            self.cnn_settings['CNN'] = 'YOLOv5x6'
            self.cnn_settings['conf_thres'] = 0.7

        self.cnn_settings['iou_thres'] = value / 100

    def classCNNAll(self):
        """
        Начать классификацию всего изображения
        """
        # спрятать выделение области
        if self.selection.isVisible():
            self.selection.hide()

        # запуск заставки
        self.start_gif()

        # на вход воркера - исходное изображение

        img_path = os.path.dirname(self.opened_img_filename)
        img_name = os.path.basename(self.opened_img_filename)

        self.goCNN(img_name=img_name, img_path=img_path)

    def classCNNArea(self):
        """
        Запуск классификации области изображения
        """

        if self.isAreaSaved:

            # спрятать выделение области
            if self.selection.isVisible():
                self.selection.hide()

            # запуск заставки
            self.start_gif()

            # путь к сохраненной области
            proj_path = os.getcwd()
            img_path = os.path.join(proj_path, "selected_areas")
            if self.is_selection_normalized:
                img_name = "selected_area-normalized1.jpg"
            else:
                img_name = "selected_area.png"

            # запуск классификации
            self.goCNN(img_name=img_name, img_path=img_path)

    def goCNN(self, img_name, img_path, scanning=False):
        """
        Запуск классификации
        img_name - имя изображения
        img_path - путь к изображению
        """
        string_format = ""
        for key in self.cnn_settings:
            string_format += "{0:s}: {1} ".format(key, self.cnn_settings[key])

        self.started_cnn = self.cnn_settings['CNN']

        conf_thres_set = self.cnn_settings['conf_thres']
        iou_thres_set = self.cnn_settings['iou_thres']

        if scanning:
            str_text = "Начинаю классифкацию СНС {0:s} сканирующим окном с параметрами {1:s}".format(self.started_cnn, string_format)
        else:
            str_text = "Начинаю классифкацию СНС {0:s} с параметрами {1:s}".format(self.started_cnn, string_format)
        print(str_text)

        self.CNN_worker = CNN_worker(conf_thres=conf_thres_set, iou_thres=iou_thres_set,
                                     cnn_type=self.cnn_settings['CNN'],
                                     img_name=img_name, img_path=img_path, classes_names=self.mask_classes_names,
                                     mask_colors=self.mask_colors, is_mask_saved=self.is_mask_saved, is_map=self.is_map,
                                     map_path=self.map_path, scanning=scanning)

        self.CNN_worker.started.connect(self.on_cnn_started)
        self.CNN_worker.finished.connect(self.on_cnn_finished)

        self.is_worker_created = True

        if not self.CNN_worker.isRunning():
            self.CNN_worker.start()

    def on_cnn_started(self):
        """
        При начале классификации
        """
        str_text = "{0:s} CNN started detection...".format(self.started_cnn)
        print(str_text)

    def on_cnn_finished(self):
        """
        При завершении классификации
        """
        str_text = "{0:s} CNN finished detection".format(self.started_cnn)
        print(str_text)

        if not self.is_map:

            img_view_window_title = "Результаты работы СНС {0:s}".format(self.started_cnn)

            # читаем путь сохрененнного изображения
            img_path = self.CNN_worker.img_detected_path

            if img_path:
                self.display_img_by_name(title=img_view_window_title,
                                         img_file_path=img_path)
            else:
                print("Can't read detected image. Maybe file doesn't exist")

        else:
            img_view_window_title = "Результаты построения план-схемы"

            # читаем путь сохрененнного изображения
            img_path = self.CNN_worker.map_path

            if img_path:
                self.display_img_by_name(title=img_view_window_title,
                                         img_file_path=img_path)
            else:
                print("Can't read detected image. Maybe file doesn't exist")

            self.is_map = False
            self.cnn_settings["CNN"] = self._cnn_name
            self.is_mask_saved = self._is_mask
            self.is_map = False

        self.CNN_worker = None
        self.splash.finish(self)

        self.splash.showMessage(
            'Обнаружение объектов завершено',
            Qt.AlignHCenter | Qt.AlignBottom, Qt.white
        )
        self.isAreaSelectMode = False

    def showCNNSettings(self):
        """
        Показать осно с настройками приложения
        """
        if self.cnn_settings['cnn_semseg_classes']:
            selected_labels_nums = []
            for i, stuff in enumerate(self.cnn_settings['cnn_semseg_classes']):
                if self.cnn_settings['cnn_semseg_classes'][stuff] == True:
                    selected_labels_nums.append(i)
        else:
            selected_labels_nums = None

        if self.cnn_settings_set:
            self._settings_window = SettingsWindow(self, self.cnn_settings, selected_labels=selected_labels_nums)
        else:
            self._settings_window = SettingsWindow(self)
        self._settings_window.okBtn.clicked.connect(self.on_settings_closed)
        self._settings_window.cancelBtn.clicked.connect(self.on_settings_closed)

        self._settings_window.show()

    def on_settings_closed(self):
        """
        При закрытии окна настроек приложения
        Осуществляет сохранение настроек
        """

        if len(self._settings_window.settings) != 0:
            self.cnn_settings = self._settings_window.settings
            self.cnn_settings_set = True
            print("Настройки сохранены:")
            str_settings = "Настройки сохранены:\n"

            for key in self.cnn_settings:
                print(key, self.cnn_settings[key])
                str_settings += "{0} {1} ".format(key, self.cnn_settings[key])

            self.thres_iou_slider.setValue(int(self.cnn_settings['iou_thres'] * 100))
            self.thres_conf_slider.setValue(int(self.cnn_settings['conf_thres'] * 100))

            if self.cnn_settings['theme'] != self.theme_str:
                print("Start change theme to " + self.cnn_settings['theme'])
                self.change_theme(self.cnn_settings['theme'])
                self.theme_str = self.cnn_settings['theme']
                theme_type = self.theme_str.split('_')[0]
                self.set_icons()

            QMessageBox.about(self, "Сохранение настроек приложения",
                              str_settings)

    def on_wcw_ok(self):
        print("WCW closed. Selected class: ", self.wcw.selected_class)

        path_tek = os.getcwd()
        sem_dataset_folder = os.path.join(path_tek, "seg_datasets")
        sem_dataset = os.path.join(sem_dataset_folder, "sem_seg_data.csv")
        if not os.path.exists(sem_dataset):
            file = open(sem_dataset, "w")
            file.close()

        file = open(sem_dataset, "a")
        shape = self.cropped_image.shape

        for x in range(shape[0]):
            for y in range(shape[1]):
                file.write(str(self.cropped_image[x, y, 0]) + ";" + str(self.cropped_image[x, y, 1]) + ";" + str(
                    self.cropped_image[x, y, 2]) + ";" + self.wcw.selected_class + "\n")
        file.close()
        print("Data appended")

    def on_wcw_cancel(self):
        pass

    def change_theme(self, theme_str):
        """
        Изменение темы приложения
        """
        # app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
        app = QApplication.instance()
        apply_stylesheet(app, theme=theme_str)
        #

    def init_cnn_settings(self):
        """
        Инициализация настроек приложения
        """
        self.cnn_settings = {}
        self.cnn_settings['iou_thres'] = 0.5
        self.cnn_settings['conf_thres'] = 0.5
        self.cnn_settings['CNN'] = 'YOLOv5x6'
        self.cnn_settings["theme"] = self.theme_str
        self.cnn_settings['Seg model'] = "CNN SemSeg"
        self.cnn_settings['k_means_clusters'] = 2
        self.cnn_settings['is_fit_window'] = True
        self.cnn_settings['is_crazy_colors'] = True
        self.cnn_settings['platform'] = 'GPU'
        self.cnn_settings['cnn_semseg_classes'] = {"город": True, "с/x земля": True, "пастбищные угодья": True,
                                                   "лес": True, "вода": True, "бесплодная земля": True}

        self.cnn_settings_set = True

        self.thres_iou_slider.setValue(int(self.cnn_settings['iou_thres'] * 100))
        self.thres_conf_slider.setValue(int(self.cnn_settings['conf_thres'] * 100))

    def scaleImage(self, factor):
        """
        Масштабировать картинку
        """
        self.scaleFactor *= factor
        self.imageLabel.resize(self.scaleFactor * self.imageLabel.pixmap().size())

        self.adjustScrollBar(self.scrollArea.horizontalScrollBar(), factor)
        self.adjustScrollBar(self.scrollArea.verticalScrollBar(), factor)

        self.zoomInAct.setEnabled(self.scaleFactor < 3.0)
        self.zoomOutAct.setEnabled(self.scaleFactor > 0.1)

    def adjustScrollBar(self, scrollBar, factor):
        """
        Подогнать скролбар
        """
        scrollBar.setValue(int(factor * scrollBar.value()
                               + ((factor - 1) * scrollBar.pageStep() / 2)))

    def getArea(self):
        """
        Действие - выбрать область
        """
        self.isAreaSelectMode = True

    def mousePressEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            if self.isAreaSelectMode or self.isGetPixelsMode:
                self.start = event.pos()
                self._start = event.globalPos()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            if self.isAreaSelectMode or self.isGetPixelsMode:
                self.end = event.pos()
                self.selection.setGeometry(QRect(self.start, self.end).normalized())
                self.selection.show()

    def mouseReleaseEvent(self, event):
        if self.isAreaSelectMode:
            self._end = event.globalPos()
            if self._start.x() == self._end.x() or self._start.y() == self._end.y():
                self.isAreaSelectMode = False
                self.selection.hide()
            else:
                self.selection.hide()
                self.is_selection_normalized = False
                QTimer.singleShot(100, self.newLabel)

        if self.isGetPixelsMode:
            self._end = event.globalPos()
            self.selection.hide()
            QTimer.singleShot(100, self.newPixels)

    def newPixels(self):
        """
        Сохранение новых пикселей для обучения моделей МО
        """
        if self._start.x() == self._end.x() or self._start.y() == self._end.y():
            pass
            # one pixel

        else:
            if self._start.x() > self._end.x():
                grab = (self._end.x(),
                        self._end.y(), self._start.x(),
                        self._start.y())

            else:
                grab = (self._start.x(),
                        self._start.y(),
                        self._end.x(),
                        self._end.y())
            res = [0, 0, 0, 0]

            # разные методы расчета координат в зависимости от режима оторажения - подогнано под экран или нет

            if not self.fitToWindowAct.isChecked():

                delta = [self.scrollArea.horizontalScrollBar().value(), self.scrollArea.verticalScrollBar().value()]
                main_geom = self.geometry().getCoords()
                scroll_geom = self.scrollArea.geometry().getCoords()
                for i in range(2):
                    res[i] = grab[i] - (main_geom[i] + scroll_geom[i]) + delta[i]

                height = grab[2] - grab[0]
                width = grab[3] - grab[1]
                res[2] = res[0] + height
                res[3] = res[1] + width

                #
                # print(self.imageLabel.pixmap().width(), self.imageLabel.pixmap().height())
                # print(self.scrollArea.width(), self.scrollArea.height())

                # x_scale = self.imageLabel.pixmap().width() / self.scrollArea.width()
                # y_scale = self.imageLabel.pixmap().height() / self.scrollArea.height()
                # print(self.scaleFactor)
                x_scale = 1.0 / self.scaleFactor
                y_scale = x_scale

                # print(res)

                # print(x_scale, y_scale)

                res_scaled = [int(res[0] * x_scale), int(res[1] * y_scale), int(res[2] * x_scale),
                              int(res[3] * y_scale)]

                # print(res_scaled)

            else:

                main_geom = self.geometry().getCoords()
                scroll_geom = self.scrollArea.geometry().getCoords()
                for i in range(2):
                    res[i] = grab[i] - (main_geom[i] + scroll_geom[i])

                height = grab[2] - grab[0]
                width = grab[3] - grab[1]
                res[2] = res[0] + height
                res[3] = res[1] + width

                # print(res)
                #
                # print(self.imageLabel.pixmap().width(), self.imageLabel.pixmap().height())
                # print(self.scrollArea.width(), self.scrollArea.height())

                x_scale = self.imageLabel.pixmap().width() / self.scrollArea.width()
                y_scale = self.imageLabel.pixmap().height() / self.scrollArea.height()
                # print(res)

                # print(x_scale, y_scale)

                res_scaled = [int(res[0] * x_scale), int(res[1] * y_scale), int(res[2] * x_scale),
                              int(res[3] * y_scale)]

                # print(res_scaled)

            if res_scaled[0] < 0:
                res_scaled[0] = 0
            if res_scaled[1] < 0:
                res_scaled[1] = 0

            # print(res_scaled)

            img = cv2.imread(self.opened_img_filename)

            # print(img.shape)  # Print image shape
            # Обрезка исходного с найденными координатами
            self.cropped_image = img[res_scaled[1]:res_scaled[3], res_scaled[0]:res_scaled[2]]

            self.wcw = WhatClassWindow(self)
            self.wcw.okBtn.clicked.connect(self.on_wcw_ok)
            self.wcw.cancelBtn.clicked.connect(self.on_wcw_cancel)
            self.wcw.show()

            cv2.waitKey(0)
            cv2.destroyAllWindows()
            self.isGetPixelsMode = False
            self.updateActions()

    def newLabel(self):
        """
        Сохранение области изображения по пути: selected_areas/selected_area.jpg
        """

        if self._start.x() > self._end.x():
            grab = (self._end.x(),
                    self._end.y(), self._start.x(),
                    self._start.y())

        else:
            grab = (self._start.x(),
                    self._start.y(),
                    self._end.x(),
                    self._end.y())
        res = [0, 0, 0, 0]

        # разные методы расчета координат в зависимости от режима оторажения - подогнано под экран или нет

        if not self.fitToWindowAct.isChecked():

            delta = [self.scrollArea.horizontalScrollBar().value(), self.scrollArea.verticalScrollBar().value()]
            main_geom = self.geometry().getCoords()
            scroll_geom = self.scrollArea.geometry().getCoords()
            for i in range(2):
                res[i] = grab[i] - (main_geom[i] + scroll_geom[i]) + delta[i]

            height = grab[2] - grab[0]
            width = grab[3] - grab[1]
            res[2] = res[0] + height
            res[3] = res[1] + width

            # print(res)
            #
            # print(self.imageLabel.pixmap().width(), self.imageLabel.pixmap().height())
            # print(self.scrollArea.width(), self.scrollArea.height())

            # x_scale = self.imageLabel.pixmap().width() / self.scrollArea.width()
            # y_scale = self.imageLabel.pixmap().height() / self.scrollArea.height()
            # print(self.scaleFactor)
            x_scale = 1.0 / self.scaleFactor
            y_scale = x_scale

            # print(res)

            # print(x_scale, y_scale)

            res_scaled = [int(res[0] * x_scale), int(res[1] * y_scale), int(res[2] * x_scale), int(res[3] * y_scale)]

            # print(res_scaled)

        else:

            main_geom = self.geometry().getCoords()
            scroll_geom = self.scrollArea.geometry().getCoords()
            for i in range(2):
                res[i] = grab[i] - (main_geom[i] + scroll_geom[i])

            height = grab[2] - grab[0]
            width = grab[3] - grab[1]
            res[2] = res[0] + height
            res[3] = res[1] + width

            # print(res)
            #
            # print(self.imageLabel.pixmap().width(), self.imageLabel.pixmap().height())
            # print(self.scrollArea.width(), self.scrollArea.height())

            x_scale = self.imageLabel.pixmap().width() / self.scrollArea.width()
            y_scale = self.imageLabel.pixmap().height() / self.scrollArea.height()
            # print(res)

            # print(x_scale, y_scale)

            res_scaled = [int(res[0] * x_scale), int(res[1] * y_scale), int(res[2] * x_scale), int(res[3] * y_scale)]

            # print(res_scaled)

        if res_scaled[0] < 0:
            res_scaled[0] = 0
        if res_scaled[1] < 0:
            res_scaled[1] = 0

        # print(res_scaled)

        img = cv2.imread(self.opened_img_filename)

        # print(img.shape)  # Print image shape
        # Обрезка исходного с найденными координатами
        cropped_image = img[res_scaled[1]:res_scaled[3], res_scaled[0]:res_scaled[2]]

        tek_path = os.getcwd()
        dest = os.path.join(tek_path, 'selected_areas')
        self.selectedImgPath = os.path.join(dest, 'selected_area.png')
        if not os.path.exists(dest):
            os.makedirs(dest)
        # img.save(self.selectedImgPath)
        print("Область изображения помещена в " + self.selectedImgPath)

        # cv2.imshow("cropped", cropped_image)
        cv2.imwrite(self.selectedImgPath, cropped_image)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()

        self.isAreaSaved = True
        self.updateActions()
        self.detectAreaAct.setEnabled(True)
        self.startSegAreaAct.setEnabled(True)

        cv2.waitKey(0)
        cv2.destroyAllWindows()
        self.selection.show()

    def closeEvent(self, event):
        # Вызывается при закрытии окна
        self.hide()  # Скрываем окно
        if self.is_worker_created and self.CNN_worker:
            self.CNN_worker.running = False  # Изменяем флаг выполнения
            self.CNN_worker.wait(5000)  # Даем время, чтобы закончить
        if self.is_seg_worker_created and self.segmentator:
            self.segmentator.running = False
            self.segmentator.wait(5000)

        event.accept()  # Закрываем окно


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    from qt_material import apply_stylesheet

    app = QApplication(sys.argv)
    # app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    apply_stylesheet(app, theme='dark_blue.xml')
    #
    # app.setStyleSheet(qdarkstyle.load_stylesheet_pyside2())

    imageViewer = ObjectDetectionWindow()
    imageViewer.show()
    sys.exit(app.exec_())
