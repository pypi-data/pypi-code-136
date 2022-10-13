# SPDX-License-Identifier: GPL-2.0-or-later OR AGPL-3.0-or-later OR CERN-OHL-S-2.0+
from typing import Tuple, Dict, Iterable, Optional, Any

from PySpice.Spice.Netlist import Circuit, SubCircuit
from PySpice.Unit import u_µm, u_Ω # type: ignore

from .typing import CornerSpec
from ... import _util
from ...technology import primitive as _prm
from ...design import circuit as _ckt


__all__ = ["PySpiceFactory"]


def _sanitize_name(name):
    return name.replace("(", "[").replace(")", "]")


class _SubCircuit(SubCircuit):
    def __init__(self, *, circuit: _ckt._Circuit, lvs: bool):
        ports = tuple(_sanitize_name(port.name) for port in circuit.ports)
        name = _sanitize_name(circuit.name)

        super().__init__(name, *ports)
        self._circuit = circuit

        netlookup = {}
        for net in circuit.nets:
            lookup = {port: net for port in net.childports}
            double = tuple(filter(lambda n: n in netlookup, lookup))
            if double:
                doublenames = tuple(net.full_name for net in double)
                raise ValueError(
                    f"Ports {doublenames} are on more than one net in circuit "
                    f"{circuit.name}"
                )
            netlookup.update(lookup)

        for inst in circuit.instances:
            if isinstance(inst, _ckt._PrimitiveInstance):
                if isinstance(inst.prim, _prm.MOSFET):
                    sgdb = []
                    for portname in (
                        "sourcedrain1", "gate", "sourcedrain2", "bulk",
                    ):
                        port = inst.ports[portname]
                        try:
                            net = netlookup[port]
                        except KeyError:
                            raise ValueError(
                                f"Port '{port.full_name}' not on any net in circuit "
                                f"'{name}'"
                            )
                        else:
                            sgdb.append(_sanitize_name(net.name))
                    # TODO: support more instance parameters
                    self.M(inst.name, *sgdb,
                        model=inst.prim.model,
                        l=u_µm(round(inst.params["l"],6)), w=u_µm(round(inst.params["w"],6)),
                    )
                elif isinstance(inst.prim, _prm.Bipolar):
                    cbe = []
                    for portname in ("collector", "base", "emitter"):
                        port = inst.ports[portname]
                        try:
                            net= netlookup[port]
                        except KeyError:
                            raise ValueError(
                                f"Port '{port.full_name}' not on any net in circuit "
                                f"'{name}'"
                            )
                        else:
                            cbe.append(_sanitize_name(net.name))
                    if not inst.prim.is_subcircuit:
                        self.Q(inst.name, *cbe, model=inst.prim.model)
                    else:
                        self.X(inst.name, inst.prim.model, *cbe)
                elif isinstance(inst.prim, _prm.Resistor):
                    has_model = inst.prim.model is not None
                    has_sheetres = inst.prim.sheetres is not None
                    if not (has_model or has_sheetres):
                        raise NotImplementedError(
                            "Resistor circuit generation without a model or sheet resistance"
                        )

                    if (not has_model) or lvs:
                        l = inst.params["height"]
                        w = inst.params["width"]
                        assert inst.prim.sheetres is not None
                        self.R(
                            inst.name,
                            _sanitize_name(netlookup[inst.ports.port1].name),
                            _sanitize_name(netlookup[inst.ports.port2].name),
                            u_Ω(round(inst.prim.sheetres*l/w, 10)),
                        )
                    else:
                        assert has_model
                        params = inst.prim.subckt_params
                        w = round(inst.params["width"], 6)
                        l = round(inst.params["height"], 6)
                        if params is None:
                            assert inst.prim.sheetres is not None
                            self.SemiconductorResistor(
                                inst.name,
                                _sanitize_name(netlookup[inst.ports.port1].name),
                                _sanitize_name(netlookup[inst.ports.port2].name),
                                u_Ω(round(inst.prim.sheetres*l/w, 10)),
                                model=inst.prim.model, w=u_µm(w), l=u_µm(l),
                            )
                        else:
                            model_args = {
                                params["width"]: w,
                                params["height"]: l,
                            }
                            self.X(
                                inst.name, inst.prim.model,
                                _sanitize_name(netlookup[inst.ports.port1].name),
                                _sanitize_name(netlookup[inst.ports.port2].name),
                                **model_args,
                            )
                elif isinstance(inst.prim, _prm.MIMCapacitor):
                    # TODO: Implement lvs
                    w = inst.params["width"]
                    h = inst.params["height"]
                    if inst.prim.subckt_params is not None:
                        param_names = inst.prim.subckt_params
                    else:
                        param_names = {"width": "w", "height": "l"}
                    model_args = {param_names["width"]: w, param_names["height"]: h}
                    # TODO: Make port order configurable
                    self.X(
                        inst.name, inst.prim.model,
                        _sanitize_name(netlookup[inst.ports.top].name),
                        _sanitize_name(netlookup[inst.ports.bottom].name),
                        **model_args,
                    )
                elif isinstance(inst.prim, _prm.Diode):
                    if inst.prim.model is None:
                        raise NotImplementedError("Diode generation without a model")
                    w = inst.params["width"]
                    h = inst.params["height"]
                    self.D(
                        inst.name,
                        _sanitize_name(netlookup[inst.ports.anode].name),
                        _sanitize_name(netlookup[inst.ports.cathode].name),
                        model=inst.prim.model, area=round(w*h, 6)*1e-12, pj=u_µm(round(2*(w + h), 6)),
                    )
            elif isinstance(inst, _ckt._CellInstance):
                pin_args = tuple()
                for port in inst.ports:
                    try:
                        net = netlookup[port]
                    except KeyError:
                        raise ValueError(
                            f"Port '{port.full_name}' not on any net in circuit "
                            f"'{name}'"
                        )
                    else:
                        pin_args += (net.name,)
                pin_args = tuple(
                    _sanitize_name(netlookup[port].name) for port in inst.ports
                )
                self.X(inst.name, _sanitize_name(inst.circuit.name), *pin_args)
            else:
                raise AssertionError("Internal error")


