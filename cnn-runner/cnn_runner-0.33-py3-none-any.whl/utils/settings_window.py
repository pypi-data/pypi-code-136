from PyQt5.QtCore import Qt
from PyQt5.QtGui import QImage, QPixmap, QPalette, QPainter
from PyQt5.QtWidgets import QLabel, QSizePolicy, QMessageBox, QMainWindow, QMenu, QAction, QCheckBox, QComboBox, \
    qApp, QWidget, QGroupBox, QFormLayout, QLineEdit, QComboBox, QSpinBox, QVBoxLayout, QHBoxLayout, QPushButton, \
    QDoubleSpinBox
from PyQt5.QtCore import Qt
import numpy as np

class SettingsCNN(QWidget):
    def __init__(self, parent, stuff_names=None, selected_labels=None):
        super().__init__(parent)
        self.setWindowTitle("Настройки CNN SemSeg")
        self.setWindowFlag(Qt.Tool)

        # Настройки обнаружения
        self.formGroupBox = QGroupBox("Выберите классы для поиска на изображении")
        layout = QFormLayout()

        self.checkboxes = []
        self.settings = {}
        self.stuff_names = stuff_names
        self.seleted_labels = selected_labels

        for i, stuff in enumerate(stuff_names):
            chbox = QCheckBox(self)
            if self.seleted_labels and i in self.seleted_labels:
                chbox.setChecked(True)

            self.checkboxes.append(chbox)
            layout.addRow(QLabel(stuff), chbox)

        self.formGroupBox.setLayout(layout)

        btnLayout = QHBoxLayout()

        self.okBtn = QPushButton('Принять', self)
        self.okBtn.clicked.connect(self.on_ok_clicked)

        self.cancelBtn = QPushButton('Отменить', self)
        self.cancelBtn.clicked.connect(self.on_cancel_clicked)

        btnLayout.addWidget(self.okBtn)
        btnLayout.addWidget(self.cancelBtn)

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.formGroupBox)
        mainLayout.addLayout(btnLayout)
        self.setLayout(mainLayout)
        self.resize(500, 300)

    def on_ok_clicked(self):

        for i, stuff in enumerate(self.stuff_names):
            if self.checkboxes[i].isChecked():
                self.settings[stuff] = True
            else:
                self.settings[stuff] = False
        # print(self.settings)
        self.close()

    def on_cancel_clicked(self):
        self.settings.clear()
        self.close()

