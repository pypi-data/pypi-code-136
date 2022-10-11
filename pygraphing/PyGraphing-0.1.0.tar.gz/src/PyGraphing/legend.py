from PySVG.SVG import Embedded, Section
from PySVG.Draw import Rect
from .icon import Icon


class Legend(Embedded):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.items = []

        self.dy = 10

        self.text = parent.text()
        self.background = Rect()
        self.active = True

    def add_item(self, name: str, shape: Icon):
        self.items.append(Item(self, name, shape))

    def xywh(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def set_items(self):
        i = 0
        for item in self.items:
            item.x, item.y = 10, i * 2 * self.dy
            self.add_child(item)
            i += 1

    def construct(self):
        self.add_child(self.background)
        self.set_items()
        return super().construct()


class Item(Section):
    def __init__(self, parent: Legend, name: str, icon: Icon):
        """
        Represents an entry into the legend.

        Parameters
        ----------
        name: The descriptive text that will be displayed in the legend
        icon : object
        """
        super().__init__(0, 0)
        self.icon = icon
        self.name = name
        self.parent = parent
        self.text = parent.text
        self.active = True

        self.add_child(self.text)
        self.add_child(self.icon)

    def construct(self):
        w, h = self.icon.w, self.icon.h
        self.text.x, self.text.y = 2 * w, h / 2
        self.text.text = self.name

        return super().construct()
