# SPDX-License-Identifier: GPL-2.0-or-later OR AGPL-3.0-or-later OR CERN-OHL-S-2.0+
# type: ignore
import unittest

from pdkmaster.technology import mask as _msk, property_ as _prp, rule as _rle
from pdkmaster.dispatch.rule import RuleDispatcher


# Simple dispatcher that just returns the type of the edge
class MyDispatcher(RuleDispatcher):
    def _Rule(self, rule: _rle._Rule):
        return type(rule)


class EdgeDispatchTest(unittest.TestCase):
    def test_notimplemented(self):
        with self.assertRaises(NotImplementedError):
            # Call ShapeDispatched._Shape() method
            mask = _msk.DesignMask(name="test", fill_space="yes")
            RuleDispatcher()(mask)

    def test_dispatch(self):
        disp = MyDispatcher()

        with self.assertRaises(RuntimeError):
            disp("error")

        prop = _prp.Property(name="prop")

        # _prp.Operators
        gt = prop > 1.0
        ge = prop >= 1.0
        sm = prop < 1.0
        se = prop <= 1.0
        eq = prop == 1.0

        mask1 = _msk.DesignMask(name="mask1", fill_space="yes")
        mask2 = _msk.DesignMask(name="mask2", fill_space="yes")

        alias = mask1.alias("alias")

        inside = mask1.is_inside(mask2)
        outside = mask2.is_outside(mask2)

        connect = _msk.Connect(mask1=mask1, mask2=mask2)

        # Just run with all mask to get code coverage
        rules = (
            gt, ge, sm, se, eq,
            mask1, alias, inside, outside, connect,
        )
        for rule in rules:
            self.assertIs(disp(rule), type(rule))
