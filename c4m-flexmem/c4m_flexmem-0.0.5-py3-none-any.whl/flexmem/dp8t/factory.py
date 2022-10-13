# SPDX-License-Identifier: GPL-2.0-or-later OR AGPL-3.0-or-later OR CERN-OHL-S-2.0+
from typing import Any, Tuple, Dict, Iterable, Optional

from pdkmaster.technology import (
    property_ as _prp, geometry as _geo, primitive as _prm,
)
from pdkmaster.design import library as _lbry

from ..common import (
    _SRAMSpecification, _SRAMFactory, _TechCache, _FactoryCell,
    _BitCell, _WordlineDriver, _RowDecoderDrivePage, _RowDecoder, _RowPeriphery,
    _Precharge, _ColMux, _ColumnPeriphery, _Column,
)


__all__ = ["DP8TSpecification", "DP8TFactory"]


class DP8TSpecification(_SRAMSpecification):
    """Class to provide specification for the single port SRAM generation.
    """
    def __init__(self, *,
        name_prefix: str="DP8T",
        nmos: _prm.MOSFET, pmos: _prm.MOSFET, stdcelllib: _lbry.Library,
        pu_l: float, pu_w: float, pd_l: float, pd_w: float, pg_l: float, pg_w: float,
        precharge_l: Optional[float] = None, precharge_w: float,
        colmux_l: Optional[float] = None, colmux_w: float,
        writedrive_l: Optional[float] = None, writedrive_w: float,
        wldrive_nmos_l: Optional[float] = None, wldrive_nmos_w: float,
        wldrive_pmos_l: Optional[float] = None, wldrive_pmos_w: float,
        prbound: Optional[_prm.Auxiliary] = None):
        super().__init__(
            name_prefix=name_prefix,
            nmos=nmos, pmos=pmos, stdcelllib=stdcelllib,
            pu_l=pu_l, pu_w=pu_w, pd_l=pd_l, pd_w=pd_w, pg_l=pg_l, pg_w=pg_w,
            precharge_l=precharge_l, precharge_w=precharge_w,
            colmux_l=colmux_l, colmux_w=colmux_w,
            writedrive_l=writedrive_l, writedrive_w=writedrive_w,
            wldrive_nmos_l=wldrive_nmos_l, wldrive_nmos_w=wldrive_nmos_w,
            wldrive_pmos_l=wldrive_pmos_l, wldrive_pmos_w=wldrive_pmos_w,
            prbound=prbound,
        )


class _DP8TFactoryCell(_FactoryCell["DP8TFactory"]):
    pass


