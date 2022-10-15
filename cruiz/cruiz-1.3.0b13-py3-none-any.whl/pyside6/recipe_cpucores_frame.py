# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'recipe_cpucores_frame.ui'
##
## Created by: Qt User Interface Compiler version 6.2.4
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QSizePolicy,
    QSpinBox, QWidget)

class Ui_cpuCoresFrame(object):
    def setupUi(self, cpuCoresFrame):
        if not cpuCoresFrame.objectName():
            cpuCoresFrame.setObjectName(u"cpuCoresFrame")
        cpuCoresFrame.resize(148, 21)
        self.horizontalLayout = QHBoxLayout(cpuCoresFrame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.cpuCoresSpin = QSpinBox(cpuCoresFrame)
        self.cpuCoresSpin.setObjectName(u"cpuCoresSpin")
        self.cpuCoresSpin.setMinimum(1)
        self.cpuCoresSpin.setMaximum(256)

        self.horizontalLayout.addWidget(self.cpuCoresSpin)


        self.retranslateUi(cpuCoresFrame)

        QMetaObject.connectSlotsByName(cpuCoresFrame)
    # setupUi

    def retranslateUi(self, cpuCoresFrame):
        cpuCoresFrame.setWindowTitle(QCoreApplication.translate("cpuCoresFrame", u"Frame", None))
        self.cpuCoresSpin.setSuffix(QCoreApplication.translate("cpuCoresFrame", u" cores", None))
    # retranslateUi

