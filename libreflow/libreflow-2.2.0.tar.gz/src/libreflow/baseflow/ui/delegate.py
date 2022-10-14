import datetime
from kabaret.app.ui.gui.widgets.flow.flow_view import QtWidgets, QtCore, QtGui
from kabaret.app import resources


FILE_CELL_MARGIN = 2
FILE_ICON_MARGIN = 5
PIXMAP_BY_STATUS = {
    'Available': resources.get_pixmap('icons.libreflow', 'checked-symbol-colored'),
    'Requested': resources.get_pixmap('icons.libreflow', 'waiting')
}


class QFileListDelegate(QtWidgets.QStyledItemDelegate):
    """
    Defines a delegate responsible for displaying file list entries.
    """

    def __init__(self, parent=None):
        super(QFileListDelegate, self).__init__(parent)

        self.font = QtGui.QFont()
        self.metrics = QtGui.QFontMetrics(self.font)
    
    def paint(self, painter, option, index):
        data = index.data(QtCore.Qt.UserRole)

        # Define draw areas
        orig_brush = painter.brush()
        orig_pen = painter.pen()
        rect_text = option.rect

        if option.state & QtWidgets.QStyle.State_Selected:
            painter.setBrush(QtGui.QColor('#004444'))
            painter.setPen(QtGui.QColor('#004444'))
            painter.drawRect(rect_text)
        
        rect_icon = QtCore.QRect(
            option.rect.left() + FILE_ICON_MARGIN,
            option.rect.top() + FILE_ICON_MARGIN,
            option.rect.height() - 2*FILE_ICON_MARGIN,
            option.rect.height() - 2*FILE_ICON_MARGIN
        )
        pixmap = resources.get_pixmap(*data.icon)
        pixmap = pixmap.scaled(
            rect_icon.size(),
            QtCore.Qt.KeepAspectRatio,
            QtCore.Qt.SmoothTransformation
        )
        painter.drawPixmap(rect_icon, pixmap)

        rect_text.setLeft(rect_text.left() + rect_icon.width() + 2*FILE_ICON_MARGIN)
        
        painter.setBrush(orig_brush)
        painter.setPen(orig_pen)
        painter.drawText(
            rect_text,
            QtCore.Qt.AlignVCenter,
            data.label
        )


class QFileHistoryDelegate(QtWidgets.QStyledItemDelegate):
    """
    Defines a delegate responsible for displaying file revision data.
    """

    def __init__(self, parent=None):
        super(QFileHistoryDelegate, self).__init__(parent)

        self.font = QtGui.QFont()
        self.metrics = QtGui.QFontMetrics(self.font)
    
    def paint(self, painter, option, index):
        data = index.data(QtCore.Qt.UserRole)
        draw_rect = option.rect
        orig_brush = painter.brush()
        orig_pen = painter.pen()

        if option.state & QtWidgets.QStyle.State_Selected:
            painter.setBrush(QtGui.QColor('#004444'))
            painter.setPen(QtGui.QColor('#004444'))
            painter.drawRect(draw_rect)
        
        painter.setBrush(orig_brush)
        painter.setPen(orig_pen)

        if index.column() == 3:
            data = datetime.datetime.fromtimestamp(data).strftime('%y-%m-%d %H:%M')
        if index.column() == 2:
            alignment = QtCore.Qt.AlignLeft
            draw_rect.setLeft(draw_rect.left() + 10)
        else:
            alignment = QtCore.Qt.AlignHCenter
        
        painter.drawText(
            draw_rect,
            QtCore.Qt.AlignVCenter | alignment,
            data
        )


class QFileStatutesDelegate(QtWidgets.QStyledItemDelegate):
    """
    Defines a delegate responsible for displaying file revision synchronisation statutes.
    """

    def __init__(self, parent=None):
        super(QFileStatutesDelegate, self).__init__(parent)

        self.font = QtGui.QFont()
        self.metrics = QtGui.QFontMetrics(self.font)
    
    def paint(self, painter, option, index):
        data = index.data(QtCore.Qt.UserRole)
        draw_rect = option.rect
        orig_brush = painter.brush()
        orig_pen = painter.pen()

        if option.state & QtWidgets.QStyle.State_Selected:
            painter.setBrush(QtGui.QColor('#004444'))
            painter.setPen(QtGui.QColor('#004444'))
            painter.drawRect(draw_rect)
        
        painter.setBrush(orig_brush)
        painter.setPen(orig_pen)

        if index.column() == 0:
            painter.drawText(
                draw_rect,
                QtCore.Qt.AlignCenter,
                data
            )
        else:
            pixmap = PIXMAP_BY_STATUS.get(data)

            if pixmap is not None:
                pixmap = pixmap.scaled(
                    draw_rect.size() - QtCore.QSize(4, 4),
                    QtCore.Qt.KeepAspectRatio,
                    QtCore.Qt.SmoothTransformation)
                x = draw_rect.center().x() - round(0.5 * pixmap.rect().width())
                y = draw_rect.center().y() - round(0.5 * pixmap.rect().height())
                
                painter.drawPixmap(
                    QtCore.QRect(x, y, pixmap.rect().width(), pixmap.rect().height()),
                    pixmap
                )
