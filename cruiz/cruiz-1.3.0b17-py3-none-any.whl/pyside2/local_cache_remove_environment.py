# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'local_cache_remove_environment.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from cruiz.manage_local_cache.widgets.configpathorurl import LineEditWithCustomContextMenu


class Ui_RemoveEnvironmentDialog(object):
    def setupUi(self, RemoveEnvironmentDialog):
        if not RemoveEnvironmentDialog.objectName():
            RemoveEnvironmentDialog.setObjectName(u"RemoveEnvironmentDialog")
        RemoveEnvironmentDialog.resize(447, 181)
        self.verticalLayout = QVBoxLayout(RemoveEnvironmentDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_3 = QLabel(RemoveEnvironmentDialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)
        self.label_3.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.label_3)

        self.line = QFrame(RemoveEnvironmentDialog)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(RemoveEnvironmentDialog)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.name = LineEditWithCustomContextMenu(RemoveEnvironmentDialog)
        self.name.setObjectName(u"name")

        self.gridLayout.addWidget(self.name, 0, 1, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout)

        self.buttonBox = QDialogButtonBox(RemoveEnvironmentDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout_2.addWidget(self.buttonBox)


        self.verticalLayout.addLayout(self.verticalLayout_2)


        self.retranslateUi(RemoveEnvironmentDialog)
        self.buttonBox.accepted.connect(RemoveEnvironmentDialog.accept)
        self.buttonBox.rejected.connect(RemoveEnvironmentDialog.reject)

        QMetaObject.connectSlotsByName(RemoveEnvironmentDialog)
    # setupUi

    def retranslateUi(self, RemoveEnvironmentDialog):
        RemoveEnvironmentDialog.setWindowTitle(QCoreApplication.translate("RemoveEnvironmentDialog", u"Remove from environment", None))
        self.label_3.setText(QCoreApplication.translate("RemoveEnvironmentDialog", u"Remove environment variable for all commands run through this local cache.", None))
        self.label.setText(QCoreApplication.translate("RemoveEnvironmentDialog", u"Name", None))
        self.name.setText("")
        self.name.setPlaceholderText(QCoreApplication.translate("RemoveEnvironmentDialog", u"Name of the variable", None))
    # retranslateUi

