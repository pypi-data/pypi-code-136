# SPDX-License-Identifier: GPL-2.0-or-later OR AGPL-3.0-or-later OR CERN-OHL-S-2.0+
# type: ignore
import unittest

from pdkmaster.technology import property_ as _prp, primitive as _prm
from pdkmaster.dispatch.primitive import PrimitiveDispatcher

from ..dummy import dummy_tech
dummy_prims = dummy_tech.primitives


# Simple dispatcher that just returns the type of the edge
class MyDispatcher(PrimitiveDispatcher):
    def _Primitive(self, prim: _prm._Primitive):
        return type(prim)


class EdgeDispatchTest(unittest.TestCase):
    def test_notimplemented(self):
        with self.assertRaises(NotImplementedError):
            # Call ShapeDispatched._Shape() method
            PrimitiveDispatcher()(dummy_prims.active)

    def test_dispatch(self):
        disp = MyDispatcher()

        with self.assertRaises(RuntimeError):
            disp("error")

        pad = _prm.PadOpening(
            name="pad", min_width=20.0, min_space=5.0,
            bottom=dummy_prims.metal, min_bottom_enclosure=_prp.Enclosure(1.0),
        )
        for prim in (*dummy_prims, pad):
            self.assertIs(disp(prim), type(prim))
