# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'recipe_cmake_features_frame.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


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

