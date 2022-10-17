from .shape import Shape
from .anchor import Anchor
from .utils import bounds_to_center_and_size

import math


class CircularShape(Shape):
    def get_center_and_radius(self):
        bounds = self.svg_element.bounds

        center_x, center_y, width, heigth = bounds_to_center_and_size(bounds)

        radius = max(width, heigth) / 2.0

        return center_x, center_y, radius

    def get_all_discrete_anchors(self):
        center_x, center_y, radius = self.get_center_and_radius()
        return [
            Anchor(center_x, center_y + radius, 0, 1),  # bottom
            Anchor(center_x, center_y - radius, 0, -1),  # top
            Anchor(center_x - radius, center_y, -1, 0),  # left
            Anchor(center_x + radius, center_y, 1, 0),  # right
        ]

    def get_closest_floating_anchor(self, x, y):
        center_x, center_y, radius = self.get_center_and_radius()
        vec_x = x - center_x
        vec_y = y - center_y

        vec_len = math.sqrt(vec_x**2 + vec_y**2)

        n_vec_x = vec_x / vec_len
        n_vec_y = vec_y / vec_len

        return Anchor(
            center_x + n_vec_x * radius,
            center_y + n_vec_y * radius,
            n_vec_x,
            n_vec_y,
        )