class _Circuit(Circuit):
    def __init__(self, *,
        fab: "PySpiceFactory", corner: CornerSpec, top: _ckt._Circuit,
        subckts: Optional[Iterable[_ckt._Circuit]], title: Optional[str], gnd: Optional[str],
    ):
        if title is None:
            title = f"{top.name} testbench"
        super().__init__(title)

        corner = _util.v2t(corner)
        invalid = tuple(filter(lambda c: c not in fab.corners, corner))
        if invalid:
            raise ValueError(f"Invalid corners(s) {invalid}")
        for c in corner:
            try:
                conflicts = fab.conflicts[c]
            except KeyError:
                pass
            else:
                for c2 in conflicts:
                    if c2 in corner:
                        raise ValueError(
                            f"Corner '{c}' conflicts with corner '{c2}'"
                        )
            self.lib(fab.libfile, c)

        self._fab = fab
        self._corner = corner

        if subckts is None:
            scan = [top]
            scanned = []

            while scan:
                circuit = scan.pop()
                try:
                    # If it is in the scanned list put the circuit at the end
                    scanned.remove(circuit)
                except ValueError:
                    # If it is not in the scanned list, add subcircuits in the scan list
                    for inst in circuit.instances.__iter_type__(_ckt._CellInstance):
                        circuit2 = inst.cell.circuit
                        try:
                            scan.remove(circuit2)
                        except ValueError:
                            pass
                        scan.append(circuit2)
                scanned.append(circuit)
            scanned.reverse()
            subckts = scanned
        psubckts = tuple(
            fab.new_pyspicesubcircuit(circuit=c) for c in (*subckts, top)
        )
        for subckt in psubckts:
            self.subcircuit(subckt)
        self.X(
            "top", top.name,
            *(self.gnd if node==gnd else node for node in psubckts[-1]._external_nodes),
        )

    # Stop pylance from deriving types from PySpice code
    def simulator(self, *args, **kwargs) -> Any:
        return super().simulator(*args, **kwargs)


class PySpiceFactory:
    def __init__(self, *,
        libfile: str, corners: Iterable[str], conflicts: Dict[str, Tuple[str, ...]],
    ):
        s = (
            "conflicts has to be a dict where the element value is a list of corners\n"
            "that conflict with the key"
        )
        for key, value in conflicts.items():
            if (key not in corners) or any(c not in corners for c in value):
                raise ValueError(s)

        self.libfile = libfile
        self.corners = set(corners)
        self.conflicts = conflicts

    def new_pyspicecircuit(self, *,
        corner: CornerSpec, top: _ckt._Circuit,
        subckts: Optional[Iterable[_ckt._Circuit]]=None, title: Optional[str]=None,
        gnd: Optional[str]=None,
    ):
        return _Circuit(
            fab=self, corner=corner, top=top, subckts=subckts, title=title,
            gnd=gnd,
        )

    def new_pyspicesubcircuit(self, *, circuit: _ckt._Circuit, lvs: bool=False):
        return _SubCircuit(circuit=circuit, lvs=lvs)
