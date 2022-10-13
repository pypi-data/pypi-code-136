"""The native technology primitives"""
# SPDX-License-Identifier: GPL-2.0-or-later OR AGPL-3.0-or-later OR CERN-OHL-S-2.0+
from itertools import product, combinations, chain
import abc
from typing import (
    Any, Generator, Iterable, Optional, List, Set, Dict, Tuple, Union, cast,
)

from ..typing import OptMultiT, cast_OptMultiT, SingleOrMulti, OptSingleOrMulti, IntFloat
from .. import _util
from . import (
    rule as rle, property_ as prp, net as net_, mask as msk, wafer_ as wfr,
    edge as edg, technology_ as tch,
)


__all__ = ["Marker", "Auxiliary", "ExtraProcess",
           "Implant", "Well",
           "Insulator", "WaferWire", "GateWire", "MetalWire", "TopMetalWire",
           "Via", "PadOpening",
           "Resistor", "Diode",
           "MOSFETGate", "MOSFET", "Bipolar",
           "Spacing",
           "UnusedPrimitiveError", "UnconnectedPrimitiveError"]


class _Primitive(abc.ABC):
    @abc.abstractmethod
    def __init__(self, *, name: str):
        self.name = name

        self.ports = _PrimitivePorts()
        self.params = _Params()

        self._rules: Optional[Tuple[rle._Rule, ...]] = None

    def __repr__(self):
        cname = self.__class__.__name__.split(".")[-1]
        return f"{cname}(name={self.name})"

    def __eq__(self, other: object) -> bool:
        """Two primitives are the same if their name is the same"""
        return (isinstance(other, _Primitive)) and (self.name == other.name)

    def __hash__(self):
        return hash(self.name)

    @property
    def rules(self) -> Tuple[rle._Rule, ...]:
        if self._rules is None:
            raise AttributeError(
                "Internal error: accessing rules before they are generated",
            )
        return self._rules

    @abc.abstractmethod
    def _generate_rules(self, *,
        tech: tch.Technology,
    ) -> Iterable[rle._Rule]:
        return tuple()

    def _derive_rules(self, tech: tch.Technology) -> None:
        if self._rules is not None:
            raise ValueError(
                "Internal error: rules can only be generated once",
            )
        self._rules = tuple(self._generate_rules(tech=tech))

    @abc.abstractproperty
    def designmasks(self) -> Iterable[msk.DesignMask]:
        return tuple()

    def cast_params(self, params):
        casted = {}
        for param in self.params:
            try:
                default = param.default
            except AttributeError:
                try:
                    v = params.pop(param.name)
                except KeyError:
                    if param.allow_none:
                        v = None
                    else:
                        raise ValueError(
                            f"Missing required parameter '{param.name}' for"
                            f" primitive '{self.name}'"
                        )
            else:
                v = params.pop(param.name, default)
            casted[param.name] = param.cast(v)

        if len(self.ports) > 0:
            try:
                portnets = params.pop("portnets")
            except KeyError:
                # Specifying nets is optional
                pass
            else:
                # If nets are specified all nets need to be specified
                portnames = {p.name for p in self.ports}
                portnetnames = set(portnets.keys())
                if (
                    (portnames != portnetnames)
                    or (len(self.ports) != len(portnets)) # Detect removal of doubles in set
                ):
                    raise ValueError(
                        f"Nets for ports {portnetnames} specified but prim '{self.name}'"
                        f" has ports {portnames}"
                    )
                casted["portnets"] = portnets

        if len(params) > 0:
            raise TypeError(
                f"primitive '{self.name}' got unexpected parameter(s) "
                f"{tuple(params.keys())}"
            )

        return casted


class _Param(prp.Property):
    def __init__(self, *, primitive: _Primitive, name: str, allow_none=False, default=None):
        super().__init__(name, allow_none=allow_none)

        self._primitive = primitive

        if default is not None:
            try:
                default = self.cast(default)
            except TypeError:
                raise TypeError(
                    f"default can't be converted to type '{self.value_type_str}'"
                )
            self.default = default

    @property
    def primitive(self) -> _Primitive:
        return self._primitive

    def cast(self, value):
        if (value is None) and hasattr(self, "default"):
            return self.default
        else:
            return super().cast(value)

    def __eq__(self, other):
        equal = super().__eq__(other)
        if isinstance(equal, rle._Rule):
            return equal
        else:
            return (
                equal
                and isinstance(other, _Param)
                and (self.primitive == other.primitive)
            )


class _IntParam(_Param):
    value_conv = None
    value_type = int
    value_type_str = "int"


class _BoolParam(_Param):
    value_conv = None
    value_type = bool
    value_type_str = "bool"


class _PrimitiveParam(_Param):
    value_conv = None
    value_type = _Primitive
    value_type_str = "'_Primitive'"

    def __init__(self, *,
        primitive: _Primitive, name: str, allow_none=False, default=None, choices=None,
    ):
        if choices is not None:
            if not _util.is_iterable(choices):
                raise TypeError(
                    "choices has to be iterable of '_Primitive' objects"
                )
            choices = tuple(choices)
            if not all(isinstance(prim, _Primitive) for prim in choices):
                raise TypeError(
                    "choices has to be iterable of '_Primitive' objects"
                )
            self.choices = choices

        super().__init__(
            primitive=primitive, name=name, allow_none=allow_none, default=default,
        )

    def cast(self, value):
        value = super().cast(value)
        if hasattr(self, "choices"):
            if not ((value is None) or (value in self.choices)):
                raise ValueError(
                    f"Param '{self.name}' is not one of the allowed values:\n"
                    f"    {self.choices}"
            )

        return value


class _EnclosureParam(_Param):
    value_type_str = "'Enclosure'"

    def cast(self, value):
        if value is None:
            if hasattr(self, "default"):
                value = self.default
            elif not self.allow_none:
                raise TypeError(
                    f"'None' value not allowed for parameter '{self.name}'"
                )
        elif not (
            isinstance(value, prp.Enclosure)
            or (value in ("wide", "tall"))
        ):
            try:
                value = prp.Enclosure(value)
            except:
                raise TypeError(
                    f"value {repr(value)} can't be converted to an Enclosure object"
                )

        return value


class _EnclosuresParam(_Param):
    value_type_str = "iterable of 'Enclosure'"

    def __init__(self, *,
        primitive: _Primitive, name: str, allow_none=False, default=None, n: int,
    ):
        self.n = n
        super().__init__(
            primitive=primitive, name=name, allow_none=allow_none, default=default,
        )

    def cast(self, value):
        if value is None:
            if hasattr(self, "default"):
                value = self.default
            elif not self.allow_none:
                raise TypeError(
                    f"'None' value not allowed for parameter '{self.name}'"
                )
        elif not _util.is_iterable(value):
            try:
                value = self.n*(prp.Enclosure(value),)
            except:
                raise TypeError(
                    f"param '{self.name}' has to be an enclosure value or an iterable \n"
                    f"of type 'Enclosure' with length {self.n}"
                )
        else:
            try:
                value = tuple(
                    (None if elem is None
                     else elem if isinstance(elem, prp.Enclosure)
                     else prp.Enclosure(elem)
                    ) for elem in value
                )
            except:
                raise TypeError(
                    f"param '{self.name}' has to be an enclosure value or an iterable \n"
                    f"of type 'Enclosure' with length {self.n}"
                )
        return value


class _Params(_util.TypedListStrMapping[_Param]):
    @property
    def _elem_type_(self):
        return _Param


class _PrimitiveNet(net_.Net):
    def __init__(self, *, prim: _Primitive, name: str):
        super().__init__(name)
        self.prim = prim

    def __hash__(self):
        return hash((self.name, self.prim))

    def __eq__(self, other: object) -> bool:
        if type(other) is not _PrimitiveNet:
            return False
        else:
            return (self.name == other.name) and (self.prim == other.prim)

    def __repr__(self):
        return f"{self.prim.name}.{self.name}"


class _PrimitivePorts(
    _util.IterableOverride[Union[_PrimitiveNet, wfr.SubstrateNet]],
    net_.Nets,
):
    @property
    def _elem_type_(self):
        return (_PrimitiveNet, wfr.SubstrateNet)


class _MaskPrimitive(_Primitive):
    @abc.abstractmethod
    def __init__(self, *,
        name: Optional[str]=None, mask: msk._Mask, grid: Optional[IntFloat]=None,
        **primitive_args,
    ):
        if name is None:
            name = mask.name
        super().__init__(name=name, **primitive_args)

        self.mask = mask

        if grid is not None:
            grid = _util.i2f(grid)
        self.grid = grid

    @abc.abstractmethod
    def _generate_rules(self, *,
        tech: tch.Technology, gen_mask: bool=True,
    ) -> Generator[rle._Rule, None, None]:
        yield from super()._generate_rules(tech=tech)

        if gen_mask and isinstance(self.mask, rle._Rule):
            yield cast(rle._Rule, self.mask)
        if self.grid is not None:
            yield cast(msk.DesignMask, self.mask).grid == self.grid

    @property
    def designmasks(self):
        return self.mask.designmasks


class _DerivedPrimitive(_MaskPrimitive):
    """A primitive that is derived from other primitives and not a
    Primitive that can be part of the primitive list of a technology.
    """
    def _generate_rules(self, *, tech: tch.Technology) -> Tuple[rle._Rule, ...]:
        """As _DerivedPrimitive will not be added to the list of primitives
        of a technology node, it does not need to generate rules.
        """
        raise RuntimeError("Internal error") # pragma: no cover


class _DesignMaskPrimitive(_MaskPrimitive):
    @property
    @abc.abstractmethod
    def fill_space(self) -> str: # pragma: no cover
        raise RuntimeError("Unimplemented abstract property")

    @abc.abstractmethod
    def __init__(self, *, name: str, **super_args):
        if "mask" in super_args:
            raise TypeError(
                f"{self.__class__.__name__} got unexpected keyword argument 'mask'",
            )
        mask = msk.DesignMask(
            name=name, fill_space=self.fill_space,
        )
        super().__init__(name=name, mask=mask, **super_args)
        self.mask: msk.DesignMask


class _BlockageAttribute(_Primitive):
    """Mixin class for primitives with a blockage attribute"""
    def __init__(self, blockage: Optional["Marker"]=None, **super_args):
        self.blockage = blockage
        super().__init__(**super_args)


class _PinAttribute(_Primitive):
    """Mixin class for primitives with a pin attribute"""
    def __init__(self,
        pin: OptSingleOrMulti["Marker"].T=None,
        **super_args,
    ):
        if pin is not None:
            pin = _util.v2t(pin)
        self.pin = pin
        super().__init__(**super_args)
        if pin is not None:
            self.params += _PrimitiveParam(
                primitive=self, name="pin", allow_none=True, choices=self.pin,
            )


class _Intersect(_MaskPrimitive):
    """A primitive representing the overlap of a list of primitives"""
    def __init__(self, *, prims: Iterable[_MaskPrimitive]):
        prims2: Tuple[_MaskPrimitive, ...] = _util.v2t(prims)
        if len(prims2) < 2:
            raise ValueError(f"At least two prims needed for '{self.__class__.__name__}'")
        self.prims = prims2

        mask = msk.Intersect(p.mask for p in prims2)
        _MaskPrimitive.__init__(self, mask=mask)

    def _generate_rules(self, *,
        tech: tch.Technology,
    ) -> Generator[rle._Rule, None, None]:
        # This seems that it should not be called.
        # see also: https://gitlab.com/Chips4Makers/PDKMaster/-/issues/27
        return super()._generate_rules(tech=tech, gen_mask=False) # pragma: no cover


