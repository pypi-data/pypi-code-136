# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'recipe_profile_frame.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLabel, QSizePolicy, QWidget)

class Ui_profileFrame(object):
    def setupUi(self, profileFrame):
        if not profileFrame.objectName():
            profileFrame.setObjectName(u"profileFrame")
        profileFrame.resize(131, 32)
        self.horizontalLayout = QHBoxLayout(profileFrame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.profileLabel = QLabel(profileFrame)
        self.profileLabel.setObjectName(u"profileLabel")

        self.horizontalLayout.addWidget(self.profileLabel)

        self.profileCombo = QComboBox(profileFrame)
        self.profileCombo.setObjectName(u"profileCombo")
        self.profileCombo.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.horizontalLayout.addWidget(self.profileCombo)


        self.retranslateUi(profileFrame)

        QMetaObject.connectSlotsByName(profileFrame)
    # setupUi

    def retranslateUi(self, profileFrame):
        profileFrame.setWindowTitle(QCoreApplication.translate("profileFrame", u"Frame", None))
        self.profileLabel.setText(QCoreApplication.translate("profileFrame", u"Profile:", None))
    # retranslateUi

