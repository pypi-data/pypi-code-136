from PyQt5 import QtWidgets, QtCore, QtGui
import sys

# Coded by Xenely

pentype = {
    "solid": QtCore.Qt.SolidLine,
    "dash": QtCore.Qt.DashLine,
    "dot": QtCore.Qt.DotLine,
    "dashdot": QtCore.Qt.DashDotLine,
    "dashdotdot": QtCore.Qt.DashDotDotLine
}

brushtype = {
    "solid": QtCore.Qt.SolidPattern,
    "dense1": QtCore.Qt.Dense1Pattern,
    "dense2": QtCore.Qt.Dense2Pattern,
    "dense3": QtCore.Qt.Dense3Pattern,
    "dense4": QtCore.Qt.Dense4Pattern,
    "dense5": QtCore.Qt.Dense5Pattern,
    "dense6": QtCore.Qt.Dense6Pattern,
    "dense7": QtCore.Qt.Dense7Pattern,
    "hor": QtCore.Qt.HorPattern,
    "ver": QtCore.Qt.VerPattern,
    "cross": QtCore.Qt.CrossPattern,
    "bdiag": QtCore.Qt.BDiagPattern,
    "fdiag": QtCore.Qt.FDiagPattern,
    "diagcross": QtCore.Qt.DiagCrossPattern,
    "nobrush": QtCore.Qt.NoBrush

}

alignment = {
    "left": QtCore.Qt.AlignLeft,
    "center": QtCore.Qt.AlignCenter,
    "right": QtCore.Qt.AlignRight
}


class OverlayFont:

    def __init__(self, font_family: str, size: int) -> None:

        self.font_family = font_family
        self.size = size

        self.font = QtGui.QFont()
        self.font.setFamily(font_family)
        self.font.setPixelSize(size)

    def set_family(self, font_family: str) -> None:

        self.font.setFamily(font_family)

    def set_size(self, size: int) -> None:

        self.font.setPixelSize(size)


