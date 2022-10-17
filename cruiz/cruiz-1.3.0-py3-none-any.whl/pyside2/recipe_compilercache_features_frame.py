# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'recipe_compilercache_features_frame.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_compilerCacheFrame(object):
    def setupUi(self, compilerCacheFrame):
        if not compilerCacheFrame.objectName():
            compilerCacheFrame.setObjectName(u"compilerCacheFrame")
        compilerCacheFrame.resize(358, 50)
        self.horizontalLayout = QHBoxLayout(compilerCacheFrame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.useCache = QCheckBox(compilerCacheFrame)
        self.useCache.setObjectName(u"useCache")

        self.horizontalLayout.addWidget(self.useCache)

        self.chooseCache = QComboBox(compilerCacheFrame)
        self.chooseCache.addItem("")
        self.chooseCache.addItem("")
        self.chooseCache.addItem("")
        self.chooseCache.addItem("")
        self.chooseCache.setObjectName(u"chooseCache")

        self.horizontalLayout.addWidget(self.chooseCache)

        self.configureCache = QPushButton(compilerCacheFrame)
        self.configureCache.setObjectName(u"configureCache")

        self.horizontalLayout.addWidget(self.configureCache)


        self.retranslateUi(compilerCacheFrame)

        QMetaObject.connectSlotsByName(compilerCacheFrame)
    # setupUi

    def retranslateUi(self, compilerCacheFrame):
        compilerCacheFrame.setWindowTitle(QCoreApplication.translate("compilerCacheFrame", u"Frame", None))
#if QT_CONFIG(tooltip)
        self.useCache.setToolTip(QCoreApplication.translate("compilerCacheFrame", u"Enable specifying the compiler cache for just this recipe.", None))
#endif // QT_CONFIG(tooltip)
        self.useCache.setText(QCoreApplication.translate("compilerCacheFrame", u"Compiler cache", None))
        self.chooseCache.setItemText(0, QCoreApplication.translate("compilerCacheFrame", u"None", None))
        self.chooseCache.setItemText(1, QCoreApplication.translate("compilerCacheFrame", u"ccache", None))
        self.chooseCache.setItemText(2, QCoreApplication.translate("compilerCacheFrame", u"sccache", None))
        self.chooseCache.setItemText(3, QCoreApplication.translate("compilerCacheFrame", u"buildcache", None))

#if QT_CONFIG(tooltip)
        self.chooseCache.setToolTip(QCoreApplication.translate("compilerCacheFrame", u"The recipe specific compiler cache that attempts to integrate with Conan's CMake and Autotools helpers.  The cruiz icon is shown beside the preferences default.  YMMV.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.configureCache.setToolTip(QCoreApplication.translate("compilerCacheFrame", u"Configure compiler caches for this recipe.", None))
#endif // QT_CONFIG(tooltip)
        self.configureCache.setText(QCoreApplication.translate("compilerCacheFrame", u"Configure...", None))
    # retranslateUi