class Marker(_DesignMaskPrimitive):
    """The Marker primitive represents a layer used by other primitives for definition
    of these primitives; typically a recognition.
    It does not represent a processing layer and thus no physical mask is corresponding
    with this primitive.
    """
    @property
    def fill_space(self):
        return "yes"

    def __init__(self, **super_args):
        super().__init__(**super_args)

        self.params += (
            _Param(primitive=self, name="width", allow_none=True),
            _Param(primitive=self, name="height", allow_none=True),
        )

    def _generate_rules(self, *,
        tech: tch.Technology,
    ) -> Iterable[rle._Rule]:
        return super()._generate_rules(tech=tech)


class Auxiliary(_DesignMaskPrimitive):
    """The Auxiliary primitive represents a layer that is defined by a foundry's
    technology but not used in other PDKMaster primitives.
    """
    @property
    def fill_space(self):
        return "no"

    def __init__(self, **super_args):
        super().__init__(**super_args)

    def _generate_rules(self, *,
        tech: tch.Technology,
    ) -> Iterable[rle._Rule]:
        return super()._generate_rules(tech=tech)


SpaceTableRow = Tuple[
    Union[float, Tuple[float, float]],
    float,
]
class _WidthSpacePrimitive(_MaskPrimitive):
    """Common abstract base class for Primitives that have width and space property.
    Subclasses of this class will need to provide certain properties as parameters
    to the object `__init__()`

    Arguments:
        min_width: min width of drawn feature
        min_space: min space between drawn features
        space_table: optional width dependent spacing rules.
            it is an iterable of rows with each row of the form
            `width, space` or `(width, height), space`
        min_density, max_density: optional minimum or maximum denity specification
    """
    @abc.abstractmethod
    def __init__(self, *,
        min_width: IntFloat, min_space: IntFloat,
        space_table: Optional[Iterable[Iterable[float]]]=None,
        min_area: Optional[IntFloat]=None,
        min_density: Optional[float]=None, max_density: Optional[float]=None,
        **maskprimitive_args
    ):
        self.min_width = min_width = _util.i2f(min_width)
        self.min_space = min_space = _util.i2f(min_space)
        self.min_area = min_area = _util.i2f(min_area)
        self.min_density = min_density
        if (
            (min_density is not None)
            and ((min_density < 0.0) or (min_density > 1.0))
        ):
            raise ValueError("min_density has be between 0.0 and 1.0")
        self.max_density = max_density
        if (
            (max_density is not None)
            and ((max_density < 0.0) or (max_density > 1.0))
        ):
            raise ValueError("max_density has be between 0.0 and 1.0")

        if space_table is not None:
            table: List[SpaceTableRow] = []
            for row in space_table:
                values = _util.i2f_recursive(row)
                width, space = values
                if not (
                    isinstance(width, float)
                    or (
                        isinstance(width, tuple) and (len(width) == 2)
                        and all(isinstance(w, float) for w in width)
                    )
                ):
                    raise TypeError(
                        "first element in a space_table row has to be a float "
                        "or an iterable of two floats"
                    )

                table.append((
                    cast(Union[float, Tuple[float, float]], width),
                    space,
                ))
            self.space_table = tuple(table)
        else:
            self.space_table = None

        super().__init__(**maskprimitive_args)

        self.params += (
            _Param(primitive=self, name="width", default=self.min_width),
            _Param(primitive=self, name="height", default=self.min_width),
        )

    def _generate_rules(self, *,
        tech: tch.Technology,
    ) -> Generator[rle._Rule, None, None]:
        yield from super()._generate_rules(tech=tech)

        yield from (
            self.mask.width >= self.min_width,
            self.mask.space >= self.min_space,
        )
        if self.min_area is not None:
            yield self.mask.area >= self.min_area
        if self.min_density is not None:
            yield self.mask.density >= self.min_density
        if self.max_density is not None:
            yield self.mask.density <= self.max_density
        if self.space_table is not None:
            for row in self.space_table:
                w = row[0]
                if isinstance(w, float):
                    submask = self.mask.parts_with(
                        condition=self.mask.width >= w,
                    )
                else:
                    submask = self.mask.parts_with(condition=(
                        self.mask.width >= w[0],
                        self.mask.length >= w[1],
                    ))
                yield msk.Spacing(submask, self.mask) >= row[1]
        if isinstance(self, _PinAttribute) and self.pin is not None:
            yield from (
                msk.Connect(self.mask, pin.mask) for pin in self.pin
            )


class _WidthSpaceDesignMaskPrimitive(_DesignMaskPrimitive, _WidthSpacePrimitive):
    """_WidthSpacePrimitive that is also a _DesignMaskPrimitive
    """
    pass


class ExtraProcess(_WidthSpaceDesignMaskPrimitive):
    """ExtraProcess is a layer indicating an ExtraProcess step not handled
    by other primitives.

    For example non-silicidation for making active or poly resistors.
    """
    def __init__(self, *, fill_space: str, **super_args):
        if not fill_space in ("no", "yes"):
            raise ValueError("fill_space has to be either 'yes' or 'no'")
        self._fill_space = fill_space
        super().__init__(**super_args)

    @property
    def fill_space(self) -> str:
        return self._fill_space


class Implant(_WidthSpaceDesignMaskPrimitive):
    """Implant is a layer that represent an implantation step in the
    semiconductor processing.

    Arguments:
        type_: type of the implant; has to be "n", "p" or "adjust"
            an "adjust" layer is extra implant that can be used on
            both n-type and p-type regions.
        super_args: `_WidthSpacePrimitive` and `_DesignMaskPrimitive`
            arguments
    """
    @property
    def fill_space(self):
        return "yes"

    # Implants are supposed to be disjoint unless they are used as combined implant
    # MOSFET and other primitives
    def __init__(self, *, type_: str, **super_args):
        if type_ not in ("n", "p", "adjust"):
            raise ValueError("type_ has to be 'n', 'p' or adjust")
        self.type_ = type_

        super().__init__(**super_args)


class Insulator(_WidthSpaceDesignMaskPrimitive):
    """Insulator is a layer representing an insulator layer.

    Typical use is for thick oxide layer for higher voltage transistors.

    Arguments:
        fill_space: wether to allow fillinig regions that are violating
            minimum spacing; it can only be "yes" or "no"; "same_net"
            does not make sense for an insulator.
    """
    def __init__(self, *, fill_space: str, **super_args):
        if not fill_space in ("no", "yes"):
            raise ValueError("fill_space has to be either 'yes' or 'no'")
        self._fill_space = fill_space
        super().__init__(**super_args)

    @property
    def fill_space(self) -> str:
        return self._fill_space


class _Conductor(_BlockageAttribute, _PinAttribute, _DesignMaskPrimitive):
    """Primitive that acts as a conductor.

    This primitive is assumed to use a DesignMask as it's mask. And will
    allow a blockage and a pin layer.
    """
    @abc.abstractmethod
    def __init__(self, **super_args):
        super().__init__(**super_args)

        self.ports += _PrimitiveNet(prim=self, name="conn")

    def _generate_rules(self, *,
        tech: tch.Technology,
    ) -> Generator[rle._Rule, None, None]:
        yield from super()._generate_rules(tech=tech)

        # Generate a mask for connection, thus without resistor parts
        # or ActiveWire without gate etc.
        indicators = chain(*tuple(r.indicator for r in filter(
            lambda p: p.wire == self,
            tech.primitives.__iter_type__(Resistor),
        )))
        polys = tuple(g.poly for g in filter(
            lambda p: p.active == self,
            tech.primitives.__iter_type__(MOSFETGate)
        ))
        removes = {p.mask for p in chain(indicators, polys)}

        if removes:
            if len(removes) == 1:
                remmask = removes.pop()
            else:
                remmask = msk.Join(removes)
            self.conn_mask = self.mask.remove(remmask).alias(self.mask.name + "__conn")
            yield self.conn_mask
        else:
            self.conn_mask = self.mask


class _DesignMaskConductor(_Conductor, _DesignMaskPrimitive):
    """_DesignMaskPrimitive that is also a _Conductor"""
    pass
class _WidthSpaceConductor(_Conductor, _WidthSpacePrimitive):
    """_WidthSpacePrimitive that is also a _Conductor"""
    pass
class _WidthSpaceDesignMaskConductor(_WidthSpaceConductor, _DesignMaskPrimitive):
    """Combination of _DesignMaskConductor and _WidthSpaceConductor"""
    @property
    def fill_space(self):
        return "same_net"


class Well(_WidthSpaceDesignMaskConductor, Implant):
    """Well is an Implant layer that has deeper implant so it forms a
    well of a certain type.

    Typical application is for both NMOS and PMOS transistors on a wafer
    without shorting the source/drain regions to the bulk.

    Arguments:
        min_space_samenet: the smaller spacing between two wells on
            the same net.
    """
    # Wells are non-overlapping by design
    def __init__(self, *,
        min_space_samenet: Optional[IntFloat]=None, **super_args,
    ):
        super().__init__(**super_args)

        if min_space_samenet is not None:
            min_space_samenet = _util.i2f(min_space_samenet)
            if min_space_samenet >= self.min_space:
                raise ValueError("min_space_samenet has to be smaller than min_space")
        self.min_space_samenet = min_space_samenet

    def _generate_rules(self, *,
        tech: tch.Technology,
    ) -> Generator[rle._Rule, None, None]:
        yield from super()._generate_rules(tech=tech)

        if self.min_space_samenet is not None:
            yield self.mask.same_net.space >= self.min_space_samenet


class DeepWell(_WidthSpaceDesignMaskConductor, Implant):
    """The DeepWell primitive defines a well deeper into the substrate and normally
    used to connect a normal Well and in that way isolate some part of the wafer
    substrate. Most commonly this is the combination of the N-Well together with a
    depp N-Well to isolate the holes in the N-Well layer.

    Currently only low-level _Layout.add_shape() is supported for DeepWell, no
    support is present for combined Well + DeepWell layout generation.
    """
    def __init__(self, *,
        well: Well, type_: Optional[str]=None,
        min_well_overlap: float, min_well_enclosure: float,
        **super_args,
    ):
        if type_ is None:
            type_ = well.type_
        elif type_ != well.type_:
            raise ValueError(
                f"DeepWell type '{type_}' is different from type {well.type_} of Well"
                f" '{well.name}'"
            )
        super().__init__(type_=type_, **super_args)

        self.well = well
        self.min_well_overlap = min_well_overlap
        self.min_well_enclosure = min_well_enclosure

    def _generate_rules(self, *,
        tech: tch.Technology,
    ) -> Generator[rle._Rule, None, None]:
        yield from super()._generate_rules(tech=tech)

        yield (
            msk.Intersect((self.mask, self.well.mask)).width >= self.min_well_overlap
        )
        yield (
            self.well.mask.remove(self.mask).width >= self.min_well_enclosure
        )


