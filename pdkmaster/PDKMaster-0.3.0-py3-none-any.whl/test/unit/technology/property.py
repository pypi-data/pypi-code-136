# SPDX-License-Identifier: GPL-2.0-or-later OR AGPL-3.0-or-later OR CERN-OHL-S-2.0+
# type: ignore
import unittest

from pdkmaster.technology import property_ as _prp


class PropertyTest(unittest.TestCase):
    def test_enclosure(self):
        with self.assertRaises(ValueError):
            _prp.Enclosure((0.0, 0.1, 0.2))

        enc1 = _prp.Enclosure(2.0)
        enc2 = _prp.Enclosure((1.0, 2.0))
        enc3 = _prp.Enclosure((2.0, 1.0))

        self.assertEqual(hash(enc1), hash(enc1.spec))
        self.assertFalse(enc1.is_assymetric)
        self.assertTrue(enc2.is_assymetric)
        self.assertNotEqual(enc1, 2.0)
        self.assertEqual(enc2.min(), 1.0)
        self.assertEqual(enc2.max(), 2.0)
        self.assertEqual(enc2.tall(), enc2)
        self.assertNotEqual(enc3.tall(), enc3)
        self.assertEqual(enc3.tall(), enc2)
        self.assertNotEqual(enc2.wide(), enc2)
        self.assertEqual(enc2.wide(), enc3)
        self.assertEqual(enc3.wide(), enc3)

    def test_property(self):
        class WrongProp(_prp.Property):
            value_conv = _prp.Property
            value_type = _prp.Property
            value_type_str = "Property"

        class StrProperty(_prp.Property):
            value_conv = None
            value_type = str
            value_type_str = "str"

        with self.assertRaises(TypeError):
            WrongProp(name="wrongprop")

        prop = _prp.Property(name="height")

        self.assertEqual(hash(prop), hash(prop.name))
        with self.assertRaises(TypeError):
            prop.cast(None)
        with self.assertRaises(TypeError):
            prop.cast("a")

        id = StrProperty(name="id")
        with self.assertRaises(TypeError):
            id.cast(2.3)

    def test_enclosureproperty(self):
        prop = _prp.EnclosureProperty(name="enclosure")

        self.assertEqual(prop.cast(2.3), _prp.Enclosure(2.3))

    def test_binarypropcond(self):
        class WrongCond(_prp._Comparison):
            pass

        with self.assertRaises(TypeError):
            WrongCond(left=None, right=None)

        prop = _prp.Property(name="width")
        cond1 = prop > 1.0
        cond2 = prop > 1.0
        cond3 = prop > 2.0
        cond4 = prop == 1.0
        cond5 = prop < 1.0
        cond6 = prop <= 1.0
        cond7 = prop >= 1.0

        self.assertEqual(cond1, cond2)
        self.assertNotEqual(cond1, cond3)
        self.assertNotEqual(cond1, cond4)
        self.assertNotEqual(cond1, cond5)
        self.assertNotEqual(cond1, cond6)
        self.assertNotEqual(cond1, cond7)
        self.assertEqual(repr(cond1), "Property(name='width', allow_non=False) > 1.0")
        with self.assertRaises(TypeError):
            bool(cond1)
        self.assertFalse(cond4)
