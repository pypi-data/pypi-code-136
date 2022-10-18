from .svg_element import SvgElement


class Circle(SvgElement):
    def __init__(self, cx, cy, r, stroke="black", stroke_width_px=1, fill="white") -> None:
        super().__init__("circle")

        self.cx = cx
        self.cy = cy
        self.r = r
        self.stroke = stroke
        self.stroke_width_px = stroke_width_px
        self.fill = fill

    @property
    def bounds(self):
        off = self.r + self.stroke_width_px / 2.0
        return [self.cx - off, self.cx + off, self.cy - off, self.cy + off]

    def _render(self, doc, tag, text, debug, inject_pre_children=None):
        self.attributes.update({
            "cx": self.cx,
            "cy": self.cy,
            "r": self.r,
            "stroke": self.stroke,
            "stroke-width": f"{self.stroke_width_px}px",
            "fill": self.fill,
        })

        return super()._render(doc, tag, text, debug, inject_pre_children)
