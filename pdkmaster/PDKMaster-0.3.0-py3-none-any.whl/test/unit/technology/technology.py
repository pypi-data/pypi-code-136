# SPDX-License-Identifier: GPL-2.0-or-later OR AGPL-3.0-or-later OR CERN-OHL-S-2.0+
# type: ignore
import unittest

# Use mainly dummy_tech for checking and code coverage
from ..dummy import dummy_tech
dummy_prims = dummy_tech.primitives

from pdkmaster.technology import (
    property_ as _prp, geometry as _geo, primitive as _prm, technology_ as _tch,
)

class TechnologyTest(unittest.TestCase):
    def test_error(self):
        with self.assertRaises(ValueError):
            # wrong substrate type
            class ErrorTech1(_tch.Technology):
                def name(self):
                    return "error"
                def grid(self):
                    return 0.005
                def substrate_type(self):
                    return "error"

                def _init(self):
                    return
            ErrorTech1()

    def test_computed(self):
        active = dummy_prims.active
        poly = dummy_prims.poly
        contact = dummy_prims.contact
        metal = dummy_prims.metal
        via = dummy_prims.via

        # min_space
        self.assertAlmostEqual(
            dummy_tech.computed.min_space(primitive1=active),
            active.min_space,
            places=6,
        )
        with self.assertRaises(AttributeError):
            # No min_space between active and poly
            dummy_tech.computed.min_space(
                primitive1=active, primitive2=poly
            )

        # min_width
        self.assertAlmostEqual(
            dummy_tech.computed.min_width(primitive=active),
            active.min_width,
            places=6,
        )
        self.assertAlmostEqual(
            dummy_tech.computed.min_width(
                primitive=metal, up=True, down=True,
            ),
            max(
                metal.min_width,
                contact.width + 2*contact.min_top_enclosure[0].max(),
                via.width + 2*via.min_bottom_enclosure[0].max(),
            ),
            places=6,
        )

        # min_pitch
        self.assertAlmostEqual(
            dummy_tech.computed.min_pitch(primitive=active),
            active.min_width + active.min_space,
            places=6,
        )
        self.assertAlmostEqual(
            dummy_tech.computed.min_pitch(
                primitive=metal, up=True, down=True,
            ),
            max(
                metal.min_width,
                contact.width + 2*contact.min_top_enclosure[0].max(),
                via.width + 2*via.min_bottom_enclosure[0].max(),
            ) + metal.min_space,
            places=6,
        )

    def test_ongrid(self):
        grid = dummy_tech.grid

        # is_ongrid() method
        self.assertTrue(dummy_tech.is_ongrid(grid))
        self.assertFalse(dummy_tech.is_ongrid(grid/2))

        # on_grid() method
        with self.assertRaises(ValueError):
            # Wrong rounding specification
            dummy_tech.on_grid(1.1*grid, rounding="error")

        self.assertAlmostEqual(
            dummy_tech.on_grid(1.1*grid, rounding="nearest"),
            grid,
            places=6,
        )
        self.assertAlmostEqual(
            dummy_tech.on_grid(1.1*grid, rounding="floor"),
            grid,
            places=6,
        )
        self.assertAlmostEqual(
            dummy_tech.on_grid(1.1*grid, rounding="ceiling"),
            2*grid,
            places=6,
        )
        self.assertAlmostEqual(
            dummy_tech.on_grid(3.1*grid, mult=2, rounding="nearest"),
            4*grid,
            places=6,
        )

        self.assertEqual(
            dummy_tech.on_grid(_geo.Point(x=1.1*grid, y=1.1*grid)),
            _geo.Point(x=grid, y=grid),
        )

    def test_dbu1(self):
        self.assertAlmostEqual(dummy_tech.dbu, 1e-3, delta=_geo.epsilon)

        class MyTech(_tch.Technology):
            @property
            def name(self) -> str:
                return "MyTech"
            @property
            def grid(self) -> float:
                return 2.5e-3
            @property
            def substrate_type(self) -> str:
                return "p"

            def _init(self):
                return
        mytech = MyTech()
        self.assertAlmostEqual(mytech.dbu, 1e-4, delta=_geo.epsilon)

        class MyTech(_tch.Technology):
            @property
            def name(self) -> str:
                return "MyTech"
            @property
            def grid(self) -> float:
                return 1.25e-3
            @property
            def substrate_type(self) -> str:
                return "p"

            def _init(self):
                return super()._init()
        mytech = MyTech()
        self.assertAlmostEqual(mytech.dbu, 1e-5, delta=_geo.epsilon)

    def test_padopening(self):
        class MyTech(_tch.Technology):
            @property
            def name(self) -> str:
                return "MyTech"
            @property
            def grid(self) -> float:
                return 5e-3
            @property
            def substrate_type(self) -> str:
                return "p"

            def _init(self):
                prims = self.primitives

                metal1 = _prm.MetalWire(name="metal1", min_width=1.0, min_space=1.0)
                pad = _prm.PadOpening(
                    name="pad", min_width=20.0, min_space=3.0,
                    bottom=metal1, min_bottom_enclosure=2.0,
                )
                prims += (metal1, pad)
        # Code coverage only
        MyTech()

    def test_check(self):
        class MyTech(_tch.Technology):
            @property
            def name(self) -> str:
                return "MyTech"
            @property
            def grid(self) -> float:
                return 2.5e-3
            @property
            def substrate_type(self) -> str:
                return "p"

            def _init(self):
                prims = self.primitives

                prims += _prm.Well(
                    name="well", min_width=5.0, min_space=3.0, type_="n",
                )
        with self.assertRaises(_prm.UnconnectedPrimitiveError):
            MyTech()

        class MyTech(_tch.Technology):
            @property
            def name(self) -> str:
                return "MyTech"
            @property
            def grid(self) -> float:
                return 5e-3
            @property
            def substrate_type(self) -> str:
                return "p"

            def _init(self):
                prims = self.primitives

                metal1 = _prm.MetalWire(name="metal1", min_width=1.0, min_space=1.0)
                prims += metal1
        with self.assertRaises(_prm.UnusedPrimitiveError):
            MyTech()

        class MyTech(_tch.Technology):
            @property
            def name(self) -> str:
                return "MyTech"
            @property
            def grid(self) -> float:
                return 5e-3
            @property
            def substrate_type(self) -> str:
                return "p"

            def _init(self):
                prims = self.primitives

                nimpl = _prm.Implant(
                    name="nimplant", min_width=1.2, min_space=1.2, type_="n",
                )
                pimpl = _prm.Implant(
                    name="pimplant", min_width=1.2, min_space=1.2, type_="p",
                )
                nwell = _prm.Well(
                    name="nwell", min_width=5.0, min_space=3.0, type_="n",
                )
                prims += (nimpl, pimpl, nwell)

                active = _prm.WaferWire(
                    name="active", min_width=0.8, min_space=0.8,
                    implant=(nimpl, pimpl), min_implant_enclosure=_prp.Enclosure(0.2),
                    implant_abut="all", allow_contactless_implant=False,
                    allow_in_substrate=True,
                    well=nwell, min_well_enclosure=_prp.Enclosure(0.8),
                    allow_well_crossing=False,
                )
                poly = _prm.GateWire(name="poly", min_width=0.8, min_space=0.8)
                prims += (active, poly)

                gate = _prm.MOSFETGate(
                    active=active, poly=poly,
                )
                prims += gate
        with self.assertRaises(_prm.UnusedPrimitiveError):
            MyTech()

        class MyTech(_tch.Technology):
            @property
            def name(self) -> str:
                return "MyTech"
            @property
            def grid(self) -> float:
                return 5e-3
            @property
            def substrate_type(self) -> str:
                return "p"

            def _init(self):
                prims = self.primitives

                nimpl = _prm.Implant(
                    name="nimplant", min_width=1.2, min_space=1.2, type_="n",
                )
                pimpl = _prm.Implant(
                    name="pimplant", min_width=1.2, min_space=1.2, type_="p",
                )
                nwell = _prm.Well(
                    name="nwell", min_width=5.0, min_space=3.0, type_="n",
                )
                prims += (nimpl, pimpl, nwell)

                active = _prm.WaferWire(
                    name="active", min_width=0.8, min_space=0.8,
                    implant=(nimpl, pimpl), min_implant_enclosure=_prp.Enclosure(0.2),
                    implant_abut="all", allow_contactless_implant=False,
                    allow_in_substrate=True,
                    well=nwell, min_well_enclosure=_prp.Enclosure(0.8),
                    allow_well_crossing=False,
                )
                poly = _prm.GateWire(name="poly", min_width=0.8, min_space=0.8)
                metal1 = _prm.MetalWire(name="metal1", min_width=1.0, min_space=1.0)
                contact = _prm.Via(
                    name="contact", width=0.8, min_space=0.8,
                    bottom=poly, min_bottom_enclosure=_prp.Enclosure(0.0),
                    top=metal1, min_top_enclosure=_prp.Enclosure(0.2),
                )
                prims += (active, poly, contact, metal1)

                gate = _prm.MOSFETGate(
                    active=active, poly=poly,
                    min_sd_width=0.35, min_polyactive_extension=0.35,
                )
                nmos = _prm.MOSFET(
                    name="nmos", gate=gate, implant=nimpl,
                    min_gateimplant_enclosure=_prp.Enclosure(0.3),
                )
                prims += (gate, nmos)
        with self.assertRaises(_tch.Technology.ConnectionError):
            MyTech()

        class MyTech(_tch.Technology):
            @property
            def name(self) -> str:
                return "MyTech"
            @property
            def grid(self) -> float:
                return 5e-3
            @property
            def substrate_type(self) -> str:
                return "p"

            def _init(self):
                prims = self.primitives

                metal1 = _prm.MetalWire(name="metal1", min_width=1.0, min_space=1.0)
                metal2 = _prm.MetalWire(name="metal1", min_width=1.0, min_space=1.0)
                via = _prm.Via(
                    name="via", width=0.8, min_space=0.8,
                    bottom=metal1, min_bottom_enclosure=_prp.Enclosure(0.2),
                    top=metal2, min_top_enclosure=_prp.Enclosure(0.2),
                )
                prims += (metal1, via, metal2)
        with self.assertRaises(_tch.Technology.ConnectionError):
            MyTech()

        class MyTech(_tch.Technology):
            @property
            def name(self) -> str:
                return "MyTech"
            @property
            def grid(self) -> float:
                return 5e-3
            @property
            def substrate_type(self) -> str:
                return "p"

            def _init(self):
                prims = self.primitives

                prims += _prm.MIMTop(name="error", min_width=1.0, min_space=1.0)
        with self.assertRaises(_prm.UnusedMIMTop):
            MyTech()

        class MyTech(_tch.Technology):
            @property
            def name(self) -> str:
                return "MyTech"
            @property
            def grid(self) -> float:
                return 5e-3
            @property
            def substrate_type(self) -> str:
                return "p"

            def _init(self):
                self.substrate
        with self.assertRaises(AttributeError):
            MyTech()
