from .shape import Shape
from .anchor import Anchor
from .utils import bounds_to_center_and_size

import math

SQRT_2 = math.sqrt(2)


class DiamondShape(Shape):
    def get_center_and_radius(self):
        bounds = self.svg_element.bounds

        center_x, center_y, width, heigth = bounds_to_center_and_size(bounds)

        radius = max(width, heigth) / 2.0

        return center_x, center_y, radius

    def get_all_discrete_anchors(self):
        center_x, center_y, radius = self.get_center_and_radius()
        return [
            # Anchor(center_x, center_y + radius, 0, 1),  # bottom
            # Anchor(center_x, center_y - radius, 0, -1),  # top
            # Anchor(center_x - radius, center_y, -1, 0),  # left
            # Anchor(center_x + radius, center_y, 1, 0),  # right
            Anchor(  # bottom right
                center_x + radius / 2,
                center_y + radius / 2,
                1, 1,
            ),
            Anchor(  # top right
                center_x + radius / 2,
                center_y - radius / 2,
                1, -1,
            ),
            Anchor(  # top left
                center_x - radius / 2,
                center_y - radius / 2,
                -1, -1,
            ),
            Anchor(  # bottom left
                center_x - radius / 2,
                center_y + radius / 2,
                -1, 1,
            ),
        ]

    def get_closest_floating_anchor(self, x, y):
        center_x, center_y, radius = self.get_center_and_radius()

        snap_distance = 2

        v_x = x - center_x
        v_y = y - center_y

        angle = math.atan2(v_y, v_x)

        n_x = 1 if v_x > 0 else -1
        n_y = 1 if v_y > 0 else -1

        if angle > math.pi / 2.0:
            t2 = (v_y*(center_x - radius) - v_x * (center_y) + v_x * center_y -
                  center_x * v_y) / (v_x - v_y)

            p1 = (center_x - radius) + t2
            p2 = (center_y) + t2
        elif angle > 0:
            t2 = (v_y*(center_x) - v_x * (center_y + radius) + v_x * center_y -
                  center_x * v_y) / (-v_x - v_y)

            p1 = (center_x) + t2
            p2 = (center_y + radius) - t2
        elif angle > -math.pi / 2.0:
            t2 = (v_y*(center_x + radius) - v_x * (center_y) + v_x * center_y -
                  center_x * v_y) / (-v_x + v_y)

            p1 = (center_x + radius) - t2
            p2 = (center_y) - t2
        else:
            t2 = (v_y*(center_x) - v_x * (center_y - radius) + v_x * center_y -
                  center_x * v_y) / (v_x + v_y)

            p1 = (center_x) - t2
            p2 = (center_y - radius) + t2

        dx = p1-center_x
        dy = p2-center_y

        if abs(dx) < snap_distance:
            if dy < 0:
                return Anchor(center_x, center_y - radius, 0, -1)
            else:
                return Anchor(center_x, center_y + radius, 0, 1)

        if abs(dy) < snap_distance:
            if dx < 0:
                return Anchor(center_x - radius, center_y, -1, 0)
            else:
                return Anchor(center_x + radius, center_y, 1, 0)

        return Anchor(
            p1,
            p2,
            n_x,
            n_y,
        )