class SettingsWindow(QWidget):
    def __init__(self, parent, settings=None, selected_labels=None):
        super().__init__(parent)
        self.setWindowTitle("Настройки приложения")
        self.setWindowFlag(Qt.Tool)

        self.selected_labels = selected_labels

        # Настройки обнаружения
        self.formGroupBox = QGroupBox("Настройки обнаружения")

        self.settings = {}
        self.stuff_names = ["город", "с/x земля", "пастбищные угодья", "лес", "вода", "бесплодная земля"]

        self.cnn_semseg_classes = {}
        for i, stuff in enumerate(self.stuff_names):
            if selected_labels:
                if i in selected_labels:
                    self.cnn_semseg_classes[stuff] = True
                else:
                    self.cnn_semseg_classes[stuff] = False
            else:
                self.cnn_semseg_classes[stuff] = True

        layout = QFormLayout()

        self.where_calc_combo = QComboBox()
        self.where_vars = np.array(["CPU", "GPU"])
        self.where_calc_combo.addItems(self.where_vars)
        where_label = QLabel("Платформа для вычислений")

        if settings:
            self.where_calc_combo.setCurrentIndex(0)
            idx = np.where(self.where_vars == settings["platform"])[0][0]
            self.where_calc_combo.setCurrentIndex(idx)

        self.cnn_combo = QComboBox()
        self.cnns = np.array([
            'YOLOv3',
            'YOLOv5l6',
            'YOLOv5x6',
            'YOLOR',
            # Detectron2 models:
            'Mask-R-CNN-R50',
            'Mask-R-CNN-R101',
            'Mask-R-CNN-X101',
            'Cascade R-CNN',
            'Retina-R50',
            'Retina-R101',
            'R-CNN-Faster-R50',
            'R-CNN-Faster-R101',
            'R-CNN-Faster-X101',
            'GN',
            # 'Deformable-Conv',
            # MMdetection models:
            'YOLACT-R101',
            'SSD',
            'DDOD-R50',
            'PAA-R101',
            'TOOD-R101-Dconv',
            'Sparce-RCNN-R50-FPN-300prop-3x',
            'Sparce-RCNN-R101-FPN-3x',
            'Dynamic R-CNN',
            'VerifocalNet-R101',
            'SOLOv2-R50',
            'SOLOv2-R101',
            'HTC-R50-1',
            'MS-R-CNN-R50',
            'SCNet-R50-20e',
            'TridentNet-R50',
            'AutoAssign',
            'FCOS-R101',
            'NAS-FCOS-R50',
            'ATSS-R101',
            'Grid R-CNN'
        ])
        self.cnn_combo.addItems(self.cnns)
        cnn_label = QLabel("Модель СНС:")

        layout.addRow(cnn_label, self.cnn_combo)
        layout.addRow(where_label, self.where_calc_combo)

        if settings:
            self.cnn_combo.setCurrentIndex(0)
            idx = np.where(self.cnns == settings["CNN"])[0][0]
            self.cnn_combo.setCurrentIndex(idx)

        self.conf_thres_spin = QDoubleSpinBox()
        self.conf_thres_spin.setDecimals(3)
        if settings:
            self.conf_thres_spin.setValue(settings['conf_thres'])
        else:
            self.conf_thres_spin.setValue(0.7)
        self.conf_thres_spin.setMinimum(0.01)
        self.conf_thres_spin.setMaximum(1.00)
        self.conf_thres_spin.setSingleStep(0.01)
        layout.addRow(QLabel("Доверительный порог:"), self.conf_thres_spin)

        self.IOU_spin = QDoubleSpinBox()
        self.IOU_spin.setDecimals(3)
        if settings:
            self.IOU_spin.setValue(settings['iou_thres'])
        else:
            self.IOU_spin.setValue(0.5)
        self.IOU_spin.setMinimum(0.01)
        self.IOU_spin.setMaximum(1.00)
        self.IOU_spin.setSingleStep(0.01)
        layout.addRow(QLabel("IOU порог:"), self.IOU_spin)

        self.formGroupBox.setLayout(layout)

        # Настройки сегментации
        self.segGroupBox = QGroupBox("Настройки сегментации")

        layout_seg = QFormLayout()

        self.stuff_button = QPushButton("Настроить классы для CNN", self)

        # setting geometry of button
        # stuff_button.setGeometry(200, 150, 100, 30)

        # adding action to a button
        self.stuff_button.clicked.connect(self.set_semseg_classes)

        self.k_means_clusters_spin = QSpinBox()
        if settings:
            self.k_means_clusters_spin.setValue(settings['k_means_clusters'])
        else:
            self.k_means_clusters_spin.setValue(2)

        self.k_means_clusters_label = QLabel("Число кластеров:")

        self.crazy_colors_label = QLabel("Использовать контрастные цвета")
        self.is_crazy_colors = QCheckBox(self)
        self.is_crazy_colors.setChecked(True)

        self.seg_combo = QComboBox()
        self.seg_models = np.array(['K-means',
                                    'Contour Detection',
                                    'Thresholding',
                                    'Color Masking',
                                    'CNN SemSeg',
                                    'RandomForest'
                                    ])
        self.seg_combo.addItems(self.seg_models)

        self.seg_combo.currentIndexChanged.connect(self.on_seg_combo_change)
        seg_label = QLabel("Метод:")

        # hor_layout.addWidget(cnn_label)
        # hor_layout.addWidget(self.cnn_combo)

        layout_seg.addRow(seg_label, self.seg_combo)

        if settings:
            self.seg_combo.setCurrentIndex(0)
            idx = np.where(self.seg_models == settings["Seg model"])[0][0]
            self.seg_combo.setCurrentIndex(idx)

        layout_seg.addRow(self.k_means_clusters_label, self.k_means_clusters_spin)

        # layout_seg.addWidget(self.is_crazy_colors)
        layout_seg.addRow(self.crazy_colors_label, self.is_crazy_colors)

        layout_seg.addRow(self.stuff_button)

        self.segGroupBox.setLayout(layout_seg)

        # настройки темы

        self.formGroupBoxGlobal = QGroupBox("Настройки приложения")

        layout_global = QFormLayout()

        self.theme_combo = QComboBox()
        self.themes = np.array(['dark_amber.xml',
                                'dark_blue.xml',
                                'dark_cyan.xml',
                                'dark_lightgreen.xml',
                                'dark_pink.xml',
                                'dark_purple.xml',
                                'dark_red.xml',
                                'dark_teal.xml',
                                'dark_yellow.xml',
                                'light_amber.xml',
                                'light_blue.xml',
                                'light_blue_500.xml',
                                'light_cyan.xml',
                                'light_cyan_500.xml',
                                'light_lightgreen.xml',
                                'light_lightgreen_500.xml',
                                'light_orange.xml',
                                'light_pink.xml',
                                'light_pink_500.xml',
                                'light_purple.xml',
                                'light_purple_500.xml',
                                'light_red.xml',
                                'light_red_500.xml',
                                'light_teal.xml',
                                'light_teal_500.xml',
                                'light_yellow.xml'])

        self.themes_rus_names = np.array(['темно-янтарная',
                                          'темно-синяя',
                                          'темно-голубая',
                                          'темно-светло-зеленая',
                                          'темно-розовая',
                                          'темно фиолетовая',
                                          'темно-красная',
                                          'темно-бирюзовая',
                                          'темно-желтая',
                                          'светлый янтарная',
                                          'светло-синяя',
                                          'светло-синяя-500',
                                          'светло-голубая',
                                          'светлый-голубая-500',
                                          'светло-зеленая',
                                          'светло-зеленая-500',
                                          'светло-оранжевая',
                                          'светло-розовая',
                                          'светло-розовая-500',
                                          'светло-фиолетовая',
                                          'светло-фиолетовая-500',
                                          'светло-красная',
                                          'светло-красная-500',
                                          'светло-бирюзовая',
                                          'светло-бирюзовая-500',
                                          'светло-желтый'])

        self.theme_combo.addItems(self.themes_rus_names)
        theme_label = QLabel("Тема приложения:")
        layout_global.addRow(theme_label, self.theme_combo)

        self.is_fit_checkbox = QCheckBox(self)
        self.is_fit_checkbox.setChecked(True)
        layout_global.addRow(QLabel("Автомасштабирование размера окна"), self.is_fit_checkbox)

        if settings:
            idx = np.where(self.themes == settings["theme"])[0][0]
            self.theme_combo.setCurrentIndex(idx)

        self.formGroupBoxGlobal.setLayout(layout_global)

        btnLayout = QHBoxLayout()

        self.okBtn = QPushButton('Принять', self)
        self.okBtn.clicked.connect(self.on_ok_clicked)

        self.cancelBtn = QPushButton('Отменить', self)
        self.cancelBtn.clicked.connect(self.on_cancel_clicked)

        btnLayout.addWidget(self.okBtn)
        btnLayout.addWidget(self.cancelBtn)

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.formGroupBoxGlobal)
        mainLayout.addWidget(self.formGroupBox)
        mainLayout.addWidget(self.segGroupBox)
        mainLayout.addLayout(btnLayout)
        self.setLayout(mainLayout)

        self.resize(500, 500)

    def set_semseg_classes(self):
        cnn_settings_window = SettingsCNN(self, self.stuff_names, selected_labels=self.selected_labels)
        cnn_settings_window.show()
        self.cnn_semseg_classes = cnn_settings_window.settings


    def on_seg_combo_change(self):
        if self.seg_combo.currentText() != "CNN SemSeg":
            if self.stuff_button:
                self.stuff_button.hide()
        else:
            if self.stuff_button:
                self.stuff_button.show()

        if self.seg_combo.currentText() != "K-means":
            if self.k_means_clusters_spin:
                self.k_means_clusters_spin.hide()
            if self.k_means_clusters_label:
                self.k_means_clusters_label.hide()
            if self.is_crazy_colors:
                self.is_crazy_colors.hide()
            if self.crazy_colors_label:
                self.crazy_colors_label.hide()
        else:
            if self.k_means_clusters_spin:
                self.k_means_clusters_spin.show()
            if self.k_means_clusters_label:
                self.k_means_clusters_label.show()
            if self.is_crazy_colors:
                self.is_crazy_colors.show()
            if self.crazy_colors_label:
                self.crazy_colors_label.show()



    def on_ok_clicked(self):
        self.settings['conf_thres'] = self.conf_thres_spin.value()
        self.settings['iou_thres'] = self.IOU_spin.value()
        self.settings['CNN'] = self.cnn_combo.currentText()
        self.settings['theme'] = self.themes[self.theme_combo.currentIndex()]
        self.settings['Seg model'] = self.seg_combo.currentText()
        self.settings['k_means_clusters'] = self.k_means_clusters_spin.value()
        self.settings['is_fit_window'] = self.is_fit_checkbox.isChecked()
        self.settings['is_crazy_colors'] = self.is_crazy_colors.isChecked()
        self.settings['cnn_semseg_classes'] = self.cnn_semseg_classes
        self.settings['platform'] = self.where_vars[self.where_calc_combo.currentIndex()]
        self.close()

    def on_cancel_clicked(self):
        self.settings.clear()
        self.close()