class WaferWire(_WidthSpaceDesignMaskConductor):
    """WaferWire is representing the wire made from wafer material and normally
    isolated by LOCOS for old technlogies and STI (shallow-trench-isolation)
    or FINFET for newer/recent ones.
    The doping type is supposed the be determing by implant layers.

    Arguments:
        implant: the valid `Implant` layers for this primitive
        min_implant_enclosure: the minimum required enclosure by the implant
            over the waferwire. If a single enclosure is specified it is
            the spec for all the implants.
        implant_abut: wether to allow the abutment of two waferwire shapes
            of opposite type.
        allow_contactless_implant: wether to allow waferwire shapes without
            a contact. If True it is assumed that abutted shapes are on the same
            net.
        allow_in_substrate: wether to allow a waferwire shape that is not in a
            well. Some processes use wafers of a certain doping type; others
            need a well for all active devices.
        well: the well primitives valid for this WaferWire,
            It is assumed that WaferWire with implant type the same as the well
            connect to that well.
        min_well_enclosure: the minimum required enclosure of the WaferWire by
            the well. If only one value is given it is valid for all the wells.
        min_well_enclosure_same_type: allow to specify other enclosure for
            WaferWires with the same type as the well.
        min_substrate_enclosure: the minimum required enclosure of the WaferWire by
            the substrate with the substrate defined as any wafer region that is
            not covered by a well. If not specified the same value as
            min_well_enclosure is used.
        min_substrate_enclosure_same_type: allow to specify other enclosure for
            WaferWires with the same type as the well. If not specified the same value
            as min_well_enclosure_same_type is used.
        allow_well_crossing: wether it is allow for a WaferWire to go over a well
            boundary
        oxide: the list of valid oxide layers for this WaferWire. This can be empty.
        min_oxide_enclosure: the minimum required enclosure of the WaferWire by
            the oxide layer. If only one value is given it is valid for all the oxide
            layers.
        super_args: the argument for `_WidthSpacePrimitive` and `_DesignMaskPrimitive`
    """
    def __init__(self, *,
        implant: SingleOrMulti[Implant].T,
        min_implant_enclosure: SingleOrMulti[prp.Enclosure].T,
        implant_abut: Union[str, SingleOrMulti[Implant].T],
        allow_contactless_implant: bool,
        allow_in_substrate: bool,
        well: SingleOrMulti[Well].T,
        min_well_enclosure: SingleOrMulti[prp.Enclosure].T,
        min_well_enclosure_same_type: OptSingleOrMulti[Optional[prp.Enclosure]].T=None,
        min_substrate_enclosure: Optional[prp.Enclosure]=None,
        min_substrate_enclosure_same_type: Optional[prp.Enclosure]=None,
        allow_well_crossing: bool,
        oxide: OptSingleOrMulti[Insulator].T=None,
        min_oxide_enclosure: SingleOrMulti[Optional[prp.Enclosure]].T=None,
        **super_args
    ):
        self.allow_in_substrate = allow_in_substrate

        self.implant = implant = _util.v2t(implant)
        for impl in implant:
            if isinstance(impl, Well):
                raise TypeError(f"well '{impl.name}' may not be part of implant")
        self.min_implant_enclosure = min_implant_enclosure = _util.v2t(
            min_implant_enclosure, n=len(implant),
        )
        if isinstance(implant_abut, str):
            _conv: Dict[str, Tuple[Implant, ...]] = {
                "all": implant, "none": tuple()
            }
            if implant_abut not in _conv:
                raise ValueError(
                    "only 'all' or 'none' allowed for a string implant_abut"
                )
            implant_abut = _conv[implant_abut]
        else:
            implant_abut = _util.v2t(implant_abut)
        for impl in implant_abut:
            if impl not in implant:
                raise ValueError(
                    f"implant_abut member '{impl.name}' not in implant list"
                )
        self.implant_abut = implant_abut
        self.allow_contactless_implant = allow_contactless_implant

        self.well = well = _util.v2t(well)
        for w in well:
            if not any(impl.type_ == w.type_ for impl in implant):
                raise UnconnectedPrimitiveError(well[0])
        self.min_well_enclosure = min_well_enclosure = _util.v2t(
            min_well_enclosure, n=len(well),
        )
        if min_well_enclosure_same_type is None:
            self.min_well_enclosure_same_type = None
        else:
            self.min_well_enclosure_same_type = cast(
                Tuple[Optional[prp.Enclosure], ...],
                _util.v2t(min_well_enclosure_same_type, n=len(well)),
            )
        if allow_in_substrate:
            if min_substrate_enclosure is None:
                if len(min_well_enclosure) == 1:
                    min_substrate_enclosure = min_well_enclosure[0]
                    if min_substrate_enclosure_same_type is not None:
                        raise TypeError(
                            "min_substrate_enclosure_same_type has to be 'None' "
                            "if min_substrate_enclosure is 'None'"
                        )
                    if self.min_well_enclosure_same_type is not None:
                        min_substrate_enclosure_same_type = \
                            self.min_well_enclosure_same_type[0]
                else:
                    raise TypeError(
                        "min_substrate_enclosure has be provided when providing "
                        "multiple wells"
                    )
        elif min_substrate_enclosure is not None:
            raise TypeError(
                "min_substrate_enclosure has to be 'None' if allow_in_substrate "
                "is 'False'"
            )
        self.allow_well_crossing = allow_well_crossing
        self.min_substrate_enclosure = min_substrate_enclosure
        self.min_substrate_enclosure_same_type = min_substrate_enclosure_same_type

        if oxide is not None:
            oxide = _util.v2t(oxide)
            min_oxide_enclosure = _util.v2t(min_oxide_enclosure, n=len(oxide))
        elif min_oxide_enclosure is not None:
            raise ValueError("min_oxide_enclosure provided with no oxide given")
        self.oxide = oxide
        self.min_oxide_enclosure = min_oxide_enclosure

        super().__init__(**super_args)

        if len(implant) > 1:
            self.params += (
                _PrimitiveParam(primitive=self, name="implant", choices=self.implant),
                _EnclosureParam(primitive=self, name="implant_enclosure", allow_none=True),
            )
        else:
            self.params += (
                _EnclosureParam(
                    primitive=self, name="implant_enclosure",
                    default=min_implant_enclosure[0],
                ),
            )
        if (len(well) > 1) or allow_in_substrate:
            self.params += (
                _PrimitiveParam(
                    primitive=self, name="well", allow_none=allow_in_substrate,
                    choices=self.well
                ),
                _EnclosureParam(primitive=self, name="well_enclosure", allow_none=True),
            )
        else:
            self.params += (
                _EnclosureParam(
                    primitive=self, name="well_enclosure", default=min_well_enclosure[0],
                ),
            )
        if self.oxide is not None:
            self.params += (
                _PrimitiveParam(primitive=self, name="oxide", choices=self.oxide, allow_none=True),
                _EnclosureParam(primitive=self, name="oxide_enclosure", allow_none=True),
            )

    def cast_params(self, params):
        well_net = params.pop("well_net", None)
        params = super().cast_params(params)

        if "implant" in params:
            implant = params["implant"]
        else:
            params["implant"] = implant = self.implant[0]
        if params["implant_enclosure"] is None:
            idx = self.implant.index(implant)
            params["implant_enclosure"] = self.min_implant_enclosure[idx]

        if "well" in params:
            well = params["well"]
            if (well is not None) and (params["well_enclosure"] is None):
                idx = self.well.index(well)
                params["well_enclosure"] = self.min_well_enclosure[idx]
        else:
            # well parameter will always be there except when next condition
            # is met.
            assert (
                (len(self.well) == 1) and (not self.allow_in_substrate)
            ), "Internal error"
            params["well"] = well = self.well[0]
        if well is not None:
            if well_net is None:
                raise TypeError(
                    f"No well net specified for primitive '{self.name}' in a well"
                )
            params["well_net"] = well_net
        elif well_net is not None:
            raise TypeError(
                f"Well net specified for primitive '{self.name}' not in a well"
            )

        if ("oxide" in params):
            oxide = params["oxide"]
            if oxide is not None:
                assert self.oxide is not None
                assert self.min_oxide_enclosure is not None
                oxide_enclosure = params["oxide_enclosure"]
                if oxide_enclosure is None:
                    idx = self.oxide.index(oxide)
                    params["oxide_enclosure"] = self.min_oxide_enclosure[idx]

        return params

    def _generate_rules(self, *,
        tech: tch.Technology,
    ) -> Generator[rle._Rule, None, None]:
        yield from super()._generate_rules(tech=tech)

        for i, impl in enumerate(self.implant):
            sd_mask_impl = msk.Intersect((self.conn_mask, impl.mask)).alias(
                f"{self.conn_mask.name}:{impl.name}",
            )
            yield from (sd_mask_impl, msk.Connect(self.conn_mask, sd_mask_impl))
            if self.allow_in_substrate and (impl.type_ == tech.substrate_type):
                yield msk.Connect(sd_mask_impl, tech.substrate)
            if impl not in self.implant_abut:
                yield edg.MaskEdge(impl.mask).interact_with(self.mask).length == 0
            enc = self.min_implant_enclosure[i]
            yield self.mask.enclosed_by(impl.mask) >= enc
            for w in self.well:
                if impl.type_ == w.type_:
                    yield msk.Connect(sd_mask_impl, w.mask)
        for implduo in combinations((impl.mask for impl in self.implant_abut), 2):
            yield msk.Intersect(implduo).area == 0
        # TODO: allow_contactless_implant

        for i, w in enumerate(self.well):
            enc = self.min_well_enclosure[i]
            if enc.is_assymetric: # pragma: no cover
                raise NotImplementedError(
                    f"Asymmetric enclosure of WaferWire '{self.name}' "
                    f"by well '{w.name}'",
                )
            if self.min_well_enclosure_same_type is None:
                yield self.mask.enclosed_by(w.mask) >= enc
            else:
                enc2 = self.min_well_enclosure_same_type[i]
                if enc2 is None:
                    yield self.mask.enclosed_by(w.mask) >= enc
                else:
                    if enc2.is_assymetric: # pragma: no cover
                        raise NotImplementedError(
                            f"Asymmetric same type enclosure of WaferWire '{self.name}"
                            f"by well '{w.name}",
                        )
                    for ww in (
                        cast("_WaferWireIntersect", self.in_(impl))
                        for impl in filter(
                            # other type
                            lambda impl2: w.type_ != impl2.type_, self.implant,
                        )
                    ):
                        yield ww.mask.enclosed_by(w.mask) >= enc
                    for ww in (
                        cast("_WaferWireIntersect", self.in_(impl))
                        for impl in filter(
                            # same type
                            lambda impl2: w.type_ == impl2.type_, self.implant,
                        )
                    ):
                        yield ww.mask.enclosed_by(w.mask) >= enc2

        if self.min_substrate_enclosure is not None:
            if self.min_substrate_enclosure_same_type is None:
                yield (
                    self.mask.enclosed_by(tech.substrate)
                    >= self.min_substrate_enclosure
                )
            else:
                for ww in (
                    cast("_WaferWireIntersect", self.in_(impl)) for impl in filter(
                    # other type
                    lambda impl2: tech.substrate_type != impl2.type_, self.implant,
                )):
                    yield (
                        ww.mask.enclosed_by(tech.substrate)
                        >= self.min_substrate_enclosure
                    )
                for ww in (
                    cast("_WaferWireIntersect", self.in_(impl)) for impl in filter(
                    # same type
                    lambda impl2: tech.substrate_type == impl2.type_, self.implant,
                )):
                    yield (
                        ww.mask.enclosed_by(tech.substrate)
                        >= self.min_substrate_enclosure_same_type
                    )

        if self.oxide is not None:
            assert self.min_oxide_enclosure is not None
            for i, ox in enumerate(self.oxide):
                enc = self.min_oxide_enclosure[i]
                if enc is not None:
                    yield self.mask.enclosed_by(ox.mask) >= enc

        if not self.allow_well_crossing:
            mask_edge = edg.MaskEdge(self.mask)
            yield from (
                mask_edge.interact_with(edg.MaskEdge(w.mask)).length == 0
                for w in self.well
            )

    def in_(self, prim: SingleOrMulti[_MaskPrimitive].T) -> "_DerivedPrimitive":
        return _WaferWireIntersect(waferwire=self, prim=prim)


