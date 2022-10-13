# SPDX-License-Identifier: GPL-2.0-or-later OR AGPL-3.0-or-later OR CERN-OHL-S-2.0+
from typing import Dict, Iterable, Union, Optional, Callable, Any, overload

import numpy as np

from pdkmaster.technology import primitive as _prm
from pdkmaster.design import circuit as _ckt
from pdkmaster.io import spice as _spc


__all__ = ["SRAMCellSP6T"]


class SRAMCellSP6T:
    """Class for a classic 6T SRAM cell with a latch and NMOS passgate transistors

    This class builds a circuit for a classic 6T single port SRAM cell.This cell consists
    of a latch, e.g. two back coupled intverters and accessed through two extra transistors.
    The 6 transistor cell is syummetrical so actual consist of 3 pairs of transistors with
    with a specific function:
        - pull-up transistor: the PMOS of the inverters
        - pull-down transistr: the NMOS of the inverters
        - pass gate: the two access transistors

    The class also provides support for simulating several performance metrics on the SRAM
    cell.

    Arguments:
        cktfab: factory to generate the circuit with
        pypspicefab: faxctory to generate spice simulation setup with
        name: name of the generated circuit
        mos_pullup, mos_pulldown, mos_passgate: the technology primitive to use for each
            type of transistor; currently the pass gate transistors are assumed to be
            n type transistors
        l_pullup, l_pulldown, l_passgate: the length for each type of transistor
        w_pullup, w_pulldown, w_passgate: the width for each type of transistor
    """
    # TODO: Check transistor types
    # TODO: Monte-Carlo simulations
    def __init__(self, *,
        cktfab: _ckt.CircuitFactory, pyspicefab: _spc.PySpiceFactory,
        name: str,
        mos_pullup: _prm.MOSFET, l_pullup: float, w_pullup: float,
        mos_pulldown: _prm.MOSFET, l_pulldown: float, w_pulldown: float,
        mos_passgate: _prm.MOSFET, l_passgate: float, w_passgate: float,
        nom_vdd: float, nom_corner: _spc.CornerSpec, nom_temperature: float,
    ):
        tech = cktfab.tech
        for mos, label in (
            (mos_pullup, "pullup"),
            (mos_pulldown, "pulldown"),
            (mos_passgate, "passgate"),
        ):
            if mos not in tech.primitives:
                raise ValueError(
                    f"mos_{label} not valid for technology {tech.name}"
                )

        self._pyspicefab = pyspicefab
        self._nom_vdd = nom_vdd
        self._nom_corner = nom_corner
        self._nom_temperature = nom_temperature

        self.ckt = ckt = cktfab.new_circuit(name=name)

        # Inverter 1
        pu1 = ckt.instantiate(mos_pullup, name="pu1", l=l_pullup, w=w_pullup)
        pd1 = ckt.instantiate(mos_pulldown, name="pd1", l=l_pulldown, w=w_pulldown)
        # Inverter 2
        pu2 = ckt.instantiate(mos_pullup, name="pu2", l=l_pullup, w=w_pullup)
        pd2 = ckt.instantiate(mos_pulldown, name="pd2", l=l_pulldown, w=w_pulldown)
        # Pass gates
        pg1 = ckt.instantiate(mos_passgate, name="pg1", l=l_passgate, w=w_passgate)
        pg2 = ckt.instantiate(mos_passgate, name="pg2", l=l_passgate, w=w_passgate)

        # Nets
        ckt.new_net(name="wl", external=True, childports=(pg1.ports.gate, pg2.ports.gate))
        ckt.new_net(name="bl", external=True, childports=pg1.ports.sourcedrain2)
        ckt.new_net(name="blb", external=True, childports=pg2.ports.sourcedrain2)
        ckt.new_net(name="vdd", external=True, childports=(
            pu1.ports.sourcedrain1, pu1.ports.bulk, pu2.ports.sourcedrain1, pu2.ports.bulk,
        ))
        ckt.new_net(name="vss", external=True, childports=(
            pd1.ports.sourcedrain2, pd1.ports.bulk, pd2.ports.sourcedrain2, pd2.ports.bulk,
            pg1.ports.bulk, pg2.ports.bulk,
        ))
        ckt.new_net(name="n", external=False, childports=(
            pu1.ports.gate, pd1.ports.gate, pu2.ports.sourcedrain2, pd2.ports.sourcedrain1,
            pg1.ports.sourcedrain1,
        ))
        ckt.new_net(name="nb", external=False, childports=(
            pu1.ports.sourcedrain2, pd1.ports.sourcedrain1, pu2.ports.gate, pd2.ports.gate,
            pg2.ports.sourcedrain1,
        ))

    @property
    def name(self):
        return self.ckt.name
    @property
    def nom_vdd(self):
        return self._nom_vdd
    @property
    def nom_corner(self):
        return self._nom_corner
    @property
    def nom_temperature(self):
        return self._nom_temperature

    def Iread(self, *,
        vwl: Optional[float]=None, vpre: Optional[float]=None,
        vdd: Optional[float]=None, corner: Optional[_spc.CornerSpec]=None,
        temperature: Optional[float]=None,
    ) -> float:
        """Simulatate the read current.

        The read current is in this case defined as the current seen on the low voltage side
        of the cell with open pass gates and the bit lines voltages on the pre-charge voltage

        This metric is an indicator for the possible speed of a SRAM block.

        Arguments:
            vwl: the voltage on the wordline in V; the `vdd` voltage is taken as default
                value
            vpre: the pre-charge voltage n V on the bitlines; the `vdd` voltage is taken as
                default value
            vdd: the supply voltage in V; `nom_vdd` property is taken as default value
            corner: the process corner(s) for the run; `nom_corner` property is taken as default
                value
            temperature: the temperature in °C; `nom_temperature` property is taken as default
                value

        Returns:
            The read current
        """
        if vdd is None:
            vdd = self.nom_vdd
        if vwl is None:
            vwl = vdd
        if vpre is None:
            vpre = vdd
        if corner is None:
            corner = self.nom_corner
        if temperature is None:
            temperature = self.nom_temperature

        ckt = self._pyspicefab.new_pyspicecircuit(
            corner=corner, top=self.ckt, title="Read current", gnd="vss",
        )

        ckt.V("vdd", "vdd", ckt.gnd, vdd)
        ckt.V("wl", "wl", ckt.gnd, vwl)
        ckt.V("bl", "bl", ckt.gnd, vpre)
        ckt.V("blb", "blb", ckt.gnd, vpre)

        sim = ckt.simulator(temperature=temperature)
        sim.node_set(**{"xtop.nb": vdd})
        op: Any = sim.operating_point()
        return float(-op.vbl[0])

    def Ileak(self, *,
        vpre: Optional[float]=None, floatbl: bool=False,
        vdd: Optional[float]=None, corner: Optional[_spc.CornerSpec]=None,
        temperature: Optional[float]=None,
    ) -> float:
        """Simulatate the leakage current.

        The leakage current is the DC current running through a cell with the word line
        claused.

        This metric is an indicator for the static power consumption of a SRAM block.

        Arguments:
            vpre: the pre-charge voltage n V on the bitlines; the `vdd` voltage is taken as
                default value
            floatbl: wether the bitline is floating. If not floating the voltage on the
                bitline is forced to the precharge voltage.
            vdd: the supply voltage in V; `nom_vdd` property is taken as default value
            corner: the process corner(s) for the run; `nom_corner` property is taken as
                default value
            temperature: the temperature in °C; `nom_temperature` property is taken as default
                value

        Returns:
            The leakage current; if bitline is not floating the extra current caused by the
            forced charging is added to the total leakage current.
        """
        if vdd is None:
            vdd = self.nom_vdd
        if vpre is None:
            vpre = vdd
        if corner is None:
            corner = self.nom_corner
        if temperature is None:
            temperature = self.nom_temperature

        ckt = self._pyspicefab.new_pyspicecircuit(
            corner=corner, top=self.ckt, title="Leakage current", gnd="vss",
        )

        ckt.V("vdd", "vdd", ckt.gnd, vdd)
        ckt.V("wl", "wl", ckt.gnd, 0)
        if not floatbl:
            ckt.V("bl", "bl", ckt.gnd, vpre)
            ckt.V("blb", "blb", ckt.gnd, vpre)
        else:
            ckt.C("bl", "bl", ckt.gnd, 0)
            ckt.C("blb", "blb", ckt.gnd, 0)

        sim = ckt.simulator(temperature=temperature)
        sim.node_set(**{"xtop.nb": vdd})
        op: Any = sim.operating_point()
        I = -float(op.vvdd[0])
        if not floatbl:
            # Look at current on for chargiug
            # If currently is higher than 0 then is is extra leakage current;
            # if current is lower than 0 it is an extra path to ground and does not need
            # to be added to the leakage current
            Ibl = -float(op.vbl[0])
            Iblb = -float(op.vblb[0])
            if Ibl > 0.0:
                I += Ibl
            if Iblb > 0.0:
                I += Iblb
        return float(I)

    @overload
    def SNM(self, *,
        read: bool, vwl: None=None, vpre: Optional[float]=None,
        vdd: Optional[float]=None, corner: Optional[_spc.CornerSpec]=None,
        temperature: Optional[float]=None,
    ) -> float:
        ... # pragma: no cover
    @overload
    def SNM(self, *,
        read: None, vwl: float, vpre: Optional[float]=None,
        vdd: Optional[float]=None, corner: Optional[_spc.CornerSpec]=None,
        temperature: Optional[float]=None,
    ) -> float:
        ... # pragma: no cover
    def SNM(self, *,
        read: Optional[bool]=True, vwl: Optional[float]=None, vpre: Optional[float]=None,
        vdd: Optional[float]=None, corner: Optional[_spc.CornerSpec]=None,
        temperature: Optional[float]=None,
    ) -> float:
        """Simulate the static noise margin

        The static noise  margin is a metric for the stability of an SRAM cell. It is used
        to design a cell so no descructive reads are happening on the cell and similar.
        More information can be found in the paper: "Static-Noise Margin Analysis of MOS
        SRAM Cells", E. Seevinck et.al., IEEE Journal of Solid-State Circuits, VOL. SC-22,
        NO. 5, October 1987
        (http://bwrcs.eecs.berkeley.edu/Classes/icdesign/ee141_f04/Project/snm.pdf)

        Arguments:
            read: wether to simulate the SNM for read; if False hold is simulated.
                Read corresponds with an open word line; hold with a closed word line.
                By default read SNM will be simulated.
            vwl: the word line voltage; when this value is not None read has to be None
            vpre: the pre-charge voltage n V on the bitlines; the `vdd` voltage is taken as
                default value
            vdd: the supply voltage in V; `nom_vdd` property is taken as default value
            corner: the process corner(s) for the run; `nom_corner` property is taken as default
                value
            temperature: the temperature in °C; `nom_temperature` property is taken as default
                value
        """
        if vdd is None:
            vdd = self.nom_vdd
        if read is None:
            assert vwl is not None
        elif read:
            assert vwl is None
            vwl = vdd # Read SNM
        else:
            assert vwl is None
            vwl = 0 # Hold SNM
        if vpre is None:
            vpre = vdd
        if corner is None:
            corner = self.nom_corner
        if temperature is None:
            temperature = self.nom_temperature

        ckt = self._pyspicefab.new_pyspicecircuit(
            corner=corner, top=self.ckt, title="SNM", gnd="vss",
        )

        ckt.V("vdd", "vdd", ckt.gnd, vdd)
        ckt.V("wl", "wl", ckt.gnd, vwl)
        ckt.V("bl", "bl", ckt.gnd, vpre)
        ckt.V("blb", "blb", ckt.gnd, vpre)

        ckt.V("n", "xtop.n", ckt.gnd, 0.0)

        sim = ckt.simulator(temperature=temperature)
        sim.save(("xtop.nb",))
        dc: Any = sim.dc(vn=slice(0.0, vdd, vdd/100))

        # Currently only one sweep is simulation and then SNM is computed by using
        # the same curve reversed with x and y axis switched.
        # This is not the right way for Monte Carlo simulations where the SRAM cell is not
        # fully symmetric.
        # In that case the other internal node has to be forced and first node measured.
        # TODO: Make simulatiµon right for Monte-Carlo simulations.

        # Rotate the curves by 45 degrees
        c = np.array(dc.sweep) + np.array(dc["xtop.nb"])*1j
        r = np.abs(c)
        a = np.angle(c)
        arot = a - np.pi/4
        crot = r * np.exp(arot*1j)
        xrot = np.imag(crot)[::-1] # reverse order
        yrot = np.real(crot)[::-1] # reverse order
        c2 = np.array(dc["xtop.nb"]) + np.array(dc.sweep)*1j
        r2 = np.abs(c2)
        a2 = np.angle(c2)
        a2rot = a2 - np.pi/4
        c2rot = r * np.exp(a2rot*1j)
        x2rot = np.imag(c2rot)
        y2rot = np.real(c2rot)

        # Compute SNM from max difference on left part
        left = np.max((np.min(xrot), np.min(x2rot)))
        xleft = np.arange(left, -left/1000, -left/100)
        yleft = np.interp(xleft, xrot, yrot)
        y2left = np.interp(xleft, x2rot, y2rot)
        snmleftsq = max(y2left - yleft)
        snmleft = snmleftsq**0.5 if snmleftsq >= 0.0 else 0.0

        # Compute SNM from max difference on right part
        right = np.min((np.max(xrot), np.max(x2rot)))
        xright = np.arange(-right/1000, right, right/100)
        yright = np.interp(xright, xrot, yrot)
        y2right = np.interp(xright, x2rot, y2rot)
        snmrightsq = max(yright - y2right)
        snmright = snmrightsq**0.5 if snmrightsq >= 0.0 else 0.0

        return min((snmleft, snmright))

    def WTP(self, *,
        vwl: Optional[float]=None, vpre: Optional[float]=None,
        vdd: Optional[float]=None, corner: Optional[_spc.CornerSpec]=None,
        temperature: Optional[float]=None, debug: Optional[Dict[str, Any]]=None,
    ):
        """
        Simulate the write trip point

        The write trip point is defined as the voltage a bitline has to drop to flip
        the state of the latch of the SRAM cell. This metric is used to see if the
        cell can be written to.

        Arguments:
            vwl: the voltage on the wordline in V; the `vdd` voltage is taken as default
                value
            vpre: the pre-charge voltage n V on the bitlines; the `vdd` voltage is taken as
                default value
            vdd: the supply voltage in V; `nom_vdd` property is taken as default value
            corner: the process corner(s) for the run; `nom_corner` property is taken as default
                value
            temperature: the temperature in °C; `nom_temperature` property is taken as default
                value
        """
        if vdd is None:
            vdd = self.nom_vdd
        if vwl is None:
            vwl = vdd
        if vpre is None:
            vpre = vdd
        if corner is None:
            corner = self.nom_corner
        if temperature is None:
            temperature = self.nom_temperature
        ttrans = 1e-3

        ckt = self._pyspicefab.new_pyspicecircuit(
            corner=corner, top=self.ckt, title="WTP", gnd="vss",
        )

        ckt.V("vdd", "vdd", ckt.gnd, vdd)
        ckt.V("wl", "wl", ckt.gnd, vwl)
        ckt.PieceWiseLinearVoltageSource(
            "bl", "bl", ckt.gnd,
            values=[(0e-3, vpre), (ttrans, 0), (2*ttrans, vpre)],
            dc=vpre,
        )
        ckt.PieceWiseLinearVoltageSource(
            "blb", "blb", ckt.gnd,
            values=[(0.0, vpre), (2*ttrans, vpre), (3*ttrans, 0), (4*ttrans, vpre)],
            dc=vpre
        )

        sim = ckt.simulator(temperature=temperature)
        sim.save(("bl", "blb", "xtop.n", "xtop.nb"))
        sim.node_set(**{"xtop.n": vdd})
        trans: Any = sim.transient(step_time=ttrans/500, end_time=4*ttrans)
        if debug is not None:
            debug["trans"] = trans

        idx1ns = sum(np.array(trans.time) <= ttrans)
        idx2ns = sum(np.array(trans.time) <= 2*ttrans)
        idx3ns = sum(np.array(trans.time) <= 3*ttrans)

        # Find the voltage on the bit line when the internal SRAM nodes have the same value
        vtp10 = np.interp([0], (trans["xtop.nb"][:idx1ns] - trans["xtop.n"][:idx1ns]), trans.bl[:idx1ns])[0]
        vtp01 = np.interp([0], (trans["xtop.n"][idx2ns:idx3ns] - trans["xtop.nb"][idx2ns:idx3ns]), trans.blb[idx2ns:idx3ns])[0]

        return min(vtp10, vtp01)
