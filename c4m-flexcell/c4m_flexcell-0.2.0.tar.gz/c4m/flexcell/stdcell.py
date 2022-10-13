# SPDX-License-Identifier: GPL-2.0-or-later OR AGPL-3.0-or-later OR CERN-OHL-S-2.0+
import itertools
from typing import (
    Any, Iterable, Mapping, MutableSet, Sequence, Tuple, List, Dict, Set,
    Optional, Union, TypeVar, cast, overload,
)
from six import add_metaclass
from abc import ABCMeta, abstractmethod

from pdkmaster.technology import primitive as _prm, geometry as _geo
from pdkmaster.design import circuit as _ckt, library as _lbry

from . import library as _loclbry

__all__ = ["BBox", "Wire", "Via", "Device", "StdCell"]

def _mean(v):
    return sum(v)/len(v)


class _OrderedPoint:
    def __init__(self, point: _geo.Point):
        self.x = point.x
        self.y = point.y
    def __lt__(self, other: "_OrderedPoint"):
        return self.x < other.x if self.x != other.x else self.y < other.y
    def __gt__(self, other: "_OrderedPoint"):
        return self.x > other.x if self.x != other.x else self.y > other.y
    def __eq__(self, other: "_OrderedPoint"):
        return (self.x == other.x) and (self.y == other.y)
    def __le__(self, other: "_OrderedPoint"):
        return self.x < other.x if self.x != other.x else self.y <= other.y
    def __ge__(self, other: "_OrderedPoint"):
        return self.x > other.x if self.x != other.x else self.y >= other.y
    def __ne__(self, other: "_OrderedPoint"):
        return (self.x != other.x) or (self.y != other.y)


BBoxType = TypeVar("BBoxType", bound="BBox")
class BBox:
    def __init__(self, x1: int, y1: int, x2: int, y2: int):
        assert x1 <= x2 and y1 <= y2
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def __repr__(self):
        return "({},{})-({},{})".format(self.x1, self.y1, self.x2, self.y2)

    def overlaps(self, box: "BBox") -> bool:
        return ((self.x2 >= box.x1)
                and (box.x2 >= self.x1)
                and (self.y2 >= box.y1)
                and (box.y2 >= self.y1)
               )

    def encloses(self, box: "BBox") -> bool:
        return ((self.x1 <= box.x1)
                and (self.y1 <= box.y1)
                and (self.x2 >= box.x2)
                and (self.y2 >= box.y2)
               )

    def copy(self: BBoxType) -> BBoxType:
        return self.__class__(self.x1, self.y1, self.x2, self.y2)


_LayerBoxType = TypeVar("_LayerBoxType", bound="_LayerBox")
class _LayerBox(BBox):
    def __init__(self, layer: str, x1: int, y1: int, x2: int, y2: int):
        super().__init__(x1, y1, x2, y2)
        self.layer = layer
        
    def __repr__(self):
        return "{}({})".format(self.layer, super().__repr__())
        
    def overlaps(self, box: "_LayerBox") -> bool:
        return (self.layer == box.layer) and super().overlaps(box)
    
    def encloses(self, box: "_LayerBox") -> bool:
        return (self.layer == box.layer) and super().encloses(box)

    def copy(self: _LayerBoxType) -> _LayerBoxType:
        return self.__class__(self.layer, self.x1, self.y1, self.x2, self.y2)


class _UniqueNetName:
    def __init__(self):
        self.netnr: int = 0

    def new(self):
        s = "*{:04d}".format(self.netnr)
        self.netnr += 1
        return s


class _LayerBoxesNets:
    def __init__(self):
        self._layerboxes: Dict[str, List[Tuple[_LayerBox, str]]] = {}
        self._netaliases: Dict[str, str] = {}
        self._uniquenet = _UniqueNetName()

    def add_alias(self, net1: str, net2: str) -> str:
        assert (net1 != "fused_net") and (net1 in self._netaliases)
        net1 = self.from_alias(net1)
        if net2 == "fused_net":
            net2 = self._uniquenet.new()
        if net2 not in self._netaliases:
            if net2[0] == "*":
                return net1
            else:
                assert net1[0] == "*", "Shorted net {} and {}".format(net1, net2)
                self._netaliases[net1] = net2
                # It can be that net2 is not in aliases when called for first time
                if net2 not in self._netaliases:
                    self._netaliases[net2] = net2
                return net2
        else:
            # net1 and net2 are there, really join them
            net2 = self.from_alias(net2)
            if net1 == net2:
                net = net1
            elif net2[0] != "*":
                assert net1[0] == "*", "Shorted nets {} and {}".format(net1, net2)
                net = net2
                self._netaliases[net1] = net
            else:
                net = net1
                self._netaliases[net2] = net

            return net

    def from_alias(self, net: str) -> str:
        while self._netaliases[net] != net:
            net = self._netaliases[net]
        return net

    def finalize_nets(self) -> Set[str]:
        starnets = set()
        for net in self._netaliases.keys():
            net2 = self.from_alias(net)
            if net2[0] == "*":
                starnets.add(net2)
        newnets = dict(
            (net, "_net{}".format(i)) for i, net in enumerate(starnets)
        )
        self._netaliases.update(newnets)
        self._netaliases.update(dict(
            (net, net) for net in newnets.values()
        ))
        return set(self.from_alias(net) for net in self._netaliases)

    def add_box(self, net: str, box: _LayerBox) -> str:
        layer = box.layer
        if layer in self._layerboxes:
            boxes = self._layerboxes[layer]
        else:
            self._layerboxes[layer] = boxes = []

        for box2, net2 in boxes:
            if box.overlaps(box2):
                net = self.add_alias(net2, net)

        if net == "fused_net":
            # Get name for unnamed net
            net = self._uniquenet.new()
        if net not in self._netaliases:
            self._netaliases[net] = net

        boxes.append((box, net))

        return net

