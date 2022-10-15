from PyQt5.QtCore import Qt
from PyQt5.QtGui import QImage, QPixmap, QPalette, QPainter
from PyQt5.QtWidgets import QLabel, QSizePolicy, QScrollArea, QMessageBox, QMainWindow, QMenu, QAction, QCheckBox, \
    QComboBox, \
    qApp, QMenuBar, QToolBar, QWidget, QGroupBox, QFileDialog, QFormLayout, QLineEdit, QComboBox, QSpinBox, QVBoxLayout, \
    QHBoxLayout, QPushButton, QDoubleSpinBox
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QImage, QFont
from PyQt5.QtPrintSupport import QPrintDialog, QPrinter
from PyQt5.QtGui import QIcon, QPalette, QColor
from PyQt5.QtWidgets import QApplication
from cnn_runner.utils.result_table import ResultsTableWindow
import os


class ShowImgWindow(QWidget):
    def __init__(self, parent, title="Изображение", is_table=True, img_file="", icon_folder="", cls_names=None,
                 cnn_type="YOLOv5",
                 parent_geo=None):
        super().__init__(parent)
        self.setWindowTitle(title)

        self.detect_info = []

        self.setWindowFlag(Qt.Window)
        self.filename = img_file
        self.is_table = is_table

        self.printer = QPrinter()
        self.scaleFactor = 0.0

        self.cnn_type = cnn_type

        if icon_folder != "":
            self.icon_folder = icon_folder
        else:
            self.icon_folder = "./icons"

        self.cls_names = cls_names

        if is_table:
            self.read_label()

        self.imageLabel = QLabel()
        self.imageLabel.setBackgroundRole(QPalette.Base)
        self.imageLabel.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self.imageLabel.setScaledContents(True)

        self.scrollArea = QScrollArea()
        self.scrollArea.setBackgroundRole(QPalette.Dark)
        self.scrollArea.setWidget(self.imageLabel)
        self.scrollArea.setVisible(False)

        self.vert_layout = QVBoxLayout(self)

        self.createActions()
        self.createToolbar()
        self.vert_layout.addWidget(self.scrollArea)
        self.open()

        self.parent_geo = parent_geo

        scale = self.get_scale_factor()
        if scale != 0:
            self.resize(int(self.image.width() * scale), int(self.image.height() * scale))
        else:
            self.resize(self.image.width(), self.image.height())

        self.show()

        if parent_geo:
            # calc parent center
            x = parent_geo.topLeft().x()
            y = parent_geo.topLeft().y()
            w = parent_geo.width()
            h = parent_geo.height()
            x_c = x + w//2
            y_c = y + h//2
            # calc pic left corner
            x_p = max(0, x_c-self.width()//2)
            y_p = max(0, y_c-self.height()//2)

            self.move(x_p, y_p)

    def read_label(self):

        label_path = os.path.join(os.path.dirname(self.filename), "labels")
        label_file = os.path.join(label_path, os.path.basename(self.filename).split(".")[0] + ".txt")

        if not os.path.exists(label_file):
            return
        detect_info = []

        with open(label_file) as f:
            for s in f:
                if self.cnn_type == 'YOLOv5l6' or self.cnn_type == "YOLOR" or self.cnn_type == 'YOLOv5x6':
                    s_list = s.split(' ')
                    if not self.cls_names:
                        detect_info.append([s_list[0].strip(), s_list[-1].strip()])
                    else:
                        name = self.cls_names[int(s_list[0].strip())]
                        prob = s_list[-1].strip()
                        detect_info.append([name, prob])

                else:
                    s_list = s.split(' ')
                    if s_list[0] == "Class":
                        if not self.cls_names:
                            detect_info.append([int(s_list[1].strip()), s_list[3].strip()])
                        else:
                            name = self.cls_names[int(s_list[1].strip())]
                            prob = s_list[3].strip()
                            detect_info.append([name, prob])

        self.detect_info = detect_info

    def get_scale_factor(self, scale=0.6):

        if self.parent_geo:
            screen = self.parent_geo.size()
            scale = 0.95

        else:
            app = QApplication.instance()
            screen = app.primaryScreen().size()

        if self.image.width() > screen.width() and self.image.height() > screen.height():
            factor = screen.width() / self.image.width()
            return factor * scale
        elif self.image.width() > screen.width():
            factor = screen.width() / self.image.width()
            return factor * scale
        elif self.image.height() > screen.height():
            factor = screen.height() / self.image.height()
            return factor * scale
        return 0

    def fit(self):
        w = self.desktop_w_h[0]
        h = self.desktop_w_h[1]
        # print(w, h)
        p_w = self.pixmap.width()
        p_h = self.pixmap.height()

        if p_w * 1.4 > w:
            scale = 0.9 * (w / (p_w * 1.4))
            # print(scale)
            p_w = int(p_w * scale)
            p_h = int(p_h * scale)
            print(p_w, p_h)
            self.pixmap = self.pixmap.scaled(p_w, p_h, aspectRatioMode=2)
            p_w = self.pixmap.width()
            p_h = self.pixmap.height()
            print(p_w, p_h)

        x = (w - p_w) // 2
        y = (h - p_h) // 2 - 30
        self.move(x, y)

    def load(self, img_file):
        pixmap = QPixmap(img_file)
        self.logoLabel.setPixmap(pixmap)
        self.fit()
        # QTimer.singleShot(100, self.pixmap)

    def open(self):
        options = QFileDialog.Options()
        # fileName = QFileDialog.getOpenFileName(self, "Open File", QDir.currentPath())
        fileName = self.filename

        if fileName:
            image = QImage(fileName)
            self.image = image
            if image.isNull():
                QMessageBox.information(self, "Модуль отображения данных",
                                        "Не могу загрузить изображение %s." % fileName)
                return

            self.imageLabel.setPixmap(QPixmap.fromImage(image))
            self.scaleFactor = 1.0

            self.scrollArea.setVisible(True)
            self.printAct.setEnabled(True)
            self.fitToWindowAct.setEnabled(True)

            self.updateActions()

            if not self.fitToWindowAct.isChecked():
                self.imageLabel.adjustSize()

            self.fitToWindowAct.setChecked(True)
            self.fitToWindow()

    def print_(self):
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
        self.scaleImage(1.25)

    def zoomOut(self):
        self.scaleImage(0.8)

    def normalSize(self):
        self.imageLabel.adjustSize()
        self.scaleFactor = 1.0

    def fitToWindow(self):
        fitToWindow = self.fitToWindowAct.isChecked()
        self.scrollArea.setWidgetResizable(fitToWindow)
        if not fitToWindow:
            self.normalSize()

        self.updateActions()

    def about(self):
        QMessageBox.about(self, "О модуле обнаружения объектов",
                          "<p><b>Модуль обнаружения объектов</b></p>"
                          "<p>Тест описания модуля</p>")

    def createActions(self):

        self.printAct = QAction("Печать...", self, shortcut="Ctrl+P", enabled=False, triggered=self.print_)
        self.printAct.setIcon(QIcon(self.icon_folder + "/printer.png"))

        self.exitAct = QAction("Выход", self, shortcut="Ctrl+Q", triggered=self.close)
        self.exitAct.setIcon(QIcon(self.icon_folder + "/logout.png"))

        self.zoomInAct = QAction("Увеличить на (25%)", self, shortcut="Ctrl++", enabled=False, triggered=self.zoomIn)
        self.zoomInAct.setIcon(QIcon(self.icon_folder + "/zoom-in.png"))

        self.zoomOutAct = QAction("Уменьшить на (25%)", self, shortcut="Ctrl+-", enabled=False, triggered=self.zoomOut)
        self.zoomOutAct.setIcon(QIcon(self.icon_folder + "/zoom-out.png"))

        self.normalSizeAct = QAction("Исходный размер", self, shortcut="Ctrl+S", enabled=False,
                                     triggered=self.normalSize)
        self.normalSizeAct.setIcon(QIcon(self.icon_folder + "/reset.png"))

        self.fitToWindowAct = QAction("Подогнать под размер окна", self, enabled=False, checkable=True,
                                      shortcut="Ctrl+F",
                                      triggered=self.fitToWindow)
        self.fitToWindowAct.setIcon(QIcon(self.icon_folder + "/fit.png"))

        if self.is_table:
            self.showTableAct = QAction("Показать результаты в виде таблицы", self, enabled=True,
                                        triggered=self.showTable)
            self.showTableAct.setIcon(QIcon(self.icon_folder + "/table.png"))

    def createMenus(self):

        self.fileMenu = QMenu("&Файл", self)
        self.fileMenu.addAction(self.printAct)
        self.fileMenu.addSeparator()
        self.fileMenu.addAction(self.exitAct)

        self.viewMenu = QMenu("&Изображение", self)
        self.viewMenu.addAction(self.zoomInAct)
        self.viewMenu.addAction(self.zoomOutAct)
        self.viewMenu.addAction(self.normalSizeAct)
        self.viewMenu.addSeparator()
        self.viewMenu.addAction(self.fitToWindowAct)

        if self.is_table:
            self.tableMenu = QMenu("Таблица", self)
            self.tableMenu.addAction(self.showTableAct)

        self.menubar = QMenuBar()
        self.menubar.addMenu(self.fileMenu)
        self.menubar.addMenu(self.viewMenu)
        self.vert_layout.addWidget(self.menubar)

    def createToolbar(self):

        toolBar = QToolBar("", self)

        toolBar.addAction(self.zoomInAct)
        toolBar.addAction(self.zoomOutAct)
        toolBar.addAction(self.fitToWindowAct)
        toolBar.addAction(self.normalSizeAct)
        if self.is_table:
            toolBar.addSeparator()
            toolBar.addAction(self.showTableAct)
        toolBar.addSeparator()
        toolBar.addAction(self.printAct)
        toolBar.addAction(self.exitAct)

        self.vert_layout.addWidget(toolBar)

    def showTable(self):

        if self.is_table:
            if len(self.detect_info) != 0:

                self._results_table_window = ResultsTableWindow(self, detect_info=self.detect_info)
                # self._settings_window.okBtn.clicked.connect(self.on_settings_closed)
                # self._settings_window.cancelBtn.clicked.connect(self.on_settings_closed)

                self._results_table_window.show()
            else:
                QMessageBox.information(self, "Модуль обнаружения объектов",
                                        "Нет обнаруженных объектов")

    def updateActions(self):
        self.zoomInAct.setEnabled(not self.fitToWindowAct.isChecked())
        self.zoomOutAct.setEnabled(not self.fitToWindowAct.isChecked())
        self.normalSizeAct.setEnabled(not self.fitToWindowAct.isChecked())

    def scaleImage(self, factor):
        self.scaleFactor *= factor
        self.imageLabel.resize(self.scaleFactor * self.imageLabel.pixmap().size())

        self.adjustScrollBar(self.scrollArea.horizontalScrollBar(), factor)
        self.adjustScrollBar(self.scrollArea.verticalScrollBar(), factor)

        self.zoomInAct.setEnabled(self.scaleFactor < 3.0)
        self.zoomOutAct.setEnabled(self.scaleFactor > 0.333)

    def adjustScrollBar(self, scrollBar, factor):
        scrollBar.setValue(int(factor * scrollBar.value()
                               + ((factor - 1) * scrollBar.pageStep() / 2)))

# if __name__=="__main__":
#     import sys
#     from PyQt5 import QtWidgets
#
#     app = QtWidgets.QApplication(sys.argv)
#     window = ShowImgWindow(title="title", img_file="D:\\MyPythonProjects\\pyqt_sns\\utils\\0 Saskuehanna.jpg")
#     # window = ShowImgWindow(title="title", img_file="D:\\MyPythonProjects\\pyqt_sns\\utils\\1 biver-valli.jpg")
#     window.setWindowTitle("Запуск и остановка потока")
#     # window.load("D:\\MyPythonProjects\\pyqt_sns\\utils\\1 biver-valli.jpg")
#     window.show()
#     sys.exit(app.exec_())
