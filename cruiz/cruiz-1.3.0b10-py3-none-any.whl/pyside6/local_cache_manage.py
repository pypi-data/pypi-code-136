# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'local_cache_manage.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QAbstractItemView, QAbstractScrollArea, QApplication,
    QCheckBox, QComboBox, QDialog, QDialogButtonBox,
    QGridLayout, QGroupBox, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QListWidget, QListWidgetItem,
    QPlainTextEdit, QPushButton, QSizePolicy, QSpacerItem,
    QTabWidget, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

from cruiz.manage_local_cache.widgets.keyvaluetable import KeyValueTable
from cruiz.manage_local_cache.widgets.remotestable import RemotesTable

class Ui_ManageLocalCaches(object):
    def setupUi(self, ManageLocalCaches):
        if not ManageLocalCaches.objectName():
            ManageLocalCaches.setObjectName(u"ManageLocalCaches")
        ManageLocalCaches.resize(561, 639)
        self.verticalLayout = QVBoxLayout(ManageLocalCaches)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.cacheNameLayout = QHBoxLayout()
        self.cacheNameLayout.setObjectName(u"cacheNameLayout")
        self.local_cache_names = QComboBox(ManageLocalCaches)
        self.local_cache_names.setObjectName(u"local_cache_names")

        self.cacheNameLayout.addWidget(self.local_cache_names)

        self.new_local_cache_button = QPushButton(ManageLocalCaches)
        self.new_local_cache_button.setObjectName(u"new_local_cache_button")
        self.new_local_cache_button.setMaximumSize(QSize(75, 16777215))

        self.cacheNameLayout.addWidget(self.new_local_cache_button)


        self.verticalLayout_5.addLayout(self.cacheNameLayout)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_2)

        self.localCacheInfo = QTabWidget(ManageLocalCaches)
        self.localCacheInfo.setObjectName(u"localCacheInfo")
        self.locationsTab = QWidget()
        self.locationsTab.setObjectName(u"locationsTab")
        self.gridLayout = QGridLayout(self.locationsTab)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_5, 2, 0, 1, 1)

        self.locationsLayout = QGridLayout()
        self.locationsLayout.setObjectName(u"locationsLayout")
        self.loc_conan_user_home_short_label = QLabel(self.locationsTab)
        self.loc_conan_user_home_short_label.setObjectName(u"loc_conan_user_home_short_label")
        self.loc_conan_user_home_short_label.setEnabled(False)

        self.locationsLayout.addWidget(self.loc_conan_user_home_short_label, 1, 0, 1, 1)

        self.label_5 = QLabel(self.locationsTab)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setEnabled(False)

        self.locationsLayout.addWidget(self.label_5, 0, 0, 1, 1)

        self.conan_user_home = QLineEdit(self.locationsTab)
        self.conan_user_home.setObjectName(u"conan_user_home")

        self.locationsLayout.addWidget(self.conan_user_home, 0, 1, 1, 1)

        self.conan_user_home_short = QLineEdit(self.locationsTab)
        self.conan_user_home_short.setObjectName(u"conan_user_home_short")

        self.locationsLayout.addWidget(self.conan_user_home_short, 1, 1, 1, 1)


        self.gridLayout.addLayout(self.locationsLayout, 0, 0, 1, 1)

        self.localCacheRecipeCount = QLabel(self.locationsTab)
        self.localCacheRecipeCount.setObjectName(u"localCacheRecipeCount")
        self.localCacheRecipeCount.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.localCacheRecipeCount, 1, 0, 1, 1)

        self.localCacheInfo.addTab(self.locationsTab, "")
        self.profilesTab = QWidget()
        self.profilesTab.setObjectName(u"profilesTab")
        self.verticalLayout_7 = QVBoxLayout(self.profilesTab)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.groupBox_2 = QGroupBox(self.profilesTab)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(2, 2, 2, 2)
        self.profilesList = QListWidget(self.groupBox_2)
        self.profilesList.setObjectName(u"profilesList")
        self.profilesList.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.verticalLayout_3.addWidget(self.profilesList)


        self.verticalLayout_6.addWidget(self.groupBox_2)

        self.groupBox = QGroupBox(self.profilesTab)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_4 = QVBoxLayout(self.groupBox)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.profilesTable = KeyValueTable(self.groupBox)
        if (self.profilesTable.columnCount() < 2):
            self.profilesTable.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.profilesTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.profilesTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.profilesTable.setObjectName(u"profilesTable")
        self.profilesTable.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.profilesTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.profilesTable.setAlternatingRowColors(True)
        self.profilesTable.setSelectionMode(QAbstractItemView.SingleSelection)
        self.profilesTable.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.profilesTable.horizontalHeader().setStretchLastSection(True)
        self.profilesTable.verticalHeader().setVisible(False)

        self.horizontalLayout_5.addWidget(self.profilesTable)

        self.profilesTableButtons = QDialogButtonBox(self.groupBox)
        self.profilesTableButtons.setObjectName(u"profilesTableButtons")
        self.profilesTableButtons.setOrientation(Qt.Vertical)
        self.profilesTableButtons.setStandardButtons(QDialogButtonBox.Close|QDialogButtonBox.Open)

        self.horizontalLayout_5.addWidget(self.profilesTableButtons)


        self.verticalLayout_4.addLayout(self.horizontalLayout_5)


        self.verticalLayout_6.addWidget(self.groupBox)


        self.verticalLayout_7.addLayout(self.verticalLayout_6)

        self.localCacheInfo.addTab(self.profilesTab, "")
        self.configTab = QWidget()
        self.configTab.setObjectName(u"configTab")
        self.verticalLayout_9 = QVBoxLayout(self.configTab)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.configPrintRunCommands = QCheckBox(self.configTab)
        self.configPrintRunCommands.setObjectName(u"configPrintRunCommands")

        self.verticalLayout_9.addWidget(self.configPrintRunCommands)

        self.configRevisions = QCheckBox(self.configTab)
        self.configRevisions.setObjectName(u"configRevisions")

        self.verticalLayout_9.addWidget(self.configRevisions)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_8)

        self.localCacheInfo.addTab(self.configTab, "")
        self.remotesTab = QWidget()
        self.remotesTab.setObjectName(u"remotesTab")
        self.verticalLayout_10 = QVBoxLayout(self.remotesTab)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.remotesTable = RemotesTable(self.remotesTab)
        if (self.remotesTable.columnCount() < 3):
            self.remotesTable.setColumnCount(3)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.remotesTable.setHorizontalHeaderItem(0, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.remotesTable.setHorizontalHeaderItem(1, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.remotesTable.setHorizontalHeaderItem(2, __qtablewidgetitem4)
        self.remotesTable.setObjectName(u"remotesTable")
        self.remotesTable.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.remotesTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.remotesTable.setDragDropOverwriteMode(False)
        self.remotesTable.setDragDropMode(QAbstractItemView.InternalMove)
        self.remotesTable.setDefaultDropAction(Qt.MoveAction)
        self.remotesTable.setAlternatingRowColors(True)
        self.remotesTable.setSelectionMode(QAbstractItemView.SingleSelection)
        self.remotesTable.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.remotesTable.horizontalHeader().setStretchLastSection(True)
        self.remotesTable.verticalHeader().setVisible(False)
        self.remotesTable.verticalHeader().setStretchLastSection(False)

        self.horizontalLayout_3.addWidget(self.remotesTable)

        self.remotesTableButtons = QDialogButtonBox(self.remotesTab)
        self.remotesTableButtons.setObjectName(u"remotesTableButtons")
        self.remotesTableButtons.setOrientation(Qt.Vertical)
        self.remotesTableButtons.setStandardButtons(QDialogButtonBox.Close|QDialogButtonBox.Open)

        self.horizontalLayout_3.addWidget(self.remotesTableButtons)


        self.verticalLayout_10.addLayout(self.horizontalLayout_3)

        self.localCacheInfo.addTab(self.remotesTab, "")
        self.hooksTab = QWidget()
        self.hooksTab.setObjectName(u"hooksTab")
        self.verticalLayout_11 = QVBoxLayout(self.hooksTab)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.hooksLayout = QVBoxLayout()
        self.hooksLayout.setSpacing(0)
        self.hooksLayout.setObjectName(u"hooksLayout")
        self.hooksTable = QTableWidget(self.hooksTab)
        if (self.hooksTable.columnCount() < 2):
            self.hooksTable.setColumnCount(2)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.hooksTable.setHorizontalHeaderItem(0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.hooksTable.setHorizontalHeaderItem(1, __qtablewidgetitem6)
        self.hooksTable.setObjectName(u"hooksTable")
        self.hooksTable.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.hooksTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.hooksTable.setAlternatingRowColors(True)
        self.hooksTable.setSelectionMode(QAbstractItemView.SingleSelection)
        self.hooksTable.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.hooksTable.horizontalHeader().setStretchLastSection(True)
        self.hooksTable.verticalHeader().setVisible(False)
        self.hooksTable.verticalHeader().setStretchLastSection(False)

        self.hooksLayout.addWidget(self.hooksTable)


        self.verticalLayout_11.addLayout(self.hooksLayout)

        self.localCacheInfo.addTab(self.hooksTab, "")
        self.environmentTab = QWidget()
        self.environmentTab.setObjectName(u"environmentTab")
        self.verticalLayout_12 = QVBoxLayout(self.environmentTab)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.groupBox_3 = QGroupBox(self.environmentTab)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.horizontalLayout_4 = QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.envTable = KeyValueTable(self.groupBox_3)
        if (self.envTable.columnCount() < 2):
            self.envTable.setColumnCount(2)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.envTable.setHorizontalHeaderItem(0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.envTable.setHorizontalHeaderItem(1, __qtablewidgetitem8)
        self.envTable.setObjectName(u"envTable")
        self.envTable.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.envTable.setEditTriggers(QAbstractItemView.DoubleClicked)
        self.envTable.setAlternatingRowColors(True)
        self.envTable.setSelectionMode(QAbstractItemView.SingleSelection)
        self.envTable.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.envTable.horizontalHeader().setStretchLastSection(True)
        self.envTable.verticalHeader().setVisible(False)

        self.horizontalLayout_4.addWidget(self.envTable)

        self.envTableButtons = QDialogButtonBox(self.groupBox_3)
        self.envTableButtons.setObjectName(u"envTableButtons")
        self.envTableButtons.setOrientation(Qt.Vertical)
        self.envTableButtons.setStandardButtons(QDialogButtonBox.Close|QDialogButtonBox.Open)

        self.horizontalLayout_4.addWidget(self.envTableButtons)


        self.verticalLayout_12.addWidget(self.groupBox_3)

        self.groupBox_4 = QGroupBox(self.environmentTab)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.horizontalLayout_6 = QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.envRemoveList = QListWidget(self.groupBox_4)
        self.envRemoveList.setObjectName(u"envRemoveList")
        self.envRemoveList.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.envRemoveList.setEditTriggers(QAbstractItemView.DoubleClicked)
        self.envRemoveList.setAlternatingRowColors(True)
        self.envRemoveList.setSelectionMode(QAbstractItemView.SingleSelection)
        self.envRemoveList.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.horizontalLayout_6.addWidget(self.envRemoveList)

        self.envRemoveButtons = QDialogButtonBox(self.groupBox_4)
        self.envRemoveButtons.setObjectName(u"envRemoveButtons")
        self.envRemoveButtons.setOrientation(Qt.Vertical)
        self.envRemoveButtons.setStandardButtons(QDialogButtonBox.Close|QDialogButtonBox.Open)

        self.horizontalLayout_6.addWidget(self.envRemoveButtons)


        self.verticalLayout_12.addWidget(self.groupBox_4)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer)

        self.localCacheInfo.addTab(self.environmentTab, "")

        self.verticalLayout_5.addWidget(self.localCacheInfo)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_3)

        self.operationsBox = QGroupBox(ManageLocalCaches)
        self.operationsBox.setObjectName(u"operationsBox")
        self.operationsBox.setFlat(False)
        self.verticalLayout_2 = QVBoxLayout(self.operationsBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.operations_installConfigButton = QPushButton(self.operationsBox)
        self.operations_installConfigButton.setObjectName(u"operations_installConfigButton")

        self.horizontalLayout_2.addWidget(self.operations_installConfigButton)

        self.operations_removeLocksButton = QPushButton(self.operationsBox)
        self.operations_removeLocksButton.setObjectName(u"operations_removeLocksButton")

        self.horizontalLayout_2.addWidget(self.operations_removeLocksButton)

        self.operations_removeAllPackagesButton = QPushButton(self.operationsBox)
        self.operations_removeAllPackagesButton.setObjectName(u"operations_removeAllPackagesButton")

        self.horizontalLayout_2.addWidget(self.operations_removeAllPackagesButton)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)

        self.moveCacheButton = QPushButton(self.operationsBox)
        self.moveCacheButton.setObjectName(u"moveCacheButton")

        self.horizontalLayout.addWidget(self.moveCacheButton)

        self.deleteCacheButton = QPushButton(self.operationsBox)
        self.deleteCacheButton.setObjectName(u"deleteCacheButton")

        self.horizontalLayout.addWidget(self.deleteCacheButton)

        self.runConanCommandButton = QPushButton(self.operationsBox)
        self.runConanCommandButton.setObjectName(u"runConanCommandButton")

        self.horizontalLayout.addWidget(self.runConanCommandButton)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_5)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.verticalLayout_5.addWidget(self.operationsBox)

        self.localCacheLog = QPlainTextEdit(ManageLocalCaches)
        self.localCacheLog.setObjectName(u"localCacheLog")
        self.localCacheLog.setContextMenuPolicy(Qt.CustomContextMenu)
        self.localCacheLog.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.localCacheLog.setUndoRedoEnabled(False)
        self.localCacheLog.setReadOnly(True)

        self.verticalLayout_5.addWidget(self.localCacheLog)

        self.buttonBox = QDialogButtonBox(ManageLocalCaches)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Apply|QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout_5.addWidget(self.buttonBox)


        self.verticalLayout.addLayout(self.verticalLayout_5)


        self.retranslateUi(ManageLocalCaches)
        self.buttonBox.accepted.connect(ManageLocalCaches.accept)
        self.buttonBox.rejected.connect(ManageLocalCaches.reject)

        self.localCacheInfo.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(ManageLocalCaches)
    # setupUi

    def retranslateUi(self, ManageLocalCaches):
        ManageLocalCaches.setWindowTitle(QCoreApplication.translate("ManageLocalCaches", u"Manage Local Caches", None))
#if QT_CONFIG(tooltip)
        self.local_cache_names.setToolTip(QCoreApplication.translate("ManageLocalCaches", u"List of all local caches cruiz is aware of", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.new_local_cache_button.setToolTip(QCoreApplication.translate("ManageLocalCaches", u"Create a new local cache", None))
#endif // QT_CONFIG(tooltip)
        self.new_local_cache_button.setText(QCoreApplication.translate("ManageLocalCaches", u"New...", None))
        self.loc_conan_user_home_short_label.setText(QCoreApplication.translate("ManageLocalCaches", u"CONAN_USER_HOME_SHORT", None))
        self.label_5.setText(QCoreApplication.translate("ManageLocalCaches", u"CONAN_USER_HOME", None))
#if QT_CONFIG(tooltip)
        self.localCacheRecipeCount.setToolTip(QCoreApplication.translate("ManageLocalCaches", u"Number of recipes in cruiz associated with this cache.  A cache can only be deleted when there are no recipe associations.", None))
#endif // QT_CONFIG(tooltip)
        self.localCacheRecipeCount.setText(QCoreApplication.translate("ManageLocalCaches", u"TextLabel", None))
        self.localCacheInfo.setTabText(self.localCacheInfo.indexOf(self.locationsTab), QCoreApplication.translate("ManageLocalCaches", u"Locations", None))
#if QT_CONFIG(tooltip)
        self.localCacheInfo.setTabToolTip(self.localCacheInfo.indexOf(self.locationsTab), QCoreApplication.translate("ManageLocalCaches", u"Locations of relevance to the local cache", None))
#endif // QT_CONFIG(tooltip)
        self.groupBox_2.setTitle(QCoreApplication.translate("ManageLocalCaches", u"Available profiles", None))
        self.groupBox.setTitle(QCoreApplication.translate("ManageLocalCaches", u"Extra profile directories", None))
        ___qtablewidgetitem = self.profilesTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("ManageLocalCaches", u"Name", None));
        ___qtablewidgetitem1 = self.profilesTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("ManageLocalCaches", u"Directory", None));
        self.localCacheInfo.setTabText(self.localCacheInfo.indexOf(self.profilesTab), QCoreApplication.translate("ManageLocalCaches", u"Profiles", None))
#if QT_CONFIG(tooltip)
        self.localCacheInfo.setTabToolTip(self.localCacheInfo.indexOf(self.profilesTab), QCoreApplication.translate("ManageLocalCaches", u"Extra directories to search for profiles (other than in the cache itself), and filenames of profiles that are visible to the cache.", None))
#endif // QT_CONFIG(tooltip)
        self.configPrintRunCommands.setText(QCoreApplication.translate("ManageLocalCaches", u"Print run commands", None))
        self.configRevisions.setText(QCoreApplication.translate("ManageLocalCaches", u"Revisions", None))
        self.localCacheInfo.setTabText(self.localCacheInfo.indexOf(self.configTab), QCoreApplication.translate("ManageLocalCaches", u"Config", None))
#if QT_CONFIG(tooltip)
        self.localCacheInfo.setTabToolTip(self.localCacheInfo.indexOf(self.configTab), QCoreApplication.translate("ManageLocalCaches", u"Current cache configuration state", None))
#endif // QT_CONFIG(tooltip)
        ___qtablewidgetitem2 = self.remotesTable.horizontalHeaderItem(0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("ManageLocalCaches", u"Enabled", None));
        ___qtablewidgetitem3 = self.remotesTable.horizontalHeaderItem(1)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("ManageLocalCaches", u"Name", None));
        ___qtablewidgetitem4 = self.remotesTable.horizontalHeaderItem(2)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("ManageLocalCaches", u"Url", None));
        self.localCacheInfo.setTabText(self.localCacheInfo.indexOf(self.remotesTab), QCoreApplication.translate("ManageLocalCaches", u"Remotes", None))
