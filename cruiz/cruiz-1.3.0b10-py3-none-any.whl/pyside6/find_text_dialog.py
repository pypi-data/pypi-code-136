# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'find_text_dialog.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QCheckBox, QDialog,
    QDialogButtonBox, QFormLayout, QLabel, QLineEdit,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_FindTextDialog(object):
    def setupUi(self, FindTextDialog):
        if not FindTextDialog.objectName():
            FindTextDialog.setObjectName(u"FindTextDialog")
        FindTextDialog.resize(258, 147)
        self.verticalLayout = QVBoxLayout(FindTextDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(FindTextDialog)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.findTextSearch = QLineEdit(FindTextDialog)
        self.findTextSearch.setObjectName(u"findTextSearch")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.findTextSearch)

        self.findTextCaseSensitive = QCheckBox(FindTextDialog)
        self.findTextCaseSensitive.setObjectName(u"findTextCaseSensitive")
        self.findTextCaseSensitive.setChecked(True)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.findTextCaseSensitive)

        self.findTextWraparound = QCheckBox(FindTextDialog)
        self.findTextWraparound.setObjectName(u"findTextWraparound")
        self.findTextWraparound.setChecked(True)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.findTextWraparound)


        self.verticalLayout.addLayout(self.formLayout)

        self.findTextButtonBox = QDialogButtonBox(FindTextDialog)
        self.findTextButtonBox.setObjectName(u"findTextButtonBox")
        self.findTextButtonBox.setOrientation(Qt.Horizontal)
        self.findTextButtonBox.setStandardButtons(QDialogButtonBox.NoButton)

        self.verticalLayout.addWidget(self.findTextButtonBox)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(FindTextDialog)
        self.findTextButtonBox.accepted.connect(FindTextDialog.accept)
        self.findTextButtonBox.rejected.connect(FindTextDialog.reject)

        QMetaObject.connectSlotsByName(FindTextDialog)
    # setupUi

    def retranslateUi(self, FindTextDialog):
        FindTextDialog.setWindowTitle(QCoreApplication.translate("FindTextDialog", u"Find text", None))
        self.label.setText(QCoreApplication.translate("FindTextDialog", u"Search", None))
        self.findTextCaseSensitive.setText(QCoreApplication.translate("FindTextDialog", u"Case sensitive", None))
        self.findTextWraparound.setText(QCoreApplication.translate("FindTextDialog", u"Wraparound", None))
    # retranslateUi

