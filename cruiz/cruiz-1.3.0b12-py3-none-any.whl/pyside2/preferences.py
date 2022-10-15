# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'preferences.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from cruiz.widgets.shortcutlineedit import ShortcutLineEdit


class Ui_PreferencesDialog(object):
    def setupUi(self, PreferencesDialog):
        if not PreferencesDialog.objectName():
            PreferencesDialog.setObjectName(u"PreferencesDialog")
        PreferencesDialog.resize(678, 670)
        self.actionForget_recipe = QAction(PreferencesDialog)
        self.actionForget_recipe.setObjectName(u"actionForget_recipe")
        self.actionForget_config = QAction(PreferencesDialog)
        self.actionForget_config.setObjectName(u"actionForget_config")
        self.actionForget_remote = QAction(PreferencesDialog)
        self.actionForget_remote.setObjectName(u"actionForget_remote")
        self.verticalLayout = QVBoxLayout(PreferencesDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.prefs_toolbox = QToolBox(PreferencesDialog)
        self.prefs_toolbox.setObjectName(u"prefs_toolbox")
        self.prefs_general = QWidget()
        self.prefs_general.setObjectName(u"prefs_general")
        self.prefs_general.setGeometry(QRect(0, 0, 639, 275))
        self.gridLayout = QGridLayout(self.prefs_general)
        self.gridLayout.setObjectName(u"gridLayout")
        self.prefs_general_busy_colour = QPushButton(self.prefs_general)
        self.prefs_general_busy_colour.setObjectName(u"prefs_general_busy_colour")

        self.gridLayout.addWidget(self.prefs_general_busy_colour, 7, 2, 1, 1)

        self.prefs_general_found_text_background_colour = QPushButton(self.prefs_general)
        self.prefs_general_found_text_background_colour.setObjectName(u"prefs_general_found_text_background_colour")

        self.gridLayout.addWidget(self.prefs_general_found_text_background_colour, 8, 2, 1, 1)

        self.prefs_general_usebatching = QCheckBox(self.prefs_general)
        self.prefs_general_usebatching.setObjectName(u"prefs_general_usebatching")

        self.gridLayout.addWidget(self.prefs_general_usebatching, 2, 2, 1, 1)

        self.prefs_general_default_recipe_dir = QLineEdit(self.prefs_general)
        self.prefs_general_default_recipe_dir.setObjectName(u"prefs_general_default_recipe_dir")

        self.gridLayout.addWidget(self.prefs_general_default_recipe_dir, 6, 2, 1, 1)

        self.prefs_general_enable_wallclock = QCheckBox(self.prefs_general)
        self.prefs_general_enable_wallclock.setObjectName(u"prefs_general_enable_wallclock")

        self.gridLayout.addWidget(self.prefs_general_enable_wallclock, 3, 2, 1, 1)

        self.prefs_general_enable_compact = QCheckBox(self.prefs_general)
        self.prefs_general_enable_compact.setObjectName(u"prefs_general_enable_compact")
        self.prefs_general_enable_compact.setVisible(False)

        self.gridLayout.addWidget(self.prefs_general_enable_compact, 5, 2, 1, 1)

        self.prefs_general_clearpanes = QCheckBox(self.prefs_general)
        self.prefs_general_clearpanes.setObjectName(u"prefs_general_clearpanes")

        self.gridLayout.addWidget(self.prefs_general_clearpanes, 0, 2, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 16, 2, 1, 1)

        self.prefs_general_new_recipe_load = QCheckBox(self.prefs_general)
        self.prefs_general_new_recipe_load.setObjectName(u"prefs_general_new_recipe_load")
        self.prefs_general_new_recipe_load.setVisible(False)

        self.gridLayout.addWidget(self.prefs_general_new_recipe_load, 9, 2, 1, 1)

        self.label_2 = QLabel(self.prefs_general)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 7, 0, 1, 1)

        self.label = QLabel(self.prefs_general)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 6, 0, 1, 1)

        self.prefs_general_combine_panes = QCheckBox(self.prefs_general)
        self.prefs_general_combine_panes.setObjectName(u"prefs_general_combine_panes")

        self.gridLayout.addWidget(self.prefs_general_combine_panes, 1, 2, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_3, 16, 0, 1, 1)

        self.label_30 = QLabel(self.prefs_general)
        self.label_30.setObjectName(u"label_30")

        self.gridLayout.addWidget(self.label_30, 8, 0, 1, 1)

        self.prefs_general_enable_darkmode = QCheckBox(self.prefs_general)
        self.prefs_general_enable_darkmode.setObjectName(u"prefs_general_enable_darkmode")

        self.gridLayout.addWidget(self.prefs_general_enable_darkmode, 4, 2, 1, 1)

        self.prefs_general_recipe_editor = QLineEdit(self.prefs_general)
        self.prefs_general_recipe_editor.setObjectName(u"prefs_general_recipe_editor")

        self.gridLayout.addWidget(self.prefs_general_recipe_editor, 15, 2, 1, 1)

        self.label_31 = QLabel(self.prefs_general)
        self.label_31.setObjectName(u"label_31")

        self.gridLayout.addWidget(self.label_31, 15, 0, 1, 1)

        self.prefs_toolbox.addItem(self.prefs_general, u"General")
        self.prefs_fonts = QWidget()
        self.prefs_fonts.setObjectName(u"prefs_fonts")
        self.prefs_fonts.setGeometry(QRect(0, 0, 432, 233))
        self.verticalLayout_2 = QVBoxLayout(self.prefs_fonts)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.groupBox = QGroupBox(self.prefs_fonts)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.prefs_font_ui_label = QLabel(self.groupBox)
        self.prefs_font_ui_label.setObjectName(u"prefs_font_ui_label")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.prefs_font_ui_label.sizePolicy().hasHeightForWidth())
        self.prefs_font_ui_label.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.prefs_font_ui_label, 0, 0, 1, 1)

        self.prefs_font_ui_preview = QLabel(self.groupBox)
        self.prefs_font_ui_preview.setObjectName(u"prefs_font_ui_preview")
        sizePolicy.setHeightForWidth(self.prefs_font_ui_preview.sizePolicy().hasHeightForWidth())
        self.prefs_font_ui_preview.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.prefs_font_ui_preview, 1, 0, 1, 1)

        self.prefs_font_ui_reset = QPushButton(self.groupBox)
        self.prefs_font_ui_reset.setObjectName(u"prefs_font_ui_reset")

        self.gridLayout_2.addWidget(self.prefs_font_ui_reset, 1, 1, 1, 1)

        self.prefs_font_ui_change = QPushButton(self.groupBox)
        self.prefs_font_ui_change.setObjectName(u"prefs_font_ui_change")

        self.gridLayout_2.addWidget(self.prefs_font_ui_change, 0, 1, 1, 1)


        self.verticalLayout_2.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.prefs_fonts)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_3 = QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.prefs_font_output_label = QLabel(self.groupBox_2)
        self.prefs_font_output_label.setObjectName(u"prefs_font_output_label")
        sizePolicy.setHeightForWidth(self.prefs_font_output_label.sizePolicy().hasHeightForWidth())
        self.prefs_font_output_label.setSizePolicy(sizePolicy)

        self.gridLayout_3.addWidget(self.prefs_font_output_label, 0, 0, 1, 1)

        self.prefs_font_output_preview = QLabel(self.groupBox_2)
        self.prefs_font_output_preview.setObjectName(u"prefs_font_output_preview")
        sizePolicy.setHeightForWidth(self.prefs_font_output_preview.sizePolicy().hasHeightForWidth())
        self.prefs_font_output_preview.setSizePolicy(sizePolicy)

        self.gridLayout_3.addWidget(self.prefs_font_output_preview, 1, 0, 1, 1)

        self.prefs_font_output_reset = QPushButton(self.groupBox_2)
        self.prefs_font_output_reset.setObjectName(u"prefs_font_output_reset")

        self.gridLayout_3.addWidget(self.prefs_font_output_reset, 1, 1, 1, 1)

        self.prefs_font_output_change = QPushButton(self.groupBox_2)
        self.prefs_font_output_change.setObjectName(u"prefs_font_output_change")

        self.gridLayout_3.addWidget(self.prefs_font_output_change, 0, 1, 1, 1)


        self.verticalLayout_2.addWidget(self.groupBox_2)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.prefs_toolbox.addItem(self.prefs_fonts, u"Fonts")
        self.prefs_conan = QWidget()
        self.prefs_conan.setObjectName(u"prefs_conan")
        self.prefs_conan.setGeometry(QRect(0, 0, 343, 172))
        self.verticalLayout_3 = QVBoxLayout(self.prefs_conan)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.groupBox_3 = QGroupBox(self.prefs_conan)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.gridLayout_4 = QGridLayout(self.groupBox_3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_7 = QLabel(self.groupBox_3)
        self.label_7.setObjectName(u"label_7")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy1)

        self.gridLayout_4.addWidget(self.label_7, 0, 0, 1, 1)

        self.prefs_conan_log_level = QComboBox(self.groupBox_3)
        self.prefs_conan_log_level.addItem("")
        self.prefs_conan_log_level.addItem("")
        self.prefs_conan_log_level.addItem("")
        self.prefs_conan_log_level.addItem("")
        self.prefs_conan_log_level.addItem("")
        self.prefs_conan_log_level.addItem("")
        self.prefs_conan_log_level.setObjectName(u"prefs_conan_log_level")

        self.gridLayout_4.addWidget(self.prefs_conan_log_level, 0, 1, 1, 1)


        self.verticalLayout_3.addWidget(self.groupBox_3)

        self.groupBox_4 = QGroupBox(self.prefs_conan)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.gridLayout_5 = QGridLayout(self.groupBox_4)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_8 = QLabel(self.groupBox_4)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_5.addWidget(self.label_8, 0, 0, 1, 1)

        self.prefs_conan_version_list_path_segment = QLineEdit(self.groupBox_4)
        self.prefs_conan_version_list_path_segment.setObjectName(u"prefs_conan_version_list_path_segment")

        self.gridLayout_5.addWidget(self.prefs_conan_version_list_path_segment, 0, 1, 1, 1)


        self.verticalLayout_3.addWidget(self.groupBox_4)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_4)

        self.prefs_toolbox.addItem(self.prefs_conan, u"Conan")
        self.prefs_localcache = QWidget()
        self.prefs_localcache.setObjectName(u"prefs_localcache")
        self.prefs_localcache.setGeometry(QRect(0, 0, 297, 203))
        self.verticalLayout_4 = QVBoxLayout(self.prefs_localcache)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.groupBox_5 = QGroupBox(self.prefs_localcache)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.gridLayout_6 = QGridLayout(self.groupBox_5)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.label_9 = QLabel(self.groupBox_5)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_6.addWidget(self.label_9, 0, 0, 1, 1)

        self.prefs_localcache_config_to_install = QLineEdit(self.groupBox_5)
        self.prefs_localcache_config_to_install.setObjectName(u"prefs_localcache_config_to_install")

        self.gridLayout_6.addWidget(self.prefs_localcache_config_to_install, 0, 1, 1, 1)

        self.label_10 = QLabel(self.groupBox_5)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_6.addWidget(self.label_10, 1, 0, 1, 1)

        self.prefs_localcache_config_git_branch = QLineEdit(self.groupBox_5)
        self.prefs_localcache_config_git_branch.setObjectName(u"prefs_localcache_config_git_branch")

        self.gridLayout_6.addWidget(self.prefs_localcache_config_git_branch, 1, 1, 1, 1)


        self.verticalLayout_4.addWidget(self.groupBox_5)

        self.groupBox_6 = QGroupBox(self.prefs_localcache)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.gridLayout_7 = QGridLayout(self.groupBox_6)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.prefs_localcache_do_forget = QPushButton(self.groupBox_6)
        self.prefs_localcache_do_forget.setObjectName(u"prefs_localcache_do_forget")

        self.gridLayout_7.addWidget(self.prefs_localcache_do_forget, 0, 1, 1, 1)

        self.prefs_localcache_forget_cache = QComboBox(self.groupBox_6)
        self.prefs_localcache_forget_cache.setObjectName(u"prefs_localcache_forget_cache")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(1)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.prefs_localcache_forget_cache.sizePolicy().hasHeightForWidth())
        self.prefs_localcache_forget_cache.setSizePolicy(sizePolicy2)

        self.gridLayout_7.addWidget(self.prefs_localcache_forget_cache, 0, 0, 1, 1)


        self.verticalLayout_4.addWidget(self.groupBox_6)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_5)

        self.prefs_toolbox.addItem(self.prefs_localcache, u"Local cache")
        self.prefs_graphviz = QWidget()
        self.prefs_graphviz.setObjectName(u"prefs_graphviz")
        self.prefs_graphviz.setGeometry(QRect(0, 0, 305, 79))
        self.gridLayout_8 = QGridLayout(self.prefs_graphviz)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_8.addItem(self.verticalSpacer_8, 2, 1, 1, 1)

        self.prefs_graphviz_bin_directory = QLineEdit(self.prefs_graphviz)
        self.prefs_graphviz_bin_directory.setObjectName(u"prefs_graphviz_bin_directory")

        self.gridLayout_8.addWidget(self.prefs_graphviz_bin_directory, 1, 1, 1, 1)

        self.label_11 = QLabel(self.prefs_graphviz)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_8.addWidget(self.label_11, 1, 0, 1, 1)

        self.label_29 = QLabel(self.prefs_graphviz)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setOpenExternalLinks(True)

        self.gridLayout_8.addWidget(self.label_29, 0, 0, 1, 2)

        self.prefs_toolbox.addItem(self.prefs_graphviz, u"GraphViz")
        self.prefs_cmake = QWidget()
        self.prefs_cmake.setObjectName(u"prefs_cmake")
        self.prefs_cmake.setGeometry(QRect(0, 0, 175, 86))
        self.gridLayout_9 = QGridLayout(self.prefs_cmake)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.label_12 = QLabel(self.prefs_cmake)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_9.addWidget(self.label_12, 0, 0, 1, 1)

        self.prefs_cmake_cmake_bin_directory = QLineEdit(self.prefs_cmake)
        self.prefs_cmake_cmake_bin_directory.setObjectName(u"prefs_cmake_cmake_bin_directory")

        self.gridLayout_9.addWidget(self.prefs_cmake_cmake_bin_directory, 0, 1, 1, 1)

        self.label_13 = QLabel(self.prefs_cmake)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_9.addWidget(self.label_13, 1, 0, 1, 1)

        self.prefs_cmake_ninja_bin_directory = QLineEdit(self.prefs_cmake)
        self.prefs_cmake_ninja_bin_directory.setObjectName(u"prefs_cmake_ninja_bin_directory")

        self.gridLayout_9.addWidget(self.prefs_cmake_ninja_bin_directory, 1, 1, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_9.addItem(self.verticalSpacer_6, 2, 0, 1, 1)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_9.addItem(self.verticalSpacer_7, 2, 1, 1, 1)

        self.prefs_toolbox.addItem(self.prefs_cmake, u"CMake")
        self.prefs_compilercache = QWidget()
        self.prefs_compilercache.setObjectName(u"prefs_compilercache")
        self.prefs_compilercache.setGeometry(QRect(0, 0, 405, 384))
        self.verticalLayout_5 = QVBoxLayout(self.prefs_compilercache)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.groupBox_7 = QGroupBox(self.prefs_compilercache)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.verticalLayout_6 = QVBoxLayout(self.groupBox_7)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.prefs_compilercache_default = QComboBox(self.groupBox_7)
        self.prefs_compilercache_default.addItem("")
        self.prefs_compilercache_default.addItem("")
        self.prefs_compilercache_default.addItem("")
        self.prefs_compilercache_default.addItem("")
        self.prefs_compilercache_default.setObjectName(u"prefs_compilercache_default")

        self.verticalLayout_6.addWidget(self.prefs_compilercache_default)


        self.verticalLayout_5.addWidget(self.groupBox_7)

        self.groupBox_8 = QGroupBox(self.prefs_compilercache)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.gridLayout_10 = QGridLayout(self.groupBox_8)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.label_15 = QLabel(self.groupBox_8)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout_10.addWidget(self.label_15, 1, 0, 1, 1)

        self.prefs_compilercache_ccache_location = QLineEdit(self.groupBox_8)
        self.prefs_compilercache_ccache_location.setObjectName(u"prefs_compilercache_ccache_location")

        self.gridLayout_10.addWidget(self.prefs_compilercache_ccache_location, 1, 1, 1, 1)

        self.label_14 = QLabel(self.groupBox_8)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setOpenExternalLinks(True)

        self.gridLayout_10.addWidget(self.label_14, 0, 0, 1, 2)


        self.verticalLayout_5.addWidget(self.groupBox_8)

        self.groupBox_9 = QGroupBox(self.prefs_compilercache)
        self.groupBox_9.setObjectName(u"groupBox_9")
        self.gridLayout_11 = QGridLayout(self.groupBox_9)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.label_17 = QLabel(self.groupBox_9)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout_11.addWidget(self.label_17, 1, 0, 1, 1)

        self.prefs_compilercache_sccache_location = QLineEdit(self.groupBox_9)
        self.prefs_compilercache_sccache_location.setObjectName(u"prefs_compilercache_sccache_location")

        self.gridLayout_11.addWidget(self.prefs_compilercache_sccache_location, 1, 1, 1, 1)

        self.label_16 = QLabel(self.groupBox_9)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setOpenExternalLinks(True)

        self.gridLayout_11.addWidget(self.label_16, 0, 0, 1, 2)


        self.verticalLayout_5.addWidget(self.groupBox_9)

        self.groupBox_10 = QGroupBox(self.prefs_compilercache)
        self.groupBox_10.setObjectName(u"groupBox_10")
        self.gridLayout_12 = QGridLayout(self.groupBox_10)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.label_19 = QLabel(self.groupBox_10)
        self.label_19.setObjectName(u"label_19")

        self.gridLayout_12.addWidget(self.label_19, 1, 0, 1, 1)

        self.prefs_compilercache_buildcache_location = QLineEdit(self.groupBox_10)
        self.prefs_compilercache_buildcache_location.setObjectName(u"prefs_compilercache_buildcache_location")

        self.gridLayout_12.addWidget(self.prefs_compilercache_buildcache_location, 1, 1, 1, 1)

        self.label_18 = QLabel(self.groupBox_10)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setOpenExternalLinks(True)

        self.gridLayout_12.addWidget(self.label_18, 0, 0, 1, 2)


        self.verticalLayout_5.addWidget(self.groupBox_10)

        self.verticalSpacer_13 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_13)

        self.prefs_toolbox.addItem(self.prefs_compilercache, u"Compiler cache")
        self.prefs_shortcuts = QWidget()
        self.prefs_shortcuts.setObjectName(u"prefs_shortcuts")
        self.prefs_shortcuts.setGeometry(QRect(0, 0, 639, 519))
        self.gridLayout_13 = QGridLayout(self.prefs_shortcuts)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.prefs_shortcuts_installupdates_edit = ShortcutLineEdit(self.prefs_shortcuts)
        self.prefs_shortcuts_installupdates_edit.setObjectName(u"prefs_shortcuts_installupdates_edit")

        self.gridLayout_13.addWidget(self.prefs_shortcuts_installupdates_edit, 4, 2, 1, 1)

        self.prefs_shortcuts_remove_edit = ShortcutLineEdit(self.prefs_shortcuts)
        self.prefs_shortcuts_remove_edit.setObjectName(u"prefs_shortcuts_remove_edit")

        self.gridLayout_13.addWidget(self.prefs_shortcuts_remove_edit, 10, 2, 1, 1)

        self.label_23 = QLabel(self.prefs_shortcuts)
        self.label_23.setObjectName(u"label_23")

        self.gridLayout_13.addWidget(self.label_23, 9, 0, 1, 1)

        self.label_20 = QLabel(self.prefs_shortcuts)
        self.label_20.setObjectName(u"label_20")

        self.gridLayout_13.addWidget(self.label_20, 6, 0, 1, 1)

        self.prefs_shortcuts_install_edit = ShortcutLineEdit(self.prefs_shortcuts)
        self.prefs_shortcuts_install_edit.setObjectName(u"prefs_shortcuts_install_edit")

        self.gridLayout_13.addWidget(self.prefs_shortcuts_install_edit, 3, 2, 1, 1)

        self.prefs_shortcuts_source_edit = ShortcutLineEdit(self.prefs_shortcuts)
        self.prefs_shortcuts_source_edit.setObjectName(u"prefs_shortcuts_source_edit")

        self.gridLayout_13.addWidget(self.prefs_shortcuts_source_edit, 5, 2, 1, 1)

        self.verticalSpacer_12 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_13.addItem(self.verticalSpacer_12, 15, 2, 1, 1)

        self.prefs_shortcuts_cmakebuildtoolverbose_edit = ShortcutLineEdit(self.prefs_shortcuts)
        self.prefs_shortcuts_cmakebuildtoolverbose_edit.setObjectName(u"prefs_shortcuts_cmakebuildtoolverbose_edit")

        self.gridLayout_13.addWidget(self.prefs_shortcuts_cmakebuildtoolverbose_edit, 13, 2, 1, 1)

        self.label_1 = QLabel(self.prefs_shortcuts)
        self.label_1.setObjectName(u"label_1")
        self.label_1.setTextFormat(Qt.RichText)

        self.gridLayout_13.addWidget(self.label_1, 0, 0, 1, 1)

        self.label_25 = QLabel(self.prefs_shortcuts)
        self.label_25.setObjectName(u"label_25")

        self.gridLayout_13.addWidget(self.label_25, 11, 0, 1, 1)

        self.label_22 = QLabel(self.prefs_shortcuts)
        self.label_22.setObjectName(u"label_22")

        self.gridLayout_13.addWidget(self.label_22, 8, 0, 1, 1)

        self.label_26 = QLabel(self.prefs_shortcuts)
        self.label_26.setObjectName(u"label_26")

        self.gridLayout_13.addWidget(self.label_26, 12, 0, 1, 1)

        self.label_5 = QLabel(self.prefs_shortcuts)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_13.addWidget(self.label_5, 4, 0, 1, 1)

        self.prefs_shortcuts_cmakebuildtool_edit = ShortcutLineEdit(self.prefs_shortcuts)
        self.prefs_shortcuts_cmakebuildtool_edit.setObjectName(u"prefs_shortcuts_cmakebuildtool_edit")

        self.gridLayout_13.addWidget(self.prefs_shortcuts_cmakebuildtool_edit, 12, 2, 1, 1)

        self.label_6 = QLabel(self.prefs_shortcuts)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_13.addWidget(self.label_6, 5, 0, 1, 1)

        self.label_27 = QLabel(self.prefs_shortcuts)
        self.label_27.setObjectName(u"label_27")

        self.gridLayout_13.addWidget(self.label_27, 13, 0, 1, 1)

        self.prefs_shortcuts_test_edit = ShortcutLineEdit(self.prefs_shortcuts)
        self.prefs_shortcuts_test_edit.setObjectName(u"prefs_shortcuts_test_edit")

        self.gridLayout_13.addWidget(self.prefs_shortcuts_test_edit, 9, 2, 1, 1)

        self.prefs_shortcuts_package_edit = ShortcutLineEdit(self.prefs_shortcuts)
        self.prefs_shortcuts_package_edit.setObjectName(u"prefs_shortcuts_package_edit")

        self.gridLayout_13.addWidget(self.prefs_shortcuts_package_edit, 7, 2, 1, 1)

        self.prefs_shortcuts_deletecmakecache_edit = ShortcutLineEdit(self.prefs_shortcuts)
        self.prefs_shortcuts_deletecmakecache_edit.setObjectName(u"prefs_shortcuts_deletecmakecache_edit")

        self.gridLayout_13.addWidget(self.prefs_shortcuts_deletecmakecache_edit, 14, 2, 1, 1)

        self.label_4 = QLabel(self.prefs_shortcuts)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_13.addWidget(self.label_4, 3, 0, 1, 1)

        self.prefs_shortcuts_cancel_edit = ShortcutLineEdit(self.prefs_shortcuts)
        self.prefs_shortcuts_cancel_edit.setObjectName(u"prefs_shortcuts_cancel_edit")

        self.gridLayout_13.addWidget(self.prefs_shortcuts_cancel_edit, 11, 2, 1, 1)

        self.label_21 = QLabel(self.prefs_shortcuts)
        self.label_21.setObjectName(u"label_21")

        self.gridLayout_13.addWidget(self.label_21, 7, 0, 1, 1)

        self.label_3 = QLabel(self.prefs_shortcuts)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_13.addWidget(self.label_3, 2, 0, 1, 1)

        self.label_28 = QLabel(self.prefs_shortcuts)
        self.label_28.setObjectName(u"label_28")

        self.gridLayout_13.addWidget(self.label_28, 14, 0, 1, 1)

        self.prefs_shortcuts_exportpackage_edit = ShortcutLineEdit(self.prefs_shortcuts)
        self.prefs_shortcuts_exportpackage_edit.setObjectName(u"prefs_shortcuts_exportpackage_edit")

        self.gridLayout_13.addWidget(self.prefs_shortcuts_exportpackage_edit, 8, 2, 1, 1)

        self.prefs_shortcuts_create_edit = ShortcutLineEdit(self.prefs_shortcuts)
        self.prefs_shortcuts_create_edit.setObjectName(u"prefs_shortcuts_create_edit")

        self.gridLayout_13.addWidget(self.prefs_shortcuts_create_edit, 0, 2, 1, 1)

        self.prefs_shortcuts_build_edit = ShortcutLineEdit(self.prefs_shortcuts)
        self.prefs_shortcuts_build_edit.setObjectName(u"prefs_shortcuts_build_edit")

        self.gridLayout_13.addWidget(self.prefs_shortcuts_build_edit, 6, 2, 1, 1)

        self.label_24 = QLabel(self.prefs_shortcuts)
        self.label_24.setObjectName(u"label_24")

        self.gridLayout_13.addWidget(self.label_24, 10, 0, 1, 1)

        self.prefs_shortcuts_imports_edit = ShortcutLineEdit(self.prefs_shortcuts)
        self.prefs_shortcuts_imports_edit.setObjectName(u"prefs_shortcuts_imports_edit")

        self.gridLayout_13.addWidget(self.prefs_shortcuts_imports_edit, 2, 2, 1, 1)

        self.label_32 = QLabel(self.prefs_shortcuts)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setTextFormat(Qt.RichText)
        self.label_32.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_13.addWidget(self.label_32, 1, 0, 1, 1)

        self.prefs_shortcuts_createupdates_edit = ShortcutLineEdit(self.prefs_shortcuts)
        self.prefs_shortcuts_createupdates_edit.setObjectName(u"prefs_shortcuts_createupdates_edit")

        self.gridLayout_13.addWidget(self.prefs_shortcuts_createupdates_edit, 1, 2, 1, 1)

        self.prefs_toolbox.addItem(self.prefs_shortcuts, u"Shortcuts")
        self.prefs_recipes = QWidget()
        self.prefs_recipes.setObjectName(u"prefs_recipes")
        self.prefs_recipes.setGeometry(QRect(0, 0, 98, 105))
        self.verticalLayout_7 = QVBoxLayout(self.prefs_recipes)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.prefs_recipes_table = QTableView(self.prefs_recipes)
        self.prefs_recipes_table.setObjectName(u"prefs_recipes_table")
        self.prefs_recipes_table.setContextMenuPolicy(Qt.CustomContextMenu)
        self.prefs_recipes_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.prefs_recipes_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.prefs_recipes_table.setAlternatingRowColors(True)
        self.prefs_recipes_table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.prefs_recipes_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.prefs_recipes_table.horizontalHeader().setStretchLastSection(True)
        self.prefs_recipes_table.verticalHeader().setVisible(False)

        self.verticalLayout_7.addWidget(self.prefs_recipes_table)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_9)

        self.prefs_toolbox.addItem(self.prefs_recipes, u"Recipes")
        self.prefs_recentconfigs = QWidget()
        self.prefs_recentconfigs.setObjectName(u"prefs_recentconfigs")
        self.prefs_recentconfigs.setGeometry(QRect(0, 0, 98, 105))
        self.verticalLayout_8 = QVBoxLayout(self.prefs_recentconfigs)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.prefs_recentconfigs_list = QListView(self.prefs_recentconfigs)
        self.prefs_recentconfigs_list.setObjectName(u"prefs_recentconfigs_list")
        self.prefs_recentconfigs_list.setContextMenuPolicy(Qt.CustomContextMenu)
        self.prefs_recentconfigs_list.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.prefs_recentconfigs_list.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.prefs_recentconfigs_list.setAlternatingRowColors(True)
        self.prefs_recentconfigs_list.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.verticalLayout_8.addWidget(self.prefs_recentconfigs_list)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_10)

        self.prefs_toolbox.addItem(self.prefs_recentconfigs, u"Recent configs")
        self.prefs_recentremotes = QWidget()
        self.prefs_recentremotes.setObjectName(u"prefs_recentremotes")
        self.prefs_recentremotes.setGeometry(QRect(0, 0, 98, 105))
        self.verticalLayout_9 = QVBoxLayout(self.prefs_recentremotes)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.prefs_recentremotes_list = QListView(self.prefs_recentremotes)
        self.prefs_recentremotes_list.setObjectName(u"prefs_recentremotes_list")
        self.prefs_recentremotes_list.setContextMenuPolicy(Qt.CustomContextMenu)
        self.prefs_recentremotes_list.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.prefs_recentremotes_list.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.prefs_recentremotes_list.setAlternatingRowColors(True)
        self.prefs_recentremotes_list.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.verticalLayout_9.addWidget(self.prefs_recentremotes_list)

        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_11)

        self.prefs_toolbox.addItem(self.prefs_recentremotes, u"Recent remotes")

        self.verticalLayout.addWidget(self.prefs_toolbox)

        self.prefs_buttons = QDialogButtonBox(PreferencesDialog)
        self.prefs_buttons.setObjectName(u"prefs_buttons")
        self.prefs_buttons.setOrientation(Qt.Horizontal)
        self.prefs_buttons.setStandardButtons(QDialogButtonBox.Apply|QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.prefs_buttons)


        self.retranslateUi(PreferencesDialog)
        self.prefs_buttons.accepted.connect(PreferencesDialog.accept)
        self.prefs_buttons.rejected.connect(PreferencesDialog.reject)

        self.prefs_toolbox.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(PreferencesDialog)
    # setupUi

    def retranslateUi(self, PreferencesDialog):
        PreferencesDialog.setWindowTitle(QCoreApplication.translate("PreferencesDialog", u"Preferences", None))
        self.actionForget_recipe.setText(QCoreApplication.translate("PreferencesDialog", u"Forget recipe", None))
        self.actionForget_config.setText(QCoreApplication.translate("PreferencesDialog", u"Forget config", None))
        self.actionForget_remote.setText(QCoreApplication.translate("PreferencesDialog", u"Forget remote", None))
        self.prefs_general_busy_colour.setText("")
        self.prefs_general_found_text_background_colour.setText("")
        self.prefs_general_usebatching.setText(QCoreApplication.translate("PreferencesDialog", u"Use batching for standard output", None))
        self.prefs_general_enable_wallclock.setText(QCoreApplication.translate("PreferencesDialog", u"Enable wall clock command timing", None))
        self.prefs_general_enable_compact.setText(QCoreApplication.translate("PreferencesDialog", u"Enable compact look", None))
        self.prefs_general_clearpanes.setText(QCoreApplication.translate("PreferencesDialog", u"Clear panes before running each command", None))