#if QT_CONFIG(tooltip)
        self.localCacheInfo.setTabToolTip(self.localCacheInfo.indexOf(self.remotesTab), QCoreApplication.translate("ManageLocalCaches", u"Remotes used to search for package installs by this cache", None))
#endif // QT_CONFIG(tooltip)
        ___qtablewidgetitem5 = self.hooksTable.horizontalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("ManageLocalCaches", u"Enabled", None));
        ___qtablewidgetitem6 = self.hooksTable.horizontalHeaderItem(1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("ManageLocalCaches", u"Path", None));
        self.localCacheInfo.setTabText(self.localCacheInfo.indexOf(self.hooksTab), QCoreApplication.translate("ManageLocalCaches", u"Hooks", None))
#if QT_CONFIG(tooltip)
        self.localCacheInfo.setTabToolTip(self.localCacheInfo.indexOf(self.hooksTab), QCoreApplication.translate("ManageLocalCaches", u"Hooks and their status used by commands in this cache", None))
#endif // QT_CONFIG(tooltip)
        self.groupBox_3.setTitle(QCoreApplication.translate("ManageLocalCaches", u"Additions", None))
        ___qtablewidgetitem7 = self.envTable.horizontalHeaderItem(0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("ManageLocalCaches", u"Name", None));
        ___qtablewidgetitem8 = self.envTable.horizontalHeaderItem(1)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("ManageLocalCaches", u"Value", None));
        self.groupBox_4.setTitle(QCoreApplication.translate("ManageLocalCaches", u"Removals", None))
        self.localCacheInfo.setTabText(self.localCacheInfo.indexOf(self.environmentTab), QCoreApplication.translate("ManageLocalCaches", u"Environment", None))
