# SPDX-License-Identifier: GPL-2.0-or-later OR AGPL-3.0-or-later OR CERN-OHL-S-2.0+
import abc
from typing import Iterable, Tuple, Dict, Generic, Optional, TypeVar, cast

from ..typing import IntFloat, SingleOrMulti, OptSingleOrMulti
from .. import _util
from ..technology import geometry as geo, primitive as prm, technology_ as tch
from . import layout as lay, circuit as ckt


__all__ = ["RoutingGauge", "Library", "StdCellLibrary"]


LibraryType = TypeVar("LibraryType", bound="Library")


class _Cell(Generic[LibraryType]):
    """A cell is an element from a `Library` and represents the building blocks
    of a circuit. A cell may contain one or more circuits and one or more layouts.

    API Notes:
        User supported ways for creating cells is not fixed. Backwards incompatible
        changes are still expected.
    """
    def __init__(self, *, lib: LibraryType, name: str):
        self.lib = lib
        self.name = name

        self.circuits = ckt._Circuits()
        self.layouts = _CellLayouts()

    @property
    def tech(self):
        return self.lib.tech
    @property
    def cktfab(self):
        return self.lib.cktfab
    @property
    def layoutfab(self):
        return self.lib.layoutfab

    @property
    def circuit(self):
        """The default circuit of the cell;' it's the one with the same name as
        the cell"""
        try:
            return self.circuits[self.name]
        except KeyError:
            raise ValueError(f"Cell '{self.name}' has no default circuit")

    @property
    def layout(self):
        """The default layout of the cell;' it's the one with the same name as
        the cell"""
        try:
            return self.layouts[self.name]
        except KeyError:
            raise ValueError(f"Cell '{self.name}' has no default layout")

    def new_circuit(self, *, name: Optional[str]=None):
        """Create a new empty circuit for the cell.

        Arguments:
            name: the name of the circuit. If not specified the same name as the
                cell will be used.
        """
        if name is None:
            name = self.name
        
        circuit = self.cktfab.new_circuit(name=name)
        self.circuits += circuit
        return circuit

    def new_layout(self, *,
        name: Optional[str]=None, boundary: Optional[geo._Rectangular]=None,
    ):
        """Create a new empty layout for the cell.

        Arguments:
            name: the name of the circuit. If not specified the same name as the
                cell will be used.
            boundary: optional boundary for the layout
        """
        if name is None:
            name = self.name

        layout = self.layoutfab.new_layout(boundary=boundary)
        self.layouts += _CellLayout(name=name, layout=layout)
        return layout

    def new_circuitlayouter(self, *,
        name: Optional[str]=None, boundary: Optional[geo._Rectangular]=None,
    ) -> "lay._CircuitLayouter":
        """Create a circuit layouter for a circuit of the cell.

        Arguments:
            name: optional name for the circuit
        API Notes:
            _CircuitLayouter API is not fixed.
                see: https://gitlab.com/Chips4Makers/PDKMaster/-/issues/25
        """
        if name is None:
            name = self.name
            circuit = self.circuit
        else:
            try:
                circuit = self.circuits[name]
            except KeyError:
                raise ValueError(f"circuit with name '{name}' not present")

        layouter = self.layoutfab.new_circuitlayouter(
            circuit=circuit, boundary=boundary,
        )
        self.layouts += _CellLayout(name=name, layout=layouter.layout)
        return layouter

    @property
    def subcells_sorted(self):
        cells = set()
        for circuit in self.circuits:
            for cell in circuit.subcells_sorted:
                if cell not in cells:
                    yield cell
                    cells.add(cell)


class _OnDemandCell(_Cell[LibraryType], abc.ABC, Generic[LibraryType]):
    """_Cell with on demand circuit and layout creation
    
    The circuit and layout will only be generated the first time it is accessed.
    """
    @property
    def circuit(self):
        try:
            return self.circuits[self.name]
        except KeyError:
            self._create_circuit()
            try:
                return self.circuits[self.name]
            except:
                raise NotImplementedError(
                    f"Cell '{self.name}' default circuit generation"
                )

    @property
    def layout(self):
        try:
            return self.layouts[self.name]
        except KeyError:
            self._create_layout()
            try:
                return self.layouts[self.name]
            except:
                raise NotImplementedError(
                    f"Cell '{self.name}' default layout generation"
                )

    @abc.abstractmethod
    def _create_circuit(self):
        ... # pragma: no cover

    @abc.abstractmethod
    def _create_layout(self):
        ... # pragma: no cover


class _Cells(_util.TypedListStrMapping[_Cell[LibraryType]], Generic[LibraryType]):
    @property
    def _elem_type_(self):
        return _Cell


class _CellLayout:
    def __init__(self, *, name: str, layout: "lay._Layout"):
        self.name = name
        self.layout = layout