#if QT_CONFIG(tooltip)
        self.prefs_general_new_recipe_load.setToolTip(QCoreApplication.translate("PreferencesDialog", u"Enable new recipe loading behaviour.\n"
"May help loading recipes that query version information during requirements() methods.\n"
"However, help stop loading recipes if they have mixed versions of dependent packages in their dependency graph or mixed case names of dependent packages on case insensitive file systems.\n"
"", None))
#endif // QT_CONFIG(tooltip)
        self.prefs_general_new_recipe_load.setText(QCoreApplication.translate("PreferencesDialog", u"New recipe loading behaviour", None))
        self.label_2.setText(QCoreApplication.translate("PreferencesDialog", u"Busy icon colour", None))
        self.label.setText(QCoreApplication.translate("PreferencesDialog", u"Default recipe browsing directory", None))
        self.prefs_general_combine_panes.setText(QCoreApplication.translate("PreferencesDialog", u"Combine output and error panes", None))
        self.label_30.setText(QCoreApplication.translate("PreferencesDialog", u"Found text background colour", None))
#if QT_CONFIG(tooltip)
        self.prefs_general_enable_darkmode.setToolTip(QCoreApplication.translate("PreferencesDialog", u"Dark mode toggles immediately,  but existing Conan output will not change", None))
