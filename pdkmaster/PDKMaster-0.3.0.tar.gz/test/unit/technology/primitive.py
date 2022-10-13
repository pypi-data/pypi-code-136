# SPDX-License-Identifier: GPL-2.0-or-later OR AGPL-3.0-or-later OR CERN-OHL-S-2.0+
# type: ignore
from re import M
import unittest

from pdkmaster.technology import (
    property_ as _prp, rule as _rle, wafer_ as _wfr, mask as _msk, primitive as _prm,
    technology_ as _tch,
)

from ..dummy import dummy_tech

class PrimitiveTest(unittest.TestCase):
    def test_simple(self):
        """Some simple tests not wanting to define own method
        """
        dummy_prims = dummy_tech.primitives

        # _Primitive
        with self.assertRaises(TypeError):
            _prm._Primitive(name="error")
        with self.assertRaises(ValueError):
            dummy_prims.metal._derive_rules(tech=dummy_tech)

        # _IntParam
        with self.assertRaises(TypeError):
            _prm._IntParam(
                primitive=dummy_prims.active, name="error", default=dummy_prims,
            )
        self.assertIsInstance(
            _prm._IntParam(primitive=dummy_prims.active, name="rule") == 1,
            _rle._Rule,
        )
        self.assertEqual(
            _prm._IntParam(
                primitive=dummy_prims.active, name="default", default=2,
            ).cast(None),
            2,
        )

        # _PrimitiveParam
        with self.assertRaises(TypeError):
            _prm._PrimitiveParam(
                primitive=dummy_prims.nplus, name="error", choices=dummy_prims.pplus,
            )
        with self.assertRaises(TypeError):
            _prm._PrimitiveParam(
                primitive=dummy_prims.nplus, name="error", choices=("e1", "e2"),
            )
        # _EnclosureParam
        self.assertEqual(
            _prm._EnclosureParam(
                primitive=dummy_prims.active, name="error", default=_prp.Enclosure(0.2),
            ).cast(None),
            _prp.Enclosure(0.2),
        )
        with self.assertRaises(TypeError):
            _prm._EnclosureParam(
                primitive=dummy_prims.active, name="error", allow_none=False,
            ).cast(None)

        # _EnclosuresParam
        with self.assertRaises(TypeError):
            self.assertEqual(
                _prm._EnclosuresParam(
                    primitive=dummy_prims.nmos, name="error", allow_none=False, n=1,
                ).cast(None)
            )

        # _DesignMaskPrimitive
        with self.assertRaises(TypeError):
            class MyPrim(_prm._DesignMaskPrimitive):
                def fill_space(self) -> str:
                    return "no"

                def __init__(self, *, name: str, **super_args):
                    super().__init__(name=name, **super_args)

                def _generate_rules(self, *, tech, gen_mask):
                    return super()._generate_rules(tech=tech, gen_mask=gen_mask)
            mask = _msk.DesignMask(name="error", fill_space="no")
            MyPrim(name="error", mask=mask)

        # _Intersect
        with self.assertRaises(ValueError):
            # only one prim for _Intersect
            _prm._Intersect(prims=(dummy_prims.active,))

    def test_marker(self):
        marker = _prm.Marker(name="TestMarker")
        marker2 = _prm.Marker(name="TestMarker2")

        with self.assertRaises(AttributeError):
            # Accessing rules before they are generated.
            marker2.rules

        rules = tuple(marker._generate_rules(tech=dummy_tech))
        self.assertEqual(rules[0], _msk.DesignMask(name="TestMarker", fill_space="yes"))

        param0 = marker.params[0]
        self.assertEqual(param0.primitive, marker)
        self.assertEqual(param0.name, "width")
        self.assertEqual(param0.value_type, float)

        self.assertEqual(marker.params[0], marker.params[0])
        self.assertNotEqual(marker.params[0], marker2.params[0])

    def test_auxiliary(self):
        prim1 = _prm.Auxiliary(name="prim1")
        prim1bis = _prm.Auxiliary(name="prim1")
        prim2 = _prm.Auxiliary(name="prim2")

        self.assertEqual(prim1, prim1bis)
        self.assertNotEqual(prim1, prim2)

        rules = tuple(prim1._generate_rules(tech=dummy_tech))
        self.assertIn(prim1.mask, rules)

    def test_extraprocess(self):
        with self.assertRaises(ValueError):
            # wrong fill_space value
            _prm.ExtraProcess(
                name="prim1", min_width=1.0, min_space=1.0, fill_space="same_net",
            )
        with self.assertRaises(TypeError):
            _prm.ExtraProcess(name="Step1", fill_space="yes")

        prim1 = _prm.ExtraProcess(
            name="prim1", min_width=1.0, min_space=1.0, fill_space="yes",
        )
        prim1bis = _prm.ExtraProcess(
            name="prim1", min_width=1.0, min_space=1.0, fill_space="yes",
        )
        prim2 = _prm.ExtraProcess(
            name="prim2", min_width=0.2, min_space=0.5, fill_space="yes",
        )

        self.assertEqual(prim1, prim1bis)
        self.assertNotEqual(prim1, prim2)

        self.assertEqual(prim1.fill_space, "yes")

        rules = tuple(prim1._generate_rules(tech=dummy_tech))
        self.assertIn(prim1.mask, rules)

    def test_implant(self):
        with self.assertRaises(ValueError):
            _prm.Implant(name="error", type_="unknown")

        prim1 = _prm.Implant(name="prim1", min_width=1.0, min_space=1.0, type_="n")
        prim1bis = _prm.Implant(name="prim1", min_width=1.0, min_space=1.0, type_="n")
        prim2 = _prm.Implant(name="prim2", min_width=0.2, min_space=0.5, type_="p")

        self.assertEqual(prim1, prim1bis)
        self.assertNotEqual(prim1, prim2)

        self.assertEqual(prim1.fill_space, "yes")

        rules = tuple(prim1._generate_rules(tech=dummy_tech))
        self.assertIn(prim1.mask, rules)

    def test_insulator(self):
        with self.assertRaises(ValueError):
            # Wrong fill_space value
            _prm.Insulator(
                name="prim1", min_width=0.5, min_space=0.5, fill_space="same_net"
            )

        prim1 = _prm.Insulator(
            name="prim1", min_width=0.5, min_space=0.5, fill_space="yes"
        )
        prim1bis = _prm.Insulator(
            name="prim1", min_width=0.5, min_space=0.5, fill_space="yes"
        )
        prim2 = _prm.Insulator(
            name="prim2", min_width=0.5, min_space=0.5, fill_space="no"
        )

        self.assertEqual(prim1, prim1bis)
        self.assertNotEqual(prim1, prim2)

        rules = tuple(prim1._generate_rules(tech=dummy_tech))
        self.assertIn(prim1.mask, rules)

    def test_well(self):
        with self.assertRaises(TypeError):
            _prm.Well(name="prim1", min_width=1.0, min_space=1.0)
        with self.assertRaises(ValueError):
            _prm.Well(
                name="prim2", min_width=0.2, min_space=0.5, min_space_samenet=0.6,
                type_="n",
            )

        prim1 = _prm.Well(name="prim1", min_width=1.0, min_space=1.0, type_="n")
        prim1bis = _prm.Well(name="prim1", min_width=1.0, min_space=1.0, type_="n")
        prim2 = _prm.Well(
            name="prim2", min_width=0.2, min_space=0.5, min_space_samenet=0.25,
            type_="n",
        )

        self.assertEqual(prim1, prim1bis)
        self.assertNotEqual(prim1, prim2)

        self.assertEqual(prim1.fill_space, "same_net")

        rules = tuple(prim2._generate_rules(tech=dummy_tech))
        self.assertIn(prim2.mask, rules)

    def test_deepwell(self):
        with self.assertRaises(TypeError):
            _prm.DeepWell(name="prim1", min_width=1.0, min_space=1.0)
        with self.assertRaises(TypeError):
            _prm.DeepWell(name="prim1", min_width=1.0, min_space=1.0, type_="p")

        well1 = _prm.Well(name="well1", min_width=1.0, min_space=1.0, type_="n")
        well2 = _prm.Well(name="well2", min_width=1.0, min_space=1.0, type_="p")

        with self.assertRaises(ValueError):
            _prm.DeepWell(
                name="typemismatch", min_width=1.0, min_space=1.0, well=well1, type_="p",
                min_well_overlap=1.5, min_well_enclosure=2.0,
            )

        prim1 = _prm.DeepWell(
            name="prim1", min_width=1.0, min_space=1.0, well=well1, type_="n",
            min_well_overlap=1.5, min_well_enclosure=2.0,
        )
        prim1bis = _prm.DeepWell(
            name="prim1", min_width=1.0, min_space=1.0, well=well1, type_="n",
            min_well_overlap=1.5, min_well_enclosure=2.0,
        )
        prim2 = _prm.DeepWell(
            name="prim2", min_width=0.2, min_space=0.5, well=well2,
            min_well_overlap=1.5, min_well_enclosure=2.0,
        )

        self.assertEqual(prim1, prim1bis)
        self.assertNotEqual(prim1, prim2)

        self.assertEqual(prim1.fill_space, "same_net")

        rules = tuple(prim2._generate_rules(tech=dummy_tech))
        self.assertIn(prim2.mask, rules)

    def test_waferwire(self):
        nimpl = _prm.Implant(name="nimplant", min_width=1.0, min_space=1.0, type_="n")
        pimpl = _prm.Implant(name="pimplant", min_width=1.0, min_space=1.0, type_="p")
        oxide = _prm.Insulator(name="oxide", min_width=1.0, min_space=1.0, fill_space="yes")
        well = _prm.Well(name="well", min_width=1.0, min_space=1.0, type_="p")
        well2 = _prm.Well(name="well2", min_width=1.0, min_space=1.0, type_="n")

        with self.assertRaises(TypeError):
            _prm.WaferWire(name="prim1", min_width=1.0, min_space=1.0)

        with self.assertRaises(_prm.UnconnectedPrimitiveError):
            # Unconnected well
            _prm.WaferWire(
                name="prim1", min_width=1.0, min_space=1.0,
                allow_in_substrate=True,
                implant=nimpl, min_implant_enclosure=_prp.Enclosure(0.05),
                implant_abut="all", allow_contactless_implant=False,
                well=well, min_well_enclosure=_prp.Enclosure(0.1),
                allow_well_crossing=False,
            )
        with self.assertRaises(TypeError):
            # well not implant
            _prm.WaferWire(
                name="prim1", min_width=1.0, min_space=1.0,
                allow_in_substrate=True,
                implant=(nimpl, well), min_implant_enclosure=_prp.Enclosure(0.05),
                implant_abut="all", allow_contactless_implant=False,
                well=well, min_well_enclosure=_prp.Enclosure(0.1),
                allow_well_crossing=False,
            )
        with self.assertRaises(ValueError):
            # wrong implant_abut string
            _prm.WaferWire(
                name="prim1", min_width=1.0, min_space=1.0,
                allow_in_substrate=True,
                implant=pimpl, min_implant_enclosure=_prp.Enclosure(0.05),
                implant_abut="", allow_contactless_implant=False,
                well=well, min_well_enclosure=_prp.Enclosure(0.1),
                allow_well_crossing=False,
            )
        with self.assertRaises(ValueError):
            # wrong implant_abut value
            _prm.WaferWire(
                name="prim1", min_width=1.0, min_space=1.0,
                allow_in_substrate=True,
                implant=pimpl, min_implant_enclosure=_prp.Enclosure(0.05),
                implant_abut=nimpl, allow_contactless_implant=False,
                well=well, min_well_enclosure=_prp.Enclosure(0.1),
                allow_well_crossing=False,
            )
        with self.assertRaises(TypeError):
            # min_well_enclosure not specified for multiple wells
            _prm.WaferWire(
                name="prim1", min_width=1.0, min_space=1.0,
                allow_in_substrate=True,
                implant=(nimpl, pimpl), min_implant_enclosure=_prp.Enclosure(0.05),
                implant_abut="all", allow_contactless_implant=False,
                well=(well, well), min_well_enclosure=_prp.Enclosure(0.1),
                allow_well_crossing=False,
            )
        with self.assertRaises(TypeError):
            # min_substrate_enclosure_same_type not None with min_substrate_enclosure
            # None
            prim1 = _prm.WaferWire(
                name="prim1", min_width=1.0, min_space=1.0,
                allow_in_substrate=True, min_substrate_enclosure_same_type=_prp.Enclosure(0.08),
                implant=(nimpl, pimpl), min_implant_enclosure=_prp.Enclosure(0.05),
                implant_abut="all", allow_contactless_implant=False,
                well=well, min_well_enclosure=_prp.Enclosure(0.1),
                allow_well_crossing=False,
            )
        with self.assertRaises(TypeError):
            # min_substrate_enclosure given with allow_in_substrate=False
            prim1 = _prm.WaferWire(
                name="prim1", min_width=1.0, min_space=1.0,
                allow_in_substrate=False, min_substrate_enclosure=_prp.Enclosure(0.1),
                implant=(nimpl, pimpl), min_implant_enclosure=_prp.Enclosure(0.05),
                implant_abut="all", allow_contactless_implant=False,
                well=well, min_well_enclosure=_prp.Enclosure(0.1),
                allow_well_crossing=False,
            )
        with self.assertRaises(ValueError):
            # min_oxide_enclosure without oxide
            prim1 = _prm.WaferWire(
                name="prim1", min_width=1.0, min_space=1.0,
                allow_in_substrate=True,
                implant=(nimpl, pimpl), min_implant_enclosure=_prp.Enclosure(0.05),
                implant_abut="all", allow_contactless_implant=False,
                well=well, min_well_enclosure=_prp.Enclosure(0.1),
                allow_well_crossing=False,
                min_oxide_enclosure=_prp.Enclosure(0.01),
            )

        prim1 = _prm.WaferWire(
            name="prim1", min_width=1.0, min_space=1.0,
            allow_in_substrate=True,
            implant=(nimpl, pimpl), min_implant_enclosure=_prp.Enclosure(0.05),
            implant_abut="all", allow_contactless_implant=False,
            well=well, min_well_enclosure=_prp.Enclosure(0.1),
            min_well_enclosure_same_type=_prp.Enclosure(0.08),
            min_substrate_enclosure=_prp.Enclosure(0.15),
            min_substrate_enclosure_same_type=_prp.Enclosure(0.1),
            allow_well_crossing=False,
        )
        prim1bis = _prm.WaferWire(
            name="prim1", min_width=1.0, min_space=1.0,
            allow_in_substrate=True,
            implant=(nimpl, pimpl), min_implant_enclosure=_prp.Enclosure(0.05),
            implant_abut="all", allow_contactless_implant=False,
            well=well, min_well_enclosure=_prp.Enclosure(0.1),
            min_well_enclosure_same_type=_prp.Enclosure(0.08),
            min_substrate_enclosure=_prp.Enclosure(0.15),
            min_substrate_enclosure_same_type=_prp.Enclosure(0.1),
            allow_well_crossing=False,
        )
        prim2 = _prm.WaferWire(
            name="prim2", min_width=0.2, min_space=0.5,
            allow_in_substrate=False,
            implant=pimpl, min_implant_enclosure=_prp.Enclosure(0.05),
            implant_abut=pimpl, allow_contactless_implant=False,
            well=well, min_well_enclosure=_prp.Enclosure(0.1),
            min_well_enclosure_same_type=_prp.Enclosure(0.08),
            allow_well_crossing=False,
            oxide=oxide, min_oxide_enclosure=_prp.Enclosure(0.08),
        )
        prim3 = _prm.WaferWire(
            name="prim3", min_width=1.0, min_space=1.0,
            allow_in_substrate=True,
            implant=(nimpl, pimpl), min_implant_enclosure=_prp.Enclosure(0.05),
            implant_abut="all", allow_contactless_implant=False,
            well=well, min_well_enclosure=_prp.Enclosure(0.1),
            min_well_enclosure_same_type=(None,),
            allow_well_crossing=False,
        )

        self.assertEqual(prim1, prim1bis)
        self.assertNotEqual(prim1, prim2)
        self.assertNotEqual(prim1, prim3)

        self.assertEqual(prim1.fill_space, "same_net")

        rules = tuple(prim1._generate_rules(tech=dummy_tech))
        self.assertIn(prim1.mask, rules)
        rules = tuple(prim2._generate_rules(tech=dummy_tech))
        self.assertIn(prim2.mask, rules)
        rules = tuple(prim3._generate_rules(tech=dummy_tech))
        self.assertIn(prim3.mask, rules)

        # cast_params
        # different variations for code coverage
        with self.assertRaises(ValueError):
            prim1 = _prm.WaferWire(
                name="prim1", min_width=1.0, min_space=1.0,
                allow_in_substrate=False,
                implant=(nimpl, pimpl), min_implant_enclosure=_prp.Enclosure(0.05),
                implant_abut="all", allow_contactless_implant=False,
                well=(well, well2), min_well_enclosure=_prp.Enclosure(0.1),
                allow_well_crossing=False,
            ).cast_params({
                "implant": nimpl,
            })
        prim1.cast_params({
            "implant": nimpl,
        })
        with self.assertRaises(TypeError):
            prim1.cast_params({
                "implant": nimpl,
                "error": "error",
            })
        prim1.cast_params({
            "implant": nimpl,
            "implant_enclosure": _prp.Enclosure((0.5, 0.3)),
        })
        params = prim1.cast_params({
            "implant": nimpl,
            "implant_enclosure": 0.3,
        })
        self.assertEqual(
            params["implant_enclosure"],
            _prp.Enclosure(0.3),
        )
        with self.assertRaises(TypeError):
            params = prim1.cast_params({
                "implant": nimpl,
                "implant_enclosure": prim1,
            })
        with self.assertRaises(ValueError):
            params = prim1.cast_params({
                "implant": nimpl,
                "portnets": {"error": _wfr.SubstrateNet(name="gnd")}
            })
        prim1.cast_params({
            "implant": nimpl,
            "well": well,
            "well_net": _wfr.SubstrateNet(name="bulk"),
        })
        with self.assertRaises(TypeError):
            # no well_net for well
            prim1.cast_params({
                "implant": nimpl,
                "well": well,
            })
        with self.assertRaises(TypeError):
            # well_net without well
            prim1.cast_params({
                "implant": nimpl,
                "well_net": _wfr.SubstrateNet(name="bulk"),
            })
        prim2.cast_params({
            "well_net": _wfr.SubstrateNet(name="bulk"),
            "oxide": oxide,
        })

        # _WaferWireIntersect
        # Not a good layer for prim1
        with self.assertRaises(ValueError):
            prim1.in_(_wfr.wafer)

    def test_metalwire(self):
        with self.assertRaises(TypeError):
            # Wrong value in space_table
            _prm.MetalWire(
                name="prim1", min_width=1.0, min_space=1.0, space_table=(
                    (2.0, 2.0),
                    ((10.0, 3.0, 2.0), 3.0),
                ),
                min_area=2.0, min_density=0.4, max_density=0.8,
            )
        with self.assertRaises(ValueError):
            # wrong min_density value
            _prm.MetalWire(
                name="prim1", min_width=1.0, min_space=1.0, space_table=(
                    (2.0, 2.0),
                    ((10.0, 3.0), 3.0),
                ),
                min_area=2.0, min_density=40, max_density=0.8,
            )
        with self.assertRaises(ValueError):
            # wrong max_density value
            _prm.MetalWire(
                name="prim1", min_width=1.0, min_space=1.0, space_table=(
                    (2.0, 2.0),
                    ((10.0, 3.0), 3.0),
                ),
                min_area=2.0, min_density=0.4, max_density=80,
            )

        prim1 = _prm.MetalWire(
            name="prim1", min_width=1.0, min_space=1.0, space_table=(
                (2.0, 2.0),
                ((10.0, 3.0), 3.0),
            ),
            min_area=2.0, min_density=0.4, max_density=0.8,
        )
        prim1bis = _prm.MetalWire(
            name="prim1", min_width=1.0, min_space=1.0, space_table=(
                (2.0, 2.0),
                ((10.0, 3.0), 3.0),
            ),
            min_area=2.0, min_density=0.4, max_density=0.8,
        )
        prim2 = _prm.MetalWire(
            name="prim2", min_width=1.0, min_space=1.0, grid=0.2,
        )

        self.assertEqual(prim1, prim1bis)
        self.assertNotEqual(prim1, prim2)

        rules = tuple(prim1._generate_rules(tech=dummy_tech))
        self.assertIn(prim1.mask, rules)
        rules = tuple(prim2._generate_rules(tech=dummy_tech))
        self.assertIn(prim2.mask, rules)

    def test_via(self):
        nimpl = _prm.Implant(name="nimplant", min_width=0.5, min_space=0.5, type_="n")
        nimpl2 = _prm.Implant(name="nimplant2", min_width=0.5, min_space=0.5, type_="n")
        pimpl = _prm.Implant(name="pimplant", min_width=0.5, min_space=0.5, type_="p")
        oxide = _prm.Insulator(name="oxide", min_width=1.0, min_space=1.0, fill_space="yes")
        well = _prm.Well(name="well", min_width=1.0, min_space=1.0, type_="p")
        well2 = _prm.Well(name="well2", min_width=1.0, min_space=1.0, type_="n")
        active = _prm.WaferWire(
            name="aa", min_width=1.0, min_space=1.0,
            allow_in_substrate=True,
            implant=(nimpl, pimpl), min_implant_enclosure=_prp.Enclosure(0.05),
            implant_abut="all", allow_contactless_implant=False,
            well=well, min_well_enclosure=_prp.Enclosure(0.1),
            min_substrate_enclosure=_prp.Enclosure(0.15),
            allow_well_crossing=False,
            oxide=oxide,
        )
        active2 = _prm.WaferWire(
            name="aa2", min_width=1.0, min_space=1.0,
            allow_in_substrate=False,
            implant=(nimpl, pimpl), min_implant_enclosure=_prp.Enclosure(0.05),
            implant_abut="all", allow_contactless_implant=False,
            well=well, min_well_enclosure=_prp.Enclosure(0.1),
            allow_well_crossing=False,
            oxide=oxide,
        )
        m1 = _prm.MetalWire(name="metal1", min_width=1.0, min_space=1.0)
        m2 = _prm.TopMetalWire(name="metal2", min_width=1.0, min_space=1.0)
        m3 = _prm.MetalWire(name="metal3", min_width=1.0, min_space=1.0)

        with self.assertRaises(TypeError):
            # TopMetalWire as bottom
            _prm.Via(
                name="prim1", width=0.8, min_space=0.8,
                bottom=m2, min_bottom_enclosure=_prp.Enclosure(0.2),
                top=m2, min_top_enclosure=_prp.Enclosure(0.2),
            )

        prim1 = _prm.Via(
            name="prim1", width=0.8, min_space=0.8,
            bottom=active, min_bottom_enclosure=_prp.Enclosure(0.2),
            top=m1, min_top_enclosure=_prp.Enclosure(0.2),
        )
        prim1bis = _prm.Via(
            name="prim1", width=0.8, min_space=0.8,
            bottom=active, min_bottom_enclosure=_prp.Enclosure(0.2),
            top=m1, min_top_enclosure=_prp.Enclosure(0.2),
        )
        prim2 = _prm.Via(
            name="prim2", width=0.8, min_space=0.8,
            bottom=m1, min_bottom_enclosure=_prp.Enclosure(0.2),
            top=(m1, m2), min_top_enclosure=_prp.Enclosure(0.2),
        )
        prim3 = _prm.Via(
            name="prim3", width=0.8, min_space=0.8,
            bottom=(m1, active2), min_bottom_enclosure=_prp.Enclosure(0.2),
            top=m2, min_top_enclosure=_prp.Enclosure(0.2),
        )

        self.assertEqual(prim1, prim1bis)
        self.assertNotEqual(prim1, prim2)
        self.assertNotEqual(prim1, prim3)

        self.assertEqual(prim1.fill_space, "no")

        # prims have to be in technolgy in order to generate the rules
        class MyTech(_tch.Technology):
            @property
            def name(self):
                return "MyTech"
            @property
            def grid(self):
                return 0.005
            @property
            def substrate_type(self) -> str:
                return "p"

            def _init(self):
                self._primitives += (nimpl, pimpl, well, oxide, active, prim1, m1)
        mytech = MyTech()

        rules = tuple(prim1._generate_rules(tech=mytech))
        self.assertIn(prim1.mask, rules)

        # cast_params
        # different variations for code coverage
        prim1.cast_params({
            "bottom_implant": nimpl,
            "bottom_well": well,
        })
        prim2.cast_params({})
        prim3.cast_params({})
        with self.assertRaises(ValueError):
            # Wrong bottom
            prim3.cast_params({"bottom": m2})
        with self.assertRaises(ValueError):
            # bottom_implant not provided
            prim1.cast_params({})
        with self.assertRaises(ValueError):
            prim1.cast_params({"bottom_implant": nimpl2})
        with self.assertRaises(ValueError):
            # wrong bottom_well
            prim1.cast_params({
                "bottom_implant": nimpl,
                "bottom_well": well2,
            })
        with self.assertRaises(ValueError):
            # wrong bottom_well
            prim1.cast_params({
                "bottom_implant": nimpl,
                "bottom_well": well2,
            })
        with self.assertRaises(ValueError):
            # Misssing bottom_well when allow_in_substrate == False
            prim3.cast_params({
                "bottom": active2,
                "bottom_implant": nimpl,
            })
        with self.assertRaises(TypeError):
            # bottom_implant for bottom that is not WaferWire
            prim3.cast_params({
                "bottom_implant": nimpl,
            })
        with self.assertRaises(TypeError):
            # bottom_implant for bottom that is not WaferWire
            prim3.cast_params({
                "bottom_implant_enclosure": _prp.Enclosure(0.12),
            })
        with self.assertRaises(TypeError):
            # bottom_well for bottom that is not WaferWire
            prim3.cast_params({
                "bottom_well": well,
            })
        with self.assertRaises(TypeError):
            # bottom_well_enclosure for bottom that is not WaferWire
            prim3.cast_params({
                "bottom_well_enclosure": _prp.Enclosure(0.12),
            })
        with self.assertRaises(ValueError):
            # Wrong top
            prim2.cast_params({"top": m3})
        with self.assertRaises(ValueError):
            prim2.cast_params({"top": m3})

        # in_()
        with self.assertRaises(ValueError):
            prim1.in_(nimpl)
        self.assertEqual(
            prim1.in_(active),
            _prm._ViaIntersect(via=prim1, prim=active),
        )
        self.assertEqual(
            prim1.in_(active.in_(nimpl)),
            _prm._ViaIntersect(via=prim1, prim=active.in_(nimpl)),
        )

    def test_padopening(self):
        m1 = _prm.MetalWire(name="metal1", min_width=1.0, min_space=1.0)
        m2 = _prm.MetalWire(name="metal2", min_width=1.0, min_space=1.0)
        m3 = _prm.TopMetalWire(name="metal3", min_width=1.0, min_space=1.0)

        with self.assertRaises(TypeError):
            # Missing arguments
            _prm.PadOpening(name="error")
        with self.assertRaises(TypeError):
            # TopMetalWire as bottom
            _prm.PadOpening(
                name="error", min_width=1.0, min_space=1.0,
                bottom=m3, min_bottom_enclosure=_prp.Enclosure(0.2)
            )

        prim1 = _prm.PadOpening(
            name="prim1", min_width=1.0, min_space=1.0,
            bottom=m1, min_bottom_enclosure=_prp.Enclosure(0.2)
        )
        prim1bis = _prm.PadOpening(
            name="prim1", min_width=1.0, min_space=1.0,
            bottom=m1, min_bottom_enclosure=_prp.Enclosure(0.2)
        )
        prim2 = _prm.PadOpening(
            name="prim2", min_width=0.2, min_space=0.5,
            bottom=m2, min_bottom_enclosure=_prp.Enclosure(0.2)
        )

        self.assertEqual(prim1, prim1bis)
        self.assertNotEqual(prim1, prim2)

        self.assertEqual(prim1.fill_space, "no")

        rules = tuple(prim1._generate_rules(tech=dummy_tech))
        self.assertIn(prim1.mask, rules)

        # designmasks
        self.assertEqual(set(prim1.designmasks), {prim1.mask, m1.mask})

    def test_resistor(self):
        well = _prm.Well(name="well", min_width=1.0, min_space=1.0, type_="p")
        nimpl = _prm.Implant(name="nimplant", min_width=0.5, min_space=0.5, type_="n")
        nimpl2 = _prm.Implant(name="nimplant2", min_width=0.5, min_space=0.5, type_="n")
        pimpl = _prm.Implant(name="pimplant", min_width=0.5, min_space=0.5, type_="p")
        active = _prm.WaferWire(
            name="aa", min_width=1.0, min_space=1.0,
            allow_in_substrate=True,
            implant=(nimpl, pimpl), min_implant_enclosure=_prp.Enclosure(0.05),
            implant_abut="all", allow_contactless_implant=False,
            well=well, min_well_enclosure=_prp.Enclosure(0.1),
            min_substrate_enclosure=_prp.Enclosure(0.15),
            allow_well_crossing=False,
        )
        actres = _prm.Marker(name="actres")
        poly = _prm.GateWire(name="poly", min_width=1.0, min_space=1.0)
        polyres = _prm.Marker(name="polyres")
        m1 = _prm.MetalWire(name="metal1", min_width=1.0, min_space=1.0)
        m1res = _prm.Marker(name="m1res")
        via = _prm.Via(
            name="via", width=0.8, min_space=0.8,
            bottom=poly, min_bottom_enclosure=_prp.Enclosure(0.2),
            top=m1, min_top_enclosure=_prp.Enclosure(0.2),
        )

        with self.assertRaises(TypeError):
            # grid not allowed
            _prm.Resistor(
                name="error", grid=0.1,
                wire=poly, contact=None, indicator=polyres, min_indicator_extension=0.5,
                sheetres=10.0,
            )
        with self.assertRaises(ValueError):
            # min_width too small
            _prm.Resistor(
                name="error", min_width=0.5,
                wire=poly, contact=None, indicator=polyres, min_indicator_extension=0.5,
                sheetres=10.0,
            )
        with self.assertRaises(ValueError):
            # min_space too small
            _prm.Resistor(
                name="error", min_space=0.5,
                wire=poly, contact=None, indicator=polyres, min_indicator_extension=0.5,
                sheetres=10.0,
            )
        with self.assertRaises(TypeError):
            # well not allowed as implant
            _prm.Resistor(
                name="error",
                wire=active, contact=None, indicator=actres, min_indicator_extension=0.5,
                implant=well, sheetres=10.0,
            )
        with self.assertRaises(ValueError):
            # wrong implant
            _prm.Resistor(
                name="error",
                wire=active, contact=None, indicator=actres, min_indicator_extension=0.5,
                implant=nimpl2, sheetres=10.0,
            )
        with self.assertRaises(ValueError):
            # implant for wire that is not WaferWire or GateWire
            _prm.Resistor(
                name="error",
                wire=m1, contact=None, indicator=m1res, min_indicator_extension=0.5,
                implant=nimpl, sheetres=10.0,
            )
        with self.assertRaises(TypeError):
            # min_implant_enclosure without implant
            prim1 = _prm.Resistor(
                name="error", min_width=1.2,
                wire=poly, contact=None, indicator=polyres, min_indicator_extension=0.5,
                min_implant_enclosure=_prp.Enclosure(0.2),
                sheetres=10.0,
            )
        with self.assertRaises(ValueError):
            # wire not in via bottom or top
            _prm.Resistor(
                name="error", min_width=1.2,
                wire=active, contact=via, min_contact_space=0.1,
                indicator=polyres, min_indicator_extension=0.5,
                implant=nimpl, sheetres=10.0,
            )
        with self.assertRaises(TypeError):
            # min_contact_space without contact
            _prm.Resistor(
                name="error", min_width=1.2,
                wire=poly, contact=None, indicator=polyres, min_indicator_extension=0.5,
                min_contact_space=0.1,
                sheetres=10.0,
            )
        with self.assertRaises(TypeError):
            # min_contact_space missing with given contact
            _prm.Resistor(
                name="error", min_width=1.2,
                wire=poly, contact=via,
                indicator=polyres, min_indicator_extension=0.5,
                implant=nimpl, sheetres=10.0,
            )
        with self.assertRaises(TypeError):
            # No sheetres or model given
            _prm.Resistor(
                name="error", min_width=1.2,
                wire=poly, contact=via, min_contact_space=0.1,
                indicator=polyres, min_indicator_extension=0.5,
                implant=nimpl,
            )
        with self.assertRaises(ValueError):
            # wrong keys for subckt_params
            _prm.Resistor(
                name="error", min_width=1.0, min_space=1.5,
                wire=m1, contact=None, indicator=m1res, min_indicator_extension=0.5,
                model="prim2res", subckt_params={"error": "error"},
            )
        with self.assertRaises(TypeError):
            # subckt_params specified without model given
            _prm.Resistor(
                name="error", min_width=1.2,
                wire=poly, contact=via, min_contact_space=0.1,
                indicator=polyres, min_indicator_extension=0.5,
                implant=nimpl, sheetres=10.0, subckt_params={"width": "w", "height": "l"},
            )
        with self.assertRaises(ValueError):
            # Wrong type for sheetres
            _prm.Resistor(
                name="error", min_width=1.2,
                wire=poly, contact=via, min_contact_space=0.1,
                indicator=polyres, min_indicator_extension=0.5,
                implant=nimpl, sheetres="error",
            )

        prim1 = _prm.Resistor(
            name="prim1", min_width=1.2,
            wire=poly, contact=via, min_contact_space=0.1,
            indicator=polyres, min_indicator_extension=0.5,
            implant=nimpl, sheetres=10.0,
        )
        prim1bis = _prm.Resistor(
            name="prim1",
            wire=poly, contact=via, min_contact_space=0.1,
            indicator=polyres, min_indicator_extension=0.5,
            implant=nimpl, sheetres=10.0,
        )
        prim2 = _prm.Resistor(
            name="prim2", min_width=1.0, min_space=1.5, min_area=3.0,
            wire=m1, contact=None, indicator=m1res, min_indicator_extension=0.5,
            model="prim2res",
        )

        self.assertEqual(prim1, prim1bis)
        self.assertNotEqual(prim1, prim2)

        rules = tuple(prim1._generate_rules(tech=dummy_tech))
        self.assertIn(prim1.mask, rules)
        rules = tuple(prim2._generate_rules(tech=dummy_tech))
        self.assertIn(prim2.mask, rules)

        # Test technology with only one mask to remove for conn_mask
        # of _Conductor
        m1 = _prm.TopMetalWire(name="m1", min_width=1.0, min_space=1.0)
        via = _prm.Via(
            name="via", width=0.8, min_space=0.8,
            bottom=(active, poly), min_bottom_enclosure=_prp.Enclosure(0.4),
            top=m1, min_top_enclosure=_prp.Enclosure(0.4),
        )
        class MyTech(_tch.Technology):
            @property
            def name(self):
                return "MyTech"
            @property
            def grid(self):
                return 0.005
            @property
            def substrate_type(self) -> str:
                return "p"

            def _init(self):
                self._primitives += (
                    well, nimpl, pimpl, active,
                    poly, polyres, prim1,
                    via, m1,
                )
        MyTech()

    def test_mimcapacitor(self): # Also include MIMTop
        m1 = _prm.MetalWire(name="metal1", min_width=1.0, min_space=1.0)
        m2 = _prm.MetalWire(name="metal2", min_width=1.0, min_space=1.0)
        m3 = _prm.MetalWire(name="metal3", min_width=1.0, min_space=1.0)
        mimtop = _prm.MIMTop(name="mimtop", min_width=1.0, min_space=1.0)
        mimtop2 = _prm.MIMTop(name="mimtop2", min_width=1.0, min_space=1.0)
        via = _prm.Via(
            name="via", width=0.8, min_space=0.8,
            bottom=(m1, mimtop), min_bottom_enclosure=_prp.Enclosure(0.2),
            top=m2, min_top_enclosure=_prp.Enclosure(0.2),
        )
        via2 = _prm.Via(
            name="via2", width=0.8, min_space=0.8,
            bottom=(m1, mimtop), min_bottom_enclosure=_prp.Enclosure(0.2),
            top=m3, min_top_enclosure=_prp.Enclosure(0.2),
        )
        with self.assertRaises(ValueError):
            # bottom not in via.bottom
            _prm.MIMCapacitor(
                name="error",
                bottom=m3, top=mimtop, via=via,
                min_bottom_top_enclosure=_prp.Enclosure(0.2),
                min_bottomvia_top_space=0.1,
                min_top_via_enclosure=_prp.Enclosure(0.1),
                min_bottom_space=None, min_top2bottom_space=None,
                model="error",
            )
        with self.assertRaises(ValueError):
            # top not in via.bottom
            _prm.MIMCapacitor(
                name="error",
                bottom=m1, top=mimtop2, via=via,
                min_bottom_top_enclosure=_prp.Enclosure(0.2),
                min_bottomvia_top_space=0.1,
                min_top_via_enclosure=_prp.Enclosure(0.1),
                min_bottom_space=None, min_top2bottom_space=None,
                model="error",
            )
        with self.assertRaises(ValueError):
            # min_width too small
            _prm.MIMCapacitor(
                name="error", min_width=0.5,
                bottom=m1, top=mimtop, via=via,
                min_bottom_top_enclosure=_prp.Enclosure(0.2),
                min_bottomvia_top_space=0.1,
                min_top_via_enclosure=_prp.Enclosure(0.1),
                min_bottom_space=None, min_top2bottom_space=None,
                model="error",
            )
        with self.assertRaises(ValueError):
            # min_space too small
            _prm.MIMCapacitor(
                name="error", min_space=0.5,
                bottom=m1, top=mimtop, via=via,
                min_bottom_top_enclosure=_prp.Enclosure(0.2),
                min_bottomvia_top_space=0.1,
                min_top_via_enclosure=_prp.Enclosure(0.1),
                min_bottom_space=None, min_top2bottom_space=None,
                model="error",
            )
        with self.assertRaises(ValueError):
            # wrong keys for subckt_params
            _prm.MIMCapacitor(
                name="error",
                bottom=m1, top=mimtop, via=via,
                min_bottom_top_enclosure=_prp.Enclosure(0.2),
                min_bottomvia_top_space=0.1,
                min_top_via_enclosure=_prp.Enclosure(0.1),
                min_bottom_space=None, min_top2bottom_space=None,
                model="error", subckt_params={"error": "error"},
            )

        prim1 = _prm.MIMCapacitor(
            name="prim1",
            bottom=m1, top=mimtop, via=via,
            min_bottom_top_enclosure=_prp.Enclosure(0.2),
            min_bottomvia_top_space=0.1,
            min_top_via_enclosure=_prp.Enclosure(0.1),
            min_bottom_space=None, min_top2bottom_space=None,
            model="prim1",
        )
        prim1bis = _prm.MIMCapacitor(
            name="prim1",
            bottom=m1, top=mimtop, via=via,
            min_bottom_top_enclosure=_prp.Enclosure(0.2),
            min_bottomvia_top_space=0.1,
            min_top_via_enclosure=_prp.Enclosure(0.1),
            min_bottom_space=None, min_top2bottom_space=None,
            model="prim1",
        )
        prim2 = _prm.MIMCapacitor(
            name="prim2",
            bottom=m1, top=mimtop, via=via2,
            min_bottom_top_enclosure=_prp.Enclosure(0.2),
            min_bottomvia_top_space=0.1,
            min_top_via_enclosure=_prp.Enclosure(0.1),
            min_bottom_space=None, min_top2bottom_space=None,
            model="prim2",
        )

        self.assertEqual(prim1, prim1bis)
        self.assertNotEqual(prim1, prim2)

        rules = tuple(mimtop._generate_rules(tech=dummy_tech))
        self.assertIn(mimtop.mask, rules)
        rules = tuple(prim1._generate_rules(tech=dummy_tech))
        self.assertIn(prim1.mask, rules)
        rules = tuple(prim2._generate_rules(tech=dummy_tech))
        self.assertIn(prim2.mask, rules)

    def test_diode(self):
        nwell = _prm.Well(name="nwell", min_width=1.0, min_space=1.0, type_="n")
        pwell = _prm.Well(name="pwell", min_width=1.0, min_space=1.0, type_="p")
        nimpl = _prm.Implant(name="nimplant", min_width=0.5, min_space=0.5, type_="n")
        nimpl2 = _prm.Implant(name="nimplant2", min_width=0.5, min_space=0.5, type_="n")
        pimpl = _prm.Implant(name="pimplant", min_width=0.5, min_space=0.5, type_="p")
        active = _prm.WaferWire(
            name="aa", min_width=1.0, min_space=1.0,
            allow_in_substrate=True,
            implant=(nimpl, pimpl), min_implant_enclosure=_prp.Enclosure(0.05),
            implant_abut="all", allow_contactless_implant=False,
            well=pwell, min_well_enclosure=_prp.Enclosure(0.1),
            min_substrate_enclosure=_prp.Enclosure(0.15),
            allow_well_crossing=False,
        )
        active2 = _prm.WaferWire(
            name="aa2", min_width=1.0, min_space=1.0,
            allow_in_substrate=False,
            implant=(nimpl, pimpl), min_implant_enclosure=_prp.Enclosure(0.05),
            implant_abut="all", allow_contactless_implant=False,
            well=(nwell, pwell), min_well_enclosure=_prp.Enclosure(0.1),
            allow_well_crossing=False,
        )
        actdiode = _prm.Marker(name="aadiode")
        mask = _msk.DesignMask(name="mask", fill_space="yes")

        with self.assertRaises(TypeError):
            # grid parameter given
            _prm.Diode(
                name="error", wire=active, grid=0.01,
                indicator=actdiode, min_indicator_enclosure=_prp.Enclosure(0.05),
                implant=pimpl,
            )
        with self.assertRaises(ValueError):
            # min_width too small
            _prm.Diode(
                name="error", wire=active, min_width=0.5,
                indicator=actdiode, min_indicator_enclosure=_prp.Enclosure(0.05),
                implant=pimpl,
            )
        with self.assertRaises(ValueError):
            # min_space too small
            _prm.Diode(
                name="error", wire=active, min_space=0.5,
                indicator=actdiode, min_indicator_enclosure=_prp.Enclosure(0.05),
                implant=pimpl,
            )
        with self.assertRaises(TypeError):
            # implant is a well
            _prm.Diode(
                name="error", wire=active,
                indicator=actdiode, min_indicator_enclosure=_prp.Enclosure(0.05),
                implant=pwell,
            )
        with self.assertRaises(ValueError):
            # wrong implant
            _prm.Diode(
                name="error", wire=active,
                indicator=actdiode, min_indicator_enclosure=_prp.Enclosure(0.05),
                implant=nimpl2,
            )
        with self.assertRaises(TypeError):
            # mask parameter given
            _prm.Diode(
                name="error", mask=mask, wire=active,
                indicator=actdiode, min_indicator_enclosure=_prp.Enclosure(0.05),
                implant=pimpl,
            )
        with self.assertRaises(TypeError):
            # well nbt provided for WaferWire with allow_in_substrate == False
            _prm.Diode(
                name="error", wire=active2,
                indicator=actdiode, min_indicator_enclosure=_prp.Enclosure(0.05),
                implant=nimpl,
            )
        with self.assertRaises(TypeError):
            # min_well_enclsoure without well
            _prm.Diode(
                name="error", wire=active,
                indicator=actdiode, min_indicator_enclosure=_prp.Enclosure(0.05),
                implant=pimpl, min_well_enclosure=_prp.Enclosure(0.2),
            )
        with self.assertRaises(ValueError):
            # well not valid for wire
            _prm.Diode(
                name="error", wire=active,
                indicator=actdiode, min_indicator_enclosure=_prp.Enclosure(0.05),
                implant=pimpl, well=nwell,
            )
        with self.assertRaises(ValueError):
            # well type euqal to implant type
            _prm.Diode(
                name="error", wire=active2,
                indicator=actdiode, min_indicator_enclosure=_prp.Enclosure(0.05),
                implant=pimpl, well=pwell,
            )

        prim1 = _prm.Diode(
            name="prim1", wire=active, min_width=1.2, min_space=1.2,
            indicator=actdiode, min_indicator_enclosure=_prp.Enclosure(0.05),
            implant=pimpl,
        )
        prim1bis = _prm.Diode(
            name="prim1", wire=active, min_width=1.2, min_space=1.2,
            indicator=actdiode, min_indicator_enclosure=_prp.Enclosure(0.05),
            implant=pimpl,
        )
        prim2 = _prm.Diode(
            name="prim2", wire=active2,
            indicator=actdiode, min_indicator_enclosure=_prp.Enclosure(0.05),
            implant=nimpl, well=pwell,
        )

        self.assertEqual(prim1, prim1bis)
        self.assertNotEqual(prim1, prim2)

        rules = tuple(prim1._generate_rules(tech=dummy_tech))
        self.assertIn(prim1.mask, rules)
        rules = tuple(prim2._generate_rules(tech=dummy_tech))
        self.assertIn(prim2.mask, rules)

    def test_mosfet(self): # also test MOSFETGate
        well = _prm.Well(name="well", min_width=1.0, min_space=1.0, type_="p")
        well2 = _prm.Well(name="well2", min_width=1.0, min_space=1.0, type_="n")
        nimpl = _prm.Implant(name="nimplant", min_width=1.0, min_space=1.0, type_="n")
        nimpl2 = _prm.Implant(name="nimplant2", min_width=1.0, min_space=1.0, type_="n")
        pimpl = _prm.Implant(name="pimplant", min_width=1.0, min_space=1.0, type_="p")
        adjust = _prm.Implant(name="nimplant", min_width=1.0, min_space=1.0, type_="adjust")
        oxide = _prm.Insulator(name="oxide", min_width=1.0, min_space=1.0, fill_space="yes")
        oxide2 = _prm.Insulator(name="oxide2", min_width=1.0, min_space=1.0, fill_space="no")
        active = _prm.WaferWire(
            name="aa", min_width=1.0, min_space=1.0,
            allow_in_substrate=True,
            implant=(nimpl, pimpl, adjust), min_implant_enclosure=_prp.Enclosure(0.05),
            implant_abut="all", allow_contactless_implant=False,
            well=well, min_well_enclosure=_prp.Enclosure(0.1),
            min_substrate_enclosure=_prp.Enclosure(0.15),
            allow_well_crossing=False,
            oxide=oxide,
        )
        active2 = _prm.WaferWire(
            name="aa2", min_width=1.0, min_space=1.0,
            allow_in_substrate=False,
            implant=(nimpl, pimpl, adjust), min_implant_enclosure=_prp.Enclosure(0.05),
            implant_abut="all", allow_contactless_implant=False,
            well=(well, well2), min_well_enclosure=_prp.Enclosure(0.1),
            allow_well_crossing=False,
            oxide=oxide,
        )
        poly = _prm.GateWire(name="poly", min_width=1.0, min_space=1.0)
        m1 = _prm.MetalWire(name="metal1", min_width=1.0, min_space=1.0)
        ch = _prm.Via(
            name="ch", width=0.8, min_space=0.8,
            bottom=(active, poly), min_bottom_enclosure=_prp.Enclosure(0.2),
            top=m1, min_top_enclosure=_prp.Enclosure(0.2),
        )
        hv = _prm.Marker(name="hv")

        # MOSFETGate
        with self.assertRaises(ValueError):
            # wrong oxide for active
            _prm.MOSFETGate(
                name="error", active=active, poly=poly,
                min_sd_width=0.15, min_polyactive_extension=0.2,
                oxide=oxide2,
            )
        with self.assertRaises(TypeError):
            # min_gateoxide_enclosure without oxide
            _prm.MOSFETGate(
                name="error", active=active, poly=poly,
                min_sd_width=0.15, min_polyactive_extension=0.2,
                min_gateoxide_enclosure=_prp.Enclosure(0.2),
            )
        with self.assertRaises(TypeError):
            # min_gateinside_enclosure without oxide
            _prm.MOSFETGate(
                name="error", active=active, poly=poly,
                min_sd_width=0.15, min_polyactive_extension=0.2,
                min_gateinside_enclosure=_prp.Enclosure(0.2),
            )
        with self.assertRaises(TypeError):
            # min_contactgate_space without contact
            _prm.MOSFETGate(
                name="error", active=active, poly=poly,
                min_sd_width=0.15, min_polyactive_extension=0.2,
                min_contactgate_space=0.15,
            )
        with self.assertRaises(TypeError):
            # contact with min_contactgate_space
            _prm.MOSFETGate(
                name="error", active=active, poly=poly, min_gate_space=1.5,
                min_sd_width=0.15, min_polyactive_extension=0.2,
                contact=ch,
            )

        gate1 = _prm.MOSFETGate(
            name="gate1", active=active, poly=poly, min_gate_space=1.5,
            min_sd_width=0.15, min_polyactive_extension=0.2,
            contact=ch, min_contactgate_space=0.1,
        )
        gate2 = _prm.MOSFETGate(
            active=active, poly=poly, oxide=oxide, min_w=1.5,
            inside=hv, min_gateinside_enclosure=_prp.Enclosure(0.2),
        )
        gate3 = _prm.MOSFETGate(
            active=active2, poly=poly, oxide=oxide, min_w=1.5,
            inside=hv, min_gateinside_enclosure=_prp.Enclosure(0.2),
        )

        self.assertNotEqual(gate1, gate2)
        self.assertNotEqual(gate1, gate3)

        self.assertAlmostEqual(gate1.min_contactgate_space, 0.1, places=6)
        self.assertAlmostEqual(gate2.computed.min_l, 1.0, places=6)

        # MOSFET
        with self.assertRaises(ValueError):
            # both n and p type implants
            _prm.MOSFET(
                name="error", gate=gate1, min_l=1.5, min_w=1.5,
                implant=(nimpl, pimpl), min_gateimplant_enclosure=_prp.Enclosure(0.2),
                min_contactgate_space=0.15, well=well,
            )
        with self.assertRaises(ValueError):
            # only adjust implant
            _prm.MOSFET(
                name="error", gate=gate1, min_l=1.5, min_w=1.5,
                implant=adjust, min_gateimplant_enclosure=_prp.Enclosure(0.2),
                min_contactgate_space=0.15, well=well,
            )
        with self.assertRaises(ValueError):
            # invalid implant for gate.active
            _prm.MOSFET(
                name="error", gate=gate1, min_l=1.5, min_w=1.5,
                implant=nimpl2, min_gateimplant_enclosure=_prp.Enclosure(0.2),
                min_contactgate_space=0.15, well=well,
            )
        with self.assertRaises(ValueError):
            # no well when gate.active.allow_in_substrate is None
            _prm.MOSFET(
                name="error", gate=gate3, min_l=1.5, min_w=1.5,
                implant=nimpl, min_gateimplant_enclosure=_prp.Enclosure(0.2),
                min_contactgate_space=0.15,
            )
        with self.assertRaises(ValueError):
            # invalid well for gate.active
            _prm.MOSFET(
                name="error", gate=gate1, min_l=1.5, min_w=1.5,
                implant=pimpl, min_gateimplant_enclosure=_prp.Enclosure(0.2),
                min_contactgate_space=0.15, well=well2,
            )
        with self.assertRaises(ValueError):
            _prm.MOSFET(
                name="error", gate=gate1, min_l=1.5, min_w=1.5,
                implant=pimpl, min_gateimplant_enclosure=_prp.Enclosure(0.2),
                min_contactgate_space=0.15, well=well,
            )
        with self.assertRaises(ValueError):
            # too low min_l,
            _prm.MOSFET(
                name="error", gate=gate1, min_l=0.5,
                implant=nimpl, min_gateimplant_enclosure=_prp.Enclosure(0.2),
            )
        with self.assertRaises(ValueError):
            # too low min_w,
            _prm.MOSFET(
                name="error", gate=gate1, min_w=0.5,
                implant=nimpl, min_gateimplant_enclosure=_prp.Enclosure(0.2),
            )
        with self.assertRaises(ValueError):
            # no min_sd_width
            _prm.MOSFET(
                name="error", gate=gate2, min_gate_space=1.5,
                implant=nimpl, min_gateimplant_enclosure=_prp.Enclosure(0.2),
                min_polyactive_extension=0.2,
            )
        with self.assertRaises(ValueError):
            # no min_polyactive_extension
            _prm.MOSFET(
                name="error", gate=gate2, min_gate_space=1.5,
                implant=nimpl, min_gateimplant_enclosure=_prp.Enclosure(0.2),
                min_sd_width=0.15,
            )
        with self.assertRaises(ValueError):
            # min_contactgate_space without contact
            _prm.MOSFET(
                name="error", gate=gate2, min_gate_space=1.5,
                implant=nimpl, min_gateimplant_enclosure=_prp.Enclosure(0.2),
                min_sd_width=0.15, min_polyactive_extension=0.2,
                min_contactgate_space=0.1,
            )
        with self.assertRaises(ValueError):
            # contact without min_contactgate_space
            _prm.MOSFET(
                name="error", gate=gate2, min_gate_space=1.5,
                implant=nimpl, min_gateimplant_enclosure=_prp.Enclosure(0.2),
                min_sd_width=0.15, min_polyactive_extension=0.2,
                contact=ch,
            )

        prim1 = _prm.MOSFET(
            name="prim1", gate=gate1, min_l=1.5, min_w=1.5,
            implant=nimpl, min_gateimplant_enclosure=_prp.Enclosure(0.2),
        )
        prim1bis = _prm.MOSFET(
            name="prim1", gate=gate1, min_l=1.5, min_w=1.5,
            implant=nimpl, min_gateimplant_enclosure=_prp.Enclosure(0.2),
        )
        prim2 = _prm.MOSFET(
            name="prim2", gate=gate2, min_gate_space=1.5,
            implant=nimpl, min_gateimplant_enclosure=_prp.Enclosure(0.2),
            min_sd_width=0.15, min_polyactive_extension=0.2,
            contact=ch, min_contactgate_space=0.1,
        )
        prim3 = _prm.MOSFET(
            name="prim3", gate=gate1, min_l=1.5, min_w=1.5,
            implant=nimpl, min_gateimplant_enclosure=_prp.Enclosure(0.2),
            min_contactgate_space=0.15, well=well,
        )

        self.assertEqual(prim1, prim1bis)
        self.assertNotEqual(prim1, prim2)
        self.assertNotEqual(prim1, prim3)

        self.assertEqual(
            prim1.gate_prim,
            _prm._Intersect(prims=(prim1.gate, *prim1.implant)),
        )
        self.assertEqual(
            prim3.gate_prim,
            _prm._Intersect(prims=(prim3.gate, *prim1.implant, prim3.well)),
        )

        self.assertAlmostEqual(prim1.computed.min_l, 1.5, places=6)
        self.assertAlmostEqual(prim1.computed.min_sd_width, 0.15, places=6)
        self.assertAlmostEqual(prim1.computed.min_contactgate_space, 0.1, places=6)
        self.assertAlmostEqual(prim3.computed.min_contactgate_space, 0.15, places=6)
        self.assertEqual(prim1.computed.contact, ch)
        self.assertAlmostEqual(prim2.computed.min_l, 1.0, places=6)
        self.assertAlmostEqual(prim2.computed.min_sd_width, 0.15, places=6)

        # Use primitives from dummy_tech for generate_rules testing
        # This is to be sure proper connectivity is there
        dummy_prims = dummy_tech.primitives
        dummy_mosgate = dummy_prims.mosgate
        dummy_nmos = dummy_prims.nmos
        dummy_pmos = dummy_prims.pmos
        self.assertIn(dummy_mosgate.mask, dummy_mosgate.rules)
        self.assertNotIn(dummy_mosgate.mask, dummy_nmos.rules)
        self.assertNotIn(dummy_mosgate.mask, dummy_pmos.rules)

        # cast_params
        params = prim1.cast_params({"gateimplant_enclosures": None})
        self.assertEqual(
            params["gateimplant_enclosures"],
            (_prp.Enclosure(0.2),),
        )
        with self.assertRaises(TypeError):
            class C:
                pass
            prim1.cast_params({
                "gateimplant_enclosures": C(),
            })
        with self.assertRaises(TypeError):
            prim1.cast_params({
                "gateimplant_enclosures": ("error", "error2"),
            })

    def test_bipolar(self):
        npn = _prm.Marker(name="npn")
        pnp = _prm.Marker(name="pnp")

        with self.assertRaises(ValueError):
            # Wrong type
            _prm.Bipolar(name="error", type_="error", indicator=npn)

        prim1 = _prm.Bipolar(name="prim1", type_="npn", indicator=npn)
        prim1bis = _prm.Bipolar(name="prim1", type_="npn", indicator=npn)
        prim2 = _prm.Bipolar(name="prim2", type_="pnp", indicator=pnp)

        self.assertEqual(prim1, prim1bis)
        self.assertNotEqual(prim1, prim2)

        tuple(prim1._generate_rules(tech=dummy_tech))
        tuple(prim2._generate_rules(tech=dummy_tech))

        self.assertIn(npn.mask, prim1.designmasks)
        self.assertIn(pnp.mask, prim2.designmasks)

    def test_ruleprimitive(self):
        with self.assertRaises(TypeError):
            # abstract methods
            _prm._RulePrimitive(name="error")

    def test_spacing(self):
        # Use Spacing added to dummy_tech to test Spacing.
        dummy_prims = dummy_tech.primitives
        nplus = dummy_prims.nplus
        pplus = dummy_prims.nplus
        poly = dummy_prims.poly
        mosgate = dummy_prims.mosgate

        prim1 = _prm.Spacing(primitives1=(nplus, pplus), min_space=0.2)
        prim1bis = _prm.Spacing(primitives1=(nplus, pplus), min_space=0.2)
        prim2 = _prm.Spacing(primitives1=(nplus, pplus, poly), min_space=0.2)
        prim3 = _prm.Spacing(
            primitives1=(nplus, pplus), primitives2=mosgate, min_space=0.25,
        )

        rules = tuple(prim1._generate_rules(tech=dummy_tech))
        self.assertIn(
            _msk.Join(prim.mask for prim in (nplus, pplus)).space >= prim1.min_space,
            rules,
        )

        self.assertEqual(prim1, prim1bis)
        self.assertNotEqual(prim1, prim2)
        self.assertNotEqual(prim1, prim3)

        self.assertEqual(
            repr(prim1),
            "Spacing((nplus,nplus),None,0.2)",
        )
        self.assertIn(nplus.mask, prim1.designmasks)
        self.assertIn(nplus.mask, prim3.designmasks)
        self.assertIn(poly.mask, prim3.designmasks)

    def test_enclosure(self):
        # Use primitives from dummy_tech
        dummy_prims = dummy_tech.primitives
        nplus = dummy_prims.nplus
        pplus = dummy_prims.pplus
        poly = dummy_prims.poly

        prim1 = _prm.Enclosure(prim=poly, by=nplus, min_enclosure=_prp.Enclosure(0.2))
        prim1bis = _prm.Enclosure(prim=poly, by=nplus, min_enclosure=_prp.Enclosure(0.2))
        prim2 = _prm.Enclosure(prim=poly, by=pplus, min_enclosure=_prp.Enclosure(0.2))
        prim3 = _prm.Enclosure(prim=poly, by=nplus, min_enclosure=_prp.Enclosure(0.15))

        self.assertEqual(prim1, prim1bis)
        self.assertNotEqual(prim1, prim2)
        self.assertNotEqual(prim1, prim3)

        rules = tuple(prim1._generate_rules(tech=dummy_tech))
        self.assertIn(
            poly.mask.enclosed_by(nplus.mask) >= _prp.Enclosure(0.2),
            rules,
        )

        self.assertIn(poly.mask, prim1.designmasks)
        self.assertIn(nplus.mask, prim1.designmasks)

        self.assertEqual(
            repr(prim1),
            "Enclosure(prim=GateWire(name=poly),by=Implant(name=nplus),min_enclosure=Enclosure(0.2))",
        )

    def test_nooverlap(self):
        # Use primitives from dummy_tech
        dummy_prims = dummy_tech.primitives
        nplus = dummy_prims.nplus
        pplus = dummy_prims.pplus
        poly = dummy_prims.poly

        prim1 = _prm.NoOverlap(prim1=nplus, prim2=pplus)
        prim1bis = _prm.NoOverlap(prim1=nplus, prim2=pplus)
        prim2 = _prm.NoOverlap(prim1=nplus, prim2=poly)

        self.assertEqual(prim1, prim1bis)
        self.assertNotEqual(prim1, prim2)

        rules = tuple(prim1._generate_rules(tech=dummy_tech))
        self.assertIn(
            _prm._Intersect(prims=(nplus, pplus)).mask.area == 0.0,
            rules,
        )

        self.assertIn(nplus.mask, prim1.designmasks)
        self.assertIn(poly.mask, prim2.designmasks)

        self.assertEqual(
            repr(prim1),
            "NoOverlap(prim1=Implant(name=nplus),prim2=Implant(name=pplus))",
        )

    def test_primitives(self):
        # Use primitives from dummy_tech
        dummy_prims = dummy_tech.primitives
        nplus = dummy_prims.nplus
        active = dummy_prims.active

        with self.assertRaises(TypeError):
            # _DerivedPrimitive
            prims = _prm.Primitives()
            prims += active.in_(nplus)
        with self.assertRaises(ValueError):
            # Primitive added twice
            prims = _prm.Primitives(nplus)
            prims += nplus


    # The exceptions will be used and tested by the technology_ unit test