@add_metaclass(ABCMeta)
class _Element:
    # Sizing parameters for bounding box derivation

    def __init__(self, *,
        external: bool, boxes: Sequence[_LayerBox], name: Optional[str],
        conn, space,
    ):
        self.external = external
        self._ignore = False
        self.boxes = boxes
        if name is not None:
            self.name = name
        if conn is not None:
            self.conn = conn
        if space is not None:
            self.space = space

        self.connects: Dict[str, Sequence["_Element"]] = {}

    def iterate_anchors(self):
        try:
            for s in self.conn.values():
                yield s
        except AttributeError:
            pass
        try:
            for s in self.space.values():
                yield s
        except AttributeError:
            pass
    
    def _str_indent(self,
        level: int, str_elem: str, prefix: str, level_str: str, net: Optional[str],
        recursive: bool=True,
    ) -> str:
        s = level*level_str + prefix + str_elem

        if recursive:
            if net is None:
                if len(self.connects) > 0:
                    for subnet, elems in self.connects.items():
                        s += "\n{}{}Net: {}".format((level + 1)*level_str, prefix, subnet)
                        for elem in elems:
                            s += "\n"+elem.str_indent(level+2, prefix=prefix, level_str=level_str, net=subnet)
            elif net in self.connects:
                for elem in self.connects[net]:
                    s += "\n"+elem.str_indent(level+1, prefix=prefix, level_str=level_str, net=net)
    
        return s

    @abstractmethod
    def str_indent(self,
        level: int, prefix: str="", level_str: str="  ", net: Optional[str]=None,
        recursive: bool=True,
    ) -> str:
        raise NotImplementedError("Abstract method not implemented")
    
    def __str__(self) -> str:
        return self.str_indent(0)
    
    def overlaps(self, other: "_Element") -> bool:
        for box1, box2 in itertools.product(self.boxes, other.boxes):
            if box1.overlaps(box2):
                return True
        
        return False
    
    def add_boxes(self, layerboxes: _LayerBoxesNets):
        if hasattr(self, "net"):
            for box in self.boxes:
                self.net = layerboxes.add_box(self.net, box)
        else:
            for i, box in enumerate(self.boxes):
                self.nets[i] = layerboxes.add_box(self.nets[i], box)

    def add_connects(self, net: str, connects: Sequence["_Element"]):
        self.connects[net] = connects

    def iterate_connects(self, net: Optional[str]=None, include_ignored: bool=False):
        stack = [self.connects]
        
        while stack:
            connects = stack.pop()
            for elems_net, elems in connects.items():
                if (net is None) or (net == elems_net):
                    for elem in elems:
                        if (not elem._ignore) or include_ignored:
                            yield elem
                        stack.append(elem.connects)

    def get_nets(self) -> Sequence[str]:
        try:
            nets = [self.net]
        except AttributeError:
            nets = self.nets
        
        return nets

    def update_nets(self, layerboxes: _LayerBoxesNets):
        try:
            self.net = layerboxes.from_alias(self.net)
        except AttributeError:
            assert hasattr(self, "nets")
            self.nets = [
                layerboxes.from_alias(net)
                for net in cast(Sequence[str], self.nets)
            ]

    def _merge(self, elem: "_Element") -> bool:
        return False
    
    def merge(self, elem: "_Element") -> bool:
        if self._ignore or elem._ignore:
            return False
        else:
            return self._merge(elem) or elem._merge(self)

    @abstractmethod
    def python_code(self, lookup: Mapping[str, str]={}) -> str:
        raise NotImplementedError("Abstract method not implemented")

    @abstractmethod
    def get_center(self) -> _geo.Point:
        raise NotImplementedError("Abstract method not implemented")