#endif // QT_CONFIG(tooltip)
        self.prefs_general_enable_darkmode.setText(QCoreApplication.translate("PreferencesDialog", u"Enable dark mode", None))
        self.label_31.setText(QCoreApplication.translate("PreferencesDialog", u"Recipe editor", None))
        self.prefs_toolbox.setItemText(self.prefs_toolbox.indexOf(self.prefs_general), QCoreApplication.translate("PreferencesDialog", u"General", None))
        self.groupBox.setTitle(QCoreApplication.translate("PreferencesDialog", u"UI font", None))
        self.prefs_font_ui_label.setText(QCoreApplication.translate("PreferencesDialog", u"The font", None))
        self.prefs_font_ui_preview.setText(QCoreApplication.translate("PreferencesDialog", u"The quick brown fox jumps over the lazy dog", None))
        self.prefs_font_ui_reset.setText(QCoreApplication.translate("PreferencesDialog", u"Reset", None))
        self.prefs_font_ui_change.setText(QCoreApplication.translate("PreferencesDialog", u"Change ...", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("PreferencesDialog", u"Output panes font", None))
        self.prefs_font_output_label.setText(QCoreApplication.translate("PreferencesDialog", u"The font", None))
        self.prefs_font_output_preview.setText(QCoreApplication.translate("PreferencesDialog", u"The quick brown fox jumps over the lazy dog", None))
        self.prefs_font_output_reset.setText(QCoreApplication.translate("PreferencesDialog", u"Reset", None))
        self.prefs_font_output_change.setText(QCoreApplication.translate("PreferencesDialog", u"Change ...", None))
        self.prefs_toolbox.setItemText(self.prefs_toolbox.indexOf(self.prefs_fonts), QCoreApplication.translate("PreferencesDialog", u"Fonts", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("PreferencesDialog", u"Logging", None))
        self.label_7.setText(QCoreApplication.translate("PreferencesDialog", u"Conan logging level", None))
        self.prefs_conan_log_level.setItemText(0, QCoreApplication.translate("PreferencesDialog", u"CRITICAL", None))
        self.prefs_conan_log_level.setItemText(1, QCoreApplication.translate("PreferencesDialog", u"ERROR", None))
        self.prefs_conan_log_level.setItemText(2, QCoreApplication.translate("PreferencesDialog", u"WARNING", None))
        self.prefs_conan_log_level.setItemText(3, QCoreApplication.translate("PreferencesDialog", u"INFO", None))
        self.prefs_conan_log_level.setItemText(4, QCoreApplication.translate("PreferencesDialog", u"DEBUG", None))
        self.prefs_conan_log_level.setItemText(5, QCoreApplication.translate("PreferencesDialog", u"NOTSET", None))

#if QT_CONFIG(tooltip)
        self.prefs_conan_log_level.setToolTip(QCoreApplication.translate("PreferencesDialog", u"Log Conan commands. Only works when a single recipe has commands run on it", None))
#endif // QT_CONFIG(tooltip)
        self.groupBox_4.setTitle(QCoreApplication.translate("PreferencesDialog", u"Parsing conandata", None))
        self.label_8.setText(QCoreApplication.translate("PreferencesDialog", u"YAML path segments to identify version list", None))
#if QT_CONFIG(tooltip)
        self.prefs_conan_version_list_path_segment.setToolTip(QCoreApplication.translate("PreferencesDialog", u"<html><head/><body><p>For example, if your conandata.yml is formatted as</p><p><br/></p><p>  sources:</p><p>    1.2.3:</p><p>    ... </p><p>    4.5.6:</p><p>    ... </p><p><br/></p><p>then specify 'sources' in order to extract the version list</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.prefs_toolbox.setItemText(self.prefs_toolbox.indexOf(self.prefs_conan), QCoreApplication.translate("PreferencesDialog", u"Conan", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("PreferencesDialog", u"New cache options", None))
        self.label_9.setText(QCoreApplication.translate("PreferencesDialog", u"Config to install", None))
        self.label_10.setText(QCoreApplication.translate("PreferencesDialog", u"Git branch", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("PreferencesDialog", u"Forget caches without recipe associations", None))
        self.prefs_localcache_do_forget.setText(QCoreApplication.translate("PreferencesDialog", u"Forget", None))
        self.prefs_toolbox.setItemText(self.prefs_toolbox.indexOf(self.prefs_localcache), QCoreApplication.translate("PreferencesDialog", u"Local cache", None))
        self.label_11.setText(QCoreApplication.translate("PreferencesDialog", u"GraphViz bin directory", None))
        self.label_29.setText(QCoreApplication.translate("PreferencesDialog", u"<html><head/><body><p>Download from <a href=\"https://graphviz.org/download/\"><span style=\" text-decoration: underline; color:#0068da;\">https://graphviz.org/download/</span></a></p></body></html>", None))
        self.prefs_toolbox.setItemText(self.prefs_toolbox.indexOf(self.prefs_graphviz), QCoreApplication.translate("PreferencesDialog", u"GraphViz", None))
        self.label_12.setText(QCoreApplication.translate("PreferencesDialog", u"CMake bin directory", None))
        self.label_13.setText(QCoreApplication.translate("PreferencesDialog", u"Ninja bin directory", None))
        self.prefs_toolbox.setItemText(self.prefs_toolbox.indexOf(self.prefs_cmake), QCoreApplication.translate("PreferencesDialog", u"CMake", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("PreferencesDialog", u"Default compiler cache", None))
        self.prefs_compilercache_default.setItemText(0, QCoreApplication.translate("PreferencesDialog", u"None", None))
        self.prefs_compilercache_default.setItemText(1, QCoreApplication.translate("PreferencesDialog", u"ccache", None))
        self.prefs_compilercache_default.setItemText(2, QCoreApplication.translate("PreferencesDialog", u"sccache", None))
        self.prefs_compilercache_default.setItemText(3, QCoreApplication.translate("PreferencesDialog", u"buildcache", None))

#if QT_CONFIG(tooltip)
        self.prefs_compilercache_default.setToolTip(QCoreApplication.translate("PreferencesDialog", u"The default compiler cache that attempts to integrate with Conan's CMake and Autotools helpers. YMMV.", None))
#endif // QT_CONFIG(tooltip)
        self.groupBox_8.setTitle(QCoreApplication.translate("PreferencesDialog", u"ccache", None))
        self.label_15.setText(QCoreApplication.translate("PreferencesDialog", u"Location", None))
        self.label_14.setText(QCoreApplication.translate("PreferencesDialog", u"<html><head/><body><p>Download from <a href=\"https://ccache.dev\"><span style=\" text-decoration: underline; color:#0068da;\">https://ccache.dev</span></a></p></body></html>", None))
        self.groupBox_9.setTitle(QCoreApplication.translate("PreferencesDialog", u"sccache", None))
        self.label_17.setText(QCoreApplication.translate("PreferencesDialog", u"Location", None))
        self.label_16.setText(QCoreApplication.translate("PreferencesDialog", u"<html><head/><body><p>Download from <a href=\"https://github.com/mozilla/sccache\"><span style=\" text-decoration: underline; color:#0068da;\">https://github.com/mozilla/sccache</span></a></p></body></html>", None))
        self.groupBox_10.setTitle(QCoreApplication.translate("PreferencesDialog", u"buildcache", None))
        self.label_19.setText(QCoreApplication.translate("PreferencesDialog", u"Location", None))
        self.label_18.setText(QCoreApplication.translate("PreferencesDialog", u"<html><head/><body><p>Download from <a href=\"https://github.com/mbitsnbites/buildcache\"><span style=\" text-decoration: underline; color:#0068da;\">https://github.com/mbitsnbites/buildcache</span></a></p></body></html>", None))
        self.prefs_toolbox.setItemText(self.prefs_toolbox.indexOf(self.prefs_compilercache), QCoreApplication.translate("PreferencesDialog", u"Compiler cache", None))
        self.label_23.setText(QCoreApplication.translate("PreferencesDialog", u"<html><head/><body><p align=\"right\"><img src=\":/testpackage.svg\" width=\"20\" height=\"20\"/> conan test</p></body></html>", None))
        self.label_20.setText(QCoreApplication.translate("PreferencesDialog", u"<html><head/><body><p align=\"right\"><img src=\":/build.svg\" width=\"20\" height=\"20\"/> conan build</p></body></html>", None))
        self.label_1.setText(QCoreApplication.translate("PreferencesDialog", u"<html><head/><body><p align=\"right\"><img src=\":/create.svg\" width=\"20\" height=\"20\"/> conan create</p></body></html>", None))
        self.label_25.setText(QCoreApplication.translate("PreferencesDialog", u"<html><head/><body><p align=\"right\"><img src=\":/cancel.svg\" width=\"20\" height=\"20\"/> Cancel current command</p></body></html>", None))
        self.label_22.setText(QCoreApplication.translate("PreferencesDialog", u"<html><head/><body><p align=\"right\"><img src=\":/exportpackage.svg\" width=\"20\" height=\"20\"/> conan export-pkg</p></body></html>", None))
        self.label_26.setText(QCoreApplication.translate("PreferencesDialog", u"<html><head/><body><p align=\"right\"><img src=\":/cmakebuildtool.svg\" width=\"20\" height=\"20\"/> CMake Build Tool</p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("PreferencesDialog", u"<html><head/><body><p align=\"right\"><img src=\":/install.svg\" width=\"20\" height=\"20\"/> conan install (update binaries)</p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("PreferencesDialog", u"<html><head/><body><p align=\"right\"><img src=\":/source.svg\" width=\"20\" height=\"20\"/> conan source</p></body></html>", None))
        self.label_27.setText(QCoreApplication.translate("PreferencesDialog", u"<html><head/><body><p align=\"right\"><img src=\":/cmakebuildtoolverbose.svg\" width=\"20\" height=\"20\"/> CMake Build Tool (verbose)</p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("PreferencesDialog", u"<html><head/><body><p align=\"right\"><img src=\":/install.svg\" width=\"20\" height=\"20\"/> conan install</p></body></html>", None))
        self.label_21.setText(QCoreApplication.translate("PreferencesDialog", u"<html><head/><body><p align=\"right\"><img src=\":/package.svg\" width=\"20\" height=\"20\"/> conan package</p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("PreferencesDialog", u"<html><head/><body><p align=\"right\"><img src=\":/imports.svg\" width=\"20\" height=\"20\"/> conan imports</p></body></html>", None))
        self.label_28.setText(QCoreApplication.translate("PreferencesDialog", u"<html><head/><body><p align=\"right\"><img src=\":/removecmakecache.svg\" width=\"20\" height=\"20\"/> Delete CMakeCache</p></body></html>", None))
        self.label_24.setText(QCoreApplication.translate("PreferencesDialog", u"<html><head/><body><p align=\"right\"><img src=\":/removepackage.svg\" width=\"20\" height=\"20\"/> conan remove</p></body></html>", None))
        self.label_32.setText(QCoreApplication.translate("PreferencesDialog", u"<html><head/><body><p align=\"right\"><img src=\":/create.svg\" width=\"20\" height=\"20\"/> conan create (update binaries)</p></body></html>", None))
        self.prefs_toolbox.setItemText(self.prefs_toolbox.indexOf(self.prefs_shortcuts), QCoreApplication.translate("PreferencesDialog", u"Shortcuts", None))
        self.prefs_toolbox.setItemText(self.prefs_toolbox.indexOf(self.prefs_recipes), QCoreApplication.translate("PreferencesDialog", u"Recipes", None))
        self.prefs_toolbox.setItemText(self.prefs_toolbox.indexOf(self.prefs_recentconfigs), QCoreApplication.translate("PreferencesDialog", u"Recent configs", None))
        self.prefs_toolbox.setItemText(self.prefs_toolbox.indexOf(self.prefs_recentremotes), QCoreApplication.translate("PreferencesDialog", u"Recent remotes", None))
    # retranslateUi

