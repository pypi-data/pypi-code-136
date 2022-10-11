from PySVG import Text, Font
from PySVG.Draw import Rect
from .plot import Plot
from .legend import Legend
from .frame import Frame
from PySVG.SVG import Embedded


class Graph(Embedded):
    def __init__(self, w: float, h: float):
        """
        Graph is an SVG Object representing a generic graph.
        A Graph is made up of several parts: Legend, Plot Area, Frame, Title.

        :param w: width of the Graph object in pixels
        :param h: height of the Graph object in pixels
        """
        # Graph Parameters
        super().__init__()
        self.w, self.h = w, h

        self.title = ''
        self.background = Rect()

        self.legend = Legend(self)
        self.plot = Plot()
        self.frame = Frame(self.plot)

        self.set_sizes()

    def _title(self):
        t = Text()
        t.x, t.y = 0.50 * self.w, 0.05 * self.h
        t.font = Font('IBM Plex Mono', 13, '700')
        t.baseline = 'central'
        t.anchor = 'middle'

        return t

    def text(self):
        t = Text()
        t.font = Font('IBM Plex Mono', 10, '600')
        t.baseline = 'central'

        return t

    def set_sizes(self):
        """
        Sets the sizes for the Graph and all of its children.
        ----------------------------------------------------------------------
        """
        w, h = self.w, self.h
        dy = 0.10 * h
        self.legend.xywh(w * 0.7, dy, w * 0.20, 0.5 * (h - 2 * dy))
        self.plot.xywh(w * .1, dy, w * .85, h - 100 - self.plot.y)

    def construct(self):
        self.add_child(self.background)
        self.add_child(self.legend, 'Legend')
        self.add_child(self.plot, 'Plot')
        self.add_child(self.frame, 'Frame')
        self.add_child(self.title)

        return super().construct()
