# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'local_cache_install_config.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from cruiz.manage_local_cache.widgets.configpathorurl import LineEditWithCustomContextMenu


class Ui_InstallConfigDialog(object):
    def setupUi(self, InstallConfigDialog):
        if not InstallConfigDialog.objectName():
            InstallConfigDialog.setObjectName(u"InstallConfigDialog")
        InstallConfigDialog.resize(632, 409)
        self.verticalLayout = QVBoxLayout(InstallConfigDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_3 = QLabel(InstallConfigDialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)
        self.label_3.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.label_3)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)

        self.line = QFrame(InstallConfigDialog)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_4)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_4 = QLabel(InstallConfigDialog)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)

        self.label = QLabel(InstallConfigDialog)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_2 = QLabel(InstallConfigDialog)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.pathOrUrl = LineEditWithCustomContextMenu(InstallConfigDialog)
        self.pathOrUrl.setObjectName(u"pathOrUrl")

        self.gridLayout.addWidget(self.pathOrUrl, 0, 1, 1, 1)

        self.gitBranch = QLineEdit(InstallConfigDialog)
        self.gitBranch.setObjectName(u"gitBranch")

        self.gridLayout.addWidget(self.gitBranch, 1, 1, 1, 1)

        self.sourceFolder = QLineEdit(InstallConfigDialog)
        self.sourceFolder.setObjectName(u"sourceFolder")

        self.gridLayout.addWidget(self.sourceFolder, 2, 1, 1, 1)

        self.label_5 = QLabel(InstallConfigDialog)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)

        self.targetFolder = QLineEdit(InstallConfigDialog)
        self.targetFolder.setObjectName(u"targetFolder")

        self.gridLayout.addWidget(self.targetFolder, 3, 1, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.installButton = QPushButton(InstallConfigDialog)
        self.installButton.setObjectName(u"installButton")

        self.horizontalLayout.addWidget(self.installButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.line_2 = QFrame(InstallConfigDialog)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line_2)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_5)

        self.progressBar = QProgressBar(InstallConfigDialog)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setMaximum(1)
        self.progressBar.setValue(0)

        self.verticalLayout_2.addWidget(self.progressBar)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.buttonBox = QDialogButtonBox(InstallConfigDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel)

        self.verticalLayout_2.addWidget(self.buttonBox)


        self.verticalLayout.addLayout(self.verticalLayout_2)


        self.retranslateUi(InstallConfigDialog)
        self.buttonBox.accepted.connect(InstallConfigDialog.accept)
        self.buttonBox.rejected.connect(InstallConfigDialog.reject)

        QMetaObject.connectSlotsByName(InstallConfigDialog)
    # setupUi

    def retranslateUi(self, InstallConfigDialog):
        InstallConfigDialog.setWindowTitle(QCoreApplication.translate("InstallConfigDialog", u"Install config", None))
        self.label_3.setText(QCoreApplication.translate("InstallConfigDialog", u"Installing a Conan configuration to the local cache copies the archive files to the local cache.\n"
"WARNING: will overwrite existing files.\n"
"Configurations can be stored in zip files or as git repositories.\n"
"Optionally specify source and target folders to install only a portion of the configuration.", None))
        self.label_4.setText(QCoreApplication.translate("InstallConfigDialog", u"Source folder", None))
        self.label.setText(QCoreApplication.translate("InstallConfigDialog", u"Path or URL", None))
        self.label_2.setText(QCoreApplication.translate("InstallConfigDialog", u"git branch", None))
        self.pathOrUrl.setPlaceholderText(QCoreApplication.translate("InstallConfigDialog", u"Local path or remote archive or git repository URL", None))
        self.gitBranch.setPlaceholderText(QCoreApplication.translate("InstallConfigDialog", u"<default branch>", None))
        self.sourceFolder.setPlaceholderText(QCoreApplication.translate("InstallConfigDialog", u"Optional source folder in the archive", None))
        self.label_5.setText(QCoreApplication.translate("InstallConfigDialog", u"Target folder", None))
        self.targetFolder.setPlaceholderText(QCoreApplication.translate("InstallConfigDialog", u"Optional target folder in the local cache", None))
        self.installButton.setText(QCoreApplication.translate("InstallConfigDialog", u"Install", None))
    # retranslateUi

