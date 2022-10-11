from .plot import Plot
from PySVG import Section, Draw


class Frame(Section):
    def __init__(self, plot: Plot):
        super().__init__(0, 0)
        self.border = Draw.Generic_Path()
        self.ax = Axis()
        self.ay = Axis()

        self.plot = plot

        self.left, self.right, self.top, self.bottom = True, True, True, True

        self.children = []

    def get_pixel(self, x=None, y=None):
        if x is not None and y is None:
            if self.ax.pixels:
                return x + self.plot.x
            else:
                return self.plot.cart2pixel_x([x])[0] + self.plot.x

        if x is None and y is not None:
            if self.ay.pixels:
                return y + self.plot.y
            else:
                return self.plot.cart2pixel_y([y])[0] + self.plot.y

        return 0

    def _set_ticks(self):
        self.ax.ticks.sort()
        self.ay.ticks.sort()

        xmin, xmax, ymin, ymax = self.plot.xmin, self.plot.xmax, self.plot.ymin, self.plot.ymax
        if self.ax.pixels:
            self.ax.p_ticks = [self.get_pixel(x=x[0]) for x in self.ax.ticks]
        else:
            self.ax.p_ticks = [self.get_pixel(x=x[0]) for x in self.ax.ticks if xmin <= x[0] <= xmax]

        if self.ay.pixels:
            self.ay.p_ticks = [self.get_pixel(y=y[0]) for y in self.ay.ticks]
        else:
            self.ay.p_ticks = [self.get_pixel(y=y[0]) for y in self.ay.ticks if ymin <= y[0] <= ymax]

    def _set_titles(self):
        if self.ax.title is not None:
            self.add_child(self.ax.title)
            self.ax.title.angle = 0
            self.ax.title.anchor = 'middle'
            self.ax.title.baseline = 'central'
            x = self.plot.x + self.plot.w / 2
            self.ax.title.x, self.ax.title.y = x, '90%'

        if self.ay.title is not None:
            self.add_child(self.ay.title)
            self.ay.title.angle = -90
            self.ay.title.anchor = 'middle'
            self.ay.title.baseline = 'central'
            self.ay.title.x, self.ay.title.y = self.plot.x / 3, self.plot.y + self.plot.h / 2

    def _get_points(self):
        x1 = self.plot.x
        x2 = self.plot.x + self.plot.w
        y1 = self.plot.y
        y2 = self.plot.y + self.plot.h

        return x1, y1, x2, y2

    def _test_xmin(self):
        if self.ax.ticks:
            ticks, _ = zip(*self.ax.ticks)
            if ticks and self.ax.lw > 0:
                if ticks[0] == self.plot.xmin:
                    return self.plot.y + self.plot.h + self.ax.lw

        return self.plot.y + self.plot.h

    def _test_xmax(self):
        if self.ax.ticks:
            ticks, _ = zip(*self.ax.ticks)
            if ticks and self.ax.lw > 0:
                if ticks[-1] == self.plot.xmax:
                    return self.plot.y + self.plot.h + self.ax.lw

        return self.plot.y + self.plot.h

    def _test_ymax(self):
        if self.ay.ticks:
            ticks, _ = zip(*self.ay.ticks)
            if ticks and self.ay.lw > 0:
                if ticks[-1] == self.plot.ymax:
                    return self.plot.x - self.ay.lw

        return self.plot.x

    def _test_ymin(self):
        if self.ay.ticks:
            ticks, _ = zip(*self.ay.ticks)
            if ticks and self.ay.lw > 0:
                if ticks[0] == self.plot.ymin:
                    return self.plot.x - self.ay.lw

        return self.plot.x

    def _LRBT(self):
        x1, y1, x2, y2 = self._get_points()
        self.border = self.border.copy(Draw.Polygon())
        self.border.points = [(x1, y1), (x2, y1), (x2, y2), (x1, y2)]

    def _LRB(self):
        x1, y1, x2, y2 = self._get_points()
        x0 = self._test_ymax()

        if x0 == x1:
            points = [('M', x1, y1)]
        else:
            self.ay.p_ticks.pop(-1)
            points = [('M', x0, y1), ('L', x1, y1)]

        self.border.points = points + [('L', x1, y2), ('L', x2, y2), ('L', x2, y1)]

    def _LRT(self):
        x1, y1, x2, y2 = self._get_points()
        x0 = self._test_ymin()

        if x0 == x1:
            points = [('M', x1, y2)]
        else:
            self.ay.p_ticks.pop(0)
            points = [('M', x0, y2), ('L', x1, y2)]

        self.border.points = points + [('L', x1, y1), ('L', x2, y1), ('L', x2, y2)]

    def _RBT(self):
        x1, y1, x2, y2 = self._get_points()
        y0 = self._test_xmin()

        if y0 == y2:
            points = [('M', x1, y2)]
        else:
            points = [('M', x1, y0), ('L', x1, y2)]
            self.ax.p_ticks.pop(0)

        self.border.points = points + [('L', x2, y2), ('L', x2, y1), ('L', x1, y1)]

    def _LBT(self):
        x1, y1, x2, y2 = self._get_points()
        y0 = self._test_xmax()

        if y0 == y2:
            points = [('M', x2, y2)]
        else:
            points = [('M', x2, y0), ('L', x2, y2)]
            self.ax.p_ticks.pop(-1)

        self.border.points = points + [('L', x1, y2), ('L', x1, y1), ('L', x2, y1)]
        pass

    def _LR(self):
        x1, y1, x2, y2 = self._get_points()
        x0 = self._test_ymin()
        x3 = self._test_ymax()

        if x0 == x1:
            points = [('M', x1, y1), ('L', x1, y2)]
        else:
            points = [('M', x0, y1), ('L', x1, y1), ('L', x1, y2)]
            self.ay.p_ticks.pop(0)

        if x3 != x1:
            points.append(('L', x3, y2))
            self.ay.p_ticks.pop(-1)

        self.border.points = points + [('M', x2, y1), ('L', x2, y2)]

    def _LT(self):
        x1, y1, x2, y2 = self._get_points()
        x0 = self._test_ymin()

        if x0 == x1:
            points = [('M', x1, y2)]
        else:
            points = [('M', x0, y2), ('L', x1, y2)]
            self.ay.p_ticks.pop(0)

        self.border.points = points + [('L', x1, y1), ('L', x2, y1)]

    def _LB(self):
        x1, y1, x2, y2 = self._get_points()
        x0 = self._test_ymax()
        y0 = self._test_xmax()

        if x0 == x1:
            points = [('M', x1, y1), ('L', x1, y2), ('L', x2, y2)]
        else:
            points = [('M', x0, y1), ('L', x1, y1), ('L', x1, y2), ('L', x2, y2)]
            self.ay.p_ticks.pop(-1)

        if y0 != y2:
            points.append(('L', x2, y0))
            self.ax.p_ticks.pop(-1)

        self.border.points = points

    def _BT(self):
        x1, y1, x2, y2 = self._get_points()
        y0 = self._test_xmin()
        y3 = self._test_xmax()

        if y0 == y2:
            points = [('M', x1, y2), ('L', x2, y2)]
        else:
            points = [('M', x1, y0), ('L', x1, y2), ('L', x2, y2)]
            self.ax.p_ticks.pop(0)

        if y3 != y2:
            points.append(('L', x2, y3))
            self.ax.p_ticks.pop(-1)

        self.border.points = points + [('M', x1, y1), ('L', x2, y1)]

    def _L(self):
        x1, y1, x2, y2 = self._get_points()
        x0 = self._test_ymax()
        x3 = self._test_ymin()

        if x0 == x1:
            points = [('M', x1, y1), ('L', x1, y2)]
        else:
            points = [('M', x0, y1), ('L', x1, y1), ('L', x1, y2)]
            self.ay.p_ticks.pop(-1)

        if x3 != x1:
            points.append(('L', x3, y2))
            self.ay.p_ticks.pop(0)

        self.border.points = points

    def _R(self):
        x1, y1, x2, y2 = self._get_points()
        self.border.points = [('M', x2, y1), ('L', x2, y2)]
        pass

    def _B(self):
        x1, y1, x2, y2 = self._get_points()
        y0 = self._test_xmin()
        y3 = self._test_xmax()

        if y0 == y2:
            points = [('M', x1, y2), ('L', x2, y2)]
        else:
            points = [('M', x1, y0), ('L', x1, y2), ('L', x2, y2)]
            self.ax.p_ticks.pop(0)

        if y3 != y2:
            points.append(('L', x2, y3))
            self.ax.p_ticks.pop(-1)

        self.border.points = points

    def _T(self):
        x1, y1, x2, y2 = self._get_points()
        self.border.points = [('M', x1, y1), ('L', x2, y1)]

    def _set_frame(self):
        if self.left and self.right and self.bottom and self.top:
            self._LRBT()

        elif self.left and self.right and self.bottom and not self.top:
            self._LRB()
        elif self.left and self.right and not self.bottom and self.top:
            self._LRT()
        elif self.left and not self.right and self.bottom and self.top:
            self._LBT()
        elif not self.left and self.right and self.bottom and self.top:
            self._RBT()

        elif self.left and not self.right and self.bottom and not self.top:
            self._LB()
        elif not self.left and not self.right and self.bottom and self.top:
            self._BT()
        elif self.left and self.right and not self.bottom and not self.top:
            self._LR()

        elif self.left and not self.right and not self.bottom and not self.top:
            self._L()
        elif not self.left and not self.right and self.bottom and not self.top:
            self._B()

    def print_ticks(self):
        ticks = self._print_xticks() + self._print_yticks()
        frame = self.border.copy()

        frame.points = ticks
        if ticks:
            self.add_child(frame)

    def _print_xticks(self):
        y = self.plot.y + self.plot.h
        dy = self.ax.lw
        points = []
        for x in self.ax.p_ticks:
            points.append(('M', x, y))
            points.append(('L', x, y + dy))

        return points

    def _print_yticks(self):
        x = self.plot.x
        dx = self.ay.lw
        points = []
        for y in self.ay.p_ticks:
            points.append(('M', x, y))
            points.append(('L', x - dx, y))

        return points

    def _ylabels(self):
        if self.ay.text is not None:
            ticks = self.ay.ticks
            x = self.plot.x - self.ay.lw - self.ay.dist2text
            for tick in ticks:
                text = self.ay.text.copy()
                text.text = tick[1]
                text.x = x
                text.y = self.plot.cart2pixel_y([tick[0]])[0] + self.plot.y

                self.add_child(text)

    def _xlabels(self):
        if self.ax.text is not None:
            ticks = self.ax.ticks
            y = self.plot.y + self.plot.h + self.ax.lw + self.ax.dist2text
            for tick in ticks:
                text = self.ax.text.copy()
                text.text = tick[1]
                text.x = self.plot.cart2pixel_x([tick[0]])[0] + self.plot.x
                text.y = y

                self.add_child(text)

    def _build_frame(self):
        self._set_ticks()
        self._set_frame()
        self.add_child(self.border)

        self.print_ticks()

        self._ylabels()
        self._xlabels()

        self._set_titles()

    def construct(self):
        self._build_frame()
        for child in self.children:
            self.add_child(child)

        return super().construct()


class Axis:
    def __init__(self):
        self.lw = 4
        self.dist2text = 5
        self.ticks = []
        self.p_ticks = []
        self.angle = 0
        self.text = None
        self.title = None

        self.pixels = False
