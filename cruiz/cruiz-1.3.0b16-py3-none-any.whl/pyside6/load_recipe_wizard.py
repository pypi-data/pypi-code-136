# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'load_recipe_wizard.ui'
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QComboBox, QHBoxLayout,
    QPlainTextEdit, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget, QWizard)

from cruiz.load_recipe.pages.initialprofilepage import LoadRecipeInitialProfilePage
from cruiz.load_recipe.pages.intropage import LoadRecipeIntroPage
from cruiz.load_recipe.pages.localcachepage import LoadRecipeLocalCachePage
from cruiz.load_recipe.pages.packageversionpage import LoadRecipePackageVersionPage

class Ui_LoadRecipeWizard(object):
    def setupUi(self, LoadRecipeWizard):
        if not LoadRecipeWizard.objectName():
            LoadRecipeWizard.setObjectName(u"LoadRecipeWizard")
        LoadRecipeWizard.resize(443, 330)
        LoadRecipeWizard.setWizardStyle(QWizard.ClassicStyle)
        LoadRecipeWizard.setOptions(QWizard.CancelButtonOnLeft|QWizard.HaveFinishButtonOnEarlyPages|QWizard.NoDefaultButton)
        self.intro = LoadRecipeIntroPage()
        self.intro.setObjectName(u"intro")
        self.verticalLayout = QVBoxLayout(self.intro)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.intro_message = QPlainTextEdit(self.intro)
        self.intro_message.setObjectName(u"intro_message")
        self.intro_message.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.verticalLayout.addWidget(self.intro_message)

        LoadRecipeWizard.setPage(0, self.intro)
        self.localcache = LoadRecipeLocalCachePage()
        self.localcache.setObjectName(u"localcache")
        self.verticalLayout_2 = QVBoxLayout(self.localcache)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.local_cache_name = QComboBox(self.localcache)
        self.local_cache_name.setObjectName(u"local_cache_name")

        self.verticalLayout_2.addWidget(self.local_cache_name)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.manage_caches = QPushButton(self.localcache)
        self.manage_caches.setObjectName(u"manage_caches")

        self.horizontalLayout.addWidget(self.manage_caches)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        LoadRecipeWizard.setPage(2, self.localcache)
        self.packageversion = LoadRecipePackageVersionPage()
        self.packageversion.setObjectName(u"packageversion")
        self.verticalLayout_3 = QVBoxLayout(self.packageversion)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.version = QComboBox(self.packageversion)
        self.version.setObjectName(u"version")

        self.verticalLayout_3.addWidget(self.version)

        LoadRecipeWizard.setPage(1, self.packageversion)
        self.initialprofile = LoadRecipeInitialProfilePage()
        self.initialprofile.setObjectName(u"initialprofile")
        self.verticalLayout_4 = QVBoxLayout(self.initialprofile)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.initial_profile = QComboBox(self.initialprofile)
        self.initial_profile.setObjectName(u"initial_profile")

        self.verticalLayout_4.addWidget(self.initial_profile)

        self.initial_profile_log = QPlainTextEdit(self.initialprofile)
        self.initial_profile_log.setObjectName(u"initial_profile_log")
        self.initial_profile_log.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.initial_profile_log.setReadOnly(True)

        self.verticalLayout_4.addWidget(self.initial_profile_log)

        LoadRecipeWizard.setPage(3, self.initialprofile)

        self.retranslateUi(LoadRecipeWizard)

        QMetaObject.connectSlotsByName(LoadRecipeWizard)
    # setupUi

    def retranslateUi(self, LoadRecipeWizard):
        LoadRecipeWizard.setWindowTitle(QCoreApplication.translate("LoadRecipeWizard", u"Load recipe wizard", None))
        self.intro.setTitle(QCoreApplication.translate("LoadRecipeWizard", u"Load Conan recipe", None))
        self.intro.setSubTitle(QCoreApplication.translate("LoadRecipeWizard", u"Use this wizard to bind to a recipe version, associate with a local cache, and select an initial profile.", None))
        self.localcache.setTitle(QCoreApplication.translate("LoadRecipeWizard", u"Local cache", None))
        self.localcache.setSubTitle(QCoreApplication.translate("LoadRecipeWizard", u"Choose the local cache to associate the recipe with.", None))
        self.manage_caches.setText(QCoreApplication.translate("LoadRecipeWizard", u"Manage local caches...", None))
        self.packageversion.setTitle(QCoreApplication.translate("LoadRecipeWizard", u"Package version", None))
        self.packageversion.setSubTitle(QCoreApplication.translate("LoadRecipeWizard", u"Choose a version to bind with this instance of the recipe.", None))
        self.initialprofile.setTitle(QCoreApplication.translate("LoadRecipeWizard", u"Initial profile", None))
        self.initialprofile.setSubTitle(QCoreApplication.translate("LoadRecipeWizard", u"Choose the initial profile from the local cache to use with the recipe.", None))
    # retranslateUi

