# SPDX-License-Identifier: GPL-2.0-or-later OR AGPL-3.0-or-later OR CERN-OHL-S-2.0+
import abc
from typing import Union, Optional, Iterable, overload

from pdkmaster.typing import OptSingleOrMulti

from .. import _util
from ..technology import (
    property_ as prp, net as net_, mask as msk, primitive as prm, technology_ as tch,
)
from . import library as lbry


__all__ = ["CircuitFactory"]


class _Instance(abc.ABC):
    """Base classes representing an instance in a _Circuit.

    Instances in a circuit are created with the `_Circuit.instantiate()` method.
    Arguments to use are given in the docs of that method.

    Attributes:
        ports: the ports of this instances.
    """
    @abc.abstractmethod
    def __init__(self, *, name: str, ports: "_InstanceNets"):
        self.name = name
        ports._freeze_()
        self.ports = ports


class _InstanceNet(net_.Net):
    """Internal `_Instance` support class"""
    def __init__(self, *, inst: _Instance, net: net_.Net):
        super().__init__(net.name)
        self.inst = inst
        self.net = net
        self.full_name = f"{inst.name}.{net.name}"

    def __hash__(self):
        return hash(self.full_name)

    def __eq__(self, other):
        return isinstance(other, _InstanceNet) and ((self.full_name) == other.full_name)


class _InstanceNets(_util.ListStrMappingOverride[_InstanceNet], net_.Nets):
    """Internal `_Instance` support class"""
    @property
    def _elem_type_(self):
        return _InstanceNet

    # TODO: Make sure only nets from the same instance are added


class _Instances(_util.TypedListStrMapping[_Instance]):
    """Internal `_Circuit` support class"""
    @property
    def _elem_type_(self):
        return _Instance


class _PrimitiveInstance(_Instance):
    """Internal `_Instance` support class"""
    def __init__(self, *, name: str, prim: prm._Primitive, **params):
        self.name = name
        super().__init__(
            name=name, ports=_InstanceNets(
                (_InstanceNet(inst=self, net=port) for port in prim.ports),
            )
        )

        self.prim = prim
        self.params = params


class _CellInstance(_Instance):
    """Internal `_Instance` support class"""
    def __init__(self, *,
        name: str, cell: lbry._Cell, circuitname: Optional[str]=None,
    ):
        self.name = name
        self.cell = cell

        if circuitname is None:
            try:
                circuit = self.cell.circuit
            except AttributeError: # pragma: no cover
                raise TypeError(
                    "no circuitname provided for cell without default circuit"
                )
        else:
            circuit = cell.circuits[circuitname]
        self.circuitname = circuitname
        self.circuit = circuit

        super().__init__(
            name=name, ports=_InstanceNets(
                (_InstanceNet(inst=self, net=port) for port in circuit.ports),
            ),
        )

    # TODO: temporary implementation in wait of better engineered polygon iteration
    # implementation in _Layout
    def net_polygons(self, *,
        net: Union[str, net_.Net], layoutname: Optional[str]=None,
    ): # pragma: no cover
        if isinstance(net, str):
            try:
                net = self.circuit.nets[net]
            except KeyError:
                raise ValueError(
                    f"net '{net}' does not exist for instance '{self.name}'"
                    f" of cell '{self.cell.name}'"
                )
        if net not in self.circuit.nets:
            raise ValueError(
                f"net '{net.name}' is not a net of instance '{self.name}'"
                f" of cell '{self.cell.name}'"
            )
        layout = None
        if layoutname is None:
            if self.circuitname is not None:
                try:
                    layout = self.cell.layouts[self.circuitname]
                except KeyError:
                    pass
        else:
            try:
                layout = self.cell.layouts[layoutname]
            except KeyError:
                raise ValueError(
                    f"layout '{layoutname}' does not exist of instance '{self.name}'"
                    f" of cell '{self.cell.name}'"
                )
        if layout is None:
            try:
                layout = self.cell.layout
            except AttributeError:
                raise ValueError(
                    f"cell '{self.cell.name}' of instance '{self.name}'"
                    " does not have a default layout"
                )
        yield from layout.net_polygons(net=net)


class _CircuitNet(net_.Net):
    """A net in a `_Circuit` object.
    It needs to be generated with the `_Circuit.new_net()` method.

    Nets in a circuit are created with the `_Circuit.new_net()` method.
    Arguments to use are given in the docs of that method.

    Attributes:
        circuit: the circuit to which this net belongs
        childports: the ports of the instances that are connected by this net
            See `_Circuit.new_net()` docs on how to populate this collection
        external: wether this is an external net; e.g. a port of the circuit
    """
    def __init__(self, *,
        circuit: "_Circuit", name: str, external: bool,
    ):
        super().__init__(name)
        self.circuit = circuit
        self.childports = _InstanceNets()
        self.external = external

    def freeze(self):
        self.childports._freeze_()