class Wire(_Element):
    layers = (
        "NWELL", "PWELL", "NTIE", "PTIE", "NDIF", "PDIF", "POLY",
        "METAL1", "METAL2", "METAL3",
    )
    dhw = {
        "NWELL": 0, "PWELL": 0, "NTIE": 2, "PTIE": 2, "NDIF": 2, "PDIF": 2,
        "POLY": 0, "METAL1": 0, "METAL2": 0, "METAL3": 0
    }
    dhl = {
        "NWELL": 0, "PWELL": 0, "NTIE": 2, "PTIE": 2, "NDIF": 2, "PDIF": 2,
        "POLY": 2, "METAL1": 2, "METAL2": 2, "METAL3": 2
    }

    @overload
    def __init__(self,
        layer: str, x: Tuple[int, int], y: int, width: int,
        external: bool=False, *,
        name: Optional[str]=None, conn=None, space=None,
    ) -> None:
        ... # pragma: no cover
    @overload
    def __init__(self,
        layer: str, x: int, y: Tuple[int, int], width: int,
        external: bool=False, *,
        name: Optional[str]=None, conn=None, space=None,
    ) -> None:
        ... # pragma: no cover
    def __init__(self,
        layer: str,
        x: Union[int, Tuple[int, int]], y: Union[int, Tuple[int, int]],
        width: int, external: bool=False, *,
        name: Optional[str]=None, conn=None, space=None,
    ) -> None:
        # assert isinstance(x, tuple) ^ isinstance(y, tuple)
        assert layer in self.layers

        self.layer = layer
        self.x = x
        self.y = y
        self.width = width

        dhw = self.dhw[layer]
        dhl = self.dhl[layer]
        if not isinstance(x, tuple):
            x1 = x - width//2 - dhw
            x2 = x + width//2 + dhw
        else:
            x1 = x[0] - dhl
            x2 = x[1] + dhl
        if not isinstance(y, tuple):
            y1 = y - width//2 - dhw
            y2 = y + width//2 + dhw
        else:
            y1 = y[0] - dhl
            y2 = y[1] + dhl
        boxes = [_LayerBox(layer, x1, y1, x2, y2)]
        if layer == "NTIE": # Make NWELL connection
            boxes.append(_LayerBox("NWELL", x1, y1, x2, y2))
        super().__init__(
            external=external, boxes=boxes, name=name, conn=conn, space=space,
        )

    def _merge(self, elem: _Element) -> bool:
        if not (isinstance(elem, Wire) and (self.layer == elem.layer)):
            return False

        merged = False

        box_self = self.boxes[0]
        box_elem = elem.boxes[0]
        hor_self = isinstance(self.x, tuple)
        hor_elem = isinstance(elem.x, tuple)
        if box_self.encloses(box_elem):
            self.external |= elem.external
            elem._ignore = True
            merged = True
        elif box_elem.encloses(box_self):
            self._ignore = True
            elem.external |= self.external
            merged = True
        elif (not hor_self) and (not hor_elem): # Both vertical
            assert isinstance(self.y, tuple) and isinstance(elem.y, tuple)
            if (self.x == elem.x) and (self.width == elem.width) and (self.y[1] >= elem.y[0]) and (elem.y[1] >= self.y[0]):
                self.y1 = box_self.y1 = min(box_self.y1, box_elem.y1)
                self.y2 = box_self.y2 = max(box_self.y2, box_elem.y2)
                self.y = (min(self.y[0], elem.y[0]), max(self.y[1], elem.y[1]))
                self.external |= elem.external
                elem._ignore = True
                merged = True
        elif hor_self and hor_elem: # Both horizontal
            assert isinstance(self.x, tuple) and isinstance(elem.x, tuple)
            if (self.y == elem.y) and (self.width == elem.width) and (self.x[1] >= elem.x[0]) and (elem.x[1] >= self.x[0]):
                self.x1 = box_self.x1 = min(box_self.x1, box_elem.x1)
                self.x2 = box_self.x2 = max(box_self.x2, box_elem.x2)
                self.x = (min(self.x[0], elem.x[0]), max(self.x[1], elem.x[1]))
                self.external |= elem.external
                elem._ignore = True
                merged = True

        if merged:
            # Some segments may have more than one box for connectivity, f.ex. NTIE with NWELL
            for box in self.boxes[1:]:
                box.x1 = box_self.x1
                box.x2 = box_self.x2
                box.y1 = box_self.y1
                box.y2 = box_self.y2
            for box in elem.boxes[1:]:
                box.x1 = box_elem.x1
                box.x2 = box_elem.x2
                box.y1 = box_elem.y1
                box.y2 = box_elem.y2

        return merged

    def str_indent(self,
        level: int, prefix: str="", level_str: str="  ", net: Optional[str]=None,
        recursive: bool=True,
    ) -> str:
        box = self.boxes[0]
        str_elem = "{}{}(({},{})-({},{}))".format(
            "EXT_" if self.external else "",
            self.layer,
            box.x1, box.y1, box.x2, box.y2,
        )

        return self._str_indent(level, str_elem, prefix, level_str, net, recursive)

    def python_code(self, lookup: Mapping[str, str]={}) -> str:
        classstr = lookup.get("Wire", "Wire")
        return "{}({!r}, {!r}, {!r}, {!r}, {!r})".format(
            classstr, self.layer, self.x, self.y, self.width, self.external,
        )

    def get_center(self) -> _geo.Point:
        x = self.x if not isinstance(self.x, tuple) else _mean(self.x)
        y = self.y if not isinstance(self.y, tuple) else _mean(self.y)
        return _geo.Point(x=x, y=y)


class Via(_Element):
    dhw = {
        "NTIE": 6,
        "PTIE": 6,
        "NDIF": 6,
        "PDIF": 6,
        "POLY": 6,
        "METAL1": 4,
        "METAL2": 4,
        "METAL3": 4,
    }

    def __init__(self,
        bottom: str, top: str, x: int, y: int, width: int, *,
        name: Optional[str]=None, conn=None, space=None,
    ):
        self.x = x
        self.y = y
        self.width = width
        self.bottom = bottom
        self.top = top

        dhw_bottom = width//2 + self.dhw[bottom]
        dhw_top = width//2 + self.dhw[top]
        boxes = [
            _LayerBox(bottom, x - dhw_bottom, y - dhw_bottom, x + dhw_bottom, y + dhw_bottom),
            _LayerBox(top, x - dhw_top, y - dhw_top, x + dhw_top, y + dhw_top),
        ]

        super().__init__(
            external=False, boxes=boxes, name=name, conn=conn, space=space,
        )

    def str_indent(self,
        level: int, prefix: str="", level_str: str="  ", net: Optional[str]=None,
        recursive: bool=True,
    ) -> str:
        str_elem = "{}<->{}(({},{}))".format(
            self.bottom, self.top,
            self.x, self.y,
        )

        return self._str_indent(level, str_elem, prefix, level_str, net, recursive)

    def python_code(self, lookup: Mapping[str, str]={}) -> str:
        classstr = lookup.get("Via", "Via")
        return "{}({!r}, {!r}, {!r}, {!r}, {!r})".format(
            classstr, self.bottom, self.top, self.x, self.y, self.width,
        )

    def get_center(self) -> _geo.Point:
        return _geo.Point(x=self.x, y=self.y)


class Device(_Element):
    SDType = Union[str, _LayerBox]
    type2gatelayer = {
        "nmos": "POLY",
        "pmos": "POLY",
    }
    type2difflayer = {
        "nmos": "NDIF",
        "pmos": "PDIF",
    }
    dhl = 0
    dhw = 4
    diffwidth = 6

    def __init__(self,
        type_: str, x: int, y: int, l: int, w: int, direction: str, *,
        name: Optional[str]=None, source_net: str="fused_net", drain_net: str="fused_net",
    ):
        assert type_ in ("nmos", "pmos")

        self.type = type_
        self.x = x
        self.y = y
        self.l = l
        self.w = w
        assert direction in ("vertical") # Todo support horizontal transistors
        self.direction = direction
        source: Dict[str, Device.SDType]
        drain: Dict[str, Device.SDType]
        self.source = source = {"net": cast(Device.SDType, source_net)}
        self.drain = drain = {"net": cast(Device.SDType, drain_net)}
        difflayer = self.type2difflayer[type_]
        dhl = l//2 + self.dhl
        dhw = w//2 + self.dhw
        x1_gate = x - dhl
        x2_gate = x + dhl
        y1_gate = y - dhw
        y2_gate = y + dhw
        x2_source = x1_gate
        x1_source = x2_source - self.diffwidth
        y1_source = y - w//2
        y2_source = y + w//2
        x1_drain = x2_gate
        x2_drain = x1_drain + self.diffwidth
        y1_drain = y1_source
        y2_drain = y2_source
        boxes = [_LayerBox(self.type2gatelayer[type_], x1_gate, y1_gate, x2_gate, y2_gate)]
        source["box"] = _LayerBox(difflayer, x1_source, y1_source, x2_source, y2_source)
        drain["box"] = _LayerBox(difflayer, x1_drain, y1_drain, x2_drain, y2_drain)
        super().__init__(
            external=False, boxes=boxes, name=name, conn=None, space=None,
        )

    def str_indent(self,
        level: int, prefix: str="", level_str: str="  ", net: Optional[str]=None,
        recursive: bool=True,
    ) -> str:
        str_elem = "{}(({},{}),l={},w={})".format(
            self.type,
            self.x, self.y,
            self.l, self.w,
        )

        return self._str_indent(level, str_elem, prefix, level_str, net, recursive)

    def python_code(self, lookup: Mapping[str, str]={}) -> str:
        classstr = lookup.get("Device", "Device")
        return "{}({!r}, {!r}, {!r}, {!r}, {!r}, {!r}, source_net={!r}, drain_net={!r})".format(
            classstr, self.type,
            self.x, self.y, self.l, self.w,
            self.direction, self.source["net"], self.drain["net"],
        )

    def get_center(self) -> _geo.Point:
        return _geo.Point(x=self.x, y=self.y)