#if QT_CONFIG(tooltip)
        self.localCacheInfo.setTabToolTip(self.localCacheInfo.indexOf(self.environmentTab), QCoreApplication.translate("ManageLocalCaches", u"Environment variables applied to conan commands in this cache", None))
#endif // QT_CONFIG(tooltip)
        self.operationsBox.setTitle(QCoreApplication.translate("ManageLocalCaches", u"Operations", None))
#if QT_CONFIG(tooltip)
        self.operations_installConfigButton.setToolTip(QCoreApplication.translate("ManageLocalCaches", u"Install an external configuration onto the local cache", None))
#endif // QT_CONFIG(tooltip)
        self.operations_installConfigButton.setText(QCoreApplication.translate("ManageLocalCaches", u"Install configuration...", None))
#if QT_CONFIG(tooltip)
        self.operations_removeLocksButton.setToolTip(QCoreApplication.translate("ManageLocalCaches", u"Remove all locks from within the local cache which may otherwise block some commands", None))
#endif // QT_CONFIG(tooltip)
        self.operations_removeLocksButton.setText(QCoreApplication.translate("ManageLocalCaches", u"Remove locks", None))
#if QT_CONFIG(tooltip)
        self.operations_removeAllPackagesButton.setToolTip(QCoreApplication.translate("ManageLocalCaches", u"Remove all installed packages from the local cache", None))
#endif // QT_CONFIG(tooltip)
        self.operations_removeAllPackagesButton.setText(QCoreApplication.translate("ManageLocalCaches", u"Remove all packages", None))
#if QT_CONFIG(tooltip)
        self.moveCacheButton.setToolTip(QCoreApplication.translate("ManageLocalCaches", u"Move the location of the local cache", None))
#endif // QT_CONFIG(tooltip)
        self.moveCacheButton.setText(QCoreApplication.translate("ManageLocalCaches", u"Move...", None))
#if QT_CONFIG(tooltip)
        self.deleteCacheButton.setToolTip(QCoreApplication.translate("ManageLocalCaches", u"Delete the local cache, from disk and from cruiz", None))
#endif // QT_CONFIG(tooltip)
        self.deleteCacheButton.setText(QCoreApplication.translate("ManageLocalCaches", u"Delete...", None))
        self.runConanCommandButton.setText(QCoreApplication.translate("ManageLocalCaches", u"Run Conan command...", None))
    # retranslateUi

