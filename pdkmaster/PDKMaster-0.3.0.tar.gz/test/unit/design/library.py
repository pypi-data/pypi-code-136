# SPDX-License-Identifier: GPL-2.0-or-later OR AGPL-3.0-or-later OR CERN-OHL-S-2.0+
# type: ignore
import unittest

from pdkmaster.technology import geometry as _geo, primitive as _prm
from pdkmaster.design import circuit as _ckt, layout as _lay, library as _lbry

from ..dummy import dummy_tech, dummy_cktfab, dummy_layoutfab, dummy_lib

class CellTest(unittest.TestCase):
    def test_property(self):
        class MyOD(_lbry._OnDemandCell):
            def _create_circuit(self):
                return
            def _create_layout(self):
                return

        empty_cell = _lbry._Cell(lib=dummy_cktfab, name="empty")
        empty_odcell = MyOD(lib=dummy_cktfab, name="empty_od")

        cell1 = dummy_lib.cells.cell1

        self.assertEqual(cell1.tech, dummy_tech)
        self.assertEqual(cell1.cktfab, dummy_cktfab)
        self.assertEqual(cell1.layoutfab, dummy_layoutfab)

        with self.assertRaises(ValueError):
            empty_cell.circuit
        with self.assertRaises(ValueError):
            empty_cell.layout
        with self.assertRaises(ValueError):
            empty_cell.new_circuitlayouter()
        with self.assertRaises(ValueError):
            empty_cell.new_circuitlayouter(name="error")

        with self.assertRaises(NotImplementedError):
            empty_odcell.circuit
        with self.assertRaises(NotImplementedError):
            empty_odcell.layout
        with self.assertRaises(NotImplementedError):
            empty_odcell.new_circuitlayouter()
        with self.assertRaises(ValueError):
            empty_odcell.new_circuitlayouter(name="error")

    def test_instsublayout(self):
        cell = dummy_lib.new_cell(name="test")
        cell.new_circuit()
        bb = _geo.Rect(left=0.0, bottom=0.0, right=1.0, top=2.0)
        cell.new_layout(boundary=bb)

        rot = _geo.Rotation.R90
        inst = _ckt._CellInstance(name="inst", cell=cell)
        sublay = _lay._InstanceSubLayout(
            inst=inst, origin=_geo.origin, layoutname=None, rotation=rot,
        )
        self.assertEqual(sublay.boundary, rot*bb)

        cell2 = dummy_lib.new_cell(name="test2")
        ckt = cell2.new_circuit()
        inst = ckt.instantiate(cell, name="inst")
        layouter = cell2.new_circuitlayouter()

        instlay = layouter.inst_layout(inst=inst, rotation=rot)
        self.assertEqual(instlay.boundary, rot*bb)


class LibraryTest(unittest.TestCase):
    def test_property(self):
        self.assertEqual(dummy_lib.tech, dummy_tech)
        self.assertEqual(dummy_lib.cktfab, dummy_cktfab)
        self.assertEqual(dummy_lib.layoutfab, dummy_layoutfab)

    def test___init__(self):
        # code coverage
        tuple(dummy_lib.sorted_cells)

        lib = _lbry.Library(name="test", tech=dummy_tech, global_nets=("vdd", "vss"))
        cell = lib.new_cell(name="test")
        ckt = cell.new_circuit()

        cell2 = lib.new_cell(name="test2")
        ckt2 = cell2.new_circuit()

        # Instantiate in first created in order to try to trigger code
        # in sorted_cells.
        ckt.instantiate(cell2, name="cell2")

        tuple(lib.sorted_cells)


class StdCellLibraryTest(unittest.TestCase):
    def test_routinggauge(self):
        prims = dummy_tech.primitives

        mw = _prm.MetalWire(name="mw", min_width=1.0, min_space=1.0)

        with self.assertRaises(ValueError):
            # wrong bottom
            _lbry.RoutingGauge(
                tech=dummy_tech, bottom=mw, bottom_direction="horizontal",
                top=prims.metal2,
            )
        with self.assertRaises(ValueError):
            # wrong top
            _lbry.RoutingGauge(
                tech=dummy_tech, bottom=prims.metal, bottom_direction="horizontal",
                top=mw,
            )
        with self.assertRaises(ValueError):
            # top not above bottom
            _lbry.RoutingGauge(
                tech=dummy_tech, bottom=prims.metal2, bottom_direction="horizontal",
                top=prims.metal,
            )
        with self.assertRaises(ValueError):
            # wrong direction
            _lbry.RoutingGauge(
                tech=dummy_tech, bottom=prims.metal, bottom_direction="error",
                top=prims.metal2,
            )
        with self.assertRaises(ValueError):
            # wrong metalwire in pitches
            _lbry.RoutingGauge(
                tech=dummy_tech, bottom=prims.metal, bottom_direction="horizontal",
                top=prims.metal2,
                pitches={
                    mw: 2.0,
                    prims.metal2: 2.0,
                },
                offsets={
                    prims.metal: 0.0,
                    prims.metal2: 1.0,
                },
            )
        with self.assertRaises(ValueError):
            # wrong metalwire in offsets
            _lbry.RoutingGauge(
                tech=dummy_tech, bottom=prims.metal, bottom_direction="horizontal",
                top=prims.metal2,
                pitches={
                    prims.metal: 2.0,
                    prims.metal2: 2.0,
                },
                offsets={
                    prims.metal: 0.0,
                    mw: 1.0,
                },
            )

        # code coverage
        rg = _lbry.RoutingGauge(
            tech=dummy_tech, bottom=prims.metal, bottom_direction="horizontal",
            top=prims.metal2,
            pitches={
                prims.metal: 2.0,
                prims.metal2: 2.0,
            },
            offsets={
                prims.metal: 0.0,
                prims.metal2: 1.0,
            },
        )
        lib = _lbry.StdCellLibrary(
            name="test", tech=dummy_tech, global_nets=("vdd", "vss"),
            routinggauge=rg, pingrid_pitch=0.4, row_height=10.0,
        )
        tuple(lib.sorted_cells)