class StdCell:
    def __init__(self,
        name: str="NoName", width: int=0, height: int=0,
        nets: Dict[str, Sequence[_Element]]={}, finalize: bool=False,
    ):
        self.name = name
        self.width = width
        self.height = height
        self.ports: Set[str] = set()
        self.nets: Dict[str, List[_Element]] = {}
        self.namedelems: Dict[str, _Element] = {}

        self._layerboxesnets = _LayerBoxesNets()

        elem = Wire("METAL1", (0, width), 12, 24, external=True)
        elem._ignore = True
        self.add_elem(elem, net="vss")
        elem = Wire("METAL1", (0, width), 188, 24, external=True)
        elem._ignore = True
        self.add_elem(elem, net="vdd")
        elem = Wire("NWELL", (-6, width+6), 156, 120)
        elem._ignore = True
        self.add_elem(elem, net="vdd")

        for net, elems in nets.items():
            for elem in elems:
                self.add_elem(elem, net)

        if finalize:
            self.finalize()

    def add_elem(self, elem: _Element, net: str="fused_net"):
        assert self._layerboxesnets is not None, "add_elem() called on cell {} in finalized state".format(self.name)

        for box in elem.boxes:
            net = self._layerboxesnets.add_box(net, box)
        if isinstance(elem, Device):
            assert isinstance(elem.source["net"], str)
            assert isinstance(elem.source["box"], _LayerBox)
            elem.source["net"] = self._layerboxesnets.add_box(elem.source["net"], elem.source["box"])
            assert isinstance(elem.drain["net"], str)
            assert isinstance(elem.drain["box"], _LayerBox)
            elem.drain["net"] = self._layerboxesnets.add_box(elem.drain["net"], elem.drain["box"])
        
        try:
            self.nets[net].append(elem)
        except KeyError:
            self.nets[net] = [elem]
        if elem.external:
            self.ports |= {net}

        if hasattr(elem, "name"):
            self.namedelems[elem.name] = elem

    def _add_elem2net(self, net: str, elem: _Element):
        try:
            self.nets[net].append(elem)
        except KeyError:
            self.nets[net] = [elem]

    def _add_elems2net(self, net: str, elems: List[_Element]):
        try:
            self.nets[net] += elems
        except KeyError:
            self.nets[net] = elems

    def _update_devicenets(self, elems: Iterable[_Element]):
        assert self._layerboxesnets is not None
        for elem in elems:
            if isinstance(elem, Device):
                source_net = elem.source["net"]
                assert isinstance(source_net, str)
                elem.source["net"] = new_net = self._layerboxesnets.from_alias(source_net)
                try:
                    elem.connects[new_net] = elem.connects.pop(source_net)
                except KeyError:
                    pass

                drain_net = elem.drain["net"]
                assert isinstance(drain_net, str)
                elem.drain["net"] = new_net = self._layerboxesnets.from_alias(drain_net)
                try:
                    elem.connects[new_net] = elem.connects.pop(drain_net)
                except KeyError:
                    pass

            for _, elems in elem.connects.items():
                self._update_devicenets(elems)

    @staticmethod
    def _connect_elem(net: str, elem: _Element, todo: MutableSet[_Element]):
        # Try to connect elem in todo set of elems and remove the connected ones from todo
        conns = set(filter(lambda other: elem.overlaps(other), todo))
        if conns:
            todo -= conns
            map(lambda elem: StdCell._connect_elem(net, elem, todo), conns)
            elem.add_connects(net, list(conns))

    def iterate_net(self, net: str, include_ignored: bool=False):
        for elem in self.nets[net]:
            if (not elem._ignore) or include_ignored:
                yield elem
            for elem2 in elem.iterate_connects(net, include_ignored=include_ignored):
                yield elem2

    def iterate_devices(self, include_ignored: bool=False):
        for net in self.nets.keys():
            for elem in self.iterate_net(net, include_ignored=include_ignored):
                if isinstance(elem, Device):
                    yield (net, elem)

    def finalize(self) -> Dict[str, Any]:
        assert self._layerboxesnets is not None
        netnames = self._layerboxesnets.finalize_nets()
        retval: Dict[str, Any] = {}

        # Add elems in nets that disappeared to the final net
        removednets = set(self.nets.keys()) - netnames
        for net in removednets:
            self._add_elems2net(self._layerboxesnets.from_alias(net), self.nets.pop(net))
        # Check that all ports have a net associated with it
        assert self.ports.issubset(set(self.nets.keys()))

        # Update the net names
        for elems in self.nets.values():
            self._update_devicenets(elems)

        # Merge elems in a net if possible
        merged = 0
        for net in self.nets.keys():
            for elem1, elem2 in itertools.combinations(self.iterate_net(net), 2):
                if elem1.merge(elem2):
                    merged += 1
        retval["merged"] = merged

        # (Re)connect the overlapping interconnects in a net
        # Do ignore the ignored elems
        for net, elems in self.nets.items(): # Only connect within the same net.
            tops = []
            # Set todo to all elems in the net that are not ignored
            todo = set(self.iterate_net(net))
            assert len(todo) > 0 or net in ("vss", "vdd"), "empty todo for net {}".format(net)
            while len(todo) > 0:
                elem = None
                # First search for external net for a port
                for it in todo:
                    if it.external:
                        elem = it
                        break
                # Then for a METAL1 segment
                if elem is None:
                    for it in todo:
                        if isinstance(it, Wire) and (it.layer == "METAL1"):
                            elem = it
                            break
                # Then first non-device
                if elem is None:
                    for it in todo:
                        if not isinstance(it, Device):
                            elem = it
                            break
                if elem is None:
                    elem = todo.pop()
                else:
                    # Remove selected elem
                    todo -= {elem}
                self._connect_elem(net, elem, todo)
                tops.append(elem)
            # Only retain the top elements in elems
            elems[:] = tops[:]
            #assert len(elems) == 1 or net in ("vss", "vdd")
            # if len(elems) != 1 and net not in ("vss", "vdd"):
            #     print("{} has {} top elems on net {}".format(self.name, len(elems), net))

        self._layerboxesnets = None

        return retval

    def python_code(self,
        level: int=0, level_str: str="    ", lookup: Mapping[str, str]={},
    ) -> str:
        classstr = lookup.get("StdCell", "StdCell")

        def indent_str() -> str:
            return level*level_str
        
        s = indent_str() + classstr + "(\n"
        level += 1
        s += indent_str() + "name={!r}, width={!r}, height={!r},\n".format(
            self.name, self.width, self.height,
        )

        s += indent_str() + "nets={\n"
        level += 1
        for netname in sorted(self.nets.keys()):
            s += indent_str() + "{!r}: [\n".format(netname)
            level += 1
            # Sort elems to have same code for same cell
            for elem in sorted(
                self.iterate_net(netname),
                key=lambda elem: _OrderedPoint(elem.get_center()),
            ):
                s += indent_str() + "{},\n".format(elem.python_code(lookup=lookup))
            level -= 1
            s += indent_str() + "],\n"
        level -= 1
        s += indent_str() + "},\n"

        if not self._layerboxesnets:
            s += "{}finalize=True,".format(indent_str())
        level -= 1
        s += "\n" + indent_str() + "),\n"

        return s

    def spice_netlist(self, lambda_: float=0.09) -> str:
        ports = sorted(self.ports - {"vss", "vdd"})
        s = ".subckt {} {} vss vdd\n".format(self.name, " ".join(ports))
        for i, (net, device) in enumerate(sorted(
            self.iterate_devices(),
            key=lambda elem: _OrderedPoint(elem[1].get_center()),
        )):
            s += "M{} {} {} {} {} {} l={}u w={}u\n".format(
                i + 1,
                device.source["net"], net, device.drain["net"], "vss" if device.type == "nmos" else "vdd",
                device.type,
                device.l*lambda_/2.0, device.w*lambda_/2.0,
            )
        s += ".ends {}\n".format(self.name)

        return s


