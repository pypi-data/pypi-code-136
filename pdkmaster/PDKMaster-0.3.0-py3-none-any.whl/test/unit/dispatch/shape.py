# SPDX-License-Identifier: GPL-2.0-or-later OR AGPL-3.0-or-later OR CERN-OHL-S-2.0+
# type: ignore
import unittest

from pdkmaster.technology import geometry as _geo
from pdkmaster.dispatch.shape import ShapeDispatcher


# Simple dispatcher that just returns the type of the shape
class MyDispatcher(ShapeDispatcher):
    def _Shape(self, shape: _geo._Shape):
        return type(shape)


class ShapeDispatchTest(unittest.TestCase):
    def test_notimplemented(self):
        with self.assertRaises(NotImplementedError):
            # Call ShapeDispatched._Shape() method
            ShapeDispatcher()(_geo.origin)

    def test_dispatch(self):
        disp = MyDispatcher()

        with self.assertRaises(RuntimeError):
            disp("error")

        line = _geo.Line(point1=_geo.origin, point2=_geo.Point(x=0.0, y=1.0))
        rect = _geo.Rect.from_size(width=2.0, height=2.0)
        polygon = _geo.Polygon.from_floats(points=(
            (0.0, 0.0),
            (0.0, 1.0),
            (1.0, 1.0),
            (1.0, 0.0),
            (0.0, 0.0),
        ))
        ring = _geo.Ring(
            outer_bound=_geo.Rect.from_size(width=2.0, height=2.0),
            ring_width=0.5,
        )
        rectring = _geo.RectRing(
            outer_bound=rect, rect_width=0.4, min_rect_space=0.4,
        )
        multishape = _geo.MultiShape(shapes=(rect, polygon))
        repeatedshape = _geo.RepeatedShape(
            shape=rect, offset0=_geo.origin, n=2, n_dxy=_geo.Point(x=0.0, y=4.0)
        )
        arrayshape = _geo.ArrayShape(
            shape=rect, offset0=_geo.origin, rows=2, columns=2, pitch_y=4.0, pitch_x=3.0,
        )

        part1 = _geo.Rect(left=0.0, bottom=0.0, right=1.0, top=1.0)
        part2 = _geo.Rect(left=1.0, bottom=0.0, right=2.0, top=1.0)
        part12 = _geo.Rect(left=0.0, bottom=0.0, right=2.0, top=1.0)
        multipartshape = _geo.MultiPartShape(fullshape=part12, parts=(part1, part2))

        # Currently only code coerage is done
        self.assertIs(disp(_geo.origin), _geo.Point)
        self.assertIs(disp(line), _geo.Line)
        self.assertIs(disp(polygon), _geo.Polygon)
        self.assertIs(disp(rect), _geo.Rect)
        self.assertIs(disp(ring), _geo.Ring)
        self.assertIs(disp(rectring), _geo.RectRing)
        self.assertIs(disp(multishape), _geo.MultiShape)
        self.assertIs(disp(multipartshape), _geo.MultiPartShape)
        self.assertIs(disp(multipartshape.parts[0]), _geo.Rect)
        self.assertIs(disp(repeatedshape), _geo.RepeatedShape)
        self.assertIs(disp(arrayshape), _geo.ArrayShape)
