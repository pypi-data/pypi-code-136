# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'local_cache_run_command_dialog.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_RunConanCommandDialog(object):
    def setupUi(self, RunConanCommandDialog):
        if not RunConanCommandDialog.objectName():
            RunConanCommandDialog.setObjectName(u"RunConanCommandDialog")
        RunConanCommandDialog.resize(597, 259)
        self.verticalLayout = QVBoxLayout(RunConanCommandDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(RunConanCommandDialog)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(RunConanCommandDialog)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.arguments = QLineEdit(RunConanCommandDialog)
        self.arguments.setObjectName(u"arguments")

        self.horizontalLayout.addWidget(self.arguments)

        self.run = QPushButton(RunConanCommandDialog)
        self.run.setObjectName(u"run")

        self.horizontalLayout.addWidget(self.run)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.log = QPlainTextEdit(RunConanCommandDialog)
        self.log.setObjectName(u"log")
        self.log.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.log.setUndoRedoEnabled(False)
        self.log.setReadOnly(True)

        self.verticalLayout.addWidget(self.log)


        self.retranslateUi(RunConanCommandDialog)

        QMetaObject.connectSlotsByName(RunConanCommandDialog)
    # setupUi

    def retranslateUi(self, RunConanCommandDialog):
        RunConanCommandDialog.setWindowTitle(QCoreApplication.translate("RunConanCommandDialog", u"Run Conan command in local cache", None))
        self.label_2.setText(QCoreApplication.translate("RunConanCommandDialog", u"Enter the arguments to Conan to run the command in the selected local cache.", None))
        self.label.setText(QCoreApplication.translate("RunConanCommandDialog", u"conan", None))
        self.arguments.setPlaceholderText(QCoreApplication.translate("RunConanCommandDialog", u"<arguments>", None))
        self.run.setText(QCoreApplication.translate("RunConanCommandDialog", u"Run", None))
    # retranslateUi

