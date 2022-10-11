from PySVG.Draw import Rect
from PySVG import Section
from ..plot import Plot


class Bar(Rect):
    def __init__(self, fill=(0, 0, 0), fill_opacity=1, stroke=None, stroke_width=1):
        super().__init__(0, 0, 0, 0)
        self.fill = fill
        self.fill_opacity = fill_opacity
        self.stroke = stroke
        self.stroke_width = stroke_width

        self.index = 0
        self.value = 0
        self.name = ''


class Group(Section):
    def __init__(self, parent):
        super().__init__(0, 0)
        self.plot = parent
        self.bars = []
        self.filled = 0.50

        self.bar_width = 0
        self.bar_space = 0

    @property
    def w(self):
        width = self.bar_width * self.nbars + self.bar_space * (1 + self.nbars)
        return width

    @property
    def position(self):
        return self.plot.pixel2cart_x([self.x + self.w/2])[0]

    @property
    def nbars(self):
        return len(self.bars)

    def add_bar(self, bar: Bar, x: int, y: float, bar_name: str = ''):
        bar = bar.copy()
        bar.index = x
        bar.value = y
        bar.name = bar_name
        self.bars.append(bar)

    def set_bars(self):
        n = len(self.bars)
        exes = [(i + 1) * self.bar_space + i * self.bar_width for i in range(n)]
        zero = self.plot.cart2pixel_y([0])[0]

        for bar in self.bars:
            bar.x, bar.w = exes[bar.index - 1], self.bar_width
            bar.y = self.plot.cart2pixel_y([bar.value])[0]
            bar.h = zero - bar.y

            self.add_child(bar)


class BarPlot(Plot):
    def __init__(self):
        super().__init__()
        self.groups = []

        self.bar_area_ratio = 0.80
        self.space_ratio = 3

        self._bar_width = 0
        self._gspace = 0
        self._bspace = 0

    def _set_dimensions(self):
        bar_area = self.w * self.bar_area_ratio
        space_area = self.w * (1 - self.bar_area_ratio)
        n_bars = sum([group.nbars for group in self.groups])
        n_groups = len(self.groups)

        self._bar_width = bar_area / n_bars
        self._bspace = space_area / (self.space_ratio*(n_groups - 1) + n_bars + n_groups)
        self._gspace = self._bspace * self.space_ratio

        a=1

    def add_group(self, group: Group):
        self.groups.append(group)

    def _set_groups(self):
        x = 0
        for group in self.groups:
            group.x = x
            group.bar_width = self._bar_width
            group.bar_space = self._bspace
            x += group.w + self._gspace
            group.set_bars()

            self.add_child(group)

    def set(self):
        self._set_dimensions()
        self._set_groups()

