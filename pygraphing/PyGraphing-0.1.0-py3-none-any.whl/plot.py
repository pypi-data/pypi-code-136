from PySVG import Draw
from PySVG.SVG import Embedded


class Plot(Embedded):
    def __init__(self):
        super().__init__()
        self.xmin, self.ymin, self.xmax, self.ymax = 0, 0, 1, 1
        self.background = Draw.Rect()

    def set_extrema(self, xmin, ymin, xmax, ymax):
        self.xmin, self.ymin, self.xmax, self.ymax = xmin, ymin, xmax, ymax

    def cart2pixel_x(self, x: list[float]) -> list[float]:
        if self.w != 0:
            dx = (self.xmax - self.xmin) / self.w
            if dx != 0:
                return [(xi - self.xmin) / dx for xi in x]
            else:
                return x
        else:
            return x

    def pixel2cart_x(self, x: list[float]) -> list[float]:
        if self.w != 0:
            dx = (self.xmax - self.xmin) / self.w
            return [(xi * dx + self.xmin) for xi in x]
        else:
            return x

    def cart2pixel_y(self, y: list[float]) -> list[float]:
        if self.h != 0:
            dy = (self.ymax - self.ymin) / self.h
            if dy != 0:
                return [self.h - ((yi - self.ymin) / dy) for yi in y]
            else:
                return y
        else:
            return y

    def pixel2cart_y(self, y: list[float]) -> list[float]:
        if self.h != 0:
            dy = (self.ymax - self.ymin) / self.h
            return [dy * (self.h - yi) + self.ymin for yi in y]
        else:
            return y

    def construct(self):
        self.add_child(self.background)

        return super().construct()

    def xywh(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