class _DP8TCell(_BitCell["DP8TFactory"]):
    def __init__(self, *, fab: "DP8TFactory", name: str):
        cache = fab._cache
        m2pin = cache.metalpin(2)
        m3pin = cache.metalpin(3)

        self.dc_signals = (("vss", m3pin), ("vdd", m3pin))
        self.wl_signals = (("wl1", m3pin), ("wl2", m3pin))
        self.bl_signals = (("bl1", m2pin), ("bl2", m2pin))

        super().__init__(fab=fab, name=name)

        self._wl1_bottom: Optional[float] = None
        self._wl1_top: Optional[float] = None
        self._wl2_bottom: Optional[float] = None
        self._wl2_top: Optional[float] = None
        self._bl1_left: Optional[float] = None
        self._bl1_right: Optional[float] = None
        self._bl1n_left: Optional[float] = None
        self._bl1n_right: Optional[float] = None
        self._bl2_left: Optional[float] = None
        self._bl2_right: Optional[float] = None
        self._bl2n_left: Optional[float] = None
        self._bl2n_right: Optional[float] = None

    @property
    def wl1_bottom(self) -> float:
        if self._wl1_bottom is None:
            self.layout # Generate layout
            assert self._wl1_bottom is not None
        return self._wl1_bottom
    @property
    def wl1_top(self) -> float:
        if self._wl1_top is None:
            self.layout # Generate layout
            assert self._wl1_top is not None
        return self._wl1_top
    @property
    def wl2_bottom(self) -> float:
        if self._wl2_bottom is None:
            self.layout # Generate layout
            assert self._wl2_bottom is not None
        return self._wl2_bottom
    @property
    def wl2_top(self) -> float:
        if self._wl2_top is None:
            self.layout # Generate layout
            assert self._wl2_top is not None
        return self._wl2_top
    @property
    def bl1_left(self) -> float:
        if self._bl1_left is None:
            self.layout # Generate layout
            assert self._bl1_left is not None
        return self._bl1_left
    @property
    def bl1_right(self) -> float:
        if self._bl1_right is None:
            self.layout # Generate layout
            assert self._bl1_right is not None
        return self._bl1_right
    @property
    def bl1n_left(self) -> float:
        if self._bl1n_left is None:
            self.layout # Generate layout
            assert self._bl1n_left is not None
        return self._bl1n_left
    @property
    def bl1n_right(self) -> float:
        if self._bl1n_right is None:
            self.layout # Generate layout
            assert self._bl1n_right is not None
        return self._bl1n_right
    @property
    def bl2_left(self) -> float:
        if self._bl2_left is None:
            self.layout # Generate layout
            assert self._bl2_left is not None
        return self._bl2_left
    @property
    def bl2_right(self) -> float:
        if self._bl2_right is None:
            self.layout # Generate layout
            assert self._bl2_right is not None
        return self._bl2_right
    @property
    def bl2n_left(self) -> float:
        if self._bl2n_left is None:
            self.layout # Generate layout
            assert self._bl2n_left is not None
        return self._bl2n_left
    @property
    def bl2n_right(self) -> float:
        if self._bl2n_right is None:
            self.layout # Generate layout
            assert self._bl2n_right is not None
        return self._bl2n_right

    def _create_circuit(self):
        fab = self.fab
        spec = fab.spec

        ckt = self.new_circuit()

        pu1 = ckt.instantiate(spec.pmos, name="pu1", l=spec.pu_l, w=spec.pu_w)
        pu2 = ckt.instantiate(spec.pmos, name="pu2", l=spec.pu_l, w=spec.pu_w)

        pd1 = ckt.instantiate(spec.nmos, name="pd1", l=spec.pd_l, w=spec.pd_w)
        pd2 = ckt.instantiate(spec.nmos, name="pd2", l=spec.pd_l, w=spec.pd_w)

        pg1 = ckt.instantiate(spec.nmos, name="pg1", l=spec.pg_l, w=spec.pg_w)
        pg1n = ckt.instantiate(spec.nmos, name="pg1n", l=spec.pg_l, w=spec.pg_w)
        pg2 = ckt.instantiate(spec.nmos, name="pg2", l=spec.pg_l, w=spec.pg_w)
        pg2n = ckt.instantiate(spec.nmos, name="pg2n", l=spec.pg_l, w=spec.pg_w)

        ckt.new_net(name="vdd", external=True, childports=(
            pu1.ports.sourcedrain1, pu1.ports.bulk,
            pu2.ports.sourcedrain1, pu2.ports.bulk,
        ))
        ckt.new_net(name="vss", external=True, childports=(
            pd1.ports.sourcedrain1, pd1.ports.bulk,
            pd2.ports.sourcedrain1, pd2.ports.bulk,
            pg1.ports.bulk, pg1n.ports.bulk,
            pg2.ports.bulk, pg2n.ports.bulk,
        ))

        ckt.new_net(name="wl1", external=True, childports=(
            pg1.ports.gate, pg1n.ports.gate,
        ))
        ckt.new_net(name="wl2", external=True, childports=(
            pg2.ports.gate, pg2n.ports.gate,
        ))

        ckt.new_net(name="bl1", external=True, childports=pg1.ports.sourcedrain1)
        ckt.new_net(name="bl1_n", external=True, childports=pg1n.ports.sourcedrain1)
        ckt.new_net(name="bl2", external=True, childports=pg2.ports.sourcedrain1)
        ckt.new_net(name="bl2_n", external=True, childports=pg2n.ports.sourcedrain1)

        ckt.new_net(name="bit", external=False, childports=(
            pg1.ports.sourcedrain2, pg2.ports.sourcedrain2,
            pd1.ports.sourcedrain2, pu1.ports.sourcedrain2,
            pd2.ports.gate, pu2.ports.gate,
        ))
        ckt.new_net(name="bit_n", external=False, childports=(
            pg1n.ports.sourcedrain2, pg2n.ports.sourcedrain2,
            pd2.ports.sourcedrain2, pu2.ports.sourcedrain2,
            pd1.ports.gate, pu1.ports.gate,
        ))

    def _create_layout(self):
        fab = self.fab
        tech = fab.tech
        spec = fab.spec
        cache = fab._cache

        nmos = spec.nmos
        pmos = spec.pmos

        nwell = cache.nwell
        pwell = cache.pwell
        active = cache.active
        nimplant = cache.nimplant
        pimplant = cache.pimplant
        contact = cache.contact
        poly = cache.poly
        metal1 = cache.metal(1)
        via1 = cache.via(1)
        metal2 = cache.metal(2)
        metal2pin = cache.metalpin(2)
        via2 = cache.via(2)
        metal3 = cache.metal(3)
        metal3pin = cache.metalpin(3)

        # First get circuit, this also ensures that it has been generated
        ckt = self.circuit
        insts = ckt.instances
        nets = ckt.nets

        layouter = self.new_circuitlayouter()
        layout = self.layout

        nwell_net = None if nwell is None else nets.vdd
        pwell_net = None if pwell is None else nets.vss

        # Compute some derived rules
        idx = contact.bottom.index(active)
        enc = contact.min_bottom_enclosure[idx]
        # For some contacts we will use minimal enclosure in all sides
        # This is to avoid that the longer extension would overlap with
        # the active under a transistor gate.
        chact_enc_min = _prp.Enclosure(enc.min())

        # Generate layout of instances and interconnects
        _pu1_lay = layouter.inst_layout(inst=insts.pu1, rotation=_geo.Rotation.R270)
        _pu2_lay = layouter.inst_layout(inst=insts.pu2, rotation=_geo.Rotation.R270)

        _pd1_lay = layouter.inst_layout(inst=insts.pd1)
        _pd2_lay = layouter.inst_layout(inst=insts.pd2, rotation=_geo.Rotation.R180)

        _pg1_lay = layouter.inst_layout(inst=insts.pg1, rotation=_geo.Rotation.R90)
        _pg1n_lay = layouter.inst_layout(inst=insts.pg1n, rotation=_geo.Rotation.R90)
        _pg2_lay = layouter.inst_layout(inst=insts.pg2, rotation=_geo.Rotation.R90)
        _pg2n_lay = layouter.inst_layout(inst=insts.pg2n, rotation=_geo.Rotation.R90)

        _chbl1_lay = layouter.wire_layout(
            net=nets.bl1, wire=contact, well_net=pwell_net,
            bottom=active, bottom_implant=nimplant, bottom_well=pwell,
            bottom_width=spec.pg_w, bottom_enclosure=chact_enc_min,
            top_enclosure="tall"
        )
        _chbl1n_lay = layouter.wire_layout(
            net=nets.bl1_n, wire=contact, well_net=pwell_net,
            bottom=active, bottom_implant=nimplant, bottom_well=pwell,
            bottom_width=spec.pg_w, bottom_enclosure=chact_enc_min,
            top_enclosure="tall",
        )
        _chbl2_lay = layouter.wire_layout(
            net=nets.bl2, wire=contact, well_net=pwell_net,
            bottom=active, bottom_implant=nimplant, bottom_well=pwell,
            bottom_width=spec.pg_w, bottom_enclosure=chact_enc_min,
            top_enclosure="tall"
        )
        _chbl2n_lay = layouter.wire_layout(
            net=nets.bl2_n, wire=contact, well_net=pwell_net,
            bottom=active, bottom_implant=nimplant, bottom_well=pwell,
            bottom_width=spec.pg_w, bottom_enclosure=chact_enc_min,
            top_enclosure="tall",
        )

        _chvsspd1_lay = layouter.wire_layout(
            net=nets.vss, wire=contact, well_net=pwell_net,
            bottom=active, bottom_implant=nimplant, bottom_well=pwell,
            bottom_height=spec.pd_w, bottom_enclosure=chact_enc_min,
            top_enclosure="tall"
        )
        _chvsspd2_lay = layouter.wire_layout(
            net=nets.vss, wire=contact, well_net=pwell_net,
            bottom=active, bottom_implant=nimplant, bottom_well=pwell,
            bottom_height=spec.pd_w, bottom_enclosure=chact_enc_min,
            top_enclosure="tall",
        )

        _chvddpu1_lay = layouter.wire_layout(
            net=nets.vdd, wire=contact, well_net=nwell_net,
            bottom=active, bottom_implant=pimplant, bottom_well=nwell,
            bottom_width=spec.pu_w, bottom_enclosure=chact_enc_min,
            top_enclosure="wide",
        )
        _chvddpu2_lay = layouter.wire_layout(
            net=nets.vdd, wire=contact, well_net=nwell_net,
            bottom=active, bottom_implant=pimplant, bottom_well=nwell,
            bottom_width=spec.pu_w, bottom_enclosure=chact_enc_min,
            top_enclosure="wide",
        )

        net = nets.bit
        _chbitnimpl1_lay = layouter.wire_layout(
            net=net, wire=contact, well_net=pwell_net,
            bottom=active, bottom_implant=nimplant, bottom_well=pwell,
            bottom_enclosure="wide", top_enclosure="tall",
        )
        _chbitnimpl2_lay = layouter.wire_layout(
            net=net, wire=contact, well_net=pwell_net,
            bottom=active, bottom_implant=nimplant, bottom_well=pwell,
            bottom_width=spec.pg_w, bottom_enclosure=chact_enc_min,
            top_enclosure="wide",
        )
        _chbitpimpl_lay = layouter.wire_layout(
            net=net, wire=contact, well_net=nwell_net,
            bottom=active, bottom_implant=pimplant, bottom_well=nwell,
            bottom_width=spec.pu_w, bottom_enclosure="wide",
            top_enclosure="tall",
        )
        _chbitpimpl_chbb = _chbitpimpl_lay.bounds(mask=contact.mask)
        _chbitgate_lay = layouter.wire_layout(
            net=net, wire=contact, bottom=poly, bottom_enclosure="wide",
            top_enclosure="tall",
        )

        net = nets.bit_n
        _chbitnnimpl1_lay = layouter.wire_layout(
            net=net, wire=contact, well_net=pwell_net,
            bottom=active, bottom_implant=nimplant, bottom_well=pwell,
            bottom_enclosure="wide", top_enclosure="tall",
        )
        _chbitnnimpl2_lay = layouter.wire_layout(
            net=net, wire=contact, well_net=pwell_net,
            bottom=active, bottom_implant=nimplant, bottom_well=pwell,
            bottom_width=spec.pg_w, bottom_enclosure=chact_enc_min,
            top_enclosure="wide",
        )
        _chbitnpimpl_lay = layouter.wire_layout(
            net=net, wire=contact, well_net=nwell_net,
            bottom=active, bottom_implant=pimplant, bottom_well=nwell,
            bottom_width=spec.pu_w, bottom_enclosure="wide",
            top_enclosure="tall",
        )
        _chbitngate_lay = layouter.wire_layout(
            net=net, wire=contact, bottom=poly, bottom_enclosure="wide",
            top_enclosure="tall",
        )
        _chbitngate2_lay = layouter.wire_layout(
            net=net, wire=contact, bottom=poly, bottom_enclosure="wide",
            top_enclosure="tall",
        )

        _chwl1_lay = layouter.wire_layout(
            net=nets.wl1, wire=contact, bottom=poly,
            bottom_enclosure="wide", top_enclosure="tall",
        )
        _chwl2_lay = layouter.wire_layout(
            net=nets.wl2, wire=contact, bottom=poly,
            bottom_enclosure="wide", top_enclosure="tall",
        )

        # Compute bounding boxes
        _pu1_actbb = _pu1_lay.bounds(mask=active.mask)
        _pu1_polybb = _pu1_lay.bounds(mask=poly.mask)
        _chvddpu1_actbb = _chvddpu1_lay.bounds(mask=active.mask)
        _chvddpu1_chbb = _chvddpu1_lay.bounds(mask=contact.mask)

        _pd1_actbb = _pd1_lay.bounds(mask=active.mask)
        _pd1_polybb = _pd1_lay.bounds(mask=poly.mask)
        _chvsspd1_actbb = _chvsspd1_lay.bounds(mask=active.mask)
        _chvsspd1_chbb = _chvsspd1_lay.bounds(mask=contact.mask)
        _chbitnimpl1_actbb = _chbitnimpl1_lay.bounds(mask=active.mask)
        _chbitnimpl2_chbb = _chbitnimpl2_lay.bounds(mask=contact.mask)

        _pg1_actbb = _pg1_lay.bounds(mask=active.mask)
        _pg1_polybb = _pg1_lay.bounds(mask=poly.mask)

        _chbl_actbb = _chbl1_lay.bounds(mask=active.mask)
        _chbl_chbb = _chbl1_lay.bounds(mask=contact.mask)

        _chbitgate_polybb = _chbitgate_lay.bounds(mask=poly.mask)

        _chwl_polybb = _chwl1_lay.bounds(mask=poly.mask)
        _chwl_m1bb = _chwl1_lay.bounds(mask=metal1.mask)

        # Put ch_vsspd1/ch_bl contact on the edge
        x_chvsspd1 = y_chbl = 0.0

        # Place pu1/pd1/pg1 minimum space fron contact
        x_pd1 = (
            x_chvsspd1 + _chvsspd1_chbb.right
            + nmos.computed.min_contactgate_space
            - _pd1_polybb.left
        )
        y_pg = ( # pg1 and pg2 at the same height
            y_chbl + _chbl_chbb.top
            + nmos.computed.min_contactgate_space
            - _pg1_polybb.bottom
        )

        # Compute placement of pd1/pg1 poly at minimum space
        y_pd = y_pg + _pg1_polybb.top + poly.min_space - _pd1_polybb.bottom
        y_chvsspd = y_pd + _pd1_actbb.top - _chvsspd1_actbb.top

        x_pg1 = max(
            x_pd1 + _pd1_polybb.right + cache.min_actpoly_space - _pg1_actbb.left,
            (
                0.5*tech.computed.min_width(active, up=True, min_enclosure=True)
                + cache.min_nactpact_space - _pg1_actbb.left
            ),
        )
        x_pg1n = x_pg1 + _pg1_actbb.width + active.min_space
        x_chbl1 = x_pg1
        x_via1bl1 = x_chbl1
        x_chbl1n = x_pg1n
        x_via1bl1n = x_chbl1n

        x_chbitnimpl1 = x_pg1 + _pg1_actbb.right - _chbitnimpl1_actbb.right
        y_chbitnimpl1 = y_pd + _pd1_actbb.top - _chbitnimpl1_actbb.top
        y_chbitnnimpl1 = y_chbitnimpl1

        x_chbitnnimpl2 = x_pg1n
        y_chbitnnimpl2 = (
            y_pg + _pg1_polybb.top + nmos.computed.min_contactgate_space
            - _chbitnimpl2_chbb.bottom
        )

        x_chwl1 = x_pg1n + _pg1_actbb.right + cache.min_actmaxpad_space - _chwl_polybb.left
        y_chwl1 = max(
            0.5*poly.min_space - _chwl_polybb.bottom,
            0.5*metal1.min_space - _chwl_m1bb.bottom,
        )
        y_chwl2 = y_chwl1 + max(
            _chwl_polybb.height + poly.min_space,
            _chwl_m1bb.height + metal1.min_space,
        )

        # x placement of pu
        x_pu1 = (
            x_pd1 + _pd1_polybb.right + cache.min_actpoly_space - _pu1_actbb.left
        )
        x_chbitpimpl = x_pu1
        x_chvddpu1 = x_pu1

        # Make place for vertical poly connection on wl2
        x_chwl2 = x_chwl1
        x_pg2 = x_chwl1 + (x_chwl1 - x_pg1n)
        y_pg2 = y_chwl2 + _chwl_polybb.bottom - _pg1_polybb.bottom
        y_chbitnimpl2 = (
            y_pg2 + _pg1_polybb.top + nmos.computed.min_contactgate_space
            - _chbitnimpl2_chbb.bottom
        )
        x_chbl2 = x_pg2
        x_via1bl2 = x_chbl2
        left_wl2polycon = x_pg2 + _pg1_actbb.right + cache.min_actpoly_space
        right_wl2polycon = left_wl2polycon + poly.min_width
        x_pg2n = right_wl2polycon + cache.min_actpoly_space - _pg1_actbb.left
        x_chbl2n = x_pg2n
        x_via1bl2n = x_chbl2n

        # Same space to edge on left and right
        cell_width = x_pg2n + x_pg1

        # y placement of pu
        nact_top = max(
            y_pd + _pd1_actbb.top,
            y_chbitnimpl2 + _chbitnimpl1_actbb.top,
        )
        nactpact_space = cache.min_actpwell_enclosure + cache.min_actnwell_enclosure

        y_chbitpimpl = nact_top + nactpact_space - _pu1_actbb.bottom
        y_pu = (
            y_chbitpimpl + _chbitpimpl_chbb.top + pmos.computed.min_contactgate_space
            - _pu1_polybb.bottom
        )
        y_chvddpu = (
            y_pu + _pu1_polybb.top + pmos.computed.min_contactgate_space
            - _chvddpu1_chbb.bottom
        )
        y_chvddnwell = y_chvddpu

        cell_height = y_chvddpu

        # The rest is place symeetric in the cell
        x_chvsspd2 = cell_width - x_chvsspd1
        x_pd2 = cell_width - x_pd1

        x_pu2 = cell_width - x_pu1
        x_chbitnnimpl1 = cell_width - x_chbitnimpl1
        x_chbitnimpl2 = x_pg2
        x_chbitnpimpl = x_pu2
        x_chvddpu2 = x_pu2

        # Place the sublayouts and compute some bounding boxes
        chvsspd1_lay = layouter.place(_chvsspd1_lay, x=x_chvsspd1, y=y_chvsspd)
        chvsspd1_actbb = chvsspd1_lay.bounds(mask=active.mask)
        pd1_lay = layouter.place(_pd1_lay, x=x_pd1, y=y_pd)
        pd1_nimplbb = pd1_lay.bounds(mask=nimplant.mask)
        pd1_actbb = pd1_lay.bounds(mask=active.mask)
        pd1_polybb = pd1_lay.bounds(mask=poly.mask)
        pg1_lay = layouter.place(_pg1_lay, x=x_pg1, y=y_pg)
        pg1_actbb = pg1_lay.bounds(mask=active.mask)
        pg1_polybb = pg1_lay.bounds(mask=poly.mask)
        chbl1_lay = layouter.place(_chbl1_lay, x=x_chbl1, y=y_chbl)
        chbl1_nimplbb = chbl1_lay.bounds(mask=nimplant.mask)
        pg1n_lay = layouter.place(_pg1n_lay, x=x_pg1n, y=y_pg)
        chbl1n_lay = layouter.place(_chbl1n_lay, x=x_chbl1n, y=y_chbl)

        chbitnimpl1_lay = layouter.place(_chbitnimpl1_lay, x=x_chbitnimpl1, y=y_chbitnimpl1)
        chbitnimpl1_m1bb = chbitnimpl1_lay.bounds(mask=metal1.mask)
        chbitnnimpl1_lay = layouter.place(_chbitnnimpl1_lay, x=x_chbitnnimpl1, y=y_chbitnnimpl1)
        chbitnnimpl1_m1bb = chbitnnimpl1_lay.bounds(mask=metal1.mask)

        chbitnimpl2_lay = layouter.place(_chbitnimpl2_lay, x=x_chbitnimpl2, y=y_chbitnimpl2)
        chbitnimpl2_m1bb = chbitnimpl2_lay.bounds(mask=metal1.mask)
        chbitnnimpl2_lay = layouter.place(_chbitnnimpl2_lay, x=x_chbitnnimpl2, y=y_chbitnnimpl2)
        chbitnnimpl2_m1bb = chbitnnimpl2_lay.bounds(mask=metal1.mask)

        chwl1_lay = layouter.place(_chwl1_lay, x=x_chwl1, y=y_chwl1)
        chwl1_polybb = chwl1_lay.bounds(mask=poly.mask)
        chwl1_m1bb = chwl1_lay.bounds(mask=metal1.mask)

        chwl2_lay = layouter.place(_chwl2_lay, x=x_chwl2, y=y_chwl2)
        chwl2_polybb = chwl2_lay.bounds(mask=poly.mask)
        chwl2_m1bb = chwl2_lay.bounds(mask=metal1.mask)

        pg2_lay = layouter.place(_pg2_lay, x=x_pg2, y=y_pg2)
        pg2_actbb = pg2_lay.bounds(mask=active.mask)
        pg2_polybb = pg2_lay.bounds(mask=poly.mask)
        chbl2_lay = layouter.place(_chbl2_lay, x=x_chbl2, y=y_chbl)
        chbl2_actbb = chbl2_lay.bounds(mask=active.mask)
        pg2n_lay = layouter.place(_pg2n_lay, x=x_pg2n, y=y_pg)
        pg2n_actbb = pg2n_lay.bounds(mask=active.mask)
        pg2n_polybb = pg2n_lay.bounds(mask=poly.mask)
        chbl2n_lay = layouter.place(_chbl2n_lay, x=x_chbl2n, y=y_chbl)
        pd2_lay = layouter.place(_pd2_lay, x=x_pd2, y=y_pd)
        pd2_actbb = pd2_lay.bounds(mask=active.mask)
        pd2_polybb = pd2_lay.bounds(mask=poly.mask)
        chvsspd2_lay = layouter.place(_chvsspd2_lay, x=x_chvsspd2, y=y_chvsspd)

        chbitpimpl_lay = layouter.place(_chbitpimpl_lay, x=x_chbitpimpl, y=y_chbitpimpl)
        chbitpimpl_m1bb = chbitpimpl_lay.bounds(mask=metal1.mask)
        pu1_lay = layouter.place(_pu1_lay, x=x_pu1, y=y_pu)
        pu1_actbb = pu1_lay.bounds(mask=active.mask)
        pu1_polybb = pu1_lay.bounds(mask=poly.mask)
        chvddpu1_lay = layouter.place(_chvddpu1_lay, x=x_chvddpu1, y=y_chvddpu)
        chvddpu1_m1bb = chvddpu1_lay.bounds(mask=metal1.mask)

        chbitnpimpl_lay = layouter.place(_chbitnpimpl_lay, x=x_chbitnpimpl, y=y_chbitpimpl)
        chbitnpimpl_m1bb = chbitnpimpl_lay.bounds(mask=metal1.mask)
        pu2_lay = layouter.place(_pu2_lay, x=x_pu2, y=y_pu)
        pu2_polybb = pu2_lay.bounds(mask=poly.mask)
        chvddpu2_lay = layouter.place(_chvddpu2_lay, x=x_chvddpu2, y=y_chvddpu)
        chvddpu2_m1bb = chvddpu2_lay.bounds(mask=metal1.mask)

        # Internally connect the cell, draw pins and connect them
        shape = _geo.Rect.from_rect(
            rect=chbl1_nimplbb, top=pd1_nimplbb.top, right=(cell_width - chbl1_nimplbb.left)
        )
        layouter.add_portless(prim=nimplant, shape=shape)

        shape = _geo.Rect.from_rect(
            rect=pg1_actbb, bottom=pg1_actbb.top, top=pd1_actbb.top,
        )
        layouter.add_wire(
            net=nets.bit, wire=active, implant=nimplant, well=pwell, well_net=pwell_net,
            shape=shape,
        )

        shape = _geo.Rect.from_rect(rect=pg1_polybb, right=chwl1_polybb.right)
        layouter.add_wire(wire=poly, net=nets.wl1, shape=shape)

        shape = _geo.Rect.from_rect(
            rect=pg2_polybb, left=chwl2_polybb.left, right=right_wl2polycon,
        )
        layouter.add_wire(wire=poly, net=nets.wl2, shape=shape)
        shape = _geo.Rect.from_rect(rect=pg2n_polybb, left=left_wl2polycon)
        layouter.add_wire(wire=poly, net=nets.wl2, shape=shape)
        shape = _geo.Rect(
            left=left_wl2polycon, bottom=pg2n_polybb.bottom,
            right=right_wl2polycon, top=pg2_polybb.top,
        )
        layouter.add_wire(wire=poly, net=nets.wl2, shape=shape)

        via1bl1_lay = layouter.add_wire(
            net=nets.bl1, wire=via1, x=x_via1bl1, y=0.0,
            bottom_enclosure="wide", top_enclosure="tall",
        )
        via1bl1_m2bb = via1bl1_lay.bounds(mask=metal2.mask)
        shape = _geo.Rect.from_rect(rect=via1bl1_m2bb, top=cell_height)
        layouter.add_wire(net=nets.bl1, wire=metal2, pin=metal2pin, shape=shape)
        self._bl1_left = shape.left
        self._bl1_right = shape.right

        via1bl1n_lay = layouter.add_wire(
            net=nets.bl1_n, wire=via1, x=x_via1bl1n, y=0.0,
            bottom_enclosure="wide", top_enclosure="tall",
        )
        via1bl1n_m2bb = via1bl1n_lay.bounds(mask=metal2.mask)
        shape = _geo.Rect.from_rect(rect=via1bl1n_m2bb, top=cell_height)
        layouter.add_wire(net=nets.bl1_n, wire=metal2, pin=metal2pin, shape=shape)
        self._bl1n_left = shape.left
        self._bl1n_right = shape.right

        via1bl2_lay = layouter.add_wire(
            net=nets.bl2, wire=via1, x=x_via1bl2, y=0.0,
            bottom_enclosure="wide", top_enclosure="tall",
        )
        via1bl2_m2bb = via1bl2_lay.bounds(mask=metal2.mask)
        shape = _geo.Rect.from_rect(rect=via1bl2_m2bb, top=cell_height)
        layouter.add_wire(net=nets.bl2, wire=metal2, pin=metal2pin, shape=shape)
        self._bl2_left = shape.left
        self._bl2_right = shape.right
        shape = _geo.Rect.from_rect(rect=chbl2_actbb, top=pg2_actbb.bottom)
        layouter.add_wire(
            net=nets.bl2, wire=active, implant=nimplant, well=pwell, well_net=pwell_net,
            shape=shape,
        )

        via1bl2n_lay = layouter.add_wire(
            net=nets.bl2_n, wire=via1, x=x_via1bl2n, y=0.0,
            bottom_enclosure="wide", top_enclosure="tall",
        )
        via1bl2n_m2bb = via1bl2n_lay.bounds(mask=metal2.mask)
        shape = _geo.Rect.from_rect(rect=via1bl2n_m2bb, top=cell_height)
        layouter.add_wire(net=nets.bl2_n, wire=metal2, pin=metal2pin, shape=shape)
        self._bl2n_left = shape.left
        self._bl2n_right = shape.right

        shape = _geo.Rect.from_rect(
            rect=pg2n_actbb, bottom=pg2n_actbb.top, top=pd2_actbb.top,
        )
        layouter.add_wire(
            net=nets.bit_n, wire=active, implant=nimplant, well=pwell, well_net=pwell_net,
            shape=shape,
        )
        shape = _geo.Rect.from_rect(rect=chbitnpimpl_m1bb, bottom=chbitnnimpl1_m1bb.bottom)
        layouter.add_wire(net=nets.bit_n, wire=metal1, shape=shape)
        shape = _geo.Rect.from_rect(rect=pd1_polybb, top=pu1_polybb.top)
        layouter.add_wire(net=nets.bit_n, wire=poly, shape=shape)

        shape = _geo.Rect.from_rect(rect=pd2_polybb, top=pu2_polybb.top)
        layouter.add_wire(net=nets.bit, wire=poly, shape=shape)
        shape = _geo.Rect.from_rect(rect=chbitpimpl_m1bb, bottom=chbitnimpl1_m1bb.bottom)
        layouter.add_wire(net=nets.bit, wire=metal1, shape=shape)

        shape = _geo.Rect.from_rect(rect=chvddpu1_m1bb, right=chvddpu2_m1bb.right)
        layouter.add_wire(net=nets.vdd, wire=metal1, shape=shape)

        # m3 wl1 pin + connection
        _via1wl1_lay = layouter.wire_layout(
            net=nets.wl1, wire=via1,
            bottom_enclosure="wide", top_enclosure="wide",
        )
        _via1wl1_m1bb = _via1wl1_lay.bounds(mask=metal1.mask)
        _via2wl1_lay = layouter.wire_layout(
            net=nets.wl1, wire=via2,
            bottom_enclosure="wide", top_enclosure="wide",
        )
        _via2wl1_m2bb = _via2wl1_lay.bounds(mask=metal2.mask)

        x_via1wl1 = x_chwl1
        y_via1wl1 = chwl1_m1bb.top - _via1wl1_m1bb.top
        via1wl1_lay = layouter.place(_via1wl1_lay, x=x_via1wl1, y=y_via1wl1)
        via1wl1_m2bb = via1wl1_lay.bounds(mask=metal2.mask)
        x_via2wl1 = x_via1wl1
        y_via2wl1 = via1wl1_m2bb.top - _via2wl1_m2bb.top
        via2wl1_lay = layouter.place(_via2wl1_lay, x=x_via2wl1, y=y_via2wl1)
        via2wl1_m3bb = via2wl1_lay.bounds(mask=metal3.mask)

        shape = _geo.Rect.from_rect(
            rect=via2wl1_m3bb, left=0.0, right=cell_width,
        )
        layouter.add_wire(net=nets.wl1, wire=metal3, pin=metal3pin, shape=shape)
        self._wl1_bottom = shape.bottom
        self._wl1_top = shape.top

        # m3 wl2 pin + connection
        _via1wl2_lay = layouter.wire_layout(
            net=nets.wl2, wire=via1,
            bottom_enclosure="wide", top_enclosure="wide",
        )
        _via1wl2_m1bb = _via1wl2_lay.bounds(mask=metal1.mask)
        _via2wl2_lay = layouter.wire_layout(
            net=nets.wl2, wire=via2,
            bottom_enclosure="wide", top_enclosure="wide",
        )
        _via2wl2_m2bb = _via2wl2_lay.bounds(mask=metal2.mask)

        x_via1wl2 = x_chwl2
        y_via1wl2 = chwl2_m1bb.top - _via1wl2_m1bb.top
        via1wl2_lay = layouter.place(_via1wl2_lay, x=x_via1wl2, y=y_via1wl2)
        via1wl2_m2bb = via1wl2_lay.bounds(mask=metal2.mask)
        x_via2wl2 = x_via1wl2
        y_via2wl2 = via1wl2_m2bb.top - _via2wl2_m2bb.top
        via2wl2_lay = layouter.place(_via2wl2_lay, x=x_via2wl2, y=y_via2wl2)
        via2wl2_m3bb = via2wl2_lay.bounds(mask=metal3.mask)

        shape = _geo.Rect.from_rect(
            rect=via2wl2_m3bb, left=0.0, right=cell_width,
        )
        layouter.add_wire(net=nets.wl2, wire=metal3, pin=metal3pin, shape=shape)
        self._wl2_bottom = shape.bottom
        self._wl2_top = shape.top

        # Place + connect chbitngate
        x_chbitngate = pd2_polybb.left - poly.min_space - _chbitgate_polybb.right
        y_chbitngate = pd2_actbb.top + cache.min_actpad_space - _chbitgate_polybb.bottom
        x_chbitngate2 = x_pg1n
        y_chbitngate2 = y_chbitngate

        chbitngate_lay = layouter.place(_chbitngate_lay, x=x_chbitngate, y=y_chbitngate)
        chbitngate_polybb = chbitngate_lay.bounds(mask=poly.mask)
        chbitngate2_lay = layouter.place(_chbitngate2_lay, x=x_chbitngate2, y=y_chbitngate2)
        chbitngate2_m1bb = chbitngate2_lay.bounds(mask=metal1.mask)

        shape = _geo.Rect(
            left=pd1_polybb.left, bottom=chbitngate_polybb.bottom,
            right=chbitngate_polybb.right, top=(chbitngate_polybb.bottom + poly.min_width),
        )
        layouter.add_wire(net=nets.bit_n, wire=poly, shape=shape)

        shape = _geo.Rect.from_rect(rect=chbitngate2_m1bb, bottom=chbitnnimpl2_m1bb.bottom)
        layouter.add_wire(net=nets.bit_n, wire=metal1, shape=shape)

        x_chbitgate = x_pg2
        y_chbitgate = y_chbitpimpl

        chbitgate_lay = layouter.place(_chbitgate_lay, x=x_chbitgate, y=y_chbitgate)
        chbitgate_polybb = chbitgate_lay.bounds(mask=poly.mask)
        chbitgate_m1bb = chbitgate_lay.bounds(mask=metal1.mask)

        shape = _geo.Rect.from_rect(rect=chbitgate_polybb, top=pu2_polybb.top)
        layouter.add_wire(net=nets.bit, wire=poly, shape=shape)
        shape = _geo.Rect.from_rect(rect=pu2_polybb, left=chbitgate_polybb.left)
        layouter.add_wire(net=nets.bit, wire=poly, shape=shape)

        shape = _geo.Rect.from_rect(rect=chbitpimpl_m1bb, right=chbitgate_m1bb.right)
        layouter.add_wire(net=nets.bit, wire=metal1, shape=shape)
        shape = _geo.Rect.from_rect(rect=chbitgate_m1bb, bottom=chbitnimpl2_m1bb.bottom)
        layouter.add_wire(net=nets.bit, wire=metal1, shape=shape)

        # bulk/well contacts
        idx = active.implant.index(pimplant)
        h = min(
            2*(y_pd + _pd1_polybb.bottom - cache.min_actpoly_space),
            2*(pd1_actbb.bottom - cache.min_nactpact_space),
        )
        w = min(
            2*(x_pg1 + _pg1_polybb.left - cache.min_actpoly_space),
            2*(pg1_actbb.left - cache.min_nactpact_space),
        )
        chvsspwell1_lay = layouter.add_wire(
            net=nets.vss, wire=contact, well_net=pwell_net, x=0.0, y=0.0,
            bottom=active, bottom_implant=pimplant, bottom_well=pwell,
            bottom_enclosure="tall", bottom_width=w, bottom_height=h,
        )
        chvsspwell1_actbb = chvsspwell1_lay.bounds(mask=active.mask)
        self._vss_tapbb = chvsspwell1_actbb
        chvsspwell1_m1bb = chvsspwell1_lay.bounds(mask=metal1.mask)
        layouter.add_wire(
            net=nets.vss, wire=contact, well_net=pwell_net, x=cell_width, y=0.0,
            bottom=active, bottom_implant=pimplant, bottom_well=pwell,
            bottom_enclosure="tall", bottom_width=w, bottom_height=h,
        )
        # Connect chvsspd1 to chvsspwell1
        shape = _geo.Rect.from_rect(rect=chvsspwell1_m1bb, top=cell_height)
        layouter.add_wire(net=nets.vss, wire=metal1, shape=shape)
        shape = _geo.Rect.from_rect(
            rect=shape, left=(cell_width - shape.right), right=(cell_width - shape.left),
        )
        layouter.add_wire(net=nets.vss, wire=metal1, shape=shape)

        left = pu1_actbb.right + cache.min_nactpact_space
        right = chbitgate_polybb.left - cache.min_actpoly_space
        layouter.add_wire(
            net=nets.vdd, wire=contact, well_net=nwell_net, y=y_chvddnwell,
            bottom=active, bottom_implant=nimplant, bottom_well=nwell,
            bottom_left=left, bottom_right=right, bottom_enclosure="wide",
            top_enclosure="wide",
        )

        # vdd m2/m3
        x_via1vdd = x_chwl1
        y_via1vdd = cell_height
        layouter.add_wire(
            net=nets.vdd, wire=via1, x=x_via1vdd, y=y_via1vdd,
            bottom_enclosure="wide", top_enclosure="tall",
        )
        via2vdd_lay = layouter.add_wire(
            net=nets.vdd, wire=via2, x=x_via1vdd, y=y_via1vdd, rows=2,
            bottom_enclosure="tall", top_enclosure="wide",
        )
        via2vdd_m3bb = via2vdd_lay.bounds(mask=metal3.mask)

        shape = _geo.Rect.from_rect(
            rect=via2vdd_m3bb, left=0.0, right=cell_width,
        )
        layouter.add_wire(net=nets.vdd, wire=metal3, pin=metal3pin, shape=shape)
        self._vdd_bottom = shape.bottom
        self._vdd_top = shape.top

        # vss m2/m3
        _via2vss_lay = layouter.wire_layout(
            net=nets.vss, wire=via2, rows=2, bottom_enclosure="tall", top_enclosure="wide",
        )
        _via2vss_m3bb = _via2vss_lay.bounds(mask=metal3.mask)
        y_via2vss = via2vdd_m3bb.bottom - metal3.min_space - _via2vss_m3bb.top
        via2vss1_lay = layouter.place(_via2vss_lay, x=0.0, y=y_via2vss)
        via2vss1_m3bb = via2vss1_lay.bounds(mask=metal3.mask)
        via2vss2_lay = layouter.place(_via2vss_lay, x=cell_width, y=y_via2vss)
        via2vss2_m3bb = via2vss2_lay.bounds(mask=metal3.mask)

        shape = _geo.Rect.from_rect(rect=via2vss1_m3bb, right=via2vss2_m3bb.right)
        layouter.add_wire(net=nets.vss, wire=metal3, pin=metal3pin, shape=shape)
        self._vss_bottom = shape.bottom
        self._vss_top = shape.top

        y_via1vss = via2vss1_m3bb.bottom
        layouter.add_wire(
            net=nets.vss, wire=via1, x=0.0, y=y_via1vss, rows=2,
            bottom_enclosure="tall", top_enclosure="tall",
        )
        layouter.add_wire(
            net=nets.vss, wire=via1, x=cell_width, y=y_via1vss, rows=2,
            bottom_enclosure="tall", top_enclosure="tall",
        )

        # Fill up wells
        if nwell is not None:
            chbitpimpl_nwbb = chbitpimpl_lay.bounds(mask=nwell.mask)
            chvddpu1_nwbb = chvddpu1_lay.bounds(mask=nwell.mask)

            shape = _geo.Rect(
                left=0.0, bottom=chbitpimpl_nwbb.bottom,
                right=cell_width, top=chvddpu1_nwbb.top,
            )
            layouter.add_wire(net=nets.vdd, wire=nwell, shape=shape)
        if pwell is not None:
            pd1_pwbb = pd1_lay.bounds(mask=pwell.mask)
            chvsspwell1_pwbb = chvsspwell1_lay.bounds(mask=pwell.mask)

            shape = _geo.Rect(
                left=0.0, bottom=chvsspwell1_pwbb.bottom,
                right=cell_width, top=pd1_pwbb.top,
            )
            layouter.add_wire(net=nets.vss, wire=pwell, shape=shape)

        # boundary
        self.set_size(width=cell_width, height=cell_height)


