from PySVG import Section
from PySVG.Draw import Rect
from .box import Box


class Scatter(Section):
    def __init__(self, plot, shape, x: list, y: list):
        super().__init__(0, 0)
        self.plot = plot
        self.shape = shape
        self.exes = x
        self.whys = y

    def _process(self):
        x = self.plot.cart2pixel_x(self.exes)
        y = self.plot.cart2pixel_y(self.whys)

        for i in range(len(x)):
            icon = self.shape.copy()
            icon.x = x[i] - icon.w / 2
            icon.y = y[i] - icon.h / 2

            self.add_child(icon)

    def construct(self):
        self._process()
        return super().construct()


class ScatterBoxes(Scatter):
    def __init__(self, plot, shape, x: list, y: list, err: list):
        super().__init__(plot, shape, x, y)
        self.rect = Rect()
        self.err = err

        self.width = 0.8

    def _process(self):
        x = self.exes
        y = self.whys
        e = self.err
        w = self.width / 2

        for i in range(len(x)):
            box = Box(self.plot, (x[i] - w, y[i] - e[i]), (x[i] + w, y[i] + e[i]))
            box.inherit(self.rect)
            self.add_child(box)

        super()._process()

    def construct(self):
        return super().construct()
