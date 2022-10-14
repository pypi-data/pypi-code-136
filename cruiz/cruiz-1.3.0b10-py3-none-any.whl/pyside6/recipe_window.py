# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'recipe_window.ui'
##
## Created by: Qt User Interface Compiler version 6.2.4
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QComboBox,
    QDockWidget, QFrame, QGridLayout, QGroupBox,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QListView, QListWidgetItem, QMainWindow, QMenu,
    QMenuBar, QPlainTextEdit, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QSplitter, QStatusBar,
    QTabWidget, QTreeView, QVBoxLayout, QWidget)

from cruiz.recipe.dependencyview import DependencyView
from cruiz.recipe.logs.command import RecipeCommandHistoryWidget
from cruiz.recipe.toolbars.behaviour import RecipeBehaviourToolbar
from cruiz.recipe.toolbars.buildfeatures import BuildFeaturesToolbar
from cruiz.recipe.toolbars.command import RecipeCommandToolbar

class Ui_RecipeWindow(object):
    def setupUi(self, RecipeWindow):
        if not RecipeWindow.objectName():
            RecipeWindow.setObjectName(u"RecipeWindow")
        RecipeWindow.resize(800, 847)
        self.actionCreateCommand = QAction(RecipeWindow)
        self.actionCreateCommand.setObjectName(u"actionCreateCommand")
        icon = QIcon()
        icon.addFile(u":/create.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionCreateCommand.setIcon(icon)
        self.actionCreateUpdateCommand = QAction(RecipeWindow)
        self.actionCreateUpdateCommand.setObjectName(u"actionCreateUpdateCommand")
        self.actionCreateUpdateCommand.setIcon(icon)
        self.actionImportsCommand = QAction(RecipeWindow)
        self.actionImportsCommand.setObjectName(u"actionImportsCommand")
        icon1 = QIcon()
        icon1.addFile(u":/imports.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionImportsCommand.setIcon(icon1)
        self.actionInstallCommand = QAction(RecipeWindow)
        self.actionInstallCommand.setObjectName(u"actionInstallCommand")
        icon2 = QIcon()
        icon2.addFile(u":/install.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionInstallCommand.setIcon(icon2)
        self.actionInstallUpdateCommand = QAction(RecipeWindow)
        self.actionInstallUpdateCommand.setObjectName(u"actionInstallUpdateCommand")
        self.actionInstallUpdateCommand.setIcon(icon2)
        self.actionSourceCommand = QAction(RecipeWindow)
        self.actionSourceCommand.setObjectName(u"actionSourceCommand")
        icon3 = QIcon()
        icon3.addFile(u":/source.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionSourceCommand.setIcon(icon3)
        self.actionBuildCommand = QAction(RecipeWindow)
        self.actionBuildCommand.setObjectName(u"actionBuildCommand")
        icon4 = QIcon()
        icon4.addFile(u":/build.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionBuildCommand.setIcon(icon4)
        self.actionPackageCommand = QAction(RecipeWindow)
        self.actionPackageCommand.setObjectName(u"actionPackageCommand")
        icon5 = QIcon()
        icon5.addFile(u":/package.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionPackageCommand.setIcon(icon5)
        self.actionExportPackageCommand = QAction(RecipeWindow)
        self.actionExportPackageCommand.setObjectName(u"actionExportPackageCommand")
        icon6 = QIcon()
        icon6.addFile(u":/exportpackage.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionExportPackageCommand.setIcon(icon6)
        self.actionTestCommand = QAction(RecipeWindow)
        self.actionTestCommand.setObjectName(u"actionTestCommand")
        icon7 = QIcon()
        icon7.addFile(u":/testpackage.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionTestCommand.setIcon(icon7)
        self.actionCancelCommand = QAction(RecipeWindow)
        self.actionCancelCommand.setObjectName(u"actionCancelCommand")
        icon8 = QIcon()
        icon8.addFile(u":/cancel.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionCancelCommand.setIcon(icon8)
        self.actionRemovePackageCommand = QAction(RecipeWindow)
        self.actionRemovePackageCommand.setObjectName(u"actionRemovePackageCommand")
        icon9 = QIcon()
        icon9.addFile(u":/removepackage.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionRemovePackageCommand.setIcon(icon9)
        self.actionCMakeBuildToolCommand = QAction(RecipeWindow)
        self.actionCMakeBuildToolCommand.setObjectName(u"actionCMakeBuildToolCommand")
        icon10 = QIcon()
        icon10.addFile(u":/cmakebuildtool.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionCMakeBuildToolCommand.setIcon(icon10)
        self.actionCMakeBuildToolVerboseCommand = QAction(RecipeWindow)
        self.actionCMakeBuildToolVerboseCommand.setObjectName(u"actionCMakeBuildToolVerboseCommand")
        icon11 = QIcon()
        icon11.addFile(u":/cmakebuildtoolverbose.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionCMakeBuildToolVerboseCommand.setIcon(icon11)
        self.actionCMakeRemoveCacheCommand = QAction(RecipeWindow)
        self.actionCMakeRemoveCacheCommand.setObjectName(u"actionCMakeRemoveCacheCommand")
        icon12 = QIcon()
        icon12.addFile(u":/removecmakecache.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionCMakeRemoveCacheCommand.setIcon(icon12)
        self.actionOpen_another_version = QAction(RecipeWindow)
        self.actionOpen_another_version.setObjectName(u"actionOpen_another_version")
        self.actionManage_associated_local_cache = QAction(RecipeWindow)
        self.actionManage_associated_local_cache.setObjectName(u"actionManage_associated_local_cache")
        self.actionClose = QAction(RecipeWindow)
        self.actionClose.setObjectName(u"actionClose")
        self.actionOpen_recipe_in_editor = QAction(RecipeWindow)
        self.actionOpen_recipe_in_editor.setObjectName(u"actionOpen_recipe_in_editor")
        self.actionOpen_recipe_folder = QAction(RecipeWindow)
        self.actionOpen_recipe_folder.setObjectName(u"actionOpen_recipe_folder")
        self.actionCopy_recipe_folder_to_clipboard = QAction(RecipeWindow)
        self.actionCopy_recipe_folder_to_clipboard.setObjectName(u"actionCopy_recipe_folder_to_clipboard")
        self.actionReload = QAction(RecipeWindow)
        self.actionReload.setObjectName(u"actionReload")
        self.centralwidget = QWidget(RecipeWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pane_tabs = QTabWidget(self.centralwidget)
        self.pane_tabs.setObjectName(u"pane_tabs")
        self.pane_tabs.setUsesScrollButtons(True)
        self.pane_tabs.setDocumentMode(True)
        self.pane_tabs.setTabsClosable(True)
        self.pane_tabs.setMovable(True)
        self.pane_tabs.setTabBarAutoHide(True)
        self.default_panes_tab = QWidget()
        self.default_panes_tab.setObjectName(u"default_panes_tab")
        self.verticalLayout_18 = QVBoxLayout(self.default_panes_tab)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.paneSplitter = QSplitter(self.default_panes_tab)
        self.paneSplitter.setObjectName(u"paneSplitter")
        self.paneSplitter.setLineWidth(0)
        self.paneSplitter.setOrientation(Qt.Vertical)
        self.paneSplitter.setHandleWidth(0)
        self.paneSplitter.setChildrenCollapsible(False)
        self.outputPane = QPlainTextEdit(self.paneSplitter)
        self.outputPane.setObjectName(u"outputPane")
        self.outputPane.setContextMenuPolicy(Qt.CustomContextMenu)
        self.outputPane.setUndoRedoEnabled(False)
        self.outputPane.setReadOnly(True)
        self.paneSplitter.addWidget(self.outputPane)
        self.errorPane = QPlainTextEdit(self.paneSplitter)
        self.errorPane.setObjectName(u"errorPane")
        self.errorPane.setContextMenuPolicy(Qt.CustomContextMenu)
        self.errorPane.setUndoRedoEnabled(False)
        self.errorPane.setReadOnly(True)
        self.paneSplitter.addWidget(self.errorPane)

        self.verticalLayout_18.addWidget(self.paneSplitter)

        self.pane_tabs.addTab(self.default_panes_tab, "")

        self.verticalLayout.addWidget(self.pane_tabs)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        RecipeWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(RecipeWindow)
        self.statusbar.setObjectName(u"statusbar")
        RecipeWindow.setStatusBar(self.statusbar)
        self.behaviourToolbar = RecipeBehaviourToolbar(RecipeWindow)
        self.behaviourToolbar.setObjectName(u"behaviourToolbar")
        RecipeWindow.addToolBar(Qt.TopToolBarArea, self.behaviourToolbar)
        self.commandToolbar = RecipeCommandToolbar(RecipeWindow)
        self.commandToolbar.setObjectName(u"commandToolbar")
        RecipeWindow.addToolBar(Qt.TopToolBarArea, self.commandToolbar)
        self.buildFeaturesToolbar = BuildFeaturesToolbar(RecipeWindow)
        self.buildFeaturesToolbar.setObjectName(u"buildFeaturesToolbar")
        RecipeWindow.addToolBar(Qt.TopToolBarArea, self.buildFeaturesToolbar)
        RecipeWindow.insertToolBarBreak(self.buildFeaturesToolbar)
        self.menuBar = QMenuBar(RecipeWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 800, 24))
        self.menuRecipe = QMenu(self.menuBar)
        self.menuRecipe.setObjectName(u"menuRecipe")
        self.menuRecipe.setToolTipsVisible(True)
        self.menuCommands = QMenu(self.menuBar)
        self.menuCommands.setObjectName(u"menuCommands")
        self.menuCommands.setToolTipsVisible(True)
        self.menuLocal_workflow = QMenu(self.menuCommands)
        self.menuLocal_workflow.setObjectName(u"menuLocal_workflow")
        self.menuLocal_workflow.setToolTipsVisible(True)
        self.menuCMake = QMenu(self.menuLocal_workflow)
        self.menuCMake.setObjectName(u"menuCMake")
        RecipeWindow.setMenuBar(self.menuBar)
        self.conanLogDock = QDockWidget(RecipeWindow)
        self.conanLogDock.setObjectName(u"conanLogDock")
        self.conanLogDock.setEnabled(True)
        self.conanLogDock.setFloating(False)
        self.dockWidgetContents = QWidget()
        self.dockWidgetContents.setObjectName(u"dockWidgetContents")
        self.verticalLayout_3 = QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.conanLog = QPlainTextEdit(self.dockWidgetContents)
        self.conanLog.setObjectName(u"conanLog")

        self.verticalLayout_3.addWidget(self.conanLog)

        self.conanLogDock.setWidget(self.dockWidgetContents)
        RecipeWindow.addDockWidget(Qt.BottomDockWidgetArea, self.conanLogDock)
        self.conanCommandsDock = QDockWidget(RecipeWindow)
        self.conanCommandsDock.setObjectName(u"conanCommandsDock")
        self.dockWidgetContents_2 = QWidget()
        self.dockWidgetContents_2.setObjectName(u"dockWidgetContents_2")
        self.verticalLayout_4 = QVBoxLayout(self.dockWidgetContents_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.conanCommandHistory = RecipeCommandHistoryWidget(self.dockWidgetContents_2)
        self.conanCommandHistory.setObjectName(u"conanCommandHistory")
        self.conanCommandHistory.setContextMenuPolicy(Qt.CustomContextMenu)
        self.conanCommandHistory.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.conanCommandHistory.setAlternatingRowColors(True)

        self.verticalLayout_4.addWidget(self.conanCommandHistory)

        self.conanCommandsDock.setWidget(self.dockWidgetContents_2)
        RecipeWindow.addDockWidget(Qt.BottomDockWidgetArea, self.conanCommandsDock)
        self.conanConfigureDock = QDockWidget(RecipeWindow)
        self.conanConfigureDock.setObjectName(u"conanConfigureDock")
        self.dockWidgetContents_3 = QWidget()
        self.dockWidgetContents_3.setObjectName(u"dockWidgetContents_3")
        self.verticalLayout_5 = QVBoxLayout(self.dockWidgetContents_3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_2 = QScrollArea(self.dockWidgetContents_3)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 313, 211))
        self.verticalLayout_13 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.groupBox_7 = QGroupBox(self.scrollAreaWidgetContents_2)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.verticalLayout_17 = QVBoxLayout(self.groupBox_7)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.configurePackageId = QLabel(self.groupBox_7)
        self.configurePackageId.setObjectName(u"configurePackageId")
        self.configurePackageId.setContextMenuPolicy(Qt.CustomContextMenu)
        self.configurePackageId.setAlignment(Qt.AlignCenter)

        self.verticalLayout_17.addWidget(self.configurePackageId)


        self.verticalLayout_13.addWidget(self.groupBox_7)

        self.configureOptionsBox = QGroupBox(self.scrollAreaWidgetContents_2)
        self.configureOptionsBox.setObjectName(u"configureOptionsBox")
        self.optionsLayout = QGridLayout(self.configureOptionsBox)
        self.optionsLayout.setObjectName(u"optionsLayout")

        self.verticalLayout_13.addWidget(self.configureOptionsBox)

        self.groupBox_2 = QGroupBox(self.scrollAreaWidgetContents_2)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_19 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.configurePkgRefNamespace = QLineEdit(self.groupBox_2)
        self.configurePkgRefNamespace.setObjectName(u"configurePkgRefNamespace")

        self.verticalLayout_19.addWidget(self.configurePkgRefNamespace)


        self.verticalLayout_13.addWidget(self.groupBox_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_13.addItem(self.verticalSpacer)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_5.addWidget(self.scrollArea_2)

        self.conanConfigureDock.setWidget(self.dockWidgetContents_3)
        RecipeWindow.addDockWidget(Qt.RightDockWidgetArea, self.conanConfigureDock)
        self.conanLocalWorkflowDock = QDockWidget(RecipeWindow)
        self.conanLocalWorkflowDock.setObjectName(u"conanLocalWorkflowDock")
        self.dockWidgetContents_4 = QWidget()
        self.dockWidgetContents_4.setObjectName(u"dockWidgetContents_4")
        self.verticalLayout_6 = QVBoxLayout(self.dockWidgetContents_4)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(self.dockWidgetContents_4)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 328, 535))
        self.verticalLayout_12 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_7 = QLabel(self.scrollAreaWidgetContents)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_3.addWidget(self.label_7, 0, 0, 1, 1)

        self.localWorkflowCwd = QComboBox(self.scrollAreaWidgetContents)
        self.localWorkflowCwd.addItem("")
        self.localWorkflowCwd.addItem("")
        self.localWorkflowCwd.setObjectName(u"localWorkflowCwd")

        self.gridLayout_3.addWidget(self.localWorkflowCwd, 0, 1, 1, 1)

        self.label_10 = QLabel(self.scrollAreaWidgetContents)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_3.addWidget(self.label_10, 1, 0, 1, 1)

        self.localWorkflowCommonSubdir = QLineEdit(self.scrollAreaWidgetContents)
        self.localWorkflowCommonSubdir.setObjectName(u"localWorkflowCommonSubdir")

        self.gridLayout_3.addWidget(self.localWorkflowCommonSubdir, 1, 1, 1, 1)


        self.verticalLayout_12.addLayout(self.gridLayout_3)

        self.line = QFrame(self.scrollAreaWidgetContents)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_12.addWidget(self.line)

        self.groupBox_4 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.verticalLayout_11 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.groupBox_4)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 3, 0, 1, 1)

        self.localWorkflowImportsFolder = QLineEdit(self.groupBox_4)
        self.localWorkflowImportsFolder.setObjectName(u"localWorkflowImportsFolder")

        self.gridLayout.addWidget(self.localWorkflowImportsFolder, 4, 1, 1, 1)

        self.label_5 = QLabel(self.groupBox_4)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 8, 0, 1, 1)

        self.label_6 = QLabel(self.groupBox_4)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 4, 0, 1, 1)

        self.localWorkflowTestFolder = QLineEdit(self.groupBox_4)
        self.localWorkflowTestFolder.setObjectName(u"localWorkflowTestFolder")

        self.gridLayout.addWidget(self.localWorkflowTestFolder, 8, 1, 1, 1)

        self.localWorkflowExpressionEditor = QPushButton(self.groupBox_4)
        self.localWorkflowExpressionEditor.setObjectName(u"localWorkflowExpressionEditor")

        self.gridLayout.addWidget(self.localWorkflowExpressionEditor, 9, 0, 1, 2)

        self.localWorkflowSourceFolder = QLineEdit(self.groupBox_4)
        self.localWorkflowSourceFolder.setObjectName(u"localWorkflowSourceFolder")

        self.gridLayout.addWidget(self.localWorkflowSourceFolder, 5, 1, 1, 1)

        self.localWorkflowInstallFolder = QLineEdit(self.groupBox_4)
        self.localWorkflowInstallFolder.setObjectName(u"localWorkflowInstallFolder")

        self.gridLayout.addWidget(self.localWorkflowInstallFolder, 3, 1, 1, 1)

        self.label_4 = QLabel(self.groupBox_4)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 7, 0, 1, 1)

        self.localWorkflowBuildFolder = QLineEdit(self.groupBox_4)
        self.localWorkflowBuildFolder.setObjectName(u"localWorkflowBuildFolder")

        self.gridLayout.addWidget(self.localWorkflowBuildFolder, 6, 1, 1, 1)

        self.localWorkflowPackageFolder = QLineEdit(self.groupBox_4)
        self.localWorkflowPackageFolder.setObjectName(u"localWorkflowPackageFolder")

        self.gridLayout.addWidget(self.localWorkflowPackageFolder, 7, 1, 1, 1)

        self.label_3 = QLabel(self.groupBox_4)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 6, 0, 1, 1)

        self.label_2 = QLabel(self.groupBox_4)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 5, 0, 1, 1)


        self.verticalLayout_11.addLayout(self.gridLayout)


        self.verticalLayout_12.addWidget(self.groupBox_4)

        self.line_2 = QFrame(self.scrollAreaWidgetContents)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_12.addWidget(self.line_2)

        self.groupBox_3 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_10 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.localWorkflowClearAll = QPushButton(self.groupBox_3)
        self.localWorkflowClearAll.setObjectName(u"localWorkflowClearAll")

        self.verticalLayout_10.addWidget(self.localWorkflowClearAll)

        self.localWorkflowCommonBuildFolder = QPushButton(self.groupBox_3)
        self.localWorkflowCommonBuildFolder.setObjectName(u"localWorkflowCommonBuildFolder")

        self.verticalLayout_10.addWidget(self.localWorkflowCommonBuildFolder)

        self.localWorkflowProfileAndVersionBasedSubdirs = QPushButton(self.groupBox_3)
        self.localWorkflowProfileAndVersionBasedSubdirs.setObjectName(u"localWorkflowProfileAndVersionBasedSubdirs")

        self.verticalLayout_10.addWidget(self.localWorkflowProfileAndVersionBasedSubdirs)


        self.verticalLayout_12.addWidget(self.groupBox_3)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer_2)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_6.addWidget(self.scrollArea)

        self.conanLocalWorkflowDock.setWidget(self.dockWidgetContents_4)
        RecipeWindow.addDockWidget(Qt.RightDockWidgetArea, self.conanLocalWorkflowDock)
        self.conanDependencyDock = QDockWidget(RecipeWindow)
        self.conanDependencyDock.setObjectName(u"conanDependencyDock")
        self.dockWidgetContents_5 = QWidget()
        self.dockWidgetContents_5.setObjectName(u"dockWidgetContents_5")
        self.verticalLayout_7 = QVBoxLayout(self.dockWidgetContents_5)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_3 = QScrollArea(self.dockWidgetContents_5)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 326, 531))
        self.verticalLayout_14 = QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.dependentsTabs = QTabWidget(self.scrollAreaWidgetContents_3)
        self.dependentsTabs.setObjectName(u"dependentsTabs")
        self.dependentsTabs.setTabBarAutoHide(True)
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_8 = QVBoxLayout(self.tab_2)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.dependenciesPackageList = QListView(self.tab_2)
        self.dependenciesPackageList.setObjectName(u"dependenciesPackageList")
        self.dependenciesPackageList.setContextMenuPolicy(Qt.CustomContextMenu)
        self.dependenciesPackageList.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.verticalLayout_8.addWidget(self.dependenciesPackageList)

        self.groupBox_5 = QGroupBox(self.tab_2)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.verticalLayout_15 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.label_11 = QLabel(self.groupBox_5)
        self.label_11.setObjectName(u"label_11")
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(True)
        self.label_11.setFont(font)
        self.label_11.setAlignment(Qt.AlignCenter)

        self.verticalLayout_15.addWidget(self.label_11)

        self.label_12 = QLabel(self.groupBox_5)
        self.label_12.setObjectName(u"label_12")
        font1 = QFont()
        font1.setPointSize(10)
        self.label_12.setFont(font1)
        self.label_12.setAlignment(Qt.AlignCenter)

        self.verticalLayout_15.addWidget(self.label_12)

        self.label_13 = QLabel(self.groupBox_5)
        self.label_13.setObjectName(u"label_13")
        font2 = QFont()
        font2.setPointSize(10)
        font2.setItalic(True)
        self.label_13.setFont(font2)
        self.label_13.setAlignment(Qt.AlignCenter)

        self.verticalLayout_15.addWidget(self.label_13)


        self.verticalLayout_8.addWidget(self.groupBox_5)

        self.dependentsTabs.addTab(self.tab_2, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_9 = QVBoxLayout(self.tab)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.dependenciesPackageTree = QTreeView(self.tab)
        self.dependenciesPackageTree.setObjectName(u"dependenciesPackageTree")
        self.dependenciesPackageTree.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.verticalLayout_9.addWidget(self.dependenciesPackageTree)

        self.dependentsTabs.addTab(self.tab, "")

        self.verticalLayout_14.addWidget(self.dependentsTabs)

        self.groupBox_6 = QGroupBox(self.scrollAreaWidgetContents_3)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.verticalLayout_16 = QVBoxLayout(self.groupBox_6)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 20)
        self.dependencyView = DependencyView(self.groupBox_6)
        self.dependencyView.setObjectName(u"dependencyView")
        self.dependencyView.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.verticalLayout_16.addWidget(self.dependencyView)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.dependency_rankdir = QComboBox(self.groupBox_6)
        self.dependency_rankdir.addItem("")
        self.dependency_rankdir.addItem("")
        self.dependency_rankdir.setObjectName(u"dependency_rankdir")

        self.horizontalLayout.addWidget(self.dependency_rankdir)


        self.verticalLayout_16.addLayout(self.horizontalLayout)


        self.verticalLayout_14.addWidget(self.groupBox_6)

        self.dependentsLog = QPlainTextEdit(self.scrollAreaWidgetContents_3)
        self.dependentsLog.setObjectName(u"dependentsLog")
        self.dependentsLog.setContextMenuPolicy(Qt.CustomContextMenu)
        self.dependentsLog.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.dependentsLog.setUndoRedoEnabled(False)
        self.dependentsLog.setReadOnly(True)

        self.verticalLayout_14.addWidget(self.dependentsLog)

        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)

        self.verticalLayout_7.addWidget(self.scrollArea_3)

        self.conanDependencyDock.setWidget(self.dockWidgetContents_5)
        RecipeWindow.addDockWidget(Qt.LeftDockWidgetArea, self.conanDependencyDock)

        self.menuBar.addAction(self.menuRecipe.menuAction())
        self.menuBar.addAction(self.menuCommands.menuAction())
        self.menuRecipe.addAction(self.actionOpen_recipe_in_editor)
        self.menuRecipe.addAction(self.actionOpen_recipe_folder)
        self.menuRecipe.addAction(self.actionCopy_recipe_folder_to_clipboard)
        self.menuRecipe.addSeparator()
        self.menuRecipe.addAction(self.actionOpen_another_version)
        self.menuRecipe.addSeparator()
        self.menuRecipe.addAction(self.actionManage_associated_local_cache)
        self.menuRecipe.addSeparator()
        self.menuRecipe.addAction(self.actionReload)
        self.menuRecipe.addSeparator()
        self.menuRecipe.addAction(self.actionClose)
        self.menuCommands.addAction(self.actionCreateCommand)
        self.menuCommands.addAction(self.actionCreateUpdateCommand)
        self.menuCommands.addSeparator()
        self.menuCommands.addAction(self.menuLocal_workflow.menuAction())
        self.menuCommands.addSeparator()
        self.menuCommands.addAction(self.actionRemovePackageCommand)
        self.menuCommands.addSeparator()
        self.menuCommands.addAction(self.actionCancelCommand)
        self.menuLocal_workflow.addAction(self.actionInstallCommand)
        self.menuLocal_workflow.addAction(self.actionInstallUpdateCommand)
        self.menuLocal_workflow.addAction(self.actionImportsCommand)
        self.menuLocal_workflow.addAction(self.actionSourceCommand)
        self.menuLocal_workflow.addAction(self.actionBuildCommand)
        self.menuLocal_workflow.addAction(self.actionPackageCommand)
        self.menuLocal_workflow.addAction(self.actionExportPackageCommand)
        self.menuLocal_workflow.addAction(self.actionTestCommand)
        self.menuLocal_workflow.addAction(self.menuCMake.menuAction())
        self.menuCMake.addAction(self.actionCMakeBuildToolCommand)
        self.menuCMake.addAction(self.actionCMakeBuildToolVerboseCommand)
        self.menuCMake.addAction(self.actionCMakeRemoveCacheCommand)

        self.retranslateUi(RecipeWindow)

        self.dependentsTabs.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(RecipeWindow)
    # setupUi

    def retranslateUi(self, RecipeWindow):
        RecipeWindow.setWindowTitle(QCoreApplication.translate("RecipeWindow", u"A recipe window", None))
        self.actionCreateCommand.setText(QCoreApplication.translate("RecipeWindow", u"Create package in local cache", None))
        self.actionCreateUpdateCommand.setText(QCoreApplication.translate("RecipeWindow", u"Create package in local cache with latest dependencies", None))
        self.actionImportsCommand.setText(QCoreApplication.translate("RecipeWindow", u"Import files from dependents", None))
        self.actionInstallCommand.setText(QCoreApplication.translate("RecipeWindow", u"Download dependencies and configure", None))
        self.actionInstallUpdateCommand.setText(QCoreApplication.translate("RecipeWindow", u"Download latest dependencies and configure", None))
        self.actionSourceCommand.setText(QCoreApplication.translate("RecipeWindow", u"Get source code", None))
        self.actionBuildCommand.setText(QCoreApplication.translate("RecipeWindow", u"Build source", None))
        self.actionPackageCommand.setText(QCoreApplication.translate("RecipeWindow", u"Make local package", None))
        self.actionExportPackageCommand.setText(QCoreApplication.translate("RecipeWindow", u"Export package to local cache", None))
        self.actionTestCommand.setText(QCoreApplication.translate("RecipeWindow", u"Test package in local cache", None))
        self.actionCancelCommand.setText(QCoreApplication.translate("RecipeWindow", u"Cancel running command", None))
        self.actionRemovePackageCommand.setText(QCoreApplication.translate("RecipeWindow", u"Remove package from local cache", None))
        self.actionCMakeBuildToolCommand.setText(QCoreApplication.translate("RecipeWindow", u"Run CMake build tool", None))
        self.actionCMakeBuildToolVerboseCommand.setText(QCoreApplication.translate("RecipeWindow", u"Run CMake build tool (verbose)", None))
        self.actionCMakeRemoveCacheCommand.setText(QCoreApplication.translate("RecipeWindow", u"Delete CMake cache", None))
        self.actionOpen_another_version.setText(QCoreApplication.translate("RecipeWindow", u"Open another version of this recipe...", None))
#if QT_CONFIG(tooltip)
        self.actionOpen_another_version.setToolTip(QCoreApplication.translate("RecipeWindow", u"Open another version of this recipe", None))
#endif // QT_CONFIG(tooltip)
        self.actionManage_associated_local_cache.setText(QCoreApplication.translate("RecipeWindow", u"Manage associated local cache...", None))
        self.actionClose.setText(QCoreApplication.translate("RecipeWindow", u"Close", None))
        self.actionOpen_recipe_in_editor.setText(QCoreApplication.translate("RecipeWindow", u"Open recipe in editor...", None))
#if QT_CONFIG(tooltip)
        self.actionOpen_recipe_in_editor.setToolTip(QCoreApplication.translate("RecipeWindow", u"Open recipe in editor set in preferences", None))
#endif // QT_CONFIG(tooltip)
        self.actionOpen_recipe_folder.setText(QCoreApplication.translate("RecipeWindow", u"Open recipe folder...", None))
        self.actionCopy_recipe_folder_to_clipboard.setText(QCoreApplication.translate("RecipeWindow", u"Copy recipe folder to clipboard", None))
#if QT_CONFIG(tooltip)
        self.actionCopy_recipe_folder_to_clipboard.setToolTip(QCoreApplication.translate("RecipeWindow", u"Copy recipe folder to clipboard", None))
#endif // QT_CONFIG(tooltip)
        self.actionReload.setText(QCoreApplication.translate("RecipeWindow", u"Reload", None))
        self.pane_tabs.setTabText(self.pane_tabs.indexOf(self.default_panes_tab), QCoreApplication.translate("RecipeWindow", u"Default", None))
        self.behaviourToolbar.setWindowTitle(QCoreApplication.translate("RecipeWindow", u"Recipe behaviours", None))
        self.commandToolbar.setWindowTitle(QCoreApplication.translate("RecipeWindow", u"Recipe commands", None))
        self.buildFeaturesToolbar.setWindowTitle(QCoreApplication.translate("RecipeWindow", u"Build features", None))
        self.menuRecipe.setTitle(QCoreApplication.translate("RecipeWindow", u"Recipe", None))
        self.menuCommands.setTitle(QCoreApplication.translate("RecipeWindow", u"Commands", None))
        self.menuLocal_workflow.setTitle(QCoreApplication.translate("RecipeWindow", u"Local workflow", None))
        self.menuCMake.setTitle(QCoreApplication.translate("RecipeWindow", u"CMake", None))
        self.conanLogDock.setWindowTitle(QCoreApplication.translate("RecipeWindow", u"Conan logging", None))
        self.conanCommandsDock.setWindowTitle(QCoreApplication.translate("RecipeWindow", u"Conan command history", None))
        self.conanConfigureDock.setWindowTitle(QCoreApplication.translate("RecipeWindow", u"Configuration", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("RecipeWindow", u"Package ID", None))
        self.configurePackageId.setText("")
        self.configureOptionsBox.setTitle(QCoreApplication.translate("RecipeWindow", u"Options", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("RecipeWindow", u"Package reference namespace", None))
        self.configurePkgRefNamespace.setPlaceholderText(QCoreApplication.translate("RecipeWindow", u"@user/channel", None))
        self.conanLocalWorkflowDock.setWindowTitle(QCoreApplication.translate("RecipeWindow", u"Local workflow", None))
        self.label_7.setText(QCoreApplication.translate("RecipeWindow", u"Working dir", None))
        self.localWorkflowCwd.setItemText(0, QCoreApplication.translate("RecipeWindow", u"Relative to recipe folder", None))
        self.localWorkflowCwd.setItemText(1, QCoreApplication.translate("RecipeWindow", u"Relative to git workspace", None))

        self.label_10.setText(QCoreApplication.translate("RecipeWindow", u"Common subdir", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("RecipeWindow", u"Conan command folders", None))
        self.label.setText(QCoreApplication.translate("RecipeWindow", u"Install", None))
        self.label_5.setText(QCoreApplication.translate("RecipeWindow", u"Test", None))
        self.label_6.setText(QCoreApplication.translate("RecipeWindow", u"Imports", None))
        self.localWorkflowExpressionEditor.setText(QCoreApplication.translate("RecipeWindow", u"Expression editor...", None))
        self.label_4.setText(QCoreApplication.translate("RecipeWindow", u"Package", None))
        self.label_3.setText(QCoreApplication.translate("RecipeWindow", u"Build", None))
        self.label_2.setText(QCoreApplication.translate("RecipeWindow", u"Source", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("RecipeWindow", u"Presets", None))
        self.localWorkflowClearAll.setText(QCoreApplication.translate("RecipeWindow", u"Clear all", None))
        self.localWorkflowCommonBuildFolder.setText(QCoreApplication.translate("RecipeWindow", u"Common 'build' folder", None))
        self.localWorkflowProfileAndVersionBasedSubdirs.setText(QCoreApplication.translate("RecipeWindow", u"Profile and version specific subfolders", None))
        self.conanDependencyDock.setWindowTitle(QCoreApplication.translate("RecipeWindow", u"Dependencies", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("RecipeWindow", u"Legend", None))
        self.label_11.setText(QCoreApplication.translate("RecipeWindow", u"Top-level package", None))
        self.label_12.setText(QCoreApplication.translate("RecipeWindow", u"Runtime dependency", None))
        self.label_13.setText(QCoreApplication.translate("RecipeWindow", u"Build dependency", None))
        self.dependentsTabs.setTabText(self.dependentsTabs.indexOf(self.tab_2), QCoreApplication.translate("RecipeWindow", u"List", None))
        self.dependentsTabs.setTabText(self.dependentsTabs.indexOf(self.tab), QCoreApplication.translate("RecipeWindow", u"Tree", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("RecipeWindow", u"Visualisation", None))
        self.dependency_rankdir.setItemText(0, QCoreApplication.translate("RecipeWindow", u"Left to right", None))
        self.dependency_rankdir.setItemText(1, QCoreApplication.translate("RecipeWindow", u"Top to bottom", None))

    # retranslateUi

