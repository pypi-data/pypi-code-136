from kabaret.app.ui.gui.widgets.flow.flow_view import QtWidgets, QtCore, QtGui
from kabaret.app.ui.gui.widgets.flow.flow_field import ObjectActionMenuManager
from kabaret.app import resources

from ...resources.icons import gui as _

from .qmodel import QFileHistoryModel, QFileStatutesModel
from .delegate import QFileHistoryDelegate, QFileStatutesDelegate


class RevisionStatutesButton(QtWidgets.QPushButton):

    def __init__(self):
        super(RevisionStatutesButton, self).__init__('')
        icon = QtGui.QIcon()
        icon.addFile(
            resources.get('icons.gui', 'location-worldwide'),
            # size=QtCore.QSize(30, 30),
            state=QtGui.QIcon.On)
        icon.addFile(
            resources.get('icons.gui', 'location-worldwide-disabled'),
            # size=QtCore.QSize(30, 30),
            state=QtGui.QIcon.Off)
        self.setIcon(icon)
        self.setIconSize(QtCore.QSize(25, 25))
        self.setCheckable(True)
        self.setToolTip('Show/hide file locations')
        self.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        self.setFixedWidth(40)


class FileHeader(QtWidgets.QWidget):

    def __init__(self, file_widget):
        super(FileHeader, self).__init__()
        self.file_widget = file_widget
        self.controller = file_widget.controller
        self.build()
    
    def build(self):
        self.label_icon = QtWidgets.QLabel('')
        self.label_icon.setFixedWidth(40)
        self.label_icon.setAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setWeight(QtGui.QFont.Bold)
        self.label_name = QtWidgets.QLabel('')
        self.label_name.setFont(font)
        self.label_name.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.button_statutes = RevisionStatutesButton()
        
        hlo = QtWidgets.QHBoxLayout()
        hlo.addWidget(self.label_icon)
        hlo.addWidget(self.label_name)
        hlo.addStretch(1)
        hlo.addWidget(self.button_statutes)
        hlo.setMargin(0)
        hlo.setSpacing(2)
        self.setLayout(hlo)

        pal = QtGui.QPalette()
        pal.setColor(QtGui.QPalette.Window, QtGui.QColor('#303233'))
        self.setAutoFillBackground(True)
        self.setPalette(pal)

        self.setFixedHeight(40)

        self.button_statutes.toggled.connect(self._on_button_statutes_toggled)
    
    def update(self):
        selected = self.controller.selected_file()
        pm = resources.get_pixmap(*selected.icon)
        self.label_icon.setPixmap(pm.scaled(28, 28, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation))
        self.label_name.setText(selected.label)
    
    def toggle_file_statutes(self):
        self.button_statutes.setChecked(
            not self.button_statutes.isChecked()
        )
    
    def _on_button_statutes_toggled(self, checked):
        self.file_widget.set_show_statutes(checked)


class FileHistoryView(QtWidgets.QTableView):
    """
    Represents the revision history of the active file.
    """
    def __init__(self, controller):
        super(FileHistoryView, self).__init__()
        self.controller = controller

        self.model_history = QFileHistoryModel(controller)
        self.model_statutes = QFileStatutesModel(controller)
        self.model = self.model_history
        # self.model = self.model_statutes
        self.delegate_history = QFileHistoryDelegate()
        self.delegate_statutes = QFileStatutesDelegate()
        self.delegate = self.delegate_history
        # self.delegate = self.delegate_statutes
        self.setModel(self.model)
        self.setItemDelegate(self.delegate)
        self.verticalHeader().hide()
        self.horizontalHeader().setMinimumSectionSize(100)
        self.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        self.horizontalHeader().setSectionResizeMode(3, QtWidgets.QHeaderView.Fixed)
        self.setColumnWidth(0, 100)
        self.setColumnWidth(1, 100)
        self.setColumnWidth(3, 100)
        self.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)

        self.action_manager = ObjectActionMenuManager(
            controller.session, controller.show_action_dialog, 'Flow.map'
        )
        self.action_menu = QtWidgets.QMenu()

        self.customContextMenuRequested.connect(self._on_context_menu_requested)
    
    def set_show_statutes(self, checked):
        if checked:
            self.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
            self.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.Fixed)
            self.setColumnWidth(0, 100)
            self.model = self.model_statutes
            self.delegate = self.delegate_statutes
        else:
            self.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Fixed)
            self.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
            self.setColumnWidth(0, 100)
            self.setColumnWidth(1, 100)
            self.setColumnWidth(3, 100)
            self.model = self.model_history
            self.delegate = self.delegate_history

        # self.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        # self.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.setModel(self.model)
        self.setItemDelegate(self.delegate)
    
    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.RightButton:
            self.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
            self.customContextMenuRequested.emit(event.pos())
            self.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        else:
            super(FileHistoryView, self).mousePressEvent(event)
    
    def _on_context_menu_requested(self, pos):
        index = self.indexAt(pos)
        if not index.isValid():
            return
        
        selected = self.selectionModel().selectedRows(0)

        if len(selected) > 1:
            oids = []
            for i in selected:
                data = self.controller.selected_file_revision_data(i.row())
                oids.append(data.oid)
            
            actions = self.action_manager.update_oids_menu(
                oids, self.action_menu, with_submenus=True
            )
        else:
            # Select right-clicked item
            self.selectionModel().select(
                index, QtCore.QItemSelectionModel.ClearAndSelect | QtCore.QItemSelectionModel.Rows
            )

            data = self.controller.selected_file_revision_data(index.row())
            actions = self.action_manager.update_oid_menu(
                data.oid, self.action_menu, with_submenus=True
            )

        if actions:
            self.action_menu.exec_(self.viewport().mapToGlobal(pos))


class FileStatutesView(QtWidgets.QTableView):
    """
    Represents the synchronisation statutes of the active file.
    """
    pass


class FileContent(QtWidgets.QWidget):

    def __init__(self, controller):
        super(FileContent, self).__init__()
        self.controller = controller
        self.build()
    
    def build(self):
        self.history_view = FileHistoryView(self.controller)
        hlo = QtWidgets.QVBoxLayout()
        hlo.addWidget(self.history_view)
        hlo.setSpacing(0)
        hlo.setMargin(0)
        self.setLayout(hlo)
    
    def update(self):
        pass


class FileWidget(QtWidgets.QWidget):
    """
    Displays the content of the task's selected file.
    """
    
    def __init__(self, task_widget, parent):
        super(FileWidget, self).__init__(parent)
        self.controller = task_widget.controller
        self.build()
    
    def build(self):
        self.header = FileHeader(self)
        self.content = FileContent(self.controller)
        vlo = QtWidgets.QVBoxLayout()
        vlo.addWidget(self.header)
        vlo.addWidget(self.content)
        vlo.setSpacing(0)
        vlo.setMargin(0)
        self.setLayout(vlo)
    
    def update(self):
        self.header.update()
        self.content.update()
    
    def beginResetHistoryModel(self):
        self.content.history_view.model.beginResetModel()

    def endResetHistoryModel(self):
        self.content.history_view.model.endResetModel()
    
    def set_show_statutes(self, b):
        self.content.history_view.set_show_statutes(b)
    
    def toggle_file_statutes(self):
        self.header.toggle_file_statutes()
