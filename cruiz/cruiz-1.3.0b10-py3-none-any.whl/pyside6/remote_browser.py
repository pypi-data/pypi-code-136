# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'remote_browser.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QCheckBox,
    QComboBox, QDockWidget, QGridLayout, QGroupBox,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QListView, QPlainTextEdit, QProgressBar, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QTableView,
    QTreeView, QVBoxLayout, QWidget)

from cruiz.remote_browser.pages.packagebinarypage import PackageBinaryPage
from cruiz.remote_browser.pages.packageidpage import PackageIdPage
from cruiz.remote_browser.pages.packagereferencepage import PackageReferencePage
from cruiz.remote_browser.pages.packagerevisionpage import PackageRevisionPage
from cruiz.remote_browser.pages.reciperevisionpage import RecipeRevisionPage

class Ui_remotebrowser(object):
    def setupUi(self, remotebrowser):
        if not remotebrowser.objectName():
            remotebrowser.setObjectName(u"remotebrowser")
        remotebrowser.setEnabled(True)
        remotebrowser.resize(493, 682)
        remotebrowser.setFeatures(QDockWidget.DockWidgetClosable|QDockWidget.DockWidgetFloatable|QDockWidget.DockWidgetMovable)
        self.dockWidgetContents = QWidget()
        self.dockWidgetContents.setObjectName(u"dockWidgetContents")
        self.verticalLayout = QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.dockWidgetContents)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.pkgref = PackageReferencePage()
        self.pkgref.setObjectName(u"pkgref")
        self.verticalLayout_2 = QVBoxLayout(self.pkgref)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.pkgref_ui_group = QGroupBox(self.pkgref)
        self.pkgref_ui_group.setObjectName(u"pkgref_ui_group")
        self.gridLayout = QGridLayout(self.pkgref_ui_group)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.pkgref_ui_group)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.remote = QComboBox(self.pkgref_ui_group)
        self.remote.setObjectName(u"remote")

        self.gridLayout.addWidget(self.remote, 2, 1, 1, 1)

        self.local_cache_name = QComboBox(self.pkgref_ui_group)
        self.local_cache_name.setObjectName(u"local_cache_name")

        self.gridLayout.addWidget(self.local_cache_name, 0, 1, 1, 1)

        self.search_pattern = QLineEdit(self.pkgref_ui_group)
        self.search_pattern.setObjectName(u"search_pattern")

        self.gridLayout.addWidget(self.search_pattern, 4, 1, 1, 1)

        self.label_2 = QLabel(self.pkgref_ui_group)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)

        self.label_3 = QLabel(self.pkgref_ui_group)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 1)

        self.revisions = QCheckBox(self.pkgref_ui_group)
        self.revisions.setObjectName(u"revisions")
        self.revisions.setEnabled(False)

        self.gridLayout.addWidget(self.revisions, 1, 0, 1, 2)

        self.alias_aware = QCheckBox(self.pkgref_ui_group)
        self.alias_aware.setObjectName(u"alias_aware")

        self.gridLayout.addWidget(self.alias_aware, 3, 0, 1, 2)


        self.verticalLayout_2.addWidget(self.pkgref_ui_group)

        self.pkgref_groupbox = QGroupBox(self.pkgref)
        self.pkgref_groupbox.setObjectName(u"pkgref_groupbox")
        self.pkgref_groupbox.setEnabled(False)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pkgref_groupbox.sizePolicy().hasHeightForWidth())
        self.pkgref_groupbox.setSizePolicy(sizePolicy)
        self.verticalLayout_7 = QVBoxLayout(self.pkgref_groupbox)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.package_references = QListView(self.pkgref_groupbox)
        self.package_references.setObjectName(u"package_references")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.package_references.sizePolicy().hasHeightForWidth())
        self.package_references.setSizePolicy(sizePolicy1)
        self.package_references.setContextMenuPolicy(Qt.CustomContextMenu)
        self.package_references.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.package_references.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.package_references.setAlternatingRowColors(True)

        self.verticalLayout_7.addWidget(self.package_references)


        self.verticalLayout_2.addWidget(self.pkgref_groupbox)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.pkgref_progress = QProgressBar(self.pkgref)
        self.pkgref_progress.setObjectName(u"pkgref_progress")
        self.pkgref_progress.setMaximum(1)
        self.pkgref_progress.setValue(-1)

        self.horizontalLayout_5.addWidget(self.pkgref_progress)

        self.pkgref_cancel = QPushButton(self.pkgref)
        self.pkgref_cancel.setObjectName(u"pkgref_cancel")
        self.pkgref_cancel.setEnabled(False)
        icon = QIcon()
        icon.addFile(u":/cancel.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pkgref_cancel.setIcon(icon)

        self.horizontalLayout_5.addWidget(self.pkgref_cancel)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.stackedWidget.addWidget(self.pkgref)
        self.rrev = RecipeRevisionPage()
        self.rrev.setObjectName(u"rrev")
        self.verticalLayout_3 = QVBoxLayout(self.rrev)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.rrev_pkgref = QLabel(self.rrev)
        self.rrev_pkgref.setObjectName(u"rrev_pkgref")
        self.rrev_pkgref.setContextMenuPolicy(Qt.CustomContextMenu)

        self.verticalLayout_3.addWidget(self.rrev_pkgref)

        self.rrev_groupbox = QGroupBox(self.rrev)
        self.rrev_groupbox.setObjectName(u"rrev_groupbox")
        self.rrev_groupbox.setEnabled(False)
        self.verticalLayout_8 = QVBoxLayout(self.rrev_groupbox)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.recipe_revisions = QTableView(self.rrev_groupbox)
        self.recipe_revisions.setObjectName(u"recipe_revisions")
        self.recipe_revisions.setContextMenuPolicy(Qt.CustomContextMenu)
        self.recipe_revisions.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.recipe_revisions.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.recipe_revisions.setAlternatingRowColors(True)
        self.recipe_revisions.setSelectionMode(QAbstractItemView.SingleSelection)
        self.recipe_revisions.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.recipe_revisions.horizontalHeader().setStretchLastSection(False)
        self.recipe_revisions.verticalHeader().setVisible(False)

        self.verticalLayout_8.addWidget(self.recipe_revisions)


        self.verticalLayout_3.addWidget(self.rrev_groupbox)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.rrev_progress = QProgressBar(self.rrev)
        self.rrev_progress.setObjectName(u"rrev_progress")
        self.rrev_progress.setMaximum(1)
        self.rrev_progress.setValue(-1)

        self.horizontalLayout_6.addWidget(self.rrev_progress)

        self.rrev_cancel = QPushButton(self.rrev)
        self.rrev_cancel.setObjectName(u"rrev_cancel")
        self.rrev_cancel.setEnabled(False)
        self.rrev_cancel.setIcon(icon)

        self.horizontalLayout_6.addWidget(self.rrev_cancel)


        self.verticalLayout_3.addLayout(self.horizontalLayout_6)

        self.rrev_buttons = QWidget(self.rrev)
        self.rrev_buttons.setObjectName(u"rrev_buttons")
        self.horizontalLayout = QHBoxLayout(self.rrev_buttons)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.rrev_back = QPushButton(self.rrev_buttons)
        self.rrev_back.setObjectName(u"rrev_back")

        self.horizontalLayout.addWidget(self.rrev_back)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_5)

        self.rrev_refresh = QPushButton(self.rrev_buttons)
        self.rrev_refresh.setObjectName(u"rrev_refresh")

        self.horizontalLayout.addWidget(self.rrev_refresh)


        self.verticalLayout_3.addWidget(self.rrev_buttons)

        self.stackedWidget.addWidget(self.rrev)
        self.package_id = PackageIdPage()
        self.package_id.setObjectName(u"package_id")
        self.verticalLayout_4 = QVBoxLayout(self.package_id)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.pid_pkgref = QLabel(self.package_id)
        self.pid_pkgref.setObjectName(u"pid_pkgref")
        self.pid_pkgref.setContextMenuPolicy(Qt.CustomContextMenu)

        self.verticalLayout_4.addWidget(self.pid_pkgref)

        self.pid_groupbox = QGroupBox(self.package_id)
        self.pid_groupbox.setObjectName(u"pid_groupbox")
        self.pid_groupbox.setEnabled(False)
        self.verticalLayout_9 = QVBoxLayout(self.pid_groupbox)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.package_ids = QTableView(self.pid_groupbox)
        self.package_ids.setObjectName(u"package_ids")
        self.package_ids.setContextMenuPolicy(Qt.CustomContextMenu)
        self.package_ids.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.package_ids.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.package_ids.setAlternatingRowColors(True)
        self.package_ids.setSelectionMode(QAbstractItemView.SingleSelection)
        self.package_ids.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.package_ids.setSortingEnabled(True)
        self.package_ids.horizontalHeader().setStretchLastSection(False)
        self.package_ids.verticalHeader().setVisible(False)

        self.verticalLayout_9.addWidget(self.package_ids)


        self.verticalLayout_4.addWidget(self.pid_groupbox)

        self.pid_filter_group = QGroupBox(self.package_id)
        self.pid_filter_group.setObjectName(u"pid_filter_group")
        self.pid_filter_group.setEnabled(False)
        self.verticalLayout_12 = QVBoxLayout(self.pid_filter_group)
        self.verticalLayout_12.setSpacing(6)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.pid_filterTable = QTableView(self.pid_filter_group)
        self.pid_filterTable.setObjectName(u"pid_filterTable")
        self.pid_filterTable.setContextMenuPolicy(Qt.CustomContextMenu)
        self.pid_filterTable.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.pid_filterTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.pid_filterTable.setAlternatingRowColors(True)
        self.pid_filterTable.setSelectionMode(QAbstractItemView.SingleSelection)
        self.pid_filterTable.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.pid_filterTable.horizontalHeader().setStretchLastSection(False)
        self.pid_filterTable.verticalHeader().setVisible(False)

        self.verticalLayout_12.addWidget(self.pid_filterTable)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.pid_filter_key = QComboBox(self.pid_filter_group)
        self.pid_filter_key.setObjectName(u"pid_filter_key")

        self.horizontalLayout_7.addWidget(self.pid_filter_key)

        self.pid_filter_value = QComboBox(self.pid_filter_group)
        self.pid_filter_value.setObjectName(u"pid_filter_value")

        self.horizontalLayout_7.addWidget(self.pid_filter_value)

        self.pid_add_filter = QPushButton(self.pid_filter_group)
        self.pid_add_filter.setObjectName(u"pid_add_filter")

        self.horizontalLayout_7.addWidget(self.pid_add_filter)


        self.verticalLayout_12.addLayout(self.horizontalLayout_7)


        self.verticalLayout_4.addWidget(self.pid_filter_group)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.pid_progress = QProgressBar(self.package_id)
        self.pid_progress.setObjectName(u"pid_progress")
        self.pid_progress.setMaximum(1)
        self.pid_progress.setValue(-1)

        self.horizontalLayout_8.addWidget(self.pid_progress)

        self.pid_cancel = QPushButton(self.package_id)
        self.pid_cancel.setObjectName(u"pid_cancel")
        self.pid_cancel.setEnabled(False)
        self.pid_cancel.setIcon(icon)

        self.horizontalLayout_8.addWidget(self.pid_cancel)


        self.verticalLayout_4.addLayout(self.horizontalLayout_8)

        self.pid_buttons = QWidget(self.package_id)
        self.pid_buttons.setObjectName(u"pid_buttons")
        self.horizontalLayout_2 = QHBoxLayout(self.pid_buttons)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pid_back = QPushButton(self.pid_buttons)
        self.pid_back.setObjectName(u"pid_back")

        self.horizontalLayout_2.addWidget(self.pid_back)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.pid_refresh = QPushButton(self.pid_buttons)
        self.pid_refresh.setObjectName(u"pid_refresh")

        self.horizontalLayout_2.addWidget(self.pid_refresh)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_6)

        self.pid_restart = QPushButton(self.pid_buttons)
        self.pid_restart.setObjectName(u"pid_restart")

        self.horizontalLayout_2.addWidget(self.pid_restart)


        self.verticalLayout_4.addWidget(self.pid_buttons)

        self.stackedWidget.addWidget(self.package_id)
        self.prev = PackageRevisionPage()
        self.prev.setObjectName(u"prev")
        self.verticalLayout_5 = QVBoxLayout(self.prev)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.prev_pkgref = QLabel(self.prev)
        self.prev_pkgref.setObjectName(u"prev_pkgref")
        self.prev_pkgref.setContextMenuPolicy(Qt.CustomContextMenu)

        self.verticalLayout_5.addWidget(self.prev_pkgref)

        self.prev_groupbox = QGroupBox(self.prev)
        self.prev_groupbox.setObjectName(u"prev_groupbox")
        self.prev_groupbox.setEnabled(False)
        self.verticalLayout_10 = QVBoxLayout(self.prev_groupbox)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.package_revisions = QTableView(self.prev_groupbox)
        self.package_revisions.setObjectName(u"package_revisions")
        self.package_revisions.setContextMenuPolicy(Qt.CustomContextMenu)
        self.package_revisions.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.package_revisions.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.package_revisions.setAlternatingRowColors(True)
        self.package_revisions.setSelectionMode(QAbstractItemView.SingleSelection)
        self.package_revisions.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.package_revisions.horizontalHeader().setStretchLastSection(False)
        self.package_revisions.verticalHeader().setVisible(False)

        self.verticalLayout_10.addWidget(self.package_revisions)


        self.verticalLayout_5.addWidget(self.prev_groupbox)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.prev_progress = QProgressBar(self.prev)
        self.prev_progress.setObjectName(u"prev_progress")
        self.prev_progress.setMaximum(1)
        self.prev_progress.setValue(-1)

        self.horizontalLayout_9.addWidget(self.prev_progress)

        self.prev_cancel = QPushButton(self.prev)
        self.prev_cancel.setObjectName(u"prev_cancel")
        self.prev_cancel.setEnabled(False)
        self.prev_cancel.setIcon(icon)

        self.horizontalLayout_9.addWidget(self.prev_cancel)


        self.verticalLayout_5.addLayout(self.horizontalLayout_9)

        self.prev_buttons = QWidget(self.prev)
        self.prev_buttons.setObjectName(u"prev_buttons")
        self.horizontalLayout_3 = QHBoxLayout(self.prev_buttons)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.prev_back = QPushButton(self.prev_buttons)
        self.prev_back.setObjectName(u"prev_back")

        self.horizontalLayout_3.addWidget(self.prev_back)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.prev_refresh = QPushButton(self.prev_buttons)
        self.prev_refresh.setObjectName(u"prev_refresh")

        self.horizontalLayout_3.addWidget(self.prev_refresh)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_7)

        self.prev_restart = QPushButton(self.prev_buttons)
        self.prev_restart.setObjectName(u"prev_restart")

        self.horizontalLayout_3.addWidget(self.prev_restart)


        self.verticalLayout_5.addWidget(self.prev_buttons)

        self.stackedWidget.addWidget(self.prev)
        self.pbinary = PackageBinaryPage()
        self.pbinary.setObjectName(u"pbinary")
        self.verticalLayout_6 = QVBoxLayout(self.pbinary)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.pbinary_pkgref = QLabel(self.pbinary)
        self.pbinary_pkgref.setObjectName(u"pbinary_pkgref")
        self.pbinary_pkgref.setContextMenuPolicy(Qt.CustomContextMenu)

        self.verticalLayout_6.addWidget(self.pbinary_pkgref)

        self.pbinary_groupbox = QGroupBox(self.pbinary)
        self.pbinary_groupbox.setObjectName(u"pbinary_groupbox")
        self.pbinary_groupbox.setEnabled(False)
        self.verticalLayout_11 = QVBoxLayout(self.pbinary_groupbox)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.package_binary = QTreeView(self.pbinary_groupbox)
        self.package_binary.setObjectName(u"package_binary")
        self.package_binary.setContextMenuPolicy(Qt.CustomContextMenu)
        self.package_binary.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.package_binary.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.package_binary.setAlternatingRowColors(True)

        self.verticalLayout_11.addWidget(self.package_binary)


        self.verticalLayout_6.addWidget(self.pbinary_groupbox)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.pbinary_progress = QProgressBar(self.pbinary)
        self.pbinary_progress.setObjectName(u"pbinary_progress")
        self.pbinary_progress.setMaximum(1)
        self.pbinary_progress.setValue(-1)

        self.horizontalLayout_10.addWidget(self.pbinary_progress)

        self.pbinary_cancel = QPushButton(self.pbinary)
        self.pbinary_cancel.setObjectName(u"pbinary_cancel")
        self.pbinary_cancel.setEnabled(False)
        self.pbinary_cancel.setIcon(icon)

        self.horizontalLayout_10.addWidget(self.pbinary_cancel)


        self.verticalLayout_6.addLayout(self.horizontalLayout_10)

        self.pbinary_buttons = QWidget(self.pbinary)
        self.pbinary_buttons.setObjectName(u"pbinary_buttons")
        self.horizontalLayout_4 = QHBoxLayout(self.pbinary_buttons)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.pbinary_back = QPushButton(self.pbinary_buttons)
        self.pbinary_back.setObjectName(u"pbinary_back")

        self.horizontalLayout_4.addWidget(self.pbinary_back)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)

        self.pbinary_restart = QPushButton(self.pbinary_buttons)
        self.pbinary_restart.setObjectName(u"pbinary_restart")

        self.horizontalLayout_4.addWidget(self.pbinary_restart)


        self.verticalLayout_6.addWidget(self.pbinary_buttons)

        self.stackedWidget.addWidget(self.pbinary)

        self.verticalLayout.addWidget(self.stackedWidget)

        self.log = QPlainTextEdit(self.dockWidgetContents)
        self.log.setObjectName(u"log")
        self.log.setContextMenuPolicy(Qt.CustomContextMenu)
        self.log.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.log.setReadOnly(True)

        self.verticalLayout.addWidget(self.log)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        remotebrowser.setWidget(self.dockWidgetContents)

        self.retranslateUi(remotebrowser)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(remotebrowser)
    # setupUi

    def retranslateUi(self, remotebrowser):
        remotebrowser.setWindowTitle(QCoreApplication.translate("remotebrowser", u"Conan remote browser", None))
        self.pkgref_ui_group.setTitle(QCoreApplication.translate("remotebrowser", u"Query package reference", None))
        self.label.setText(QCoreApplication.translate("remotebrowser", u"Local cache name", None))
        self.label_2.setText(QCoreApplication.translate("remotebrowser", u"Remote", None))
        self.label_3.setText(QCoreApplication.translate("remotebrowser", u"Search pattern", None))
        self.revisions.setText(QCoreApplication.translate("remotebrowser", u"Revisions enabled", None))
