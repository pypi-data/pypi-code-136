# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'remote_browser_fileview.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from PySide2.QtWebEngineWidgets import QWebEngineView



class Ui_remote_browser_fileview(object):
    def setupUi(self, remote_browser_fileview):
        if not remote_browser_fileview.objectName():
            remote_browser_fileview.setObjectName(u"remote_browser_fileview")
        remote_browser_fileview.resize(400, 300)
        self.verticalLayout = QVBoxLayout(remote_browser_fileview)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.fileview = QWebEngineView(remote_browser_fileview)
        self.fileview.setObjectName(u"fileview")
        self.fileview.setUrl(QUrl(u"about:blank"))

        self.verticalLayout.addWidget(self.fileview)

        self.buttonBox = QDialogButtonBox(remote_browser_fileview)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(remote_browser_fileview)
        self.buttonBox.accepted.connect(remote_browser_fileview.accept)
        self.buttonBox.rejected.connect(remote_browser_fileview.reject)

        QMetaObject.connectSlotsByName(remote_browser_fileview)
    # setupUi

    def retranslateUi(self, remote_browser_fileview):
        remote_browser_fileview.setWindowTitle(QCoreApplication.translate("remote_browser_fileview", u"Remote browser file viewer", None))
    # retranslateUi

