# SPDX-License-Identifier: GPL-2.0-or-later OR AGPL-3.0-or-later OR CERN-OHL-S-2.0+
# type: ignore
import unittest

from pdkmaster.technology import net as _net
from pdkmaster.design import circuit as _ckt, library as _lbry

from ..dummy import dummy_tech, dummy_lib
dummy_prims = dummy_tech.primitives


class TechnologyTest(unittest.TestCase):
    def test__instance(self):
        with self.assertRaises(TypeError):
            _ckt._Instance(name="error", ports=_net.Nets())

    def test__instancenet(self):
        inst = _ckt._PrimitiveInstance(name="inst", prim=dummy_prims.nmos)
        net1 = _ckt._InstanceNet(inst=inst, net=inst.ports.gate)
        net2 = _ckt._InstanceNet(inst=inst, net=inst.ports.bulk)

        self.assertNotEqual(net1, net2)

        self.assertEqual(hash(net1), hash(net1.full_name))
        self.assertNotEqual(hash(net1), hash(net2))

    def test__cellinstance(self):
        # Code coverage
        _ = _ckt._CellInstance(name="inst", cell=dummy_lib.cells.cell1)
        _ = _ckt._CellInstance(name="inst", cell=dummy_lib.cells.cell1, circuitname="cell1")

    def test__circuitnet(self):
        # Code coverage
        dummy_lib.cells.cell1.circuit.nets.i.freeze()

    def test__circuit(self):
        # Code coverage
        cell1 = _lbry._Cell(lib=dummy_lib, name="test1")
        ckt1 = cell1.new_circuit()

        inst1 = ckt1.instantiate(dummy_prims.nmos, name="nmos")
        ckt1.instantiate(dummy_lib.cells.cell1, name="cell1")

        vss = ckt1.new_net(name="vss", external=True, childports=inst1.ports.bulk)
        self.assertEqual(
            ckt1.net_lookup(port=inst1.ports.bulk),
            vss,
        )
        with self.assertRaises(ValueError):
            ckt1.net_lookup(port=inst1.ports.gate)

        self.assertEqual(
            tuple(ckt1.subcells_sorted),
            (dummy_lib.cells.cell1,),
        )
            
        cell2 = _lbry._Cell(lib=dummy_lib, name="test1")
        ckt2 = cell2.new_circuit()

        ckt2.instantiate(cell1, name="cell1")

        self.assertEqual(
            tuple(ckt2.subcells_sorted),
            (dummy_lib.cells.cell1, cell1),
        )