class _StdCellConverter:
    def __init__(self, *, lib: "_loclbry.Library"):
        self.pdklib = lib
        self.layoutfab = lib.layoutfab
        self.canvas = lib.canvas

    def __call__(self, *, src: StdCell, target: _lbry._Cell):
        canvas = self.canvas

        self.cell = src
        self.pdkcell = target

        self.circuit = target.new_circuit()
        self.layouter = target.new_circuitlayouter(boundary=_geo.Rect(
            left=0.0, bottom=0.0,
            right=canvas._l2r(src.width), top=canvas._l2r(src.height),
        ))

        self.nets: Dict[str, _ckt._CircuitNet] = {}
        self.named_layouts = {}

        self.place_mosfets()
        self.connect_wires()

        self.pdkcell = None
        self.circuit = None
        self.layouter = None
        self.names_layouts = None
        self.vssnet = None
        self.vddnet = None

    def get_net(self, name: str) -> _ckt._CircuitNet:
        try:
            return self.nets[name]
        except KeyError:
            assert self.circuit is not None
            net = self.circuit.new_net(name=name, external=(name in self.cell.ports))
            self.nets[name] = net
            return net

    def place_mosfets(self):
        canvas = self.canvas

        assert self.circuit is not None
        assert self.layouter is not None

        places = []
        for i, (net, device) in enumerate(self.cell.iterate_devices()):
            is_nmos = device.type == "nmos"

            prim = canvas.nmos if is_nmos else canvas.pmos
            w = canvas._l2r(device.w)

            source = self.get_net(cast(str, device.source["net"]))
            drain = self.get_net(cast(str, device.drain["net"]))
            gate = self.get_net(net)
            bulk = self.get_net("vss" if is_nmos else "vdd")

            name = getattr(device, "name", f"mos{i+1}")
            mos = self.circuit.instantiate(prim, name=name, l=canvas.l, w=w)
            source.childports += mos.ports.sourcedrain1
            drain.childports += mos.ports.sourcedrain2
            gate.childports += mos.ports.gate
            bulk.childports += mos.ports.bulk

            places.append((mos, canvas._l2r(device.x), canvas._l2r(device.y)))

        # Place the transistors
        for mos, x, y in places:
            self.named_layouts[mos.name] = self.layouter.place(mos, x=x, y=y)

    def connect_wires(self):
        canvas = self.canvas

        assert self.layouter is not None

        # Standard cell frame wires
        self.vssnet = vssnet = self.get_net("vss")
        self.vddnet = vddnet = self.get_net("vdd")

        elems_spec = (
            (vssnet, "vssrail", Wire("METAL1", (0, self.cell.width), 12, 24)),
            (vddnet, "vddrail", Wire("METAL1", (0, self.cell.width), 188, 24)),
            (vddnet, "well", Wire("NWELL", (-6, self.cell.width + 6), 156, 120)),
        )
        if canvas._pwell is not None:
            elems_spec += (
                (vssnet, "pwell", Wire("PWELL", (-6, self.cell.width + 6), 40, 112)),
            )
        for net, name, elem in elems_spec:
            assert isinstance(elem.x, tuple) and isinstance(elem.y, int)
            wire_params = {
                "net": net,
                "x": canvas._l2r(sum(elem.x)/2.0),
                "y": canvas._l2r(elem.y),
                "width": canvas._l2r(elem.x[1] - elem.x[0]),
                "height": canvas._l2r(elem.width),
            }

            if elem.layer == "METAL1":
                wire_params["wire"] = canvas._metal1
                if canvas._metal1.pin is not None:
                    assert len(canvas._metal1.pin) == 1
                    wire_params["pin"] = canvas._metal1.pin[0]
            elif elem.layer == "NWELL":
                wire_params["wire"] = canvas._nwell
            elif elem.layer == "PWELL":
                wire_params["wire"] = canvas._pwell
            else:
                raise AssertionError("Internal error")

            self.named_layouts[name] = self.layouter.add_wire(**wire_params)

        # Cell wires
        to_process = tuple()
        for net in self.cell.nets.keys():
            to_process += tuple(
                (net, elem, set(elem.iterate_anchors()))
                for elem in self.cell.iterate_net(net)
            )

        def try_place(v):
            net, elem, anchors = v
            if all(s in self.named_layouts for s in anchors):
                self.place_elem(elem, self.get_net(net))
                return True
            else:
                return False

        while to_process:
            n_process = len(to_process)
            to_process = tuple(filter(
                lambda v: not try_place(v), to_process
            ))
            if n_process == len(to_process):
                raise ValueError("Unfound anchor")

    def place_elem(self, elem: _Element, cktnet: _ckt._CircuitNet):
        if isinstance(elem, Device):
            return
        
        if isinstance(elem, Via):
            wire_layout = self.place_Via(elem, cktnet)
        elif isinstance(elem, Wire):
            wire_layout = self.place_Wire(elem, cktnet)
        else:
            raise AssertionError("Internal error")

        if hasattr(elem, "name"):
            assert elem.name not in self.named_layouts
            self.named_layouts[elem.name] = wire_layout

    def place_Via(self, elem: Via, cktnet: _ckt._CircuitNet):
        canvas = self.canvas

        assert self.layouter is not None
        assert any((
            (
                (elem.bottom in ("NDIF", "NTIE", "PDIF", "PTIE", "POLY"))
                and (elem.top == "METAL1")
            ),
            (
                (elem.bottom == "METAL1") and (elem.top == "METAL2")
            ),
            (
                (elem.bottom == "METAL2") and (elem.top == "METAL3")
            ),
        )), "Unsupported Via() specification"

        x = canvas._l2r(elem.x)
        y = canvas._l2r(elem.y)
        wire_params = {"net": cktnet, "x": x, "columns": 1}
        if not (
            hasattr(elem, "space") or hasattr(elem, "conn")
        ):
            wire_params.update({"y": y, "rows": 1})
        else:
            hasspace = hasattr(elem, "space") and (len(elem.space) > 0)
            if (
                (hasspace and not hasattr(elem, "conn"))
                or (elem.bottom == "POLY")
            ):
                wire_params.update({"y": y, "rows": 1})
            else:
                bound_spec = {}

                if "left" in elem.conn:
                    conn_elem = self.cell.namedelems[elem.conn["left"]]
                    assert isinstance(conn_elem, Device)
                    bottom = conn_elem.y - 0.5*conn_elem.w
                    top = bottom + conn_elem.w
                    if "right" in elem.conn:
                        conn_elem = self.cell.namedelems[elem.conn["right"]]
                        assert isinstance(conn_elem, Device)
                        bottom = min(bottom, conn_elem.y - 0.5*conn_elem.w)
                        top = max(top, conn_elem.y + 0.5*conn_elem.w)
                elif "right" in elem.conn:
                    conn_elem = self.cell.namedelems[elem.conn["right"]]
                    assert isinstance(conn_elem, Device)
                    bottom = conn_elem.y - 0.5*conn_elem.w
                    top = bottom + conn_elem.w
                else:
                    raise AssertionError("Internal error")
                if bottom <= elem.y <= top:
                    # Only extend bottom and top if original y was between
                    # the new bottom and top.
                    bound_spec = {
                        "bottom_bottom": canvas._l2r(bottom),
                        "bottom_top": canvas._l2r(top),
                    }

                    if "up" in elem.conn:
                        if (hasspace
                            and (("bottom" in elem.space) or ("top" in elem.space))
                        ):
                            raise ValueError(
                                "Clash between up connection and bottom/top spacing"
                            )
                        conn_layout = self.named_layouts[elem.conn["up"]]
                        bounds = conn_layout.bounds(mask=canvas._metal1.mask)
                        bound_spec.update({
                            "top_bottom": bounds.bottom, "top_top": bounds.top,
                        })
                    if hasspace:
                        if "bottom" in elem.space:
                            space_layout = self.named_layouts[elem.space["bottom"]]
                            bounds = space_layout.bounds(mask=canvas._metal1.mask)
                            bound_spec.update({
                                "top_bottom": bounds.top + canvas._metal1.min_space,
                            })
                        if "top" in elem.space:
                            space_layout = self.named_layouts[elem.space["top"]]
                            bounds = space_layout.bounds(mask=canvas._metal1.mask)
                            bound_spec.update({
                                "top_top": bounds.bottom - canvas._metal1.min_space,
                            })

                    wire_params.update(bound_spec)
                else:
                    wire_params.update({"y": y, "rows": 1})

        if elem.top == "METAL1":
            wire_params["wire"] = canvas._contact
            if len(canvas._contact.top) > 1:
                wire_params["top"] = canvas._metal1
            if elem.bottom in ("NDIF", "NTIE"):
                wire_params.update({
                    "bottom": canvas._active, "bottom_implant": canvas._nimplant,
                })
            if elem.bottom in ("PDIF", "PTIE"):
                wire_params.update({
                    "bottom": canvas._active, "bottom_implant": canvas._pimplant,
                })
            if (elem.bottom in ("NTIE", "PDIF")) and (canvas._nwell is not None):
                wire_params.update({
                    "well_net": self.vddnet, "bottom_well": canvas._nwell,
                })
            if (elem.bottom in ("PTIE", "NDIF")) and (canvas._pwell is not None):
                wire_params.update({
                    "well_net": self.vssnet, "bottom_well": canvas._pwell,
                })
            if elem.bottom == "POLY":
                wire_params["bottom"] = canvas._poly
        elif elem.top == "METAL2":
            wire_params["wire"] = canvas._via1
        else:
            assert (elem.top == "METAL3"), "Internal error"
            wire_params["wire"] = canvas._via2

        wire_layout = self.layouter.add_wire(**wire_params)

        if hasattr(elem, "conn"):
            bottom_wire = wire_params["bottom"]
            bottom_bounds = wire_layout.bounds(mask=bottom_wire.mask)

            if "bottom_implant" in wire_params:
                extra_params = {"implant": wire_params["bottom_implant"]}
            else:
                extra_params = {}
            if "bottom_well" in wire_params:
                well_params = {
                    "well": wire_params["bottom_well"],
                    "well_net": wire_params["well_net"],
                }
            elif "well_net" in wire_params:
                well_params = {"well_net": wire_params["well_net"]}
            else:
                well_params = {}
            extra_params.update(well_params)

            if "left" in elem.conn:
                conn_layout = self.named_layouts[elem.conn["left"]]
                conn_bounds = conn_layout.bounds(mask=bottom_wire.mask)
                self._connect_left(
                    net=cktnet, wire=bottom_wire, **extra_params,
                    from_rect=bottom_bounds, to_rect=conn_bounds,
                )

            if "right" in elem.conn:
                conn_layout = self.named_layouts[elem.conn["right"]]
                conn_bounds = conn_layout.bounds(mask=bottom_wire.mask)
                self._connect_right(
                    net=cktnet, wire=bottom_wire, **extra_params,
                    from_rect=bottom_bounds, to_rect=conn_bounds
                )

            if "bottom" in elem.conn:
                # conn = self.cell.namedelems[elem.conn["bottom"]]
                # assert isinstance(conn, Wire) and conn.layer == "METAL1", "Unsupported"
                conn_layout = self.named_layouts[elem.conn["bottom"]]
                conn_bounds = conn_layout.bounds(mask=canvas._metal1.mask)
                wire_bounds = wire_layout.bounds(mask=canvas._metal1.mask)
                left = wire_bounds.left
                bottom = conn_bounds.bottom
                right = wire_bounds.right
                top = wire_bounds.top

                x = 0.5*(left + right)
                y = 0.5*(bottom + top)
                width = right - left
                height = top - bottom

                self.layouter.add_wire(
                    net=cktnet, wire=canvas._metal1,
                    x=x, y=y, width=width, height=height,
                )

            if "top" in elem.conn:
                # conn = self.cell.namedelems[elem.conn["top"]]
                # assert isinstance(conn, Wire) and conn.layer == "METAL1", "Unsupported"
                conn_layout = self.named_layouts[elem.conn["top"]]
                conn_bounds = conn_layout.bounds(mask=canvas._metal1.mask)
                wire_bounds = wire_layout.bounds(mask=canvas._metal1.mask)
                left = wire_bounds.left
                bottom = wire_bounds.bottom
                right = wire_bounds.right
                top = conn_bounds.top

                x = 0.5*(left + right)
                y = 0.5*(bottom + top)
                width = right - left
                height = top - bottom

                self.layouter.add_wire(
                    net=cktnet, wire=canvas._metal1,
                    x=x, y=y, width=width, height=height,
                )

        return wire_layout

    def place_Wire(self, elem: Wire, cktnet: _ckt._CircuitNet):
        canvas = self.canvas

        assert self.layouter is not None

        wire_params: Dict[str, Any] = {"net": cktnet}

        if isinstance(elem.x, tuple):
            assert isinstance(elem.y, int)
            left = canvas._l2r(elem.x[0])
            right = canvas._l2r(elem.x[1])
            bottom = canvas._l2r(elem.y - 0.5*elem.width)
            top = bottom + canvas._l2r(elem.width)
        elif isinstance(elem.y, tuple):
            left = canvas._l2r(elem.x - 0.5*elem.width)
            right = left + canvas._l2r(elem.width)
            bottom = canvas._l2r(elem.y[0])
            top = canvas._l2r(elem.y[1])
        else:
            raise AssertionError("Internal error")

        wire: Optional[_prm._Conductor] = None
        if elem.layer in ("NDIF", "NTIE"):
            wire = canvas._active
            wire_params.update({
                "wire": wire, "implant": canvas._nimplant,
            })
        if elem.layer in ("PDIF", "PTIE"):
            wire = canvas._active
            wire_params.update({
                "wire": wire, "implant": canvas._pimplant,
            })
        if (elem.layer in ("NTIE", "PDIF")) and (canvas._nwell is not None):
            wire_params.update({
                "well_net": self.vddnet, "well": canvas._nwell,
            })
        if (elem.layer in ("PTIE", "NDIF")) and (canvas._pwell is not None):
            wire_params.update({
                "well_net": self.vssnet, "well": canvas._pwell,
            })
        if elem.layer == "POLY":
            wire_params["wire"] = wire = canvas._poly
        elif elem.layer in ("METAL1", "METAL2", "METAL3"):
            lookup = {
                "METAL1": canvas._metal1,
                "METAL2": canvas._metal2,
                "METAL3": canvas._metal3,
            }
            wire_params["wire"] = wire = lookup[elem.layer]
            if elem.external and wire.pin is not None:
                wire_params["pin"] = wire.pin[0]

        if hasattr(elem, "conn"):
            assert wire is not None
            if "bottom" in elem.conn:
                conn_layout = self.named_layouts[elem.conn["bottom"]]
                bottom = (
                    conn_layout.bounds(mask=wire.mask).top - wire.min_width
                )
            if "top" in elem.conn:
                conn_layout = self.named_layouts[elem.conn["top"]]
                top = (
                    conn_layout.bounds(mask=wire.mask).bottom + wire.min_width
                )

        if hasattr(elem, "space"):
            assert wire is not None
            if "left" in elem.space:
                space_layout = self.named_layouts[elem.space["left"]]
                left = space_layout.bounds(mask=wire.mask).right + wire.min_space

            if "bottom" in elem.space:
                space_layout = self.named_layouts[elem.space["bottom"]]
                bottom = space_layout.bounds(mask=wire.mask).top + wire.min_space

            if "right" in elem.space:
                space_layout = self.named_layouts[elem.space["right"]]
                right = space_layout.bounds(mask=wire.mask).left - wire.min_space

            if "top" in elem.space:
                space_layout = self.named_layouts[elem.space["top"]]
                top = space_layout.bounds(mask=wire.mask).bottom - wire.min_space

        x = (left + right)/2.0
        y = (bottom + top)/2.0
        width = right - left
        height = top - bottom

        if hasattr(elem, "space") or hasattr(elem, "conn") or hasattr(elem, "name"):
            if elem.external:
                assert elem.layer == "METAL1"
                min_width = canvas._pin_width
            else:
                assert wire is not None
                min_width = wire.min_width

            if isinstance(elem.x, tuple):
                height = min_width
            else:
                width = min_width

        # TODO: abs(height) should not be needed
        # it can be caused by top conn that falls inside rail and then the
        # wire does not need to be drawn
        wire_params.update({
            "x": x, "y": y, "width": width, "height": abs(height),
        })

        assert "wire" in wire_params, "Internal error"
        wire_layout = self.layouter.add_wire(**wire_params)

        if hasattr(elem, "conn"):
            assert wire is not None
            for key in ("x", "y", "width", "height"):
                wire_params.pop(key)

            wire_bounds = wire_layout.bounds(mask=wire.mask)
            if "left" in elem.conn:
                conn_layout = self.named_layouts[elem.conn["left"]]
                conn_bounds = conn_layout.bounds(mask=wire.mask)
                self._connect_left(
                    from_rect=wire_bounds, to_rect=conn_bounds, **wire_params,
                )
            if "right" in elem.conn:
                conn_layout = self.named_layouts[elem.conn["right"]]
                conn_bounds = conn_layout.bounds(mask=wire.mask)
                self._connect_right(
                    from_rect=wire_bounds, to_rect=conn_bounds, **wire_params,
                )

        return wire_layout

    def _connect_left(self, *, net, wire, from_rect, to_rect, **wire_params):
        canvas = self.canvas

        assert self.layouter is not None

        if wire == canvas._active:
            if to_rect.right < from_rect.right:
                self.layouter.add_wire(
                    net=net, wire=wire, shape=_geo.Rect(
                        left=to_rect.right, bottom=to_rect.bottom,
                        right=from_rect.right, top=to_rect.top,
                    ), **wire_params,
                )

            left = from_rect.left
            right = from_rect.right
            try:
                minw = wire.min_width
            except:
                pass
            else:
                if (right - left) < minw:
                    left, right = (
                        0.5*(left + right - minw),
                        0.5*(left + right + minw),
                    )
            if from_rect.top < to_rect.bottom:
                self.layouter.add_wire(
                    net=net, wire=wire, shape=_geo.Rect(
                        left=left, bottom=from_rect.bottom,
                        right=right, top=to_rect.top,
                    ), **wire_params,
                )
            elif from_rect.bottom > to_rect.top:
                self.layouter.add_wire(
                    net=net, wire=wire, shape=_geo.Rect(
                        left=left, bottom=to_rect.bottom,
                        right=right, top=from_rect.top,
                    ), **wire_params,
                )
        else:
            left = to_rect.right - wire.min_width
            if left < from_rect.left:
                rect = _geo.Rect.from_rect(rect=from_rect, left=left)
                self.layouter.add_wire(
                    net=net, wire=wire, shape=rect, **wire_params,
                )
            else:
                rect = from_rect

            if from_rect.top < to_rect.bottom:
                self.layouter.add_wire(
                    net=net, wire=wire, shape=_geo.Rect.from_rect(
                        rect=rect, right=to_rect.right, top=to_rect.bottom,
                    ), **wire_params,
                )
            elif from_rect.bottom > to_rect.top:
                self.layouter.add_wire(
                    net=net, wire=wire, shape=_geo.Rect.from_rect(
                        rect=rect, bottom=to_rect.top, right=to_rect.right,
                    ), **wire_params,
                )

    def _connect_right(self, *, net, wire, from_rect, to_rect, **wire_params):
        canvas = self.canvas
        assert self.layouter is not None

        if wire == canvas._active:
            if from_rect.left < to_rect.left:
                self.layouter.add_wire(
                    net=net, wire=wire, shape=_geo.Rect(
                        left=from_rect.left, bottom=to_rect.bottom,
                        right=to_rect.left, top=to_rect.top,
                    ), **wire_params,
                )

            left = from_rect.left
            right = from_rect.right
            try:
                minw = wire.min_width
            except:
                pass
            else:
                if (right - left) < minw:
                    left, right = (
                        0.5*(left + right - minw),
                        0.5*(left + right + minw),
                    )
            if from_rect.top < to_rect.bottom:
                self.layouter.add_wire(
                    net=net, wire=wire, shape=_geo.Rect(
                        left=left, bottom=from_rect.bottom,
                        right=right, top=to_rect.top,
                    ), **wire_params,
                )
            elif from_rect.bottom > to_rect.top:
                self.layouter.add_wire(
                        net=net, wire=wire, shape=_geo.Rect(
                        left=left, bottom=to_rect.bottom,
                        right=right, top=from_rect.top,
                    ), **wire_params,
                )
        else:
            right = to_rect.left + wire.min_width
            if right > from_rect.right:
                rect = _geo.Rect.from_rect(rect=from_rect, right=right)
                self.layouter.add_wire(
                    net=net, wire=wire, shape=rect, **wire_params,
                )
            else:
                rect = from_rect

            if from_rect.top < to_rect.bottom:
                self.layouter.add_wire(
                    net=net, wire=wire, shape=_geo.Rect.from_rect(
                        rect=rect, left=to_rect.left, top=to_rect.bottom,
                    ), **wire_params,
                )
            elif from_rect.bottom > to_rect.top:
                self.layouter.add_wire(
                    net=net, wire=wire, shape=_geo.Rect.from_rect(
                        rect=rect, left=to_rect.left, bottom=to_rect.top,
                    ), **wire_params,
                )