class _DP8TColumn(_Column["DP8TFactory"]):
    def __init__(self, *,
        rows: int, bits: int, colmux: int,
        fab: "DP8TFactory", name: str,
    ):
        super().__init__(rows=rows, bits=bits, colmux=colmux, fab=fab, name=name)

        cache = fab._cache
        m2pin = cache.metalpin(2)
        m3pin = cache.metalpin(3)

        self.ctrl_signals = (
            ("vss", m3pin), ("vdd", m3pin),
            ("clk1", m2pin), ("clk2", m2pin),
            ("precharge1_n", m3pin), ("precharge2_n", m3pin),
            ("we_en1", m2pin), ("we_en2", m2pin),
        )
        self.row_signals = (("wl1", m3pin), ("wl2", m3pin))
        self.col_signals = (("mux1", m3pin), ("mux2", m3pin),)
        self.bit_signals = (
            ("q1", m3pin), ("q2", m3pin),
            ("d1", m3pin), ("d2", m3pin),
        )
        self.we_signals = (("we1", m3pin), ("we2", m3pin))

    def _create_circuit(self) -> None:
        fab = self.fab

        columns = self.bits*self.colmux

        ckt = self.new_circuit()

        array_cell = fab.bitarray(rows=self.rows, columns=columns)
        array = ckt.instantiate(array_cell, name="array")

        periph1_cell = fab.columnperiphery(
            bits=self.bits, colmux=self.colmux, bl=1,
        )
        periph1 = ckt.instantiate(periph1_cell, name="periph1")
        periph2_cell = fab.columnperiphery(
            bits=self.bits, colmux=self.colmux, bl=2,
        )
        periph2 = ckt.instantiate(periph2_cell, name="periph2")

        ckt.new_net(name="vss", external=True, childports=(
            array.ports.vss, periph1.ports.vss, periph2.ports.vss
        ))
        ckt.new_net(name="vdd", external=True, childports=(
            array.ports.vdd, periph1.ports.vdd, periph2.ports.vdd,
        ))

        for row in range(self.rows):
            for sig in ("wl1", "wl2"):
                net_name = f"{sig}[{row}]"
                ckt.new_net(name=net_name, external=True, childports=array.ports[net_name])

        for bit in range(self.bits):
            port_name = f"q[{bit}]"
            net_name = f"q1[{bit}]"
            ckt.new_net(name=net_name, external=True, childports=periph1.ports[port_name])
            net_name = f"q2[{bit}]"
            ckt.new_net(name=net_name, external=True, childports=periph2.ports[port_name])

            port_name = f"d[{bit}]"
            net_name = f"d1[{bit}]"
            ckt.new_net(name=net_name, external=True, childports=periph1.ports[port_name])
            net_name = f"d2[{bit}]"
            ckt.new_net(name=net_name, external=True, childports=periph2.ports[port_name])

        ckt.new_net(name="we1", external=True, childports=periph1.ports.we)
        ckt.new_net(name="clk1", external=True, childports=periph1.ports.clk)
        ckt.new_net(name="we_en1", external=True, childports=periph1.ports.we_en)
        ckt.new_net(name="precharge1_n", external=True, childports=periph1.ports.precharge_n)

        ckt.new_net(name="we2", external=True, childports=periph2.ports.we)
        ckt.new_net(name="clk2", external=True, childports=periph2.ports.clk)
        ckt.new_net(name="we_en2", external=True, childports=periph2.ports.we_en)
        ckt.new_net(name="precharge2_n", external=True, childports=periph2.ports.precharge_n)

        for col in range(self.colmux):
            port_name = f"mux[{col}]"
            net_name = f"mux1[{col}]"
            ckt.new_net(name=net_name, external=True, childports=periph1.ports[port_name])
            net_name = f"mux2[{col}]"
            ckt.new_net(name=net_name, external=True, childports=periph2.ports[port_name])

        for column in range(columns):
            port_name = f"bl[{column}]"
            net_name = f"bl1[{column}]"
            ckt.new_net(name=net_name, external=False, childports=(
                array.ports[net_name], periph1.ports[port_name],
            ))
            net_name = f"bl2[{column}]"
            ckt.new_net(name=net_name, external=False, childports=(
                array.ports[net_name], periph2.ports[port_name],
            ))

            port_name = f"bl_n[{column}]" 
            net_name = f"bl1_n[{column}]"
            ckt.new_net(name=net_name, external=False, childports=(
                array.ports[net_name], periph1.ports[port_name],
            ))
            net_name = f"bl2_n[{column}]"
            ckt.new_net(name=net_name, external=False, childports=(
                array.ports[net_name], periph2.ports[port_name],
            ))

    def _create_layout(self) -> None:
        fab = self.fab
        cache = fab._cache

        columns = self.bits*self.colmux
        cell_width = columns*cache.bit_width

        nets = self.circuit.nets
        insts = self.circuit.instances

        metal2 = cache.metal(2)
        metal2pin = cache.metalpin(2)
        metal3 = cache.metal(3)
        metal3pin = cache.metalpin(3)

        layouter = self.new_circuitlayouter()
        layout = layouter.layout

        _array_lay = layouter.inst_layout(inst=insts.array)
        _array_bb = _array_lay.boundary
        assert _array_bb is not None

        _periph1_lay = layouter.inst_layout(inst=insts.periph1)
        _periph1_bb = _periph1_lay.boundary
        assert _periph1_bb is not None

        _periph2_lay = layouter.inst_layout(inst=insts.periph2, rotation=_geo.Rotation.MX)
        _periph2_bb = _periph2_lay.boundary
        assert _periph2_bb is not None

        y_periph1 = -_periph1_bb.bottom
        periph1_lay = layouter.place(_periph1_lay, x=0.0, y=y_periph1)
        periph1_bb = periph1_lay.boundary
        assert periph1_bb is not None

        y_array = periph1_bb.top - _array_bb.bottom
        array_lay = layouter.place(_array_lay, x=0.0, y=y_array)
        array_bb = array_lay.boundary
        assert array_bb is not None

        y_periph2 = array_bb.top - _periph2_bb.bottom
        periph2_lay = layouter.place(_periph2_lay, x=0.0, y=y_periph2)
        periph2_bb = periph2_lay.boundary
        assert periph2_bb is not None

        cell_height = periph2_bb.top

        m2pin_nets = ("clk1", "clk2", "we_en1", "we_en2")
        for m2pin_net in m2pin_nets:
            net = nets[m2pin_net]
            for m2pinms in layout.filter_polygons(
                net=net, mask=metal2pin.mask, depth=1,
            ):
                layouter.add_wire(net=net, wire=metal2, pin=metal2pin, shape=m2pinms.shape)

        m3pin_nets = (
            "vss", "vdd", "precharge1_n", "precharge2_n", "we1", "we2",
            *(f"wl1[{row}]" for row in range(self.rows)),
            *(f"wl2[{row}]" for row in range(self.rows)),
            *(f"mux1[{col}]" for col in range(self.colmux)),
            *(f"mux2[{col}]" for col in range(self.colmux)),
            *(f"q1[{bit}]" for bit in range(self.bits)),
            *(f"q2[{bit}]" for bit in range(self.bits)),
            *(f"d1[{bit}]" for bit in range(self.bits)),
            *(f"d2[{bit}]" for bit in range(self.bits)),
        )
        for m3pin_net in m3pin_nets:
            net = nets[m3pin_net]
            for m3pinms in layout.filter_polygons(
                net=net, mask=metal3pin.mask, depth=1,
            ):
                layouter.add_wire(net=net, wire=metal3, pin=metal3pin, shape=m3pinms.shape)

        # boundary
        self.set_size(width=cell_width, height=cell_height)


