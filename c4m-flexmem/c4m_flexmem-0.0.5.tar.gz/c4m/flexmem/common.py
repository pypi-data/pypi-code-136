# SPDX-License-Identifier: GPL-2.0-or-later OR AGPL-3.0-or-later OR CERN-OHL-S-2.0+
from math import log2, floor
from itertools import product
from typing import (
    Any, Tuple, List, Dict, Iterable, Collection, Optional, Type, TypeVar, Generic,
    cast,
)
import abc

from pdkmaster.technology import (
    geometry as _geo, primitive as _prm, technology_ as _tch,
)
from pdkmaster.design import circuit as _ckt, layout as _lay, library as _lbry


SigSpec = Collection[Tuple[str, _prm.Marker]]

_factory_type_ = TypeVar("_factory_type_", bound="_SRAMFactory")
_cell_type_ = TypeVar("_cell_type_", bound="_FactoryCell")


def _ispow2(n):
    return ((n & (n - 1)) == 0) and (n != 0)


class _SRAMSpecification:
    """Class to provide specification for the single port SRAM generation.
    """
    def __init__(self, *,
        name_prefix: str,
        nmos: _prm.MOSFET, pmos: _prm.MOSFET, stdcelllib: _lbry.Library,
        pu_l: float, pu_w: float, pd_l: float, pd_w: float, pg_l: float, pg_w: float,
        precharge_l: Optional[float]=None, precharge_w: float,
        colmux_l: Optional[float]=None, colmux_w: float,
        writedrive_l: Optional[float]=None, writedrive_w: float,
        wldrive_nmos_l: Optional[float]=None, wldrive_nmos_w: float,
        wldrive_pmos_l: Optional[float]=None, wldrive_pmos_w: float,
        prbound: Optional[_prm.Auxiliary]=None,
    ):
        self.name_prefix = name_prefix
        self._nmos = nmos
        self._pmos = pmos
        self._stdcelllib = stdcelllib
        self._pu_l = pu_l
        self._pu_w = pu_w
        self._pd_l = pd_l
        self._pd_w = pd_w
        self._pg_l = pg_l
        self._pg_w = pg_w
        self._precharge_l = precharge_l if precharge_l is not None else pmos.computed.min_l
        self._precharge_w = precharge_w
        self._colmux_l = colmux_l if colmux_l is not None else nmos.computed.min_l
        self._colmux_w = colmux_w
        self._writedrive_l = (
            writedrive_l if writedrive_l is not None
            else nmos.computed.min_l
        )
        self._writedrive_w = writedrive_w
        self._wldrive_nmos_l = (
            wldrive_nmos_l if wldrive_nmos_l is not None
            else nmos.computed.min_l
        )
        self._wldrive_nmos_w = wldrive_nmos_w
        self._wldrive_pmos_l = (
            wldrive_pmos_l if wldrive_pmos_l is not None
            else pmos.computed.min_l
        )
        self._wldrive_pmos_w = wldrive_pmos_w
        self._prbound = prbound

    @property
    def nmos(self) -> _prm.MOSFET:
        return self._nmos
    @property
    def pmos(self) -> _prm.MOSFET:
        return self._pmos
    @property
    def stdcelllib(self) -> _lbry.Library:
        return self._stdcelllib
    @property
    def pu_l(self) -> float:
        return self._pu_l
    @property
    def pu_w(self) -> float:
        return self._pu_w
    @property
    def pd_l(self) -> float:
        return self._pd_l
    @property
    def pd_w(self) -> float:
        return self._pd_w
    @property
    def pg_l(self) -> float:
        return self._pg_l
    @property
    def pg_w(self) -> float:
        return self._pg_w
    @property
    def precharge_l(self) -> float:
        return self._precharge_l
    @property
    def precharge_w(self) -> float:
        return self._precharge_w
    @property
    def colmux_l(self) -> float:
        return self._colmux_l
    @property
    def colmux_w(self) -> float:
        return self._colmux_w
    @property
    def writedrive_l(self) -> float:
        return self._writedrive_l
    @property
    def writedrive_w(self) -> float:
        return self._writedrive_w
    @property
    def wldrive_nmos_l(self) -> float:
        return self._wldrive_nmos_l
    @property
    def wldrive_nmos_w(self) -> float:
        return self._wldrive_nmos_w
    @property
    def wldrive_pmos_l(self) -> float:
        return self._wldrive_pmos_l
    @property
    def wldrive_pmos_w(self) -> float:
        return self._wldrive_pmos_w
    @property
    def prbound(self) -> Optional[_prm.Auxiliary]:
        return self._prbound


class _TechCache:
    """Cache and pre computation of technology derived parameters.

    This is a helper class to cache and precompute commonly needed parameters in
    different circuit and layout generation code.
    During intialization of this class it is also checked if the given technology
    fulfills assumption made on the given technology.
    """
    def __init__(self, *, fab: "_SRAMFactory", spec: _SRAMSpecification):
        self._fab = fab
        tech = fab.lib.tech
        prims = tech.primitives

        nmos = spec.nmos
        if nmos not in prims:
            raise ValueError(f"NMOS '{nmos.name}' not of technology '{tech.name}'")
        mosgate = nmos.gate
        self.poly = poly = mosgate.poly
        self.active = active = mosgate.active
        self.pwell = pwell = nmos.well
        if len(nmos.implant) != 1:
            raise NotImplementedError("NMOS with more than one implant")
        self.nimplant = nimplant = nmos.implant[0]
        nimpl_idx = active.implant.index(nimplant)

        pmos = spec.pmos
        if nmos not in prims:
            raise ValueError(f"PMOS '{nmos.name}' not of technology '{tech.name}'")
        if (pmos.gate.poly != mosgate.poly) or (pmos.gate.active != mosgate.active):
            raise NotImplementedError("NMOS and PMOS with a different gate or active layer")
        if pmos.well is None:
            raise NotImplementedError("PMOS transistor in the bulk")
        self.nwell = nwell = pmos.well
        if len(pmos.implant) != 1:
            raise NotImplementedError("PMOS with more than one implant")
        self.pimplant = pimplant = pmos.implant[0]
        pimpl_idx = active.implant.index(pimplant)

        self.min_actpoly_space = tech.computed.min_space(active, poly)
        self.min_nactpact_space = max(
            active.min_space,
            (
                active.min_implant_enclosure[nimpl_idx].max()
                + active.min_implant_enclosure[pimpl_idx].max()
            ),
        )

        nwell_idx = active.well.index(nwell)
        self.min_actnwell_enclosure = active.min_well_enclosure[nwell_idx].max()
        if pwell is None:
            assert active.min_substrate_enclosure is not None
            self.min_actpwell_enclosure = active.min_substrate_enclosure.max()
        else:
            pwell_idx = active.well.index(pwell)
            self.min_actpwell_enclosure = active.min_well_enclosure[pwell_idx].max()

        self.vias = vias = tuple(prims.__iter_type__(_prm.Via))
        self.contact = contact = vias[0]
        if poly not in contact.bottom:
            raise NotImplementedError(
                f"Gate poly layer '{poly.name}' not bottom connected by contact '{contact.name}'"
            )
        if active not in contact.bottom:
            raise NotImplementedError(
                f"Gate active layer '{active.name}' not bottom connected by contact '{contact.name}'"
            )
        for via in vias:
            if len(via.top) != 1:
                raise NotImplementedError(f"Via '{via.name}' with more than one top")
        for i in range(1, len(vias)):
            prevvia = vias[i - 1]
            via = vias[i]
            if (len(via.bottom) != 1) and not isinstance(via.bottom[0], _prm.MetalWire):
                raise NotImplementedError(f"Via '{via.name}' with more than one bottom")
            if prevvia.top[0] != via.bottom[0]:
                raise NotImplementedError(
                    f"Top of via '{prevvia.name}' is not bottom of '{via.name}'"
                )

        min_actpad_space = self.min_actpoly_space
        min_actmaxpad_space = min_actpad_space
        try:
            s = tech.computed.min_space(active, contact)
        except ValueError:
            pass
        else:
            idx = contact.bottom.index(poly)
            enc = contact.min_bottom_enclosure[idx].min()
            enc_max = contact.min_bottom_enclosure[idx].max()
            min_actpad_space = max(min_actpad_space, s - enc)
            min_actmaxpad_space = max(min_actmaxpad_space, s - enc_max)
        self.min_actpad_space = min_actpad_space
        self.min_actmaxpad_space = min_actmaxpad_space

        self.metals = metals = tuple(filter(
            lambda m: not isinstance(m, _prm.MIMTop),
            prims.__iter_type__(_prm.MetalWire),
        ))
        for metal in metals:
            if (metal.pin is None) or (len(metal.pin) != 1):
                raise NotImplementedError(
                    f"Metal '{metal.name}' not with a single pin layer"
                )
        self.metalpins = tuple(
            cast(Tuple[_prm.Marker], metal.pin)[0]
            for metal in metals
        )

        # Remember metal2 connection width for colmux computation
        self._m2colmux_connwidth = tech.computed.min_width(
            primitive=self.metal(2), up=False, down=True, min_enclosure=True,
        )

        # Generate bit_cell parameters on demand to avoid chicken and egg problem during
        # creation of factory & cache
        self._bit_bb: Optional[_geo.Rect] = None
        self._bit_nwellbb: Optional[_geo.Rect] = None
        self._bit_m1bb: Optional[_geo.Rect] = None
        self._bit_via1bb: Optional[_geo.Rect] = None
        self._bit_m2bb: Optional[_geo.Rect] = None

    @property
    def bit_bb(self) -> _geo.Rect:
        if self._bit_bb is None:
            bit_bb = self._fab.bitcell().layout.boundary
            assert isinstance(bit_bb, _geo.Rect)
            self._bit_bb = bit_bb

        return self._bit_bb
    @property
    def bit_width(self) -> float:
        return self.bit_bb.width
    @property
    def bit_height(self) -> float:
        return self.bit_bb.height
    @property
    def bit_nwellbb(self) -> _geo.Rect:
        if self._bit_nwellbb is None:
            bitcell = self._fab.bitcell()
            bit_lay = bitcell.layout
            bb = bit_lay.bounds(mask=self.nwell.mask)
            assert isinstance(bb, _geo.Rect)
            self._bit_nwellbb = bb

        return self._bit_nwellbb
    @property
    def bit_m1bb(self) -> _geo.Rect:
        if self._bit_m1bb is None:
            bitcell = self._fab.bitcell()
            bit_lay = bitcell.layout
            bb = bit_lay.bounds(mask=self.metal(1).mask)
            assert isinstance(bb, _geo.Rect)
            self._bit_m1bb = bb

        return self._bit_m1bb
    @property
    def bit_via1bb(self) -> _geo.Rect:
        if self._bit_via1bb is None:
            bitcell = self._fab.bitcell()
            bit_lay = bitcell.layout
            bb = bit_lay.bounds(mask=self.via(1).mask)
            assert isinstance(bb, _geo.Rect)
            self._bit_via1bb = bb

        return self._bit_via1bb
    @property
    def bit_m2bb(self) -> _geo.Rect:
        if self._bit_m2bb is None:
            bitcell = self._fab.bitcell()
            bit_lay = bitcell.layout
            bb = bit_lay.bounds(mask=self.metal(2).mask)
            assert isinstance(bb, _geo.Rect)
            self._bit_m2bb = bb

        return self._bit_m2bb
    # colmux pins have fixed vertical location
    @property
    def colmux_left(self) -> float:
        return 2*self.bit_width - 0.5*self._m2colmux_connwidth
    @property
    def colmux_right(self) -> float:
        return 2*self.bit_width + 0.5*self._m2colmux_connwidth
    @property
    def colmuxn_left(self) -> float:
        return self.bit_width - 0.5*self._m2colmux_connwidth
    @property
    def colmuxn_right(self) -> float:
        return self.bit_width + 0.5*self._m2colmux_connwidth

    def via(self, idx: int) -> _prm.Via:
        """Get nth via starting with 1 for first via

        The layer connecting typically the poly and active layer is considered
        to be the contact layer and not a via layer.
        """
        assert idx > 0
        return self.vias[idx]

    def metal(self, idx: int) -> _prm.MetalWire:
        """Get nth metal starting with 1 for first metal layer"""
        assert idx > 0
        return self.metals[idx - 1]

    def metalpin(self, idx: int) -> _prm.Marker:
        """Get nth metal pin starting with 1 for the pin of first metal layer"""
        assert idx > 0
        return self.metalpins[idx - 1]


class _FactoryCell(_lbry._OnDemandCell[_lbry.Library], Generic[_factory_type_]):
    def __init__(self, *, fab: _factory_type_, name: str):
        self.fab = fab
        super().__init__(lib=fab.lib, name=name)

    def set_boundary(self, *, bb: _geo.Rect) -> None:
        lay = self.layout
        lay.boundary = bb
        prbound = self.fab.spec.prbound
        if prbound is not None:
            lay.add_shape(prim=prbound, net=None, shape=bb)

    def set_size(self, *, width: float, height: float) -> None:
        self.set_boundary(bb=_geo.Rect(left=0.0, bottom=0.0, right=width, top=height))


class _BitCell(_FactoryCell[_factory_type_], Generic[_factory_type_]):
    # Describe the single/multi-port signals present in the cell
    # Currently supported configurations
    # single port: 1 wl signal and 1 bl signal
    # dual port: 2 wl signals and 2 bl signals. First of each is for port 1
    #     and second of each for the second port.
    dc_signals: SigSpec # Has to be named vss and vdd, used to specify pin layer.
    wl_signals: SigSpec # Word line signals
    bl_signals: SigSpec # Bit line signals (_n name will be inferred)

    def __init__(self, *, fab: _factory_type_, name: str):
        self.fab = fab
        super().__init__(fab=fab, name=name)

        assert set(sig for sig, _ in self.dc_signals) == {"vss", "vdd"}
        assert len(self.wl_signals) == len(self.bl_signals) # Corresponding to port
        assert len(self.wl_signals) in (1, 2) # Single or dual port

        # Dimension that need to be defined during cell layout generation
        self._vss_bottom: Optional[float] = None
        self._vss_top: Optional[float] = None
        self._vss_tapbb: Optional[_geo.Rect] = None
        self._vdd_bottom: Optional[float] = None
        self._vdd_top: Optional[float] = None

    @property
    def vss_bottom(self) -> float:
        if self._vss_bottom is None:
            self._create_layout()
            assert self._vss_bottom is not None
        return self._vss_bottom
    @property
    def vss_top(self) -> float:
        if self._vss_top is None:
            self._create_layout()
            assert self._vss_top is not None
        return self._vss_top
    @property
    def vss_tapbb(self) -> _geo.Rect:
        if self._vss_tapbb is None:
            self._create_layout()
            assert self._vss_tapbb is not None
        return self._vss_tapbb
    @property
    def vdd_bottom(self) -> float:
        if self._vdd_bottom is None:
            self._create_layout()
            assert self._vdd_bottom is not None
        return self._vdd_bottom
    @property
    def vdd_top(self) -> float:
        if self._vdd_top is None:
            self._create_layout()
            assert self._vdd_top is not None
        return self._vdd_top


