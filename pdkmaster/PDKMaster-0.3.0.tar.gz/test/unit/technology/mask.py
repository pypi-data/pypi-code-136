# SPDX-License-Identifier: GPL-2.0-or-later OR AGPL-3.0-or-later OR CERN-OHL-S-2.0+
# type: ignore
import unittest

from pdkmaster.technology import mask as _msk


class MaskTest(unittest.TestCase):
    def test_error(self):
        class WrongCond(_msk._MultiMaskCondition):
            pass

        with self.assertRaises(AttributeError):
            WrongCond(
                mask=_msk.DesignMask(name="MyMask", fill_space="no"),
                others=_msk.DesignMask(name="Other", fill_space="yes"),
            )

        mask = _msk.DesignMask(name="mask", fill_space="yes")

        with self.assertRaises(ValueError):
            _msk.Spacing(mask1=mask, mask2=mask)
        with self.assertRaises(ValueError):
            _msk.OverlapWidth(mask1=mask, mask2=mask)

    def test_nmask(self):
        with self.assertRaises(ValueError):
            _msk.DesignMask(name="MyMask", fill_space="bollocks")

        # We use DesignMask object to also cover code for _Mask and other
        # classes
        mask = _msk.DesignMask(name="MyMask", fill_space="yes")
        mask2 = _msk.DesignMask(name="MyMask2", fill_space="no")
        mask3 = _msk.DesignMask(name="MyMask3", fill_space="no")
        
        alias = mask.alias("Alias")
        samenet = mask.same_net

        cond = mask.width >= 1.0
        cond2 = mask2.length <= 2.0

        self.assertEqual(mask.width, _msk._MaskProperty(mask=mask, name="width"))
        self.assertNotEqual(mask.width, mask.length)
        self.assertEqual(
            mask.extend_over(other=mask2),
            _msk._DualMaskProperty(
                mask1=mask, mask2=mask2, name="extend_over", commutative=False,
            ),
        )
        self.assertNotEqual(
            mask.extend_over(other=mask2),
            _msk._DualMaskProperty(
                mask1=mask, mask2=mask3, name="extend_over", commutative=False,
            ),
        )
        self.assertEqual(
            mask.enclosed_by(other=mask2),
            _msk._DualMaskEnclosureProperty(
                mask1=mask, mask2=mask2, name="enclosed_by",
            ),
        )
        self.assertEqual(
            mask.is_inside(mask2, mask3),
            _msk._InsideCondition(mask=mask, others=(mask3, mask2)),
        )
        self.assertEqual(
            mask.is_outside(mask2),
            _msk._OutsideCondition(mask=mask, others=(mask2)),
        )
        self.assertEqual(
            mask.parts_with(cond),
            _msk._PartsWith(mask=mask, condition=cond),
        )
        with self.assertRaises(TypeError):
            mask.parts_with(cond2)
        self.assertEqual(
            mask.remove(mask2),
            _msk._MaskRemove(from_=mask, what=mask2),
        )
        self.assertEqual(
            alias, _msk._MaskAlias(mask=mask, name="Alias"),
        )
        self.assertEqual(samenet, _msk._SameNet(mask))

        self.assertNotEqual(alias, "")
        self.assertNotEqual(samenet, "")
        self.assertNotEqual(mask.extend_over(other=mask2), "")
        self.assertNotEqual(mask.enclosed_by(other=mask2), "")
        self.assertNotEqual(mask.is_inside(mask2, mask3), "")
        self.assertNotEqual(mask.is_outside(mask2), "")
        self.assertNotEqual(mask.parts_with(cond), "")
        self.assertNotEqual(mask.remove(mask2), "")
        self.assertNotEqual(_msk.Join((mask, mask2)), "")
        self.assertNotEqual(_msk.Intersect((mask, mask3)), "")

        self.assertEqual(tuple(mask.designmasks), (mask,))
        self.assertEqual(samenet.designmasks, (mask,))
        self.assertEqual(set(mask.parts_with(cond).designmasks), {mask})
        self.assertEqual(set(mask.remove(mask2).designmasks), {mask, mask2})
        self.assertEqual(set(_msk.Join((mask, mask2)).designmasks), {mask, mask2})
        self.assertEqual(
            set(_msk.Intersect((mask, mask2, mask3)).designmasks),
            {mask, mask2, mask3},
        )

        self.assertEqual(_msk.Join((mask, mask2)), _msk.Join((mask2, mask)))
        self.assertEqual(_msk.Intersect((mask, mask2)), _msk.Intersect((mask2, mask)))

        self.assertEqual(
            mask.parts_with(cond).name, 
            f"{mask.name}.parts_with({cond})",
        )
        self.assertEqual(
            mask.remove(mask2).name,
            f"{mask.name}.remove({mask2.name})",
        )
        self.assertEqual(
            _msk.Join((mask, mask2)).name,
            f"join({mask.name},{mask2.name})"
        )
        self.assertEqual(
            _msk.Intersect((mask, mask2, mask3)).name,
            f"intersect({mask.name},{mask2.name},{mask3.name})"
        )

        self.assertEqual(hash(alias), hash(alias.name))
        self.assertEqual(hash(samenet), hash(samenet.name))
        self.assertEqual(
            hash(mask.is_inside(mask2, mask3)),
            hash(_msk._InsideCondition(mask=mask, others=(mask3, mask2))),
        )
        self.assertEqual(
            hash(mask.parts_with(cond)), 
            hash(f"{mask.name}.parts_with({cond})"),
        )
        self.assertEqual(
            hash(mask.remove(mask2)),
            hash((mask, mask2)),
        )
        self.assertEqual(
            hash(mask.remove(_msk.Join((mask2, mask3)))),
            hash(mask.remove(_msk.Join((mask3, mask2)))),
        )
        self.assertEqual(
            hash(_msk.Join((mask, mask2))),
            hash(_msk.Join((mask2, mask))),
        )
        self.assertEqual(
            hash(_msk.Intersect((mask, mask2))),
            hash(_msk.Intersect((mask2, mask))),
        )

        self.assertEqual(
            mask.parts_with(cond).name, 
            f"{mask.parts_with(cond)!r}", 
        )
        self.assertEqual(
            f"{mask.is_inside(mask2)!r}",
            f"{mask!r}.is_inside({mask2!r})",
        )

    def test_connect(self):
        mask = _msk.DesignMask(name="mask", fill_space="no")
        mask2 = _msk.DesignMask(name="mask2", fill_space="no")
        mask3 = _msk.DesignMask(name="mask3", fill_space="no")

        self.assertEqual(
            _msk.Connect(mask, mask2), _msk.Connect(mask2, mask),
        )
        self.assertEqual(
            _msk.Connect(mask, (mask2, mask3)), _msk.Connect((mask3, mask2), mask),
        )

        self.assertEqual(
            hash(_msk.Connect(mask, mask2)), hash(_msk.Connect(mask2, mask)),
        )
        self.assertEqual(
            hash(_msk.Connect(mask, (mask2, mask3))),
            hash(_msk.Connect((mask3, mask2), mask)),
        )