class _DP8TBlock(_DP8TFactoryCell):
    def __init__(self, *,
        address_groups: Tuple[int, ...], word_size: int, we_size: int,
        fab: "DP8TFactory", name: str,
    ):
        super().__init__(fab=fab, name=name)
        if (word_size%we_size) != 0:
            raise ValueError(
                f"word_size {word_size} is not a multiple of we_szie {we_size}"
            )
        if address_groups != (3, 4, 2):
            raise NotImplementedError(f"address_grpups {address_groups} != (3, 4, 2")
        if word_size//we_size != 8:
            raise NotImplementedError(
                f"word bits per we bit != 8 but {word_size//we_size}"
            )
        self._address_groups = address_groups
        self._word_size = word_size
        self._we_size = we_size

        self._colmux_bits = colmux_bits = address_groups[-1]
        pd0_bits = address_groups[0]
        pd1_bits = pd1_bits = address_groups[1]
        self._a_bits = a_bits = colmux_bits + pd0_bits + pd1_bits
        self._words = 2**a_bits

    @property
    def address_groups(self) -> Tuple[int, ...]:
        return self._address_groups
    @property
    def words(self) -> int:
        return self._words
    @property
    def word_size(self) -> int:
        return self._word_size
    @property
    def we_size(self) -> int:
        return self._we_size
    @property
    def a_bits(self) -> int:
        return self._a_bits

    def _create_circuit(self):
        fab = self.fab

        ckt = self.new_circuit()

        assert self.words == 512, "Internal error"
        colmux_bits = self._colmux_bits
        colmux_lines = 2**colmux_bits
        a_bits = self._a_bits

        rows = self.words//(2**colmux_bits)

        rowperiph1_cell = fab.rowperiphery(
            address_groups=self.address_groups,
            colperiph_kwargs={"bits": self.word_size//self.we_size},
            port=1,
        )
        rowperiph2_cell = fab.rowperiphery(
            address_groups=self.address_groups,
            colperiph_kwargs={"bits": self.word_size//self.we_size},
            port=2,
        )
        columnblock_cell = fab.columnblock(
            rows=rows, bits=self.word_size, colmux=colmux_lines, webits=self.we_size,
        )

        rowperiph1 = ckt.instantiate(rowperiph1_cell, name="rowperiph1")
        rowperiph2 = ckt.instantiate(rowperiph2_cell, name="rowperiph2")
        columnblock = ckt.instantiate(columnblock_cell, name=f"columnblock")

        ckt.new_net(name="clk1", external=True, childports=rowperiph1.ports.clk)
        ckt.new_net(name="clk2", external=True, childports=rowperiph2.ports.clk)

        for a_bit in range(a_bits):
            periphnet_name = f"a[{a_bit}]"
            net_name = f"a1[{a_bit}]"
            ckt.new_net(
                name=net_name, external=True, childports=rowperiph1.ports[periphnet_name]
            )
            net_name = f"a2[{a_bit}]"
            ckt.new_net(
                name=net_name, external=True, childports=rowperiph2.ports[periphnet_name]
            )

        for sig_name, _ in columnblock_cell.signals:
            net_name = sig_name
            if sig_name in ("vss", "vdd"):
                external = True
                extra_ports = tuple(inst.ports[net_name] for inst in ckt.instances)
            elif sig_name == "clk1":
                external = False
                net_name = "columnclk1"
                extra_ports = (rowperiph1.ports.columnclk,)
            elif sig_name == "clk2":
                external = False
                net_name = "columnclk2"
                extra_ports = (rowperiph2.ports.columnclk,)
            elif (
                sig_name in ("precharge1_n", "we_en1")
                or sig_name.startswith(("mux1[", "wl1["))
            ):
                idx = sig_name.index("1")
                port_name = sig_name[:idx] + sig_name[idx+1:]
                external = False
                extra_ports = (rowperiph1.ports[port_name],)
            elif (
                sig_name in ("precharge2_n", "we_en2")
                or sig_name.startswith(("mux2[", "wl2["))
            ):
                idx = sig_name.index("2")
                port_name = sig_name[:idx] + sig_name[idx+1:]
                external = False
                extra_ports = (rowperiph2.ports[port_name],)
            elif sig_name.startswith((
                    "d1[", "q1[", "we1[", "d2[", "q2[", "we2[",
                )):
                external = True
                extra_ports = tuple()
            else:
                assert False, f"Internal error: unhandled sig_name '{sig_name}'"
            ckt.new_net(
                name=net_name, external=external,
                childports=(columnblock.ports[sig_name], *extra_ports),
            )

    def _create_layout(self):
        fab = self.fab
        cache = fab._cache

        ckt = self.circuit
        nets = ckt.nets
        insts = ckt.instances

        metal2 = cache.metal(2)
        metal2pin = cache.metalpin(2)
        metal3 = cache.metal(3)
        metal3pin = cache.metalpin(3)

        a_bits = self._a_bits

        layouter = self.new_circuitlayouter()
        layout = layouter.layout

        _rowperiph1_lay = layouter.inst_layout(inst=insts.rowperiph1)
        _rowperiph1_bb = _rowperiph1_lay.boundary
        assert _rowperiph1_bb is not None

        _rowperiph2_lay = layouter.inst_layout(
            inst=insts.rowperiph2, rotation=_geo.Rotation.R180,
        )
        _rowperiph2_bb = _rowperiph2_lay.boundary
        assert _rowperiph2_bb is not None

        _columnblock_lay = layouter.inst_layout(inst=insts.columnblock)
        _columnblock_bb = _columnblock_lay.boundary
        assert _columnblock_bb is not None

        x_rowperiph1 = -_rowperiph1_bb.left
        y_rowperiph1 = -_rowperiph1_bb.bottom
        rowperiph1_lay = layouter.place(
            _rowperiph1_lay, x=x_rowperiph1, y=y_rowperiph1,
        )
        rowperiph1_bb = rowperiph1_lay.boundary
        assert rowperiph1_bb is not None

        x_columnblock = rowperiph1_bb.right - _columnblock_bb.left
        y_columnblock = -_columnblock_bb.bottom
        columnblock_lay = layouter.place(
            _columnblock_lay, x=x_columnblock, y=y_columnblock,
        )
        columnblock_bb = columnblock_lay.boundary
        assert columnblock_bb is not None

        cell_height = columnblock_bb.top

        x_rowperiph2 = columnblock_bb.right - _rowperiph2_bb.left
        y_rowperiph2 = cell_height - _rowperiph2_bb.top
        rowperiph2_lay = layouter.place(
            _rowperiph2_lay, x=x_rowperiph2, y=y_rowperiph2,
        )
        rowperiph2_bb = rowperiph2_lay.boundary
        assert rowperiph2_bb is not None

        cell_width = rowperiph2_bb.right

        # vss/vdd
        # extend the stripes of the first column of the whole width
        for net in (nets.vss, nets.vdd):
            for m3pinms in columnblock_lay.filter_polygons(
                net=net, mask=metal3pin.mask, depth=1, split=True,
            ):
                shape = m3pinms.shape
                layouter.add_wire(net=net, wire=metal3, pin=metal3pin, shape=shape)

        # a
        # on m1pin for coldec, on m2pin for rowdec
        for a_bit in range(a_bits):
            net = nets[f"a1[{a_bit}]"]
            m2pinbb = rowperiph1_lay.bounds(mask=metal2pin.mask, net=net, depth=1)
            layouter.add_wire(net=net, wire=metal2, pin=metal2pin, shape=m2pinbb)
            net = nets[f"a2[{a_bit}]"]
            m2pinbb = rowperiph2_lay.bounds(mask=metal2pin.mask, net=net, depth=1)
            layouter.add_wire(net=net, wire=metal2, pin=metal2pin, shape=m2pinbb)

        # clk
        m3pinbb = rowperiph1_lay.bounds(mask=metal3pin.mask, net=nets.clk1, depth=1)
        layouter.add_wire(net=nets.clk1, wire=metal3, pin=metal3pin, shape=m3pinbb)
        m3pinbb = rowperiph2_lay.bounds(mask=metal3pin.mask, net=nets.clk2, depth=1)
        layouter.add_wire(net=nets.clk2, wire=metal3, pin=metal3pin, shape=m3pinbb)

        # Signal connected by abutment:
        # - wl[]
        # - precharge_n
        # - mux[]
        # - we_en
        # - columnclk connected by abutoment

        # d[n]/q[n]/we[m]
        m3pinnets = (
            *(f"q1[{bit}]" for bit in range(self.word_size)),
            *(f"q2[{bit}]" for bit in range(self.word_size)),
            *(f"d1[{bit}]" for bit in range(self.word_size)),
            *(f"d2[{bit}]" for bit in range(self.word_size)),
            *(f"we1[{we}]" for we in range(self.we_size)),
            *(f"we2[{we}]" for we in range(self.we_size)),
        )
        for m3pinnet in m3pinnets:
            net = nets[m3pinnet]
            m3pinbb = layout.bounds(mask=metal3pin.mask, net=net, depth=1)
            layouter.add_wire(net=net, wire=metal3, pin=metal3pin, shape=m3pinbb)

        # boundary
        self.set_size(width=cell_width, height=cell_height)


class DP8TFactory(_SRAMFactory):
    def __init__(self, *, lib: _lbry.Library, spec: DP8TSpecification) -> None:
        self._lib = lib
        self._spec = spec
        self._cache = _TechCache(fab=self, spec=spec)

    @property
    def lib(self) -> _lbry.Library:
        return self._lib
    @property
    def spec(self) -> DP8TSpecification:
        return self._spec

    def bitcell(self) -> _DP8TCell:
        return self._get_cell(cell_name="Cell", cls=_DP8TCell, cls_args={})

    def wordlinedriver(self, *, wl: int) -> _WordlineDriver:
        if wl not in (1, 2):
            raise ValueError("wl has to be 1 or 2")

        b = self.bitcell()
        wl_bottom = b.wl1_bottom if wl == 1 else b.wl2_bottom
        wl_top = b.wl1_top if wl == 1 else b.wl2_top
        return super().wordlinedriver(
            name_suffix=f"_wl{wl}", wl_bottom=wl_bottom, wl_top=wl_top,
        )

    def rowdecoderdrivepage(self, *,
        pds: int, rows: int, wl: int,
    ) -> _RowDecoderDrivePage:
        return super().rowdecoderdrivepage(
            pds=pds, rows=rows,
            wldriver_kwargs={"wl": wl}, name_suffix=f"_wl{wl}",
        )

    def rowdecoder(self, *,
        address_groups: Iterable[int], reverse: bool, wl: int,
    ) -> _RowDecoder:
        return super().rowdecoder(
            address_groups=address_groups, reverse=reverse,
            page_kwargs={"wl": wl}, name_suffix=f"_wl{wl}",
        )

    def rowperiphery(self, *,
        address_groups: Iterable[int], colperiph_kwargs: Dict[str, Any],
        port: int,
    ) -> _RowPeriphery:
        assert port in (1, 2)
        assert "bl" not in colperiph_kwargs
        colperiph_kwargs["bl"] = port
        return super().rowperiphery(
            address_groups=address_groups, colperiph_kwargs=colperiph_kwargs,
            rowdec_kwargs={"wl": port, "reverse": port != 1}, name_suffix=f"_wl{port}",
        )

    def precharge(self, *, bl: int) -> _Precharge:
        if bl not in (1, 2):
            raise ValueError("bl has to be 1 or 2")

        b = self.bitcell()
        bl_left = b.bl1_left if bl == 1 else b.bl2_left
        bl_right = b.bl1_right if bl == 1 else b.bl2_right
        bln_left = b.bl1n_left if bl == 1 else b.bl2n_left
        bln_right = b.bl1n_right if bl == 1 else b.bl2n_right
        return super().precharge(
            bl_left=bl_left, bl_right=bl_right,
            bln_left=bln_left, bln_right=bln_right,
            name_suffix=f"_bl{bl}",
        )

    def colmux(self, *, columns: int, bl: int) -> _ColMux:
        if bl not in (1, 2):
            raise ValueError("bl has to be 1 or 2")

        b = self.bitcell()
        bl_left = b.bl1_left if bl == 1 else b.bl2_left
        bl_right = b.bl1_right if bl == 1 else b.bl2_right
        bln_left = b.bl1n_left if bl == 1 else b.bl2n_left
        bln_right = b.bl1n_right if bl == 1 else b.bl2n_right
        return super().colmux(
            columns=columns,
            bl_left=bl_left, bl_right=bl_right,
            bln_left=bln_left, bln_right=bln_right,
            name_suffix=f"_bl{bl}",
        )

    def columnperiphery(self, *,
        bits: int, colmux: int, bl: int,
    ) -> _ColumnPeriphery:
        bl_kwargs = {"bl": bl}
        return super().columnperiphery(
            bits=bits, colmux=colmux, precharge_kwargs=bl_kwargs, colmux_kwargs=bl_kwargs,
            name_suffix=f"_bl{bl}",
        )

    def column(self, *,
        rows: int, bits: int, colmux: int,
    ) -> _DP8TColumn:
        return self._get_cell(
            cell_name=f"Column_{rows}R{bits}B{colmux}M",
            cls=_DP8TColumn, cls_args={"rows": rows, "bits": bits, "colmux": colmux},
        )

    def block(self, *,
        address_groups: Iterable[int], word_size: int, we_size: int,
        cell_name: Optional[str]=None,
    ):
        address_groups = tuple(address_groups)
        if cell_name is None:
            address_str = "-".join(str(bits) for bits in address_groups)
            cell_name = f"Block_{address_str}x{word_size}_{we_size}WE"
        return self._get_cell(
            cell_name=cell_name, cls=_DP8TBlock, cls_args={
                "address_groups": address_groups,
                "word_size": word_size, "we_size": we_size,
            }
        )