class _WaferWireIntersect(_DerivedPrimitive, _Intersect):
    """Intersect of WaferWire with one or more of it's implants, wells and
    oxides"""
    def __init__(self, *,
        waferwire: WaferWire, prim: SingleOrMulti[_MaskPrimitive].T,
    ):
        ww_prims: Set[_MaskPrimitive] = set(waferwire.implant)
        if waferwire.well is not None:
            ww_prims.update(waferwire.well)
        if waferwire.oxide is not None:
            ww_prims.update(waferwire.oxide)
        prim = _util.v2t(prim)
        for p in prim:
            if p not in ww_prims:
                raise ValueError(
                    f"prim '{p.name}' not an implant, well or oxide layer for"
                    f" WaferWire '{waferwire.name}'"
                )
        self.waferwire = waferwire
        self.prim = prim

        super().__init__(prims=(waferwire, *prim))


class GateWire(_WidthSpaceDesignMaskConductor):
    """GateWire is a _WidthSpaceDesignMaskConductor that can act as the
    gate of a MOSFET.

    No extra arguments next to the `_WidthSpacePrimitive` and `_DesignMaskPrimitive`
    ones.
    """
    def __init__(self, **super_args):
        super().__init__(**super_args)


class MetalWire(_WidthSpaceDesignMaskConductor):
    """GateWire is a _WidthSpaceDesignMaskConductor that acts as an
    interconnect layer.

    No extra arguments next to the `_WidthSpacePrimitive` and `_DesignMaskPrimitive`
    ones.
    """
    def __init__(self, **super_args):
        super().__init__(**super_args)


class MIMTop(MetalWire):
    """MIMTop is a primitive to be used as the top of a MIM Capacitor
    """
    pass
class TopMetalWire(MetalWire):
    """TopMetalWire is a primitive for top metal layer. A top metal layer
    does not have to appear in the bottom list of a `Via`.
    """
    pass


ViaBottom = Union[WaferWire, GateWire, MetalWire, "Resistor"]
ViaTop = Union[MetalWire, "Resistor"]
class Via(_DesignMaskConductor):
    """A Via layer is a layer that connect two conductor layer vertically.

    Arguments:
        width: the fixed width; only squares with this width are allowed
            on the Via layer.
        bottom: list of valid bottom primitives for this Via layer.
            These have to be `WaferWire`, `GateWire`, `MetalWire` or `Resistor`
            objects
        min_bottom_enclosure: the minimum required enclosure of the Via by
            the bottom layer. If only one value is given it is valid for all the
            bottom layers.
        top: list of valid bottom primitives for this Via layer.
            These have to be `WaferWire`, `GateWire`, `MetalWire` or `Resistor`
            objects
        min_bottom_enclosure: the minimum required enclosure of the Via by
            the top layer. If only one value is given it is valid for all the
            top layers.
        super_args: parameters for `_DesignMaskPrimitive`
    """
    @property
    def fill_space(self):
        return "no"

    # When drawing via and bottom or top is not specified by default the first layer
    # will be used if it is a MetalWire, otherwise it needs to be specified.
    def __init__(self, *,
        width: IntFloat, min_space: IntFloat,
        bottom: SingleOrMulti[ViaBottom].T, top: SingleOrMulti[ViaTop].T,
        min_bottom_enclosure: SingleOrMulti[prp.Enclosure].T,
        min_top_enclosure: SingleOrMulti[prp.Enclosure].T,
        **super_args,
    ):
        super().__init__(**super_args)

        self.bottom = bottom = _util.v2t(bottom)
        self.min_bottom_enclosure = min_bottom_enclosure = _util.v2t(min_bottom_enclosure, n=len(bottom))
        for b in bottom:
            if isinstance(b, TopMetalWire):
                raise TypeError(
                    f"TopMetalWire '{b.name} not allowed as bottom of Via '{self.name}'",
                )
        self.top = top = _util.v2t(top)
        self.min_top_enclosure = min_top_enclosure = _util.v2t(
            min_top_enclosure, n=len(top),
        )
        self.width = width = _util.i2f(width)
        self.min_space = min_space = _util.i2f(min_space)

        self.params += (
            _Param(primitive=self, name="space", default=min_space),
            _IntParam(primitive=self, name="rows", allow_none=True),
            _IntParam(primitive=self, name="columns", allow_none=True),
            _EnclosureParam(primitive=self, name="bottom_enclosure", allow_none=True),
            _Param(primitive=self, name="bottom_width", allow_none=True),
            _Param(primitive=self, name="bottom_height", allow_none=True),
            _EnclosureParam(primitive=self, name="top_enclosure", allow_none=True),
            _Param(primitive=self, name="top_width", allow_none=True),
            _Param(primitive=self, name="top_height", allow_none=True),
        )
        if len(bottom) > 1:
            default = bottom[0]
            if not isinstance(default, MetalWire) or isinstance(default, MIMTop):
                default = None
            self.params += _PrimitiveParam(
                primitive=self, name="bottom", default=default, choices=bottom,
            )
        choices = sum(
            (cast(WaferWire, wire).implant for wire in filter(
                lambda w: isinstance(w, WaferWire),
                bottom,
            )),
            tuple(),
        )
        if choices:
            self.params += (
                _PrimitiveParam(
                    primitive=self, name="bottom_implant",
                    allow_none=True, choices=choices,
                ),
                _EnclosureParam(
                    primitive=self, name="bottom_implant_enclosure", allow_none=True,
                ),
                _PrimitiveParam(primitive=self, name="bottom_well", allow_none=True),
                _EnclosureParam(
                    primitive=self, name="bottom_well_enclosure", allow_none=True,
                ),
            )
        choices = sum(
            (cast(Tuple[Insulator, ...], cast(WaferWire, wire).oxide)
            for wire in filter(
                lambda w: isinstance(w, WaferWire) and (w.oxide is not None),
                bottom,
            )),
            tuple(),
        )
        if choices:
            self.params += (
                _PrimitiveParam(
                    primitive=self, name="bottom_oxide", allow_none=True, choices=choices,
                ),
                _EnclosureParam(
                    primitive=self, name="bottom_oxide_enclosure", allow_none=True,
                ),
            )
        if len(top) > 1:
            default = top[0]
            assert isinstance(default, MetalWire), "Not implemented"
            self.params += _PrimitiveParam(
                primitive=self, name="top", default=default, choices=top,
            )

    def cast_params(self, params):
        well_net = params.pop("well_net", None)
        params = super().cast_params(params)

        def _check_param(name):
            return (name in params) and (params[name] is not None)

        has_bottom = _check_param("bottom")
        # has_bottom_enclosure = _check_param("bottom_enclosure")
        has_bottom_implant = _check_param("bottom_implant")
        has_bottom_implant_enclosure = _check_param("bottom_implant_enclosure")
        has_bottom_well = _check_param("bottom_well")
        has_bottom_well_enclosure = _check_param("bottom_well_enclosure")
        has_bottom_width = _check_param("bottom_width")
        has_bottom_height = _check_param("bottom_height")

        has_top = _check_param("top")

        has_rows = _check_param("rows")
        has_columns = _check_param("columns")
        has_top_width = _check_param("top_width")
        has_top_height = _check_param("top_height")

        if has_bottom:
            bottom = params["bottom"]
        else:
            bottom = params["bottom"] = self.bottom[0]
        if isinstance(bottom, WaferWire):
            impl = params["bottom_implant"]
            if impl is None:
                raise ValueError(
                    "bottom_implant parameter not provided for use of\n"
                    f"bottom '{bottom.name}' for via '{self.name}'"
                )

            if not has_bottom_implant_enclosure:
                idx = bottom.implant.index(impl)
                params["bottom_implant_enclosure"] = bottom.min_implant_enclosure[idx]

            if has_bottom_well:
                bottom_well = params["bottom_well"]
                if bottom_well not in bottom.well:
                    raise ValueError(
                        f"bottom_well '{bottom_well.name}' not a valid well for "
                        f"bottom wire '{bottom.name}'"
                    )
                if not has_bottom_well_enclosure:
                    idx = bottom.well.index(bottom_well)
                    params["bottom_well_enclosure"] = (
                        bottom.min_well_enclosure[idx]
                    )
                params["well_net"] = well_net
            elif not bottom.allow_in_substrate:
                raise ValueError(
                    f"bottom wire '{bottom.name}' needs a well"
                )
        elif has_bottom_implant:
            bottom_implant = params["bottom_implant"]
            raise TypeError(
                f"bottom_implant '{bottom_implant.name}' not a valid implant for "
                f"bottom wire '{bottom.name}'"
            )
        elif has_bottom_implant_enclosure:
            raise TypeError(
                "bottom_implant_enclosure wrongly provided for bottom wire "
                f"'{bottom.name}'"
            )
        elif has_bottom_well:
            bottom_well = params["bottom_well"]
            raise TypeError(
                f"bottom_well '{bottom_well.name}' not a valid well for "
                f"bottom wire '{bottom.name}'"
            )
        elif has_bottom_well_enclosure:
            raise TypeError(
                "bottom_well_enclosure wrongly provided for bottom wire "
                f"'{bottom.name}'"
            )

        if has_top:
            top = params["top"]
        else:
            top = params["top"] = self.top[0]

        if not any((has_rows, has_bottom_height, has_top_height)):
            params["rows"] = 1

        if not any((has_columns, has_bottom_width, has_top_width)):
            params["columns"] = 1

        return params

    def _generate_rules(self, *,
        tech: tch.Technology,
    ) -> Generator[rle._Rule, None, None]:
        yield from super()._generate_rules(tech=tech)

        yield from (
            self.mask.width == self.width,
            self.mask.space >= self.min_space,
            msk.Connect((b.conn_mask for b in self.bottom), self.mask),
            msk.Connect(self.mask, (b.conn_mask for b in self.top)),
        )
        for i in range(len(self.bottom)):
            bot_mask = self.bottom[i].mask
            enc = self.min_bottom_enclosure[i]
            yield self.mask.enclosed_by(bot_mask) >= enc
        for i in range(len(self.top)):
            top_mask = self.top[i].mask
            enc = self.min_top_enclosure[i]
            yield self.mask.enclosed_by(top_mask) >= enc

    @property
    def designmasks(self):
        yield from super().designmasks
        for conn in self.bottom + self.top:
            yield from conn.designmasks

    def in_(self, prim: SingleOrMulti[_MaskPrimitive].T) -> _DerivedPrimitive:
        return _ViaIntersect(via=self, prim=prim)


class _ViaIntersect(_DerivedPrimitive, _Intersect):
    """Intersect of WaferWire with one or more of it's implants, wells and
    oxides"""
    def __init__(self, *,
        via: Via, prim: SingleOrMulti[_MaskPrimitive].T,
    ):
        via_prims: Set[_MaskPrimitive] = {*via.bottom, *via.top}
        prim = _util.v2t(prim)
        for p in prim:
            if isinstance(p, _WaferWireIntersect):
                p = p.waferwire
            if p not in via_prims:
                raise ValueError(
                    f"prim '{p.name}' not a bottom or top layer for Via '{via.name}'"
                )
        self.via = via
        self.prin = prim

        super().__init__(prims=(via, *prim))


