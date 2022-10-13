# SPDX-License-Identifier: GPL-2.0-or-later OR AGPL-3.0-or-later OR CERN-OHL-S-2.0+
# type: ignore
import unittest

from pdkmaster.technology import mask as _msk, wafer_ as _wfr

class WaferTest(unittest.TestCase):
    def test_error(self):
        with self.assertRaises(ValueError):
            _wfr._Wafer()

    def test_wafer(self):
        self.assertEqual(_wfr.wafer, _wfr.wafer)
        self.assertEqual(hash(_wfr.wafer), hash(_wfr.wafer))
        self.assertEqual(_wfr.wafer.designmasks, tuple())

    def test_outside(self):
        mask1 = _msk.DesignMask(name="mask1", fill_space="yes")
        mask2 = _msk.DesignMask(name="mask2", fill_space="no")
        masks = (mask1, mask2)
        self.assertEqual(_wfr.outside(mask1), _wfr.wafer.remove(mask1))
        self.assertEqual(
            _wfr.outside(masks, alias="out"),
            _wfr.wafer.remove(_msk.Join(masks)).alias("out")
        )

    def test_substratenet(self):
        self.assertNotEqual(
            _wfr.SubstrateNet(name="substrate"),
            _wfr.SubstrateNet(name="sub2"),
        )