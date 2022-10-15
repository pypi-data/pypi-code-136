# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'local_cache_add_environment.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from cruiz.manage_local_cache.widgets.configpathorurl import LineEditWithCustomContextMenu


class Ui_AddEnvironmentDialog(object):
    def setupUi(self, AddEnvironmentDialog):
        if not AddEnvironmentDialog.objectName():
            AddEnvironmentDialog.setObjectName(u"AddEnvironmentDialog")
        AddEnvironmentDialog.resize(447, 195)
        self.verticalLayout = QVBoxLayout(AddEnvironmentDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_3 = QLabel(AddEnvironmentDialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)
        self.label_3.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.label_3)

        self.line = QFrame(AddEnvironmentDialog)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_2 = QLabel(AddEnvironmentDialog)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.name = LineEditWithCustomContextMenu(AddEnvironmentDialog)
        self.name.setObjectName(u"name")

        self.gridLayout.addWidget(self.name, 0, 1, 1, 1)

        self.value = QLineEdit(AddEnvironmentDialog)
        self.value.setObjectName(u"value")

        self.gridLayout.addWidget(self.value, 1, 1, 1, 1)

        self.label = QLabel(AddEnvironmentDialog)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout)

        self.buttonBox = QDialogButtonBox(AddEnvironmentDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout_2.addWidget(self.buttonBox)


        self.verticalLayout.addLayout(self.verticalLayout_2)


        self.retranslateUi(AddEnvironmentDialog)
        self.buttonBox.accepted.connect(AddEnvironmentDialog.accept)
        self.buttonBox.rejected.connect(AddEnvironmentDialog.reject)

        QMetaObject.connectSlotsByName(AddEnvironmentDialog)
    # setupUi

    def retranslateUi(self, AddEnvironmentDialog):
        AddEnvironmentDialog.setWindowTitle(QCoreApplication.translate("AddEnvironmentDialog", u"Add environment", None))
        self.label_3.setText(QCoreApplication.translate("AddEnvironmentDialog", u"Add environment variables. Prefer the use of config variables but this may be used for other purposes.", None))
        self.label_2.setText(QCoreApplication.translate("AddEnvironmentDialog", u"Value", None))
        self.name.setText("")
        self.name.setPlaceholderText(QCoreApplication.translate("AddEnvironmentDialog", u"Name of the variable", None))
        self.value.setPlaceholderText(QCoreApplication.translate("AddEnvironmentDialog", u"Value of the variable", None))
        self.label.setText(QCoreApplication.translate("AddEnvironmentDialog", u"Name", None))
    # retranslateUi