class PadOpening(_WidthSpaceDesignMaskConductor):
    """PadOpening is a layer representing an opening in the top layer in the
    processing of a semiconductor wafer.

    Typical application is for wirebonding, bumping for flip-chip or an RDL
    (redistribution) layer.

    Arguments:
        bottom: the MetalWire layer for which on top of which an opening in
            the isolation is made.
        min_bottom_enclsoure: the minimum enclosure of the `PadOpening` layer
            by the bottom layer.
        super_args: arguments for `WidthSpacePrimitive` and `_DesignMaskPrimitive`
    """
    @property
    def fill_space(self):
        return "no"

    def __init__(self, *,
        bottom: MetalWire, min_bottom_enclosure: prp.Enclosure, **super_args,
    ):
        super().__init__(**super_args)

        if isinstance(bottom, TopMetalWire):
            raise TypeError(
                f"TopMetalWire '{bottom.name}' not allowed for PadOpening '{self.name}'",
            )
        self.bottom = bottom
        self.min_bottom_enclosure = min_bottom_enclosure

    def _generate_rules(self, *,
        tech: tch.Technology,
    ) -> Generator[rle._Rule, None, None]:
        yield from super()._generate_rules(tech=tech)

        yield (
            self.mask.enclosed_by(self.bottom.mask)
            >= self.min_bottom_enclosure
        )

    @property
    def designmasks(self):
        yield from super().designmasks
        yield from self.bottom.designmasks


ResistorWire = Union[WaferWire, GateWire, MetalWire]
ResistorIndicator = Union[Marker, ExtraProcess]
class Resistor(_WidthSpacePrimitive):
    """Resistor is a primitive that represent a resistor device.
    The resistor itself is not drawn by defined by the overlap
    of other drawn layers.

    Attributes:
        mask: the resulting mask with the shape of the mask. It is
            the overlapping part of the base wire with all the
            indicators
    Arguments:
        wire: the base wire used to make a resistor device.
            It has to be a `WaferWire`, a `Gatewire` or a `MetalWire`
        contact: optional Via layer used to connect the base wire.
        min_contact_space: the minimum of the contact to the overlap
            of the base wire and all the indicator layers.
        indicator: list of indicator layers for the Resistor. Only the
            overlapping area of all the indicator layers will be seen as
            the Resistor device.
            For am indicator of type ExtraProcess it is assumed that this
            extra process does influence the resulting resistance as with
            a Marker type it does not and is thus just a recognition layer.
        min_indicator_extension: minimum required extension of the indicator
            shapes over the base wire. If only one value is given it will
            be used for all the indicators.
        implant: optional implant layer for the resistor. This allows to
            have different sheet resistance and models for wire with
            different implants. If wire is a WaferWire the implant
            layer has to be a valid implant for that waferwire.
        model: spice model name of the Resistor; the width and height of
            the overlapping area are used as parameters.
        subckt_params: Conversion of width and height parameter to the name
            used by the model. It is thus a dict with keys "width" and "height"
            and the value for each the actual spice model parameter name.
            By default "width" is translated to "w" and "height to "l".
        sheetres: the optional sheet resistance value.
            If both sheetres and model are given, sheetres will be used for LVS
            and model for generating extracted netlist meant for simulation.
    """
    def __init__(self, *, name: str,
        wire: ResistorWire,
        contact: Optional[Via], min_contact_space: Optional[IntFloat]=None,
        indicator: SingleOrMulti[ResistorIndicator].T,
        min_indicator_extension: SingleOrMulti[IntFloat].T,
        implant: Optional[Implant]=None,
        min_implant_enclosure: Optional[prp.Enclosure]=None,
        model: Optional[str]=None, subckt_params: Optional[Dict[str, str]]=None,
        sheetres: Optional[IntFloat]=None, **widthspace_args,
    ):
        # If both model and sheetres are specified, sheetres will be used for
        # LVS circuit generation in pyspice export.
        self.wire = wire

        if "grid" in widthspace_args:
            raise TypeError("Resistor got an unexpected keyword argument 'grid'")

        if "min_width" in widthspace_args:
            if widthspace_args["min_width"] < wire.min_width:
                raise ValueError("min_width may not be smaller than base wire min_width")
        else:
            widthspace_args["min_width"] = wire.min_width

        if "min_space" in widthspace_args:
            if widthspace_args["min_space"] < wire.min_space:
                raise ValueError("min_space may not be smaller than base wire min_space")
        else:
            widthspace_args["min_space"] = wire.min_space

        self.indicator = indicator = _util.v2t(indicator)
        self.min_indicator_extension = min_indicator_extension = _util.v2t(
            _util.i2f_recursive(min_indicator_extension), n=len(indicator),
        )

        if implant is not None:
            if isinstance(implant, Well):
                raise TypeError(
                    f"Resistor implant may not be Well '{implant.name}'",
                )
            if isinstance(wire, WaferWire):
                if implant not in wire.implant:
                    raise ValueError(
                        f"implant '{implant.name}' is not valid for waferwire '{wire.name}'"
                    )
            elif not isinstance(wire, GateWire):
                raise ValueError(
                    f"Resistor {name}: "
                    "implant may only be provided for a wire of type "
                    "'WaferWire' or 'GateWire'"
                )
        elif min_implant_enclosure is not None:
            raise TypeError(
                "min_implant_enclosure has to be 'None' if no implant is given"
            )
        self.implant = implant
        self.min_implant_enclosure = min_implant_enclosure

        prims = (wire, *indicator)
        if implant:
            prims += (implant,)
        mask = msk.Intersect(prim.mask for prim in prims).alias(f"resistor:{name}")

        super().__init__(name=name, mask=mask, **widthspace_args)

        self.ports += (
            _PrimitiveNet(prim=self, name=name)
            for name in ("port1", "port2")
        )

        if contact is not None:
            if wire not in (contact.bottom + contact.top):
                raise ValueError(
                    f"wire {wire.name} does not connect to via {contact.name}"
                )
            if min_contact_space is None:
                raise TypeError(
                    "min_contact_space not given when contact is given"
                )
        elif min_contact_space is not None:
            raise TypeError(
                "min_contact_space has to be 'None' if no contact layer is given"
            )
        self.contact = contact
        self.min_contact_space = min_contact_space

        if (model is None) and (sheetres is None):
            raise TypeError(
                "Either model or sheetres have to be specified"
            )

        if model is not None:
            if subckt_params is not None:
                if set(subckt_params.keys()) != {"width", "height"}:
                    raise ValueError(
                        "subckt_params has to be None or a dict with keys ('width', 'height')"
                    )
        elif subckt_params is not None:
            raise TypeError("subckt_params provided without a model")
        self.model = model
        self.subckt_params = subckt_params

        sheetres = _util.i2f(sheetres)
        self.sheetres = sheetres

    def _generate_rules(self, *,
        tech: tch.Technology,
    ) -> Generator[rle._Rule, None, None]:
        # Do not generate the default width/space rules.
        yield from _Primitive._generate_rules(self, tech=tech)

        # TODO: Can we provide proper type for self.mask ?
        yield cast(msk.DesignMask, self.mask)
        self.conn_mask = msk.Intersect((self.mask, *(p.mask for p in self.indicator)))
        if self.min_width > self.wire.min_width:
            yield self.mask.width >= self.min_width
        if self.min_space > self.wire.min_space:
            yield self.mask.space >= self.min_space
        if self.min_area is not None:
            if (self.wire.min_area is None) or (self.min_area > self.wire.min_area):
                yield self.mask.area >= self.min_area
        for i, ind in enumerate(self.indicator):
            ext = self.min_indicator_extension[i]
            mask = self.wire.mask.remove(ind.mask)
            yield mask.width >= ext


class Capacitor(_WidthSpacePrimitive):
    """This is a abstract base class for all capacitor types.
    It needs to be subclassed.
    """
    pass


class MIMCapacitor(Capacitor):
    """`MIMCapactor` represents the so-called Metal-Insulator-Metal
    type of capacitor.
    Currently it specifically tackles the MIM capacitor made with
    a dieletric on top of a MetalWire with on top of that an
    intermediate metal layer.

    Arguments:
        name: the name of the MIMCapacitor
        bottom: the bottom layer of the MIM capacitor
        top: the top layer of the MIM capacitor
        via: the Via layer contacting both the bottom and top layer
            of the MIM capacitor
        min_bottom_top_enclosure: min required enclosure of the top
            layer by the bottom layer
        min_bottomvia_top_space: min space from a via contacting the bottom
            layer to the top layers
        min_top_via_enclosure: min enclosure of a via contacting the top
            layer by the top layer.
        min_bottom_space: minimum space from a shape that is used as the
            bottom of a MIM capacitor to any other shape on the bottom
            MetalWire layer.
        min_top2bottom_space: minimum space from the top layer to any shape
            on the bottom MetalWire that is not the bottom plate of the
            same capacitor.
        model: the spice model name for the capacitor
        subckt_params: Conversion of width and height parameter to the name
            used by the model. It is thus a dict with keys "width" and "height"
            and the value for each the actual spice model parameter name.
            By default "width" is translated to "w" and "height to "l".
    """
    def __init__(self, *, name: str,
        bottom: MetalWire, top: MIMTop, via: Via,
        min_bottom_top_enclosure: prp.Enclosure, min_bottomvia_top_space: IntFloat,
        min_top_via_enclosure: prp.Enclosure,
        min_bottom_space: Optional[IntFloat], min_top2bottom_space: Optional[IntFloat],
        model: str, subckt_params: Optional[Dict[str, str]]=None,
        **widthspace_args,
    ):
        if not bottom in via.bottom:
            raise ValueError(
                f"MIMCapacitor '{name}':"
                f" bottom '{bottom.name}' is not a bottom layer for via '{via.name}'"
            )
        if not top in via.bottom:
            raise ValueError(
                f"MIMCapacitor '{name}':"
                f" top '{top.name}' is not a bottom layer for via '{via.name}'"
            )

        if "min_width" in widthspace_args:
            if widthspace_args["min_width"] < top.min_width:
                raise ValueError("min_width may not be smaller than top wire min_width")
        else:
            widthspace_args["min_width"] = top.min_width

        if "min_space" in widthspace_args:
            if widthspace_args["min_space"] < top.min_space:
                raise ValueError("min_space may not be smaller than top wire min_space")
        else:
            widthspace_args["min_space"] = top.min_space

        self.bottom = bottom
        self.top = top
        self.via = via

        self.min_bottom_top_enclosure = min_bottom_top_enclosure
        self.min_bottomvia_top_space = min_bottomvia_top_space
        self.min_top_via_enclosure = min_top_via_enclosure
        self.min_bottom_space = min_bottom_space
        self.min_top2bottom_space = min_top2bottom_space

        mask = top.mask.alias(f"mimcap:{name}")

        super().__init__(name=name, mask=mask, **widthspace_args)

        self.params += (
            _BoolParam(primitive=self, name="bottom_connect_up", default=True),
        )

        self.ports += (
            _PrimitiveNet(prim=self, name=name)
            for name in ("bottom", "top")
        )

        if subckt_params is not None:
            if set(subckt_params.keys()) != {"width", "height"}:
                raise ValueError(
                    "subckt_params has to be None or a dict with keys ('width', 'height')"
                )
        self.model = model
        self.subckt_params = subckt_params

    def _generate_rules(self, *,
        tech: tch.Technology,
    ) -> Generator[rle._Rule, None, None]:
        yield from super()._generate_rules(tech=tech)

        # TODO: MIMCapacitor rules


