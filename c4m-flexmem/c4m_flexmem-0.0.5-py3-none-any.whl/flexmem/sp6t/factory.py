# SPDX-License-Identifier: GPL-2.0-or-later OR AGPL-3.0-or-later OR CERN-OHL-S-2.0+
from math import floor
from typing import Any, List, Tuple, Dict, Iterable, Optional, cast

from pdkmaster.technology import (
    property_ as _prp, geometry as _geo, primitive as _prm,
)
from pdkmaster.design import circuit as _ckt, layout as _lay, library as _lbry

from ..common import (
    _ispow2, _SRAMSpecification, _SRAMFactory, _FactoryCell,
    _BitCell, _WordlineDriver, _RowDecoderDrivePage, _RowDecoder, _RowPeriphery,
    _Precharge, _ColMux, _ColumnPeriphery, _Column,
)


__all__ = ["SP6TSpecification", "SP6TFactory"]


class SP6TSpecification(_SRAMSpecification):
    def __init__(self, *,
        name_prefix: str="SP6T",
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

class _SP6TFactoryCell(_FactoryCell["SP6TFactory"]):
    pass


class _SP6TCell(_BitCell["SP6TFactory"]):
    def __init__(self, *, fab: "SP6TFactory", name: str):
        cache = fab._cache
        m2pin = cache.metalpin(2)
        m3pin = cache.metalpin(3)

        self.dc_signals = (("vss", m3pin), ("vdd", m3pin))
        self.wl_signals = (("wl", m3pin),)
        self.bl_signals = (("bl", m2pin),)

        super().__init__(fab=fab, name=name)

        self._wl_bottom: Optional[float] = None
        self._wl_top: Optional[float] = None
        self._bl_left: Optional[float] = None
        self._bl_right: Optional[float] = None
        self._bln_left: Optional[float] = None
        self._bln_right: Optional[float] = None

    @property
    def wl_bottom(self) -> float:
        if self._wl_bottom is None:
            self.layout # Generate layout
            assert self._wl_bottom is not None
        return self._wl_bottom
    @property
    def wl_top(self) -> float:
        if self._wl_top is None:
            self.layout # Generate layout
            assert self._wl_top is not None
        return self._wl_top
    @property
    def bl_left(self) -> float:
        if self._bl_left is None:
            self.layout # Generate layout
            assert self._bl_left is not None
        return self._bl_left
    @property
    def bl_right(self) -> float:
        if self._bl_right is None:
            self.layout # Generate layout
            assert self._bl_right is not None
        return self._bl_right
    @property
    def bln_left(self) -> float:
        if self._bln_left is None:
            self.layout # Generate layout
            assert self._bln_left is not None
        return self._bln_left
    @property
    def bln_right(self) -> float:
        if self._bln_right is None:
            self.layout # Generate layout
            assert self._bln_right is not None
        return self._bln_right

    def _create_circuit(self):
        fab = self.fab
        spec = fab.spec

        ckt = self.new_circuit()

        pu1 = ckt.instantiate(spec.pmos, name="pu1", l=spec.pu_l, w=spec.pu_w)
        pu2 = ckt.instantiate(spec.pmos, name="pu2", l=spec.pu_l, w=spec.pu_w)

        pd1 = ckt.instantiate(spec.nmos, name="pd1", l=spec.pd_l, w=spec.pd_w)
        pd2 = ckt.instantiate(spec.nmos, name="pd2", l=spec.pd_l, w=spec.pd_w)

        pg1 = ckt.instantiate(spec.nmos, name="pg1", l=spec.pg_l, w=spec.pg_w)
        pg2 = ckt.instantiate(spec.nmos, name="pg2", l=spec.pg_l, w=spec.pg_w)

        ckt.new_net(name="vdd", external=True, childports=(
            pu1.ports.sourcedrain1, pu1.ports.bulk,
            pu2.ports.sourcedrain2, pu2.ports.bulk,
        ))
        ckt.new_net(name="vss", external=True, childports=(
            pd1.ports.sourcedrain1, pd1.ports.bulk,
            pd2.ports.sourcedrain2, pd2.ports.bulk,
            pg1.ports.bulk, pg2.ports.bulk,
        ))

        ckt.new_net(name="wl", external=True, childports=(
            pg1.ports.gate, pg2.ports.gate,
        ))
        ckt.new_net(name="bl", external=True, childports=(
            pg1.ports.sourcedrain1,
        ))
        ckt.new_net(name="bl_n", external=True, childports=(
            pg2.ports.sourcedrain1,
        ))

        ckt.new_net(name="bit", external=False, childports=(
            pg1.ports.sourcedrain2,
            pd1.ports.sourcedrain2, pu1.ports.sourcedrain2,
            pd2.ports.gate, pu2.ports.gate,
        ))
        ckt.new_net(name="bit_n", external=False, childports=(
            pg2.ports.sourcedrain2,
            pd2.ports.sourcedrain1, pu2.ports.sourcedrain1,
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
        poly = cache.poly
        contact = cache.contact
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
        _pu1_lay = layouter.inst_layout(inst=insts.pu1)
        _pu2_lay = layouter.inst_layout(inst=insts.pu2)

        _pd1_lay = layouter.inst_layout(inst=insts.pd1)
        _pd2_lay = layouter.inst_layout(inst=insts.pd2)

        _pg1_lay = layouter.inst_layout(inst=insts.pg1, rotation=_geo.Rotation.R90)
        _pg2_lay = layouter.inst_layout(inst=insts.pg2, rotation=_geo.Rotation.R90)

        _chbl_lay = layouter.wire_layout(
            net=nets.bl, wire=contact, well_net=pwell_net,
            bottom=active, bottom_implant=nimplant, bottom_well=pwell,
            bottom_width=spec.pg_w, bottom_enclosure=chact_enc_min,
            top_enclosure="tall"
        )
        _chbln_lay = layouter.wire_layout(
            net=nets.bl_n, wire=contact, well_net=pwell_net,
            bottom=active, bottom_implant=nimplant, bottom_well=pwell,
            bottom_width=spec.pg_w, bottom_enclosure=chact_enc_min,
            top_enclosure="tall",
        )

        _chvsspd1_lay = layouter.wire_layout(
            net=nets.vss, wire=contact, well_net=pwell_net,
            bottom=active, bottom_implant=nimplant, bottom_well=pwell,
            bottom_height=spec.pd_w, bottom_enclosure=chact_enc_min,
            top_enclosure="tall",
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
            bottom_height=spec.pu_w, bottom_enclosure=chact_enc_min,
            top_enclosure="tall",
        )
        _chvddpu2_lay = layouter.wire_layout(
            net=nets.vdd, wire=contact, well_net=nwell_net,
            bottom=active, bottom_implant=pimplant, bottom_well=nwell,
            bottom_height=spec.pu_w, bottom_enclosure=chact_enc_min,
            top_enclosure="tall",
        )

        net = nets.bit
        _chbitnimpl_lay = layouter.wire_layout(
            net=net, wire=contact, well_net=pwell_net,
            bottom=active, bottom_implant=nimplant, bottom_well=pwell,
            bottom_enclosure="wide", top_enclosure="tall",
        )
        _chbitpimpl_lay = layouter.wire_layout(
            net=net, wire=contact, well_net=nwell_net,
            bottom=active, bottom_implant=pimplant, bottom_well=nwell,
            bottom_enclosure="wide", top_enclosure="tall",
        )
        _chbitgate_lay = layouter.wire_layout(
            net=net, wire=contact, bottom=poly, bottom_enclosure="wide",
            top_enclosure="wide",
        )

        net = nets.bit_n
        _chbitnnimpl_lay = layouter.wire_layout(
            net=net, wire=contact, well_net=pwell_net,
            bottom=active, bottom_implant=nimplant, bottom_well=pwell,
            bottom_enclosure="wide", top_enclosure="tall",
        )
        _chbitnpimpl_lay = layouter.wire_layout(
            net=net, wire=contact, well_net=nwell_net,
            bottom=active, bottom_implant=pimplant, bottom_well=nwell,
            bottom_enclosure="wide", top_enclosure="tall",
        )
        _chbitngate_lay = layouter.wire_layout(
            net=net, wire=contact, bottom=poly, bottom_enclosure="wide",
            top_enclosure="wide",
        )

        _chwl_lay = layouter.wire_layout(
            net=nets.wl, wire=contact, bottom=poly, bottom_enclosure="tall",
            top_enclosure="tall",
        )

        # Compute bounding boxes
        _pu1_actbb = _pu1_lay.bounds(mask=active.mask)
        _pu1_polybb = _pu1_lay.bounds(mask=poly.mask)
        _chvddpu1_chbb = _chvddpu1_lay.bounds(mask=contact.mask)

        _pd1_actbb = _pd1_lay.bounds(mask=active.mask)
        _pd1_polybb = _pd1_lay.bounds(mask=poly.mask)
        _chvsspd1_chbb = _chvsspd1_lay.bounds(mask=contact.mask)

        _pg1_actbb = _pg1_lay.bounds(mask=active.mask)
        _pg1_polybb = _pg1_lay.bounds(mask=poly.mask)

        _chbl_chbb = _chbl_lay.bounds(mask=contact.mask)

        _chbitnimpl_actbb = _chbitnimpl_lay.bounds(mask=active.mask)
        _chbitpimpl_actbb = _chbitpimpl_lay.bounds(mask=active.mask)

        _chbitgate_polybb = _chbitgate_lay.bounds(mask=poly.mask)
        _chbitgate_m1bb = _chbitgate_lay.bounds(mask=metal1.mask)

        _chwl_polybb = _chwl_lay.bounds(mask=poly.mask)

        # Put ch_vsspd1/ch_vddpu1/ch_bl contact on the edge
        x_chvsspd1 = x_chvddpu1 = y_chbl = 0.0

        # Place pu1/pd1/pg1 minimum space fron contact
        x_pd1 = (
            x_chvsspd1 + _chvsspd1_chbb.right
            + nmos.computed.min_contactgate_space
            - _pd1_polybb.left
        )
        x_pu1 = (
            x_chvddpu1 + _chvddpu1_chbb.right
            + pmos.computed.min_contactgate_space
            - _pu1_polybb.left
        )
        y_pg = ( # pg1 and pg2 at the same height
            y_chbl + _chbl_chbb.top
            + nmos.computed.min_contactgate_space
            - _pg1_polybb.bottom
        )

        # Compute placement of pd1/pg1 poly at minimum space
        y_pd = y_pg + _pg1_polybb.top + poly.min_space - _pd1_polybb.bottom
        y_chvsspd = y_pd
        x_pg1 = max(
            x_pd1 + _pd1_polybb.right + cache.min_actpoly_space - _pg1_actbb.left,
            (
                0.5*tech.computed.min_width(active, up=True, min_enclosure=True)
                + cache.min_nactpact_space - _pg1_actbb.left
            ),
        )
        x_chbl = x_pg1

        # Compute placement of chwl
        x_chwl = x_pg1 + _pg1_actbb.right + cache.min_actpad_space - _chwl_polybb.left
        y_chwl = y_pg + _pg1_polybb.bottom - _chwl_polybb.bottom

        # Compute placement of pu
        actpupd_space = max(
            cache.min_actpwell_enclosure + cache.min_actnwell_enclosure,
            2*cache.min_actpad_space + _chbitgate_polybb.height + poly.min_space
            + poly.min_width,
        )

        y_pu = y_pd + 0.5*spec.pd_w + actpupd_space + 0.5*spec.pu_w
        y_chvddpu = y_pu

        # Align active chbit(n|p)impl with active of pd1/pg1
        x_chbitnimpl = x_pg1 + _pg1_actbb.right - _chbitnimpl_actbb.right
        y_chbitnimpl = y_pd + _pd1_actbb.top - _chbitnimpl_actbb.top

        x_chbitpimpl = x_chbitnimpl
        y_chbitpimpl = y_pu + _pd1_actbb.bottom - _chbitpimpl_actbb.bottom

        x_chbitgate = min(
            x_chbitnimpl - _chbitgate_m1bb.left,
            x_chwl - 0.5*poly.min_space - _chbitgate_polybb.right,
        )
        y_chbitgate = (
            y_pd + _pd1_actbb.top + cache.min_actpad_space - _chbitgate_polybb.bottom
        )
        y_chbitngate = (
            y_pu + _pu1_actbb.bottom - cache.min_actpad_space - _chbitgate_polybb.top
        )

        # Min contact space for chbitnimpl
        y_chbitnimpl = min(
            y_chbitnimpl,
            y_chbitgate - (contact.width + contact.min_space),
        )

        # Symmetric placement of the transistor in the cell
        cell_width = 2*x_chwl
        x_pg2 = cell_width - x_pg1
        x_pd2 = cell_width - x_pd1
        x_pu2 = cell_width - x_pu1

        x_chbln = cell_width - x_chbl
        x_chvsspd2 = cell_width - x_chvsspd1
        x_chvddpu2 = cell_width - x_chvddpu1
        x_chvsspd2 = cell_width - x_chvsspd1
        x_chbitnnimpl = cell_width - x_chbitnimpl
        x_chbitnpimpl = cell_width - x_chbitpimpl
        x_chbitngate = cell_width - x_chbitgate

        # Place the sublayouts and compute some bounding boxes
        pd1_lay = layouter.place(_pd1_lay, x=x_pd1, y=y_pd)
        pd1_actbb = pd1_lay.bounds(mask=active.mask)
        pd1_polybb = pd1_lay.bounds(mask=poly.mask)
        pd1_nimplbb = pd1_lay.bounds(mask=nimplant.mask)
        pd2_lay = layouter.place(_pd2_lay, x=x_pd2, y=y_pd)

        chvsspd1_lay = layouter.place(_chvsspd1_lay, x=x_chvsspd1, y=y_chvsspd)
        chvsspd1_nimplbb = chvsspd1_lay.bounds(mask=nimplant.mask)
        chvsspd1_m1bb = chvsspd1_lay.bounds(mask=metal1.mask)
        chvsspd2_lay = layouter.place(_chvsspd2_lay, x=x_chvsspd2, y=y_chvsspd)

        pu1_lay = layouter.place(_pu1_lay, x=x_pu1, y=y_pu)
        pu1_actbb = pu1_lay.bounds(mask=active.mask)
        pu1_polybb = pu1_lay.bounds(mask=poly.mask)
        pu1_pimplbb = pu1_lay.bounds(mask=pimplant.mask)
        pu2_lay = layouter.place(_pu2_lay, x=x_pu2, y=y_pu)

        chvddpu1_lay = layouter.place(_chvddpu1_lay, x=x_chvddpu1, y=y_chvddpu)
        chvddpu1_pimplbb = chvddpu1_lay.bounds(mask=pimplant.mask)
        chvddpu1_m1bb = chvddpu1_lay.bounds(mask=metal1.mask)
        chvddpu2_lay = layouter.place(_chvddpu2_lay, x=x_chvddpu2, y=y_chvddpu)

        pg1_lay = layouter.place(_pg1_lay, x=x_pg1, y=y_pg)
        pg1_actbb = pg1_lay.bounds(mask=active.mask)
        pg1_polybb = pg1_lay.bounds(mask=poly.mask)
        pg1_nimplbb = pg1_lay.bounds(mask=nimplant.mask)
        layouter.place(_pg2_lay, x=x_pg2, y=y_pg)

        chbl_lay = layouter.place(_chbl_lay, x=x_chbl, y=y_chbl)
        chbl_nimplbb = chbl_lay.bounds(mask=nimplant.mask)
        chbln_lay = layouter.place(_chbln_lay, x=x_chbln, y=y_chbl)

        chbitnimpl_lay = layouter.place(_chbitnimpl_lay, x=x_chbitnimpl, y=y_chbitnimpl)
        chbitnimpl_m1bb = chbitnimpl_lay.bounds(mask=metal1.mask)
        chbitnnimpl_lay = layouter.place(_chbitnnimpl_lay, x=x_chbitnnimpl, y=y_chbitnimpl)

        chbitpimpl_lay = layouter.place(_chbitpimpl_lay, x=x_chbitpimpl, y=y_chbitpimpl)
        chbitpimpl_actbb = chbitpimpl_lay.bounds(mask=active.mask)
        chbitpimpl_m1bb = chbitpimpl_lay.bounds(mask=metal1.mask)
        chbitnpimpl_lay = layouter.place(_chbitnpimpl_lay, x=x_chbitnpimpl, y=y_chbitpimpl)

        chbitgate_lay = layouter.place(_chbitgate_lay, x=x_chbitgate, y=y_chbitgate)
        chbitgate_polybb = chbitgate_lay.bounds(mask=poly.mask)
        chbitngate_lay = layouter.place(_chbitngate_lay, x=x_chbitngate, y=y_chbitngate)
        chbitngate_polybb = chbitngate_lay.bounds(mask=poly.mask)

        chwl_lay = layouter.place(_chwl_lay, x=x_chwl, y=y_chwl)
        chwl_m1bb = chwl_lay.bounds(mask=metal1.mask)

        # Connect cells up
        if spec.pd_l <= spec.pu_l:
            shape = _geo.Rect.from_rect(rect=pd1_polybb, top=pu1_polybb.bottom)
        else:
            shape = _geo.Rect.from_rect(rect=pu1_polybb, bottom=pd1_polybb.top)
        layouter.add_wire(net=nets.bit_n, wire=poly, shape=shape)
        shape = _geo.Rect.from_rect(
            rect=shape, left=(cell_width - shape.right), right=(cell_width - shape.left),
        )
        layouter.add_wire(net=nets.bit, wire=poly, shape=shape)

        shape = _geo.Rect.from_rect(rect=pg1_actbb, bottom=pg1_actbb.top, top=pd1_actbb.top)
        layouter.add_wire(net=nets.bit, wire=active, implant=nimplant, shape=shape)
        shape = _geo.Rect.from_rect(
            rect=shape, left=(cell_width - shape.right), right=(cell_width - shape.left)
        )
        layouter.add_wire(net=nets.bit_n, wire=active, implant=nimplant, shape=shape)
        if pd1_actbb.right < pg1_actbb.left:
            shape = _geo.Rect.from_rect(
                rect=pd1_actbb, left=pd1_actbb.right, right=pg1_actbb.right,
            )
            layouter.add_wire(net=nets.bit, wire=active, implant=nimplant, shape=shape)
            shape = _geo.Rect.from_rect(
                rect=shape, left=(cell_width - shape.right), right=(cell_width - shape.left)
            )
            layouter.add_wire(net=nets.bit_n, wire=active, implant=nimplant, shape=shape)

        shape = _geo.Rect.from_rect(
            rect=pu1_actbb, left=_pu1_actbb.right, right=chbitpimpl_actbb.right,
        )
        layouter.add_wire(
            net=nets.bit, wire=active, well_net=nwell_net,
            implant=pimplant, well=nwell, shape=shape,
        )
        shape = _geo.Rect.from_rect(
            rect=shape, left=(cell_width - shape.right), right=(cell_width - shape.left)
        )
        layouter.add_wire(
            net=nets.bit_n, wire=active, well_net=nwell_net,
            implant=pimplant, well=nwell, shape=shape,
        )

        shape = _geo.Rect.from_rect(
            rect=pg1_polybb, right=(cell_width - pg1_polybb.left),
        )
        layouter.add_wire(net=nets.wl, wire=poly, shape=shape)

        shape = _geo.Rect.from_rect(rect=chbitnimpl_m1bb, top=chbitpimpl_m1bb.top)
        layouter.add_wire(net=nets.bit, wire=metal1, shape=shape)
        shape = _geo.Rect.from_rect(
            rect=shape, left=(cell_width - shape.right), right=(cell_width - shape.left),
        )
        layouter.add_wire(net=nets.bit_n, wire=metal1, shape=shape)

        shape = _geo.Rect(
            left=x_chbitgate, bottom=chbitgate_polybb.bottom,
            right=x_pd2, top=(chbitgate_polybb.bottom + poly.min_width),
        )
        layouter.add_wire(net=nets.bit, wire=poly, shape=shape)
        shape = _geo.Rect(
            left=x_pd1, bottom=(chbitngate_polybb.top - poly.min_width),
            right=x_chbitngate, top=chbitngate_polybb.top,
        )
        layouter.add_wire(net=nets.bit_n, wire=poly, shape=shape)

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
        chvsspwell_lay = layouter.add_wire(
            net=nets.vss, wire=contact, well_net=pwell_net, x=0.0, y=0.0,
            bottom=active, bottom_implant=pimplant, bottom_well=pwell,
            bottom_enclosure="tall", bottom_width=w, bottom_height=h,
        )
        chvsspwell_actbb = chvsspwell_lay.bounds(mask=active.mask)
        self._vss_tapbb = chvsspwell_actbb
        layouter.add_wire(
            net=nets.vss, wire=contact, well_net=pwell_net, x=cell_width, y=0.0,
            bottom=active, bottom_implant=pimplant, bottom_well=pwell,
            bottom_enclosure="tall", bottom_width=w, bottom_height=h,
        )
        # Connect chvsspd1 to chvsspwell1
        shape = _geo.Rect.from_rect(rect=chvsspd1_m1bb, bottom=0.0)
        layouter.add_wire(net=nets.vss, wire=metal1, shape=shape)
        shape = _geo.Rect.from_rect(
            rect=shape, left=(cell_width - shape.right), right=(cell_width - shape.left),
        )
        layouter.add_wire(net=nets.vss, wire=metal1, shape=shape)

        _chvddnwell_lay = layouter.wire_layout(
            net=nets.vdd, wire=contact, well_net=nwell_net,
            bottom=active, bottom_implant=nimplant, bottom_well=nwell,
            bottom_enclosure="wide", top_enclosure="wide"
        )
        _chvddnwell_actbb = _chvddnwell_lay.bounds(mask=active.mask)
        y_chvddnwell = max(
            pu1_polybb.top + cache.min_actpoly_space - _chvddnwell_actbb.bottom,
            pu1_actbb.top + cache.min_nactpact_space - _chvddnwell_actbb.bottom,
        )
        chvddnwell_lay = layouter.place(_chvddnwell_lay, x=0.0, y=y_chvddnwell)
        layouter.place(_chvddnwell_lay, x=cell_width, y=y_chvddnwell)
        chvddnwell_actbb = chvddnwell_lay.bounds(mask=active.mask)
        chvddnwell_m1bb = chvddnwell_lay.bounds(mask=metal1.mask)

        cell_height = y_chvddnwell

        shape = _geo.Rect.from_rect(
            rect=chvddnwell_actbb, right=(cell_width - chvddnwell_actbb.left),
        )
        layouter.add_wire(
            net=nets.vdd, wire=active, well_net=nwell_net,
            implant=nimplant, well=nwell, shape=shape,
        )
        shape = _geo.Rect.from_rect(
            rect=chvddnwell_m1bb, right=(cell_width - chvddnwell_m1bb.left),
        )
        layouter.add_wire(net=nets.vdd, wire=metal1, shape=shape)
        # Connect chvddpu1 to chvddnwell
        shape = _geo.Rect.from_rect(rect=chvddpu1_m1bb, top=cell_height)
        layouter.add_wire(net=nets.vdd, wire=metal1, shape=shape)
        shape = _geo.Rect.from_rect(
            rect=shape, left=(cell_width - shape.right), right=(cell_width - shape.left),
        )
        layouter.add_wire(net=nets.vdd, wire=metal1, shape=shape)

        # implants/wells
        # implants are extended to avoid the odd rule in Sky130 of min. contact on poly
        # to pimplant spaciong.
        shape = _geo.Rect(
            left=pg1_nimplbb.left, bottom=chbl_nimplbb.bottom,
            right=(cell_width - pg1_nimplbb.left), top=pd1_nimplbb.top,
        )
        layouter.add_portless(prim=nimplant, shape=shape)
        if pd1_nimplbb.left < chvsspd1_nimplbb.left: # Take most left edge
            shape = _geo.Rect.from_rect(
                rect=pd1_nimplbb, top=chbitgate_polybb.top,
                right=(cell_width - pd1_nimplbb.left),
            )
        else:
            shape = _geo.Rect.from_rect(
                rect=chvsspd1_nimplbb, top=chbitgate_polybb.top,
                right=(cell_width - chvsspd1_nimplbb.left),
            )
        layouter.add_portless(prim=nimplant, shape=shape)

        if pu1_pimplbb.left < chvddpu1_pimplbb.left: # Take most left edge
            shape = _geo.Rect.from_rect(
                rect=pu1_pimplbb, right=(cell_width - pu1_pimplbb.left),
                bottom=chbitngate_polybb.bottom,
            )
        else:
            shape = _geo.Rect.from_rect(
                rect=chvddpu1_pimplbb, right=(cell_width - chvddpu1_pimplbb.left),
                bottom=chbitngate_polybb.bottom,
            )
        layouter.add_portless(prim=pimplant, shape=shape)

        if nwell is not None:
            shape = layout.bounds(mask=nwell.mask)
            layouter.add_wire(net=nets.vdd, wire=nwell, shape=shape)

        # M2/M3 pins; bl/bln on M2; wl/vss/vdd on M3
        _via1vss_lay = layouter.wire_layout(
            net=nets.vss, wire=via1, bottom_enclosure="tall", top_enclosure="tall",
        )
        _via2vss_lay = layouter.wire_layout(
            net=nets.vss, wire=via2, bottom_enclosure="tall", top_enclosure="wide",
        )
        _via1vdd_lay = layouter.wire_layout(
            net=nets.vdd, wire=via1, bottom_enclosure="tall", top_enclosure="tall",
        )
        _via2vdd_lay = layouter.wire_layout(
            net=nets.vdd, wire=via2, bottom_enclosure="tall", top_enclosure="wide",
        )
        _via1bl_lay = layouter.wire_layout(
            net=nets.bl, wire=via1, bottom_enclosure="tall", top_enclosure="tall",
        )
        _via1bln_lay = layouter.wire_layout(
            net=nets.bl_n, wire=via1, bottom_enclosure="tall", top_enclosure="tall",
        )
        _via1wl_lay = layouter.wire_layout(
            net=nets.wl, wire=via1, bottom_enclosure="tall", top_enclosure="tall",
        )
        _via1wl_m1bb = _via1wl_lay.bounds(mask=metal1.mask)
        _via2wl_lay = layouter.wire_layout(
            net=nets.wl, wire=via2, bottom_enclosure="tall", top_enclosure="wide",
        )
        _via2wl_m2bb = _via2wl_lay.bounds(mask=metal2.mask)

        layouter.place(_via1vss_lay, x=0.0, y=0.0)
        via2vss_lay = layouter.place(_via2vss_lay, x=0.0, y=0.0)
        via2vss_m3bb = via2vss_lay.bounds(mask=metal3.mask)
        layouter.place(_via1vss_lay, x=cell_width, y=0.0)
        layouter.place(_via2vss_lay, x=cell_width, y=0.0)

        shape = _geo.Rect.from_rect(
            rect=via2vss_m3bb, right=(cell_width - via2vss_m3bb.left)
        )
        layouter.add_wire(net=nets.vss, wire=metal3, pin=metal3pin, shape=shape)
        self._vss_bottom = shape.bottom
        self._vss_top = shape.top

        x_via1wl = x_chwl
        y_via1wl = chwl_m1bb.top - _via1wl_m1bb.bottom
        via1wl_lay = layouter.place(_via1wl_lay, x=x_via1wl, y=y_via1wl)
        via1wl_m2bb = via1wl_lay.bounds(mask=metal2.mask)
        x_via2wl = x_chwl
        y_via2wl = via1wl_m2bb.top - _via2wl_m2bb.bottom
        via2wl_lay = layouter.place(_via2wl_lay, x=x_via2wl, y=y_via2wl)
        via2wl_m3bb = via2wl_lay.bounds(mask=metal3.mask)
        shape = _geo.Rect.from_rect(rect=via2wl_m3bb, left=0.0, right=cell_width)
        layouter.add_wire(net=nets.wl, wire=metal3, pin=metal3pin, shape=shape)
        self._wl_bottom = shape.bottom
        self._wl_top = shape.top

        x_via1bl = tech.on_grid(0.5*x_chwl, rounding="floor")
        x_via1bln = cell_width - x_via1bl
        y_via1bln = y_via1bl = 0.0
        via1bl_lay = layouter.place(_via1bl_lay, x=x_via1bl, y=y_via1bl)
        via1bl_m2bb = via1bl_lay.bounds(mask=metal2.mask)
        layouter.place(_via1bln_lay, x=x_via1bln, y=y_via1bln)
        shape = _geo.Rect.from_rect(rect=via1bl_m2bb, top=cell_height)
        layouter.add_wire(net=nets.bl, wire=metal2, pin=metal2pin, shape=shape)
        self._bl_left = shape.left
        self._bl_right = shape.right
        shape = _geo.Rect.from_rect(
            rect=shape, left=(cell_width - shape.right), right=(cell_width - shape.left),
        )
        layouter.add_wire(net=nets.bl_n, wire=metal2, pin=metal2pin, shape=shape)
        self._bln_left = shape.left
        self._bln_right = shape.right

        layouter.place(_via1vdd_lay, x=0.0, y=cell_height)
        via2vdd_lay = layouter.place(_via2vdd_lay, x=0.0, y=cell_height)
        via2vdd_m3bb = via2vdd_lay.bounds(mask=metal3.mask)
        layouter.place(_via1vdd_lay, x=cell_width, y=cell_height)
        layouter.place(_via2vdd_lay, x=cell_width, y=cell_height)
        shape = _geo.Rect.from_rect(rect=via2vdd_m3bb, right=(cell_width - via2vdd_m3bb.left))
        layouter.add_wire(net=nets.vdd, wire=metal3, pin=metal3pin, shape=shape)
        self._vdd_bottom = shape.bottom
        self._vdd_top = shape.top

        # boundary
        self.set_size(width=cell_width, height=cell_height)


class _SP6TColumn(_Column["SP6TFactory"]):
    def __init__(self, *,
        rows: int, bits: int, colmux: int,
        fab: "SP6TFactory", name: str,
    ):
        super().__init__(rows=rows, bits=bits, colmux=colmux, fab=fab, name=name)

        cache = fab._cache
        m2pin = cache.metalpin(2)
        m3pin = cache.metalpin(3)

        self.ctrl_signals = (
            ("vss", m3pin), ("vdd", m3pin), ("clk", m2pin),
            ("precharge_n", m3pin), ("we_en", m2pin),
        )
        self.row_signals = (("wl", m3pin),)
        self.col_signals = (("mux", m3pin),)
        self.bit_signals = (("q", m3pin), ("d", m3pin))
        self.we_signals = (("we", m3pin),)

    def _create_circuit(self) -> None:
        fab = self.fab

        columns = self.bits*self.colmux

        ckt = self.new_circuit()

        array_cell = fab.bitarray(rows=self.rows, columns=columns)
        array = ckt.instantiate(array_cell, name="array")

        periph_cell = fab.columnperiphery(bits=self.bits, colmux=self.colmux)
        periph = ckt.instantiate(periph_cell, name="periph")

        ckt.new_net(name="vss", external=True, childports=(
            array.ports.vss, periph.ports.vss,
        ))
        ckt.new_net(name="vdd", external=True, childports=(
            array.ports.vdd, periph.ports.vdd,
        ))

        for row in range(self.rows):
            net_name = f"wl[{row}]"
            ckt.new_net(name=net_name, external=True, childports=array.ports[net_name])

        for bit in range(self.bits):
            net_name = f"q[{bit}]"
            ckt.new_net(name=net_name, external=True, childports=periph.ports[net_name])

            net_name = f"d[{bit}]"
            ckt.new_net(name=net_name, external=True, childports=periph.ports[net_name])

        ckt.new_net(name="we", external=True, childports=periph.ports.we)
        ckt.new_net(name="clk", external=True, childports=periph.ports.clk)
        ckt.new_net(name="we_en", external=True, childports=periph.ports.we_en)
        ckt.new_net(name="precharge_n", external=True, childports=periph.ports.precharge_n)

        for col in range(self.colmux):
            net_name = f"mux[{col}]"
            ckt.new_net(name=net_name, external=True, childports=periph.ports[net_name])

        for column in range(columns):
            net_name = f"bl[{column}]"
            ckt.new_net(name=net_name, external=False, childports=(
                array.ports[net_name], periph.ports[net_name],
            ))

            net_name = f"bl_n[{column}]"
            ckt.new_net(name=net_name, external=False, childports=(
                array.ports[net_name], periph.ports[net_name],
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

        array_inst = cast(_ckt._CellInstance, insts.array)
        periph_inst = cast(_ckt._CellInstance, insts.periph)

        _periph_bb = periph_inst.cell.layout.boundary
        assert _periph_bb is not None
        y_periph = -_periph_bb.bottom
        periph_lay = layouter.place(periph_inst, x=0.0, y=y_periph)
        periph_bb = periph_lay.boundary
        assert periph_bb is not None

        y_array = periph_bb.top
        array_lay = layouter.place(array_inst, x=0.0, y=y_array)
        array_bb = array_lay.boundary
        assert array_bb is not None
        cell_height = array_bb.top

        m2pin_nets = (
            "clk", "we_en",
        )
        for m2pin_net in m2pin_nets:
            net = nets[m2pin_net]
            for m2pinms in layout.filter_polygons(
                net=net, mask=metal2pin.mask, depth=1,
            ):
                layouter.add_wire(net=net, wire=metal2, pin=metal2pin, shape=m2pinms.shape)

        m3pin_nets = (
            "vss", "vdd", "precharge_n", "we",
            *(f"wl[{row}]" for row in range(self.rows)),
            *(f"mux[{col}]" for col in range(self.colmux)),
            *(f"q[{bit}]" for bit in range(self.bits)),
            *(f"d[{bit}]" for bit in range(self.bits)),
        )
        for m3pin_net in m3pin_nets:
            net = nets[m3pin_net]
            for m3pinms in layout.filter_polygons(
                net=net, mask=metal3pin.mask, depth=1,
            ):
                layouter.add_wire(net=net, wire=metal3, pin=metal3pin, shape=m3pinms.shape)

        # boundary
        self.set_size(width=cell_width, height=cell_height)


class _SP6TBlock(_SP6TFactoryCell):
    def __init__(self, *,
        address_groups: Tuple[int, ...], word_size: int, we_size: int,
        fab: "SP6TFactory", name: str,
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
        self._pd0_bits = pd0_bits = address_groups[0]
        self._pd1_bits = pd1_bits = address_groups[1]
        self._a_bits = a_bits = colmux_bits + pd0_bits + pd1_bits
        self._words = 2**a_bits

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
        pd0_bits = self._pd0_bits
        pd1_bits = self._pd1_bits
        a_bits = self._a_bits

        rows = self.words//(2**colmux_bits)

        rowperiph_cell = fab.rowperiphery(
            address_groups=(pd0_bits, pd1_bits, colmux_bits),
            colperiph_kwargs={"bits": self.word_size//self.we_size}
        )
        columnblock_cell = fab.columnblock(
            rows=rows, bits=self.word_size, colmux=colmux_lines, webits=self.we_size,
        )

        rowperiph = ckt.instantiate(rowperiph_cell, name="rowperiph")
        columnblock = ckt.instantiate(columnblock_cell, name=f"columnblock")

        ckt.new_net(name="clk", external=True, childports=rowperiph.ports.clk)

        for a_bit in range(a_bits):
            net_name = f"a[{a_bit}]"
            ckt.new_net(
                name=net_name, external=True, childports=rowperiph.ports[net_name]
            )

        for sig_name, _ in columnblock_cell.signals:
            net_name = sig_name
            if sig_name in ("vss", "vdd"):
                external = True
                extra_ports = tuple(inst.ports[net_name] for inst in ckt.instances)
            elif sig_name == "clk":
                external = False
                net_name = "columnclk"
                extra_ports = (rowperiph.ports.columnclk,)
            elif (
                sig_name in ("precharge_n", "we_en")
                or sig_name.startswith(("mux[", "wl["))
            ):
                external = False
                extra_ports = (rowperiph.ports[net_name],)
            elif sig_name.startswith(("d[", "q[", "we[")):
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

        _rowperiph_lay = layouter.inst_layout(inst=insts.rowperiph)
        _rowperiph_bb = _rowperiph_lay.boundary
        assert _rowperiph_bb is not None

        _columnblock_lay = layouter.inst_layout(inst=insts.columnblock)
        _columnblock_bb = _columnblock_lay.boundary
        assert _columnblock_bb is not None

        x_rowperiph = -_rowperiph_bb.left
        y_rowperiph = -_rowperiph_bb.bottom
        rowperiph_lay = layouter.place(
            _rowperiph_lay, x=x_rowperiph, y=y_rowperiph,
        )
        rowperiph_bb = rowperiph_lay.boundary
        assert rowperiph_bb is not None

        x_columnblock = rowperiph_bb.right - _columnblock_bb.left
        y_columnblock = -_columnblock_bb.bottom
        columnblock_lay = layouter.place(
            _columnblock_lay, x=x_columnblock, y=y_columnblock,
        )
        columnblock_bb = columnblock_lay.boundary
        assert columnblock_bb is not None

        cell_height = columnblock_bb.top
        cell_width = columnblock_bb.right

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
            net = nets[f"a[{a_bit}]"]
            m2pinbb = rowperiph_lay.bounds(mask=metal2pin.mask, net=net, depth=1)
            layouter.add_wire(net=net, wire=metal2, pin=metal2pin, shape=m2pinbb)

        # clk
        m3pinbb = rowperiph_lay.bounds(mask=metal3pin.mask, net=nets.clk, depth=1)
        layouter.add_wire(net=nets.clk, wire=metal3, pin=metal3pin, shape=m3pinbb)

        # Signal connected by abutment:
        # - wl[]
        # - precharge_n
        # - mux[]
        # - we_en
        # - columnclk connected by abutoment

        # d[n]/q[n]
        m3pinnets = (
            *(f"q[{bit}]" for bit in range(self.word_size)),
            *(f"d[{bit}]" for bit in range(self.word_size)),
            *(f"we[{we}]" for we in range(self.we_size)),
        )
        for m3pinnet in m3pinnets:
            net = nets[m3pinnet]
            m3pinbb = layout.bounds(mask=metal3pin.mask, net=net, depth=1)
            layouter.add_wire(net=net, wire=metal3, pin=metal3pin, shape=m3pinbb)

        # boundary
        self.set_size(width=cell_width, height=cell_height)


class SP6TFactory(_SRAMFactory):
    def __init__(self, *, lib: _lbry.Library, spec: SP6TSpecification):
        super().__init__(lib=lib, spec=spec)

    @property
    def spec(self) -> SP6TSpecification:
        return cast(SP6TSpecification, self._spec)

    def bitcell(self) -> _SP6TCell:
        return self._get_cell(
            cell_name=f"Cell",
            cls=_SP6TCell, cls_args={},
        )

    def wordlinedriver(self) -> _WordlineDriver:
        b = self.bitcell()
        return super().wordlinedriver(name_suffix="", wl_bottom=b.wl_bottom, wl_top=b.wl_top)

    def rowdecoderdrivepage(self, *, pds: int, rows: int) -> _RowDecoderDrivePage:
        return super().rowdecoderdrivepage(
            pds=pds, rows=rows, wldriver_kwargs={}, name_suffix="",
        )

    def rowdecoder(self, *, address_groups: Iterable[int]) -> _RowDecoder:
        return super().rowdecoder(
            address_groups=address_groups, reverse=False,
            page_kwargs={}, name_suffix="",
        )

    def rowperiphery(self, *,
        address_groups: Iterable[int], colperiph_kwargs: Dict[str, Any],
    ) -> _RowPeriphery:
        return super().rowperiphery(
            address_groups=address_groups, colperiph_kwargs=colperiph_kwargs,
            rowdec_kwargs={}, name_suffix="",
        )

    def precharge(self) -> _Precharge:
        b = self.bitcell()
        return super().precharge(
            bl_left=b.bl_left, bl_right=b.bl_right,
            bln_left=b.bln_left, bln_right=b.bln_right,
            name_suffix="",
        )

    def colmux(self, *, columns: int) -> _ColMux:
        b = self.bitcell()
        return super().colmux(
            columns=columns,
            bl_left=b.bl_left, bl_right=b.bl_right,
            bln_left=b.bln_left, bln_right=b.bln_right,
            name_suffix="",
        )

    def columnperiphery(self, *,
        bits: int, colmux: int,
    ) -> _ColumnPeriphery:
        return super().columnperiphery(
            bits=bits, colmux=colmux, precharge_kwargs={}, colmux_kwargs={},
            name_suffix="",
        )

    def column(self, *,
        rows: int, bits: int, colmux: int,
    ) -> _SP6TColumn:
        return self._get_cell(
            cell_name=f"Column_{rows}R{bits}B{colmux}M",
            cls=_SP6TColumn, cls_args={"rows": rows, "bits": bits, "colmux": colmux},
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
            cell_name=cell_name, cls=_SP6TBlock, cls_args={
                "address_groups": address_groups,
                "word_size": word_size, "we_size": we_size,
            }
        )