class _CircuitNets(_util.ListStrMappingOverride[_CircuitNet], net_.Nets):
    """Internal `_Circuit` support class"""
    _elem_type = _CircuitNet


class _Circuit:
    """A circuit consists of instances of subelements and nets to connect
    ports of the instances. Nets can be external and nets are then ports
    that can be used in hierarchically instantiated cells.

    New circuits are created with the `CircuitFactory.new_circuit()` method.
    Arguments to use are given in the docs of that method.

    Arguments:
        instances: the instances of this circuit
        nets: the nets of this circuit
        porrts: the ports of this circuit; e.g. the external nets
    """
    def __init__(self, *, name: str, fab: "CircuitFactory"):
        self.name = name
        self.fab = fab

        self.instances = _Instances()
        self.nets = _CircuitNets()
        self.ports = _CircuitNets()

    @overload
    def instantiate(self,
        object_: prm._Primitive, *, name: str, **params,
    ) -> _PrimitiveInstance:
        ... # pragma: no cover
    @overload
    def instantiate(self,
        object_: lbry._Cell, *, name: str, **params,
    ) -> _CellInstance:
        ... # pragma: no cover
    def instantiate(self, object_: Union[prm._Primitive, lbry._Cell], *,
        name: str, **params,
    ) -> _Instance:
        """Instantiate an element in a circuit.

        Arguments:
            object_: the element to instantiate
                Currently a `_Primitive` object or a `_Cell` object are supported
            name: name of the instance
                This name can used to access the instance from the `instances`
                attribute.
            params: the params for the instance.
                Currently params are only support when instantiating a `_Primitive`.
                Parametric circuit are currently not supported.
        """
        if isinstance(object_, prm._Primitive):
            params = object_.cast_params(params)
            inst = _PrimitiveInstance(name=name, prim=object_, **params)
        elif isinstance(object_, lbry._Cell):
            circuitname = params.pop("circuitname", None)
            if params: # pragma: no cover
                raise NotImplementedError("Parametric Circuit instance")
            inst = _CellInstance(name=name, cell=object_, circuitname=circuitname)
        else: # pragma: no cover
            raise TypeError(
                f"object_ has to be of type '_Primitive' or '_Cell', not {type(object_)}",
            )

        self.instances += inst
        return inst

    def new_net(self, *,
        name: str, external: bool, childports: OptSingleOrMulti[_InstanceNet].T=None,
    ):
        """Create a new net in a circuit.

        Arguments:
            name: the name of the net
            external: wether this is an external net; e.g. a port of this circuit
            childports: the ports of instances in this class that are connected
                by this nets.
                A strategy is to first instantiate all elements in a circuit and then
                pass the ports for the nets during circuit generation. Alternative
                is to not specify it during net creation but add ports to `childports`
                attribute when one goes along. Or a combination of both.
        """
        net = _CircuitNet(circuit=self, name=name, external=external)
        self.nets += net
        if external:
            self.ports += net
        if childports:
            net.childports += childports
        return net

    @property
    def subcells_sorted(self) -> Iterable[lbry._Cell]:
        """Return sorted iterable of the hierarchical cell instantiation.
        The cells will be sorted such that a cell is in the list before a
        cell where it is instantiated.

        Main use of this attribute will be for the `Library.subcells_sorted`
        attribute.
        """
        cells = set()
        for inst in self.instances.__iter_type__(_CellInstance):
            if inst.cell not in cells:
                for subcell in inst.cell.subcells_sorted:
                    if subcell not in cells:
                        yield subcell
                        cells.add(subcell)
                yield inst.cell
                cells.add(inst.cell)

    def net_lookup(self, *, port: "_InstanceNet") -> "_CircuitNet":
        """Look up to which net a instance port belongs.

        Arguments:
            port: the port to look up
        """
        for net in self.nets:
            for childport in net.childports:
                if (childport.inst == port.inst) and (childport.name == port.name):
                    return net
        else:
            raise ValueError(
                f"Net for port {port.name} of instance {port.inst.name} not found",
            )


class _Circuits(_util.TypedListStrMapping[_Circuit]):
    """Internal `_Cell` support cloass"""
    @property
    def _elem_type_(self):
        return _Circuit


class CircuitFactory:
    """The user facing class for creating circuits. This class is also a base
    class on which own factory classes can be built with specific extensions.

    Parameters:
        tech: the technology for which to create circuits. Created circuits may
            only contain instances from primitives from this technology.

    API Notes:
        The contract for making subclasses has not been finaziled. Backwards
            incompatible changes are still expected for subclasses of this class.
    """
    def __init__(self, *, tech: tch.Technology):
        self.tech = tech

    def new_circuit(self, *, name: str):
        """Create a circuit.

        This method is the user facing API to generate circuits.
        Returns a `_Circuit` object; see docs for that class on user facing API
        for that class.
        """
        return _Circuit(name=name, fab=self)