DiodeIndicator = Union[Marker, ExtraProcess]
class Diode(_WidthSpacePrimitive):
    """`Diode` represent a diode device made up of a WaferWire object.
    A diode device needs a pn-junction which does need to be achieved by
    implants.

    Arguments:
        name: optional name for the diode; otherwise a unique name starting
            with "diode:" will be generated.
        wire: the base layer for the diode
        indicator: list of indicator layers for the Diode. Only the
            overlapping area of all the indicator layers will be seen as
            the Resistor device.
            Both ExtraProcess and Marker are valid indicator layers.
        min_indicator_extension: minimum required enclosure of the base wire
            by the indicator. If only one value is given it will
            be used for all the indicators.
        implant: the implant layer of the WaferWire forming the diode.
            The implant layer has to be a valid implant layer for the
            base WaferWire primitive.
        min_implant_enclosure: the optional minimum required enclosure
            of the base wire by the implant. If not provided the one specified
            for the base wire will be used as default.
        well: optional well to place the diode in. This well has to be of
            opposite type of the implant layer. If no well is specified
            the diode is in the substrate. So then the base wire must be
            allowed to be placed in the substrate and the technology
            substrate type has to be the opposite of the implant of
            the diode.
        min_well_enclosure: optional minimum required enclosure of the
            base wire by the well. If no well is specified no
            min_well_enclosure may be specified either. If a well is
            specified but no min_well_enclosure the minimum well enclosure
            from the base WaferWire will be used.
        model: the spice model name
        widthspace_args: the arguments for `_WidthSpacePrimitive`
    """
    def __init__(self, *, name: Optional[str]=None,
        wire: WaferWire, indicator: SingleOrMulti[DiodeIndicator].T,
        min_indicator_enclosure: SingleOrMulti[prp.Enclosure].T,
        implant: Implant, min_implant_enclosure: Optional[prp.Enclosure]=None,
        well: Optional[Well]=None, min_well_enclosure: Optional[prp.Enclosure]=None,
        model: Optional[str]=None, **widthspace_args,
    ):
        self.wire = wire

        self.indicator = indicator = _util.v2t(indicator)

        if "grid" in widthspace_args:
            raise TypeError("Resistor got an unexpected keyword argument 'grid'")

        if "min_width" in widthspace_args:
            if widthspace_args["min_width"] < wire.min_width:
                raise ValueError("min_width may not be smaller than base wire min_width")
        else:
            widthspace_args["min_width"] = wire.min_width

        if "min_space" in widthspace_args:
            if widthspace_args["min_space"] < wire.min_space:
                raise ValueError("min_space may not be smaller than base wire min_space")
        else:
            widthspace_args["min_space"] = wire.min_space

        self.min_indicator_enclosure = min_indicator_enclosure = _util.v2t(
            min_indicator_enclosure, n=len(indicator),
        )

        if isinstance(implant, Well):
            raise TypeError(f"implant '{implant.name}' is a well")
        if not implant in wire.implant:
            raise ValueError(
                f"implant '{implant.name}' is not valid for waferwire '{wire.name}'"
            )
        self.implant = implant
        self.min_implant_enclosure = min_implant_enclosure

        if "mask" in widthspace_args:
            raise TypeError("Diode got an unexpected keyword argument 'mask'")
        else:
            widthspace_args["mask"] = msk.Intersect(
                prim.mask for prim in (wire, *indicator, implant)
            ).alias(f"diode:{name}")

        super().__init__(name=name, **widthspace_args)

        self.ports += (
            _PrimitiveNet(prim=self, name=name)
            for name in ("anode", "cathode")
        )

        if well is None:
            if not wire.allow_in_substrate:
                raise TypeError(f"wire '{wire.name}' has to be in a well")
            # TODO: check types of substrate and implant
            if min_well_enclosure is not None:
                raise TypeError("min_well_enclosure given without a well")
        else:
            if well not in wire.well:
                raise ValueError(
                    f"well '{well.name}' is not a valid well for wire '{wire.name}'"
                )
            if well.type_ == implant.type_:
                raise ValueError(
                    f"type of implant '{implant.name}' may not be the same as"
                    " type of well '{well.name}' for a diode"
                )
        self.well = well
        self.min_well_enclosure = min_well_enclosure

        self.model = model

    def _generate_rules(self, *,
        tech: tch.Technology,
    ) -> Generator[rle._Rule, None, None]:
        # Do not generate the default width/space rules.
        yield from _Primitive._generate_rules(self, tech=tech)

        # TODO: Can we provide proper type for self.mask ?
        yield cast(msk.DesignMask, self.mask)
        if self.min_width > self.wire.min_width:
            yield self.mask.width >= self.min_width
        if self.min_space > self.wire.min_space:
            yield self.mask.space >= self.min_space
        for i, ind in enumerate(self.indicator):
            enc = self.min_indicator_enclosure[i]
            yield self.wire.mask.enclosed_by(ind.mask) >= enc
        if self.min_implant_enclosure is not None:
            enc = self.min_implant_enclosure
            yield self.mask.enclosed_by(self.implant.mask) >= enc


class MOSFETGate(_WidthSpacePrimitive):
    """MOSFETGate is a primitive representing the gate of a MOSFET transistor.
    A self-aligned process is assumed for the MOSFET so the gate is basically
    the area where a gate layer crosses the active layer. A dielectric layer
    in between the two layers is forming the gate capacitor the is part of the
    basic principles of how a MOSFET device funtions.
    The gate has a seaparte primitive as it often is common between different
    MOSFET devices (e.g. nmos and pmos or multi-Vt devices) with common rules.

    Arguments:
        name: optional name for the gate.
            If not specified a unique name based on the layers is given
        active: the bottom layer for the gate.
            The part of the active layer under the gate layer is acting as the
            channel of the MOSFET.
        poly: the top layer of gate.
        oxide: optionally an oxide layer can be given to have gate for different
            types of devices.
            If not specified it means to default oxide layer of the process is
            present to form the
        min_gateoxide_enclosure: optional minimum required enclosure of the gate
            by the oxide layer
        inside: optional marker layers for the gate.
            This allows to specify alternative rules for a device that is
            physically processed the same as another device.
            Example use is the marking of ESD devices with own rules but
            being physically the same device as the other higher voltage
            devices.
        min_gateinside_enclosure: optional minimum required enclosure of the gate
            by the inside layer. If 1 value is specified it is used for all the
            inside layers.
        min_l: optional minimum l specification valid for all MOSFET devices
            using this gate.
            If not specified the minimum poly layer width will be used as
            the minimum l.
        min_w: optional minimum w specification valid for all MOSFET devices
            using this gate.
            If not specified the minimum active layer width will be used as
            the minimum w.
        min_sd_width: optional minimum extension of the active layer over
            the gate.
        min_polyactive_extension: optional minimum extension of the poly layer
            over the gate.
        min_gate_space: optional minimum spacing between two gates sharing
            the same active wire
        contact: optional contact layer for this device; this is needed to
            allow to specify the minimum contact to gate spacing.
        min_contactgate_space: optional common specification of minimum contact
            to gate spacing
    """
    class _ComputedProps:
        def __init__(self, gate: "MOSFETGate"):
            self.gate = gate

        @property
        def min_l(self) -> float:
            min_l = self.gate.min_l
            if min_l is None:
                min_l = self.gate.poly.min_width
            return min_l

        @property
        def min_w(self) -> float:
            min_w = self.gate.min_w
            if min_w is None:
                min_w = self.gate.active.min_width
            return min_w

        @property
        def min_gate_space(self) -> float:
            s = self.gate.min_gate_space
            if s is None:
                s = self.gate.poly.min_space
            return s

        @property
        def min_sd_width(self) -> Optional[float]:
            return self.gate.min_sd_width

        @property
        def min_polyactive_extension(self) -> Optional[float]:
            return self.gate.min_polyactive_extension

    @property
    def computed(self):
        """the computed property allows to get values for parameters that
        were not specified during object init.
        For example assume that `gate` is MOSFETGate object that did not
        specify `min_l`. Then `gate.min_l` is `None` and `gate.computed.min_l`
        is equal to `gate.poly.min_width`.
        This separation is done to server different use cases. When looking
        at DRC rules `gate.min_l` being `None` indicated no extra rule
        needs to be generated for this gate. For layout it is easier to use
        `gate.computed.min_l` to derive the dimension of the device to be
        drawn.
        """
        return MOSFETGate._ComputedProps(self)

    def __init__(self, *, name: Optional[str]=None,
        active: WaferWire, poly: GateWire,
        oxide: Optional[Insulator]=None,
        min_gateoxide_enclosure: Optional[prp.Enclosure]=None,
        inside: OptSingleOrMulti[Marker].T=None,
        min_gateinside_enclosure: OptSingleOrMulti[prp.Enclosure].T=None,
        min_l: Optional[IntFloat]=None, min_w: Optional[IntFloat]=None,
        min_sd_width: Optional[IntFloat]=None,
        min_polyactive_extension: Optional[IntFloat]=None,
        min_gate_space: Optional[IntFloat]=None,
        contact: Optional[Via]=None,
        min_contactgate_space: Optional[IntFloat]=None,
    ):
        self.active = active
        self.poly = poly

        prims = (poly, active)
        if oxide is not None:
            if (active.oxide is None) or (oxide not in active.oxide):
                raise ValueError(
                    f"oxide '{oxide.name}' is not valid for active '{active.name}'"
                )
            prims += (oxide,)
        elif min_gateoxide_enclosure is not None:
            raise TypeError("min_gateoxide_enclosure provided without an oxide")
        self.oxide = oxide
        self.min_gateoxide_enclosure = min_gateoxide_enclosure

        if inside is not None:
            inside = _util.v2t(inside)
            prims += inside
            if min_gateinside_enclosure is not None:
                min_gateinside_enclosure = _util.v2t(min_gateinside_enclosure, n=len(inside))
        elif min_gateinside_enclosure is not None:
            raise TypeError("min_gateinside_enclosure provided without inside provided")
        self.inside = inside
        self.min_gateinside_enclosure = min_gateinside_enclosure

        if name is None:
            name = "gate({})".format(",".join(prim.name for prim in prims))
            gatename = "gate:" + "+".join(prim.name for prim in prims)
        else:
            gatename = f"gate:{name}"

        if min_l is not None:
            min_l = _util.i2f(min_l)
            self.min_l = min_l
        else:
            # local use only
            min_l = poly.min_width
            self.min_l = None

        if min_w is not None:
            min_w = _util.i2f(min_w)
            self.min_w = min_w
        else:
            # local use only
            min_w = active.min_width
            self.min_w = None

        if min_sd_width is not None:
            min_sd_width = _util.i2f(min_sd_width)
        self.min_sd_width = min_sd_width

        if min_polyactive_extension is not None:
            min_polyactive_extension = _util.i2f(min_polyactive_extension)
        self.min_polyactive_extension = min_polyactive_extension

        if min_gate_space is not None:
            min_gate_space = _util.i2f(min_gate_space)
            self.min_gate_space = min_gate_space
        else:
            # Local use only
            min_gate_space = poly.min_space
            self.min_gate_space = None

        if min_contactgate_space is not None:
            if contact is None:
                raise TypeError(
                    "min_contactgate_space given without contact layer"
                )
            min_contactgate_space = _util.i2f(min_contactgate_space)
        elif contact is not None:
            raise TypeError(
                "contact layer provided without min_contactgate_space specification"
            )
        self.contact = contact
        self.min_contactgate_space = min_contactgate_space

        mask = msk.Intersect(prim.mask for prim in prims).alias(gatename)
        super().__init__(
            name=name, mask=mask,
            min_width=min(min_l, min_w), min_space=min_gate_space,
        )

    def _generate_rules(self, *,
        tech: tch.Technology,
    ) -> Generator[rle._Rule, None, None]:
        active_mask = self.active.mask
        poly_mask = self.poly.conn_mask

        # Update mask if it has no oxide
        extra_masks = tuple()
        if self.oxide is None:
            extra_masks += tuple(
                cast(Any, gate).oxide.mask for gate in filter(
                    lambda prim: (
                        isinstance(prim, MOSFETGate)
                        and prim.active == self.active
                        and prim.poly == self.poly
                        and (prim.oxide is not None)
                    ), tech.primitives,
                )
            )
        if self.inside is None:
            def get_key(gate: "MOSFETGate"):
                if gate.oxide is not None:
                    return frozenset((gate.active, gate.poly, gate.oxide))
                else:
                    return frozenset((gate.active, gate.poly))

            for gate in filter(
                lambda prim: (
                    isinstance(prim, MOSFETGate)
                    and (get_key(prim) == get_key(self))
                    and prim.inside is not None
                ), tech.primitives,
            ):
                extra_masks += tuple(inside.mask for inside in cast(Any, gate).inside)
        masks = (active_mask, poly_mask)
        if self.oxide is not None:
            masks += (self.oxide.mask,)
        if self.inside is not None:
            masks += tuple(inside.mask for inside in self.inside)
        if extra_masks:
            masks += (wfr.outside(extra_masks),)
        # Keep the alias but change the mask of the alias
        cast(msk._MaskAlias, self.mask).mask = msk.Intersect(masks)
        mask = self.mask

        mask_used = False
        rules: List[rle._Rule] = []
        if self.min_l is not None:
            rules.append(
                edg.Intersect(
                    (edg.MaskEdge(active_mask), edg.MaskEdge(self.mask))
                ).length >= self.min_l,
            )
        if self.min_w is not None:
            rules.append(
                edg.Intersect(
                    (edg.MaskEdge(poly_mask), edg.MaskEdge(self.mask))
                ).length >= self.min_w,
            )
        if self.min_sd_width is not None:
            rules.append(active_mask.extend_over(mask) >= self.min_sd_width)
            mask_used = True
        if self.min_polyactive_extension is not None:
            rules.append(
                poly_mask.extend_over(mask) >= self.min_polyactive_extension,
            )
            mask_used = True
        if self.min_gate_space is not None:
            rules.append(mask.space >= self.min_gate_space)
            mask_used = True
        if self.min_contactgate_space is not None:
            assert self.contact is not None
            rules.append(
                msk.Spacing(mask, self.contact.mask) >= self.min_contactgate_space,
            )
            mask_used = True

        if mask_used:
            # This rule has to be put before the other rules that use the alias
            yield cast(rle._Rule, mask)
        yield from _MaskPrimitive._generate_rules(self, tech=tech, gen_mask=False)
        yield from rules


