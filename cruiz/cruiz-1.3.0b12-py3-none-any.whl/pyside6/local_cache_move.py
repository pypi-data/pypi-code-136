# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'local_cache_move.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QGridLayout, QLabel, QLineEdit, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_LocalCacheMove(object):
    def setupUi(self, LocalCacheMove):
        if not LocalCacheMove.objectName():
            LocalCacheMove.setObjectName(u"LocalCacheMove")
        LocalCacheMove.resize(632, 158)
        self.verticalLayout = QVBoxLayout(LocalCacheMove)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_4 = QLabel(LocalCacheMove)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 0, 2, 1, 1)

        self.newUserHome = QLineEdit(LocalCacheMove)
        self.newUserHome.setObjectName(u"newUserHome")

        self.gridLayout.addWidget(self.newUserHome, 1, 2, 1, 1)

        self.label = QLabel(LocalCacheMove)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

        self.label_3 = QLabel(LocalCacheMove)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 0, 1, 1, 1)

        self.currentUserHome = QLabel(LocalCacheMove)
        self.currentUserHome.setObjectName(u"currentUserHome")

        self.gridLayout.addWidget(self.currentUserHome, 1, 1, 1, 1)

        self.userHomeShortLabel = QLabel(LocalCacheMove)
        self.userHomeShortLabel.setObjectName(u"userHomeShortLabel")

        self.gridLayout.addWidget(self.userHomeShortLabel, 2, 0, 1, 1)

        self.currentUserHomeShort = QLabel(LocalCacheMove)
        self.currentUserHomeShort.setObjectName(u"currentUserHomeShort")

        self.gridLayout.addWidget(self.currentUserHomeShort, 2, 1, 1, 1)

        self.newUserHomeShort = QLineEdit(LocalCacheMove)
        self.newUserHomeShort.setObjectName(u"newUserHomeShort")

        self.gridLayout.addWidget(self.newUserHomeShort, 2, 2, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout)

        self.buttonBox = QDialogButtonBox(LocalCacheMove)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout_2.addWidget(self.buttonBox)


        self.verticalLayout.addLayout(self.verticalLayout_2)


        self.retranslateUi(LocalCacheMove)

        QMetaObject.connectSlotsByName(LocalCacheMove)
    # setupUi

    def retranslateUi(self, LocalCacheMove):
        LocalCacheMove.setWindowTitle(QCoreApplication.translate("LocalCacheMove", u"Move local cache", None))
        self.label_4.setText(QCoreApplication.translate("LocalCacheMove", u"New", None))
        self.label.setText(QCoreApplication.translate("LocalCacheMove", u"CONAN_USER_HOME", None))
        self.label_3.setText(QCoreApplication.translate("LocalCacheMove", u"Current", None))
        self.currentUserHome.setText(QCoreApplication.translate("LocalCacheMove", u"<empty>", None))
        self.userHomeShortLabel.setText(QCoreApplication.translate("LocalCacheMove", u"CONAN_USER_HOME_SHORT", None))
        self.currentUserHomeShort.setText(QCoreApplication.translate("LocalCacheMove", u"<empty>", None))
    # retranslateUi

