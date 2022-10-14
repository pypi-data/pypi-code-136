from kabaret.app.ui.gui.widgets.flow.flow_view import QtWidgets, QtCore, QtGui
from kabaret.app.ui.gui.widgets.flow.flow_field import ObjectActionMenuManager
from kabaret.app import resources

from ...resources.icons import libreflow as _

from .qmodel import QFileListModel
from .delegate import QFileListDelegate


class QCustomMenu(QtWidgets.QMenu):

    def __init__(self, title, parent):
        super(QCustomMenu, self).__init__(title)
        self.parent = parent

    def event(self, event):
        if event.type() == QtCore.QEvent.Show:
            self.move(self.parent.mapToGlobal(QtCore.QPoint(0,0)) + QtCore.QPoint(self.parent.width() - self.width(), self.parent.height()))
        
        return super(QCustomMenu, self).event(event)


class FileActionsButton(QtWidgets.QToolButton):
    """
    Holds the file's action shortcuts displayed in the file list.
    """
    def __init__(self, flow_page, file_type, row, action_manager, controller):
        super(FileActionsButton, self).__init__()
        self.controller = controller
        self.action_manager = action_manager
        self.file_type = file_type
        self.row = row
        self.flow_page = flow_page
        self.build()
    
    def build(self):
        self.setIcon(resources.get_icon(('icons.gui', 'menu')))
        self.setIconSize(QtCore.QSize(16, 16))
        self.setStyleSheet('QToolButton::menu-indicator { image: none; }')
        self.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        self.setFixedWidth(30)

        # Add actions
        self.menu = QCustomMenu('File actions', self)
        self.setPopupMode(QtWidgets.QToolButton.InstantPopup)
        self.setArrowType(QtCore.Qt.NoArrow)
        self.setMenu(self.menu)
    
    def mousePressEvent(self, event):
        data = self.controller.file_data(self.file_type, self.row)
        data.update_actions()

        self.action_manager.update_oid_menu(
            data.oid, self.menu, with_submenus=True
        )
        super(FileActionsButton, self).mousePressEvent(event)

    def _on_action_menu_triggered(self, action):
        self.flow_page.show_action_dialog(action.oid)


class FileListItemWidget(QtWidgets.QWidget):
    """
    Represents a file in a list.
    """
    def __init__(self, flow_page, file_type, row, action_manager, controller):
        super(FileListItemWidget, self).__init__()
        self.controller = controller
        self.action_manager = action_manager
        self.file_type = file_type
        self.row = row
        self.flow_page = flow_page
        self.build()
    
    def build(self):
        self.button_secondary = FileActionsButton(self.flow_page, self.file_type, self.row, self.action_manager, self.controller)
        self.button_secondary.setFixedWidth(30)
        self.button_secondary.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)

        self.buttons_main = []
        data = self.controller.file_data(self.file_type, self.row)
        data.update_actions()

        for fa in data.main_actions:
            b = QtWidgets.QPushButton('')
            b.setIcon(resources.get_icon(fa.icon))
            b.setToolTip(fa.label)
            b.setFixedWidth(30)
            b.setStyleSheet('background-color: rgba(255, 255, 255, 0);')
            b.clicked.connect(lambda checked=False, a=fa: self._on_action_menu_triggered(a))
            self.buttons_main.append(b)
        
        hlo = QtWidgets.QHBoxLayout()
        hlo.addStretch(1)

        for b in self.buttons_main:
            hlo.addWidget(b)
        
        hlo.addWidget(self.button_secondary)
        hlo.setSpacing(0)
        hlo.setMargin(0)
        self.setLayout(hlo)

    def _on_action_menu_triggered(self, action):
        self.flow_page.show_action_dialog(action.oid)


class FileList(QtWidgets.QTableView):
    """
    Represents a list of files of a given type (input, output, work) present in a task.
    """
    def __init__(self, task_widget, file_type):
        super(FileList, self).__init__()
        self.controller = task_widget.controller
        self.file_type = file_type
        
        self.model = QFileListModel(self.controller, file_type)
        self.setModel(self.model)
        self.setItemDelegate(QFileListDelegate())
        self.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.verticalHeader().hide()
        self.horizontalHeader().setStretchLastSection(True)
        self.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)

        self.action_manager = ObjectActionMenuManager(
            task_widget.session, task_widget.page.show_action_dialog, 'Flow.map'
        )
        self.action_menu = QtWidgets.QMenu()

        for row in range(self.model.rowCount()):
            self.setIndexWidget(
                self.model.index(row, 0),
                FileListItemWidget(task_widget.page, self.file_type, row, self.action_manager, self.controller)
            )

        self.customContextMenuRequested.connect(self._on_context_menu_requested)
        self.doubleClicked.connect(self._on_item_double_clicked)
    
    def selectionChanged(self, selected, deselected):
        if selected.indexes():
            index = selected.indexes()[0]
            self.controller.update_selected(self.file_type, index.row())
    
    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.RightButton:
            self.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
            self.customContextMenuRequested.emit(event.pos())
            self.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        else:
            super(FileList, self).mousePressEvent(event)
            
            if event.button() == QtCore.Qt.LeftButton:
                if not self.indexAt(event.pos()).isValid():
                    self.controller.clear_selected()
    
    def _on_context_menu_requested(self, pos):
        index = self.indexAt(pos)
        if not index.isValid():
            return
        
        data = self.controller.file_data(self.file_type, index.row())
        actions = self.action_manager.update_oid_menu(
            data.oid, self.action_menu, with_submenus=True
        )

        if actions:
            self.action_menu.exec_(self.viewport().mapToGlobal(pos))
    
    def _on_item_double_clicked(self, index):
        data = self.controller.file_data(self.file_type, index.row())
        
        if data.activate_oid is None:
            self.controller.goto(data.oid)
        else:
            self.controller.show_action_dialog(data.activate_oid)


class FileListsWidget(QtWidgets.QWidget):
    """
    Displays the task's input, output and working files.
    """
    def __init__(self, task_widget, parent):
        super(FileListsWidget, self).__init__(parent)
        self.task_widget = task_widget
        self.file_lists = {}
        self.build()
    
    def build(self):
        self.file_lists['Inputs'] = FileList(self.task_widget, 'Inputs')
        self.file_lists['Works'] = FileList(self.task_widget, 'Works')
        self.file_lists['Outputs'] = FileList(self.task_widget, 'Outputs')

        hlo = QtWidgets.QHBoxLayout()
        hlo.addWidget(self.file_lists['Inputs'])
        hlo.addWidget(self.file_lists['Works'])
        hlo.addWidget(self.file_lists['Outputs'])
        hlo.setSpacing(2)
        hlo.setMargin(0)
        self.setLayout(hlo)
    
    def clear_list_selection(self, file_type):
        self.file_lists[file_type].clearSelection()
    
    def clear_selection(self):
        for l in self.file_lists.values():
            l.clearSelection()
