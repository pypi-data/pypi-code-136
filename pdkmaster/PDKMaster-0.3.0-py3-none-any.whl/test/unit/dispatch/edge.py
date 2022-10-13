# SPDX-License-Identifier: GPL-2.0-or-later OR AGPL-3.0-or-later OR CERN-OHL-S-2.0+
# type: ignore
import unittest

from pdkmaster.technology import mask as _msk, edge as _edg
from pdkmaster.dispatch.edge import EdgeDispatcher


# Simple dispatcher that just returns the type of the edge
class MyDispatcher(EdgeDispatcher):
    def _Edge(self, edge: _edg._Edge):
        return type(edge)


class EdgeDispatchTest(unittest.TestCase):
    def test_notimplemented(self):
        with self.assertRaises(NotImplementedError):
            # Call ShapeDispatched._Shape() method
            mask = _msk.DesignMask(name="test", fill_space="yes")
            EdgeDispatcher()(_edg.MaskEdge(mask))

    def test_dispatch(self):
        disp = MyDispatcher()

        with self.assertRaises(RuntimeError):
            disp("error")

        mask1 = _msk.DesignMask(name="mask1", fill_space="yes")
        mask2 = _msk.DesignMask(name="mask2", fill_space="yes")

        edge1 = _edg.MaskEdge(mask1)
        edge2 = _edg.MaskEdge(mask2)
        operation = edge1.interact_with(mask2)
        join = _edg.Join(edges=(edge1, edge2))
        intersect = _edg.Intersect(edges=(edge1, edge2))

        # Just run with all mask to get code coverage
        edges = (
            edge1, operation, join, intersect
        )
        for edge in edges:
            self.assertIs(disp(edge), type(edge))
