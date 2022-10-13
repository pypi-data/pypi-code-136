# SPDX-License-Identifier: GPL-2.0-or-later OR AGPL-3.0-or-later OR CERN-OHL-S-2.0+
# type: ignore
import unittest

from pdkmaster.technology import mask as _msk, wafer_ as _wfr
from pdkmaster.dispatch.mask import MaskDispatcher


# Simple dispatcher that just returns the type of the mask
class MyDispatcher(MaskDispatcher):
    def _Mask(self, mask: _msk._Mask):
        return type(mask)


class MaskDispatchTest(unittest.TestCase):
    def test_notimplemented(self):
        with self.assertRaises(NotImplementedError):
            # Call ShapeDispatched._Shape() method
            MaskDispatcher()(_msk.DesignMask(
                name="test", fill_space="yes",
            ))

    def test_dispatch(self):
        disp = MyDispatcher()

        with self.assertRaises(RuntimeError):
            disp("error")

        mask1 = _msk.DesignMask(name="mask1", fill_space="yes")
        mask2 = _msk.DesignMask(name="mask2", fill_space="no")
        alias = mask1.alias("alias")
        partswith = mask1.parts_with(mask1.width > 1.0)
        join = _msk.Join(masks=(mask1, mask2))
        intersect = _msk.Intersect(masks=(mask1, mask2))
        rem = mask1.remove(mask2)
        samenet = mask1.same_net

        # Just run with all mask to get code coverage
        masks = (
            mask1, mask2, alias, partswith, join, intersect,
            rem, samenet, _wfr.wafer,
        )
        for mask in masks:
            self.assertIs(disp(mask), type(mask))
