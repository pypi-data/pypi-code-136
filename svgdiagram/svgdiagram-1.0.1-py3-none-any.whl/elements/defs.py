from .svg_element import SvgElement


class Defs(SvgElement):
    def __init__(self, children):
        super().__init__("defs", children=children)

    @property
    def bounds(self):
        return None
