# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'local_cache_add_profile_directory.ui'
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
    QFrame, QGridLayout, QLabel, QLineEdit,
    QSizePolicy, QVBoxLayout, QWidget)

from cruiz.manage_local_cache.widgets.configpathorurl import LineEditWithCustomContextMenu

class Ui_AddExtraProfileDirectoryDialog(object):
    def setupUi(self, AddExtraProfileDirectoryDialog):
        if not AddExtraProfileDirectoryDialog.objectName():
            AddExtraProfileDirectoryDialog.setObjectName(u"AddExtraProfileDirectoryDialog")
        AddExtraProfileDirectoryDialog.resize(447, 195)
        self.verticalLayout = QVBoxLayout(AddExtraProfileDirectoryDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_3 = QLabel(AddExtraProfileDirectoryDialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)
        self.label_3.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.label_3)

        self.line = QFrame(AddExtraProfileDirectoryDialog)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_2 = QLabel(AddExtraProfileDirectoryDialog)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.name = QLineEdit(AddExtraProfileDirectoryDialog)
        self.name.setObjectName(u"name")

        self.gridLayout.addWidget(self.name, 0, 1, 1, 1)

        self.directory = LineEditWithCustomContextMenu(AddExtraProfileDirectoryDialog)
        self.directory.setObjectName(u"directory")

        self.gridLayout.addWidget(self.directory, 1, 1, 1, 1)

        self.label = QLabel(AddExtraProfileDirectoryDialog)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout)

        self.buttonBox = QDialogButtonBox(AddExtraProfileDirectoryDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout_2.addWidget(self.buttonBox)


        self.verticalLayout.addLayout(self.verticalLayout_2)


        self.retranslateUi(AddExtraProfileDirectoryDialog)
        self.buttonBox.accepted.connect(AddExtraProfileDirectoryDialog.accept)
        self.buttonBox.rejected.connect(AddExtraProfileDirectoryDialog.reject)

        QMetaObject.connectSlotsByName(AddExtraProfileDirectoryDialog)
    # setupUi

    def retranslateUi(self, AddExtraProfileDirectoryDialog):
        AddExtraProfileDirectoryDialog.setWindowTitle(QCoreApplication.translate("AddExtraProfileDirectoryDialog", u"Add extra profile directory", None))
        self.label_3.setText(QCoreApplication.translate("AddExtraProfileDirectoryDialog", u"Extra directories outside of the Conan local cache can be provided in order to scan for Conan profiles", None))
        self.label_2.setText(QCoreApplication.translate("AddExtraProfileDirectoryDialog", u"Directory", None))
        self.name.setText("")
        self.name.setPlaceholderText(QCoreApplication.translate("AddExtraProfileDirectoryDialog", u"Identifier of this directory", None))
        self.directory.setPlaceholderText(QCoreApplication.translate("AddExtraProfileDirectoryDialog", u"Directory to scan for profiles", None))
        self.label.setText(QCoreApplication.translate("AddExtraProfileDirectoryDialog", u"Name", None))
    # retranslateUi

