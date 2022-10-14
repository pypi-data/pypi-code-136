from kabaret.app.ui.gui.widgets.flow.flow_view import QtWidgets, QtCore, QtGui


class QFileListModel(QtCore.QAbstractTableModel):
    
    def __init__(self, controller, file_type, parent=None):
        super(QFileListModel, self).__init__(parent)
        self.controller = controller
        self.file_type = file_type

    def rowCount(self, parent=None):
        return self.controller.task_file_count(self.file_type)
        # return 12

    def columnCount(self, parent=None):
        return 1
    
    def headerData(self, section, orientation, role):
        if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return self.file_type
        
        return None

    def data(self, index, role):
        # name = self.controller.file_display_name(index.column())
        if role == QtCore.Qt.UserRole:
            data = self.controller.file_data(self.file_type, index.row())
            # print(index.row(), role)
            return data
            # return 'file.txt'
    
    # def dataChanged(self, topLeft, bottomRight, roles):
    #     print('data changed')
    #     super(QFileListModel, self).dataChanged(topLeft, bottomRight, roles)
    
    def flags(self, index):
        return QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable


class QFileHistoryModel(QtCore.QAbstractTableModel):

    def __init__(self, controller, parent=None):
        super(QFileHistoryModel, self).__init__(parent)
        self.controller = controller
    
    def rowCount(self, parent=None):
        return self.controller.selected_file_revision_count()

    def columnCount(self, parent=None):
        return 4
    
    def headerData(self, section, orientation, role):
        if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return self.controller.file_history_header(section)
        
        return None

    def data(self, index, role):
        # name = self.controller.file_display_name(index.column())
        if role == QtCore.Qt.UserRole:
            data = self.controller.selected_file_revision_data(
                index.row(), index.column()
            )
            # print(index.row(), role)
            return data
            # return 'file.txt'
    
    # def dataChanged(self, topLeft, bottomRight, roles):
    #     print('data changed')
    #     super(QFileListModel, self).dataChanged(topLeft, bottomRight, roles)
    
    def flags(self, index):
        return QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable


class QFileStatutesModel(QtCore.QAbstractTableModel):

    def __init__(self, controller, parent=None):
        super(QFileStatutesModel, self).__init__(parent)
        self.controller = controller
    
    def rowCount(self, parent=None):
        return self.controller.selected_file_revision_count()

    def columnCount(self, parent=None):
        return self.controller.site_count()
    
    def headerData(self, section, orientation, role):
        if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return self.controller.file_statutes_header(section)
        
        return None

    def data(self, index, role):
        if role == QtCore.Qt.UserRole:
            data = self.controller.selected_file_revision_status(
                index.row(), index.column(), 
            )
            return data
    
    def flags(self, index):
        return QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable
