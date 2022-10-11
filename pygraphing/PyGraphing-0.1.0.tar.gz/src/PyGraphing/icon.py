from PySVG.SVG import Embedded


class Icon(Embedded):
    def __init__(self, svg_object, w: int, h: int):
        super().__init__()
        self.w, self.h = w, h
        self.add_child(svg_object)
