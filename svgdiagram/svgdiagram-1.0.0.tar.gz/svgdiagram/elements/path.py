from .svg_element import SvgElement
import math


class Path(SvgElement):
    def __init__(
        self,
        points,
        close=False,
        stroke='black',
        stroke_width_px=1,
        fill='transparent',
        marker_start=None,
        marker_end=None,
        corner_radius=None
    ):

        self.points = points
        self.close = close

        self.stroke = stroke
        self.stroke_width_px = stroke_width_px
        self.fill = fill

        self.marker_start = marker_start
        self.marker_end = marker_end

        self.corner_radius = corner_radius

        super().__init__('path')

    @property
    def bounds(self):
        [x, y] = zip(*self.points)

        xmin = min(x)-self.stroke_width_px / 2.0
        xmax = max(x)+self.stroke_width_px / 2.0
        ymin = min(y)-self.stroke_width_px / 2.0
        ymax = max(y)+self.stroke_width_px / 2.0

        return [xmin, xmax, ymin, ymax]

    @property
    def defs(self):
        ds = {}

        if self.marker_start and self.marker_start.ref_id not in ds:
            ds[self.marker_start.ref_id] = self.marker_start

        if self.marker_end and self.marker_end.ref_id not in ds:
            ds[self.marker_end.ref_id] = self.marker_end

        return list(ds.values())

    def _calc_poly_text_d(self):
        if self.corner_radius and len(self.points) >= 3:
            _points = self.points
            if self.close:
                first_point = _points[0]
                last_point = _points[-1]
                _points = [last_point] + _points + [first_point]
                d = ""
            else:
                d = f"M {_points[0][0]:.2f} {_points[0][1]:.2f}"

            for index in range(1, len(_points)-1):
                x1, y1 = _points[index-1]
                xm, ym = _points[index]
                x3, y3 = _points[index+1]

                v1_x = x1 - xm
                v1_y = y1 - ym
                v1_len = math.sqrt(v1_x**2 + v1_y**2)
                v1_x /= v1_len
                v1_y /= v1_len

                v3_x = x3 - xm
                v3_y = y3 - ym
                v3_len = math.sqrt(v3_x**2 + v3_y**2)
                v3_x /= v3_len
                v3_y /= v3_len

                dot = (v1_x * v3_x + v1_y * v3_y)
                cross = (v1_x * v3_y - v1_y * v3_x)
                alpha = math.atan2(cross, dot)

                sweep_angle = 1 if alpha < 0 else 0

                s = self.corner_radius / math.sin(alpha/2.0)

                b = math.sqrt(s**2 - self.corner_radius**2)

                a1_x = xm + v1_x * b
                a1_y = ym + v1_y * b
                a3_x = xm + v3_x * b
                a3_y = ym + v3_y * b

                if index == 1 and self.close:
                    d += f" M {a1_x:.2f} {a1_y:.2f}"
                else:
                    d += f" L {a1_x:.2f} {a1_y:.2f}"
                d += f" A {self.corner_radius:.2f} {self.corner_radius:.2f} {0} {0} {sweep_angle} {a3_x:.2f} {a3_y:.2f}"

            if self.close:
                d += " Z"
            else:
                d += f" L {_points[-1][0]:.2f} {_points[-1][1]:.2f}"

            return d
        else:
            d = f'M {self.points[0][0]:.2f} {self.points[0][1]:.2f}'

            for p in self.points[1:]:
                d += f' L {p[0]:.2f} {p[1]:.2f}'

            if self.close:
                d += " Z"

            return d

    def _layout(self, x_con_min, x_con_max, y_con_min, y_con_max):
        super()._layout(x_con_min, x_con_max, y_con_min, y_con_max)

        # shorten path by marker overlength
        if self.marker_start:
            first_point = self.points[0]
            next_first_point = self.points[1]
            overlen = self.marker_start.over_length * self.stroke_width_px
            vec_x = first_point[0] - next_first_point[0]
            vec_y = first_point[1] - next_first_point[1]
            vec_len = math.sqrt(vec_x**2 + vec_y**2)

            new_first_point_x = next_first_point[0] + \
                vec_x * (vec_len - overlen) / vec_len
            new_first_point_y = next_first_point[1] + \
                vec_y * (vec_len - overlen) / vec_len

            self.points[0] = (new_first_point_x, new_first_point_y)

        if self.marker_end:
            last_point = self.points[-1]
            prev_last_point = self.points[-2]
            overlen = self.marker_end.over_length * self.stroke_width_px
            vec_x = last_point[0] - prev_last_point[0]
            vec_y = last_point[1] - prev_last_point[1]
            vec_len = math.sqrt(vec_x**2 + vec_y**2)

            new_last_point_x = prev_last_point[0] + \
                vec_x * (vec_len - overlen) / vec_len
            new_last_point_y = prev_last_point[1] + \
                vec_y * (vec_len - overlen) / vec_len

            self.points[-1] = (new_last_point_x, new_last_point_y)

        # Set Marker Color
        if self.marker_start:
            self.marker_start.set_colors(self.stroke)

        if self.marker_end:
            self.marker_end.set_colors(self.stroke)

    def _render(self, doc, tag, text, debug):
        self.attributes.update({
            "d": self._calc_poly_text_d(),
            "stroke": self.stroke,
            "stroke-width": f"{self.stroke_width_px}px",
            "fill": self.fill,
        })

        if self.marker_start:
            self.marker_start.set_colors(self.stroke)
            self.attributes.update({
                "marker-start": self.marker_start.ref_uri
            })
        if self.marker_end:
            self.marker_end.set_colors(self.stroke)
            self.attributes.update({
                "marker-end": self.marker_end.ref_uri
            })

        return super()._render(doc, tag, text, debug)
