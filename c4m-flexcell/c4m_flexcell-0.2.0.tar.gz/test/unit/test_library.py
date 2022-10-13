# SPDX-License-Identifier: GPL-2.0-or-later OR AGPL-3.0-or-later OR CERN-OHL-S-2.0+
import unittest
from textwrap import dedent

from c4m.flexcell import Library

class CellTest(unittest.TestCase):
    def test_spice_netlist(self):
        lib = Library()
        cell = lib["inv_x1"]
        self.assertEqual(cell.spice_netlist(lambda_=0.175), dedent("""
            .subckt inv_x1 i nq vss vdd
            M1 vss i nq vss nmos l=0.35u w=1.75u
            M2 vdd i nq vdd pmos l=0.35u w=3.5u
            .ends inv_x1
            """
        )[1:])

    def test_python_code(self):
        lib = Library()
        cell = lib["inv_x1"]
        s1 = cell.python_code()
        s2 = dedent("""
            StdCell(
                name='inv_x1', width=60, height=200,
                nets={
                    'i': [
                        Via('POLY', 'METAL1', 20, 80, 2),
                        Wire('METAL1', 20, (62, 158), 6, True),
                        Device('nmos', 30, 40, 4, 20, 'vertical', source_net='vss', drain_net='nq'),
                        Wire('POLY', 30, (56, 104), 2, False),
                        Device('pmos', 30, 130, 4, 40, 'vertical', source_net='vdd', drain_net='nq'),
                    ],
                    'nq': [
                        Via('NDIF', 'METAL1', 40, 40, 2),
                        Wire('METAL1', 40, (42, 158), 6, True),
                        Via('PDIF', 'METAL1', 40, 120, 2),
                    ],
                    'vdd': [
                        Via('PDIF', 'METAL1', 20, 182, 2),
                        Wire('NTIE', 40, (178, 186), 10, False),
                        Via('NTIE', 'METAL1', 40, 182, 2),
                    ],
                    'vss': [
                        Via('NDIF', 'METAL1', 20, 14, 2),
                        Via('PTIE', 'METAL1', 40, 14, 2),
                        Wire('PTIE', 40, (10, 18), 10, False),
                    ],
                },
                finalize=True,
            ),
        """)[1:]
        # Currently order of elements is not deterministic.
        # Check only first four lines.
        self.assertEqual(s1[:75], s2[:75])

class LibraryTest(unittest.TestCase):
    def test_nocell(self):
        lib = Library()
        with self.assertRaises(KeyError):
            lib["foo"]

    def test_write_python(self):
        lib = Library()
        lib.write_python("/tmp/cells.py")

    def test_write_spice(self):
        lib = Library()
        lib.write_spice("/tmp")

    def test_write_spice_no_dir(self):
        lib = Library()
        with self.assertRaisesRegex(
            ValueError, "Please provide directory to write spice netlists to",
        ):
            lib.write_spice()