class Overlay(QtWidgets.QWidget):
    """Базовый класс Qt оверлея.

    Basic class of Qt overlay.

    >>> from pyextoverlay import *
    >>> # Qt требует создания объекта application и его дальнейшего запуска.
    >>> # Qt reqire create of application object and running it.
    >>> application = application_init()
    >>> # Создаем оверлей, делаем оверлей в полный экран и отображаем его.
    >>> # Create overlay, make overlay fullscreen and show it.
    >>> overlay = Overlay(update_interval_ms=20)
    >>> overlay.showFullScreen()
    >>> ovelay.show()
    >>>
    >>> # Здесь создаем ф-ию в отдельном потоке, которя будет менять содержимое overlay.draw_stack()
    >>> # Here we can make a function in thread that will change content of overlay.draw_start()
    >>>
    >>> # Запускаем оверлей.
    >>> # Overlay start.
    >>> application_start(application)
    """

    def __init__(self, update_interval_ms: int) -> None:

        QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_DisableHighDpiScaling)

        super().__init__()

        # Set up transparency
        self.setWindowFlags(QtCore.Qt.Tool | QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint | QtCore.Qt.WindowTransparentForInput)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # Init some stuffs
        self.draw_stack = []
        self.geometry_stack = []
        self.is_hidden = False
        self.__overlay_painter = QtGui.QPainter()

        # Timer (necessary for update and triggering paintEvent)
        self.__timer = QtCore.QTimer(self)
        self.__timer.setInterval(update_interval_ms)
        self.__timer.timeout.connect(lambda: self.update())
        self.__timer.start()

    def paintEvent(self, event: object) -> None:

        self.__overlay_painter.begin(self)
        self.__overlay_painter.setRenderHint(QtGui.QPainter.Antialiasing)

        if self.is_hidden:
            if not self.isHidden():
                self.hide()

        else:
            if self.isHidden():
                self.show()

        if self.geometry_stack:
            self.setGeometry(*self.geometry_stack)
            self.geometry_stack.clear()

        for shape in self.draw_stack:

            if shape["type"] == "polygon":
                self.draw_polygon(event, self.__overlay_painter, shape["points"], shape["linesize"], shape["linetype"], shape["color"])

            if shape["type"] == "rect":
                self.draw_rect(event, self.__overlay_painter, shape["x"], shape["y"], shape["width"], shape["height"], shape["linesize"], shape["linetype"], shape["color"])

            if shape["type"] == "ellipse":
                self.draw_ellipse(event, self.__overlay_painter, shape["x"], shape["y"], shape["width"], shape["height"], shape["linesize"], shape["linetype"], shape["color"])

            if shape["type"] == "line":
                self.draw_line(event, self.__overlay_painter, shape["x1"], shape["y1"], shape["x2"], shape["y2"], shape["linesize"], shape["linetype"], shape["color"])

            if shape["type"] == "text":
                self.draw_text(event, self.__overlay_painter, shape["x"], shape["y"], shape["width"], shape["height"], shape["text"], shape["font"], shape["fontsize"], shape["align"], shape["color"])

        self.__overlay_painter.end()

    def draw_polygon(self, event: object, painter: object, points: list, linesize: int, linetype: object, color: tuple) -> None:

        if linesize <= 0:
            painter.setPen(QtGui.QPen(QtGui.QColor(*color), linesize, linetype))
            painter.setBrush(QtGui.QBrush(QtGui.QColor(*color), brushtype["solid"]))
            polygon = []

            for point in points:
                polygon.append(QtCore.QPoint(point["x"], point["y"]))

            polygon = QtGui.QPolygon(polygon)

        else:
            painter.setPen(QtGui.QPen(QtGui.QColor(*color), linesize, linetype))
            painter.setBrush(QtGui.QBrush(QtGui.QColor(*color), brushtype["nobrush"]))
            polygon = []

            for point in points:
                polygon.append(QtCore.QPoint(point["x"], point["y"]))

            polygon = QtGui.QPolygon(polygon)

        painter.drawPolygon(polygon)
        polygon.clear()

    def draw_rect(self, event: object, painter: object, x: int, y: int, w: int, h: int, linesize: int, linetype: object, color: tuple) -> None:

        if linesize <= 0:
            painter.setPen(QtGui.QPen(QtGui.QColor(*color), linesize, linetype))
            painter.setBrush(QtGui.QBrush(QtGui.QColor(*color), brushtype["solid"]))
            painter.drawRect(x, y, w, h)

        else:
            painter.setBrush(QtGui.QBrush(QtGui.QColor(*color), brushtype["nobrush"]))
            painter.setPen(QtGui.QPen(QtGui.QColor(*color), linesize, linetype))
            painter.drawRect(x, y, w, h)

    def draw_ellipse(self, event: object, painter: object, x: int, y: int, w: int, h: int, linesize: int, linetype: object, color: tuple) -> None:

        if linesize <= 0:
            painter.setPen(QtGui.QPen(QtGui.QColor(*color), linesize, linetype))
            painter.setBrush(QtGui.QBrush(QtGui.QColor(*color), brushtype["solid"]))
            painter.drawEllipse(x, y, w, h)

        else:
            painter.setBrush(QtGui.QBrush(QtGui.QColor(*color), brushtype["nobrush"]))
            painter.setPen(QtGui.QPen(QtGui.QColor(*color), linesize, linetype))
            painter.drawEllipse(x, y, w, h)

    def draw_line(self, event: object, painter: object, x1: int, y1: int, x2: int, y2: int, linesize: int, linetype: object, color: tuple) -> None:

        painter.setPen(QtGui.QPen(QtGui.QColor(*color), linesize, linetype))
        painter.drawLine(x1, y1, x2, y2)

    def draw_text(self, event: object, painter: object, x: int, y: int, w: int, h: int, text: str, font: OverlayFont, align: object, color: tuple):

        painter.setPen(QtGui.QPen(QtGui.QColor(*color)))
        painter.setFont(font.font)
        painter.drawText(QtCore.QRect(x, y, w, h), align, text)


def application_init() -> None:
    """Инициализация QApplication.

    Initialize QApplication.
    """

    return QtWidgets.QApplication(sys.argv)


def application_start(application: object) -> None:
    """Запуск объекта QApplication.

    Start QApplication object."""

    application.exec()