class _CellLayouts(_util.TypedListStrMapping[_CellLayout]):
    @property
    def _elem_type_(self):
        return _CellLayout

    def __getitem__(self, item: str) -> "lay._Layout":
        elem = super().__getitem__(item)
        assert isinstance(elem, _CellLayout)
        return elem.layout


class RoutingGauge:
    """
    API Notes:
        API for RoutingGause is not fixed. Backwards incompatible changes may still be
            expected.
        see: https://gitlab.com/Chips4Makers/PDKMaster/-/issues/36
            code likely to be moved to c4m-flexcell in the future
    """
    directions = frozenset(("horizontal", "vertical"))

    def __init__(self, *,
        tech: tch.Technology,
        bottom: prm.MetalWire, bottom_direction: str, top: prm.MetalWire,
        pitches: Dict[prm.MetalWire, IntFloat]={},
        offsets: Dict[prm.MetalWire, IntFloat]={},
    ):
        self.tech = tech

        metals = tuple(tech.primitives.__iter_type__(prm.MetalWire))
        if bottom not in metals:
            raise ValueError(f"bottom is not a MetalWire of technology '{tech.name}'")
        if top not in metals:
            raise ValueError(f"top is not a MetalWire of technology '{tech.name}'")
        bottom_idx = metals.index(bottom)
        top_idx = metals.index(top)
        if bottom_idx >= top_idx:
            raise ValueError("bottom layer has to be below top layer")
        self.bottom = bottom
        self.top = top

        if not bottom_direction in self.directions:
            raise ValueError(f"bottom_direction has to be one of {self.directions}")
        self.bottom_direction = bottom_direction

        for wire, _ in pitches.items():
            if not (
                (wire in metals)
                and (bottom_idx <= metals.index(wire) <= top_idx)
            ):
                raise ValueError(f"wire '{wire.name}' is not part of the Gauge set")
        pitches2: Dict[prm.MetalWire, float] = {
            wire: _util.i2f(pitch) for wire, pitch in pitches.items()
        }
        self.pitches = pitches2

        for wire, _ in offsets.items():
            if not (
                (wire in metals)
                and (bottom_idx <= metals.index(wire) <= top_idx)
            ):
                raise ValueError(f"wire '{wire.name}' is not part of the Gauge set")
        offsets2: Dict[prm.MetalWire, float] = {
            wire: _util.i2f(offset) for wire, offset in offsets.items()
        }
        self.offsets = offsets2


class Library:
    """
    API Notes:
        API with global_nets not None is not fully clear yet. Libraries with
            global_nets not None may get backwards incompatible changes in the
            future.
    """
    def __init__(self, *,
        name: str, tech: tch.Technology, cktfab: Optional["ckt.CircuitFactory"]=None,
        layoutfab: Optional["lay.LayoutFactory"]=None,
        global_nets: OptSingleOrMulti[str].T=None,
    ):
        self.name = name
        self.tech = tech
        if cktfab is None:
            cktfab = ckt.CircuitFactory(tech=tech)
        self.cktfab = cktfab
        if layoutfab is None:
            layoutfab = lay.LayoutFactory(tech=tech)
        self.layoutfab = layoutfab

        if global_nets is not None:
            global_nets2 = cast(Tuple[str, ...], _util.v2t(global_nets))
            self.global_nets = frozenset(global_nets2)
        else:
            self.global_nets = None

        self.cells = _Cells[Library]()
    
    def new_cell(self, *, name: str) -> _Cell["Library"]:
        cell = _Cell[Library](lib=self, name=name)
        self.cells += cell
        return cell

    @property
    def sorted_cells(self) -> Iterable[_Cell["Library"]]:
        cells = set()
        for cell in self.cells:
            if cell not in cells:
                for subcell in cell.subcells_sorted:
                    if subcell not in cells:
                        yield subcell
                        cells.add(subcell)
                yield cell
                cells.add(cell)


class StdCellLibrary(Library):
    """
    API Notes:
        API for StdCellLibrary is not fixed. Backwards incompatible changes may still be
            expected.
        see: https://gitlab.com/Chips4Makers/PDKMaster/-/issues/36
            code likely to be moved to c4m-flexcell in the future
    """
    def __init__(self, *,
        name: str, tech: tch.Technology, cktfab: Optional["ckt.CircuitFactory"]=None,
        layoutfab: Optional["lay.LayoutFactory"]=None,
        global_nets: OptSingleOrMulti[str].T=None,
        routinggauge: SingleOrMulti[RoutingGauge].T,
        pingrid_pitch: IntFloat, row_height: IntFloat,
    ):
        super().__init__(
            name=name, tech=tech, cktfab=cktfab, layoutfab=layoutfab,
            global_nets=global_nets,
        )

        self.routinggauge = _util.v2t(routinggauge)
        self.pingrid_pitch = _util.i2f(pingrid_pitch)
        self.row_height = _util.i2f(row_height)

    @property
    def sorted_cells(self) -> Iterable[_Cell["StdCellLibrary"]]:
        return cast(Iterable[_Cell["StdCellLibrary"]], super().sorted_cells)