#if QT_CONFIG(tooltip)
        self.alias_aware.setToolTip(QCoreApplication.translate("remotebrowser", u"Check this option to perform additional processing to identify alias packages", None))
#endif // QT_CONFIG(tooltip)
        self.alias_aware.setText(QCoreApplication.translate("remotebrowser", u"Alias aware", None))
        self.pkgref_groupbox.setTitle(QCoreApplication.translate("remotebrowser", u"0 package references found", None))
        self.pkgref_cancel.setText("")
        self.rrev_pkgref.setText(QCoreApplication.translate("remotebrowser", u"Package reference", None))
        self.rrev_groupbox.setTitle(QCoreApplication.translate("remotebrowser", u"0 recipe revisions found", None))
        self.rrev_cancel.setText("")
        self.rrev_back.setText(QCoreApplication.translate("remotebrowser", u"Back", None))
        self.rrev_refresh.setText(QCoreApplication.translate("remotebrowser", u"Refresh", None))
        self.pid_pkgref.setText(QCoreApplication.translate("remotebrowser", u"Package ref + revision", None))
        self.pid_groupbox.setTitle(QCoreApplication.translate("remotebrowser", u"0 package_ids found", None))
        self.pid_filter_group.setTitle(QCoreApplication.translate("remotebrowser", u"Filtering", None))
        self.pid_filter_key.setPlaceholderText(QCoreApplication.translate("remotebrowser", u"Select filter key", None))
        self.pid_filter_value.setPlaceholderText(QCoreApplication.translate("remotebrowser", u"Select filter value", None))
        self.pid_add_filter.setText(QCoreApplication.translate("remotebrowser", u"Add", None))
        self.pid_cancel.setText("")
        self.pid_back.setText(QCoreApplication.translate("remotebrowser", u"Back", None))
        self.pid_refresh.setText(QCoreApplication.translate("remotebrowser", u"Refresh", None))
        self.pid_restart.setText(QCoreApplication.translate("remotebrowser", u"Restart", None))
        self.prev_pkgref.setText(QCoreApplication.translate("remotebrowser", u"Pkg ref + rrev + package_id", None))
        self.prev_groupbox.setTitle(QCoreApplication.translate("remotebrowser", u"0 package revisions found", None))
        self.prev_cancel.setText("")
        self.prev_back.setText(QCoreApplication.translate("remotebrowser", u"Back", None))
        self.prev_refresh.setText(QCoreApplication.translate("remotebrowser", u"Refresh", None))
        self.prev_restart.setText(QCoreApplication.translate("remotebrowser", u"Restart", None))
        self.pbinary_pkgref.setText(QCoreApplication.translate("remotebrowser", u"Pkg ref + rrev + package_id + prev", None))
        self.pbinary_groupbox.setTitle(QCoreApplication.translate("remotebrowser", u"Package archive", None))
        self.pbinary_cancel.setText("")
        self.pbinary_back.setText(QCoreApplication.translate("remotebrowser", u"Back", None))
        self.pbinary_restart.setText(QCoreApplication.translate("remotebrowser", u"Restart", None))
    # retranslateUi

