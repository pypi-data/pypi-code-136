# SPDX-License-Identifier: GPL-2.0-or-later OR AGPL-3.0-or-later OR CERN-OHL-S-2.0+
# type: ignore
import unittest

from pdkmaster.technology import mask as _msk, edge as _edg

class GeometryTest(unittest.TestCase):
    def test_error(self):
        mask1 = _msk.DesignMask(name="mask1", fill_space="yes")
        mask2 = _msk.DesignMask(name="mask2", fill_space="no")

        with self.assertRaises(TypeError):
            _edg.Intersect((mask1, mask2))

    def test_edgeproperty(self):
        mask1 = _msk.DesignMask(name="mask1", fill_space="yes")
        mask2 = _msk.DesignMask(name="mask2", fill_space="no")

        edge1 = _edg.MaskEdge(mask1)
        edge2 = _edg.MaskEdge(mask2)

        # Just do coverage of code
        prop1 = _edg._DualEdgeProperty(
            edge1=edge1, edge2=edge2, name="prop1",
            commutative=True, allow_mask2=False,
        )
        prop2 = _edg._DualEdgeProperty(
            edge1=edge2, edge2=edge1, name="prop2",
            commutative=False, allow_mask2=True,
        )

    def test_maskedge(self):
        mask1 = _msk.DesignMask(name="mask1", fill_space="yes")
        mask2 = _msk.DesignMask(name="mask2", fill_space="no")

        # Just do coverage of code
        edge1 = _edg.MaskEdge(mask1)
        edge2 = _edg.MaskEdge(mask2)

        _edg.Join((edge1, edge2))
        _edg.Intersect((edge1, edge2))
        edge1.enclosed_by(edge2)
