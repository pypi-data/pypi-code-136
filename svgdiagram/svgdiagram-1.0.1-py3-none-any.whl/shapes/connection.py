from .anchor import Anchor
from .shape import Shape

from enum import Enum


class ShapeConnectType(Enum):
    FLOATING = 0
    CLOSEST = 1


def is_valid_point(point):
    return isinstance(point, Anchor) or isinstance(point, Shape) or (
        isinstance(point, (list, tuple)) and len(point) == 2)


class Connection:
    def __init__(
        self,
        start_point, end_point,
        normal_len=20, mid_points=None,
        start_shape_connect_type=None, end_shape_connect_type=None,
    ):

        assert is_valid_point(start_point), \
            "Startpoint is not an achor nor shape nor has 2 elements!"

        if isinstance(start_point, Shape):
            assert isinstance(start_shape_connect_type, ShapeConnectType), \
                "Startpoint is a shape but the connect type is not set!"

        assert is_valid_point(end_point), \
            "Endpoint is not an achor nor shape nor has 2 elements!"

        if isinstance(end_point, Shape):
            assert isinstance(end_shape_connect_type, ShapeConnectType), \
                "Endpoint is a shape but the connect type is not set!"

        if mid_points:
            for mid_p in mid_points:
                assert len(mid_p) == 2,\
                    "Midpoint does not have 2 elements!"

        self.start_point = start_point
        self.end_point = end_point
        self.normal_len = normal_len
        self.mid_points = mid_points

        self.start_shape_connect_type = start_shape_connect_type
        self.end_shape_connect_type = end_shape_connect_type

    def calc_direct_point(self, point):
        if isinstance(point, (list, tuple)):
            direct_x = point[0]
            direct_y = point[1]
        elif isinstance(point, Shape):
            direct_x, direct_y, _, _ = point.get_center_and_size()
        elif isinstance(point, Anchor):
            direct_x = point.x + point.normal_x * self.normal_len
            direct_y = point.y + point.normal_y * self.normal_len
        else:
            raise NotImplementedError

        return direct_x, direct_y

    def _calculate_direct_points(self):
        if self.mid_points:
            direct_start_x = self.mid_points[0][0]
            direct_start_y = self.mid_points[0][1]
            direct_end_x = self.mid_points[-1][0]
            direct_end_y = self.mid_points[-1][1]
        else:
            direct_start_x, direct_start_y = self.calc_direct_point(
                self.end_point,
            )
            direct_end_x, direct_end_y = self.calc_direct_point(
                self.start_point,
            )

            # if any if shape closest recalculate the direct points
            if isinstance(self.start_point, Shape) and self.start_shape_connect_type == ShapeConnectType.CLOSEST:
                start_anchor = self.start_point.get_closest_discrete_anchor(
                    direct_start_x,
                    direct_start_y,
                )
                direct_end_x = start_anchor.x + start_anchor.normal_x * self.normal_len
                direct_end_y = start_anchor.y + start_anchor.normal_y * self.normal_len

            if isinstance(self.end_point, Shape) and self.end_shape_connect_type == ShapeConnectType.CLOSEST:
                end_anchor = self.end_point.get_closest_discrete_anchor(
                    direct_end_x,
                    direct_end_y,
                )
                direct_start_x = end_anchor.x + end_anchor.normal_x * self.normal_len
                direct_start_y = end_anchor.y + end_anchor.normal_y * self.normal_len

        return direct_start_x, direct_start_y, direct_end_x, direct_end_y

    def _calculate_start_points(self, direct_start_x, direct_start_y):
        points = []

        # if there are midpoints the overrule any starting behavior
        if isinstance(self.start_point, (list, tuple)):
            points.append(self.start_point)
        else:
            if isinstance(self.start_point, Anchor):
                start_anchor = self.start_point
            elif isinstance(self.start_point, Shape):
                if self.start_shape_connect_type == ShapeConnectType.FLOATING:
                    start_anchor = self.start_point.get_closest_floating_anchor(
                        direct_start_x,
                        direct_start_y,
                    )
                elif self.start_shape_connect_type == ShapeConnectType.CLOSEST:
                    start_anchor = self.start_point.get_closest_discrete_anchor(
                        direct_start_x,
                        direct_start_y,
                    )
                else:
                    raise NotImplementedError
            else:
                raise NotImplementedError

            points.append((start_anchor.x, start_anchor.y))
            points.append((
                start_anchor.x + start_anchor.normal_x * self.normal_len,
                start_anchor.y + start_anchor.normal_y * self.normal_len,
            ))

        return points

    def _calculate_end_points(self, direct_end_x, direct_end_y):
        points = []

        if isinstance(self.end_point, (list, tuple)):
            points.append(self.end_point)
        else:
            if isinstance(self.end_point, Anchor):
                end_anchor = self.end_point
            elif isinstance(self.end_point, Shape):
                if self.end_shape_connect_type == ShapeConnectType.FLOATING:
                    end_anchor = self.end_point.get_closest_floating_anchor(
                        direct_end_x,
                        direct_end_y,
                    )
                elif self.end_shape_connect_type == ShapeConnectType.CLOSEST:
                    end_anchor = self.end_point.get_closest_discrete_anchor(
                        direct_end_x,
                        direct_end_y,
                    )
                else:
                    raise NotImplementedError
            else:
                raise NotImplementedError

            points.append((
                end_anchor.x + end_anchor.normal_x * self.normal_len,
                end_anchor.y + end_anchor.normal_y * self.normal_len,
            ))
            points.append((end_anchor.x, end_anchor.y))

        return points

    def calculate_points(self):
        direct_start_x, direct_start_y, direct_end_x, direct_end_y = self._calculate_direct_points()

        points = []

        points.extend(self._calculate_start_points(
            direct_start_x, direct_start_y))

        if self.mid_points:
            points.extend(self.mid_points)

        points.extend(self._calculate_end_points(direct_end_x, direct_end_y))

        return points
