# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'local_cache_add_remote.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from cruiz.manage_local_cache.widgets.configpathorurl import LineEditWithCustomContextMenu


class Ui_AddRemoteDialog(object):
    def setupUi(self, AddRemoteDialog):
        if not AddRemoteDialog.objectName():
            AddRemoteDialog.setObjectName(u"AddRemoteDialog")
        AddRemoteDialog.resize(447, 195)
        self.verticalLayout = QVBoxLayout(AddRemoteDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_3 = QLabel(AddRemoteDialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)
        self.label_3.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.label_3)

        self.line = QFrame(AddRemoteDialog)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_2 = QLabel(AddRemoteDialog)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.name = QLineEdit(AddRemoteDialog)
        self.name.setObjectName(u"name")

        self.gridLayout.addWidget(self.name, 0, 1, 1, 1)

        self.url = LineEditWithCustomContextMenu(AddRemoteDialog)
        self.url.setObjectName(u"url")

        self.gridLayout.addWidget(self.url, 1, 1, 1, 1)

        self.label = QLabel(AddRemoteDialog)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout)

        self.buttonBox = QDialogButtonBox(AddRemoteDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout_2.addWidget(self.buttonBox)


        self.verticalLayout.addLayout(self.verticalLayout_2)


        self.retranslateUi(AddRemoteDialog)
        self.buttonBox.accepted.connect(AddRemoteDialog.accept)
        self.buttonBox.rejected.connect(AddRemoteDialog.reject)

        QMetaObject.connectSlotsByName(AddRemoteDialog)
    # setupUi

    def retranslateUi(self, AddRemoteDialog):
        AddRemoteDialog.setWindowTitle(QCoreApplication.translate("AddRemoteDialog", u"Add remote", None))
        self.label_3.setText(QCoreApplication.translate("AddRemoteDialog", u"Adding additional remotes allows Conan to search in additional servers for published recipes and binaries.", None))
        self.label_2.setText(QCoreApplication.translate("AddRemoteDialog", u"URL", None))
        self.name.setText("")
        self.name.setPlaceholderText(QCoreApplication.translate("AddRemoteDialog", u"Name of the remote", None))
        self.url.setPlaceholderText(QCoreApplication.translate("AddRemoteDialog", u"URL of the remote", None))
        self.label.setText(QCoreApplication.translate("AddRemoteDialog", u"Name", None))
    # retranslateUi