class _CellArray(_FactoryCell["_SRAMFactory"]):
    def __init__(self, *,
        rows: int, columns: int, fab: "_SRAMFactory", name: str,
    ):
        super().__init__(fab=fab, name=name)

        if rows%2 != 0:
            raise NotImplementedError(f"Odd number of rows {rows}")
        if not _ispow2(columns):
            raise NotImplementedError(f"Number of columns {columns} not a power of two")
        self.rows = rows
        self.columns = columns

        self.row_insts: Optional[int] = None
        self.col_insts: Optional[int] = None

    def _create_circuit(self) -> None:
        fab = self.fab

        bit_cell = fab.bitcell()

        rows = self.rows
        assert rows%2 == 0, "Internal error"
        columns = self.columns
        assert _ispow2(columns), "Internal error"

        ckt = self.new_circuit()

        is_bitcell: bool = False
        if _ispow2(rows):
            if (columns >= rows):
                self.row_insts = 1
                self.col_insts = 2
                subcell = fab.bitarray(rows=rows, columns=columns//2)
                ckt.instantiate(subcell, name="inst0x0")
                ckt.instantiate(subcell, name="inst0x1")
            else:
                assert columns < rows, "Internal error"
                self.row_insts = 2
                self.col_insts = 1
                if rows == 2:
                    assert columns == 1, "Internal error"
                    subcell = fab.bitcell()
                    is_bitcell = True
                else:
                    subcell = fab.bitarray(rows=rows//2, columns=columns)
                ckt.instantiate(subcell, name="inst0x0")
                ckt.instantiate(subcell, name="inst1x0")
        else: # not _ispow2(rows)
            self.col_insts = 1
            row_insts = 0
            rem_rows = rows
            while rem_rows > 0:
                assert rem_rows > 1, "Internal error"
                rows2 = 2**floor(log2(rem_rows))
                n_insts = rem_rows//rows2
                subcell = fab.bitarray(rows=rows2, columns=columns)
                for _ in range(n_insts):
                    ckt.instantiate(subcell, name=f"inst{row_insts}x0")
                    row_insts += 1
                    rem_rows -= rows2
            assert row_insts > 0
            self.row_insts = row_insts

        assert self.row_insts is not None
        assert self.col_insts is not None

        insts = ckt.instances

        # vss/vdd nets
        vssports = []
        vddports = []
        for row in range(self.row_insts):
            for col in range(self.col_insts):
                inst = insts[f"inst{row}x{col}"]
                vssports.append(inst.ports.vss)
                vddports.append(inst.ports.vdd)
        ckt.new_net(name="vss", external=True, childports=vssports)
        ckt.new_net(name="vdd", external=True, childports=vddports)

        # wl/bl/bl_n nets and set subports
        if is_bitcell:
            assert (rows == 2) and (columns == 1), "Internal error"
            inst0 = cast(_ckt._CellInstance, insts[f"inst0x0"])
            inst1 = cast(_ckt._CellInstance, insts[f"inst1x0"])

            for sig, _ in bit_cell.wl_signals:
                ckt.new_net(
                    name=f"{sig}[0]", external=True, childports=(inst0.ports[sig],),
                )
                ckt.new_net(
                    name=f"{sig}[1]", external=True, childports=(inst1.ports[sig],),
                )
            for sig, _ in bit_cell.bl_signals:
                ckt.new_net(name=f"{sig}[0]", external=True, childports=(
                    inst0.ports[sig], inst1.ports[sig],
                ))
                ckt.new_net(name=f"{sig}_n[0]", external=True, childports=(
                    inst0.ports[f"{sig}_n"], inst1.ports[f"{sig}_n"],
                ))
        else:
            # wl
            row = 0
            for inst_row in range(self.row_insts):
                inst0 = cast(_ckt._CellInstance, insts[f"inst{inst_row}x0"])
                cell0 = inst0.cell
                assert isinstance(cell0, _CellArray)

                for inst_wl in range(cell0.rows):
                    for sig, _ in bit_cell.wl_signals:
                        instwlname = f"{sig}[{inst_wl}]"
                        wlports = []
                        for inst_col in range(self.col_insts):
                            instname = f"inst{inst_row}x{inst_col}"
                            inst = cast(_ckt._CellInstance, insts[instname])
                            wlports.append(inst.ports[instwlname])
                        ckt.new_net(name=f"{sig}[{row}]", external=True, childports=wlports)
                    row += 1

            # bl/bl_n
            col = 0
            for inst_col in range(self.col_insts):
                inst0 = cast(_ckt._CellInstance, insts[f"inst0x{inst_col}"])
                cell0 = inst0.cell
                assert isinstance(cell0, _CellArray)

                for inst_bl in range(cell0.columns):
                    for sig, _ in bit_cell.bl_signals:
                        instblname = f"{sig}[{inst_bl}]"
                        instblnname = f"{sig}_n[{inst_bl}]"
                        blports = []
                        blnports = []
                        for inst_row in range(self.row_insts):
                            instname = f"inst{inst_row}x{inst_col}"
                            inst = cast(_ckt._CellInstance, insts[instname])
                            blports.append(inst.ports[instblname])
                            blnports.append(inst.ports[instblnname])
                        ckt.new_net(
                            name=f"{sig}[{col}]", external=True, childports=blports,
                        )
                        ckt.new_net(
                            name=f"{sig}_n[{col}]", external=True, childports=blnports,
                        )
                    col += 1

    def _create_layout(self):
        fab = self.fab
        spec = fab.spec
        cache = fab._cache

        ckt = self.circuit # Will generate circuit if it does not yet exist
        insts = ckt.instances
        nets = ckt.nets

        assert self.row_insts is not None, "Internal error"
        assert self.col_insts is not None, "Internal error"

        metal2 = cache.metal(2)
        metal2pin = cache.metalpin(2)
        metal3 = cache.metal(3)
        metal3pin = cache.metalpin(3)

        metal_lookup = {metal2pin: metal2, metal3pin: metal3}

        layouter = self.new_circuitlayouter()
        layout = layouter.layout

        bit_cell = fab.bitcell()
        bit_width = cache.bit_width
        bit_height = cache.bit_height
        # Get vdd/vss pins; take into account mirroring of cell
        vdd_m3bb0 = _geo.Rect(
            left=0.0, bottom=(bit_cell.vdd_bottom - bit_height),
            right=bit_width, top=(bit_cell.vdd_top - bit_height),
        )
        vss_m3bb0 = _geo.Rect(
            left=0.0, bottom=(bit_cell.vss_bottom + bit_height),
            right=bit_width, top=(bit_cell.vss_top + bit_height),
        )

        if (self.rows == 2) and (self.columns == 1):
            inst0 = cast(_ckt._CellInstance, insts["inst0x0"])
            inst1 = cast(_ckt._CellInstance, insts["inst1x0"])

            layouter.place(inst0, x=0.0, y=bit_height, rotation=_geo.Rotation.MX)
            layouter.place(inst1, x=0.0, y=bit_height)

            cell_width = bit_width
            cell_height = 2*bit_height
        else:
            x = None
            y = 0.0
            lay = None
            for inst_row in range(self.row_insts):
                x = 0.0
                for inst_col in range(self.col_insts):
                    inst = cast(_ckt._CellInstance, insts[f"inst{inst_row}x{inst_col}"])
                    layouter.place(inst, x=x, y=y)
                    lay = inst.cell.layout
                    assert lay.boundary is not None
                    x += lay.boundary.width
                assert (lay is not None) and (lay.boundary is not None)
                y += lay.boundary.height
            assert x is not None
            cell_width = x
            cell_height = y

        # vss/vdd m3 pins
        vss_left = vss_m3bb0.left
        vss_right = cell_width - vss_left
        vdd_left = vdd_m3bb0.left
        vdd_right = cell_width - vdd_left
        for drow in range(self.rows//2):
            dy = 2*drow*bit_height

            shape = _geo.Rect(
                left=vss_left, bottom=(vss_m3bb0.bottom + dy),
                right=vss_right, top=(vss_m3bb0.top + dy),
            )
            layouter.add_wire(net=nets.vss, wire=metal3, pin=metal3pin, shape=shape)

            shape = _geo.Rect(
                left=vdd_left, bottom=(vdd_m3bb0.bottom + dy),
                right=vdd_right, top=(vdd_m3bb0.top + dy),
            )
            layouter.add_wire(net=nets.vdd, wire=metal3, pin=metal3pin, shape=shape)

        dy = self.rows*bit_height

        shape = _geo.Rect(
            left=vdd_left, bottom=(vdd_m3bb0.bottom + dy),
            right=vdd_right, top=(vdd_m3bb0.top + dy),
        )
        layouter.add_wire(net=nets.vdd, wire=metal3, pin=metal3pin, shape=shape)

        # wl m3 pins
        for row in range(self.rows):
            for sig, pin in bit_cell.wl_signals:
                metal = metal_lookup[pin]

                net = nets[f"{sig}[{row}]"]
                shape = layout.bounds(mask=pin.mask, net=net, depth=1)
                layouter.add_wire(net=net, wire=metal, pin=pin, shape=shape)

        # bl/bl_n m2 pins
        for col in range(self.columns):
            for sig, pin in bit_cell.bl_signals:
                metal = metal_lookup[pin]

                net = nets[f"{sig}[{col}]"]
                shape = layout.bounds(mask=pin.mask, net=net, depth=1)
                layouter.add_wire(net=net, wire=metal, pin=pin, shape=shape)

                net = nets[f"{sig}_n[{col}]"]
                shape = layout.bounds(mask=pin.mask, net=net, depth=1)
                layouter.add_wire(net=net, wire=metal, pin=pin, shape=shape)

        # boundary
        self.set_size(width=cell_width, height=cell_height)


class _WordlineDriver(_FactoryCell["_SRAMFactory"]):
    # The w of the trnasistors will be two times the specified w
    def __init__(self, *,
        nmos_l: float, nmos_w: float, pmos_l: float, pmos_w: float,
        wl_bottom: float, wl_top: float,
        fab: "_SRAMFactory", name: str,
    ):
        super().__init__(fab=fab, name=name)
        self.nmos_l = nmos_l
        self.nmos_w = nmos_w
        self.pmos_l = pmos_l
        self.pmos_w = pmos_w
        self.wl_bottom = wl_bottom
        self.wl_top = wl_top

    def _create_circuit(self):
        fab = self.fab
        spec = fab.spec

        ckt = self.new_circuit()

        nmos1 = ckt.instantiate(
            spec.nmos, name="nmos1", l=spec.wldrive_nmos_l, w=spec.wldrive_nmos_w,
        )
        nmos2 = ckt.instantiate(
            spec.nmos, name="nmos2", l=spec.wldrive_nmos_l, w=spec.wldrive_nmos_w,
        )
        pmos1 = ckt.instantiate(
            spec.pmos, name="pmos1", l=spec.wldrive_pmos_l, w=spec.wldrive_pmos_w,
        )
        pmos2 = ckt.instantiate(
            spec.pmos, name="pmos2", l=spec.wldrive_pmos_l, w=spec.wldrive_pmos_w,
        )

        ckt.new_net(name="vss", external=True, childports=(
            nmos1.ports.sourcedrain1, nmos1.ports.bulk,
            nmos2.ports.sourcedrain2, nmos2.ports.bulk,
        ))
        ckt.new_net(name="vdd", external=True, childports=(
            pmos1.ports.sourcedrain1, pmos1.ports.bulk,
            pmos2.ports.sourcedrain2, pmos2.ports.bulk,
        ))

        ckt.new_net(name="wl_n", external=True, childports=(
            nmos1.ports.gate, nmos2.ports.gate,
            pmos1.ports.gate, pmos2.ports.gate,
        ))
        ckt.new_net(name="wl_drive", external=True, childports=(
            nmos1.ports.sourcedrain2, nmos2.ports.sourcedrain1,
            pmos1.ports.sourcedrain2, pmos2.ports.sourcedrain1,
        ))

    def _create_layout(self):
        fab = cast("_SRAMFactory", self.fab)
        tech = fab.tech
        spec = fab.spec
        cache = fab._cache

        nets = self.circuit.nets
        insts = self.circuit.instances

        nwell = cache.nwell
        pwell = cache.pwell
        nimplant = cache.nimplant
        pimplant = cache.pimplant
        active = cache.active
        poly = cache.poly
        contact = cache.contact
        metal1 = cache.metal(1)
        metal1pin = cache.metalpin(1)
        via1 = cache.via(1)
        metal2 = cache.metal(2)
        via2 = cache.via(2)
        metal3 = cache.metal(3)
        metal3pin = cache.metalpin(3)

        layouter = self.new_circuitlayouter()
        layout = layouter.layout

        nwell_net = None if nwell is None else nets.vdd
        pwell_net = None if pwell is None else nets.vss

        bit_cell = fab.bitcell()
        cell_height = cache.bit_height

        # Precompute some values
        vss_y = 0.5*(bit_cell.vss_bottom + bit_cell.vss_top)
        vss_height = bit_cell.vss_top - bit_cell.vss_bottom
        vdd_y = 0.5*(bit_cell.vdd_bottom + bit_cell.vdd_top)
        vdd_height = bit_cell.vdd_top - bit_cell.vdd_bottom

        # Generate sub layouts
        _nmos1_lay = layouter.inst_layout(inst=insts.nmos1, rotation=_geo.Rotation.R270)
        _nmos2_lay = layouter.inst_layout(inst=insts.nmos2, rotation=_geo.Rotation.R270)
        _pmos1_lay = layouter.inst_layout(inst=insts.pmos1, rotation=_geo.Rotation.R270)
        _pmos2_lay = layouter.inst_layout(inst=insts.pmos2, rotation=_geo.Rotation.R270)

        _via2wld_lay = layouter.wire_layout(
            net=nets.wl_drive, wire=via2,
            bottom_enclosure="tall",
            top_height=(self.wl_top - self.wl_bottom), top_enclosure="wide",
        )
        _via2wld_m2bb = _via2wld_lay.bounds(mask=metal2.mask)

        # Compute placement
        # This cell is designed to be put next to the SRAM bit cell, we thus
        # base some of the coordinates of the bit cell layout
        x_via2wld = cache.bit_m2bb.left - metal2.min_space - _via2wld_m2bb.right
        y_via2wld = 0.5*(self.wl_bottom + self.wl_top)

        y_mos1 = tech.on_grid(0.75*cache.bit_height, rounding="floor")
        y_mos2 = tech.on_grid(0.25*cache.bit_height, rounding="ceiling")

        _nmos1_actbb = _nmos1_lay.bounds(mask=active.mask)
        _nmos1_nimplbb = _nmos1_lay.bounds(mask=nimplant.mask)
        # Assume precharge has a vdd contact on the left so also take the nwell
        # edge of that into account
        _ch_lay = layouter.fab.layout_primitive(
            prim=contact, well_net=nwell_net,
            bottom=active, bottom_implant=pimplant, bottom_well=nwell,
            bottom_enclosure="wide",
        )
        _ch_nwbb = _ch_lay.bounds(mask=nwell.mask)
        nwell_left = min(cache.bit_nwellbb.left, _ch_nwbb.left)
        x_nmos = min(
            -nimplant.min_space - _nmos1_nimplbb.right,
            min(
                x_via2wld + _via2wld_m2bb.left - metal2.min_space,
                # cache.bit_nwellbb.left - cache.min_actpwell_enclosure,
                nwell_left - cache.min_actpwell_enclosure,
            ) - _nmos1_actbb.right,
        )
        nmos1_lay = layouter.place(_nmos1_lay, x=x_nmos, y=y_mos1)
        nmos2_lay = layouter.place(_nmos2_lay, x=x_nmos, y=y_mos2)

        nmos1_act = nmos1_lay.bounds(mask=active.mask)
        _pmos1_actbb = _pmos1_lay.bounds(mask=active.mask)
        _pmos1_nwellbb = _pmos1_lay.bounds(mask=nwell.mask)
        x_pmos = min(
            nmos1_act.left - max(
                cache.min_nactpact_space,
                cache.min_actnwell_enclosure + cache.min_actpwell_enclosure,
            )
            - _pmos1_actbb.right,
            nwell_left - nwell.min_space - _pmos1_nwellbb.right,
        )
        pmos1_lay = layouter.place(_pmos1_lay, x=x_pmos, y=y_mos1)
        pmos2_lay = layouter.place(_pmos2_lay, x=x_pmos, y=y_mos2)

        nmos1_actbb = nmos1_lay.bounds(mask=active.mask)
        pmos1_actbb = pmos1_lay.bounds(mask=active.mask)

        nmos1_polybb = nmos1_lay.bounds(mask=poly.mask)
        nmos2_polybb = nmos2_lay.bounds(mask=poly.mask)
        pmos1_polybb = pmos1_lay.bounds(mask=poly.mask)
        pmos2_polybb = pmos2_lay.bounds(mask=poly.mask)

        # wl_n
        h = tech.on_grid(
            pmos1_polybb.top - pmos2_polybb.bottom, mult=2,
            rounding="floor",
        )
        _chpolywln_lay = layouter.wire_layout(
            net=nets.wl_n, wire=contact, bottom=poly,
            bottom_height=h, bottom_enclosure="tall",
        )
        _chpolywln_polybb = _chpolywln_lay.bounds(mask=poly.mask)
        x_chpolywln = (
            pmos1_actbb.left - cache.min_actpad_space - _chpolywln_polybb.right
        )
        y_chpolywln = tech.on_grid(0.5*cache.bit_height)
        chpolywln_lay = layouter.place(_chpolywln_lay, x=x_chpolywln, y=y_chpolywln)
        chpolywln_polybb = chpolywln_lay.bounds(mask=poly.mask)
        chpolywln_m1bb = chpolywln_lay.bounds(mask=metal1.mask)

        shape = _geo.Rect.from_rect(
            rect=pmos1_polybb, left=chpolywln_polybb.left, right=nmos1_polybb.right,
        )
        layouter.add_wire(net=nets.wl_n, wire=poly, shape=shape)
        shape = _geo.Rect.from_rect(
            rect=pmos2_polybb, left=chpolywln_polybb.left, right=nmos2_polybb.right,
        )
        layouter.add_wire(net=nets.wl_n, wire=poly, shape=shape)

        cell_left = chpolywln_polybb.left - poly.min_space

        shape = _geo.Rect.from_rect(rect=chpolywln_m1bb, left=cell_left)
        layouter.add_wire(net=nets.wl_n, wire=metal1, pin=metal1pin, shape=shape)

        # wl_drive
        bottom_shape = _geo.Rect(
            left=nmos1_actbb.left,
            bottom=tech.on_grid(
                nmos2_polybb.top + spec.nmos.computed.min_contactgate_space,
                mult=2, rounding="ceiling",
            ),
            right=nmos1_actbb.right,
            top=tech.on_grid(
                nmos1_polybb.bottom - spec.nmos.computed.min_contactgate_space,
                mult=2, rounding="floor",
            ),
        )
        layouter.add_wire(
            net=nets.wl_drive, wire=contact, well_net=pwell_net, origin=bottom_shape.center,
            bottom=active, bottom_implant=nimplant, bottom_well=pwell,
            bottom_width=bottom_shape.width, bottom_height=bottom_shape.height,
            bottom_enclosure="tall", top_enclosure="wide",
        )

        bottom_shape = _geo.Rect(
            left=pmos1_actbb.left,
            bottom=tech.on_grid(
                pmos2_polybb.top + spec.pmos.computed.min_contactgate_space,
                mult=2, rounding="ceiling"
            ),
            right=pmos1_actbb.right,
            top=tech.on_grid(
                pmos1_polybb.bottom - spec.pmos.computed.min_contactgate_space,
                mult=2, rounding="floor",
            ),
        )
        chwldnmos_lay = layouter.add_wire(
            net=nets.wl_drive, wire=contact, well_net=nwell_net, origin=bottom_shape.center,
            bottom=active, bottom_implant=pimplant, bottom_well=nwell,
            bottom_width=bottom_shape.width, bottom_height=bottom_shape.height,
            bottom_enclosure="tall", top_enclosure="wide",
        )
        chwldpmos_m1bb = chwldnmos_lay.bounds(mask=metal1.mask)

        via2wld_lay = layouter.place(_via2wld_lay, x=x_via2wld, y=y_via2wld)
        via2wld_m2bb = via2wld_lay.bounds(mask=metal2.mask)
        via2wld_m3bb = via2wld_lay.bounds(mask=metal3.mask)

        shape = _geo.Rect.from_rect(rect=via2wld_m3bb, right=0.0)
        layouter.add_wire(net=nets.wl_drive, wire=metal3, pin=metal3pin, shape=shape)

        _via1wld_lay = layouter.wire_layout(
            net=nets.wl_drive, wire=via1,
            bottom_height=chwldpmos_m1bb.height, bottom_enclosure="wide",
            top_enclosure="tall",
        )
        _via1wld_m1bb = _via1wld_lay.bounds(mask=metal1.mask)
        _via1wld_via1bb = _via1wld_lay.bounds(mask=via1.mask)
        _via1wld_m2bb = _via1wld_lay.bounds(mask=metal2.mask)
        x_via1wld = min(
            x_via2wld,
            cache.bit_m1bb.left - metal1.min_space - _via1wld_m1bb.right,
            cache.bit_via1bb.left - via1.min_space - _via1wld_via1bb.right,
            cache.bit_m2bb.left - metal2.min_space - _via1wld_m2bb.right,
        )
        y_via1wld = y=chwldpmos_m1bb.center.y
        via1wld_lay = layouter.place(_via1wld_lay, x=x_via1wld, y=y_via1wld)
        via1wld_m1bb = via1wld_lay.bounds(mask=metal1.mask)
        via1wld_m2bb = via1wld_lay.bounds(mask=metal2.mask)

        shape=_geo.Rect.from_rect(rect=chwldpmos_m1bb, right=via1wld_m1bb.right)
        layouter.add_wire(net=nets.wl_drive, wire=metal1, shape=shape)

        shape=_geo.Rect.from_rect(rect=via2wld_m2bb, top=via1wld_m2bb.top)
        layouter.add_wire(net=nets.wl_drive, wire=metal2, shape=shape)

        # vss
        h = 2*(nmos2_polybb.bottom - spec.nmos.computed.min_contactgate_space)
        w = spec.wldrive_nmos_w
        layouter.add_wire(
            net=nets.vss, wire=contact, well_net=pwell_net, x=x_nmos, y=0.0,
            bottom=active, bottom_implant=nimplant, bottom_well=pwell,
            bottom_width=w, bottom_height=h, bottom_enclosure="tall",
            top_width=w, top_enclosure="wide",
        )
        layouter.add_wire(
            net=nets.vss, wire=contact, well_net=pwell_net, x=x_nmos, y=cell_height,
            bottom=active, bottom_implant=nimplant, bottom_well=pwell,
            bottom_width=w, bottom_height=h, bottom_enclosure="tall",
            top_width=w, top_enclosure="wide",
        )
        via1vss_lay = layouter.add_wire(
            net=nets.vss, wire=via1, x=x_nmos, y=0.0,
            bottom_width=w, bottom_enclosure="wide",
            top_width=w, top_enclosure="wide",
        )
        via1vss_m2bb1 = via1vss_lay.bounds(mask=metal2.mask)
        via1vss_lay = layouter.add_wire(
            net=nets.vss, wire=via1, x=x_nmos, y=cell_height,
            bottom_width=w, bottom_enclosure="wide",
            top_width=w, top_enclosure="wide",
        )
        via1vss_m2bb2 = via1vss_lay.bounds(mask=metal2.mask)

        # vss metal2 line will be done after vdd using that m2 line

        layouter.add_wire(
            net=nets.vss, wire=via2, x=x_nmos, y=vss_y,
            bottom_enclosure="wide",
            top_height=vss_height, top_enclosure="wide",
        )
        shape = _geo.Rect(
            left=cell_left, bottom=bit_cell.vss_bottom,
            right=0.0, top=bit_cell.vss_top,
        )
        layouter.add_wire(net=nets.vss, wire=metal3, pin=metal3pin, shape=shape)

        # bulk contact on right edge
        chvsspwell_lay = layouter.add_wire(
            net=nets.vss, wire=contact, well_net=pwell_net, x=0.0, y=0.0,
            bottom=active, bottom_implant=pimplant, bottom_well=pwell,
            bottom_enclosure="tall", bottom_height=bit_cell.vss_tapbb.height,
            top_enclosure="wide",
        )
        chvsspwell_pwellbb: Optional[_geo.Rect] = None
        if pwell is not None:
            chvsspwell_pwellbb = chvsspwell_lay.bounds(mask=pwell.mask)
        chvsspwell_m1bb = chvsspwell_lay.bounds(mask=metal1.mask)

        shape = _geo.Rect.from_rect(rect=chvsspwell_m1bb, left=x_nmos)
        layouter.add_wire(net=nets.vss, wire=metal1, shape=shape)

        # vdd
        h = 2*(pmos2_polybb.bottom - spec.pmos.computed.min_contactgate_space)
        w = spec.wldrive_pmos_w
        chvdd_lay = layouter.add_wire(
            net=nets.vdd, wire=contact, well_net=nwell_net, x=x_pmos, y=0.0,
            bottom=active, bottom_implant=pimplant, bottom_well=nwell,
            bottom_width=w, bottom_height=h, bottom_enclosure="tall",
            top_width=w, top_enclosure="wide",
        )
        chvdd_pimplbb1 = chvdd_lay.bounds(mask=pimplant.mask)
        chvdd_lay = layouter.add_wire(
            net=nets.vdd, wire=contact, well_net=nwell_net, x=x_pmos, y=cell_height,
            bottom=active, bottom_implant=pimplant, bottom_well=nwell,
            bottom_width=w, bottom_height=h, bottom_enclosure="tall",
            top_width=w, top_enclosure="wide",
        )
        chvdd_pimplbb2 = chvdd_lay.bounds(mask=pimplant.mask)
        via1vdd_lay = layouter.add_wire(
            net=nets.vdd, wire=via1, x=x_pmos, y=0.0,
            bottom_width=w, bottom_enclosure="wide",
            top_width=w, top_enclosure="wide",
        )
        via1vdd_m2bb1 = via1vdd_lay.bounds(mask=metal2.mask)
        via1vdd_lay = layouter.add_wire(
            net=nets.vdd, wire=via1, x=x_pmos, y=cell_height,
            bottom_width=w, bottom_enclosure="wide",
            top_width=w, top_enclosure="wide",
        )
        via1vdd_m2bb2 = via1vdd_lay.bounds(mask=metal2.mask)

        m2vdd_bb = _geo.Rect.from_rect(rect=via1vdd_m2bb1, top=via1vdd_m2bb2.top)
        layouter.add_wire(net=nets.vdd, wire=metal2, shape=m2vdd_bb)

        layouter.add_wire(
            net=nets.vdd, wire=via2, x=x_pmos, y=vdd_y,
            bottom_width=w, bottom_enclosure="wide",
            top_height=vdd_height, top_enclosure="wide",
        )
        shape = _geo.Rect(
            left=cell_left, bottom=bit_cell.vdd_bottom,
            right=0.0, top=bit_cell.vdd_top,
        )
        layouter.add_wire(net=nets.vdd, wire=metal3, pin=metal3pin, shape=shape)

        # m2 for vss
        right = min(via1wld_m2bb.left, via2wld_m2bb.left) - metal2.min_space
        shape = _geo.Rect(
            left=(m2vdd_bb.right + metal2.min_space), bottom=via1vss_m2bb1.bottom,
            right=right, top=via1vss_m2bb2.top,
        )
        layouter.add_wire(net=nets.vss, wire=metal2, shape=shape)

        # nwell contact on left edge
        chvddnwell_lay = layouter.add_wire(
            net=nets.vdd, wire=contact, well_net=nwell_net,
            x=cell_left, y=vdd_y,
            bottom=active, bottom_implant=nimplant, bottom_well=nwell,
            bottom_enclosure="wide", top_enclosure="wide",
        )
        chvddnwell_nwellbb: Optional[_geo.Rect] = None
        if nwell is not None:
            chvddnwell_nwellbb = chvddnwell_lay.bounds(mask=nwell.mask)
        chvddnwell_m1bb = chvddnwell_lay.bounds(mask=metal1.mask)

        shape = _geo.Rect.from_rect(rect=chvddnwell_m1bb, right=x_pmos)
        layouter.add_wire(net=nets.vdd, wire=metal1, shape=shape)

        # nimplant
        shape  = _geo.Rect.from_rect(rect=chvdd_pimplbb1, top=chvdd_pimplbb2.top)
        layout.add_shape(prim=pimplant, shape=shape)
        # Cover poly ch with implant
        shape = _geo.Rect.from_rect(rect=chpolywln_polybb, right=chvdd_pimplbb1.right)
        layout.add_shape(prim=pimplant, shape=shape)

        for nimplms in bit_cell.layout.filter_polygons(mask=nimplant.mask, split=True):
            nimplbb = nimplms.bounds
            if nimplbb.left < 0.0:
                shape = _geo.Rect.from_rect(rect=nimplbb, left=x_nmos, right=0.0)
                layouter.add_portless(prim=nimplant, shape=shape)

        # wells
        if nwell is not None:
            assert chvddnwell_nwellbb is not None
            bb = layout.bounds(mask=nwell.mask)
            shape = _geo.Rect(
                left=chvddnwell_nwellbb.left, right=bb.right,
                bottom=min(
                    chvddnwell_nwellbb.bottom,
                    cell_height - 0.5*nwell.min_width,
                ),
                top=max(
                    chvddnwell_nwellbb.top,
                    cell_height + 0.5*nwell.min_width,
                ),
            )
            layouter.add_wire(net=nets.vdd, wire=nwell, shape=shape)
        if pwell is not None:
            assert chvsspwell_pwellbb is not None
            bb = layout.bounds(mask=pwell.mask)
            shape = _geo.Rect(
                right=chvsspwell_pwellbb.right, left = bb.left,
                bottom=min(
                    chvsspwell_pwellbb.bottom,
                    -0.5*pwell.min_width,
                ),
                top=max(
                    chvsspwell_pwellbb.top,
                    0.5*pwell.min_width,
                ),
            )
            layouter.add_wire(net=nets.vdd, wire=nwell, shape=shape)
        # boundary
        self.set_boundary(
            bb=_geo.Rect(left=cell_left, bottom=0.0, right=0.0, top=cell_height),
        )


class _RowDecoderNand3(_FactoryCell["_SRAMFactory"]):
    def _create_circuit(self):
        fab = self.fab
        tech = fab.tech
        spec = fab.spec
        cache = fab._cache

        nmos = spec.nmos
        pmos = spec.pmos

        active = cache.active
        poly = cache.poly
        contact = cache.contact

        nactpact_space = max(
            cache.min_nactpact_space,
            cache.min_actnwell_enclosure + cache.min_actpwell_enclosure,
        )
        try:
            s = tech.computed.min_space(contact, active)
        except ValueError:
            pass
        else:
            nactpact_space = max(nactpact_space, 2*s + contact.width)
        w2 = (
            cache.bit_height
            - (
                poly.min_space + nmos.computed.min_polyactive_extension
                + pmos.computed.min_polyactive_extension
            )
            - nactpact_space
        )
        l_n = nmos.computed.min_l
        w_n = tech.on_grid(w2/2, mult=2, rounding="floor")
        l_p = pmos.computed.min_l
        w_p = w_n

        ckt = self.new_circuit()

        nmoses = tuple(
            ckt.instantiate(nmos, name=f"nmos[{mos}]", l=l_n, w=w_n)
            for mos in range(3)
        )
        pmoses = tuple(
            ckt.instantiate(pmos, name=f"pmos[{mos}]", l=l_p, w=w_p)
            for mos in range(3)
        )

        ckt.new_net(name="vss", external=True, childports=(
            nmoses[0].ports.sourcedrain1, *(nmos.ports.bulk for nmos in nmoses),
        ))
        ckt.new_net(name="vdd", external=True, childports=(
            pmoses[0].ports.sourcedrain1, pmoses[1].ports.sourcedrain2,
            pmoses[2].ports.sourcedrain1, *(pmos.ports.bulk for pmos in pmoses),
        ))

        ckt.new_net(name="pd[0]", external=True, childports=(
            nmoses[0].ports.gate, pmoses[0].ports.gate,
        ))
        ckt.new_net(name="pd[1]", external=True, childports=(
            nmoses[1].ports.gate, pmoses[1].ports.gate,
        ))
        ckt.new_net(name="wl_en", external=True, childports=(
            nmoses[2].ports.gate, pmoses[2].ports.gate,
        ))

        ckt.new_net(name="int[0]", external=False, childports=(
            nmoses[0].ports.sourcedrain2, nmoses[1].ports.sourcedrain1,
        ))
        ckt.new_net(name="int[1]", external=False, childports=(
            nmoses[1].ports.sourcedrain2, nmoses[2].ports.sourcedrain1,
        ))

        ckt.new_net(name="wl_n", external=True, childports=(
            nmoses[2].ports.sourcedrain2, pmoses[0].ports.sourcedrain2,
            pmoses[1].ports.sourcedrain1, pmoses[2].ports.sourcedrain2,
        ))

    def _create_layout(self):
        fab = self.fab
        tech = fab.tech
        spec = fab.spec
        cache = fab._cache

        nets = self.circuit.nets
        insts = self.circuit.instances

        nmos = spec.nmos
        pmos = spec.pmos

        nwell = cache.nwell
        pwell = cache.pwell
        active = cache.active
        pimplant = cache.pimplant
        nimplant = cache.nimplant
        poly = cache.poly
        contact = cache.contact
        metal1 = cache.metal(1)
        metal1pin = cache.metalpin(1)
        via1 = cache.via(1)
        via2 = cache.via(2)
        metal3 = cache.metal(3)
        metal3pin = cache.metalpin(3)

        nwell_net = None if nwell is None else nets.vdd
        pwell_net = None if pwell is None else nets.vss

        cell_height = cache.bit_height
        y_chpad = tech.on_grid(0.5*cell_height)

        layouter = self.new_circuitlayouter()
        layout = layouter.layout

        _chvsspwell_lay = layouter.wire_layout(
            net=nets.vss, wire=contact, well_net=pwell_net,
            bottom=active, bottom_implant=pimplant, bottom_well=pwell,
            bottom_enclosure="tall", top_enclosure="wide",
        )
        _chvsspwell_pimplbb = _chvsspwell_lay.bounds(mask=pimplant.mask)

        x_chvsspwell = 0.5*pimplant.min_space - _chvsspwell_pimplbb.left
        y_chvsspwell = 0.0
        chvsspwell_lay = layouter.place(_chvsspwell_lay, x=x_chvsspwell, y=y_chvsspwell)
        chvsspwell_actbb = chvsspwell_lay.bounds(mask=active.mask)

        _chvddnwell_lay = layouter.wire_layout(
            net=nets.vdd, wire=contact, well_net=nwell_net,
            bottom=active, bottom_implant=nimplant, bottom_well=nwell,
            bottom_enclosure="tall", top_enclosure="wide",
        )
        _chvddnwell_nimplbb = _chvddnwell_lay.bounds(mask=nimplant.mask)

        x_chvddnwell = 0.5*nimplant.min_space - _chvddnwell_nimplbb.left
        y_chvddnwell = cell_height
        chvddnwell_lay = layouter.place(_chvddnwell_lay, x=x_chvddnwell, y=y_chvddnwell)
        chvddnwell_actbb = chvddnwell_lay.bounds(mask=active.mask)

        _chvssnact_lay = layouter.wire_layout(
            net=nets.vss, wire=contact, well_net=pwell_net,
            bottom=active, bottom_implant=nimplant, bottom_well=pwell,
            bottom_enclosure="tall", top_enclosure="wide",
        )
        _chvssnact_actbb = _chvssnact_lay.bounds(mask=active.mask)
        x_chvssnact = (
            chvsspwell_actbb.right + cache.min_nactpact_space - _chvssnact_actbb.left
        )
        y_chvssnact = 0.0
        chvssnact_lay = layouter.place(_chvssnact_lay, x=x_chvssnact, y=y_chvssnact)
        chvssnact_actbb = chvssnact_lay.bounds(mask=active.mask)
        chvssnact_nimplbb = chvssnact_lay.bounds(mask=nimplant.mask)
        chvssnact_m1bb = chvssnact_lay.bounds(mask=metal1.mask)

        _chvddpact_lay = layouter.wire_layout(
            net=nets.vdd, wire=contact, well_net=nwell_net,
            bottom=active, bottom_implant=pimplant, bottom_well=nwell,
            bottom_enclosure="tall", top_enclosure="wide",
        )
        _chvddpact_actbb = _chvddpact_lay.bounds(mask=active.mask)
        x_chvddpact = (
            chvddnwell_actbb.right + cache.min_nactpact_space - _chvddpact_actbb.left
        )
        y_chvddpact = cell_height
        chvddpact_lay = layouter.place(_chvddpact_lay, x=x_chvddpact, y=y_chvddpact)
        chvddpact_actbb = chvddpact_lay.bounds(mask=active.mask)
        chvddpact_pimplbb = chvddpact_lay.bounds(mask=pimplant.mask)
        chvddpact_m1bb = chvddpact_lay.bounds(mask=metal1.mask)

        # place moses
        gate_space = max(
            chvddpact_actbb.width + 2*cache.min_actpoly_space,
            2*pmos.computed.min_contactgate_space + contact.width,
        )

        _nmos_lays = tuple(
            layouter.inst_layout(inst=insts[f"nmos[{mos}]"])
            for mos in range(3)
        )
        _pmos_lays = tuple(
            layouter.inst_layout(inst=insts[f"pmos[{mos}]"])
            for mos in range(3)
        )
        _nmos_polybbs = tuple(
            _nmos_lay.bounds(mask=poly.mask) for _nmos_lay in _nmos_lays
        )
        _pmos_polybbs = tuple(
            _pmos_lay.bounds(mask=poly.mask) for _pmos_lay in _pmos_lays
        )

        y_nmos = 0.5*poly.min_space - _nmos_polybbs[0].bottom
        y_pmos = cell_height - 0.5*poly.min_space - _pmos_polybbs[0].top

        nmos_lays: List[_lay._Layout] = []
        nmos_actbbs: List[_geo.Rect] = []
        nmos_polybbs: List[_geo.Rect] = []
        pmos_lays: List[_lay._Layout] = []
        pmos_actbbs: List[_geo.Rect] = []
        pmos_polybbs: List[_geo.Rect] = []
        for mos in range(3):
            if mos == 0:
                x_nmos = (
                    chvssnact_actbb.right + cache.min_actpoly_space - _nmos_polybbs[mos].left
                )
                x_pmos = (
                    chvddpact_actbb.right + cache.min_actpoly_space - _pmos_polybbs[mos].left
                )
            else:
                x_nmos = (
                    nmos_polybbs[mos - 1].right + gate_space - _nmos_polybbs[mos].left
                )
                x_pmos = (
                    pmos_polybbs[mos - 1].right + gate_space - _pmos_polybbs[mos].left
                )

            lay = layouter.place(_nmos_lays[mos], x=x_nmos, y=y_nmos)
            actbb = lay.bounds(mask=active.mask)
            polybb = lay.bounds(mask=poly.mask)
            nmos_lays.append(lay)
            nmos_actbbs.append(actbb)
            nmos_polybbs.append(polybb)

            lay = layouter.place(_pmos_lays[mos], x=x_pmos, y=y_pmos)
            actbb = lay.bounds(mask=active.mask)
            polybb = lay.bounds(mask=poly.mask)
            pmos_lays.append(lay)
            pmos_actbbs.append(actbb)
            pmos_polybbs.append(polybb)
        assert (len(nmos_lays) == 3) and (len(pmos_lays) == 3), "Internal error"
        assert (len(nmos_actbbs) == 3) and (len(pmos_actbbs) == 3), "Internal error"
        assert (len(nmos_polybbs) == 3) and (len(pmos_polybbs) == 3), "Internal error"

        # wl_n
        _chwlnpact_lay = layouter.wire_layout(
            net=nets.wl_n, wire=contact, well_net=nwell_net,
            bottom=active, bottom_implant=pimplant, bottom_well=nwell,
            bottom_enclosure="wide", top_enclosure="wide",
        )
        _chwlnpact_actbb = _chwlnpact_lay.bounds(mask=active.mask)
        x_chwlnpact = tech.on_grid(0.5*(pmos_actbbs[0].right + pmos_actbbs[1].left))
        y_chwlnpact = pmos_actbbs[1].top - _chwlnpact_actbb.top
        chwlnpact_lay = layouter.place(_chwlnpact_lay, x=x_chwlnpact, y=y_chwlnpact)
        chwlnpact_m1bb1 = chwlnpact_lay.bounds(mask=metal1.mask)

        _chwlnpact_lay = layouter.wire_layout(
            net=nets.wl_n, wire=contact, well_net=nwell_net,
            bottom=active, bottom_implant=pimplant, bottom_well=nwell,
            bottom_height=pmos_actbbs[-1].height, bottom_enclosure="tall",
            top_enclosure="tall",
        )
        _chwlnpact_chbb = _chwlnpact_lay.bounds(mask=contact.mask)
        _chwlnnact_lay = layouter.wire_layout(
            net=nets.wl_n, wire=contact, well_net=pwell_net,
            bottom=active, bottom_implant=nimplant, bottom_well=pwell,
            bottom_height=nmos_actbbs[-1].height, bottom_enclosure="tall",
            top_enclosure="tall",
        )
        _chwlnnact_chbb = _chwlnnact_lay.bounds(mask=contact.mask)

        x_chwlnpact = (
            pmos_polybbs[-1].right + pmos.computed.min_contactgate_space
            - _chwlnpact_chbb.left
        )
        y_chwlnpact = pmos_actbbs[-1].center.y
        x_chwlnnact = (
            nmos_polybbs[-1].right + nmos.computed.min_contactgate_space
            - _chwlnnact_chbb.left
        )
        y_chwlnnact = nmos_actbbs[-1].center.y

        chwlnpact_lay = layouter.place(_chwlnpact_lay, x=x_chwlnpact, y=y_chwlnpact)
        chwlnpact_pimplbb = chwlnpact_lay.bounds(mask=pimplant.mask)
        chwlnpact_m1bb2 = chwlnpact_lay.bounds(mask=metal1.mask)
        chwlnnact_lay = layouter.place(_chwlnnact_lay, x=x_chwlnnact, y=y_chwlnnact)
        chwlnnact_nimplbb = chwlnnact_lay.bounds(mask=nimplant.mask)
        chwlnnact_m1bb = chwlnnact_lay.bounds(mask=metal1.mask)

        shape = _geo.Rect.from_rect(rect=chwlnnact_m1bb, top=chwlnpact_m1bb2.top)
        layouter.add_wire(net=nets.wl_n, wire=metal1, pin=metal1pin, shape=shape)
        shape = _geo.Rect.from_rect(rect=chwlnpact_m1bb1, right=chwlnpact_m1bb2.right)
        layouter.add_wire(net=nets.wl_n, wire=metal1, shape=shape)

        cell_width = max(
            max(chwlnpact_m1bb2.right, chwlnnact_m1bb.right) + metal1.min_space,
            chwlnpact_pimplbb.right + pimplant.min_space,
            chwlnnact_nimplbb.right + nimplant.min_space,
        )
        assert (round(cell_width/tech.grid)%2) == 0, "Not implemented"

        # vss/vdd
        shape = _geo.Rect.from_rect(rect=chvssnact_actbb, top=nmos_actbbs[0].top)
        layouter.add_wire(
            net=nets.vss, wire=active, well_net=pwell_net,
            implant=nimplant, well=pwell, shape=shape,
        )

        shape = _geo.Rect.from_rect(rect=chvddpact_actbb, bottom=pmos_actbbs[0].bottom)
        layouter.add_wire(
            net=nets.vdd, wire=active, well_net=nwell_net,
            implant=pimplant, well=nwell, shape=shape,
        )

        x_vdd = tech.on_grid(0.5*(pmos_actbbs[1].right + pmos_actbbs[2].left))
        lay = layouter.place(_chvddpact_lay, x=x_vdd, y=cell_height)
        actbb = lay.bounds(mask=active.mask)
        shape = _geo.Rect.from_rect(rect=actbb, bottom=pmos_actbbs[1].bottom)
        layouter.add_wire(
            net=nets.vdd, wire=active, well_net=nwell_net,
            implant=pimplant, well=nwell, shape=shape,
        )

        shape = _geo.Rect.from_rect(rect=chvssnact_m1bb, left=0.0, right=cell_width)
        layouter.add_wire(net=nets.vss, wire=metal1, shape=shape)
        shape = _geo.Rect.from_rect(rect=chvddpact_m1bb, left=0.0, right=cell_width)
        layouter.add_wire(net=nets.vdd, wire=metal1, shape=shape)

        layouter.add_wire(
            net=nets.vss, wire=via1, x=x_chvsspwell, y=0.0, rows=2,
            bottom_enclosure="tall", top_enclosure="tall",
        )
        via2vssrail_lay = layouter.add_wire(
            net=nets.vss, wire=via2, x=x_chvsspwell, y=0.0,
            bottom_enclosure="tall", top_enclosure="wide",
        )
        via2vssrail_m3bb=via2vssrail_lay.bounds(mask=metal3.mask)
        shape = _geo.Rect.from_rect(
            rect=via2vssrail_m3bb, left=0.0, right=cell_width,
        )
        layouter.add_wire(net=nets.vss, wire=metal3, pin=metal3pin, shape=shape)

        layouter.add_wire(
            net=nets.vdd, wire=via1, x=x_chvddnwell, y=cell_height, rows=2,
            bottom_enclosure="tall", top_enclosure="tall",
        )
        via2vddrail_lay = layouter.add_wire(
            net=nets.vdd, wire=via2, x=x_chvddnwell, y=cell_height,
            bottom_enclosure="tall", top_enclosure="wide",
        )
        via2vddrail_m3bb=via2vddrail_lay.bounds(mask=metal3.mask)
        shape =_geo.Rect.from_rect(
            rect=via2vddrail_m3bb, left=0.0, right=cell_width,
        )
        layouter.add_wire(net=nets.vdd, wire=metal3, pin=metal3pin, shape=shape)

        # gate nets
        m1pin_top = chwlnpact_m1bb1.bottom - metal1.min_space
        m1pin_bottom = chvssnact_m1bb.top + metal1.min_space
        for mos, net in enumerate((nets["pd[0]"], nets["pd[1]"], nets.wl_en)):
            nmos_polybb = nmos_polybbs[mos]
            pmos_polybb = pmos_polybbs[mos]
            if pmos_polybb.width < nmos_polybb.width:
                shape = _geo.Rect.from_rect(rect=pmos_polybb, bottom=nmos_polybb.top)
            else:
                shape = _geo.Rect.from_rect(rect=nmos_polybb, top=pmos_polybb.bottom)
            gate_lay = layouter.add_wire(net=net, wire=poly, shape=shape)
            gate_polybb = gate_lay.bounds(mask=poly.mask)

            if mos < 2:
                _chpad_lay = layouter.wire_layout(
                    net=net, wire=contact, bottom=poly, bottom_enclosure="wide",
                    top_enclosure="tall",
                )
                _chpad_polybb = _chpad_lay.bounds(mask=poly.mask)
                x_chpad = gate_polybb.right - _chpad_polybb.right
            else:
                _chpad_lay = layouter.wire_layout(
                    net=net, wire=contact, bottom=poly, bottom_enclosure="tall",
                    top_enclosure="tall",
                )
                _chpad_polybb = _chpad_lay.bounds(mask=poly.mask)
                # Move last pad as far as possible to the left in order
                # to avoid possible minimum metal1 space violation
                nmos_polybb2 = nmos_polybbs[mos - 1]
                pmos_polybb2 = pmos_polybbs[mos - 1]
                x_chpad = (
                    max(nmos_polybb2.right, pmos_polybb2.right) + poly.min_space
                    - _chpad_polybb.left
                )
            chpad_lay = layouter.place(_chpad_lay, x=x_chpad, y=y_chpad)
            chpad_m1bb = chpad_lay.bounds(mask=metal1.mask)

            shape = _geo.Rect.from_rect(
                rect=chpad_m1bb, bottom=m1pin_bottom, top=m1pin_top,
            )
            layouter.add_wire(net=net, wire=metal1, pin=metal1pin, shape=shape)

        # wells
        if nwell is not None:
            assert nwell_net is not None
            shape = layout.bounds(mask=nwell.mask)
            # TODO: More generic fixing of nwell shape
            if shape.left > -cache.min_actnwell_enclosure:
                shape = _geo.Rect.from_rect(rect=shape, left=-cache.min_actnwell_enclosure)
            if shape.right < (cell_width + nwell.min_width):
                shape = _geo.Rect.from_rect(
                    rect=shape, right=(cell_width + nwell.min_width),
                )
            layouter.add_wire(net=nwell_net, wire=nwell, shape=shape)
        if pwell is not None:
            assert pwell_net is not None
            shape = layout.bounds(mask=pwell.mask)
            # TODO: More generic fixing of nwell shape
            if shape.left > -cache.min_actpwell_enclosure:
                shape = _geo.Rect.from_rect(rect=shape, left=-cache.min_actpwell_enclosure)
            if shape.right < cell_width:
                shape = _geo.Rect.from_rect(rect=shape, right=cell_width)
            layouter.add_wire(net=pwell_net, wire=pwell, shape=shape)

        # nimplant/pimplant
        shape = _geo.Rect.from_rect(
            rect=chvssnact_nimplbb, right=chwlnnact_nimplbb.right,
            top=chwlnnact_nimplbb.top,
        )
        layouter.add_portless(prim=nimplant, shape=shape)
        shape = _geo.Rect.from_rect(
            rect=chvddpact_pimplbb, right=chwlnpact_pimplbb.right,
            # TODO: more generic solution for contact on polypad to implant spacing
            # bottom=chwlnpact_pimplbb.bottom,
            bottom=chwlnnact_nimplbb.top,
        )
        layouter.add_portless(prim=pimplant, shape=shape)

        # boundary
        self.set_size(width=cell_width, height=cell_height)


class _RowDecoderDrivePage(_FactoryCell["_SRAMFactory"]):
    def __init__(self, *,
        pds: int, rows: int, fab: "_SRAMFactory", name: str,
        wldriver_kwargs: Dict[str, Any],
    ):
        super().__init__(fab=fab, name=name)
        if pds != 2:
            raise NotImplementedError(f"pds {pds} != 2")
        if not _ispow2(rows):
            raise ValueError(f"rows has to be power of two; not {rows}")
        self.pds = pds
        self.rows = rows
        self.wldriver_kwargs = wldriver_kwargs

    def _create_circuit_nand3(self):
        fab = self.fab

        nand3_cell = fab.rowdecodernand3()
        drive_cell = fab.wordlinedriver(**self.wldriver_kwargs)

        ckt = self.new_circuit()

        nand3s = tuple(
            ckt.instantiate(nand3_cell, name=f"nand3[{row}]")
            for row in range(self.rows)
        )
        drivers = tuple(
            ckt.instantiate(drive_cell, name=f"drive[{row}]")
            for row in range(self.rows)
        )

        ckt.new_net(name="vss", external=True, childports=(
            inst.ports.vss for inst in (*nand3s, *drivers)
        ))
        ckt.new_net(name="vdd", external=True, childports=(
            inst.ports.vdd for inst in (*nand3s, *drivers)
        ))

        for row in range(self.rows):
            ckt.new_net(
                name=f"pd[0][{row}]", external=True, childports=nand3s[row].ports["pd[0]"],
            )
            ckt.new_net(name=f"wl_n[{row}]", external=False, childports=(
                nand3s[row].ports.wl_n, drivers[row].ports.wl_n,
            ))
            ckt.new_net(
                name=f"wl[{row}]", external=True, childports=drivers[row].ports.wl_drive,
            )

        ckt.new_net(name="pd[1]", external=True, childports=(
            nand3.ports["pd[1]"] for nand3 in nand3s
        ))
        ckt.new_net(name="wl_en", external=True, childports=(
            nand3.ports.wl_en for nand3 in nand3s
        ))

    def _create_layout_nand3(self):
        fab = self.fab
        tech = fab.tech
        cache = fab._cache

        nets = self.circuit.nets
        insts = self.circuit.instances

        metal1 = cache.metal(1)
        metal1pin = cache.metalpin(1)
        via1 = cache.via(1)
        metal2 = cache.metal(2)
        metal2pin = cache.metalpin(2)
        metal3 = cache.metal(3)
        metal3pin = cache.metalpin(3)

        layouter = self.new_circuitlayouter()
        layout = layouter.layout

        cell_height = self.rows * cache.bit_height

        x_nand3 = 0.0
        cell_width: Optional[float] = None
        for row in range(self.rows):
            if row%2 == 0:
                y_row = (row + 1)*cache.bit_height
                rot = _geo.Rotation.MX
            else: # odd row
                y_row = row*cache.bit_height
                rot = _geo.Rotation.R0

            nand3_lay = layouter.place(
                insts[f"nand3[{row}]"], x=x_nand3, y=y_row, rotation=rot,
            )
            nand3_bb = nand3_lay.boundary
            assert nand3_bb is not None

            _drive_lay = layouter.inst_layout(inst=insts[f"drive[{row}]"])
            _drive_bb = _drive_lay.boundary
            assert _drive_bb is not None
            x_drive = nand3_bb.right - _drive_bb.left
            drive_lay = layouter.place(
                _drive_lay, x=x_drive, y=y_row, rotation=rot,
            )
            if row == 0:
                drive_bb = drive_lay.boundary
                assert drive_bb is not None
                cell_width = drive_bb.right

            # pd[0]
            net = nets[f"pd[0][{row}]"]
            pd0_m1pinbb = nand3_lay.bounds(mask=metal1pin.mask, net=net, depth=1)
            layouter.add_wire(net=net, wire=metal1, pin=metal1pin, shape=pd0_m1pinbb)

            # pd[1], wl_en
            for net in (nets["pd[1]"], nets.wl_en):
                m1pinbb = nand3_lay.bounds(mask=metal1pin.mask, net=net, depth=1)
                layouter.add_wire(
                    net=net, wire=via1, origin=tech.on_grid(m1pinbb.center),
                    bottom_enclosure="tall", top_enclosure="tall",
                )

            # wl_n
            net = nets[f"wl_n[{row}]"]
            wlnnand3_m1pinbb = nand3_lay.bounds(mask=metal1pin.mask, net=net, depth=1)
            wlndrive_m1pinbb = drive_lay.bounds(mask=metal1pin.mask, net=net, depth=1)
            shape = _geo.Rect.from_rect(rect=wlndrive_m1pinbb, left=wlnnand3_m1pinbb.left)
            layouter.add_wire(net=net, wire=metal1, shape=shape)

            # wl
            net = nets[f"wl[{row}]"]
            m3pinbb = drive_lay.bounds(mask=metal3pin.mask, net=net, depth=1)
            layouter.add_wire(net=net, wire=metal3, pin=metal3pin, shape=m3pinbb)

            # vss/vdd
            if row%2 == 0 or (row == (self.rows - 1)):
                vddnand3_m3pinbb = nand3_lay.bounds(
                    mask=metal3pin.mask, net=nets.vdd, depth=1,
                )
                vdddrive_m3pinbb = drive_lay.bounds(
                    mask=metal3pin.mask, net=nets.vdd, depth=1,
                )
                d = abs(vddnand3_m3pinbb.center.y - vdddrive_m3pinbb.center.y)
                assert d < _geo.epsilon, "Unsupported vdd layout"
                shape = _geo.Rect.from_rect(
                    rect=vddnand3_m3pinbb, right=vdddrive_m3pinbb.right,
                )
                layouter.add_wire(net=nets.vdd, wire=metal3, pin=metal3pin, shape=shape)
            if row%2 == 1:
                vssnand3_m3pinbb = nand3_lay.bounds(
                    mask=metal3pin.mask, net=nets.vss, depth=1,
                )
                vssdrive_m3pinbb = drive_lay.bounds(
                    mask=metal3pin.mask, net=nets.vss, depth=1,
                )
                d = abs(vssnand3_m3pinbb.center.y - vssdrive_m3pinbb.center.y)
                if d < _geo.epsilon:
                    shape = _geo.Rect.from_rect(
                        rect=vssnand3_m3pinbb, right=vssdrive_m3pinbb.right,
                    )
                    layouter.add_wire(net=nets.vss, wire=metal3, pin=metal3pin, shape=shape)
                else:
                    assert (
                        vssdrive_m3pinbb.bottom > vssnand3_m3pinbb.top
                    ), "Unsupported vss layout"
                    y = vssnand3_m3pinbb.center.y
                    w = vssnand3_m3pinbb.height
                    bottom2 = 2*y - vssdrive_m3pinbb.top
                    top2 = 2*y - vssdrive_m3pinbb.bottom
                    shape = _geo.Polygon.from_floats(points=(
                        (vssnand3_m3pinbb.left, vssnand3_m3pinbb.bottom),
                        (vssnand3_m3pinbb.left, vssnand3_m3pinbb.top),
                        (vssdrive_m3pinbb.left, vssnand3_m3pinbb.top),
                        (vssdrive_m3pinbb.left, vssdrive_m3pinbb.top),
                        (vssdrive_m3pinbb.right, vssdrive_m3pinbb.top),
                        (vssdrive_m3pinbb.right, vssdrive_m3pinbb.bottom),
                        (vssdrive_m3pinbb.left + w, vssdrive_m3pinbb.bottom),
                        (vssdrive_m3pinbb.left + w, top2),
                        (vssdrive_m3pinbb.right, top2),
                        (vssdrive_m3pinbb.right, bottom2),
                        (vssdrive_m3pinbb.left, bottom2),
                        (vssdrive_m3pinbb.left, vssnand3_m3pinbb.bottom),
                        (vssnand3_m3pinbb.left, vssnand3_m3pinbb.bottom),
                    ))
                    layouter.add_wire(net=nets.vss, wire=metal3, shape=shape)
                    layouter.add_wire(
                        net=nets.vss, wire=metal3, pin=metal3pin, shape=vssnand3_m3pinbb,
                    )
        assert cell_width is not None

        # pd[1]/wl_en pt.2
        for net in (nets["pd[1]"], nets.wl_en):
            m2bb = layout.bounds(mask=metal2.mask, net=net, depth=1)
            layouter.add_wire(net=net, wire=metal2, pin=metal2pin, shape=m2bb)

        # boundary
        self.set_size(width=cell_width, height=cell_height)

    def _create_circuit(self):
        assert self.pds == 2, "Internal error"
        self._create_circuit_nand3()

    def _create_layout(self):
        assert self.pds == 2, "Internal error"
        self._create_layout_nand3()


class _RowPreDecoders(_FactoryCell["_SRAMFactory"]):
    def __init__(self, *,
        address_groups: Tuple[int, ...], fab: "_SRAMFactory", name: str,
    ):
        super().__init__(fab=fab, name=name)
        if len(address_groups) != 2:
            raise NotImplementedError("number of predecs (e.g len(bits)) != 2")
        if (address_groups[0] != 3) or (address_groups[1] != 4):
            raise NotImplementedError("bits[0] != 3 or bits[1] != 4")
        self.address_groups = address_groups
        self.lines = tuple(2**bit for bit in address_groups)

    def _create_circuit(self):
        fab = self.fab
        spec = fab.spec

        stdcells = spec.stdcelllib.cells
        ff_cell = stdcells.sff1_x4
        inv_cell = stdcells.inv_x1
        and3_cell = stdcells.a3_x2
        and4_cell = stdcells.a4_x2

        ckt = self.new_circuit()

        abits = sum(self.address_groups)

        affs = tuple(
            ckt.instantiate(ff_cell, name=f"aff[{abit}]")
            for abit in range(abits)
        )
        ainvs = tuple(
            ckt.instantiate(inv_cell, name=f"ainv[{abit}]")
            for abit in range(abits)
        )

        pd0_ands = tuple(
            ckt.instantiate(and3_cell, name=f"pd[0]and[{pd0_line}]")
            for pd0_line in range(self.lines[0])
        )
        pd1_ands = tuple(
            ckt.instantiate(and4_cell, name=f"pd[1]and[{pd1_line}]")
            for pd1_line in range(self.lines[1])
        )

        ckt.new_net(name="vss", external=True, childports=(
            inst.ports.vss for inst in (*affs, *ainvs, *pd0_ands, *pd1_ands)
        ))
        ckt.new_net(name="vdd", external=True, childports=(
            inst.ports.vdd for inst in (*affs, *ainvs, *pd0_ands, *pd1_ands)
        ))

        ckt.new_net(name="clk", external=True, childports=(
            aff.ports.ck for aff in affs
        ))

        for abit in range(abits):
            ckt.new_net(name=f"a[{abit}]", external=True, childports=affs[abit].ports.i)

            # Get input ports of ands connected to aint and aint_n signal
            if abit < self.address_groups[0]:
                a_ports = tuple(
                    pd0_ands[pd0_line].ports[f"i{abit}"]
                    for pd0_line in filter(
                        # Is bit abit set ?
                        lambda i: (i & (1<<abit)) != 0, range(self.lines[0])
                    )
                )
                an_ports = tuple(
                    pd0_ands[pd0_line].ports[f"i{abit}"]
                    for pd0_line in filter(
                        # Is bit abit not set ?
                        lambda i: (i & (1<<abit)) == 0, range(self.lines[0])
                    )
                )
            else:
                abit2 = abit - self.address_groups[0]
                a_ports = tuple(
                    pd1_ands[pd1_line].ports[f"i{abit2}"]
                    for pd1_line in filter(
                        # Is bit abit set ?
                        lambda i: (i & (1<<abit2)) != 0, range(self.lines[1])
                    )
                )
                an_ports = tuple(
                    pd1_ands[pd1_line].ports[f"i{abit2}"]
                    for pd1_line in filter(
                        # Is bit abit not set ?
                        lambda i: (i & (1<<abit2)) == 0, range(self.lines[1])
                    )
                )
            ckt.new_net(name=f"aint[{abit}]", external=False, childports=(
                affs[abit].ports.q, ainvs[abit].ports.i, *a_ports,
            ))
            ckt.new_net(name=f"aint_n[{abit}]", external=False, childports=(
                ainvs[abit].ports.nq, *an_ports,
            ))

        for pd0_line in range(self.lines[0]):
            ckt.new_net(name=f"pd[0][{pd0_line}]", external=True, childports=(
                pd0_ands[pd0_line].ports.q,
            ))
        for pd1_line in range(self.lines[1]):
            ckt.new_net(name=f"pd[1][{pd1_line}]", external=True, childports=(
                pd1_ands[pd1_line].ports.q,
            ))

    def _create_layout(self):
        fab = self.fab
        tech = fab.tech
        spec = fab.spec
        cache = fab._cache

        abits = sum(self.address_groups)
        wordlines = self.lines[0]*self.lines[1]

        ckt = self.circuit
        nets = ckt.nets
        insts = ckt.instances

        metal1 = cache.metal(1)
        metal1pin = cache.metalpin(1)
        via1 = cache.via(1)
        metal2 = cache.metal(2)
        metal2pin = cache.metalpin(2)
        via2 = cache.via(2)
        metal3 = cache.metal(3)

        layouter = self.new_circuitlayouter()
        layout = layouter.layout

        page_width = self.lines[0]*cache.bit_height
        cell_width = wordlines*cache.bit_height

        stdcells = spec.stdcelllib.cells

        tie_cell = stdcells.tie_diff_w4
        tie_bb = tie_cell.layout.boundary
        assert tie_bb is not None
        ties = 0

        m2connwidth = tech.computed.min_width(
            primitive=metal2, down=True, up=True, min_enclosure=True,
        )
        m2connpitch = tech.computed.min_pitch(
            primitive=metal2, down=True, up=True, min_enclosure=True,
        )

        # vss/vdd
        # Take vss/vdd from the inv
        fill_lay = stdcells.fill.layout
        fill_bb = fill_lay.boundary
        assert fill_bb is not None

        vssfill_m1pinbb = fill_lay.bounds(mask=metal1pin.mask, net=nets.vss, depth=1)
        shape = _geo.Rect.from_rect(rect=vssfill_m1pinbb, right=cell_width)
        layouter.add_wire(net=nets.vss, wire=metal1, pin=metal1pin, shape=shape)
        shape = _geo.Rect.from_rect(
            rect=_geo.Rotation.MX*vssfill_m1pinbb, right=cell_width,
        )
        layouter.add_wire(net=nets.vss, wire=metal1, pin=metal1pin, shape=shape)

        vddfill_m1pinbb = fill_lay.bounds(mask=metal1pin.mask, net=nets.vdd, depth=1)
        shape = _geo.Rect.from_rect(rect=vddfill_m1pinbb, right=cell_width)
        layouter.add_wire(net=nets.vdd, wire=metal1, pin=metal1pin, shape=shape)
        shape = _geo.Rect.from_rect(
            rect=_geo.Rotation.MX*vddfill_m1pinbb, right=cell_width,
        )
        layouter.add_wire(net=nets.vdd, wire=metal1, pin=metal1pin, shape=shape)

        # Place ffs and inverters
        x_top = 0.0
        for abit in range(abits):
            aff_lay = layouter.place(insts[f"aff[{abit}]"], x=x_top, y=0.0)
            aff_bb = aff_lay.boundary
            assert aff_bb is not None
            x_top = aff_bb.right

            ainv_lay = layouter.place(insts[f"ainv[{abit}]"], x=x_top, y=0.0)
            ainv_bb = ainv_lay.boundary
            assert ainv_bb is not None
            x_top = ainv_bb.right

        # Fill up bottom row with tie cells
        while (x_top + tie_bb.width + _geo.epsilon) < cell_width:
            tie_inst = ckt.instantiate(tie_cell, name=f"tie[{ties}]")
            ties += 1
            tie_lay = layouter.place(tie_inst, x=x_top, y=0.0)
            tie_bb = tie_lay.boundary
            assert tie_bb is not None
            x_top = tie_bb.right

        # Place the and cells of the pre decoders
        x_bottom = 0.0
        assert self.address_groups[1] == 4, "Internal error"
        and4_cell = stdcells.a4_x2
        and4_nets = and4_cell.circuit.nets
        and4_lay = and4_cell.layout
        qand4_m1pinbb = and4_lay.bounds(mask=metal1pin.mask, net=and4_nets.q, depth=1)
        pd1_line = 0
        for pd0_line in range(self.lines[0]):
            # Put pd[1] and cell close to middle of the page
            if (x_bottom + qand4_m1pinbb.center.x) > (pd1_line + 0.5)*page_width:
                pd1and_lay = layouter.place(
                    insts[f"pd[1]and[{pd1_line}]"], x=x_bottom, y=0.0,
                    rotation=_geo.Rotation.MX,
                )
                pd1and_bb = pd1and_lay.boundary
                assert pd1and_bb is not None
                x_bottom = pd1and_bb.right
                pd1_line += 1

            pd0and_lay = layouter.place(
                insts[f"pd[0]and[{pd0_line}]"], x=x_bottom, y=0.0, rotation=_geo.Rotation.MX,
            )
            pd0and_bb = pd0and_lay.boundary
            assert pd0and_bb is not None
            x_bottom = pd0and_bb.right
        self.x_topand0 = x_bottom

        # Fill up bottom row with tie cells
        while  (x_bottom + tie_bb.width + _geo.epsilon) < cell_width:
            # Put pd[1] and cell close to middle of the page
            if (x_bottom + qand4_m1pinbb.center.x) > (pd1_line + 0.5)*page_width:
                pd1and_lay = layouter.place(
                    insts[f"pd[1]and[{pd1_line}]"], x=x_bottom, y=0.0,
                    rotation=_geo.Rotation.MX,
                )
                pd1and_bb = pd1and_lay.boundary
                assert pd1and_bb is not None
                x_bottom = pd1and_bb.right
                pd1_line += 1

            tie_inst = ckt.instantiate(tie_cell, name=f"tie[{ties}]")
            ties += 1
            tie_lay = layouter.place(
                tie_inst, x=x_bottom, y=0.0, rotation=_geo.Rotation.MX,
            )
            tie_bb = tie_lay.boundary
            assert tie_bb is not None
            x_bottom = tie_bb.right

        # Connect vss/vdd of tie cells
        nets.vss.childports += (
            insts[f"tie[{tie}]"].ports.vss for tie in range(ties)
        )
        nets.vdd.childports += (
            insts[f"tie[{tie}]"].ports.vdd for tie in range(ties)
        )

        # Compute y for the different lines
        # Use dummy layouts that are not placed
        _ff_lay = layouter.inst_layout(inst=insts["aff[0]"])
        _iff_m1pinbb = _ff_lay.bounds(mask=metal1pin.mask, net=nets["a[0]"], depth=1)
        _via1_lay = layouter.wire_layout(
            net=nets["a[0]"], wire=via1, bottom_enclosure="tall", top_enclosure="wide"
        )
        _via1_m1bb = _via1_lay.bounds(mask=metal1.mask)
        y_a = _iff_m1pinbb.top - _via1_m1bb.top
        y_clk = y_a - m2connpitch
        y_aint = tuple(y_clk - (abit + 1)*m2connpitch for abit in range(abits))
        y_aintn = tuple(y_clk - (abits + abit + 1)*m2connpitch for abit in range(abits))
        assert y_aintn[-1] > (_iff_m1pinbb.bottom - _via1_m1bb.bottom), "Not implemented"
        # shuffle coordinates to reduce parasitic capacitance
        assert abits == 7, "Internal error"
        shuffle = (3, 0, 4, 1, 5, 2, 6)
        y_aint = tuple(y_aint[i] for i in shuffle)
        y_aintn = tuple(y_aintn[i] for i in shuffle)

        # clk
        x_right = 0.0
        net = nets.clk
        for m1pinms in layout.filter_polygons(
            net=net, mask=metal1pin.mask, depth=1, split=True,
        ):
            m1pinbb = m1pinms.shape.bounds
            x_via1 = m1pinbb.center.x
            layouter.add_wire(
                net=net, wire=via1, x=x_via1, y=y_clk,
                bottom_enclosure="tall", top_enclosure="wide",
            )
            x_right = max(x_right, x_via1)
        shape = _geo.Rect(
            left=0.0, bottom=(y_clk - 0.5*m2connwidth),
            right=x_right, top=(y_clk + 0.5*m2connwidth),
        )
        layouter.add_wire(net=net, wire=metal2, pin=metal2pin, shape=shape)

        # a/aint/aint_n
        for abit in range(abits):
            # a
            net = nets[f"a[{abit}]"]
            m1pinbb = layout.bounds(net=net, mask=metal1pin.mask, depth=2)
            via1_lay = layouter.add_wire(
                net=net, wire=via1, x=m1pinbb.center.x, y=y_a,
                bottom_enclosure="tall", top_enclosure="wide",
            )
            via1_m2bb = via1_lay.bounds(mask=metal2.mask)
            shape = _geo.Rect.from_rect(rect=via1_m2bb, top=fill_bb.top)
            layouter.add_wire(net=net, wire=metal2, pin=metal2pin, shape=shape)

            # aint/aint_n
            y_and_i = 0.0
            for net, y_via1 in (
                (nets[f"aint[{abit}]"], y_aint[abit]),
                (nets[f"aint_n[{abit}]"], y_aintn[abit]),
            ):
                x_left = cell_width
                x_right = 0.0
                for m1pinms in layout.filter_polygons(
                    net=net, mask=metal1pin.mask, depth=1, split=True,
                ):
                    m1pinbb = m1pinms.shape.bounds
                    x_via1 = m1pinbb.center.x

                    if m1pinbb.center.y > 0.0: # On top row
                        layouter.add_wire(
                            net=net, wire=via1, x=x_via1, y=y_via1,
                            bottom_enclosure="tall", top_enclosure="wide",
                        )
                    else:
                        _via1_lay = layouter.wire_layout(
                            net=net, wire=via1,
                            bottom_enclosure="tall", top_enclosure="wide",
                        )
                        _via1_m1bb = _via1_lay.bounds(mask=metal1.mask)
                        y_via1_2 = m1pinbb.top - _via1_m1bb.top
                        y_and_i = min(y_and_i, y_via1_2)
                        via1_lay = layouter.place(_via1_lay, x=x_via1, y=y_via1_2)
                        via1_m2bb = via1_lay.bounds(mask=metal2.mask)

                        _via2_lay = layouter.wire_layout(
                            net=net, wire=via2, rows=2,
                            bottom_enclosure="tall", top_enclosure="tall",
                        )
                        _via2_m2bb = _via2_lay.bounds(mask=metal2.mask)
                        x_via2 = x_via1
                        y_via2 = via1_m2bb.bottom - _via2_m2bb.bottom
                        via2_lay = layouter.place(_via2_lay, x=x_via2, y=y_via2)
                        via2_m3bb = via2_lay.bounds(mask=metal3.mask)

                        shape = _geo.Rect.from_rect(rect=via2_m3bb, top=y_via1)
                        layouter.add_wire(net=net, wire=metal3, shape=shape)

                        layouter.add_wire(
                            net=net, wire=via2, columns=2, x=x_via1, y=y_via1,
                            bottom_enclosure="wide", top_enclosure="wide",
                        )

                    x_left = min(x_left, m1pinbb.center.x)
                    x_right = max(x_right, m1pinbb.center.x)
                shape = _geo.Rect(
                    left=x_left, bottom=(y_via1 - 0.5*m2connwidth),
                    right=x_right, top=(y_via1 + 0.5*m2connwidth),
                )
                layouter.add_wire(net=net, wire=metal2, shape=shape)

        # pd[n][m]
        for pd, lines in enumerate(self.lines):
            for line in range(lines):
                net = nets[f"pd[{pd}][{line}]"]
                m1pinbb = layout.bounds(net=net, mask=metal1pin.mask, depth=2)
                layouter.add_wire(net=net, wire=metal1, pin=metal1pin, shape=m1pinbb)

        # boundary
        self.set_boundary(
            bb=_geo.Rect(left=0.0, bottom=-fill_bb.top, right=cell_width, top=fill_bb.top),
        )


class _RowDecoder(_FactoryCell["_SRAMFactory"]):
    def __init__(self, *,
        address_groups: Tuple[int, ...], reverse: bool, page_kwargs: Dict[str, Any],
        fab: "_SRAMFactory", name: str,
    ):
        super().__init__(fab=fab, name=name)
        if len(address_groups) != 2:
            raise NotImplementedError("number of predecs (e.g len(bits)) != 2")
        if (address_groups[0] != 3) or (address_groups[1] != 4):
            raise NotImplementedError("bits[0] != 3 or bits[1] != 4")
        self.address_groups = address_groups
        self.reverse = reverse
        self.page_kwargs = page_kwargs

    def _create_circuit(self):
        fab = self.fab

        ckt = self.new_circuit()

        pds = len(self.address_groups)

        abits = sum(self.address_groups)

        predec_cell = fab.rowpredecoders(address_groups=self.address_groups)
        (pagerows, pages) = predec_cell.lines
        rows = pages*pagerows
        page_cell = fab.rowdecoderdrivepage(pds=pds, rows=pagerows, **self.page_kwargs)

        predec = ckt.instantiate(predec_cell, name="predec")
        pagedrives = tuple(
            ckt.instantiate(page_cell, name=f"page[{page}]")
            for page in range(predec_cell.lines[1])
        )

        ckt.new_net(name="vss", external=True, childports=(
            inst.ports.vss for inst in (predec, *pagedrives)
        ))
        ckt.new_net(name="vdd", external=True, childports=(
            inst.ports.vdd for inst in (predec, *pagedrives)
        ))

        for abit in range(abits):
            net_name = f"a[{abit}]"
            ckt.new_net(name=net_name, external=True, childports=predec.ports[net_name])

        ckt.new_net(name="clk", external=True, childports=predec.ports.clk)

        ckt.new_net(name="wl_en", external=True, childports=(
            pagedrive.ports.wl_en for pagedrive in pagedrives
        ))

        for pagerow in range(pagerows):
            net_name = f"pd[0][{pagerow}]"
            ckt.new_net(name=net_name, external=False, childports=(
                predec.ports[net_name], *(page.ports[net_name] for page in pagedrives),
            ))
        for page in range(pages):
            net_name = f"pd[1][{page}]"
            ckt.new_net(name=net_name, external=False, childports=(
                predec.ports[net_name], pagedrives[page].ports["pd[1]"],
            ))
        for row in range(rows):
            page = row//pagerows
            pagerow = row%pagerows
            ckt.new_net(
                name=f"wl[{row}]", external=True,
                childports=pagedrives[page].ports[f"wl[{pagerow}]"],
            )

    def _create_layout(self):
        fab = self.fab
        tech = fab.tech
        cache = fab._cache

        nets = self.circuit.nets
        insts = self.circuit.instances

        nwell = cache.nwell
        active = cache.active
        metal1 = cache.metal(1)
        metal1pin = cache.metalpin(1)
        via1 = cache.via(1)
        metal2 = cache.metal(2)
        metal2pin = cache.metalpin(2)
        via2 = cache.via(2)
        metal3 = cache.metal(3)
        metal3pin = cache.metalpin(3)

        layouter = self.new_circuitlayouter()
        layout = layouter.layout

        m2connwidth = tech.computed.min_width(
            primitive=metal2, down=True, up=True, min_enclosure=True,
        )
        # Use two times min space to decrease parasitic capacitance
        m2connpitch = tech.computed.min_pitch(
            primitive=metal2, down=True, up=True, min_enclosure=True,
        ) + metal2.min_space

        _predec_inst = cast(_ckt._CellInstance, insts.predec)
        _predec_cell = cast(_RowPreDecoders, _predec_inst.cell)
        (pagerows, pages) = _predec_cell.lines
        rows = pages*pagerows
        abits = sum(self.address_groups)

        page_height = pagerows*cache.bit_height
        cell_height = rows*cache.bit_height

        _predec_lay = layouter.inst_layout(inst=_predec_inst)
        _predec_nwellbb = _predec_lay.bounds(mask=nwell.mask)
        _predec_bb = _predec_lay.boundary
        assert _predec_bb is not None
        y_topand0 = _predec_cell.x_topand0

        x_predec = _predec_bb.top
        y_predec = -_predec_bb.left
        predec_lay = layouter.place(
            _predec_lay, x=x_predec, y=y_predec, rotation=_geo.Rotation.R90,
        )
        # TODO: Fix nweel bounds computation
        # predec_nwellbb = predec_lay.bounds(mask=nwell.mask)
        predec_m2bb = predec_lay.bounds(mask=metal2.mask)
        predec_bb = predec_lay.boundary
        assert predec_bb is not None

        if not self.reverse:
            _page0_lay = layouter.inst_layout(inst=insts["page[0]"])
            _page0_actbb = _page0_lay.bounds(mask=active.mask)
            _page0_bb = _page0_lay.boundary
            assert _page0_bb is not None
            x_page = max(
                predec_bb.right - _page0_bb.left + metal1.min_space,
                x_predec - _predec_nwellbb.bottom + cache.min_actpwell_enclosure
                - _page0_actbb.left,
            )

            y_page = -_page0_bb.bottom
            page_lays = tuple(
                layouter.place(
                    insts[f"page[{page}]"], x=x_page, y=(y_page + page*page_height)
                ) for page in range(pages)
            )
            bottompage_lay = page_lays[0]
        else: # Reverse row order
            _page0_lay = layouter.inst_layout(
                inst=insts["page[0]"], rotation=_geo.Rotation.MX,
            )
            _page0_actbb = _page0_lay.bounds(mask=active.mask)
            _page0_bb = _page0_lay.boundary
            assert _page0_bb is not None
            x_page = max(
                predec_bb.right - _page0_bb.left + metal1.min_space,
                x_predec - _predec_nwellbb.bottom + cache.min_actpwell_enclosure
                - _page0_actbb.left,
            )

            y_page = -_page0_bb.top + pages*page_height
            page_lays = tuple(
                layouter.place(
                    insts[f"page[{page}]"], rotation=_geo.Rotation.MX,
                    x=x_page, y=(y_page - page*page_height)
                ) for page in range(pages)
            )
            bottompage_lay = page_lays[-1]

        # cell_width
        page0_bb = bottompage_lay.boundary
        assert page0_bb is not None
        cell_width = page0_bb.right

        # vss/vdd
        # Get m1 stripes of the predecoders
        predec_vssm1pinbbs = tuple(
            cast(_geo.Rect, ms.shape.bounds)
            for ms in predec_lay.filter_polygons(
                mask=metal1pin.mask, net=nets.vss, depth=1, split=True,
            )
        )
        predec_vddm1pinbbs = tuple(
            cast(_geo.Rect, ms.shape.bounds)
            for ms in predec_lay.filter_polygons(
                mask=metal1pin.mask, net=nets.vdd, depth=1, split=True,
            )
        )

        # Get top m3 stripes of first page
        page0_topvss_m3pinbb: Optional[_geo.Rect] = None
        page0_topvdd_m3pinbb: Optional[_geo.Rect] = None
        for vssm3pinms in bottompage_lay.filter_polygons(
            mask=metal3pin.mask, net=nets.vss, depth=1, split=True,
        ):
            vssm3pinbb = cast(_geo.Rect, vssm3pinms.shape.bounds)
            if (
                (page0_topvss_m3pinbb is None)
                or (vssm3pinbb.center.y > page0_topvss_m3pinbb.center.y)
            ):
                page0_topvss_m3pinbb = vssm3pinbb
        for vddm3pinms in bottompage_lay.filter_polygons(
            mask=metal3pin.mask, net=nets.vdd, depth=1, split=True,
        ):
            vddm3pinbb = cast(_geo.Rect, vddm3pinms.shape.bounds)
            if (
                (page0_topvdd_m3pinbb is None)
                or (vddm3pinbb.center.y > page0_topvdd_m3pinbb.center.y)
            ):
                page0_topvdd_m3pinbb = vddm3pinbb
        assert page0_topvss_m3pinbb is not None
        assert page0_topvdd_m3pinbb is not None
        # Stretch stipes to left of cell
        page0_topvss_m3pinbb = _geo.Rect.from_rect(
            rect=page0_topvss_m3pinbb, left=0.0,
        )
        page0_topvdd_m3pinbb = _geo.Rect.from_rect(
            rect=page0_topvdd_m3pinbb, left=0.0,
        )

        # Don't stretch vss/vdd where there are and cells of the first
        # predecoder(s)
        firstpage = floor(y_topand0/page_height) + 1
        assert (firstpage < pages), "Not implemented"
        for page in range(firstpage, pages):
            dxy = _geo.Point(x=0.0, y=page*page_height)
            vss_m3shape = page0_topvss_m3pinbb + dxy
            layouter.add_wire(net=nets.vss, wire=metal3, pin=metal3pin, shape=vss_m3shape)
            vdd_m3shape = page0_topvdd_m3pinbb + dxy
            layouter.add_wire(net=nets.vdd, wire=metal3, pin=metal3pin, shape=vdd_m3shape)

            h = vss_m3shape.height
            y = vss_m3shape.center.y
            for m1pinbb in predec_vssm1pinbbs:
                w = m1pinbb.width
                x = m1pinbb.center.x
                layouter.add_wire(
                    net=nets.vss, wire=via1, x=x, y=y,
                    bottom_width=w, bottom_height=h, bottom_enclosure="wide",
                    top_width=w, top_height=h, top_enclosure="wide",
                )
                layouter.add_wire(
                    net=nets.vss, wire=via2, x=x, y=y,
                    bottom_width=w, bottom_height=h, bottom_enclosure="wide",
                    top_width=w, top_height=h, top_enclosure="wide",
                )

            h = vdd_m3shape.height
            y = vdd_m3shape.center.y
            for m1pinbb in predec_vddm1pinbbs:
                w = m1pinbb.width
                x = m1pinbb.center.x
                layouter.add_wire(
                    net=nets.vdd, wire=via1, x=x, y=y,
                    bottom_width=w, bottom_height=h, bottom_enclosure="wide",
                    top_width=w, top_height=h, top_enclosure="wide",
                )
                layouter.add_wire(
                    net=nets.vdd, wire=via2, x=x, y=y,
                    bottom_width=w, bottom_height=h, bottom_enclosure="wide",
                    top_width=w, top_height=h, top_enclosure="wide",
                )

        # a[n]
        for abit in range(abits):
            net = nets[f"a[{abit}]"]
            m2pinbb = predec_lay.bounds(mask=metal2pin.mask, net=net, depth=1)
            layouter.add_wire(net=net, wire=metal2, pin=metal2pin, shape=m2pinbb)

        # clk
        net = nets.clk
        m2pinbb = layout.bounds(mask=metal2pin.mask, net=net, depth=1)
        shape = _geo.Rect.from_rect(rect=m2pinbb, bottom=0.0)
        layouter.add_wire(net=net, wire=metal2, pin=metal2pin, shape=shape)

        # wl_en
        net = nets.wl_en
        m2pinbb = layout.bounds(mask=metal2pin.mask, net=net, depth=1)
        shape = _geo.Rect.from_rect(rect=m2pinbb, bottom=0.0)
        layouter.add_wire(net=net, wire=metal2, pin=metal2pin, shape=shape)

        # wl[n]
        for row in range(rows):
            net = nets[f"wl[{row}]"]
            m3pinbb = layout.bounds(mask=metal3pin.mask, net=net, depth=1)
            layouter.add_wire(net=net, wire=metal3, pin=metal3pin, shape=m3pinbb)

        # pd[0][n]
        x_pd0 = tuple(
            predec_m2bb.right + (pagerow + 1)*m2connpitch
            for pagerow in range(pagerows)
        )
        assert (x_pd0[-1] + m2connpitch) < x_page
        # shuffle to allow little smaller capacitance
        assert _predec_cell.lines[0] == 8, "Internal error"
        x_pd0 = tuple(
            x_pd0[i] for i in (0, 4, 1, 5, 2, 6, 3, 7)
        )
        for pagerow in range(pagerows):
            x_via1 = x_pd0[pagerow]
            net = nets[f"pd[0][{pagerow}]"]
            y_bottom = cell_height
            y_top = 0.0
            for m1pinms in layout.filter_polygons(
                net=net, mask=metal1pin.mask, depth=1, split=True,
            ):
                m1pinbb = m1pinms.shape.bounds

                x_via1_2 = m1pinbb.center.x
                y_via1 = tech.on_grid(m1pinbb.center.y)

                if x_via1_2 < predec_bb.right:
                    layouter.add_wire(
                        net=net, wire=via1, x=x_via1, y=y_via1,
                        bottom_enclosure="tall", top_enclosure="tall",
                    )
                else:
                    layouter.add_wire(
                        net=net, wire=via1, rows=2, x=x_via1_2, y=y_via1,
                        bottom_enclosure="tall", top_enclosure="tall",
                    )
                    via2_lay = layouter.add_wire(
                        net=net, wire=via2, rows=2, x=x_via1_2, y=y_via1,
                        bottom_enclosure="tall", top_enclosure="tall",
                    )
                    via2_m3bb1 = via2_lay.bounds(mask=metal3.mask)
                    via2_lay = layouter.add_wire(
                        net=net, wire=via2, rows=2, x=x_via1, y=y_via1,
                        bottom_enclosure="tall", top_enclosure="tall",
                    )
                    via2_m3bb2 = via2_lay.bounds(mask=metal3.mask)
                    shape = _geo.Rect.from_rect(rect=via2_m3bb1, left=via2_m3bb2.left)
                    layouter.add_wire(net=net, wire=metal3, shape=shape)
                y_bottom = min(y_bottom, y_via1)
                y_top = max(y_top, y_via1)
            shape = _geo.Rect(
                left=(x_via1 - 0.5*m2connwidth), bottom=y_bottom,
                right=(x_via1 + 0.5*m2connwidth), top=y_top,
            )
            layouter.add_wire(net=net, wire=metal2, shape=shape)

        # pd[1][n]
        for page, page_lay in enumerate(page_lays):
            net = nets[f"pd[1][{page}]"]

            dec_m1pinbb = predec_lay.bounds(mask=metal1pin.mask, net=net, depth=1)
            page_m2pinbb = page_lay.bounds(mask=metal2pin.mask, net=net, depth=1)

            _via1_lay = layouter.wire_layout(
                net=net, wire=via1,
                bottom_enclosure="wide", top_enclosure="tall",
            )
            _via1_m1bb = _via1_lay.bounds(mask=metal1.mask)

            x_via1 = dec_m1pinbb.right - _via1_m1bb.right
            y_via1 = dec_m1pinbb.center.y
            via1_lay = layouter.place(_via1_lay, x=x_via1, y=y_via1)
            via1_m2bb = via1_lay.bounds(mask=metal2.mask)

            # TODO: More generic solution to avoid metal2 DRC violations
            # with the vdd contact
            bottom = tech.on_grid(page_m2pinbb.center.y + 1.5*m2connpitch)
            top = bottom + m2connwidth
            if bottom < via1_m2bb.bottom:
                shape = _geo.Rect.from_rect(rect=via1_m2bb, bottom=bottom)
            else:
                shape = _geo.Rect.from_rect(rect=via1_m2bb, top=top)
            layouter.add_wire(net=net, wire=metal2, shape=shape)
            shape = _geo.Rect(
                left=via1_m2bb.left, bottom=bottom, right=page_m2pinbb.right, top=top,
            )
            layouter.add_wire(net=net, wire=metal2, shape=shape)

        # wells
        # TODO: Fix hacky nwell shape fix
        if nwell is not None:
            right = x_predec - _predec_nwellbb.bottom
            bottom = min(
                0.0, y_predec + _predec_nwellbb.left - nwell.min_width
            )
            top = max(
                cell_height, y_predec + _predec_nwellbb.left + nwell.min_width
            )
            shape = _geo.Rect(
                left=(right - nwell.min_width), bottom=bottom,
                right=right, top=top,
            )
            layouter.add_wire(net=nets.vdd, wire=nwell, shape=shape)
        assert cache.pwell is None, "Not implamented"
        # boundary
        self.set_size(width=cell_width, height=cell_height)


class _NonOverlapClock(_FactoryCell["_SRAMFactory"]):
    def __init__(self, *,
        stages: int, fab: "_SRAMFactory", name: str,
    ):
        super().__init__(fab=fab, name=name)
        if (stages%2) != 0:
            raise ValueError(f"stages has to be even not {stages}")
        self.stages = stages

    def _create_circuit(self):
        fab = self.fab
        spec = fab.spec

        stdcells = spec.stdcelllib.cells

        inv = stdcells.inv_x0
        nand2 = stdcells.nand2_x0

        ckt = self.new_circuit()

        clkinv = ckt.instantiate(inv, name="clkinv")

        firstnand2 = ckt.instantiate(nand2, name="firstnand2")
        firststages = tuple(
            ckt.instantiate(inv, name=f"firststage[{stage}]")
            for stage in range(self.stages)
        )

        secondnand2 = ckt.instantiate(nand2, name="secondnand2")
        secondstages = tuple(
            ckt.instantiate(inv, name=f"secondstage[{stage}]")
            for stage in range(self.stages)
        )

        ckt.new_net(name="vss", external=True, childports=(
            clkinv.ports.vss,
            firstnand2.ports.vss, *(stage.ports.vss for stage in firststages),
            secondnand2.ports.vss, *(stage.ports.vss for stage in secondstages),
        ))
        ckt.new_net(name="vdd", external=True, childports=(
            clkinv.ports.vdd,
            firstnand2.ports.vdd, *(stage.ports.vdd for stage in firststages),
            secondnand2.ports.vdd, *(stage.ports.vdd for stage in secondstages),
        ))

        ckt.new_net(name="clk", external=True, childports=(
            firstnand2.ports.i0, clkinv.ports.i,
        ))
        ckt.new_net(name="clk_n", external=False, childports=(
            clkinv.ports.nq, secondnand2.ports.i0,
        ))

        for stage, firststage in enumerate(firststages):
            ckt.new_net(name=f"firststage[{stage}]", external=True, childports=(
                firstnand2.ports.nq if stage == 0 else firststages[stage -1].ports.nq,
                firststage.ports.i,
            ))
        ckt.new_net(name=f"firststage[{self.stages}]", external=True, childports=(
            firststages[self.stages - 1].ports.nq, secondnand2.ports.i1,
        ))

        for stage, secondstage in enumerate(secondstages):
            ckt.new_net(name=f"secondstage[{stage}]", external=True, childports=(
                secondnand2.ports.nq if stage == 0 else secondstages[stage -1].ports.nq,
                secondstage.ports.i,
            ))
        ckt.new_net(name=f"secondstage[{self.stages}]", external=True, childports=(
            secondstages[self.stages - 1].ports.nq, firstnand2.ports.i1,
        ))

    def _create_layout(self):
        fab = self.fab
        spec = fab.spec
        cache = fab._cache

        nets = self.circuit.nets
        insts = self.circuit.instances

        metal1 = cache.metal(1)
        metal1pin = cache.metalpin(1)
        via1 = cache.via(1)
        metal2 = cache.metal(2)
        metal2pin = cache.metalpin(2)

        layouter = self.new_circuitlayouter()
        layout = layouter.layout

        x = 0.0
        firstnand2_lay = layouter.place(insts.firstnand2, x=x, y=0.0)
        vss_bb0 = firstnand2_lay.bounds(mask=metal1pin.mask, net=nets.vss, depth=1)
        vdd_bb0 = firstnand2_lay.bounds(mask=metal1pin.mask, net=nets.vdd, depth=1)
        nand2_bb = firstnand2_lay.boundary
        assert nand2_bb is not None
        x = nand2_bb.right
        firststage_lays = []
        for stage in range(self.stages):
            inst = insts[f"firststage[{stage}]"]
            stage_lay = layouter.place(inst, x=x, y=0.0)
            firststage_lays.append(stage_lay)
            stage_bb = stage_lay.boundary
            assert stage_bb is not None
            x = stage_bb.right
            cell_top = stage_bb.top
        cell_width = x

        x = 0.0
        clkinv_lay = layouter.place(insts.clkinv, x=x, y=0.0, rotation=_geo.Rotation.MX)
        vss_bb1 = clkinv_lay.bounds(mask=metal1pin.mask, net=nets.vss, depth=1)
        vdd_bb1 = clkinv_lay.bounds(mask=metal1pin.mask, net=nets.vdd, depth=1)
        inv_bb = clkinv_lay.boundary
        assert inv_bb is not None
        x = inv_bb.right
        secondnand2_lay = layouter.place(insts.secondnand2, x=x, y=0.0, rotation=_geo.Rotation.MX)
        nand2_bb = secondnand2_lay.boundary
        assert nand2_bb is not None
        x = nand2_bb.right
        secondstage_lays = []
        for stage in range(self.stages):
            inst = insts[f"secondstage[{stage}]"]
            stage_lay = layouter.place(inst, x=x, y=0.0, rotation=_geo.Rotation.MX)
            secondstage_lays.append(stage_lay)
            stage_bb = stage_lay.boundary
            assert stage_bb is not None
            x = stage_bb.right
            cell_bottom = stage_bb.bottom
        cell_width = max(cell_width, x)

        # vss/vdd
        shape = _geo.Rect.from_rect(rect=vss_bb0, left=0.0, right=cell_width)
        layouter.add_wire(net=nets.vss, wire=metal1, pin=metal1pin, shape=shape)
        shape = _geo.Rect.from_rect(rect=vss_bb1, left=0.0, right=cell_width)
        layouter.add_wire(net=nets.vss, wire=metal1, pin=metal1pin, shape=shape)

        shape = _geo.Rect.from_rect(rect=vdd_bb0, left=0.0, right=cell_width)
        layouter.add_wire(net=nets.vdd, wire=metal1, pin=metal1pin, shape=shape)
        shape = _geo.Rect.from_rect(rect=vdd_bb1, left=0.0, right=cell_width)
        layouter.add_wire(net=nets.vdd, wire=metal1, pin=metal1pin, shape=shape)

        # clk
        firstnand2clk_m1pinbb = firstnand2_lay.bounds(
            mask=metal1pin.mask, net=nets.clk, depth=1,
        )
        clkinvclk_m1pinbb = clkinv_lay.bounds(
            mask=metal1pin.mask, net=nets.clk, depth=1,
        )
        _via1clk_lay = layouter.wire_layout(
            net=nets.clk, wire=via1, rows=2, bottom_enclosure="tall", top_enclosure="tall",
        )
        _via1clk_m1bb = _via1clk_lay.bounds(mask=metal1.mask)
        x_via1 = firstnand2clk_m1pinbb.center.x
        y_via1 = firstnand2clk_m1pinbb.bottom - _via1clk_m1bb.bottom
        via1clk_lay = layouter.place(_via1clk_lay, x=x_via1, y=y_via1)
        via1clk_m2bb1 = via1clk_lay.bounds(mask=metal2.mask)
        x_via1 = clkinvclk_m1pinbb.center.x
        y_via1 = clkinvclk_m1pinbb.top - _via1clk_m1bb.top
        via1clk_lay = layouter.place(_via1clk_lay, x=x_via1, y=y_via1)
        via1clk_m2bb2 = via1clk_lay.bounds(mask=metal2.mask)

        shape = _geo.Rect(
            left=min(via1clk_m2bb1.left, via1clk_m2bb2.left),
            bottom=via1clk_m2bb2.bottom,
            right=max(via1clk_m2bb1.right, via1clk_m2bb2.right),
            top=via1clk_m2bb1.top,
        )
        layouter.add_wire(net=nets.clk, wire=metal2, pin=metal2pin, shape=shape)

        # clk_n
        clkinvclkn_m1pinbb = clkinv_lay.bounds(
            mask=metal1pin.mask, net=nets.clk_n, depth=1,
        )
        secondnand2clkn_m1pinbb = secondnand2_lay.bounds(
            mask=metal1pin.mask, net=nets.clk_n, depth=1,
        )
        shape = _geo.Rect(
            left=clkinvclkn_m1pinbb.left,
            bottom=max(clkinvclkn_m1pinbb.bottom, secondnand2clkn_m1pinbb.bottom),
            right=secondnand2clkn_m1pinbb.right,
            top=min(clkinvclkn_m1pinbb.top, secondnand2clkn_m1pinbb.top),
        )
        layouter.add_wire(net=nets.clk_n, wire=metal1, shape=shape)

        # stage nets
        for stage, stage_lay in enumerate(firststage_lays):
            net = nets[f"firststage[{stage}]"]
            if stage != 0:
                prevstage_lay = firststage_lays[stage - 1]
            else:
                prevstage_lay = firstnand2_lay
            prevstage_m1pinbb = prevstage_lay.bounds(mask=metal1pin.mask, net=net, depth=1)
            stage_m1pinbb = stage_lay.bounds(mask=metal1pin.mask, net=net, depth=1)
            shape = _geo.Rect(
                left=prevstage_m1pinbb.left,
                bottom=max(prevstage_m1pinbb.bottom, stage_m1pinbb.bottom),
                right=stage_m1pinbb.right,
                top=min(prevstage_m1pinbb.top, stage_m1pinbb.top),
            )
            layouter.add_wire(net=net, wire=metal1, pin=metal1pin, shape=shape)

        for stage, stage_lay in enumerate(secondstage_lays):
            net = nets[f"secondstage[{stage}]"]
            if stage != 0:
                prevstage_lay = secondstage_lays[stage - 1]
            else:
                prevstage_lay = secondnand2_lay
            prevstage_m1pinbb = prevstage_lay.bounds(mask=metal1pin.mask, net=net, depth=1)
            stage_m1pinbb = stage_lay.bounds(mask=metal1pin.mask, net=net, depth=1)
            shape = _geo.Rect(
                left=prevstage_m1pinbb.left,
                bottom=max(prevstage_m1pinbb.bottom, stage_m1pinbb.bottom),
                right=stage_m1pinbb.right,
                top=min(prevstage_m1pinbb.top, stage_m1pinbb.top),
            )
            layouter.add_wire(net=net, wire=metal1, pin=metal1pin, shape=shape)

        firstnet = nets[f"firststage[{self.stages}]"]
        firststage_m1pinbb = firststage_lays[-1].bounds(
            mask=metal1pin.mask, net=firstnet,
        )
        firstnand_m1pinbb = secondnand2_lay.bounds(
            mask=metal1pin.mask, net=firstnet, depth=1,
        )
        _via1first_lay = layouter.wire_layout(
            net=firstnet, wire=via1, rows=2, bottom_enclosure="tall", top_enclosure="tall",
        )
        _via1first_m1bb = _via1first_lay.bounds(mask=metal1.mask)
        _via1first_m2bb = _via1first_lay.bounds(mask=metal2.mask)

        secondnet = nets[f"secondstage[{self.stages}]"]
        secondstage_m1pinbb = secondstage_lays[-1].bounds(
            mask=metal1pin.mask, net=secondnet,
        )
        secondnand_m1pinbb = firstnand2_lay.bounds(
            mask=metal1pin.mask, net=secondnet, depth=1,
        )
        _via1second_lay = layouter.wire_layout(
            net=secondnet, wire=via1, rows=2, bottom_enclosure="tall", top_enclosure="tall",
        )
        _via1second_m1bb = _via1second_lay.bounds(mask=metal1.mask)
        _via1second_m2bb = _via1second_lay.bounds(mask=metal2.mask)

        x_via1first = firststage_m1pinbb.center.x
        y_via1first = firststage_m1pinbb.bottom - _via1first_m1bb.bottom
        via1firstinv_lay = layouter.place(_via1first_lay, x=x_via1first, y=y_via1first)
        via1firstinv_m2bb = via1firstinv_lay.bounds(mask=metal2.mask)
        x_via1second = secondstage_m1pinbb.center.x
        y_via1second = secondstage_m1pinbb.top - _via1second_m1bb.top
        via1secondinv_lay = layouter.place(_via1second_lay, x=x_via1second, y=y_via1second)
        via1secondinv_m2bb = via1secondinv_lay.bounds(mask=metal2.mask)

        assert (
            (via1firstinv_m2bb.right + metal2.min_space) < via1secondinv_m2bb.left
        ), "Not implemented"

        x_via1first2 = firstnand_m1pinbb.center.x
        y_via1first2 = y_via1second
        via1firstnand_lay = layouter.place(_via1first_lay, x=x_via1first2, y=y_via1first2)
        via1firstnand_m2bb = via1firstnand_lay.bounds(mask=metal2.mask)
        x_via1second2 = secondnand_m1pinbb.center.x
        y_via1second2 = via1firstinv_m2bb.top + metal2.min_space - _via1second_m2bb.bottom
        via1secondnand_lay = layouter.place(_via1second_lay, x=x_via1second2, y=y_via1second2)
        via1secondnand_m2bb = via1secondnand_lay.bounds(mask=metal2.mask)

        shape = _geo.Rect.from_rect(
            rect=via1firstinv_m2bb, bottom=via1firstnand_m2bb.bottom,
        )
        layouter.add_wire(net=firstnet, wire=metal2, shape=shape)
        shape = _geo.Rect.from_rect(
            rect=via1firstnand_m2bb, right=via1firstinv_m2bb.right,
        )
        layouter.add_wire(net=firstnet, wire=metal2, pin=metal2pin, shape=shape)

        shape = _geo.Rect.from_rect(
            rect=via1secondinv_m2bb, top=via1secondnand_m2bb.top,
        )
        layouter.add_wire(net=secondnet, wire=metal2, shape=shape)
        shape = _geo.Rect.from_rect(
            rect=via1secondnand_m2bb, right=via1secondinv_m2bb.right,
        )
        layouter.add_wire(net=secondnet, wire=metal2, pin=metal2pin, shape=shape)

        # boundary
        self.set_boundary(
            bb=_geo.Rect(left=0.0, bottom=cell_bottom, right=cell_width, top=cell_top),
        )


class _ClockGenerator(_FactoryCell["_SRAMFactory"]):
    def _create_circuit(self) -> None:
        fab = self.fab
        spec = fab.spec

        stdcells = spec.stdcelllib.cells
        buf_cell = stdcells.buf_x2
        inv_cell = stdcells.inv_x2

        ckt = self.new_circuit()

        # TODO: make stages configurable
        nonovl_cell = fab.nonoverlapclock(stages=8)

        nonovl = ckt.instantiate(nonovl_cell, name="nonovl")

        decodeclkbuf = ckt.instantiate(buf_cell, name="decodeclkbuf")
        columnclkbuf = ckt.instantiate(buf_cell, name="columnclkbuf")
        wlenbuf = ckt.instantiate(buf_cell, name="wlenbuf")
        weenbuf = ckt.instantiate(buf_cell, name="weenbuf")
        prechargeinv = ckt.instantiate(inv_cell, name="prechargeinv")

        ckt.new_net(name="vss", external=True, childports=(
            nonovl.ports.vss,
            decodeclkbuf.ports.vss, columnclkbuf.ports.vss,
            wlenbuf.ports.vss, weenbuf.ports.vss,
            prechargeinv.ports.vss,
        ))
        ckt.new_net(name="vdd", external=True, childports=(
            nonovl.ports.vdd,
            decodeclkbuf.ports.vdd, columnclkbuf.ports.vdd,
            wlenbuf.ports.vdd, weenbuf.ports.vdd,
            prechargeinv.ports.vdd,
        ))

        ckt.new_net(name="clk", external=True, childports=(
            nonovl.ports.clk, decodeclkbuf.ports.i, columnclkbuf.ports.i,
        ))
        ckt.new_net(
            name="decodeclk", external=True, childports=decodeclkbuf.ports.q,
        )
        ckt.new_net(
            name="columnclk", external=True, childports=columnclkbuf.ports.q,
        )

        ckt.new_net(
            name="precharge_n", external=True, childports=prechargeinv.ports.nq,
        )
        ckt.new_net(
            name="wl_en", external=True, childports=wlenbuf.ports.q,
        )
        ckt.new_net(
            name="we_en", external=True, childports=weenbuf.ports.q,
        )

        ckt.new_net(name="firstpulse", external=False, childports=(
            nonovl.ports["firststage[7]"], wlenbuf.ports.i, weenbuf.ports.i,
        ))
        ckt.new_net(name="secondpulse", external=False, childports=(
            nonovl.ports["secondstage[7]"], prechargeinv.ports.i,
        ))

        # non connected nonovl pins
        for stage in (*range(7), 8): # stage 7 is used
            net_name = f"firststage[{stage}]"
            ckt.new_net(name=net_name, external=False, childports=nonovl.ports[net_name])
            net_name = f"secondstage[{stage}]"
            ckt.new_net(name=net_name, external=False, childports=nonovl.ports[net_name])

    def _create_layout(self) -> None:
        fab = self.fab
        cache = fab._cache

        nets = self.circuit.nets
        insts = self.circuit.instances

        metal1 = cache.metal(1)
        metal1pin = cache.metalpin(1)
        via1 = cache.via(1)
        metal2 = cache.metal(2)
        metal2pin = cache.metalpin(2)

        layouter = self.new_circuitlayouter()
        layout = layouter.layout

        nonovl_lay = layouter.place(insts.nonovl, x=0.0, y=0.0)
        nonovl_bb = nonovl_lay.boundary
        assert nonovl_bb is not None
        x_top = x_bottom = nonovl_bb.right

        decodeclkbuf_lay = layouter.place(insts.decodeclkbuf, x=x_top, y=0.0)
        decodeclkbuf_bb = decodeclkbuf_lay.boundary
        assert decodeclkbuf_bb is not None
        x_top = decodeclkbuf_bb.right
        columnclkbuf_lay = layouter.place(
            insts.columnclkbuf, x=x_bottom, y=0.0, rotation=_geo.Rotation.MX,
        )
        columnclkbuf_bb = columnclkbuf_lay.boundary
        assert columnclkbuf_bb is not None
        x_bottom = columnclkbuf_bb.right

        wlenbuf_lay = layouter.place(insts.wlenbuf, x=x_top, y=0.0)
        wlenbuf_bb = wlenbuf_lay.boundary
        assert wlenbuf_bb is not None
        x_top = wlenbuf_bb.right
        weenbuf_lay = layouter.place(
            insts.weenbuf, x=x_bottom, y=0.0, rotation=_geo.Rotation.MX,
        )
        weenbuf_bb = weenbuf_lay.boundary
        assert weenbuf_bb is not None
        x_bottom = weenbuf_bb.right

        prechargeninv_lay = layouter.place(
            insts.prechargeinv, x=x_bottom, y=0.0, rotation=_geo.Rotation.MX,
        )
        prechargeninv_bb = prechargeninv_lay.boundary
        assert prechargeninv_bb is not None
        x_bottom = prechargeninv_bb.right

        cell_width = max(x_top, x_bottom)

        # vss/vdd
        nonovlvss_m1pinbb = nonovl_lay.bounds(mask=metal1pin.mask, net=nets.vss, depth=1)
        shape = _geo.Rect.from_rect(rect=nonovlvss_m1pinbb, right=cell_width)
        layouter.add_wire(net=nets.vss, wire=metal1, pin=metal1pin, shape=shape)

        for nonovlvdd_m1pinms in nonovl_lay.filter_polygons(
            net=nets.vdd, mask=metal1pin.mask, split=True, depth=1,
        ):
            rect = nonovlvdd_m1pinms.shape
            assert isinstance(rect, _geo.Rect), "Not implemented"
            shape = _geo.Rect.from_rect(rect=rect, right=cell_width)
            layouter.add_wire(net=nets.vdd, wire=metal1, pin=metal1pin, shape=shape)

        # clk
        nonovlclk_m2pinbb = nonovl_lay.bounds(mask=metal2pin.mask, net=nets.clk, depth=1)
        columnclkbufclk_m1pinbb = columnclkbuf_lay.bounds(
            mask=metal1pin.mask, net=nets.clk, depth=1,
        )
        decodeclkbufclk_m1pinbb = decodeclkbuf_lay.bounds(
            mask=metal1pin.mask, net=nets.clk, depth=1,
        )

        nonovl_m2bb = nonovl_lay.bounds(mask=metal2.mask)
        _via1clk_lay = layouter.wire_layout(
            net=nets.clk, wire=via1, rows=2, bottom_enclosure="tall", top_enclosure="tall",
        )
        _via1clk_m1bb = _via1clk_lay.bounds(mask=metal1.mask)
        _via1clk_m2bb = _via1clk_lay.bounds(mask=metal2.mask)
        x_via1clk = columnclkbufclk_m1pinbb.center.x
        y_via1clk = min(
            nonovl_m2bb.bottom - 2*metal2.min_space - _via1clk_m2bb.top,
            columnclkbufclk_m1pinbb.top - _via1clk_m1bb.top,
        )
        via1clkcolumn_lay = layouter.place(_via1clk_lay, x=x_via1clk, y=y_via1clk)
        via1clkcolumn_m2bb = via1clkcolumn_lay.bounds(mask=metal2.mask)
        x_via1clk = decodeclkbufclk_m1pinbb.center.x
        y_via1clk = decodeclkbufclk_m1pinbb.bottom - _via1clk_m1bb.bottom
        via1clkdecode_lay = layouter.place(_via1clk_lay, x=x_via1clk, y=y_via1clk)
        via1clkdecode_m2bb = via1clkdecode_lay.bounds(mask=metal2.mask)

        shape = _geo.Rect.from_rect(
            rect=nonovlclk_m2pinbb, bottom=via1clkcolumn_m2bb.bottom,
        )
        layouter.add_wire(net=nets.clk, wire=metal2, pin=metal2pin, shape=shape)

        shape = _geo.Rect.from_rect(
            rect=via1clkcolumn_m2bb, left=nonovlclk_m2pinbb.left,
            right=max(via1clkcolumn_m2bb.right, via1clkdecode_m2bb.right),
        )
        layouter.add_wire(net=nets.clk, wire=metal2, shape=shape)
        shape = _geo.Rect.from_rect(
            rect=via1clkdecode_m2bb, bottom=via1clkcolumn_m2bb.bottom,
        )
        layouter.add_wire(net=nets.clk, wire=metal2, shape=shape)

        # firstpulse
        net = nets.firstpulse
        fpnonovl_m1pinbb = nonovl_lay.bounds(mask=metal1pin.mask, net=net, depth=1)
        fpwlen_m1pinbb = wlenbuf_lay.bounds(mask=metal1pin.mask, net=net, depth=1)
        fpween_m1pinbb = weenbuf_lay.bounds(mask=metal1pin.mask, net=net, depth=1)

        _via1fp_lay = layouter.wire_layout(
            net=net, wire=via1, rows=2, bottom_enclosure="tall", top_enclosure="tall",
        )
        _via1fp_m1bb = _via1fp_lay.bounds(mask=metal1.mask)
        x_via1fp = fpnonovl_m1pinbb.right - _via1fp_m1bb.right
        y_via1fp = fpnonovl_m1pinbb.center.y
        via1fpnonovl_lay = layouter.place(_via1fp_lay, x=x_via1fp, y=y_via1fp)
        via1fpnonovl_m2bb = via1fpnonovl_lay.bounds(mask=metal2.mask)
        x_via1fp = fpwlen_m1pinbb.center.x
        via1fpwl_lay = layouter.place(_via1fp_lay, x=x_via1fp, y=y_via1fp)
        via1fpwl_m2bb = via1fpwl_lay.bounds(mask=metal2.mask)
        x_via1fp = fpween_m1pinbb.center.x
        y_via1fp = fpween_m1pinbb.top - _via1fp_m1bb.top
        via1fpwe_lay = layouter.place(_via1fp_lay, x=x_via1fp, y=y_via1fp)
        via1fpwe_m2bb = via1fpwe_lay.bounds(mask=metal2.mask)

        shape = _geo.Rect.from_rect(
            rect=via1fpnonovl_m2bb, right=max(via1fpwl_m2bb.right, via1fpwe_m2bb.right),
        )
        layouter.add_wire(net=net, wire=metal2, shape=shape)
        shape = _geo.Rect.from_rect(rect=via1fpwe_m2bb, top=via1fpnonovl_m2bb.top)
        layouter.add_wire(net=net, wire=metal2, shape=shape)

        # secondpulse
        net = nets.secondpulse
        spnonovl_m1pinbb = nonovl_lay.bounds(mask=metal1pin.mask, net=net, depth=1)
        sppchg_m1pinbb = prechargeninv_lay.bounds(mask=metal1pin.mask, net=net, depth=1)

        _via1sp_lay = layouter.wire_layout(
            net=net, wire=via1, rows=2, bottom_enclosure="tall", top_enclosure="tall",
        )
        _via1sp_m1bb = _via1sp_lay.bounds(mask=metal1.mask)
        x_via1sp = spnonovl_m1pinbb.right - _via1sp_m1bb.right
        y_via1sp = spnonovl_m1pinbb.center.y
        via1spnonovl_lay = layouter.place(_via1sp_lay, x=x_via1sp, y=y_via1sp)
        via1spnonovl_m2bb = via1spnonovl_lay.bounds(mask=metal2.mask)
        x_via1sp = sppchg_m1pinbb.center.x
        via1sppchg_lay = layouter.place(_via1sp_lay, x=x_via1sp, y=y_via1sp)
        via1sppchg_m2bb = via1sppchg_lay.bounds(mask=metal2.mask)

        shape = _geo.Rect.from_rect(
            rect=via1spnonovl_m2bb, right=via1sppchg_m2bb.right,
        )
        layouter.add_wire(net=net, wire=metal2, shape=shape)

        # decodeclk, columnclk, wl_en, we_en, precharge_n (all metal1 pins)
        for net_name in ("decodeclk", "columnclk", "wl_en", "we_en", "precharge_n"):
            net = nets[net_name]
            m1pinbb = layout.bounds(mask=metal1pin.mask, net=net, depth=2)
            layouter.add_wire(net=net, wire=metal1, pin=metal1pin, shape=m1pinbb)

        # boundary
        self.set_boundary(bb=_geo.Rect.from_rect(rect=nonovl_bb, right=cell_width))


class _LatchedDecoder2Row(_FactoryCell["_SRAMFactory"]):
    def __init__(self, *, addressbits: int, fab: "_SRAMFactory", name: str):
        super().__init__(fab=fab, name=name)
        if addressbits != 2:
            # TODO: Support higher number of bits
            raise NotImplementedError("Latched decoder # address bits != 2")
        self.addressbits = addressbits

    def _create_circuit(self) -> None:
        fab = self.fab
        spec = fab.spec

        lines = 2**self.addressbits

        stdcells = spec.stdcelllib.cells

        ff_cell = stdcells.sff1_x4
        inv1_cell = stdcells.inv_x1
        inv2_cell = stdcells.inv_x2
        nand_cell = stdcells.nand2_x0

        ckt = self.new_circuit()

        affs = tuple(
            ckt.instantiate(ff_cell, name=f"aff[{abit}]")
            for abit in range(self.addressbits)
        )
        ainvs = tuple(
            ckt.instantiate(inv1_cell, name=f"ainv[{abit}]")
            for abit in range(self.addressbits)
        )

        linenands = tuple(
            ckt.instantiate(nand_cell, name=f"linenand[{line}]")
            for line in range(lines)
        )
        lineinvs = tuple(
            ckt.instantiate(inv2_cell, name=f"lineinv[{line}]")
            for line in range(lines)
        )

        ckt.new_net(name="vss", external=True, childports=(
            inst.ports.vss for inst in (*affs, *ainvs, *linenands, *lineinvs)
        ))
        ckt.new_net(name="vdd", external=True, childports=(
            inst.ports.vdd for inst in (*affs, *ainvs, *linenands, *lineinvs)
        ))

        ckt.new_net(name="clk", external=True, childports=(
            aff.ports.ck for aff in affs
        ))

        for abit in range(self.addressbits):
            ckt.new_net(
                name=f"a[{abit}]", external=True, childports=affs[abit].ports.i,
            )
            ckt.new_net(name=f"aint[{abit}]", external=False, childports=(
                affs[abit].ports.q, ainvs[abit].ports.i,
                *(linenands[j].ports[f"i{abit}"] for j in filter(
                    lambda n: (n & (1<<abit)) != 0, range(lines))
                ),
            ))
            ckt.new_net(name=f"aint_n[{abit}]", external=False, childports=(
                ainvs[abit].ports.nq,
                *(linenands[j].ports[f"i{abit}"] for j in filter(
                    lambda n: (n & (1<<abit)) == 0, range(lines))
                ),
            ))

        for line in range(lines):
            ckt.new_net(
                name=f"line_n[{line}]", external=False, childports=(
                    linenands[line].ports.nq, lineinvs[line].ports.i,
                )
            )
            ckt.new_net(
                name=f"line[{line}]", external=True, childports=lineinvs[line].ports.nq
            )

    def _create_layout(self) -> None:
        fab = self.fab
        tech = fab.tech
        spec = fab.spec
        cache = fab._cache

        lines = 2**self.addressbits

        metal1 = cache.metal(1)
        metal1pin = cache.metalpin(1)
        via1 = cache.via(1)
        metal2 = cache.metal(2)
        metal2pin = cache.metalpin(2)

        m2pitch = tech.computed.min_pitch(
            primitive=metal2, down=True, min_enclosure=True,
        )

        nets = self.circuit.nets
        insts = self.circuit.instances

        stdcells = spec.stdcelllib.cells

        _ff_cell = stdcells.sff1_x4
        _ff_bb = _ff_cell.layout.boundary
        assert _ff_bb is not None
        _inv1_cell = stdcells.inv_x1
        _inv1_bb = _inv1_cell.layout.boundary
        assert _inv1_bb is not None

        layouter = self.new_circuitlayouter()
        layout = layouter.layout

        assert self.addressbits == 2, "Internal error"

        # Place ffs in top row
        aff_lays: List[_lay._Layout] = []
        x_top = 0.0
        cell_top: Optional[float] = None
        for abit in range(self.addressbits):
            if abit < (self.addressbits + 1)//2:
                rot = _geo.Rotation.MY
                x_top += _ff_bb.right
            else:
                rot = _geo.Rotation.R0
                x_top += _ff_bb.left
            ff_lay = layouter.place(insts[f"aff[{abit}]"], x=x_top, y=0.0, rotation=rot)
            aff_lays.append(ff_lay)
            ff_bb = ff_lay.boundary
            assert ff_bb is not None
            x_top = ff_bb.right

            if abit == 0:
                cell_top = ff_bb.top
        assert cell_top is not None
        cell_width = x_top

        # vss/vdd for the flipflops
        vss_m1pinbb = layout.bounds(mask=metal1pin.mask, net=nets.vss, depth=2)
        layouter.add_wire(net=nets.vss, wire=metal1, pin=metal1pin, shape=vss_m1pinbb)
        vdd_m1pinbb = layout.bounds(mask=metal1pin.mask, net=nets.vdd, depth=2)
        layouter.add_wire(net=nets.vdd, wire=metal1, pin=metal1pin, shape=vdd_m1pinbb)

        # clk
        _via1clk_lay = layouter.wire_layout(
            net=nets.clk, wire=via1, rows=2, bottom_enclosure="tall", top_enclosure="tall",
        )
        _via1clk_m2bb = _via1clk_lay.bounds(mask=metal2.mask)
        y_clk = tech.on_grid(0.5*cell_top)
        x_left = cell_width
        x_right = 0.0
        for aff_lay in aff_lays:
            m1pinbb = aff_lay.bounds(mask=metal1pin.mask, net=nets.clk, depth=1)
            x_via1 = m1pinbb.center.x
            layouter.place(_via1clk_lay, x=x_via1, y=y_clk)

            x_left = min(x_left, x_via1)
            x_right = max(x_right, x_via1)
        shape = _geo.Rect(
            left=x_left, bottom=(y_clk - 0.5*_via1clk_m2bb.height),
            right=x_right, top=(y_clk + 0.5*_via1clk_m2bb.height),
        )
        layouter.add_wire(net=nets.clk, wire=metal2, pin=metal2pin, shape=shape)

        # Place a inverters in bottom row
        x_left = 0.0
        x_right = cell_width
        cell_bottom: Optional[float] = None
        a_m1_top: Optional[float] = None
        for abit in range(self.addressbits):
            if abit < (self.addressbits + 1)//2:
                x_left += _inv1_bb.left
                inv_lay = layouter.place(
                    insts[f"ainv[{abit}]"], x=x_left, y=0.0, rotation=_geo.Rotation.MX,
                )
                inv_bb = inv_lay.boundary
                assert inv_bb is not None
                x_left = inv_bb.right
            else:
                x_right -= _inv1_bb.right
                inv_lay = layouter.place(
                    insts[f"ainv[{abit}]"], x=x_right, y=0.0, rotation=_geo.Rotation.MX,
                )
                inv_bb = inv_lay.boundary
                assert inv_bb is not None
                x_right = inv_bb.left

            if abit == 0:
                # vss/vdd for bottom row
                vss_m1pinbb = inv_lay.bounds(mask=metal1pin.mask, net=nets.vss, depth=1)
                shape = _geo.Rect.from_rect(rect=vss_m1pinbb, right=cell_width)
                layouter.add_wire(net=nets.vss, wire=metal1, pin=metal1pin, shape=shape)
                vdd_m1pinbb = inv_lay.bounds(mask=metal1pin.mask, net=nets.vdd, depth=1)
                shape = _geo.Rect.from_rect(rect=vdd_m1pinbb, right=cell_width)
                layouter.add_wire(net=nets.vdd, wire=metal1, pin=metal1pin, shape=shape)

                cell_bottom = inv_bb.bottom

                # get m1_top for aint
                m1pinbb = inv_lay.bounds(
                    mask=metal1pin.mask, net=nets[f"aint[0]"], depth=1,
                )
                a_m1_top = m1pinbb.top
        assert cell_bottom is not None
        assert a_m1_top is not None

        # Place nand + inverters in bottom row
        for line in range(lines):
            nand_lay = layouter.place(
                insts[f"linenand[{line}]"], x=x_left, y=0.0, rotation=_geo.Rotation.MX,
            )
            nand_bb = nand_lay.boundary
            assert nand_bb is not None
            x_left = nand_bb.right

            inv_lay = layouter.place(
                insts[f"lineinv[{line}]"], x=x_left, y=0.0, rotation=_geo.Rotation.MX,
            )
            inv_bb = inv_lay.boundary
            assert inv_bb is not None
            x_left = inv_bb.right

            if line == 0:
                # See if m1_top needs to be lowered for aint
                m1pinbb = nand_lay.bounds(
                    mask=metal1pin.mask, net=nets["aint_n[0]"], depth=1,
                )
                a_m1_top = min(a_m1_top, m1pinbb.top)

            # line_n
            net = nets[f"line_n[{line}]"]
            linennand_m1pinbb = nand_lay.bounds(mask=metal1pin.mask, net=net, depth=1)
            lineninv_m1pinbb = inv_lay.bounds(mask=metal1pin.mask, net=net, depth=1)
            shape = _geo.Rect(
                left=linennand_m1pinbb.left,
                bottom=max(linennand_m1pinbb.bottom, lineninv_m1pinbb.bottom),
                right=lineninv_m1pinbb.right,
                top=min(linennand_m1pinbb.top, lineninv_m1pinbb.top),
            )
            layouter.add_wire(net=net, wire=metal1, shape=shape)

            # line
            net = nets[f"line[{line}]"]
            lineinv_m1pinbb = inv_lay.bounds(mask=metal1pin.mask, net=net, depth=1)
            layouter.add_wire(net=net, wire=metal1, pin=metal1pin, shape=lineinv_m1pinbb)

        # a
        for abit in range(self.addressbits):
            net = nets[f"a[{abit}]"]
            m1pinbb = aff_lays[abit].bounds(mask=metal1pin.mask, net=net, depth=1)
            layouter.add_wire(net=net, wire=metal1, pin=metal1pin, shape=m1pinbb)

        # aint
        y_a: Optional[float] = None
        for abit in range(self.addressbits):
            net = nets[f"aint[{abit}]"]
            _via1aint_lay = layouter.wire_layout(
                net=net, wire=via1, bottom_enclosure="tall", top_enclosure="wide",
            )
            _via1aint_m1bb = _via1aint_lay.bounds(mask=metal1.mask)
            _via1aint_m2bb = _via1aint_lay.bounds(mask=metal2.mask)
            h = _via1aint_m2bb.height
            if y_a is None:
                y_a = a_m1_top - _via1aint_m1bb.top
            x_left = cell_width
            x_right = 0.0
            for m1pinms in layout.filter_polygons(
                mask=metal1pin.mask, net=net, split=True, depth=1,
            ):
                m1pinbb = m1pinms.shape.bounds
                x_via1 = m1pinbb.center.x
                if m1pinbb.center.y > 0:
                    # Top row nand
                    y_via1 = m1pinbb.bottom - _via1aint_m1bb.bottom
                    via1aint_lay = layouter.place(_via1aint_lay, x=x_via1, y=y_via1)
                    via1aint_m2bb = via1aint_lay.bounds(mask=metal2.mask)
                    shape = _geo.Rect.from_rect(
                        rect=via1aint_m2bb, bottom = y_a - 0.5*h,
                    )
                    layouter.add_wire(net=net, wire=metal2, shape=shape)
                else:
                    y_via1 = y_a
                    layouter.place(_via1aint_lay, x=x_via1, y=y_via1)
                x_left = min(x_left, x_via1)
                x_right = max(x_right, x_via1)
            shape = _geo.Rect(
                left=x_left, bottom=(y_a - 0.5*h), right=x_right, top=(y_a + 0.5*h),
            )
            layouter.add_wire(net=net, wire=metal2, shape=shape)

            y_a -= m2pitch
        assert y_a is not None

        # aint_n
        for abit in range(self.addressbits):
            net = nets[f"aint_n[{abit}]"]
            _via1aint_lay = layouter.wire_layout(
                net=net, wire=via1, bottom_enclosure="tall", top_enclosure="wide",
            )
            _via1aint_m1bb = _via1aint_lay.bounds(mask=metal1.mask)
            _via1aint_m2bb = _via1aint_lay.bounds(mask=metal2.mask)
            h = _via1aint_m2bb.height
            x_left = cell_width
            x_right = 0.0
            for m1pinms in layout.filter_polygons(
                mask=metal1pin.mask, net=net, split=True, depth=1,
            ):
                m1pinbb = m1pinms.shape.bounds
                x_via1 = m1pinbb.center.x
                assert m1pinbb.center.y < 0, "Internal error"
                y_via1 = y_a
                layouter.place(_via1aint_lay, x=x_via1, y=y_via1)
                x_left = min(x_left, x_via1)
                x_right = max(x_right, x_via1)
            shape = _geo.Rect(
                left=x_left, bottom=(y_a - 0.5*h), right=x_right, top=(y_a + 0.5*h),
            )
            layouter.add_wire(net=net, wire=metal2, shape=shape)
            y_a -= m2pitch

        # boundary
        self.set_boundary(
            bb=_geo.Rect(left=0.0, bottom=cell_bottom, right=cell_width, top=cell_top),
        )


class _RowPeriphery(_FactoryCell["_SRAMFactory"]):
    def __init__(self, *,
        address_groups: Tuple[int, ...], rowdec_kwargs: Dict[str, Any],
        colperiph_kwargs: Dict[str, Any],
        fab: "_SRAMFactory", name: str,
    ):
        super().__init__(fab=fab, name=name)

        self.address_groups = address_groups
        n = len(address_groups)
        if n != 3:
            raise ValueError(
                f"Unsupport config: # address groups not 3 but {n}"
            )
        self.rowdec_kwargs = rowdec_kwargs
        self.colperiph_kwargs = colperiph_kwargs

        self._colmux_bits = colmux_bits = address_groups[-1]
        self._pd0_bits = pd0_bits = address_groups[0]
        self._pd1_bits = pd1_bits = address_groups[1]
        self._a_bits = a_bits = colmux_bits + pd0_bits + pd1_bits
        if address_groups != (3, 4, 2):
            raise ValueError(
                f"Unsupported config: address_groups not (3, 4, 2) but '{address_groups}'"
            )
        self._words = words = 2**a_bits
        self._rows = words//(2**colmux_bits)

        if "colmux" in colperiph_kwargs:
            colmux = colperiph_kwargs["colmux"]
            if 2**colmux_bits != colmux:
                raise ValueError(
                    f"Mismatch between # colmux bits {colmux_bits} and specified "
                    f"colmux {colmux} in colperiph_kwargs\n"
                    f"\t2**{colmux_bits} != {colmux}"
                )
        else:
            colperiph_kwargs["colmux"] = 2**colmux_bits

    @property
    def words(self) -> int:
        return self._words
    @property
    def rows(self) -> int:
        return self._rows

    def _create_circuit(self):
        fab = self.fab

        ckt = self.new_circuit()
        insts = ckt.instances

        colmux_bits = self._colmux_bits
        colmux = 2**colmux_bits
        pd0_bits = self._pd0_bits
        pd1_bits = self._pd1_bits
        a_bits = self._a_bits


        clkgen_cell = fab.clockgenerator()
        coldec_cell = fab.latcheddecoder2row(addressbits=colmux_bits)
        rowdec_cell = fab.rowdecoder(
            address_groups=(pd0_bits, pd1_bits), **self.rowdec_kwargs,
        )

        clkgen = ckt.instantiate(clkgen_cell, name="clkgen")
        coldec = ckt.instantiate(coldec_cell, name="coldec")
        rowdec = ckt.instantiate(rowdec_cell, name="rowdec")

        ckt.new_net(name="vss", external=True, childports=(
            inst.ports.vss for inst in insts
        ))
        ckt.new_net(name="vdd", external=True, childports=(
            inst.ports.vdd for inst in insts
        ))

        ckt.new_net(name="clk", external=True, childports=clkgen.ports.clk)

        for a_bit in range(a_bits):
            net_name = f"a[{a_bit}]"
            if a_bit < colmux_bits:
                port = coldec.ports[net_name]
            else:
                port_name = f"a[{a_bit - colmux_bits}]"
                port = rowdec.ports[port_name]
            ckt.new_net(name=net_name, external=True, childports=port)

        for row in range(self.rows):
            sig_name = f"wl[{row}]"
            ckt.new_net(
                name=sig_name, external=True, childports=rowdec.ports[sig_name],
            )

        ckt.new_net(name="decodeclk", external=False, childports=(
            clkgen.ports.decodeclk, coldec.ports.clk, rowdec.ports.clk,
        ))
        ckt.new_net(name="wl_en", external=False, childports=(
            clkgen.ports.wl_en, rowdec.ports.wl_en,
        ))

        for n_colmux in range(colmux):
            sig_name = f"mux[{n_colmux}]"
            decsig_name = f"line[{n_colmux}]"
            ckt.new_net(
                name=sig_name, external=True, childports=coldec.ports[decsig_name],
            )
        ckt.new_net(
            name="columnclk", external=True, childports=clkgen.ports.columnclk,
        )
        ckt.new_net(
            name="precharge_n", external=True, childports=clkgen.ports.precharge_n,
        )
        ckt.new_net(name="we_en", external=True, childports=clkgen.ports.we_en)

    def _create_layout(self):
        fab = self.fab
        tech = fab.tech
        cache = fab._cache

        ckt = self.circuit
        nets = ckt.nets
        insts = ckt.instances

        metal1 = cache.metal(1)
        metal1pin = cache.metalpin(1)
        via1 = cache.via(1)
        metal2 = cache.metal(2)
        metal2pin = cache.metalpin(2)
        via2 = cache.via(2)
        metal3 = cache.metal(3)
        metal3pin = cache.metalpin(3)

        colmux_bits = self._colmux_bits
        colmux_lines = 2**colmux_bits
        a_bits = self._a_bits

        layouter = self.new_circuitlayouter()
        layout = layouter.layout

        _clkgen_lay = layouter.inst_layout(inst=insts.clkgen)
        _clkgen_bb = _clkgen_lay.boundary
        assert _clkgen_bb is not None

        _coldec_lay = layouter.inst_layout(inst=insts.coldec)
        _coldec_bb = _coldec_lay.boundary
        assert _coldec_bb is not None

        _rowdec_lay = layouter.inst_layout(inst=insts.rowdec)
        _rowdec_bb = _rowdec_lay.boundary
        assert _rowdec_bb is not None

        _colperiph_cell = fab.columnperiphery(**self.colperiph_kwargs)
        _colperiph_nets = _colperiph_cell.circuit.nets
        _colperiph_lay = _colperiph_cell.layout
        _columnperiph_bb = _colperiph_lay.boundary
        assert _columnperiph_bb is not None
        dxy_colperiph = _geo.Point(x=(-_columnperiph_bb.left), y=(-_columnperiph_bb.bottom))
        _columnperiph_bb += dxy_colperiph

        x_rowdec = -_rowdec_bb.left
        y_rowdec = _columnperiph_bb.top

        x_coldec = _coldec_bb.top
        y_coldec = y_rowdec + _rowdec_bb.bottom - _coldec_bb.right
        rot_coldec = _geo.Rotation.R90

        x_clkgen = _clkgen_bb.top
        y_clkgen = y_coldec - _coldec_bb.left - _clkgen_bb.right
        rot_clkgen = _geo.Rotation.R90

        clkgen_lay = layouter.place(
            _clkgen_lay, x=x_clkgen, y=y_clkgen, rotation=rot_clkgen,
        )
        clkgen_bb = clkgen_lay.boundary
        assert clkgen_bb is not None
        assert clkgen_bb.bottom > -_geo.epsilon, "Not implemented"
        coldec_lay = layouter.place(
            _coldec_lay, x=x_coldec, y=y_coldec, rotation=rot_coldec,
        )
        rowdec_lay = layouter.place(_rowdec_lay, x=x_rowdec, y=y_rowdec)

        rowdec_bb = rowdec_lay.boundary
        assert rowdec_bb is not None
        cell_height = rowdec_bb.top
        cell_width = rowdec_bb.right

        # a
        # on m1pin for coldec, on m2pin for rowdec
        for a_bit in range(a_bits):
            net = nets[f"a[{a_bit}]"]
            if a_bit < colmux_bits:
                m1pinbb = coldec_lay.bounds(mask=metal1pin.mask, net=net, depth=1)

                _via1_lay = layouter.wire_layout(
                    net=net, wire=via1, bottom_enclosure="wide", top_enclosure="tall",
                )
                _via1_m1bb = _via1_lay.bounds(mask=metal1.mask)

                x_via1 = m1pinbb.left - _via1_m1bb.left
                y_via1 = m1pinbb.center.y
                via1_lay = layouter.place(_via1_lay, x=x_via1, y=y_via1)
                via1_m2bb = via1_lay.bounds(mask=metal2.mask)

                shape = _geo.Rect.from_rect(rect=via1_m2bb, left=0.0)
                layouter.add_wire(net=net, wire=metal2, pin=metal2pin, shape=shape)
            else:
                m2pinbb = rowdec_lay.bounds(mask=metal2pin.mask, net=net, depth=1)
                layouter.add_wire(net=net, wire=metal2, pin=metal2pin, shape=m2pinbb)

        # clk
        m2pinbb = clkgen_lay.bounds(mask=metal2pin.mask, net=nets.clk, depth=1)
        w = tech.on_grid(m2pinbb.width, mult=2, rounding="floor")
        h = tech.on_grid(m2pinbb.height, mult=2, rounding="floor")
        via2_lay = layouter.add_wire(
            net=nets.clk, wire=via2, origin=tech.on_grid(m2pinbb.center),
            bottom_width=w, bottom_height=h,
        )
        via2_m3bb = via2_lay.bounds(mask=metal3.mask)
        shape = _geo.Rect.from_rect(rect=via2_m3bb, bottom=0.0)
        layouter.add_wire(net=nets.clk, wire=metal3, pin=metal3pin, shape=shape)

        # decodeclk
        net = nets.decodeclk
        clkgen_m1pinbb = clkgen_lay.bounds(mask=metal1pin.mask, net=net, depth=1)
        rowdec_m2pinbb = rowdec_lay.bounds(mask=metal2pin.mask, net=net, depth=1)
        coldec_m2pinbb = coldec_lay.bounds(mask=metal2pin.mask, net=net, depth=1)

        _via1_lay = layouter.wire_layout(
            net=net, wire=via1, bottom_enclosure="wide", top_enclosure="tall",
        )

        x_via1 = rowdec_m2pinbb.center.x
        y_via1 = clkgen_m1pinbb.center.y
        via1_lay = layouter.place(_via1_lay, x=x_via1, y=y_via1)
        via1_m2bb = via1_lay.bounds(mask=metal2.mask)

        shape = _geo.Rect.from_rect(rect=rowdec_m2pinbb, bottom=via1_m2bb.bottom)
        layouter.add_wire(net=net, wire=metal2, shape=shape)
        shape = _geo.Rect.from_rect(rect=coldec_m2pinbb, left=x_via1)
        layouter.add_wire(net=net, wire=metal2, shape=shape)

        # wl
        for row in range(self.rows):
            net = nets[f"wl[{row}]"]
            wlm3pin_bb = rowdec_lay.bounds(mask=metal3pin.mask, net=net, depth=1)
            layouter.add_wire(net=net, wire=metal3, pin=metal3pin, shape=wlm3pin_bb)

        # columnclk
        net = nets.columnclk
        clkgen_m1pinbb = clkgen_lay.bounds(mask=metal1pin.mask, net=net, depth=1)
        net2 = _colperiph_nets.clk
        columnblock_m2pinbb = (
            _colperiph_lay.bounds(mask=metal2pin.mask, net=net2, depth=0)
            + dxy_colperiph
        )

        _via1_lay = layouter.wire_layout(
            net=net, wire=via1, columns=2,
            bottom_enclosure="wide", top_enclosure="tall",
        )
        _via1_m1bb = _via1_lay.bounds(mask=metal1.mask)

        x_via1 = clkgen_m1pinbb.right - _via1_m1bb.right
        y_via1 = clkgen_m1pinbb.center.y
        via1_lay = layouter.place(_via1_lay, x=x_via1, y=y_via1)
        via1_m2bb = via1_lay.bounds(mask=metal2.mask)
        ween_m2left = via1_m2bb.right + 2*metal2.min_space

        shape = _geo.Rect.from_rect(rect=via1_m2bb, bottom=columnblock_m2pinbb.bottom)
        layouter.add_wire(net=net, wire=metal2, shape=shape)
        shape = _geo.Rect.from_rect(
            rect=columnblock_m2pinbb, left=via1_m2bb.left, right=cell_width,
        )
        layouter.add_wire(net=net, wire=metal2, pin=metal2pin, shape=shape)

        # we_en
        net = nets.we_en
        clkgen_m1pinbb = clkgen_lay.bounds(mask=metal1pin.mask, net=net, depth=1)
        net2 = _colperiph_nets.we_en
        columnblock_m2pinbb = (
            _colperiph_lay.bounds(mask=metal2pin.mask, net=net2, depth=0)
            + dxy_colperiph
        )

        _via1_lay = layouter.wire_layout(
            net=net, wire=via1, columns=2,
            bottom_enclosure="wide", top_enclosure="tall",
        )
        _via1_m1bb = _via1_lay.bounds(mask=metal1.mask)

        x_via1 = clkgen_m1pinbb.right - _via1_m1bb.right
        y_via1 = clkgen_m1pinbb.center.y
        via1_lay = layouter.place(_via1_lay, x=x_via1, y=y_via1)
        via1_m2bb = via1_lay.bounds(mask=metal2.mask)

        left = ween_m2left
        bottom = columnblock_m2pinbb.bottom
        right = (left + columnblock_m2pinbb.height)
        top = via1_m2bb.top
        shape = _geo.Rect(left=left, bottom=bottom, right=right, top=top)
        layouter.add_wire(net=net, wire=metal2, shape=shape)
        shape = _geo.Rect.from_rect(rect=via1_m2bb, right=right)
        layouter.add_wire(net=net, wire=metal2, shape=shape)
        shape = _geo.Rect.from_rect(
            rect=columnblock_m2pinbb, left=left, right=cell_width,
        )
        layouter.add_wire(net=net, wire=metal2, pin=metal2pin, shape=shape)

        # mux[n]
        prechargen_m3right = cell_width
        m2_left: Optional[float] = None
        for mux in reversed(range(colmux_lines)):
            net_name = f"mux[{mux}]"
            net = nets[net_name]
            coldec_m1pinbb = coldec_lay.bounds(mask=metal1.mask, net=net, depth=1)
            net2 = _colperiph_nets[net_name]
            columnblock_m3pinbb = (
                _colperiph_lay.bounds(mask=metal3pin.mask, net=net2, depth=0)
                + dxy_colperiph
            )

            _via1_lay = layouter.wire_layout(
                net=net, wire=via1, columns=2,
                bottom_enclosure="wide", top_enclosure="wide",
            )
            _via1_m1bb = _via1_lay.bounds(mask=metal1.mask)

            x_via1 = coldec_m1pinbb.right - _via1_m1bb.right
            y_via1 = coldec_m1pinbb.center.y
            via1_lay = layouter.place(_via1_lay, x=x_via1, y=y_via1)
            via1_m2bb = via1_lay.bounds(mask=metal2.mask)

            _via2_lay = layouter.wire_layout(
                net=net, wire=via2, columns=2,
                bottom_enclosure="wide", top_enclosure="wide",
            )
            _via2_m3bb = _via2_lay.bounds(mask=metal3.mask)

            x_via2 = cell_width - _via2_m3bb.right
            y_via2 = columnblock_m3pinbb.center.y
            via2_lay = layouter.place(_via2_lay, x=x_via2, y=y_via2)
            via2_m2bb = via2_lay.bounds(mask=metal2.mask)
            via2_m3bb = via2_lay.bounds(mask=metal3.mask)
            prechargen_m3right = min(
                prechargen_m3right,
                via2_m3bb.left - 2*metal3.min_space,
            )

            layouter.add_wire(net=net, wire=metal3, pin=metal3pin, shape=via2_m3bb)
            if m2_left is None:
                shape = _geo.Rect.from_rect(rect=via1_m2bb, top=via2_m2bb.top)
                layouter.add_wire(net=net, wire=metal2, shape=shape)
                shape = _geo.Rect.from_rect(rect=via2_m2bb, left=via1_m2bb.left)
                layouter.add_wire(net=net, wire=metal2, shape=shape)

                m2_left = via1_m2bb.right + 2*metal2.min_space
            else:
                left = m2_left
                right = left + columnblock_m3pinbb.height
                bottom = via1_m2bb.bottom
                top = via2_m2bb.top
                shape = _geo.Rect(left=left, bottom=bottom, right=right, top=top)
                layouter.add_wire(net=net, wire=metal2, shape=shape)
                shape = _geo.Rect.from_rect(rect=via1_m2bb, right=right)
                layouter.add_wire(net=net, wire=metal2, shape=shape)
                shape = _geo.Rect.from_rect(rect=via2_m2bb, left=left)
                layouter.add_wire(net=net, wire=metal2, shape=shape)

                m2_left = right + 2*metal2.min_space

        # precharge_n
        net = nets.precharge_n
        clkgen_m1pinbb = clkgen_lay.bounds(mask=metal1pin.mask, net=net, depth=1)
        net2 = _colperiph_nets.precharge_n
        columnblock_m3pinbb = (
            _colperiph_lay.bounds(mask=metal3pin.mask, net=net, depth=0)
            + dxy_colperiph
        )

        _via1_lay = layouter.wire_layout(
            net=net, wire=via1, columns=2,
            bottom_enclosure="wide", top_enclosure="wide",
        )
        _via1_m1bb = _via1_lay.bounds(mask=metal1.mask)

        x_via1 = clkgen_m1pinbb.right - _via1_m1bb.right
        y_via1 = clkgen_m1pinbb.center.y
        via1_lay = layouter.place(_via1_lay, x=x_via1, y=y_via1)
        via1_m2bb = via1_lay.bounds(mask=metal2.mask)

        _via2_lay = layouter.wire_layout(
            net=net, wire=via2, rows=2,
            bottom_enclosure="tall", top_enclosure="tall",
        )
        _via2_m3bb = _via2_lay.bounds(mask=metal3.mask)

        x_via2 = prechargen_m3right - _via2_m3bb.right
        y_via2 = y_via1
        via2_lay = layouter.place(_via2_lay, x=x_via2, y=y_via2)
        via2_m2bb = via2_lay.bounds(mask=metal2.mask)
        via2_m3bb = via2_lay.bounds(mask=metal3.mask)

        shape = _geo.Rect.from_rect(rect=via1_m2bb, right=via2_m2bb.right)
        layouter.add_wire(net=net, wire=metal2, shape=shape)
        shape = _geo.Rect.from_rect(rect=via2_m3bb, top=columnblock_m3pinbb.top)
        layouter.add_wire(net=net, wire=metal3, shape=shape)
        shape = _geo.Rect.from_rect(
            rect=columnblock_m3pinbb, left=via2_m3bb.left, right=cell_width,
        )
        layouter.add_wire(net=net, wire=metal3, pin=metal3pin, shape=shape)

        wlen_m3right = via2_m3bb.left - 2*metal3.min_space

        # wl_en
        net = nets.wl_en
        clkgen_m1pinbb = clkgen_lay.bounds(mask=metal1pin.mask, net=net, depth=1)
        rowdec_m2pinbb = rowdec_lay.bounds(mask=metal2pin.mask, net=net, depth=1)

        _via1_lay = layouter.wire_layout(
            net=net, wire=via1, columns=2,
            bottom_enclosure="wide", top_enclosure="wide",
        )
        _via1_m1bb = _via1_lay.bounds(mask=metal1.mask)

        x_via1 = clkgen_m1pinbb.right - _via1_m1bb.right
        y_via1 = clkgen_m1pinbb.center.y
        via1_lay = layouter.place(_via1_lay, x=x_via1, y=y_via1)
        x_via2 = x_via1
        y_via2 = y_via1
        via2_lay = layouter.add_wire(
            net=net, wire=via2, columns=2, x=x_via2, y=y_via2,
            bottom_enclosure="wide", top_enclosure="wide",
        )
        via2_m3bb1 = via2_lay.bounds(mask=metal3.mask)

        _via2_lay = layouter.wire_layout(
            net=net, wire=via2, rows=2,
            bottom_enclosure="tall", top_enclosure="tall",
        )
        _via2_m2bb = _via2_lay.bounds(mask=metal2.mask)

        x_via2 = rowdec_m2pinbb.center.x
        y_via2 = rowdec_m2pinbb.bottom - _via2_m2bb.top - 4*metal3.min_space
        via2_lay = layouter.place(_via2_lay, x=x_via2, y=y_via2)
        via2_m2bb = via2_lay.bounds(mask=metal2.mask)
        via2_m3bb2 = via2_lay.bounds(mask=metal3.mask)
        assert via2_m3bb2.right < (wlen_m3right + _geo.epsilon)

        shape = _geo.Rect.from_rect(rect=via2_m3bb1, right=via2_m3bb2.right)
        layouter.add_wire(net=net, wire=metal3, shape=shape)
        shape = _geo.Rect.from_rect(rect=via2_m3bb2, bottom=via2_m3bb1.bottom)
        layouter.add_wire(net=net, wire=metal3, shape=shape)
        shape = _geo.Rect.from_rect(rect=via2_m2bb, top=rowdec_m2pinbb.bottom)
        layouter.add_wire(net=net, wire=metal2, shape=shape)

        # boundary
        self.set_size(width=cell_width, height=cell_height)


class _Precharge(_FactoryCell["_SRAMFactory"]):
    def __init__(self, *,
        bl_left: float, bl_right: float, bln_left: float, bln_right: float,
        fab: "_SRAMFactory", name: str,
    ):
        super().__init__(fab=fab, name=name)
        assert bl_right < (bln_left - _geo.epsilon), "Unsupported config"
        self.bl_left = bl_left
        self.bl_right = bl_right
        self.bln_left = bln_left
        self.bln_right = bln_right

    def _create_circuit(self):
        fab = self.fab
        spec = fab.spec

        ckt = self.new_circuit()

        pc1 = ckt.instantiate(
            spec.pmos, name="pc1", l=spec.precharge_l, w=spec.precharge_w,
        )
        pc2 = ckt.instantiate(
            spec.pmos, name="pc2", l=spec.precharge_l, w=spec.precharge_w,
        )
        pc3 = ckt.instantiate(
            spec.pmos, name="pc3", l=spec.precharge_l, w=spec.precharge_w,
        )

        ckt.new_net(name="vdd", external=True, childports=(
            pc1.ports.sourcedrain1, pc1.ports.bulk, pc2.ports.bulk,
            pc3.ports.sourcedrain2, pc3.ports.bulk,
        ))
        ckt.new_net(name="bl", external=True, childports=(
            pc1.ports.sourcedrain2, pc2.ports.sourcedrain1,
        ))
        ckt.new_net(name="bl_n", external=True, childports=(
            pc2.ports.sourcedrain2, pc3.ports.sourcedrain1,
        ))
        ckt.new_net(name="precharge_n", external=True, childports=(
            pc1.ports.gate, pc2.ports.gate, pc3.ports.gate,
        ))

    def _create_layout(self):
        fab = self.fab
        tech = fab.tech
        spec = fab.spec
        cache = fab._cache

        nwell = cache.nwell
        active = cache.active
        nimplant = cache.nimplant
        pimplant = cache.pimplant
        poly = cache.poly
        contact = cache.contact
        metal1 = cache.metal(1)
        metal1pin = cache.metalpin(1)
        via1 = cache.via(1)
        metal2 = cache.metal(2)
        metal2pin = cache.metalpin(2)
        via2 = cache.via(2)
        metal3 = cache.metal(3)
        metal3pin = cache.metalpin(3)

        # First get circuit, this also ensures that it has been generated
        ckt = self.circuit

        layouter = self.new_circuitlayouter()
        insts = ckt.instances
        nets = ckt.nets

        nwell_net = None if nwell is None else nets.vdd

        bit_cell = fab.bitcell()
        bit_height = cache.bit_height
        cell_width = cache.bit_width

        # Compute some derived rules
        bl_x = 0.5*(self.bl_left + self.bl_right)
        bln_x = 0.5*(self.bln_left + self.bln_right)

        min_actpoly_space = tech.computed.min_space(active, poly)
        min_actch_space = None
        try:
            min_actch_space = tech.computed.min_space(active, contact)
        except ValueError:
            pass
        try:
            s = tech.computed.min_space(contact.in_(poly), pimplant)
        except ValueError:
            pass
        else:
            idx = active.implant.index(pimplant)
            enc = max(
                spec.pmos.min_gateimplant_enclosure[0].max(),
                active.min_implant_enclosure[idx].max(),
            )
            if min_actch_space is None:
                min_actch_space = s + enc
            else:
                min_actch_space = max(min_actch_space, s + enc)

        # Create layout for transistors and contacts
        _pc1_lay = layouter.inst_layout(inst=insts.pc1)
        _pc1_actbb = _pc1_lay.bounds(mask=active.mask)
        _pc2_lay = layouter.inst_layout(inst=insts.pc2)
        _pc3_lay = layouter.inst_layout(inst=insts.pc3)

        _chpcgate_lay = layouter.wire_layout(
            net=nets.precharge_n, wire=contact, bottom=poly, bottom_enclosure="tall",
            top_enclosure="wide",
        )
        _chpcgate_polybb = _chpcgate_lay.bounds(mask=poly.mask)
        _via1pcgate_lay = layouter.wire_layout(
            net=nets.precharge_n, wire=via1, bottom_enclosure="wide",
            top_enclosure="tall",
        )
        _via2pcgate_lay = layouter.wire_layout(
            net=nets.precharge_n, wire=via2, bottom_enclosure="tall",
            top_enclosure="wide",
        )

        _chvddpc_lay = layouter.wire_layout(
            net=nets.vdd, wire=contact, well_net=nwell_net,
            bottom=active, bottom_implant=pimplant, bottom_well=nwell,
            bottom_enclosure="wide", bottom_height=spec.precharge_w,
            top_enclosure="tall",
        )

        _chbl_lay = layouter.wire_layout(
            net=nets.bl, wire=contact, well_net=nwell_net,
            bottom=active, bottom_implant=pimplant, bottom_well=nwell,
            bottom_enclosure="wide", bottom_height=spec.precharge_w,
            top_enclosure="tall",
        )
        _chbln_lay = layouter.wire_layout(
            net=nets.bl_n, wire=contact, well_net=nwell_net,
            bottom=active, bottom_implant=pimplant, bottom_well=nwell,
            bottom_enclosure="wide", bottom_height=spec.precharge_w,
            top_enclosure="tall",
        )

        tap_width = tech.computed.min_width(
            primitive=active, up=True, min_enclosure=True,
        )
        m3conn_width = tech.computed.min_width(
            primitive=metal3, down=True, min_enclosure=True,
        )

        _via1vdd = layouter.wire_layout(
            net=nets.vdd, wire=via1, bottom_enclosure="tall",
            top_enclosure="tall",
        )
        _via2vdd = layouter.wire_layout(
            net=nets.vdd, wire=via2, bottom_enclosure="tall",
            top_enclosure="wide",
        )

        # Compute placement
        x_pc1 = tech.on_grid(cell_width/6.0, rounding="ceiling")
        x_chbl = tech.on_grid(cell_width/3.0, rounding="ceiling")
        x_pc2 = 0.5*cell_width
        x_chbln = cell_width - x_chbl
        x_pc3 = cell_width - x_pc1

        x_chpcgate = 0.5*cell_width
        y_chpcgate = poly.min_space - _chpcgate_polybb.bottom
        y_pc = y_chpcgate + _chpcgate_polybb.top + min_actpoly_space - _pc1_actbb.bottom
        if min_actch_space is not None:
            y_pc = max(
                y_pc,
                y_chpcgate + 0.5*contact.width + min_actch_space - _pc1_actbb.bottom
            )
        y_tap = y_pc + _pc1_actbb.top + cache.min_nactpact_space + 0.5*tap_width

        cell_height = y_tap

        # Place transistors and contacts
        chpcgate_lay = layouter.place(_chpcgate_lay, x=x_chpcgate, y=y_chpcgate)
        chpcgate_polybb = chpcgate_lay.bounds(mask=poly.mask)
        chpcgate_m1bb = chpcgate_lay.bounds(mask=metal1.mask)
        layouter.place(_via1pcgate_lay, x=x_chpcgate, y=y_chpcgate)
        via2pcgate_lay = layouter.place(_via2pcgate_lay, x=x_chpcgate, y=y_chpcgate)
        via2pcgate_m3bb = via2pcgate_lay.bounds(mask=metal3.mask)

        chvddpc_lay = layouter.place(_chvddpc_lay, x=0.0, y=y_pc)
        chvddpc_actbb = chvddpc_lay.bounds(mask=active.mask)
        chvddpc_m1bb = chvddpc_lay.bounds(mask=metal1.mask)
        pc1_lay = layouter.place(_pc1_lay, x=x_pc1, y=y_pc)
        pc1_actbb = pc1_lay.bounds(mask=active.mask)
        chbl_lay = layouter.place(_chbl_lay, x=x_chbl, y=y_pc)
        chbl_actbb = chbl_lay.bounds(mask=active.mask)
        chbl_m1bb = chbl_lay.bounds(mask=metal1.mask)
        pc2_lay = layouter.place(_pc2_lay, x=x_pc2, y=y_pc)
        pc2_actbb = pc2_lay.bounds(mask=active.mask)
        chbln_lay = layouter.place(_chbln_lay, x=x_chbln, y=y_pc)
        chbln_actbb = chbln_lay.bounds(mask=active.mask)
        chbln_m1bb = chbln_lay.bounds(mask=metal1.mask)
        pc3_lay = layouter.place(_pc3_lay, x=x_pc3, y=y_pc)
        pc3_actbb = pc3_lay.bounds(mask=active.mask)
        chvddpc2_lay = layouter.place(_chvddpc_lay, x=cell_width, y=y_pc)
        chvddpc2_actbb = chvddpc2_lay.bounds(mask=active.mask)

        # Extra connections
        # active of precharge trans and contact if there are gaps.
        if chvddpc_actbb.right < pc1_actbb.left:
            shape = _geo.Rect.from_rect(rect=chvddpc_actbb, right=pc1_actbb.left)
            layouter.add_wire(
                net=nets.vdd, wire=active, implant=pimplant, well=nwell, well_net=nwell_net,
                shape=shape,
            )
        if (
            (chbl_actbb.left > pc1_actbb.right)
            or (chbl_actbb.right < pc2_actbb.left)
        ):
            shape = _geo.Rect.from_rect(
                rect=chbl_actbb, left=pc1_actbb.right, right=pc2_actbb.left,
            )
            layouter.add_wire(
                net=nets.bl, wire=active, implant=pimplant, well=nwell, well_net=nwell_net,
                shape=shape,
            )
        if (
            (chbln_actbb.left > pc2_actbb.right)
            or (chbln_actbb.right < pc3_actbb.left)
        ):
            shape = _geo.Rect.from_rect(
                rect=chbln_actbb, left=pc2_actbb.right, right=pc3_actbb.left,
            )
            layouter.add_wire(
                net=nets.bl_n, wire=active, implant=pimplant, well=nwell, well_net=nwell_net,
                shape=shape,
            )
        if chvddpc2_actbb.left > pc3_actbb.right:
            shape = _geo.Rect.from_rect(rect=chvddpc2_actbb, left=pc3_actbb.right)
            layouter.add_wire(
                net=nets.vdd, wire=active, implant=pimplant, well=nwell, well_net=nwell_net,
                shape=shape,
            )

        # precharge_n
        for lay in (pc1_lay, pc2_lay, pc3_lay):
            polybb = lay.bounds(mask=poly.mask)
            shape = _geo.Rect.from_rect(rect=polybb, bottom=y_chpcgate)
            layouter.add_wire(net=nets.precharge_n, wire=poly, shape=shape)

        shape = _geo.Rect.from_rect(rect=chpcgate_polybb, left=0.0, right=cell_width)
        layouter.add_wire(net=nets.precharge_n, wire=poly, shape=shape)
        shape = _geo.Rect.from_rect(rect=chpcgate_m1bb, left=0.0, right=cell_width)
        layouter.add_wire(net=nets.precharge_n, wire=metal1, pin=metal1pin, shape=shape)
        shape = _geo.Rect.from_rect(rect=via2pcgate_m3bb, left=0.0, right=cell_width)
        layouter.add_wire(net=nets.precharge_n, wire=metal3, pin=metal3pin, shape=shape)

        # bl/bl_n
        _via1bl_lay = layouter.wire_layout(
            net=nets.bl, wire=via1, bottom_enclosure="tall",
            top_enclosure="tall",
        )
        _via1bln_lay = layouter.wire_layout(
            net=nets.bl_n, wire=via1, bottom_enclosure="tall",
            top_enclosure="tall",
        )

        if chbl_m1bb.left > self.bl_right:
            x_via1bl = bl_x
            via1bl_lay = layouter.place(_via1bl_lay, x=x_via1bl, y=y_pc)
            via1bl_m1bb = via1bl_lay.bounds(mask=metal1.mask)

            if via1bl_m1bb.left < chbl_m1bb.left:
                shape = _geo.Rect.from_rect(rect=chbl_m1bb, left=via1bl_m1bb.left)
                layouter.add_wire(net=nets.bl, wire=metal1, shape=shape)
        else:
            x_via1bl = x_chbl
            via1bl_lay = layouter.place(_via1bl_lay, x=x_via1bl, y=y_pc)
            via1bl_m2bb = via1bl_lay.bounds(mask=metal2.mask)

            if bl_x > via1bl_m2bb.right:
                shape = _geo.Rect.from_rect(rect=via1bl_m2bb, right=bl_x)
                layouter.add_wire(net=nets.bl, wire=metal2, shape=shape)

        if chbln_m1bb.right < self.bln_left:
            x_via1bln = bln_x

            via1bln_lay = layouter.place(_via1bln_lay, x=x_via1bln, y=y_pc)
            via1bln_m1bb = via1bln_lay.bounds(mask=metal1.mask)

            if via1bln_m1bb.right > chbln_m1bb.right:
                shape = _geo.Rect.from_rect(rect=chbln_m1bb, right=via1bln_m1bb.right)
                layouter.add_wire(net=nets.bl_n, wire=metal1, shape=shape)
        else:
            x_via1bln = x_chbln

            via1bln_lay = layouter.place(_via1bln_lay, x=x_via1bln, y=y_pc)
            via1bln_m2bb = via1bln_lay.bounds(mask=metal2.mask)

            if bln_x < via1bln_m2bb.left:
                shape = _geo.Rect.from_rect(rect=via1bln_m2bb, left=bln_x)
                layouter.add_wire(net=nets.bl_n, wire=metal2, shape=shape)

        shape = _geo.Rect(
            left=self.bl_left, bottom=0.0, right=self.bl_right, top=cell_height,
        )
        layouter.add_wire(net=nets.bl, wire=metal2, pin=metal2pin, shape=shape)
        shape = _geo.Rect(
            left=self.bln_left, bottom=0.0, right=self.bln_right, top=cell_height,
        )
        layouter.add_wire(net=nets.bl_n, wire=metal2, pin=metal2pin, shape=shape)

        # vdd
        layouter.place(_via1vdd, x=0.0, y=y_pc)
        layouter.place(_via1vdd, x=cell_width, y=y_pc)
        via2vdd_lay = layouter.place(_via2vdd, x=0.0, y=y_pc)
        via2vdd_m3bb = via2vdd_lay.bounds(mask=metal3.mask)
        layouter.place(_via2vdd, x=cell_width, y=y_pc)

        shape = _geo.Rect.from_rect(rect=via2vdd_m3bb, top=(y_tap + 0.5*m3conn_width))
        layouter.add_wire(net=nets.vdd, wire=metal3, shape=shape)
        shape = _geo.Rect.from_rect(
            rect=shape, left=(cell_width - shape.right), right=(cell_width - shape.left))
        layouter.add_wire(net=nets.vdd, wire=metal3, shape=shape)
        shape = _geo.Rect(
            left=0.0, bottom=(y_tap - 0.5*m3conn_width),
            right=cell_width , top=(y_tap + 0.5*m3conn_width),
        )
        layouter.add_wire(net=nets.vdd, wire=metal3, pin=metal3pin, shape=shape)

        # nwell
        if nwell is not None:
            assert nwell_net is not None
            nwell_bb = layouter.layout.bounds(mask=nwell.mask)
            if nwell_bb.top < y_tap:
                shape = _geo.Rect.from_rect(rect=nwell_bb, top=y_tap)
                layouter.add_wire(net=nwell_net, wire=nwell, shape=shape)

        # pimplant
        # Possibly connect pimplant with pimplant of SRAM cell if it sticks out
        # of the cell on top
        for ms in bit_cell.layout.filter_polygons(mask=pimplant.mask, split=True):
            bit_shape = ms.shape
            if bit_shape.bounds.top > bit_height:
                assert isinstance(bit_shape, _geo.Rect)
                shape = _geo.Rect.from_rect(
                    rect=bit_shape, bottom=y_pc, top=cell_height,
                )
                layouter.add_portless(prim=pimplant, shape=shape)

        # boundary
        self.set_size(width=cell_width, height=cell_height)


class _ColMux(_FactoryCell["_SRAMFactory"]):
    def __init__(self, *,
        columns: int,
        bl_left: float, bl_right: float, bln_left: float, bln_right: float,
        fab: "_SRAMFactory", name: str,
    ):
        super().__init__(fab=fab, name=name)

        if not _ispow2(columns):
            raise NotImplementedError(f"Number of columns {columns} not a power of two")
        assert bl_right < (bln_left - _geo.epsilon), "Unsupported config"
        self.columns = columns
        self.bl_left = bl_left
        self.bl_right = bl_right
        self.bln_left = bln_left
        self.bln_right = bln_right

    def _create_circuit(self) -> None:
        fab = self.fab
        spec = fab.spec

        ckt = self.new_circuit()

        vssports = []
        muxblports = []
        muxblnports = []

        for col in range(self.columns):
            pgbl = ckt.instantiate(
                spec.nmos, name=f"pgbl{col}", l=spec.colmux_l, w=spec.colmux_w,
            )
            pgbln = ckt.instantiate(
                spec.nmos, name=f"pgbln{col}", l=spec.colmux_l, w=spec.colmux_w,
            )

            ckt.new_net(
                name=f"bl[{col}]", external=True, childports=pgbl.ports.sourcedrain1,
            )
            ckt.new_net(
                name=f"bl_n[{col}]", external=True, childports=pgbln.ports.sourcedrain2,
            )
            ckt.new_net(name=f"mux[{col}]", external=True, childports=(
                pgbl.ports.gate, pgbln.ports.gate,
            ))

            vssports += [pgbl.ports.bulk, pgbln.ports.bulk]
            muxblports.append(pgbl.ports.sourcedrain2)
            muxblnports.append(pgbln.ports.sourcedrain1)

        ckt.new_net(name="vss", external=True, childports=vssports)
        ckt.new_net(name="muxbl", external=True, childports=muxblports)
        ckt.new_net(name="muxbl_n", external=True, childports=muxblnports)

    def _create_layout(self) -> None:
        # Currently we put mux[n] lines on metal3; as metal1 is high resistive on Sky130
        # TODO: options to put mux[n] on metal1 or maybe ven metal1 + metal3 for bigger
        #     number of cols.
        fab = self.fab
        tech = fab.tech
        spec = fab.spec
        cache = fab._cache

        ckt = self.circuit
        insts = ckt.instances
        nets = ckt.nets

        col_nets = tuple(nets[f"mux[{col}]"] for col in range(self.columns))
        bl_nets = tuple(nets[f"bl[{col}]"] for col in range(self.columns))
        bln_nets = tuple(nets[f"bl_n[{col}]"] for col in range(self.columns))

        nmos = spec.nmos

        pwell = cache.pwell
        pwell_net = None if pwell is None else nets.vss
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

        layouter = self.new_circuitlayouter()
        layout = layouter.layout

        # Pre-computed rules
        min_colm3pitch = tech.computed.min_pitch(primitive=metal3, down=True)
        min_m1padpitch = tech.computed.min_pitch(
            primitive=metal1, down=True, up=True, min_enclosure=True,
        )

        # Create sublayouts
        _pgbl_lays = tuple(
            layouter.inst_layout(inst=insts[f"pgbl{col}"])
            for col in range(self.columns)
        )
        _pgbln_lays = tuple(
            layouter.inst_layout(inst=insts[f"pgbln{col}"])
            for col in range(self.columns)
        )
        _pgbln0_polybb = _pgbln_lays[0].bounds(mask=poly.mask)

        _chblpg_lays = tuple(
            layouter.wire_layout(
                net=bl_net, wire=contact, well_net=pwell_net,
                bottom=active, bottom_implant=nimplant, bottom_well=pwell,
                bottom_height=spec.colmux_w, bottom_enclosure="tall",
                top_height= spec.colmux_w, top_enclosure="tall",
            )
            for bl_net in bl_nets
        )
        _via1blpg_lays = tuple(
            layouter.wire_layout(
                net=bl_net, wire=via1,
                bottom_enclosure="tall", bottom_height=spec.colmux_w,
                top_enclosure="wide",
            )
            for bl_net in bl_nets
        )
        _chblnpg_lays = tuple(
            layouter.wire_layout(
                net=bln_net, wire=contact, well_net=pwell_net,
                bottom=active, bottom_implant=nimplant, bottom_well=pwell,
                bottom_height=spec.colmux_w, bottom_enclosure="tall",
                top_height= spec.colmux_w, top_enclosure="tall",
            )
            for bln_net in bln_nets
        )
        _via1blnpg_lays = tuple(
            layouter.wire_layout(
                net=bln_net, wire=via1,
                bottom_enclosure="tall", bottom_height=spec.colmux_w,
                top_enclosure="wide",
            )
            for bln_net in bln_nets
        )

        _chmuxbl_lay = layouter.wire_layout(
            net=nets.muxbl, wire=contact, well_net=pwell_net,
            bottom=active, bottom_implant=nimplant, bottom_well=pwell,
            bottom_enclosure="tall", bottom_height=spec.colmux_w,
            top_enclosure="tall",
        )
        _chmuxbln_lay = layouter.wire_layout(
            net=nets.muxbl_n, wire=contact, well_net=pwell_net,
            bottom=active, bottom_implant=nimplant, bottom_well=pwell,
            bottom_enclosure="tall", bottom_height=spec.colmux_w,
            top_enclosure="tall",
        )

        _chcolgates = tuple(
            layouter.wire_layout(
                net=col_net, wire=contact, columns=2,
                bottom=poly, bottom_enclosure="wide", top_enclosure="wide",
            )
            for col_net in col_nets
        )
        _chvia1gates = tuple(
            layouter.wire_layout(
                net=col_net, wire=via1,
                bottom_enclosure="wide", top_enclosure="wide",
            )
            for col_net in col_nets
        )
        _chvia2gates = tuple(
            layouter.wire_layout(
                net=col_net, wire=via2,
                bottom_enclosure="wide", top_enclosure="wide",
            )
            for col_net in col_nets
        )

        # Compute placement
        y_col0 = min_colm3pitch
        y_coltop = y_col0 + (self.columns - 1)*min_colm3pitch

        y_m1muxbln = y_coltop + min_m1padpitch

        y_pgbln = y_m1muxbln + min_m1padpitch + 0.5*spec.colmux_w
        y_pgbl = y_pgbln + spec.colmux_w + metal1.min_width + 2*metal1.min_space

        y_m1muxbl = 0.5*(y_pgbl + y_pgbln)

        cell_width = self.columns*cache.bit_width

        dx_chact = (
            0.5*spec.colmux_l + nmos.computed.min_contactgate_space
            + 0.5*contact.width
        )

        cell_height: Optional[float] = None
        left_m1muxbl: Optional[float] = None
        left_m1muxbln: Optional[float] = None
        right_m1muxbl: Optional[float] = None
        right_m1muxbln: Optional[float] = None
        for col, col_net in enumerate(col_nets):
            bl_left = self.bl_left + col*cache.bit_width
            bl_right = self.bl_right + col*cache.bit_width
            bln_left = self.bln_left + col*cache.bit_width
            bln_right = self.bln_right + col*cache.bit_width

            # Compute placement
            x_pg = (col + 0.5)*cache.bit_width
            x_chbl = x_pg - dx_chact
            x_chmuxbl = x_pg + dx_chact
            x_chbln = x_pg + dx_chact
            x_chmuxbln = x_pg - dx_chact

            y_col = (col + 1)*min_colm3pitch

            # Place col pin contact/vias
            layouter.place(_chcolgates[col], x=x_pg, y=y_col)
            layouter.place(_chvia1gates[col], x=x_pg, y=y_col)
            chvia2gate_lay = layouter.place(_chvia2gates[col], x=x_pg, y=y_col)
            chvia2gate_m3bb = chvia2gate_lay.bounds(mask=metal3.mask)

            # Place pass gates
            pgbln_lay = layouter.place(_pgbln_lays[col], x=x_pg, y=y_pgbln)
            pgbl_lay = layouter.place(_pgbl_lays[col], x=x_pg, y=y_pgbl)
            pgbl_polybb = pgbl_lay.bounds(mask=poly.mask)

            # Place contact/vias
            chblpg_lay = layouter.place(_chblpg_lays[col], x=x_chbl, y=y_pgbl)
            chblpg_nimplbb = chblpg_lay.bounds(mask=nimplant.mask)
            chblpg_m1bb = chblpg_lay.bounds(mask=metal1.mask)
            chblnpg_lay = layouter.place(_chblnpg_lays[col], x=x_chbln, y=y_pgbln)
            chblnpg_nimplbb = chblnpg_lay.bounds(mask=nimplant.mask)
            chblnpg_m1bb = chblnpg_lay.bounds(mask=metal1.mask)

            chmuxbl_lay = layouter.place(_chmuxbl_lay, x=x_chmuxbl, y=y_pgbl)
            chmuxbl_m1bb = chmuxbl_lay.bounds(mask=metal1.mask)
            chmuxbln_lay = layouter.place(_chmuxbln_lay, x=x_chmuxbln, y=y_pgbln)
            chmuxbln_m1bb = chmuxbln_lay.bounds(mask=metal1.mask)

            _via1blpg_m1bb = _via1blpg_lays[col].bounds(mask=metal1.mask)
            _via1blpg_m2bb = _via1blpg_lays[col].bounds(mask=metal2.mask)
            x_via1blpg = chblpg_m1bb.right - _via1blpg_m1bb.right
            m2_right = x_via1blpg + _via1blpg_m2bb.right
            if m2_right < (bln_left - metal2.min_space):
                via1blpg_lay = layouter.place(_via1blpg_lays[col], x=x_via1blpg, y=y_pgbl)
            else:
                x_via1blpg = bln_left - metal2.min_space - _via1blpg_m2bb.right
                via1blpg_lay = layouter.place(_via1blpg_lays[col], x=x_via1blpg, y=y_pgbl)
                via1blpg_m1bb = via1blpg_lay.bounds(mask=metal1.mask)

                shape = _geo.Rect.from_rect(rect=chblpg_m1bb, left=via1blpg_m1bb.left)
                layouter.add_wire(net=bl_nets[col], wire=metal1, shape=shape)
            via1blpg_m2bb = via1blpg_lay.bounds(mask=metal2.mask)

            _via1blnpg_m1bb = _via1blnpg_lays[col].bounds(mask=metal1.mask)
            x_via1blnpg = chblnpg_m1bb.right - _via1blnpg_m1bb.right
            via1blnpg_lay = layouter.place(_via1blnpg_lays[col], x=x_via1blnpg, y=y_pgbln)
            via1blnpg_m2bb = via1blnpg_lay.bounds(mask=metal2.mask)

            if col == 0:
                # Take a little margin for cell_height by adding min_spce and
                # not 0.5*min_space
                cell_height = max(
                    pgbl_polybb.top + poly.min_space,
                    chblpg_nimplbb.top + nimplant.min_space
                )
            assert cell_height is not None

            # muxbl/muxbl_n
            shape = _geo.Rect.from_rect(rect=chmuxbl_m1bb, bottom=y_m1muxbl)
            layouter.add_wire(net=nets.muxbl, wire=metal1, shape=shape)
            shape = _geo.Rect.from_rect(rect=chmuxbln_m1bb, bottom=y_m1muxbln)
            layouter.add_wire(net=nets.muxbl_n, wire=metal1, shape=shape)
            if col == 0:
                left_m1muxbl = chmuxbl_m1bb.left
                left_m1muxbln = chmuxbln_m1bb.left
            if col == (self.columns - 1):
                right_m1muxbl = chmuxbl_m1bb.right
                right_m1muxbln = chmuxbln_m1bb.right

            # bl/bl_n m2 pins
            shape = _geo.Rect(
                left=bl_left, bottom=via1blpg_m2bb.bottom,
                right=bl_right, top=cell_height,
            )
            layouter.add_wire(net=bl_nets[col], wire=metal2, pin=metal2pin, shape=shape)
            if via1blpg_m2bb.left > shape.right:
                shape = _geo.Rect.from_rect(rect=via1blpg_m2bb, left=shape.left)
                layouter.add_wire(net=bl_nets[col], wire=metal2, pin=metal2pin, shape=shape)
            elif via1blpg_m2bb.right < shape.left:
                shape = _geo.Rect.from_rect(rect=via1blpg_m2bb, right=shape.right)
                layouter.add_wire(net=bl_nets[col], wire=metal2, pin=metal2pin, shape=shape)

            shape = _geo.Rect(
                left=bln_left, bottom=via1blnpg_m2bb.bottom,
                right=bln_right, top=cell_height,
            )
            layouter.add_wire(net=bln_nets[col], wire=metal2, pin=metal2pin, shape=shape)
            if via1blnpg_m2bb.left > shape.right:
                shape = _geo.Rect.from_rect(rect=via1blnpg_m2bb, left=shape.left)
                layouter.add_wire(net=bln_nets[col], wire=metal2, pin=metal2pin, shape=shape)
            elif via1blnpg_m2bb.right < shape.left:
                shape = _geo.Rect.from_rect(rect=via1blnpg_m2bb, right=shape.right)
                layouter.add_wire(net=bln_nets[col], wire=metal2, pin=metal2pin, shape=shape)

            # nimplant
            shape = _geo.Rect(
                left=chblpg_nimplbb.left, bottom=chblnpg_nimplbb.bottom,
                right=chblnpg_nimplbb.right, top=chblpg_nimplbb.top,
            )
            layout.add_shape(prim=nimplant, net=None, shape=shape)

            # poly
            shape = _geo.Rect.from_rect(rect=pgbl_polybb, bottom=y_col)
            layouter.add_wire(net=col_net, wire=poly, shape=shape)

            # m3pin
            shape = _geo.Rect.from_rect(rect=chvia2gate_m3bb, left=0.0, right=cell_width)
            layouter.add_wire(net=col_net, wire=metal3, pin=metal3pin, shape=shape)
        assert cell_height is not None
        assert left_m1muxbl is not None
        assert left_m1muxbln is not None
        assert right_m1muxbl is not None
        assert right_m1muxbln is not None

        # muxbl/muxbl_n
        shape = _geo.Rect(
            left=left_m1muxbl, bottom=(y_m1muxbl - 0.5*metal1.min_width),
            right=right_m1muxbl, top=(y_m1muxbl + 0.5*metal1.min_width)
        )
        layouter.add_wire(net=nets.muxbl, wire=metal1, shape=shape)
        shape = _geo.Rect(
            left=left_m1muxbln, bottom=(y_m1muxbln - 0.5*metal1.min_width),
            right=right_m1muxbln, top=(y_m1muxbln + 0.5*metal1.min_width)
        )
        layouter.add_wire(net=nets.muxbl_n, wire=metal1, shape=shape)

        via1muxbl_lay = layouter.add_wire(
            net=nets.muxbl, wire=via1, x=2*cache.bit_width, y=y_m1muxbl, rows=2,
            bottom_enclosure="tall", top_enclosure="wide",
        )
        via1muxbl_m2bb = via1muxbl_lay.bounds(mask=metal2.mask)
        shape = _geo.Rect.from_rect(rect=via1muxbl_m2bb, bottom=0.0)
        layouter.add_wire(net=nets.muxbl, wire=metal2, pin=metal2pin, shape=shape)

        via1muxbln_lay = layouter.add_wire(
            net=nets.muxbl_n, wire=via1, x=cache.bit_width, y=y_m1muxbln, rows=2,
            bottom_enclosure="tall", top_enclosure="wide",
        )
        via1muxbln_m2bb = via1muxbln_lay.bounds(mask=metal2.mask)
        shape = _geo.Rect.from_rect(rect=via1muxbln_m2bb, bottom=0.0)
        layouter.add_wire(net=nets.muxbl_n, wire=metal2, pin=metal2pin, shape=shape)

        # vss
        layouter.add_wire(
            net=nets.vss, wire=contact, well_net=pwell_net,
            x=0.0, y=y_pgbl, rows=2,
            bottom=active, bottom_implant=pimplant, bottom_well=pwell,
            bottom_enclosure="tall", top_enclosure="tall",
        )
        layouter.add_wire(
            net=nets.vss, wire=contact, well_net=pwell_net,
            x=cell_width, y=y_pgbl, rows=2,
            bottom=active, bottom_implant=pimplant, bottom_well=pwell,
            bottom_enclosure="tall", top_enclosure="tall",
        )
        layouter.add_wire(
            net=nets.vss, wire=via1, x=0.0, y=y_pgbl, rows=2,
            bottom_enclosure="tall", top_enclosure="tall",
        )
        layouter.add_wire(
            net=nets.vss, wire=via1, x=cell_width, y=y_pgbl, rows=2,
            bottom_enclosure="tall", top_enclosure="tall",
        )
        via2vssleft_lay = layouter.add_wire(
            net=nets.vss, wire=via2, x=0.0, y=y_pgbl, rows=2,
            bottom_enclosure="tall", top_enclosure="tall",
        )
        via2vssleft_m3bb = via2vssleft_lay.bounds(mask=metal3.mask)
        via2vssright_lay = layouter.add_wire(
            net=nets.vss, wire=via2, x=cell_width, y=y_pgbl, rows=2,
            bottom_enclosure="tall", top_enclosure="tall",
        )
        via2vssright_m3bb = via2vssright_lay.bounds(mask=metal3.mask)

        shape = _geo.Rect.from_rect(rect=via2vssleft_m3bb, right=via2vssright_m3bb.right)
        layouter.add_wire(
            net=nets.vss, wire=metal3, pin=metal3pin, shape=shape,
        )

        # boundary
        self.set_size(width=cell_width, height=cell_height)


class _SenseAmp(_FactoryCell["_SRAMFactory"]):
    def __init__(self, *, colmux: int, fab: "_SRAMFactory", name: str):
        super().__init__(fab=fab, name=name)

        self.colmux = colmux

    def _create_circuit(self) -> None:
        fab = self.fab
        spec = fab.spec
        stdcells = spec.stdcelllib.cells

        ckt = self.new_circuit()

        sr = ckt.instantiate(stdcells.nsnrlatch_x1, name="latch")
        tie = ckt.instantiate(stdcells.tie, name="tie")

        ckt.new_net(name="vss", external=True, childports=(
            sr.ports.vss, tie.ports.vss,
        ))
        ckt.new_net(name="vdd", external=True, childports=(
            sr.ports.vdd, tie.ports.vdd,
        ))

        ckt.new_net(name="bl", external=True, childports=sr.ports.nrst)
        ckt.new_net(name="bl_n", external=True, childports=sr.ports.nset)
        ckt.new_net(name="q", external=True, childports=sr.ports.q)
        ckt.new_net(name="nq", external=False, childports=sr.ports.nq)

    def _create_layout(self) -> None:
        fab = self.fab
        cache = fab._cache

        ckt = self.circuit
        nets = ckt.nets
        insts = ckt.instances

        metal1 = cache.metal(1)
        metal1pin = cache.metalpin(1)
        via1 = cache.via(1)
        metal2 = cache.metal(2)
        metal2pin = cache.metalpin(2)

        layouter = self.new_circuitlayouter()

        cell_width = self.colmux*cache.bit_width

        # Place the subcells
        sr_lay = layouter.place(insts.latch, x=0.0, y=0.0)
        sr_bb = sr_lay.boundary
        assert sr_bb is not None
        srvss_m1pinbb = sr_lay.bounds(mask=metal1pin.mask, net=nets.vss, depth=1)
        srvdd_m1pinbb = sr_lay.bounds(mask=metal1pin.mask, net=nets.vdd, depth=1)
        srbl_m1pinbb = sr_lay.bounds(mask=metal1pin.mask, net=nets.bl, depth=1)
        srbln_m1pinbb = sr_lay.bounds(mask=metal1pin.mask, net=nets.bl_n, depth=1)
        srq_m1pinbb = sr_lay.bounds(mask=metal1pin.mask, net=nets.q, depth=1)
        # nq signal is left floating

        cell_height = sr_bb.top

        layouter.place(insts.tie, x=sr_bb.right, y=0.0)

        # vss/vdd
        shape = _geo.Rect.from_rect(rect=srvss_m1pinbb, right=cell_width)
        layouter.add_wire(net=nets.vss, wire=metal1, pin=metal1pin, shape=shape)
        shape = _geo.Rect.from_rect(rect=srvdd_m1pinbb, right=cell_width)
        layouter.add_wire(net=nets.vdd, wire=metal1, pin=metal1pin, shape=shape)

        # bl/bl_n
        _via1srbl_lay = layouter.wire_layout(net=nets.bl, wire=via1, rows=2)
        via1srbl_lay = layouter.place(_via1srbl_lay, origin=srbl_m1pinbb.center)
        via1srbl_m2bb = via1srbl_lay.bounds(mask=metal2.mask)

        _via1srbln_lay = layouter.wire_layout(net=nets.bl_n, wire=via1, rows=2)
        via1srbln_lay = layouter.place(_via1srbln_lay, origin=srbln_m1pinbb.center)
        via1srbln_m2bb = via1srbln_lay.bounds(mask=metal2.mask)

        shape = _geo.Rect(
            left=cache.colmux_left, bottom=0.0,
            right=cache.colmux_right, top=cell_height,
        )
        layouter.add_wire(net=nets.bl, wire=metal2, pin=metal2pin, shape=shape)
        if via1srbl_m2bb.left > cache.colmux_right:
            shape = _geo.Rect.from_rect(rect=via1srbl_m2bb, left=cache.colmux_left)
            layouter.add_wire(net=nets.bl, wire=metal2, shape=shape)
        elif via1srbl_m2bb.right < cache.colmux_left:
            shape = _geo.Rect.from_rect(rect=via1srbl_m2bb, right=cache.colmux_right)
            layouter.add_wire(net=nets.bl, wire=metal2, shape=shape)

        shape = _geo.Rect(
            left=cache.colmuxn_left, bottom=0.0,
            right=cache.colmuxn_right, top=cell_height,
        )
        layouter.add_wire(net=nets.bl_n, wire=metal2, pin=metal2pin, shape=shape)
        if via1srbln_m2bb.left > cache.colmuxn_right:
            shape = _geo.Rect.from_rect(rect=via1srbln_m2bb, left=cache.colmuxn_left)
            layouter.add_wire(net=nets.bl_n, wire=metal2, shape=shape)
        elif via1srbln_m2bb.right < cache.colmuxn_left:
            shape = _geo.Rect.from_rect(rect=via1srbln_m2bb, right=cache.colmuxn_right)
            layouter.add_wire(net=nets.bl_n, wire=metal2, shape=shape)

        # q
        layouter.add_wire(net=nets.q, wire=metal1, pin=metal1pin, shape=srq_m1pinbb)

        # boundary
        self.set_size(width=cell_width, height=cell_height)


class _WriteDriver(_FactoryCell["_SRAMFactory"]):
    def __init__(self, *, colmux: int, bits: int, fab: "_SRAMFactory", name: str):
        super().__init__(fab=fab, name=name)
        self.colmux = colmux
        self.bits = bits

    def _create_circuit(self):
        fab = self.fab
        spec = fab.spec
        stdcells = spec.stdcelllib.cells

        nmos = spec.nmos

        ff_cell = stdcells.sff1_x4
        nor_cell = stdcells.nor2_x0
        inv_cell = stdcells.inv_x0

        ckt = self.new_circuit()

        ffs = tuple(
            ckt.instantiate(ff_cell, name=f"ff[{bit}]")
            for bit in range(self.bits)
        )
        noras = tuple(
            ckt.instantiate(nor_cell, name=f"nora[{bit}]")
            for bit in range(self.bits)
        )
        invs = tuple(
            ckt.instantiate(inv_cell, name=f"inv[{bit}]")
            for bit in range(self.bits)
        )
        norbs = tuple(
            ckt.instantiate(nor_cell, name=f"norb[{bit}]")
            for bit in range(self.bits)
        )

        bl_pds = tuple(
            ckt.instantiate(
                nmos, name=f"blpd[{bit}]", l=spec.writedrive_l, w=spec.writedrive_w,
            )
            for bit in range(self.bits)
        )
        bln_pds = tuple(
            ckt.instantiate(
                nmos, name=f"blnpd[{bit}]", l=spec.writedrive_l, w=spec.writedrive_w,
            )
            for bit in range(self.bits)
        )

        cells: Tuple[_ckt._CellInstance] = (*ffs, *noras, *invs, *norbs)

        ckt.new_net(name="vss", external=True, childports=(
            *(cell.ports.vss for cell in cells),
            *(pd.ports.sourcedrain1 for pd in bl_pds),
            *(pd.ports.sourcedrain2 for pd in bln_pds),
            *(pd.ports.bulk for pd in (*bl_pds, *bln_pds)),
        ))
        ckt.new_net(name="vdd", external=True, childports=(
            cell.ports.vdd for cell in cells
        ))

        ckt.new_net(name="clk", external=True, childports=(
            ff.ports.ck for ff in ffs
        ))
        ckt.new_net(name="we_n", external=True, childports=(
            nor.ports.i1 for nor in (*noras, *norbs)
        ))

        for bit in range(self.bits):
            bl_pd = bl_pds[bit]
            bln_pd = bln_pds[bit]
            ff = ffs[bit]
            inv = invs[bit]
            nora = noras[bit]
            norb = norbs[bit]

            ckt.new_net(
                name=f"bl[{bit}]", external=True, childports=bl_pd.ports.sourcedrain2,
            )
            ckt.new_net(
                name=f"bl_n[{bit}]", external=True,
                childports=bln_pd.ports.sourcedrain1,
            )

            ckt.new_net(name=f"d[{bit}]", external=True, childports=ff.ports.i)
            ckt.new_net(name=f"d_latched[{bit}]", external=False, childports=(
                ff.ports.q, inv.ports.i, nora.ports.i0,
            ))
            ckt.new_net(name=f"d_n[{bit}]", external=False, childports=(
                inv.ports.nq, norb.ports.i0,
            ))

            ckt.new_net(name=f"bl_drive[{bit}]", external=False, childports=(
                nora.ports.nq, bl_pd.ports.gate,
            ))
            ckt.new_net(name=f"bln_drive[{bit}]", external=False, childports=(
                norb.ports.nq, bln_pd.ports.gate,
            ))

    def _create_layout(self):
        fab = self.fab
        tech = fab.tech
        spec = fab.spec
        cache = fab._cache

        ckt = self.circuit
        nets = ckt.nets
        insts = ckt.instances

        nwell = cache.nwell
        pwell = cache.pwell
        active = cache.active
        nimplant = cache.nimplant
        poly = cache.poly
        contact = cache.contact
        metal1 = cache.metal(1)
        metal1pin = cache.metalpin(1)
        via1 = cache.via(1)
        metal2 = cache.metal(2)
        metal2pin = cache.metalpin(2)

        pwell_net = None if pwell is None else nets.vss

        layouter = self.new_circuitlayouter()
        layout = layouter.layout

        colmux_width = self.colmux*cache.bit_width
        cell_width = self.bits*colmux_width

        actpoly_space = tech.computed.min_space(active, poly)
        chgate_space = spec.nmos.computed.min_contactgate_space
        m2pitch = tech.computed.min_pitch(primitive=metal2, down=True, up=True)

        ff_cell = spec.stdcelllib.cells.sff1_x4
        ff_bb = ff_cell.layout.boundary
        assert ff_bb is not None
        row_height = ff_bb.height

        # The layout of the write driver is with all the flipflop on top
        # of each other and then the other logic cell on top.

        if self.bits%2 == 0:
            # even number of bits
            y_logic = self.bits*row_height
            rot_logic = _geo.Rotation.R0
            cell_height = y_logic + row_height
        else:
            # odd number of bits
            y_logic = (self.bits + 1)*ff_bb.height
            rot_logic = _geo.Rotation.MX
            cell_height = y_logic

        y_m2blconn = cell_height - m2pitch
        y_m2blnconn = y_m2blconn - m2pitch

        y_ff = 0.0
        vss_m1bb: Optional[_geo.Rect]=None
        vdd_m1bb: Optional[_geo.Rect]=None
        vdd_nwellbb: Optional[_geo.Rect]=None
        via1clkff_m2bb0 = None
        via1wennora_m2bb0 = None
        for bit in range(self.bits):
            d_net = nets[f"d[{bit}]"]
            dn_net = nets[f"d_n[{bit}]"]
            dlatch_net = nets[f"d_latched[{bit}]"]

            bl_net = nets[f"bl[{bit}]"]
            bln_net = nets[f"bl_n[{bit}]"]
            bldrv_net = nets[f"bl_drive[{bit}]"]
            blndrv_net = nets[f"bln_drive[{bit}]"]

            blpd = insts[f"blpd[{bit}]"]
            blnpd = insts[f"blnpd[{bit}]"]
            ff = insts[f"ff[{bit}]"]
            inv = insts[f"inv[{bit}]"]
            nora = insts[f"nora[{bit}]"]
            norb = insts[f"norb[{bit}]"]

            dxy = _geo.Point(x=bit*colmux_width, y=0.0)
            colmux_left = cache.colmux_left + bit*colmux_width
            colmux_right = cache.colmux_right + bit*colmux_width
            colmuxn_left = cache.colmuxn_left + bit*colmux_width
            colmuxn_right = cache.colmuxn_right + bit*colmux_width

            if bit%2 == 0:
                ff_lay = layouter.place(ff, x=0.0, y=y_ff)
            else:
                ff_lay = layouter.place(ff,
                    x=0.0, y=(y_ff + row_height), rotation=_geo.Rotation.MX,
                )
            y_ff += row_height

            ffvss_m1pinbb = ff_lay.bounds(mask=metal1pin.mask, net=nets.vss)
            shape = _geo.Rect.from_rect(rect=ffvss_m1pinbb, right=cell_width)
            layouter.add_wire(
                net=nets.vss, wire=metal1, pin=metal1pin, shape=shape,
            )

            ffvdd_m1pinbb = ff_lay.bounds(mask=metal1pin.mask, net=nets.vdd)
            shape = _geo.Rect.from_rect(rect=ffvdd_m1pinbb, right=cell_width)
            layouter.add_wire(
                net=nets.vdd, wire=metal1, pin=metal1pin, shape=shape,
            )

            if nwell is not None:
                ff_nwellbb = ff_lay.bounds(mask=nwell.mask)
                shape=_geo.Rect.from_rect(
                    rect=ff_nwellbb, right=(cell_width - ff_nwellbb.left),
                )
                layouter.add_wire(net=nets.vdd, wire=nwell, shape=shape)
            if pwell is not None:
                ff_pwellbb = ff_lay.bounds(mask=nwell.mask)
                shape=_geo.Rect.from_rect(
                    rect=ff_pwellbb, right=(cell_width - ff_pwellbb.left),
                )
                layouter.add_wire(net=nets.vss, wire=nwell, shape=shape)

            x_logic = bit*colmux_width
            nora_lay = layouter.place(nora, x=x_logic, y=y_logic, rotation=rot_logic)
            nora_bb = nora_lay.boundary
            assert nora_bb is not None
            x_logic = nora_bb.right
            inv_lay = layouter.place(inv, x=x_logic, y=y_logic, rotation=rot_logic)
            inv_bb = inv_lay.boundary
            assert inv_bb is not None
            x_logic = inv_bb.right
            norb_lay = layouter.place(norb, x=x_logic, y=y_logic, rotation=rot_logic)
            norb_nimplbb = norb_lay.bounds(mask=nimplant.mask)
            norb_bb = norb_lay.boundary
            assert norb_bb is not None
            x_logic = norb_bb.right

            # vss/vdd/nwell
            if bit == 0:
                noravss_m1pinbb = nora_lay.bounds(mask=metal1pin.mask, net=nets.vss)
                shape = _geo.Rect.from_rect(rect=noravss_m1pinbb, right=cell_width)
                vss_m1lay = layouter.add_wire(
                    net=nets.vss, wire=metal1, pin=metal1pin, shape=shape,
                )
                vss_m1bb = vss_m1lay.bounds()

                noravdd_m1pinbb = nora_lay.bounds(mask=metal1pin.mask, net=nets.vdd)
                shape = _geo.Rect.from_rect(rect=noravdd_m1pinbb, right=cell_width)
                vdd_m1lay = layouter.add_wire(
                    net=nets.vdd, wire=metal1, pin=metal1pin, shape=shape,
                )
                vdd_m1bb = vdd_m1lay.bounds()

                if nwell is not None:
                    nora_nwellbb = nora_lay.bounds(mask=nwell.mask)
                    shape=_geo.Rect.from_rect(
                        rect=nora_nwellbb, right=(cell_width - nora_nwellbb.left),
                    )
                    vdd_nwelllay = layouter.add_wire(net=nets.vdd, wire=nwell, shape=shape)
                    vdd_nwellbb = vdd_nwelllay.bounds()
                if pwell is not None:
                    nora_pwellbb = nora_lay.bounds(mask=nwell.mask)
                    shape=_geo.Rect.from_rect(
                        rect=nora_pwellbb, right=(cell_width - nora_pwellbb.left),
                    )
                    layouter.add_wire(net=nets.vss, wire=nwell, shape=shape)
            assert vss_m1bb is not None
            assert vdd_m1bb is not None
            assert vdd_nwellbb is not None

            # Add the two pd transistors
            # Create sublayouts
            _chblpd_lay = layouter.wire_layout(
                net=bl_net, wire=contact, well_net=pwell_net, rows=5,
                bottom=active, bottom_implant=nimplant, bottom_well=pwell,
                bottom_enclosure="tall", top_enclosure="tall",
            )
            _chblpd_actbb = _chblpd_lay.bounds(mask=active.mask)
            _blpd_lay = layouter.inst_layout(inst=blpd)
            _blpd_nimplbb = _blpd_lay.bounds(mask=nimplant.mask)
            _blpd_actbb = _blpd_lay.bounds(mask=active.mask)
            _blpd_polybb = _blpd_lay.bounds(mask=poly.mask)
            _chvsspd_lay = layouter.wire_layout(
                net=nets.vss, wire=contact, well_net=pwell_net,
                bottom=active, bottom_implant=nimplant, bottom_well=pwell,
                bottom_enclosure="tall", bottom_height=spec.writedrive_w,
                top_enclosure="tall", top_height=spec.writedrive_w,
            )
            _blnpd_lay = layouter.inst_layout(inst=blnpd)
            _blnpd_polybb = _blnpd_lay.bounds(mask=poly.mask)
            _chblnpd_lay = layouter.wire_layout(
                net=bln_net, wire=contact, well_net=pwell_net, rows=5,
                bottom=active, bottom_implant=nimplant, bottom_well=pwell,
                bottom_enclosure="tall", top_enclosure="tall",
            )
            _chblnpd_nimplbb = _chblnpd_lay.bounds(mask=nimplant.mask)

            # Compute placement
            x_chblnpd = norb_nimplbb.right + nimplant.min_space - _chblnpd_nimplbb.left
            x_blnpd = x_chblnpd + 0.5*contact.width + chgate_space - _blnpd_polybb.left
            x_chvsspd = x_blnpd + _blnpd_polybb.right + chgate_space + 0.5*contact.width
            x_blpd = x_chvsspd + 0.5*contact.width + chgate_space - _blpd_polybb.left
            x_chblpd = x_blpd + _blpd_polybb.right + chgate_space + 0.5*contact.width

            y_blpd = y_logic + max(
                # We take a little margin by using full min_space and not 0.5*min_space
                nimplant.min_space - _blpd_nimplbb.bottom,
                poly.min_space - _blpd_polybb.bottom,
                active.min_space - _blpd_actbb.bottom,
            )
            y_chblpd = y_blpd + _blpd_actbb.top - _chblpd_actbb.top
            y_chvsspd = y_blpd
            y_blnpd = y_blpd
            y_chblnpd = y_chblpd

            # Place sublayout
            chblpd_lay = layouter.place(_chblpd_lay, x=x_chblpd, y=y_chblpd)
            chblpd_nimplbb = chblpd_lay.bounds(mask=nimplant.mask)
            chblpd_actbb = chblpd_lay.bounds(mask=active.mask)
            chblpd_m1bb = chblpd_lay.bounds(mask=metal1.mask)
            blpd_lay = layouter.place(_blpd_lay, x=x_blpd, y=y_blpd)
            blpd_actbb = blpd_lay.bounds(mask=active.mask)
            blpd_polybb = blpd_lay.bounds(mask=poly.mask)
            layouter.place(_chvsspd_lay, x=x_chvsspd, y=y_chvsspd)
            blnpd_lay = layouter.place(_blnpd_lay, x=x_blnpd, y=y_blnpd)
            blnpd_polybb = blnpd_lay.bounds(mask=poly.mask)
            chblnpd_lay = layouter.place(_chblnpd_lay, x=x_chblnpd, y=y_chblnpd)
            chblnpd_nimplbb = chblnpd_lay.bounds(mask=nimplant.mask)
            chblnpd_actbb = chblnpd_lay.bounds(mask=active.mask)
            chblnpd_m1bb = chblnpd_lay.bounds(mask=metal1.mask)

            # Connections
            # bl/bl_n
            _via1blpd_lay = layouter.wire_layout(
                net=bl_net, wire=via1, rows=2,
                bottom_enclosure="tall", top_enclosure="tall",
            )
            _via1blpd_m1bb = _via1blpd_lay.bounds(mask=metal1.mask)
            x_via1blpd = chblpd_m1bb.left - _via1blpd_m1bb.left
            y_via1blpd = chblpd_m1bb.top - _via1blpd_m1bb.top
            via1blpd_lay = layouter.place(_via1blpd_lay, x=x_via1blpd, y=y_via1blpd)
            via1blpd_m2bb = via1blpd_lay.bounds(mask=metal2.mask)

            _via1blnpd_lay = layouter.wire_layout(
                net=bln_net, wire=via1, rows=2,
                bottom_enclosure="tall", top_enclosure="tall",
            )
            _via1blnpd_m1bb = _via1blnpd_lay.bounds(mask=metal1.mask)
            x_via1blnpd = chblnpd_m1bb.right - _via1blnpd_m1bb.right
            y_via1blnpd = chblnpd_m1bb.top - _via1blnpd_m1bb.top
            via1blnpd_lay = layouter.place(_via1blnpd_lay, x=x_via1blnpd, y=y_via1blnpd)
            via1blnpd_m2bb = via1blnpd_lay.bounds(mask=metal2.mask)

            shape = _geo.Rect.from_rect(
                rect=chblpd_actbb, bottom=(chblpd_actbb.top - spec.writedrive_w),
            )
            layouter.add_wire(
                net=bl_net, wire=active, well_net=pwell,
                implant=nimplant, well=pwell, shape=shape,
            )

            shape = _geo.Rect.from_rect(rect=chblnpd_nimplbb, right=chblpd_nimplbb.right)
            layout.add_shape(prim=nimplant, net=None, shape=shape)

            shape = _geo.Rect.from_rect(
                rect=chblnpd_actbb, bottom=(chblnpd_actbb.top - spec.writedrive_w),
            )
            layouter.add_wire(
                net=bln_net, wire=active, well_net=pwell,
                implant=nimplant, well=pwell, shape=shape,
            )

            conn_top = y_m2blconn + 0.5*metal2.min_width
            conn_bottom = y_m2blconn - 0.5*metal2.min_width
            shape = _geo.Polygon.from_floats(points=(
                (via1blpd_m2bb.left, via1blpd_m2bb.bottom),
                (via1blpd_m2bb.right, via1blpd_m2bb.bottom),
                (via1blpd_m2bb.right, conn_top),
                (colmux_right, conn_top),
                (colmux_right, cell_height),
                (colmux_left, cell_height),
                (colmux_left, conn_bottom),
                (via1blpd_m2bb.left, conn_bottom),
                (via1blpd_m2bb.left, via1blpd_m2bb.bottom),
            ))
            layouter.add_wire(net=bl_net, wire=metal2, pin=metal2pin, shape=shape)

            conn_top = y_m2blnconn + 0.5*metal2.min_width
            conn_bottom = y_m2blnconn - 0.5*metal2.min_width
            shape = _geo.Polygon.from_floats(points=(
                (via1blnpd_m2bb.left, via1blnpd_m2bb.bottom),
                (via1blnpd_m2bb.right, via1blnpd_m2bb.bottom),
                (via1blnpd_m2bb.right, conn_top),
                (colmuxn_right, conn_top),
                (colmuxn_right, cell_height),
                (colmuxn_left, cell_height),
                (colmuxn_left, conn_bottom),
                (via1blnpd_m2bb.left, conn_bottom),
                (via1blnpd_m2bb.left, via1blnpd_m2bb.bottom),
            ))
            layouter.add_wire(net=bln_net, wire=metal2, pin=metal2pin, shape=shape)

            # bl_drive/bln_drive
            bldrvnora_m1pinbb = nora_lay.bounds(
                mask=metal1pin.mask, net=bldrv_net, depth=1,
            )
            blndrvnorb_m1pinbb = norb_lay.bounds(
                mask=metal1pin.mask, net=blndrv_net, depth=1,
            )

            _chpadblndrv_lay = layouter.wire_layout(
                net=blndrv_net, wire=contact, rows=2,
                bottom=poly, bottom_enclosure="tall", top_enclosure="wide",
            )
            _chpadblndrv_polybb = _chpadblndrv_lay.bounds(mask=poly.mask)
            _chpadblndrv_m1bb = _chpadblndrv_lay.bounds(mask=metal1.mask)
            x_chpadblndrv = blndrvnorb_m1pinbb.right - _chpadblndrv_m1bb.left
            y_chpadblndrv = blpd_actbb.top + actpoly_space - _chpadblndrv_polybb.bottom
            chpadblndrv_lay = layouter.place(
                _chpadblndrv_lay, x=x_chpadblndrv, y=y_chpadblndrv,
            )
            chpadblndrv_polybb = chpadblndrv_lay.bounds(mask=poly.mask)

            shape = _geo.Rect.from_rect(rect=chpadblndrv_polybb, right=blnpd_polybb.right)
            layouter.add_wire(net=blndrv_net, wire=poly, shape=shape)

            _chpadbldrv_lay = layouter.wire_layout(
                net=bldrv_net, wire=contact, rows=2,
                bottom=poly, bottom_enclosure="tall", top_enclosure="tall",
            )
            _chpadbldrv_polybb = _chpadbldrv_lay.bounds(mask=poly.mask)
            _chpadbldrv_m1bb = _chpadbldrv_lay.bounds(mask=metal1.mask)
            _via1bldrv_lay = layouter.wire_layout(
                net=bldrv_net, wire=via1, rows=2, bottom_enclosure="tall",
                top_enclosure="tall",
            )
            _via1bldrv_m1bb = _via1bldrv_lay.bounds(mask=metal1.mask)
            _via1bldrv_m2bb = _via1bldrv_lay.bounds(mask=metal2.mask)

            x_via1bldrvpd = (
                via1blnpd_m2bb.left - metal2.min_space - _via1bldrv_m2bb.right
            )
            x_chpadbldrv = x_via1bldrvpd
            y_chpadbldrv = (
                chpadblndrv_polybb.top + poly.min_space - _chpadbldrv_polybb.bottom
            )
            y_via1bldrv = y_chpadbldrv

            chpadbldrv_lay = layouter.place(
                _chpadbldrv_lay, x=x_chpadbldrv, y=y_chpadbldrv,
            )
            chpadbldrv_polybb = chpadbldrv_lay.bounds(mask=poly.mask)

            shape = _geo.Rect.from_rect(rect=chpadbldrv_polybb, right=blpd_polybb.right)
            layouter.add_wire(net=bldrv_net, wire=poly, shape=shape)
            shape = _geo.Rect.from_rect(rect=blpd_polybb, top=chpadbldrv_polybb.top)
            layouter.add_wire(net=bldrv_net, wire=poly, shape=shape)

            via1bldrvpd_lay = layouter.place(_via1bldrv_lay, x=x_via1bldrvpd, y=y_via1bldrv)
            via1bldrvpd_m2bb = via1bldrvpd_lay.bounds(mask=metal2.mask)
            x_via1bldrvnora = bldrvnora_m1pinbb.left - _via1bldrv_m1bb.left
            via1bldrvnora_lay = layouter.place(
                _via1bldrv_lay, x=x_via1bldrvnora, y=y_via1bldrv,
            )
            via1bldrvnora_m2bb = via1bldrvnora_lay.bounds(mask=metal2.mask)

            shape = _geo.Rect.from_rect(rect=via1bldrvnora_m2bb, right=via1bldrvpd_m2bb.right)
            layouter.add_wire(net=bldrv_net, wire=metal2, shape=shape)

            # d
            dff_m1pinbb = ff_lay.bounds(mask=metal1pin.mask, net=d_net, depth=1)
            layouter.add_wire(net=d_net, wire=metal1, pin=metal1pin, shape=dff_m1pinbb)

            # dlatch
            dlatchff_m1pinbb = ff_lay.bounds(mask=metal1pin.mask, net=dlatch_net, depth=1)
            dlatchinv_m1pinbb = inv_lay.bounds(mask=metal1pin.mask, net=dlatch_net, depth=1)
            dlatchnora_m1pinbb = nora_lay.bounds(mask=metal1pin.mask, net=dlatch_net, depth=1)

            _via1dlatch_lay = layouter.wire_layout(
                net=dlatch_net, wire=via1, rows=2,
                bottom_enclosure="tall", top_enclosure="tall"
            )
            _via1dlatch_m1bb = _via1dlatch_lay.bounds(mask=metal1.mask)

            x_via1dlatchff = dlatchff_m1pinbb.center.x
            y_via1dlatchff = dlatchff_m1pinbb.top - _via1dlatch_m1bb.top
            x_via1dlatchinv = dlatchinv_m1pinbb.center.x
            y_via1dlatchinv = dlatchinv_m1pinbb.bottom - _via1dlatch_m1bb.bottom
            x_via1dlatchnora = dlatchnora_m1pinbb.center.x
            y_via1dlatchnora = dlatchnora_m1pinbb.bottom - _via1dlatch_m1bb.bottom
            via1dlatchff_lay = layouter.place(_via1dlatch_lay,
                x=x_via1dlatchff, y=y_via1dlatchff,
            )
            via1dlatchff_m2bb = via1dlatchff_lay.bounds(mask=metal2.mask)
            via1dlatchinv_lay = layouter.place(_via1dlatch_lay,
                x=x_via1dlatchinv, y=y_via1dlatchinv,
            )
            via1dlatchinv_m2bb = via1dlatchinv_lay.bounds(mask=metal2.mask)
            via1dlatchnora_lay = layouter.place(_via1dlatch_lay,
                x=x_via1dlatchnora, y=y_via1dlatchnora,
            )
            via1dlatchnora_m2bb = via1dlatchnora_lay.bounds(mask=metal2.mask)

            if via1dlatchff_m2bb.right > via1dlatchinv_m2bb.right:
                shape = _geo.Polygon.from_floats(points=(
                    (via1dlatchinv_m2bb.left, via1dlatchff_m2bb.bottom),
                    (via1dlatchff_m2bb.right, via1dlatchff_m2bb.bottom),
                    (via1dlatchff_m2bb.right, via1dlatchff_m2bb.top),
                    (via1dlatchinv_m2bb.right, via1dlatchff_m2bb.top),
                    (via1dlatchinv_m2bb.right, via1dlatchinv_m2bb.top),
                    (via1dlatchnora_m2bb.left, via1dlatchinv_m2bb.top),
                    (via1dlatchnora_m2bb.left, via1dlatchnora_m2bb.bottom),
                    (via1dlatchinv_m2bb.left, via1dlatchnora_m2bb.bottom),
                    (via1dlatchinv_m2bb.left, via1dlatchff_m2bb.bottom),
                ))
            elif via1dlatchff_m2bb.left < via1dlatchnora_m2bb.left:
                shape = _geo.Polygon.from_floats(points=(
                    (via1dlatchff_m2bb.left, via1dlatchff_m2bb.bottom),
                    (via1dlatchff_m2bb.left, via1dlatchinv_m2bb.top),
                    (via1dlatchinv_m2bb.right, via1dlatchinv_m2bb.top),
                    (via1dlatchinv_m2bb.right, via1dlatchinv_m2bb.bottom),
                    (via1dlatchff_m2bb.right, via1dlatchinv_m2bb.bottom),
                    (via1dlatchff_m2bb.right, via1dlatchff_m2bb.bottom),
                    (via1dlatchff_m2bb.left, via1dlatchff_m2bb.bottom),
                ))
            else:
                shape = _geo.Polygon.from_floats(points=(
                    (via1dlatchff_m2bb.left, via1dlatchff_m2bb.bottom),
                    (via1dlatchff_m2bb.left, via1dlatchnora_m2bb.bottom),
                    (via1dlatchnora_m2bb.left, via1dlatchnora_m2bb.bottom),
                    (via1dlatchnora_m2bb.left, via1dlatchinv_m2bb.top),
                    (via1dlatchinv_m2bb.right, via1dlatchinv_m2bb.top),
                    (via1dlatchinv_m2bb.right, via1dlatchinv_m2bb.bottom),
                    (via1dlatchff_m2bb.right, via1dlatchinv_m2bb.bottom),
                    (via1dlatchff_m2bb.right, via1dlatchff_m2bb.bottom),
                    (via1dlatchff_m2bb.left, via1dlatchff_m2bb.bottom),
                ))
            layouter.add_wire(net=dlatch_net, wire=metal2, shape=shape)

            # dn
            dninv_m1pinbb = inv_lay.bounds(mask=metal1pin.mask, net=dn_net, depth=1)
            dnnorb_m1pinbb = norb_lay.bounds(mask=metal1pin.mask, net=dn_net, depth=1)
            m1_bottom = max(dninv_m1pinbb.bottom, dnnorb_m1pinbb.bottom)

            _via1dn_lay = layouter.wire_layout(
                net=dn_net, wire=via1, rows=2,
                bottom_enclosure="tall", top_enclosure="tall",
            )
            _via1dn_m1bb = _via1dn_lay.bounds(mask=metal1.mask)
            y_via1dn = m1_bottom - _via1dn_m1bb.bottom
            x_via1dninv = dninv_m1pinbb.center.x
            x_via1dnnorb = dnnorb_m1pinbb.center.x

            via1dninv_lay = layouter.place(_via1dn_lay, x=x_via1dninv, y=y_via1dn)
            via1dninv_m2bb = via1dninv_lay.bounds(mask=metal2.mask)
            via1dnnorb_lay = layouter.place(_via1dn_lay, x=x_via1dnnorb, y=y_via1dn)
            via1dnnorb_m2bb = via1dnnorb_lay.bounds(mask=metal2.mask)

            # clk
            clkff_m1pinbb = ff_lay.bounds(mask=metal1pin.mask, net=nets.clk, depth=1)
            via1clkff_lay = layouter.add_wire(
                net=nets.clk, wire=via1, rows=2, origin=clkff_m1pinbb.center,
                bottom_enclosure="tall", top_enclosure="tall",
            )
            if bit == 0:
                via1clkff_m2bb0 = via1clkff_lay.bounds(mask=metal2.mask)
            assert via1clkff_m2bb0 is not None
            if bit == (self.bits - 1):
                via1clkff_m2bb = via1clkff_lay.bounds(mask=metal2.mask)

                shape = _geo.Rect.from_rect(rect=via1clkff_m2bb0, top=via1clkff_m2bb.top)
                layouter.add_wire(net=nets.clk, wire=metal2, pin=metal2pin, shape=shape)

            # we_n
            wennora_m1pinbb = nora_lay.bounds(mask=metal1pin.mask, net=nets.we_n, depth=1)
            wennorb_m1pinbb = norb_lay.bounds(mask=metal1pin.mask, net=nets.we_n, depth=1)
            m1_bottom = max(wennora_m1pinbb.bottom, wennorb_m1pinbb.bottom)

            _via1wen_lay = layouter.wire_layout(
                net=nets.we_n, wire=via1, rows=2,
                bottom_enclosure="tall", top_enclosure="tall",
            )
            _via1wen_m1bb = _via1wen_lay.bounds(mask=metal1.mask)
            y_via1wen = m1_bottom - _via1wen_m1bb.bottom

            via1wennora_lay = layouter.place(_via1wen_lay,
                x=wennora_m1pinbb.center.x, y=y_via1wen,
            )
            if bit == 0:
               via1wennora_m2bb0 = via1wennora_lay.bounds(mask=metal2.mask)
            assert via1wennora_m2bb0 is not None
            via1wennorb_lay = layouter.place(_via1wen_lay,
                x=wennorb_m1pinbb.center.x, y=y_via1wen,
            )
            if bit == (self.bits - 1):
                via1wennorb_m2bb = via1wennorb_lay.bounds(mask=metal2.mask)

                shape = _geo.Rect.from_rect(
                    rect=via1wennora_m2bb0, right=via1wennorb_m2bb.right,
                )
                layouter.add_wire(net=nets.we_n, wire=metal2, pin=metal2pin, shape=shape)

            shape = _geo.Rect.from_rect(rect=via1dninv_m2bb, right=via1dnnorb_m2bb.right)
            layouter.add_wire(net=dn_net, wire=metal2, shape=shape)

        self.set_size(width=cell_width, height=cell_height)


class _ClockBufWordEnable(_FactoryCell["_SRAMFactory"]):
    def _create_circuit(self):
        spec = self.fab.spec
        stdcells = spec.stdcelllib.cells

        buf_cell = stdcells.buf_x2
        ff_cell = stdcells.sff1_x4
        nand_cell = stdcells.nand2_x0

        ckt = self.new_circuit()

        clk_buf = ckt.instantiate(buf_cell, name="clkbuf")
        we_ff = ckt.instantiate(ff_cell, name="weff")
        we_nand = ckt.instantiate(nand_cell, name="wenand")

        ckt.new_net(name="vss", external=True, childports=(
            clk_buf.ports.vss, we_ff.ports.vss, we_nand.ports.vss,
        ))
        ckt.new_net(name="vdd", external=True, childports=(
            clk_buf.ports.vdd, we_ff.ports.vdd, we_nand.ports.vdd,
        ))

        ckt.new_net(name="clkup", external=True, childports=clk_buf.ports.i)
        ckt.new_net(name="clklow", external=True, childports=(
            clk_buf.ports.q, we_ff.ports.ck,
        ))

        ckt.new_net(name="we", external=True, childports=we_ff.ports.i)
        ckt.new_net(name="we_en", external=True, childports=we_nand.ports.i0)
        ckt.new_net(name="we_latched", external=False, childports=(
            we_ff.ports.q, we_nand.ports.i1,
        ))
        ckt.new_net(name="we_n", external=True, childports=we_nand.ports.nq)

    def _create_layout(self):
        fab = self.fab
        spec = fab.spec
        cache = fab._cache

        nets = self.circuit.nets
        insts = self.circuit.instances

        metal1 = cache.metal(1)
        metal1pin = cache.metalpin(1)
        via1 = cache.via(1)
        metal2 = cache.metal(2)
        metal2pin = cache.metalpin(2)

        layouter = self.new_circuitlayouter()
        layout = layouter.layout

        x = 0.0
        y = 0.0

        # Place the subcells
        buf_lay = layouter.place(insts["clkbuf"], x=x, y=y)
        buf_bb = buf_lay.boundary
        assert buf_bb is not None
        x = buf_bb.right
        ff_lay = layouter.place(insts["weff"], x=x, y=y)
        ff_bb = ff_lay.boundary
        assert ff_bb is not None
        x = ff_bb.right
        nand_lay = layouter.place(insts["wenand"], x=x, y=y)
        nand_bb = nand_lay.boundary
        assert nand_bb is not None
        x = nand_bb.right

        cell_width = x
        cell_height = nand_bb.top

        # clkup
        clkupbuf_m1pinbb = buf_lay.bounds(mask=metal1pin.mask, net=nets.clkup, depth=1)
        layouter.add_wire(
            net=nets.clkup, wire=metal1, pin=metal1pin, shape=clkupbuf_m1pinbb,
        )

        # we
        weff_m1pinbb = ff_lay.bounds(mask=metal1pin.mask, net=nets.we, depth=1)
        layouter.add_wire(
            net=nets.we, wire=metal1, pin=metal1pin, shape=weff_m1pinbb,
        )

        # we_en
        weennand_m1pinbb = nand_lay.bounds(mask=metal1pin.mask, net=nets.we_en, depth=1)
        layouter.add_wire(net=nets.we_en, wire=metal1, pin=metal1pin, shape=weennand_m1pinbb)

        # we_n
        wennand_m1pinbb = nand_lay.bounds(mask=metal1pin.mask, net=nets.we_n, depth=1)
        layouter.add_wire(
            net=nets.we_n, wire=metal1, pin=metal1pin, shape=wennand_m1pinbb,
        )

        # clklow
        clklowbuf_m1pinbb = buf_lay.bounds(mask=metal1pin.mask, net=nets.clklow, depth=1)
        clklowff_m1pinbb = ff_lay.bounds(mask=metal1pin.mask, net=nets.clklow, depth=1)
        _via1clklow_lay = layouter.wire_layout(
            net=nets.clklow, wire=via1, rows=2,
            bottom_enclosure="tall", top_enclosure="tall",
        )
        x_via1clklowbuf = clklowbuf_m1pinbb.center.x
        x_via1clklowff = clklowff_m1pinbb.center.x
        y_via1clklow = clklowbuf_m1pinbb.center.y
        via1clklowbuf_lay = layouter.place(
            _via1clklow_lay, x=x_via1clklowbuf, y=y_via1clklow,
        )
        via1clklowbuf_m2bb = via1clklowbuf_lay.bounds(mask=metal2.mask)
        via1clklowff_lay = layouter.place(
            _via1clklow_lay, x=x_via1clklowff, y=y_via1clklow,
        )
        via1clklowff_m2bb = via1clklowff_lay.bounds(mask=metal2.mask)
        shape = _geo.Rect.from_rect(rect=via1clklowbuf_m2bb, right=via1clklowff_m2bb.right)
        layouter.add_wire(net=nets.clklow, wire=metal2, pin=metal2pin, shape=shape)

        # we_latched
        weltchff_m1pinbb = ff_lay.bounds(mask=metal1pin.mask, net=nets.we_latched, depth=1)
        weltchnand_m1pinbb = nand_lay.bounds(mask=metal1pin.mask, net=nets.we_latched, depth=1)
        _via1weltch_lay = layouter.wire_layout(
            net=nets.we_latched, wire=via1, rows=2,
            bottom_enclosure="tall", top_enclosure="tall",
        )
        _via1weltch_m1bb = _via1weltch_lay.bounds(mask=metal1.mask)
        x_via1weltchff = weltchff_m1pinbb.center.x
        x_via1weltchnand = weltchnand_m1pinbb.center.x
        y_via1weltch = weltchff_m1pinbb.center.y
        via1weltchff_lay = layouter.place(
            _via1weltch_lay, x=x_via1weltchff, y=y_via1weltch,
        )
        via1weltchff_m2bb = via1weltchff_lay.bounds(mask=metal2.mask)
        via1weltchnand_lay = layouter.place(
            _via1weltch_lay, x=x_via1weltchnand, y=y_via1weltch,
        )
        via1weltchnand_m2bb = via1weltchnand_lay.bounds(mask=metal2.mask)
        shape = _geo.Rect.from_rect(rect=via1weltchff_m2bb, right=via1weltchnand_m2bb.right)
        layouter.add_wire(net=nets.we_latched, wire=metal2, shape=shape)

        # vss/vdd
        vss_bb = layout.bounds(mask=metal1pin.mask, net=nets.vss, depth=2)
        layouter.add_wire(net=nets.vss, wire=metal1, pin=metal1pin, shape=vss_bb)
        vdd_bb = layout.bounds(mask=metal1pin.mask, net=nets.vdd, depth=2)
        layouter.add_wire(net=nets.vdd, wire=metal1, pin=metal1pin, shape=vdd_bb)

        # boundary
        self.set_size(width=cell_width, height=cell_height)


class _ColumnPeriphery(_FactoryCell[_factory_type_], Generic[_factory_type_]):
    def __init__(self, *,
        bits: int, colmux: int,
        precharge_kwargs: Dict[str, Any], colmux_kwargs: Dict[str, Any],
        fab: _factory_type_, name: str,
    ):
        super().__init__(fab=fab, name=name)

        # TODO compute driverbits from ff dimensions
        driverbits = 2
        if (bits%driverbits) != 0:
            raise ValueError(
                f"bits ({bits}) not a multiple driverbits ({driverbits})",
            )
        self.bits = bits
        self.colmux = colmux
        self.driverbits = driverbits
        self.precharge_kwargs = precharge_kwargs
        self.colmux_kwargs = colmux_kwargs

    def _create_circuit(self):
        fab = self.fab

        ckt = self.new_circuit()

        cell = fab.precharge(**self.precharge_kwargs)
        prechargers = tuple(
            ckt.instantiate(cell, name=f"precharge[{column}]")
            for column in range(self.bits*self.colmux)
        )
        cell = fab.colmux(columns=self.colmux, **self.colmux_kwargs)
        colmuxes = tuple(
            ckt.instantiate(cell, name=f"colmux[{bit}]")
            for bit in range(self.bits)
        )
        cell = fab.senseamp(colmux=self.colmux)
        senseamps = tuple(
            ckt.instantiate(cell, name=f"senseamp[{bit}]")
            for bit in range(self.bits)
        )
        cell = fab.writedriver(colmux=self.colmux, bits=self.driverbits)
        n_wdrivers = self.bits//self.driverbits
        wdrivers = tuple(
            ckt.instantiate(cell, name=f"writedrive[{wdrive}]")
            for wdrive in range(n_wdrivers)
        )
        clkwe = ckt.instantiate(fab.clockwe(), name="clkwe")

        ckt.new_net(name="vss", external=True, childports=(
            *(colmux.ports.vss for colmux in colmuxes),
            *(senseamp.ports.vss for senseamp in senseamps),
            *(wdrive.ports.vss for wdrive in wdrivers),
            clkwe.ports.vss,
        ))
        ckt.new_net(name="vdd", external=True, childports=(
            *(precharge.ports.vdd for precharge in prechargers),
            *(senseamp.ports.vdd for senseamp in senseamps),
            *(wdrive.ports.vdd for wdrive in wdrivers),
            clkwe.ports.vdd,
        ))

        ckt.new_net(name="clk", external=True, childports=clkwe.ports.clkup)
        ckt.new_net(name="intclk", external=False, childports=(
            clkwe.ports.clklow, *(wdrive.ports.clk for wdrive in wdrivers)
        ))

        ckt.new_net(name="precharge_n", external=True, childports=(
            precharge.ports.precharge_n for precharge in prechargers
        ))
        ckt.new_net(name="we", external=True, childports=clkwe.ports.we)
        ckt.new_net(name="we_en", external=True, childports=clkwe.ports.we_en)
        ckt.new_net(name="we_n", external=False, childports=(
            clkwe.ports.we_n, *(wdrive.ports.we_n for wdrive in wdrivers),
        ))

        for bit in range(self.bits):
            q_name = f"q[{bit}]"
            d_name = f"d[{bit}]"
            muxbl_name = f"muxbl[{bit}]"
            muxbln_name = f"muxbl_n[{bit}]"

            senseamp = senseamps[bit]
            wdrive = wdrivers[bit//self.driverbits]
            wdrive_bit = bit%self.driverbits
            wdrive_d = f"d[{wdrive_bit}]"
            wdrive_bl = f"bl[{wdrive_bit}]"
            wdrive_bln = f"bl_n[{wdrive_bit}]"
            colmux = colmuxes[bit]

            ckt.new_net(name=q_name, external=True, childports=senseamp.ports.q)
            ckt.new_net(name=d_name, external=True, childports=wdrive.ports[wdrive_d])
            ckt.new_net(name=muxbl_name, external=False, childports=(
                colmux.ports.muxbl, senseamp.ports.bl, wdrive.ports[wdrive_bl],
            ))
            ckt.new_net(name=muxbln_name, external=False, childports=(
                colmux.ports.muxbl_n, senseamp.ports.bl_n, wdrive.ports[wdrive_bln],
            ))

            for n_colmux in range(self.colmux):
                cmbl_name = f"bl[{n_colmux}]"
                cmbln_name = f"bl_n[{n_colmux}]"
                column = bit*self.colmux + n_colmux
                bl_name = f"bl[{column}]"
                bln_name = f"bl_n[{column}]"

                precharge = prechargers[column]
                ckt.new_net(name=bl_name, external=True, childports=(
                    precharge.ports.bl, colmux.ports[cmbl_name],
                ))
                ckt.new_net(name=bln_name, external=True, childports=(
                    precharge.ports.bl_n, colmux.ports[cmbln_name]
                ))

        for n_colmux in range(self.colmux):
            col_name = f"mux[{n_colmux}]"
            ckt.new_net(name=col_name, external=True, childports=(
                colmux.ports[col_name] for colmux in colmuxes
            ))

    def _create_layout(self):
        fab = self.fab
        tech = fab.tech
        spec = fab.spec
        cache = fab._cache

        columns = self.bits*self.colmux
        cell_width = columns*cache.bit_width

        nets = self.circuit.nets
        insts = self.circuit.instances

        metal1 = cache.metal(1)
        metal1pin = cache.metalpin(1)
        via1 = cache.via(1)
        metal2 = cache.metal(2)
        metal2pin = cache.metalpin(2)
        via2 = cache.via(2)
        metal3 = cache.metal(3)
        metal3pin = cache.metalpin(3)

        layouter = self.new_circuitlayouter()
        layout = layouter.layout

        m3pitch = tech.computed.min_pitch(metal3, down=True, up=True)

        # Layout the cell from top to bottom with 0.0 as the top y
        precharge_cell = cast(_ckt._CellInstance, insts["precharge[0]"]).cell
        precharge_bb = precharge_cell.layout.boundary
        assert precharge_bb is not None
        y_precharge = -precharge_bb.height
        for column in range(columns):
            inst_name = f"precharge[{column}]"
            layouter.place(insts[inst_name], x=column*precharge_bb.width, y=y_precharge)

        colmux_cell = cast(_ckt._CellInstance, insts["colmux[0]"]).cell
        colmux_bb = colmux_cell.layout.boundary
        assert colmux_bb is not None
        y_colmux = y_precharge - colmux_bb.height
        colmux_lays = tuple(
            layouter.place(insts[f"colmux[{bit}]"], x=bit*colmux_bb.width, y=y_colmux)
            for bit in range(self.bits)
        )

        senseamp_cell = fab.senseamp(colmux=self.colmux)
        senseamp_bb = senseamp_cell.layout.boundary
        assert senseamp_bb is not None
        y_senseamp = y_colmux - senseamp_bb.height
        senseamp_lays = tuple(
            layouter.place(
                insts[f"senseamp[{bit}]"], x=bit*senseamp_bb.width, y=y_colmux,
                rotation=_geo.Rotation.MX,
            )
            for bit in range(self.bits)
        )

        wdrive_cell = fab.writedriver(colmux=self.colmux, bits=self.driverbits)
        wdrive_bb = wdrive_cell.layout.boundary
        assert wdrive_bb is not None
        y_wdrive = y_senseamp - wdrive_bb.height
        wdrive_lays = tuple(
            layouter.place(insts[f"writedrive[{drive}]"], x=drive*wdrive_bb.width, y=y_wdrive)
            for drive in range(self.bits//self.driverbits)
        )

        clkwe_cell = fab.clockwe()
        clkwe_bb = clkwe_cell.layout.boundary
        assert clkwe_bb is not None
        # TODO: get stdcell height from the standard cell library
        stdcell_height = clkwe_bb.height
        y_clkwe = y_wdrive - clkwe_bb.height
        clkwe_lay = layouter.place(
            insts["clkwe"], x=0.0, y=y_wdrive, rotation=_geo.Rotation.MX,
        )

        cell_bottom = y_clkwe

        # vss/vdd
        vss_m3pinbb = layout.bounds(mask=metal3pin.mask, net=nets.vss, depth=2)
        layouter.add_wire(net=nets.vss, wire=metal3, pin=metal3pin, shape=vss_m3pinbb)
        vdd_m3pinbb = layout.bounds(mask=metal3pin.mask, net=nets.vdd, depth=2)
        layouter.add_wire(net=nets.vdd, wire=metal3, pin=metal3pin, shape=vdd_m3pinbb)

        vsssenseamp0_m1pinbb = senseamp_lays[0].bounds(
            mask=metal1pin.mask, net=nets.vss, depth=1,
        )

        _via1vss_lay = layouter.wire_layout(
            net=nets.vss, wire=via1, rows=2, columns=2,
            bottom_enclosure="tall", top_enclosure="tall",
        )
        _via2vss_lay = layouter.wire_layout(
            net=nets.vss, wire=via2, rows=2, columns=2,
            bottom_enclosure="tall", top_enclosure="tall",
        )
        _via2vss_m3bb = _via2vss_lay.bounds(mask=metal3.mask)
        _via1vdd_lay = layouter.wire_layout(
            net=nets.vdd, wire=via1, rows=2, columns=2,
            bottom_enclosure="tall", top_enclosure="tall",
        )
        _via2vdd_lay = layouter.wire_layout(
            net=nets.vdd, wire=via2, rows=2, columns=2,
            bottom_enclosure="tall", top_enclosure="tall",
        )
        _via2vdd_m3bb = _via2vdd_lay.bounds(mask=metal3.mask)

        x_vss = wdrive_bb.width
        x_vdd = 2*wdrive_bb.width

        y_vss = vsssenseamp0_m1pinbb.center.y
        layouter.place(_via1vss_lay, x=x_vss, y=y_vss)
        via2vss_lay = layouter.place(_via2vss_lay, x=x_vss, y=y_vss)
        via2vss_m2bb = via2vss_lay.bounds(mask=metal2.mask)
        via2vss_m3bb = via2vss_lay.bounds(mask=metal3.mask)
        shape = _geo.Rect.from_rect(rect=via2vss_m3bb, left=0.0, right=cell_width)
        layouter.add_wire(net=nets.vss, wire=metal3, pin=metal3pin, shape=shape)

        top = shape.bottom - metal3.min_space
        bottom = top - _via2vdd_m3bb.height
        shape = _geo.Rect(left=0.0, bottom=bottom, right=cell_width, top=top)
        layouter.add_wire(net=nets.vdd, wire=metal3, pin=metal3pin, shape=shape)
        y_topvdd = shape.center.y

        y_topvss = shape.bottom - metal3.min_space - _via2vss_m3bb.top
        via2vss_lay = layouter.place(_via2vss_lay, x=x_vss, y=y_topvss)
        via2vss_m2bb2 = via2vss_lay.bounds(mask=metal2.mask)
        shape = _geo.Rect.from_rect(rect=via2vss_m2bb, bottom=via2vss_m2bb2.bottom)
        layouter.add_wire(net=nets.vss, wire=metal2, shape=shape)

        for i in range(self.driverbits//2 + 1):
            y_vss = y_wdrive + 2*i*stdcell_height
            layouter.place(_via1vss_lay, x=x_vss, y=y_vss)
            via2vss_lay = layouter.place(_via2vss_lay, x=x_vss, y=y_vss)
            if i == 0:
                via2vss_m3bb = via2vss_lay.bounds(mask=metal3.mask)
                shape = _geo.Rect.from_rect(rect=via2vss_m3bb, top=y_topvss)
                layouter.add_wire(net=nets.vss, wire=metal3, shape=shape)

            y_vdd = y_senseamp - 2*i*stdcell_height
            layouter.place(_via1vdd_lay, x=x_vdd, y=y_vdd)
            layouter.place(_via2vdd_lay, x=x_vdd, y=y_vdd)

        vssclkwe_m1pinbb = clkwe_lay.bounds(mask=metal1pin.mask, net=nets.vss, depth=1)
        shape = _geo.Rect.from_rect(rect=vssclkwe_m1pinbb, right=cell_width)
        layouter.add_wire(net=nets.vss, wire=metal1, shape=shape)
        vddclkwe_m1pinbb = clkwe_lay.bounds(mask=metal1pin.mask, net=nets.vdd, depth=1)
        shape = _geo.Rect.from_rect(rect=vddclkwe_m1pinbb, right=cell_width)
        layouter.add_wire(net=nets.vdd, wire=metal1, shape=shape)

        y_vdd = vddclkwe_m1pinbb.center.y
        layouter.place(_via1vdd_lay, x=x_vdd, y=y_vdd)
        via2vdd_lay = layouter.place(_via2vdd_lay, x=x_vdd, y=y_vdd)
        via2vdd_m3bb = via2vdd_lay.bounds(mask=metal3.mask)
        shape = _geo.Rect.from_rect(rect=via2vdd_m3bb, top=y_topvdd)
        layouter.add_wire(net=nets.vdd, wire=metal3, shape=shape)

        # precharge_n
        pchgn_m3pinbb = layout.bounds(mask=metal3pin.mask, net=nets.precharge_n, depth=2)
        layouter.add_wire(
            net=nets.precharge_n, wire=metal3, pin=metal3pin, shape=pchgn_m3pinbb,
        )

        # col
        for col in range(self.colmux):
            net = nets[f"mux[{col}]"]
            col_m3pinbb = layout.bounds(mask=metal3pin.mask, net=net, depth=2)
            layouter.add_wire(net=net, wire=metal3, pin=metal3pin, shape=col_m3pinbb)

        # we
        net = nets.we
        m1pinbb = clkwe_lay.bounds(net=net, mask=metal1pin.mask, depth=1)

        _via1_lay = layouter.wire_layout(
            net=net, wire=via1, rows=2,
            bottom_enclosure="tall", top_enclosure="tall",
        )
        _via1_m1bb = _via1_lay.bounds(mask=metal1.mask)
        _via2_lay = layouter.wire_layout(
            net=net, wire=via2, rows=2,
            bottom_enclosure="tall", top_enclosure="tall",
        )

        x_via = m1pinbb.center.x
        y_via = m1pinbb.bottom - _via1_m1bb.bottom

        via1_lay = layouter.place(_via1_lay, x=x_via, y=y_via)
        via1weclkwe_m2bb = via1_lay.bounds(mask=metal2.mask)
        via2_lay = layouter.place(_via2_lay, x=x_via, y=y_via)
        via2weclkwe_m2bb = via2_lay.bounds(mask=metal2.mask)
        via2_m3bb = via2_lay.bounds(mask=metal3.mask)
        shape = _geo.Rect.from_rect(rect=via2_m3bb, bottom=cell_bottom)
        layouter.add_wire(net=net, wire=metal3, pin=metal3pin, shape=shape)

        # clk
        net = nets.clk
        m1pinbb = clkwe_lay.bounds(net=net, mask=metal1pin.mask, depth=1)

        _via1_lay = layouter.wire_layout(
            net=net, wire=via1, rows=2,
            bottom_enclosure="tall", top_enclosure="tall",
        )
        _via1_m2bb = _via1_lay.bounds(mask=metal2.mask)

        x_via = m1pinbb.center.x
        y_via = (
            max(via1weclkwe_m2bb.top, via2weclkwe_m2bb.top)
            + metal2.min_space - _via1_m2bb.bottom
        )
        via1_lay = layouter.place(_via1_lay, x=x_via, y=y_via)
        via1clk_m2bb = via1_lay.bounds(mask=metal2.mask)
        shape = _geo.Rect.from_rect(rect=via1clk_m2bb, left=0.0, right=cell_width)
        layouter.add_wire(net=net, wire=metal2, pin=metal2pin, shape=shape)

        # we_en
        net = nets.we_en
        m1pinbb = clkwe_lay.bounds(net=net, mask=metal1pin.mask, depth=1)

        _via1_lay = layouter.wire_layout(
            net=net, wire=via1, rows=2,
            bottom_enclosure="tall", top_enclosure="tall",
        )
        _via1_m2bb = _via1_lay.bounds(mask=metal2.mask)

        x_via = m1pinbb.center.x
        y_via = via1clk_m2bb.top + 2*metal2.min_space - _via1_m2bb.bottom
        via1_lay = layouter.place(_via1_lay, x=x_via, y=y_via)
        via1ween_m2bb = via1_lay.bounds(mask=metal2.mask)
        shape = _geo.Rect.from_rect(rect=via1ween_m2bb, left=0.0, right=cell_width)
        layouter.add_wire(net=net, wire=metal2, pin=metal2pin, shape=shape)

        # we_n
        net = nets.we_n

        m2pinbb0 = wdrive_lays[0].bounds(mask=metal2pin.mask, net=net, depth=1)
        m2pinbbm1 = wdrive_lays[-1].bounds(mask=metal2pin.mask, net=net, depth=1)
        shape = _geo.Rect.from_rect(rect=m2pinbb0, right=m2pinbbm1.right)
        layouter.add_wire(net=net, wire=metal2, shape=shape)

        m1pinbb = clkwe_lay.bounds(mask=metal1pin.mask, net=net, depth=1)
        _via1_lay = layouter.wire_layout(
            net=net, wire=via1, rows=2, bottom_enclosure="tall", top_enclosure="tall",
        )
        _via1_m1bb = _via1_lay.bounds(mask=metal1.mask)
        _via2_lay = layouter.wire_layout(
            net=net, wire=via2, rows=2, bottom_enclosure="tall", top_enclosure="tall",
        )
        x_via = m1pinbb.center.x
        y_via = m1pinbb.top - _via1_m1bb.top
        via1_lay = layouter.place(_via1_lay, x=x_via, y=y_via)
        via1_m2bb = via1_lay.bounds(mask=metal2.mask)
        via2_lay = layouter.place(_via2_lay, x=x_via, y=y_via)
        via2_m2bb = via2_lay.bounds(mask=metal2.mask)
        via2_m3bb1 = via2_lay.bounds(mask=metal3.mask)
        y_via = m2pinbb0.center.y
        via2_lay = layouter.place(_via2_lay, x=x_via, y=y_via)
        via2_m3bb2 = via2_lay.bounds(mask=metal3.mask)

        shape = _geo.Rect.from_rect(rect=via2_m3bb1, top=via2_m3bb2.top)
        layouter.add_wire(net=net, wire=metal3, shape=shape)

        # intclk
        net = nets.intclk

        m2pinbb = clkwe_lay.bounds(mask=metal2pin.mask, net=net, depth=1)
        w = m2pinbb.height

        top = min(via1_m2bb.bottom, via2_m2bb.bottom) - metal2.min_space
        y_intclk = top - 0.5*w

        shape = _geo.Rect(
            left=m2pinbb.left,
            bottom=m2pinbb.center.y,
            right=m2pinbb.left + w,
            top=y_intclk,
        )
        hor_left = shape.left
        hor_right = shape.right
        layouter.add_wire(net=net, wire=metal2, shape=shape)

        for wdrive_lay in wdrive_lays:
            m2pinbb = wdrive_lay.bounds(mask=metal2pin.mask, net=net, depth=1)
            hor_left = min(hor_left, m2pinbb.left)
            hor_right = max(hor_right, m2pinbb.right)
            shape = _geo.Rect.from_rect(rect=m2pinbb, bottom=y_intclk)
            layouter.add_wire(net=net, wire=metal2, shape=shape)

        shape = _geo.Rect(
            left=hor_left, bottom=(y_intclk - 0.5*w),
            right=hor_right, top=(y_intclk + 0.5*w)
        )
        layouter.add_wire(net=net, wire=metal2, shape=shape)

        # q
        for bit, senseamp_lay in enumerate(senseamp_lays):
            net = nets[f"q[{bit}]"]
            m1pinbb = senseamp_lay.bounds(mask=metal1pin.mask, net=net, depth=1)

            _via1_lay = layouter.wire_layout(
                net=net, wire=via1, rows=2,
                bottom_enclosure="tall", top_enclosure="tall",
            )
            _via1_m1bb = _via1_lay.bounds(mask=metal1.mask)
            _via2_lay = layouter.wire_layout(
                net=net, wire=via2, rows=2,
                bottom_enclosure="tall", top_enclosure="tall",
            )

            x_via = m1pinbb.center.x
            y_via = m1pinbb.bottom - _via1_m1bb.bottom

            layouter.place(_via1_lay, x=x_via, y=y_via)
            via2_lay = layouter.place(_via2_lay, x=x_via, y=y_via)
            via2_m3bb = via2_lay.bounds(mask=metal3.mask)
            shape = _geo.Rect.from_rect(rect=via2_m3bb, bottom=cell_bottom)
            layouter.add_wire(net=net, wire=metal3, pin=metal3pin, shape=shape)

        # d
        for drive, wdrive_lay in enumerate(wdrive_lays):
            for drivebit in range(self.driverbits):
                bit = drive*self.driverbits + drivebit
                net = nets[f"d[{bit}]"]
                m1pinbb = wdrive_lay.bounds(mask=metal1pin.mask, net=net, depth=1)

                _via1_lay = layouter.wire_layout(
                    net=net, wire=via1, rows=2,
                    bottom_enclosure="tall", top_enclosure="tall",
                )
                _via1_m1bb = _via1_lay.bounds(mask=metal1.mask)
                _via2_lay = layouter.wire_layout(
                    net=net, wire=via2, rows=2,
                    bottom_enclosure="tall", top_enclosure="tall",
                )

                x_via1 = m1pinbb.center.x
                x_via2 = x_via1 + drivebit*m3pitch
                y_via = m1pinbb.bottom - _via1_m1bb.bottom

                via1_lay = layouter.place(_via1_lay, x=x_via1, y=y_via)
                via2_lay = layouter.place(_via2_lay, x=x_via2, y=y_via)

                if drivebit > 0:
                    via1_m2bb = via1_lay.bounds(mask=metal2.mask)
                    via2_m2bb = via2_lay.bounds(mask=metal2.mask)
                    shape = _geo.Rect.from_rect(rect=via1_m2bb, right=via2_m2bb.right)
                    layouter.add_wire(net=net, wire=metal2, shape=shape)
                via2_m3bb = via2_lay.bounds(mask=metal3.mask)
                shape = _geo.Rect.from_rect(rect=via2_m3bb, bottom=cell_bottom)
                layouter.add_wire(net=net, wire=metal3, pin=metal3pin, shape=shape)

        # boundary
        self.set_boundary(
            bb=_geo.Rect(left=0.0, bottom=cell_bottom, right=cell_width, top=0.0),
        )


class _Column(_FactoryCell[_factory_type_], Generic[_factory_type_]):
    ctrl_signals: SigSpec # Non vector signal, metal3 left to right
    row_signals: SigSpec # Vector signals of size rows
    col_signals: SigSpec # Vector signals of size colmux
    bit_signals: SigSpec # Vector signals of size bits
    we_signals: SigSpec # Non vector signal, vector in ColumnBlock

    def __init__(self, *,
        rows: int, bits: int, colmux: int, fab: _factory_type_, name: str,
    ):
        super().__init__(fab=fab, name=name)

        self.rows = rows
        self.bits = bits
        self.colmux = colmux


class _ColumnBlock(_FactoryCell["_SRAMFactory"]):
    signals: SigSpec

    def __init__(self, *,
        rows: int, bits: int, colmux: int, webits: int,
        fab: "_SRAMFactory", name: str,
    ):
        if (bits%webits) != 0:
            raise ValueError(f"bits {bits} is not a multiple of webits {webits}")
        super().__init__(fab=fab, name=name)

        self.rows = rows
        self.bits = bits
        self.colmux = colmux
        self.webits = webits

        self._colbits = colbits = self.bits//self.webits
        self._column_cell = column_cell = fab.column(
            rows=self.rows, bits=colbits, colmux=self.colmux,
        )

        ctrl_signals: SigSpec = column_cell.ctrl_signals
        self._ctrl_signals = ctrl_signals
        row_signals: SigSpec = tuple(
            (f"{sig}[{row}]", pin)
            for (sig, pin), row in product(column_cell.row_signals, range(self.rows))
        )
        self._row_signals = row_signals
        col_signals: SigSpec = tuple(
            (f"{sig}[{col}]", pin)
            for (sig, pin), col in product(column_cell.col_signals, range(self.colmux))
        )
        self._col_signals = col_signals
        bit_signals: SigSpec = tuple(
            (f"{sig}[{bit}]", pin)
            for (sig, pin), bit in product(column_cell.bit_signals, range(self.bits))
        )
        we_signals: SigSpec = tuple(
            (f"{sig}[{we}]", pin)
            for (sig, pin), we in product(column_cell.we_signals, range(self.webits))
        )
        self.signals = (
            *ctrl_signals, *row_signals, *col_signals, *bit_signals, *we_signals
        )

    def _create_circuit(self) -> None:
        fab = self.fab

        ckt = self.new_circuit()

        colbits = self._colbits
        column_cell = self._column_cell
        columns = tuple(
            ckt.instantiate(column_cell, name=f"column[{webit}]")
            for webit in range(self.webits)
        )

        assert all(tuple(
            hasattr(column_cell, attr)
            for attr in (
                "ctrl_signals", "row_signals", "col_signals", "bit_signals", "we_signals",
            )
        )), "Missing attribute for _Column object"

        for net_name, _ in (
            *self._ctrl_signals, *self._row_signals, *self._col_signals,
        ):
            ckt.new_net(name=net_name, external=True, childports=(
                column.ports[net_name] for column in columns
            ))

        for webit, column in enumerate(columns):
            for (sig, _) in column_cell.we_signals:
                ckt.new_net(
                    name=f"{sig}[{webit}]", external=True, childports=column.ports[sig],
                )

            for colbit in range(colbits):
                bit = webit*colbits + colbit
                for (sig, _) in column_cell.bit_signals:
                    ckt.new_net(
                        name=f"{sig}[{bit}]", external=True,
                        childports=column.ports[f"{sig}[{colbit}]"],
                    )

    def _create_layout(self) -> None:
        fab = self.fab
        cache = fab._cache

        nets = self.circuit.nets
        insts = self.circuit.instances

        metal1 = cache.metal(1)
        metal1pin = cache.metalpin(1)
        metal2 = cache.metal(2)
        metal2pin = cache.metalpin(2)
        metal3 = cache.metal(3)
        metal3pin = cache.metalpin(3)

        metal_lookup = {metal1pin: metal1, metal2pin: metal2, metal3pin: metal3}

        layouter = self.new_circuitlayouter()
        layout = layouter.layout

        x_column = 0.0
        columns_lays = []
        cell_height: Optional[float] = None
        for webit in range(self.webits):
            column_lay = layouter.place(insts[f"column[{webit}]"], x=x_column, y=0.0)
            column_bb = column_lay.boundary
            assert column_bb is not None
            cell_height = column_bb.top
            x_column = column_bb.right

            columns_lays.append(column_lay)
        cell_width = x_column
        assert cell_height is not None

        for net_name, pin in self.signals:
            net = nets[net_name]
            for ms in layout.filter_polygons(net=net, mask=pin.mask, depth=1):
                layouter.add_wire(
                    net=net, wire=metal_lookup[pin], pin=pin, shape=ms.shape)

        # boundary
        self.set_size(width=cell_width, height=cell_height)


class _SRAMFactory(abc.ABC):
    def __init__(self, *, lib: _lbry.Library, spec: _SRAMSpecification):
        self._lib = lib
        self._spec = spec
        self._cache = _TechCache(fab=self, spec=spec)

    @property
    def lib(self) -> _lbry.Library:
        return self._lib
    @property
    def tech(self) -> _tch.Technology:
        return self.lib.tech
    @property
    def spec(self) -> _SRAMSpecification:
        return self._spec

    def _get_cell(self, *,
        cell_name: str, cls: Type[_cell_type_], cls_args: Dict[str, Any],
    ) -> _cell_type_:
        prefix = self.spec.name_prefix
        full_name = f"{prefix}{cell_name}"
        try:
            cell = cast(cls, self.lib.cells[full_name])
        except KeyError:
            cell = cls(fab=self, name=full_name, **cls_args)
            self.lib.cells += cell

        return cell

    @abc.abstractmethod
    def bitcell(self) -> _BitCell:
        ...

    def bitarray(self, *, rows: int, columns: int) -> _CellArray:
        return self._get_cell(
            cell_name=f"Array_{rows}X{columns}",
            cls=_CellArray, cls_args={"rows": rows, "columns": columns},
        )

    def wordlinedriver(self, *,
        wl_bottom: float, wl_top: float, name_suffix: str,
    ) -> _WordlineDriver:
        spec = self.spec
        tech = self.tech
        nln = round(spec.wldrive_nmos_l/tech.grid)
        nwn = round(spec.wldrive_nmos_w/tech.grid)
        nlp = round(spec.wldrive_pmos_l/tech.grid)
        nwp = round(spec.wldrive_pmos_w/tech.grid)

        return self._get_cell(
            cell_name=f"WLDrive_{nln}LN{nwn}WN{nlp}LP{nwp}WP{name_suffix}",
            cls=_WordlineDriver, cls_args={
                "nmos_l": spec.wldrive_nmos_l, "nmos_w": spec.wldrive_nmos_w,
                "pmos_l": spec.wldrive_pmos_l, "pmos_w": spec.wldrive_pmos_w,
                "wl_bottom": wl_bottom, "wl_top": wl_top,
            }
        )

    def rowdecodernand3(self) -> _RowDecoderNand3:
        return self._get_cell(
            cell_name="RowDecoderNand3",
            cls=_RowDecoderNand3, cls_args={},
        )

    def rowdecoderdrivepage(
        self, *, pds: int, rows: int,
        wldriver_kwargs: Dict[str, Any], name_suffix: str,
    ) -> _RowDecoderDrivePage:
        return self._get_cell(
            cell_name=f"RowDecoderDriverPage_{pds}PD{rows}R{name_suffix}",
            cls=_RowDecoderDrivePage, cls_args={
                "pds": pds, "rows": rows, "wldriver_kwargs": wldriver_kwargs},
        )

    def rowpredecoders(self, *, address_groups: Iterable[int]) -> _RowPreDecoders:
        address_groups = tuple(address_groups)
        bitstr = "_".join(str(bit) for bit in address_groups) + "B"
        return self._get_cell(
            cell_name=f"RowPredecoders_{bitstr}",
            cls=_RowPreDecoders, cls_args={"address_groups": address_groups},
        )

    def rowdecoder(self, *,
        address_groups: Iterable[int], reverse: bool,
        page_kwargs: Dict[str, Any], name_suffix: str,
    ) -> _RowDecoder:
        address_groups = tuple(address_groups)
        bitstr = "_".join(str(bit) for bit in address_groups) + "B"
        return self._get_cell(
            cell_name=f"RowDecoder_{bitstr}{name_suffix}",
            cls=_RowDecoder, cls_args={
                "address_groups": address_groups, "reverse": reverse, "page_kwargs": page_kwargs,
            },
        )

    def nonoverlapclock(self, *, stages: int) -> _NonOverlapClock:
        return self._get_cell(
            cell_name=f"NonOverlapClock_{stages}S",
            cls=_NonOverlapClock, cls_args={"stages": stages},
        )

    def clockgenerator(self) -> _ClockGenerator:
        return self._get_cell(
            cell_name=f"ClockGenerator",
            cls=_ClockGenerator, cls_args={},
        )

    def latcheddecoder2row(self, *, addressbits: int) -> _LatchedDecoder2Row:
        return self._get_cell(
            cell_name=f"LatchedDecoder_{addressbits}A2R",
            cls=_LatchedDecoder2Row, cls_args={"addressbits": addressbits},
        )

    def rowperiphery(self, *,
        address_groups: Iterable[int],
        rowdec_kwargs: Dict[str, Any], colperiph_kwargs: Dict[str, Any],
        name_suffix: str,
    ) -> _RowPeriphery:
        address_groups = tuple(address_groups)
        address_str = "_".join(str(bits) for bits in address_groups)
        return self._get_cell(
            cell_name=f"RowPeriphery_{address_str}{name_suffix}",
            cls=_RowPeriphery, cls_args={
                "address_groups": address_groups,
                "rowdec_kwargs": rowdec_kwargs,
                "colperiph_kwargs": colperiph_kwargs,
            }
        )

    def precharge(self, *,
        bl_left: float, bl_right:float, bln_left: float, bln_right: float,
        name_suffix: str,
    ) -> _Precharge:
        return self._get_cell(
            cell_name=f"Precharge{name_suffix}",
            cls=_Precharge, cls_args={
                "bl_left": bl_left, "bl_right": bl_right,
                "bln_left": bln_left, "bln_right": bln_right,
            },
        )

    def colmux(self, *,
        columns: int,
        bl_left: float, bl_right: float, bln_left: float, bln_right: float,
        name_suffix: str,
    ) -> _ColMux:
        assert columns == 4, "Unsupported config"
        return self._get_cell(
            cell_name=f"ColMux_{columns}C{name_suffix}",
            cls=_ColMux, cls_args={
                "columns": columns,
                "bl_left": bl_left, "bl_right": bl_right,
                "bln_left": bln_left, "bln_right": bln_right,
            },
        )

    def senseamp(self, *, colmux: int) -> _SenseAmp:
        return self._get_cell(
            cell_name=f"SenseAmp_{colmux}M",
            cls=_SenseAmp, cls_args={"colmux": colmux},
        )

    def writedriver(self, *, colmux: int, bits: int) -> _WriteDriver:
        return self._get_cell(
            cell_name=f"WriteDriver_{colmux}M{bits}B",
            cls=_WriteDriver, cls_args={"colmux": colmux, "bits": bits},
        )

    def clockwe(self) -> _ClockBufWordEnable:
        return self._get_cell(
            cell_name="ClockWE",
            cls=_ClockBufWordEnable, cls_args={},
        )

    def columnperiphery(self, *,
        bits: int, colmux: int,
        precharge_kwargs: Dict[str, Any], colmux_kwargs: Dict[str, Any],
        name_suffix: str,
    ) -> _ColumnPeriphery:
        return self._get_cell(
            cell_name=f"ColumnPeriphery_{bits}B{colmux}M{name_suffix}",
            cls=_ColumnPeriphery, cls_args={
                "bits": bits, "colmux": colmux,
                "precharge_kwargs": precharge_kwargs, "colmux_kwargs": colmux_kwargs,
            },
        )

    @abc.abstractclassmethod
    def column(self, *,
        rows: int, bits: int, colmux: int, **kawrgs,
    ) -> _Column:
        ...

    def columnblock(self, *,
        rows: int, bits: int, colmux: int, webits: int,
    ) -> _ColumnBlock:
        return self._get_cell(
            cell_name=f"ColumnBlock_{rows}R{bits}B{colmux}M{webits}W",
            cls=_ColumnBlock, cls_args={
                "rows": rows, "bits": bits, "colmux": colmux, "webits": webits,
            },
        )
