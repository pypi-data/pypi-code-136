# SPDX-License-Identifier: GPL-2.0-or-later OR AGPL-3.0-or-later OR CERN-OHL-S-2.0+
from math import floor, ceil
import abc
from typing import Optional, Union, Iterable, cast, overload

from .. import _util
from ..typing import IntFloat
from . import (
    property_ as prp, rule as rle, mask as msk, wafer_ as wfr, geometry as geo,
    primitive as prm,
)


__all__ = ["Technology"]


class Technology(abc.ABC):
    """A `Technology` object is the representation of a semiconductor process.
    It's mainly a list of `_Primitive` objects with these primitives describing
    the capabilities of the technolgy.

    the `Technology` class is an abstract base class so subclasses need to
    implement some of the abstract methods defined in this base class.

    The setup of the primitives for a technology is done in the `_init()` method.
    Typically subclasses should not overload the `__init__()` method.

    Next to the `_init()` abstract method subclasses also need to define some
    abstract properties to define some properties of the technology. These are
    `name()`, `grid()` and `substrate_type()`.
    """
    class ConnectionError(Exception):
        pass

    class _ComputedSpecs:
        """`Technology._ComputedSpecs` is a helper class that allow to compute
        some properties on a technology. This class should not be instantiated
        by user code by is access through the `computed` attribute of a `Technology`
        object.
        """
        def __init__(self, tech: "Technology"):
            self.tech = tech

        @overload
        def min_space(self,
            primitive1: "prm._MaskPrimitive", primitive2: None=None,
        ) -> float:
            ... # pragma: no cover
        @overload
        def min_space(self,
            primitive1: "prm._Primitive", primitive2: "prm._Primitive",
        ) -> float:
            ... # pragma: no cover
        def min_space(self,
            primitive1: "prm._Primitive", primitive2: Optional["prm._Primitive"]=None,
        ) -> float:
            """Compute the minimum space between one or two primitives. It will go
            over all the rules to determine the minimum space for the provided
            primitive.
            This function allows to compute the min_space on primitives that are
            derived from other primitives.

            Arguments:
                primitive1: the first primitive
                    if primitive2 is not given, the minimum space between shapes
                    on the primitive1 layer is returned.
                primitive2: the optional second primitive.
                    if specified the minimum space between shape on layer primitive1
                    and shapes on layer primitive2 is returned.
            """
            def check_prim(prim: prm.Spacing) -> bool:
                if primitive2 is None:
                    return (
                        (primitive1 in prim.primitives1)
                        and (prim.primitives2 is None)
                    )
                elif prim.primitives2 is not None:
                    return (
                        (
                            (primitive1 in prim.primitives1)
                            and (primitive2 in prim.primitives2)
                        )
                        or (
                            (primitive1 in prim.primitives2)
                            and (primitive2 in prim.primitives1)
                        )
                    )
                else:
                    return False

            spaces = list(
                p.min_space for p in filter(
                    check_prim, self.tech.primitives.__iter_type__(prm.Spacing),
                )
            )
            if (primitive2 is None) or (primitive1 == primitive2):
                try:
                    space = cast(prm._WidthSpacePrimitive, primitive1).min_space
                except AttributeError: # pragma: no cover
                    pass
                else:
                    spaces.append(space)

            try:
                return max(spaces)
            except ValueError:
                raise AttributeError(
                    f"min_space between {primitive1} and {primitive2} not found",
                )

        def min_width(self, primitive: "prm._WidthSpacePrimitive", *,
            up: bool=False, down: bool=False, min_enclosure: bool=False,
        ):
            """Compute the minimum width of a primitive.
            This method allows to take into account via enclosure rules to compute
            minimum width but still be contacted through a via.

            Arguments:
                primitive: the primitive
                up: wether it needs to take a connection from the top with a Via
                    into account.
                down: wether it needs to take a connection from the bottom with a Via
                    into account.
                min_enclosure: if True it will take the minimum value minimum value
                    of the relevant via enclosure rule; otherwise the maximum value.
            """
            assert primitive.min_width is not None, (
                "primitive has to have the min_with attribute"
            )

            def wupdown(via):
                if up and (primitive in via.bottom):
                    idx = via.bottom.index(primitive)
                    enc = via.min_bottom_enclosure[idx]
                    w = via.width
                elif down and (primitive in via.top):
                    idx = via.top.index(primitive)
                    enc = via.min_top_enclosure[idx]
                    w = via.width
                else:
                    enc = prp.Enclosure(0.0)
                    w = 0.0

                enc = enc.min() if min_enclosure else enc.max()
                return w + 2*enc

            return max((
                primitive.min_width,
                *(wupdown(via) for via in self.tech.primitives.__iter_type__(prm.Via)),
            ))

        def min_pitch(self, primitive: "prm._WidthSpacePrimitive", *,
            up: bool=False, down: bool=False, min_enclosure: bool=False,
        ):
            """Compute the minimum pitch of a primitive.
            It's the minimum width plus the minimum space.

            Arguments:
                primitive: the primitive
                up: wether it needs to take a connection from the top with a Via
                    into account.
                down: wether it needs to take a connection from the bottom with a Via
                    into account.
                min_enclosure: if True it will take the minimum value minimum value
                    of the relevant via enclosure rule; otherwise the maximum value.
            """
            w = self.min_width(primitive, up=up, down=down, min_enclosure=min_enclosure)
            return w + primitive.min_space

    @property
    @abc.abstractmethod
    def name(self) -> str:
        """property with the name of the technology"""
        ... # pragma: no cover
    @property
    @abc.abstractmethod
    def grid(self) -> float:
        """property with the minimum grid of the technology

        Optionally primitives may define a bigger grid for their shapes.
        """
        ... # pragma: no cover
    @property
    @abc.abstractmethod
    def substrate_type(self) -> str:
        """property with the substrate type of the technology

        It has to be "n", "p" or "undoped".
        """
        ... # pragma: no cover

    def __init__(self):
        self._init_done = False

        if not self.substrate_type in ("n", "p", "undoped"):
            raise ValueError(
                "substrate_type Technology class attribute has to be 'n', 'p' or 'undoped'",
            )

        self._primitives = prims = prm.Primitives()

        self._init()

        self._init_done = True
        self._substrate = None

        self._build_interconnect()
        self._build_rules()

        prims._freeze_()

        self.computed = self._ComputedSpecs(self)

    def is_ongrid(self, v: float, mult: int=1) -> float:
        """Returns wether a value is on grid or not.

        Arguments:
            w: value to check
            mult: value has to be on `mult*grid`
        """
        g = mult*self.grid
        ng = round(v/g)
        return abs(v - ng*g) < geo.epsilon

    @overload
    def on_grid(self,
        dim: IntFloat, *, mult: int=1, rounding: str="nearest",
    ) -> float:
        ... # pragma: no cover
    @overload
    def on_grid(self,
        dim: geo.Point, *, mult: int=1, rounding: str="nearest",
    ) -> geo.Point:
        ... # pragma: no cover
    def on_grid(self,
        dim: Union[IntFloat, geo.Point], *, mult: int=1, rounding: str="nearest",
    ) -> Union[float, geo.Point]:
        """Compute a value on grid from a given value.

        Arguments:
            dim: value to put on grid
            mult: value will be put on `mult*grid`
            rounding: how to round the value
                Has to be one of "floor", "nearest", "ceiling"; "nearest" is the
                default.
        """
        if isinstance(dim, geo.Point):
            return geo.Point(
                x=self.on_grid(dim.x, mult=mult, rounding=rounding),
                y=self.on_grid(dim.y, mult=mult, rounding=rounding),
            )
        dim = _util.i2f(dim)
        if rounding == "floor":
            dim += geo.epsilon
        elif rounding == "ceiling":
            dim -= geo.epsilon
        else:
            if rounding != "nearest":
                raise ValueError(
                    "rounding has to be one of ('floor', 'nearest', 'ceiling') "
                    f"not '{rounding}'"
                )
        flookup = {"nearest": round, "floor": floor, "ceiling": ceil}
        try:
            f = flookup[rounding]
        except KeyError: # pragma: no cover
            raise RuntimeError(f"Not implemeted: rounding '{rounding}'")

        return f(dim/(mult*self.grid))*mult*self.grid

    @property
    def dbu(self) -> float:
        """Returns database unit compatible with technology grid. An exception is
        raised if the technology grid is not a multuple of 10pm.

        This method is specifically for use to export to format that use the dbu.
        """
        igrid = int(round(1e6*self.grid))
        assert (igrid%10) == 0
        if (igrid%100) != 0:
            return 1e-5
        elif (igrid%1000) != 0:
            return 1e-4
        else:
            return 1e-3

    @abc.abstractmethod
    def _init(self):
        """Abstract method that needs to setup the primitives.

        When entering this function the object's `_primitives` attribute will be empty
        and upon return from this method this attribute will have to be filled with
        all the primitives of the given technology.

        After the initialization has called this function it will perform connectivity
        and other consistency checks on the provided list of primitives.
        """
        ... # pragma: no cover

    def _build_interconnect(self):
        prims = self._primitives

        neworder = []
        def add_prims(prims2):
            for prim in prims2:
                if prim is None:
                    continue
                idx = prims.index(prim)
                if idx not in neworder:
                    neworder.append(idx)

        def get_name(prim):
            return prim.name

        # set that are build up when going over the primitives
        # bottomwires: primitives that still need to be bottomconnected by a via
        bottomwires = set()
        # implants: used implant not added yet
        implants = set() # Implants to add
        markers = set() # Markers to add
        # the wells, fixed
        deepwells = set(prims.__iter_type__(prm.DeepWell))
        wells = set(prims.__iter_type__(prm.Well))

        # Wells are the first primitives in line
        add_prims(sorted(deepwells, key=get_name))
        add_prims(sorted(wells, key=get_name))

        # process waferwires
        waferwires = set(prims.__iter_type__(prm.WaferWire))
        bottomwires.update(waferwires) # They also need to be connected
        conn_wells = set()
        for wire in waferwires:
            implants.update((*wire.implant, *wire.well))
            conn_wells.update(wire.well)
        if conn_wells != wells:
            raise prm.UnconnectedPrimitiveError((wells - conn_wells).pop())

        # process gatewires
        bottomwires.update(prims.__iter_type__(prm.GateWire))

        # Already add implants that are used in the waferwires
        add_prims(sorted(implants, key=get_name))
        implants = set()

        # Add the oxides
        for ww in waferwires:
            if ww.oxide is not None:
                add_prims(sorted(ww.oxide, key=get_name))

        # process vias
        vias = set(prims.__iter_type__(prm.Via))

        def allwires(wire):
            if isinstance(wire, prm.Resistor):
                yield from allwires(wire.wire)
                yield from wire.indicator
            if isinstance(wire, prm._PinAttribute) and wire.pin is not None:
                yield from wire.pin
            if isinstance(wire, prm._BlockageAttribute) and wire.blockage is not None:
                yield wire.blockage
            yield wire

        connvias = set(filter(lambda via: any(w in via.bottom for w in bottomwires), vias))
        if connvias:
            viatops = set()
            while connvias:
                viabottoms = set()
                viatops = set()
                for via in connvias:
                    viabottoms.update(via.bottom)
                    viatops.update(via.top)

                noconn = tuple(filter(
                    # MIMTop does not need to be connected from bottom
                    lambda l: not isinstance(l, prm.MIMTop),
                    bottomwires - viabottoms,
                ))
                if noconn:
                    raise Technology.ConnectionError(
                        f"wires ({', '.join(wire.name for wire in noconn)})"
                        " not in bottom list of any via"
                    )

                for bottom in viabottoms:
                    add_prims(allwires(bottom))

                bottomwires -= viabottoms
                bottomwires.update(viatops)

                vias -= connvias
                connvias = set(filter(lambda via: any(w in via.bottom for w in bottomwires), vias))
            # Add the top layers of last via to the prims
            for top in viatops:
                add_prims(allwires(top))

        if vias:
            raise Technology.ConnectionError(
                f"vias ({', '.join(via.name for via in vias)}) have no connection to"
                " a technology bottom wire"
            )

        # Add via and it's blockage layers
        vias = tuple(prims.__iter_type__(prm.Via))
        add_prims(prim.blockage for prim in vias)
        # Now add all vias
        add_prims(vias)

        # process mosfets
        mosfets = set(prims.__iter_type__(prm.MOSFET))
        gates = {mosfet.gate for mosfet in mosfets}
        allgates = set(prims.__iter_type__(prm.MOSFETGate))
        if gates != allgates:
            diff = allgates - gates
            if diff:
                raise prm.UnusedPrimitiveError(diff.pop())
            raise RuntimeError("Unhandled error condition") # pragma: no cover
        actives = {gate.active for gate in gates}
        polys = {gate.poly for gate in gates}
        for mosfet in mosfets:
            implants.update(mosfet.implant)
            if mosfet.well is not None:
                implants.add(mosfet.well)
            if mosfet.gate.inside is not None:
                markers.update(mosfet.gate.inside)

        add_prims((
            *sorted(implants, key=get_name),
            *sorted(actives, key=get_name), *sorted(polys, key=get_name),
            *sorted(markers, key=get_name), *sorted(gates, key=get_name),
            *sorted(mosfets, key=get_name),
        ))
        implants = set()
        markers = set()

        # proces pad openings
        padopenings = set(prims.__iter_type__(prm.PadOpening))
        viabottoms = set()
        for padopening in padopenings:
            add_prims(allwires(padopening.bottom))
        add_prims(padopenings)

        # process top metal wires
        add_prims(prims.__iter_type__(prm.TopMetalWire))

        # process resistors
        resistors = set(prims.__iter_type__(prm.Resistor))
        for resistor in resistors:
            markers.update(resistor.indicator)

        # process capacitors
        mimtops = set(prims.__iter_type__(prm.MIMTop))
        mimcaps = tuple(prims.__iter_type__(prm.MIMCapacitor))
        usedtops = set(c.top for c in mimcaps)
        unusedtops = mimtops - usedtops
        if unusedtops:
            raise prm.UnusedMIMTop(unusedtops.pop())

        # process diodes
        diodes = set(prims.__iter_type__(prm.Diode))
        for diode in diodes:
            markers.update(diode.indicator)

        # process bipolars
        bipolars = set(prims.__iter_type__(prm.Bipolar))
        for bipolar in bipolars:
            markers.update(bipolar.indicator)

        # extra rules
        rules = set(prims.__iter_type__(prm._RulePrimitive))

        add_prims((*markers, *resistors, *mimcaps, *diodes, *bipolars, *rules))

        # process auxiliary
        def aux_key(aux: prm.Auxiliary) -> str:
            return aux.name
        add_prims(sorted(prims.__iter_type__(prm.Auxiliary), key=aux_key))

        # reorder primitives
        unused = set(range(len(prims))) - set(neworder)
        if unused:
            raise prm.UnusedPrimitiveError(prims[unused.pop()])
        prims._reorder_(neworder)

    def _build_rules(self):
        prims = self._primitives
        self._rules = rules = rle.Rules()

        # grid
        rules += wfr.wafer.grid == self.grid

        # Generate the rule but don't add them yet.
        for prim in prims:
            prim._derive_rules(self)

        # First add substrate alias if needed. This will only be clear
        # after the rules have been generated.
        sub = self.substrate
        if isinstance(sub, msk._MaskAlias):
            self._rules += sub
        if sub != wfr.wafer:
            self._rules += msk.Connect(sub, wfr.wafer)

        # Now we can add the rules
        for prim in prims:
            self._rules += prim.rules

        rules._freeze_()

    @property
    def substrate(self) -> msk._Mask:
        """Property representing the substrate of the technology; it's defined as the area
        that is outside any of the wells of the technology.

        As this value needs access to the list of wells it's only available afcer the
        technology has been initialized and is not available during run of the `_init()`
        method.
        """
        if not self._init_done:
            raise AttributeError("substrate may not be accessed during object initialization")
        if self._substrate is None:
            well_masks = tuple(
                prim.mask for prim in self._primitives.__iter_type__(prm.Well)
            )
            if not well_masks:
                self._substrate = wfr.wafer
            else:
                self._substrate = wfr.outside(well_masks, alias=f"substrate:{self.name}")
        return self._substrate

    @property
    def rules(self) -> Iterable[rle._Rule]:
        """Return all the rules that are derived from the primitives of the technology."""
        return self._rules

    @property
    def primitives(self) -> "prm.Primitives":
        """Return the primitives of the technology."""
        return self._primitives

    @property
    def designmasks(self) -> Iterable[msk.DesignMask]:
        """Return all the `DesignMask`s defined by the primitives of the technology

        The property makes sure there are no duplicates in the returned iterable.
        """
        masks = set()
        for prim in self._primitives:
            for mask in prim.designmasks:
                if mask not in masks:
                    yield mask
                    masks.add(mask)