class MOSFET(_Primitive):
    """MOSFET is a primitive representing a MOSFET transistor.

    MOS stands for metal-oxide-semiconductor; see
    https://en.wikipedia.org/wiki/MOSFET for explanation of a MOSFET device.

    Arguments:
        name: name for the gate.
        gate: the `MOSFETGate` object for this device
        implant: implant layers for this device
        well: optional well in which this MOSFET needs to be located.
            If gate.active can't be put in substrate well has to be
            specified. If specified the well has to be valid for
            gate.active and the implant type has to be opposite to the
            implant types.
        min_l: optional minimum l specification for the MOSFET device
            If not specified the min_l of the gate will be used, which
            in turn could be the gate poly layer minimum width.
        min_w: optional minimum w specification valid the MOSFET device
            If not specified the min_w of the gate will be used, which
            in turn could be the gate active layer minimum width.
        min_sd_width: optional minimum extension of the active layer over
            the gate.
            If not specified the value from the gate will be used.
            This value has to be specified either here or for the gate.
        min_polyactive_extension: optional minimum extension of the poly layer
            over the gate.
            If not specified the value from the gate will be used.
            This value has to be specified either here or for the gate.
        min_gateimplant_enclosure: SingleOrMulti[prp.Enclosure].T,
        min_gate_space: optional minimum spacing between two gates sharing
            the same active wire
            If not specified the value from the gate will be used.
            This value has to be specified either here or for the gate.
        contact: optional contact layer for this device; this is needed to
            allow to specify the minimum contact to gate spacing.
            If not specified the value from the gate will be used.
        min_contactgate_space: optional common specification of minimum contact
            to gate spacing
            If not specified the value from the gate will be used.
            If neither the gate nor here contact is specified this parameter may
            not be specified either. Otherwise here and/or the gate have to
            speicify a value.
        model: optional spice model name for the device. Needed when one wants
            to do spice simulations or LVS.
    """
    class _ComputedProps:
        def __init__(self, mosfet: "MOSFET"):
            self.mosfet = mosfet

        def _lookup(self, name: str, allow_none: bool):
            mosfet = self.mosfet
            v = getattr(mosfet, name)
            if v is None:
                v = getattr(mosfet.gate.computed, name, None)
            if v is None:
                v = getattr(mosfet.gate, name, None)
            if not allow_none:
                assert v is not None, "needed attribute"
            return v

        @property
        def min_l(self) -> float:
            return cast(float, self._lookup("min_l", False))

        @property
        def min_w(self) -> float:
            return cast(float, self._lookup("min_w", False))

        @property
        def min_sd_width(self) -> float:
            return cast(float, self._lookup("min_sd_width", False))

        @property
        def min_polyactive_extension(self) -> float:
            return cast(float, self._lookup("min_polyactive_extension", False))

        @property
        def min_gate_space(self) -> float:
            return cast(float, self._lookup("min_gate_space", False))

        @property
        def contact(self) -> Optional[Via]:
            return cast(Optional[Via], self._lookup("contact", True))

        @property
        def min_contactgate_space(self) -> float:
            return cast(float, self._lookup("min_contactgate_space", False))

    @property
    def computed(self):
        """the computed property allows to get values for parameters that
        were not specified during object init.
        For example assume that `nmos` is MOSFET object that did not
        specify `min_l`. Then `nmos.min_l` is `None` and `nmos.computed.min_l`
        is equal to `nmos.gate.computed.min_l`, which can then
        refer further to `nmos.gate.poly.min_width`.
        This separation is done to server different use cases. When looking
        at DRC rules `gate.min_l` being `None` indicated no extra rule
        needs to be generated for this gate. For layout it is easier to use
        `gate.computed.min_l` to derive the dimension of the device to be
        drawn.
        """
        return MOSFET._ComputedProps(self)

    def __init__(
        self, *, name: str,
        gate: MOSFETGate, implant: SingleOrMulti[Implant].T,
        well: Optional[Well]=None,
        min_l: Optional[IntFloat]=None, min_w: Optional[IntFloat]=None,
        min_sd_width: Optional[IntFloat]=None,
        min_polyactive_extension: Optional[IntFloat]=None,
        min_gateimplant_enclosure: SingleOrMulti[prp.Enclosure].T,
        min_gate_space: Optional[IntFloat]=None,
        contact: Optional[Via]=None,
        min_contactgate_space: Optional[IntFloat]=None,
        model: Optional[str]=None,
    ):
        super().__init__(name=name)

        implant = _util.v2t(implant)
        type_ = None
        for impl in implant:
            if not (impl.type_ == "adjust"):
                if type_ is None:
                    type_ = impl.type_
                elif type_ != impl.type_:
                    raise ValueError(
                        "both n and p type implants for same MOSFET are not allowed"
                    )
        if type_ is None:
            raise ValueError(
                "at least one n or p type implant has to be specified"
            )
        wrong = tuple(filter(
            lambda impl: impl not in gate.active.implant,
            implant
        ))
        if wrong:
            names = tuple(impl.name for impl in wrong)
            raise ValueError(
                f"implants {names} not valid for gate.active '{gate.active.name}'"
            )

        if well is None:
            if not gate.active.allow_in_substrate:
                raise ValueError(
                    f"well needed as gate active '{gate.active.name}'"
                    " can't be put in substrate"
                )
        else:
            if well not in gate.active.well:
                raise ValueError(
                    f"well '{well.name}' not valid for gate.active '{gate.active.name}'"
                )
            if type_ == well.type_:
                raise ValueError("well and implant(s) have to be of different type")

        self.gate = gate
        self.implant = implant
        self.well = well

        if min_l is not None:
            min_l = _util.i2f(min_l)
            if min_l <= gate.computed.min_l:
                raise ValueError("min_l has to be bigger than gate min_l if not 'None'")
        self.min_l = min_l

        if min_w is not None:
            min_w = _util.i2f(min_w)
            if min_w <= gate.computed.min_w:
                raise ValueError("min_w has to be bigger than gate min_w if not 'None'")
        self.min_w = min_w

        if min_sd_width is not None:
            min_sd_width = _util.i2f(min_sd_width)
        elif gate.min_sd_width is None:
            raise ValueError(
                "min_sd_width neither provided for the transistor gate or the transistor",
            )
        self.min_sd_width = min_sd_width

        if min_polyactive_extension is not None:
            min_polyactive_extension = _util.i2f(min_polyactive_extension)
        elif gate.min_polyactive_extension is None:
            raise ValueError(
                "min_polyactive_extension neither provided for the transistor gate"
                " or the transistor",
            )
        self.min_polyactive_extension = min_polyactive_extension

        self.min_gateimplant_enclosure = min_gateimplant_enclosure = _util.v2t(
            min_gateimplant_enclosure, n=len(implant),
        )

        if min_gate_space is not None:
            min_gate_space = _util.i2f(min_gate_space)
        self.min_gate_space = min_gate_space

        if min_contactgate_space is not None:
            min_contactgate_space = _util.i2f(min_contactgate_space)
            if contact is None:
                if gate.contact is None:
                    raise ValueError(
                        "no contact layer provided for min_contactgate_space specification",
                    )
                contact = gate.contact
        elif contact is not None:
            raise ValueError(
                "contact layer provided without min_contactgate_space specification",
            )
        self.min_contactgate_space = min_contactgate_space
        self.contact = contact

        self.model = model

        # MOSFET is symmetric so both diffusion regions can be source or drain
        bulknet = (
            _PrimitiveNet(prim=self, name="bulk") if well is not None
            else wfr.SubstrateNet(name="bulk")
        )
        self.ports += (
            _PrimitiveNet(prim=self, name="sourcedrain1"),
            _PrimitiveNet(prim=self, name="sourcedrain2"),
            _PrimitiveNet(prim=self, name="gate"),
            bulknet,
        )

        for impl in implant:
            try:
                idx = gate.active.implant.index(impl)
            except: # pragma: no cover
                continue
            else:
                impl_act_enc = gate.active.min_implant_enclosure[idx]
                break
        else: # pragma: no cover
            raise AssertionError("Internal error")

        self.params += (
            _Param(primitive=self, name="l", default=self.computed.min_l),
            _Param(primitive=self, name="w", default=self.computed.min_w),
            _EnclosureParam(
                primitive=self, name="activeimplant_enclosure",
                default=impl_act_enc,
            ),
            _Param(primitive=self, name="sd_width", default=self.computed.min_sd_width),
            _Param(
                primitive=self, name="polyactive_extension",
                default=self.computed.min_polyactive_extension,
            ),
            _EnclosuresParam(
                primitive=self, name="gateimplant_enclosures", n=len(implant),
                default=min_gateimplant_enclosure,
            ),
        )

        spc = self.computed.min_gate_space
        if spc is not None:
            self.params += _Param(primitive=self, name="gate_space", default=spc)
        if self.computed.contact is not None:
            spc = self.computed.min_contactgate_space
            assert spc is not None
            self.params += _Param(primitive=self, name="contactgate_space", default=spc)

    @property
    def gate_prim(self) -> _Intersect:
        """gate_prim attribute is the primitive representing the gate of the MOSFET
        object. Main reason it exists is to use it in rules; for example a minimum spacing
        to the gate of a transistor.
        """
        prims: Tuple[_MaskPrimitive, ...] = (self.gate, *self.implant)
        if self.well is not None:
            prims += (self.well,)

        return _Intersect(prims=prims)

    @property
    def gate_mask(self):
        return self._gate_mask

    def _generate_rules(self, *,
        tech: tch.Technology,
    ) -> Generator[rle._Rule, None, None]:
        yield from super()._generate_rules(tech=tech)

        markers = (self.well.mask if self.well is not None else tech.substrate,)
        if self.implant is not None:
            markers += tuple(impl.mask for impl in self.implant)
        derivedgate_mask = msk.Intersect((self.gate.mask, *markers)).alias(
            f"gate:mosfet:{self.name}",
        )
        self._gate_mask = derivedgate_mask
        derivedgate_edge = edg.MaskEdge(derivedgate_mask)
        poly_mask = self.gate.poly.mask
        poly_edge = edg.MaskEdge(poly_mask)
        channel_edge = edg.Intersect((derivedgate_edge, poly_edge))
        active_mask = self.gate.active.mask
        active_edge = edg.MaskEdge(active_mask)
        fieldgate_edge = edg.Intersect((derivedgate_edge, active_edge))

        yield derivedgate_mask
        if self.min_l is not None:
            yield edg.Intersect(
                (derivedgate_edge, active_edge),
            ).length >= self.min_l
        if self.min_w is not None:
            yield edg.Intersect(
                (derivedgate_edge, poly_edge),
            ).length >= self.min_w
        if self.min_sd_width is not None:
            yield (
                active_mask.extend_over(derivedgate_mask) >= self.min_sd_width
            )
        if self.min_polyactive_extension is not None:
            yield (
                poly_mask.extend_over(derivedgate_mask)
                >= self.min_polyactive_extension
            )
        for i in range(len(self.implant)):
            impl_mask = self.implant[i].mask
            enc = self.min_gateimplant_enclosure[i]
            if not enc.is_assymetric:
                yield derivedgate_mask.enclosed_by(impl_mask) >= enc
            else:
                yield channel_edge.enclosed_by(impl_mask) >= enc.spec[0]
                yield fieldgate_edge.enclosed_by(impl_mask) >= enc.spec[1]
        if self.min_gate_space is not None:
            yield derivedgate_mask.space >= self.min_gate_space
        if self.min_contactgate_space is not None:
            assert self.contact is not None
            yield (
                msk.Spacing(derivedgate_mask, self.contact.mask)
                >= self.min_contactgate_space
            )

    @property
    def designmasks(self):
        yield from super().designmasks
        yield from self.gate.designmasks
        if self.implant is not None:
            for impl in self.implant:
                yield from impl.designmasks
        if self.well is not None:
            yield from self.well.designmasks
        if self.contact is not None:
            if (self.gate.contact is None) or (self.contact != self.gate.contact):
                yield from self.contact.designmasks


