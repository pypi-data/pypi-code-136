from .svg_element import SvgElement
from .path import Path


class Marker(SvgElement):
    def __init__(
        self,
        root_id,
        refX, refY,
        child,
        orient="auto-start-reverse",
    ):
        super().__init__("marker", children=[child])

        self.root_id = root_id
        self.refX = refX
        self.refY = refY
        self.orient = orient
        self.primary_color = None
        self.secondary_color = None

    @property
    def ref_id(self):
        rid = self.root_id
        rid += f"-{self.primary_color}" if self.primary_color else ""
        rid += f"-{self.secondary_color}" if self.secondary_color else ""

        return rid

    @property
    def ref_uri(self):
        return f"url(#{self.ref_id})"

    @property
    def over_length(self):
        xmax = self.children[0].bounds[1]
        return xmax - self.refX

    def set_colors(self, primary_color, secondary_color=None):
        self.primary_color = primary_color
        self.secondary_color = secondary_color

    def _render(self, doc, tag, text, debug):
        bounds = self.children[0].bounds
        width = bounds[1]-bounds[0]
        height = bounds[3]-bounds[2]

        self.attributes.update({
            "id": self.ref_id,
            "viewBox": f"{bounds[0]:.2f} {bounds[2]:.2f} {width:.2f} {height:.2f}",
            "refX": f"{self.refX:.2f}",
            "refY": f"{self.refY:.2f}",
            "markerWidth": f"{width:.2f}",
            "markerHeight": f"{height:.2f}",
            "orient": self.orient,
        })

        return super()._render(doc, tag, text, debug)


class MarkerArrow(Marker):
    def __init__(self):
        super().__init__("builtin_arrow", 3, 3, Path(
            points=[(0, 0), (6, 3), (0, 6)],
            close=True,
            fill="black",
            stroke="transparent",
            stroke_width_px=0,
        ))

    def set_colors(self, primary_color, secondary_color=None):
        super().set_colors(primary_color, secondary_color)

        self.children[0].fill = self.primary_color
