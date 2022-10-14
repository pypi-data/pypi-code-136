# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'recipe_compiler_cache_configuration_dialog.ui'
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
    QGridLayout, QGroupBox, QLabel, QLineEdit,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_CompilerCacheConfigurationDialog(object):
    def setupUi(self, CompilerCacheConfigurationDialog):
        if not CompilerCacheConfigurationDialog.objectName():
            CompilerCacheConfigurationDialog.setObjectName(u"CompilerCacheConfigurationDialog")
        CompilerCacheConfigurationDialog.resize(313, 199)
        self.verticalLayout = QVBoxLayout(CompilerCacheConfigurationDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(CompilerCacheConfigurationDialog)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.sccache_arguments = QLineEdit(self.groupBox)
        self.sccache_arguments.setObjectName(u"sccache_arguments")

        self.gridLayout.addWidget(self.sccache_arguments, 1, 1, 1, 1)

        self.ccache_arguments = QLineEdit(self.groupBox)
        self.ccache_arguments.setObjectName(u"ccache_arguments")

        self.gridLayout.addWidget(self.ccache_arguments, 0, 1, 1, 1)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.buildcache_arguments = QLineEdit(self.groupBox)
        self.buildcache_arguments.setObjectName(u"buildcache_arguments")

        self.gridLayout.addWidget(self.buildcache_arguments, 2, 1, 1, 1)


        self.verticalLayout.addWidget(self.groupBox)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.buttonBox = QDialogButtonBox(CompilerCacheConfigurationDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Apply|QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(CompilerCacheConfigurationDialog)
        self.buttonBox.accepted.connect(CompilerCacheConfigurationDialog.accept)
        self.buttonBox.rejected.connect(CompilerCacheConfigurationDialog.reject)

        QMetaObject.connectSlotsByName(CompilerCacheConfigurationDialog)
    # setupUi

    def retranslateUi(self, CompilerCacheConfigurationDialog):
        CompilerCacheConfigurationDialog.setWindowTitle(QCoreApplication.translate("CompilerCacheConfigurationDialog", u"Compiler Cache Configuration", None))
        self.groupBox.setTitle(QCoreApplication.translate("CompilerCacheConfigurationDialog", u"Autotools configure arguments", None))
        self.label_2.setText(QCoreApplication.translate("CompilerCacheConfigurationDialog", u"SCCACHE", None))
        self.label.setText(QCoreApplication.translate("CompilerCacheConfigurationDialog", u"CCACHE", None))
        self.label_3.setText(QCoreApplication.translate("CompilerCacheConfigurationDialog", u"BUILDCACHE", None))
    # retranslateUi