class Bipolar(_Primitive):
    """The Bipolar primitive represents the bipolar injunction transistors.
    It's thus a PNP or a NPN device.

    For more info see https://en.wikipedia.org/wiki/Bipolar_junction_transistor

    Currently no layout generation for this device is implemented and the
    technology will need to provide fixed layout implementations. Bipolar
    devices are assumed to have fixed layouts for each technology.

    Arguments:
        name: name of the Bipolar device
        type_: the bipolar type; has to be 'npn' or 'pnp'
        model: the optional (spice) model name for the device
        indicator: the layer(s) to mark a certain structure as a bipolar device

    API Notes:
        Bipolar does not have a fixed API yet. Backwards incompatible changes
        are reserved for implemting more general layout generation.
    """
    # TODO: add the specification for WaferWire and implants with which the
    #     collector, base and emittor of the device are made.
    def __init__(self, *,
        name: str, type_: str, model: Optional[str]=None, is_subcircuit=False,
        indicator: SingleOrMulti[Marker].T,
    ):
        if type_ not in ("npn", "pnp"):
            raise ValueError(f"type_ hos to be 'pnp' or 'npn' not '{type_}'")
        super().__init__(name=name)

        self.type_ = type_
        self.model = model
        self.is_subcircuit = is_subcircuit
        self.indicator = _util.v2t(indicator)

        self.ports += (
            _PrimitiveNet(prim=self, name="collector"),
            _PrimitiveNet(prim=self, name="base"),
            _PrimitiveNet(prim=self, name="emitter"),
        )

    def _generate_rules(self, *, tech: tch.Technology) -> Iterable[rle._Rule]:
        return super()._generate_rules(tech=tech)

    @property
    def designmasks(self) -> Iterable[msk.DesignMask]:
        yield from super().designmasks
        for indicator in self.indicator:
            yield from indicator.designmasks


class _RulePrimitive(_Primitive):
    """Subclasses of _RulePrimitive represent extra design rules without further
    physical representation of a Primitive. They thus don't have a layout etc.
    It's a base class that needs to be subclassed.
    """
    pass


class Spacing(_RulePrimitive):
    """A _RulePrimitive that allows to define extra minimum space requirement
    that is not derived from the parameters from any of the primitives in the
    a technology

    Argumnets:
        primitives1: first set of primitives
            If primitives2 is not provided this set has to contain more than
            one primitive and the minimum space requirement is for the
            combined shape of joining all shapes in all the layers in this
            set.
        primitives2: optinal second set of primitives
            If this set is provided the minimum space specification is for
            each shape on a layer in primitives1 to each shape on a layer
            in primitives2.
        min_space: the minimum space specifcation
    """
    def __init__(self, *,
        primitives1: SingleOrMulti[_MaskPrimitive].T,
        primitives2: Optional[SingleOrMulti[_MaskPrimitive].T]=None,
        min_space: IntFloat,
    ):
        primitives1 = _util.v2t(primitives1)
        primitives2 = _util.v2t(primitives2) if primitives2 is not None else None
        min_space = _util.i2f(min_space)

        if primitives2 is not None:
            name = "Spacing({},{:.6})".format(
                ",".join(
                    (
                        prims[0].name if len(prims) == 1
                        else "({})".format(",".join(prim.name for prim in prims))
                    ) for prims in (primitives1, primitives2)
                ),
                min_space,
            )
        else:
            s_prim1 = (
                primitives1[0].name if len(primitives1) == 1
                else "({})".format(",".join(prim.name for prim in primitives1))
            )
            name = f"Spacing({s_prim1},None,{min_space:.6})"
        super().__init__(name=name)
        self.primitives1 = primitives1
        self.primitives2 = primitives2
        self.min_space = min_space

    def _generate_rules(self, *,
        tech: tch.Technology,
    ) -> Generator[rle._Rule, None, None]:
        yield from super()._generate_rules(tech=tech)

        if self.primitives2 is None:
            joined = msk.Join(prim1.mask for prim1 in self.primitives1)
            yield joined.space >= self.min_space
        else:
            yield from (
                msk.Spacing(prim1.mask, prim2.mask) >= self.min_space
                for prim1, prim2 in product(self.primitives1, self.primitives2)
            )

    @property
    def designmasks(self):
        yield from super().designmasks
        if self.primitives2 is not None:
            for prim in (*self.primitives1, *self.primitives2):
                yield from prim.designmasks
        else:
            for prim in self.primitives1:
                yield from prim.designmasks

    def __repr__(self):
        return self.name


class Enclosure(_RulePrimitive):
    """A _RulePrimitive that allows to define extra minimum enclosure
    requirement that is not derived from the parameters from any of the
    primitives in a technology.

    Argumnets:
        prim: the base primitive
        by: the enclosing primitive
        min_enclosure: the minimum `Enclosure` of `prim` by `by`
    """
    def __init__(self, *,
        prim: _MaskPrimitive, by: _MaskPrimitive, min_enclosure: prp.Enclosure,
    ):
        name = f"Enclosure(prim={prim!r},by={by!r},min_enclosure={min_enclosure!r})"
        super().__init__(name=name)

        self.prim = prim
        self.by = by
        self.min_enclosure = min_enclosure

    def _generate_rules(self, *,
        tech: tch.Technology,
    ) -> Generator[rle._Rule, None, None]:
        yield from super()._generate_rules(tech=tech)

        yield self.prim.mask.enclosed_by(self.by.mask) >= self.min_enclosure

    @property
    def designmasks(self) -> Generator[msk.DesignMask, None, None]:
        yield from super().designmasks
        yield from self.prim.designmasks
        yield from self.by.designmasks

    def __repr__(self) -> str:
        return self.name


class NoOverlap(_RulePrimitive):
    """A _RulePrimitive that allows to define extra no overlap
    requirement that is not derived from the parameters from any of the
    primitives in a technology.

    Argumnets:
        prim1, prim2:  the two primitives where none of the shape may
            have a overlapping part.
    """
    def __init__(self, *, prim1: _MaskPrimitive, prim2: _MaskPrimitive):
        name = f"NoOverlap(prim1={prim1!r},prim2={prim2!r})"
        super().__init__(name=name)

        self.prim1 = prim1
        self.prim2 = prim2

    def _generate_rules(self, *,
        tech: tch.Technology,
    ) -> Generator[rle._Rule, None, None]:
        yield from super()._generate_rules(tech=tech)

        intersect = _Intersect(prims=(self.prim1, self.prim2))
        yield intersect.mask.area == 0.0

    @property
    def designmasks(self) -> Generator[msk.DesignMask, None, None]:
        yield from super().designmasks
        yield from self.prim1.designmasks
        yield from self.prim2.designmasks

    def __repr__(self) -> str:
        return self.name


class Primitives(_util.TypedListStrMapping[_Primitive]):
    """A collection of `_Primitive` objects"""
    @property
    def _elem_type_(self):
        return _Primitive

    def __iadd__(self, x: SingleOrMulti[_Primitive].T) -> "Primitives":
        x = _util.v2t(x)
        for elem in x:
            if isinstance(elem, _DerivedPrimitive):
                raise TypeError(
                    f"_DerivedPrimitive '{elem.name}' can't be added to 'Primitives'",
                )
            if elem in self:
                raise ValueError(
                    f"Adding primitive with name '{elem.name}' twice"
                )
        return cast("Primitives", super().__iadd__(x))


class UnusedPrimitiveError(Exception):
    """Exception used by `Technology` when checking the primitives list
    of a technology"""
    def __init__(self, primitive: _Primitive):
        super().__init__(
            f"primitive '{primitive.name}' defined but not used"
        )


class UnusedMIMTop(Exception):
    """Exception used by `Technology` when checking the primitives list
    of a technology"""
    def __init__(self, mimtop: MIMTop):
        super().__init__(
            f"MIMTop '{mimtop.name}' not used as a top in a MIMCapacitor"
        )


class UnconnectedPrimitiveError(Exception):
    """Exception used by `Technology` when checking the primitives list
    of a technology"""
    def __init__(self, primitive: _Primitive):
        super().__init__(
            f"primitive '{primitive.name}' is not connected"
        )
