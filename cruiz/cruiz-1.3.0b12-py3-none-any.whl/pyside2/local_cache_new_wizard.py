# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'local_cache_new_wizard.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from cruiz.manage_local_cache.widgets.newlocalcachewizardpages import NewLocalCacheNamePage
from cruiz.manage_local_cache.widgets.newlocalcachewizardpages import NewLocalCacheLocationPage
from cruiz.manage_local_cache.widgets.newlocalcachewizardpages import NewLocalCacheCreatePage


class Ui_NewLocalCacheWizard(object):
    def setupUi(self, NewLocalCacheWizard):
        if not NewLocalCacheWizard.objectName():
            NewLocalCacheWizard.setObjectName(u"NewLocalCacheWizard")
        NewLocalCacheWizard.setWindowModality(Qt.ApplicationModal)
        NewLocalCacheWizard.resize(629, 400)
        NewLocalCacheWizard.setMinimumSize(QSize(600, 290))
        NewLocalCacheWizard.setWizardStyle(QWizard.ClassicStyle)
        NewLocalCacheWizard.setOptions(QWizard.CancelButtonOnLeft)
        self.preamblePage = QWizardPage()
        self.preamblePage.setObjectName(u"preamblePage")
        self.gridLayout = QGridLayout(self.preamblePage)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.preamblePage)
        self.label.setObjectName(u"label")
        self.label.setTextFormat(Qt.MarkdownText)
        self.label.setWordWrap(True)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_2 = QLabel(self.preamblePage)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setTextFormat(Qt.MarkdownText)
        self.label_2.setWordWrap(True)

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.label_3 = QLabel(self.preamblePage)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setTextFormat(Qt.MarkdownText)
        self.label_3.setWordWrap(True)

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        NewLocalCacheWizard.addPage(self.preamblePage)
        self.namePage = NewLocalCacheNamePage()
        self.namePage.setObjectName(u"namePage")
        self.verticalLayout = QVBoxLayout(self.namePage)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_4 = QLabel(self.namePage)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setTextFormat(Qt.MarkdownText)
        self.label_4.setWordWrap(True)

        self.verticalLayout.addWidget(self.label_4)

        self.new_cache_name = QLineEdit(self.namePage)
        self.new_cache_name.setObjectName(u"new_cache_name")

        self.verticalLayout.addWidget(self.new_cache_name)

        NewLocalCacheWizard.addPage(self.namePage)
        self.locationsPage = NewLocalCacheLocationPage()
        self.locationsPage.setObjectName(u"locationsPage")
        self.verticalLayout_2 = QVBoxLayout(self.locationsPage)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_5 = QLabel(self.locationsPage)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setTextFormat(Qt.MarkdownText)
        self.label_5.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.label_5)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_6 = QLabel(self.locationsPage)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_2.addWidget(self.label_6, 0, 0, 1, 1)

        self.userHome = QLineEdit(self.locationsPage)
        self.userHome.setObjectName(u"userHome")

        self.gridLayout_2.addWidget(self.userHome, 0, 1, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout_2)

        self.userHomeShortExplanation = QLabel(self.locationsPage)
        self.userHomeShortExplanation.setObjectName(u"userHomeShortExplanation")
        self.userHomeShortExplanation.setTextFormat(Qt.MarkdownText)
        self.userHomeShortExplanation.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.userHomeShortExplanation)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.userHomeShortLabel = QLabel(self.locationsPage)
        self.userHomeShortLabel.setObjectName(u"userHomeShortLabel")

        self.gridLayout_3.addWidget(self.userHomeShortLabel, 0, 0, 1, 1)

        self.userHomeShort = QLineEdit(self.locationsPage)
        self.userHomeShort.setObjectName(u"userHomeShort")

        self.gridLayout_3.addWidget(self.userHomeShort, 0, 1, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout_3)

        NewLocalCacheWizard.addPage(self.locationsPage)
        self.configPage = QWizardPage()
        self.configPage.setObjectName(u"configPage")
        self.verticalLayout_3 = QVBoxLayout(self.configPage)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_7 = QLabel(self.configPage)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setWordWrap(True)

        self.verticalLayout_3.addWidget(self.label_7)

        self.queryConfigInstall = QCheckBox(self.configPage)
        self.queryConfigInstall.setObjectName(u"queryConfigInstall")
        self.queryConfigInstall.setChecked(True)

        self.verticalLayout_3.addWidget(self.queryConfigInstall)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.configUrl = QLabel(self.configPage)
        self.configUrl.setObjectName(u"configUrl")

        self.gridLayout_4.addWidget(self.configUrl, 0, 1, 1, 1)

        self.configBranch = QLabel(self.configPage)
        self.configBranch.setObjectName(u"configBranch")

        self.gridLayout_4.addWidget(self.configBranch, 1, 1, 1, 1)

        self.label_8 = QLabel(self.configPage)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_4.addWidget(self.label_8, 0, 0, 1, 1)

        self.label_9 = QLabel(self.configPage)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_4.addWidget(self.label_9, 1, 0, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayout_4)

        NewLocalCacheWizard.addPage(self.configPage)
        self.createPage = NewLocalCacheCreatePage()
        self.createPage.setObjectName(u"createPage")
        self.verticalLayout_4 = QVBoxLayout(self.createPage)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_10 = QLabel(self.createPage)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout_4.addWidget(self.label_10)

        self.summary_name = QLabel(self.createPage)
        self.summary_name.setObjectName(u"summary_name")

        self.verticalLayout_4.addWidget(self.summary_name)

        self.summary_user_home = QLabel(self.createPage)
        self.summary_user_home.setObjectName(u"summary_user_home")

        self.verticalLayout_4.addWidget(self.summary_user_home)

        self.summary_user_home_short = QLabel(self.createPage)
        self.summary_user_home_short.setObjectName(u"summary_user_home_short")

        self.verticalLayout_4.addWidget(self.summary_user_home_short)

        self.summary_install_config = QLabel(self.createPage)
        self.summary_install_config.setObjectName(u"summary_install_config")
        self.summary_install_config.setWordWrap(True)

        self.verticalLayout_4.addWidget(self.summary_install_config)

        self.summary_switch_to_new = QCheckBox(self.createPage)
        self.summary_switch_to_new.setObjectName(u"summary_switch_to_new")

        self.verticalLayout_4.addWidget(self.summary_switch_to_new)

        self.createCache = QPushButton(self.createPage)
        self.createCache.setObjectName(u"createCache")

        self.verticalLayout_4.addWidget(self.createCache)

        self.createProgress = QProgressBar(self.createPage)
        self.createProgress.setObjectName(u"createProgress")
        self.createProgress.setValue(24)

        self.verticalLayout_4.addWidget(self.createProgress)

        self.summary_log = QPlainTextEdit(self.createPage)
        self.summary_log.setObjectName(u"summary_log")
        self.summary_log.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.summary_log.setUndoRedoEnabled(False)
        self.summary_log.setReadOnly(True)

        self.verticalLayout_4.addWidget(self.summary_log)

        NewLocalCacheWizard.addPage(self.createPage)

        self.retranslateUi(NewLocalCacheWizard)

        self.createCache.setDefault(True)


        QMetaObject.connectSlotsByName(NewLocalCacheWizard)
    # setupUi

    def retranslateUi(self, NewLocalCacheWizard):
        NewLocalCacheWizard.setWindowTitle(QCoreApplication.translate("NewLocalCacheWizard", u"New Local Cache", None))
        self.label.setText(QCoreApplication.translate("NewLocalCacheWizard", u"Conan's local cache is a directory that can contain the following:\n"
"* Configuration metadata controlling the behaviour of Conan.\n"
"* Profiles containing logically grouped data controlling package identification.\n"
"* Lists of external Artifactory remotes.\n"
"* Python scripts that hook into Conan commands.\n"
"\n"
"The default local cache is in your home directory.\n"
"Multiple local caches may exist though, and can switch Conan between them via environment variables.", None))
        self.label_2.setText(QCoreApplication.translate("NewLocalCacheWizard", u"cruiz associates recipes with local caches.\n"
"Conan itself does not do this.\n"
"cruiz manages the local caches it is made aware of.", None))
        self.label_3.setText(QCoreApplication.translate("NewLocalCacheWizard", u"This wizard allows the user to create new local caches, or make cruiz aware of existing local caches.", None))
        self.label_4.setText(QCoreApplication.translate("NewLocalCacheWizard", u"cruiz requires a name to associate with a local cache", None))
        self.new_cache_name.setPlaceholderText(QCoreApplication.translate("NewLocalCacheWizard", u"Enter name of the local cache", None))
        self.label_5.setText(QCoreApplication.translate("NewLocalCacheWizard", u"Each local cache exists in a .conan folder in the specified directory.", None))
        self.label_6.setText(QCoreApplication.translate("NewLocalCacheWizard", u"CONAN_USER_HOME", None))
        self.userHomeShortExplanation.setText(QCoreApplication.translate("NewLocalCacheWizard", u"\n"
"\n"
"On Windows, a path to where 'short' package paths are stored is also required.", None))
        self.userHomeShortLabel.setText(QCoreApplication.translate("NewLocalCacheWizard", u"CONAN_USER_HOME_SHORT", None))
        self.label_7.setText(QCoreApplication.translate("NewLocalCacheWizard", u"After creating the new local cache, a configuration can be installed to it to set it up to your site or product policies.", None))
        self.queryConfigInstall.setText(QCoreApplication.translate("NewLocalCacheWizard", u"Install the default configuration to this new local cache?", None))
        self.configUrl.setText(QCoreApplication.translate("NewLocalCacheWizard", u"<empty>", None))
        self.configBranch.setText(QCoreApplication.translate("NewLocalCacheWizard", u"<empty>", None))
        self.label_8.setText(QCoreApplication.translate("NewLocalCacheWizard", u"URL", None))
        self.label_9.setText(QCoreApplication.translate("NewLocalCacheWizard", u"Branch", None))
        self.label_10.setText(QCoreApplication.translate("NewLocalCacheWizard", u"Click Create to make the following local cache from this summary:", None))
        self.summary_name.setText(QCoreApplication.translate("NewLocalCacheWizard", u"<name>", None))
        self.summary_user_home.setText(QCoreApplication.translate("NewLocalCacheWizard", u"<user home>", None))
        self.summary_user_home_short.setText(QCoreApplication.translate("NewLocalCacheWizard", u"<user home short>", None))
        self.summary_install_config.setText(QCoreApplication.translate("NewLocalCacheWizard", u"<install configuration>", None))
        self.summary_switch_to_new.setText(QCoreApplication.translate("NewLocalCacheWizard", u"Switch to the new local cache", None))
        self.createCache.setText(QCoreApplication.translate("NewLocalCacheWizard", u"Create", None))
    # retranslateUi

