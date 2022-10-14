# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'recipe_cmake_features_frame.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QHBoxLayout,
    QSizePolicy, QWidget)

class Ui_cmakeFeaturesFrame(object):
    def setupUi(self, cmakeFeaturesFrame):
        if not cmakeFeaturesFrame.objectName():
            cmakeFeaturesFrame.setObjectName(u"cmakeFeaturesFrame")
        cmakeFeaturesFrame.resize(270, 39)
        self.horizontalLayout = QHBoxLayout(cmakeFeaturesFrame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.cmakeFindDebug = QCheckBox(cmakeFeaturesFrame)
        self.cmakeFindDebug.setObjectName(u"cmakeFindDebug")

        self.horizontalLayout.addWidget(self.cmakeFindDebug)

        self.cmakeVerbose = QCheckBox(cmakeFeaturesFrame)
        self.cmakeVerbose.setObjectName(u"cmakeVerbose")

        self.horizontalLayout.addWidget(self.cmakeVerbose)


        self.retranslateUi(cmakeFeaturesFrame)

        QMetaObject.connectSlotsByName(cmakeFeaturesFrame)
    # setupUi

    def retranslateUi(self, cmakeFeaturesFrame):
        cmakeFeaturesFrame.setWindowTitle(QCoreApplication.translate("cmakeFeaturesFrame", u"Frame", None))
#if QT_CONFIG(tooltip)
        self.cmakeFindDebug.setToolTip(QCoreApplication.translate("cmakeFeaturesFrame", u"Append CMAKE_FIND_DEBUG_MODE=ON to the CMake definitions used during configuration.  Requires CMake 3.17+.", None))
#endif // QT_CONFIG(tooltip)
        self.cmakeFindDebug.setText(QCoreApplication.translate("cmakeFeaturesFrame", u"CMake find debug", None))
#if QT_CONFIG(tooltip)
        self.cmakeVerbose.setToolTip(QCoreApplication.translate("cmakeFeaturesFrame", u"Append CMAKE_VERBOSE_MAKEFILE=ON to the CMake definitions used during configuration.", None))
#endif // QT_CONFIG(tooltip)
        self.cmakeVerbose.setText(QCoreApplication.translate("cmakeFeaturesFrame", u"CMake verbose", None))
    # retranslateUi

