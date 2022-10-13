# SPDX-License-Identifier: GPL-2.0-or-later OR AGPL-3.0-or-later OR CERN-OHL-S-2.0+
"""The pdkmaster.design.layout module provides classes to represent layout shapes
in a PDKMaster technology. These classes are designed to only allow to create
layout that conform to the technology definition. In order to detect design
shorts as fast as possible shapes are put on nets.

A LayoutFactory class is provided to generate layouts for a certain technology and
it's primitives.

Internally the klayout API is used to represent the shapes and perform manipulations
on them.
"""
import abc
from pdkmaster.typing import IntFloat, SingleOrMulti
from typing import (
    Any, Iterable, Generator, Sequence, Mapping, Tuple, Dict, Optional, Union,
    Type, cast, overload,
)

from .. import _util, dispatch as dsp
from ..technology import (
    property_ as prp, net as net_, mask as msk, geometry as geo,
    primitive as prm, technology_ as tch,
)
from . import circuit as ckt

__all__ = [
    "MaskShapesSubLayout",
    "SubLayouts",
    "LayoutFactory",
]


class NetOverlapError(Exception):
    pass


def _rect(
    left: float, bottom: float, right: float, top: float, *,
    enclosure: Optional[Union[float, Sequence[float], prp.Enclosure]]=None,
) -> geo.Rect:
    """undocumented deprecated function;
    see: https://gitlab.com/Chips4Makers/PDKMaster/-/issues/39
    """
    if enclosure is not None:
        if isinstance(enclosure, prp.Enclosure):
            enclosure = enclosure.spec
        if isinstance(enclosure, float):
            left -= enclosure
            bottom -= enclosure
            right += enclosure
            top += enclosure
        else:
            left -= enclosure[0]
            bottom -= enclosure[1]
            right += enclosure[0]
            top += enclosure[1]

    return geo.Rect(
        left=left, bottom=bottom, right=right, top=top,
    )


def _via_array(
    left: float, bottom: float, width: float, pitch: float, rows: int, columns: int,
):
    """undocumented deprecated function;
    see: https://gitlab.com/Chips4Makers/PDKMaster/-/issues/39
    """
    via = geo.Rect.from_size(width=width, height=width)
    xy0 = geo.Point(x=(left + 0.5*width), y=(bottom + 0.5*width))

    if (rows == 1) and (columns == 1):
        return via + xy0
    else:
        return geo.ArrayShape(
            shape=via, offset0=xy0, rows=rows, columns=columns, pitch_x=pitch, pitch_y=pitch,
        )


class _SubLayout(abc.ABC):
    """Internal `_Layout` support class"""
    @abc.abstractmethod
    def __init__(self):
        ... # pragma: no cover

    @property
    @abc.abstractmethod
    def polygons(self) -> Iterable[geo.MaskShape]:
        ... # pragma: no cover

    @abc.abstractmethod
    def dup(self) -> "_SubLayout":
        ... # pragma: no cover

    @abc.abstractmethod
    def move(self, *,
        dxy: geo.Point, move_context: Optional[geo.MoveContext]=None,
    ) -> None:
        ... # pragma: no cover

    @abc.abstractmethod
    def moved(self, *,
        dxy: geo.Point, move_context: Optional[geo.MoveContext]=None,
    ) -> "_SubLayout":
        ... # pragma: no cover

    @abc.abstractmethod
    def rotate(self, *,
        rotation: geo.Rotation, rot_context: Optional[geo.RotationContext]=None,
    ) -> None:
        ... # pragma: no cover

    @abc.abstractmethod
    def rotated(self, *,
        rotation: geo.Rotation, rot_context: Optional[geo.RotationContext]=None,
    ) -> "_SubLayout":
        ... # pragma: no cover

    @property
    @abc.abstractmethod
    def _hier_strs_(self) -> Generator[str, None, None]:
        ... # pragma: no cover


class MaskShapesSubLayout(_SubLayout):
    """Object representing the sublayout of a net consisting of geometry._Shape
    objects.

    Arguments:
        net: The net of the SubLayout
            `None` value represents no net for the shapes.
        shapes: The maskshapes on the net.
    """
    def __init__(self, *, net: Optional[net_.Net], shapes: geo.MaskShapes):
        self._net = net
        self._shapes = shapes

    @property
    def net(self) -> Optional[net_.Net]:
        return self._net
    @property
    def shapes(self) -> geo.MaskShapes:
        return self._shapes

    @property
    def polygons(self) -> Generator[geo.MaskShape, None, None]:
        yield from self.shapes

    def add_shape(self, *, shape: geo.MaskShape):
        self._shapes += shape

    def move(self, *,
        dxy: geo.Point, move_context: Optional[geo.MoveContext]=None,
    ) -> None:
        self._shapes = self.shapes.moved(dxy=dxy, context=move_context)

    def moved(self, *,
        dxy: geo.Point, move_context: Optional[geo.MoveContext]=None,
    ) -> "MaskShapesSubLayout":
        return MaskShapesSubLayout(
            net=self.net, shapes=self.shapes.moved(dxy=dxy, context=move_context),
        )

    def rotate(self, *,
        rotation: geo.Rotation, rot_context: Optional[geo.RotationContext]=None,
    ) -> None:
        self.shapes.rotate(rotation=rotation, context=rot_context)

    def rotated(self, *,
        rotation: geo.Rotation, rot_context: Optional[geo.RotationContext]=None,
    ) -> "MaskShapesSubLayout":
        return MaskShapesSubLayout(
            net=self.net,
            shapes=self.shapes.rotated(rotation=rotation, context=rot_context),
        )

    def dup(self) -> "MaskShapesSubLayout":
        return MaskShapesSubLayout(
            net=self.net, shapes=geo.MaskShapes(self.shapes),
        )

    @property
    def _hier_strs_(self) -> Generator[str, None, None]:
        yield f"MaskShapesSubLayout net={self.net}"
        for ms in self.shapes:
            yield "  " + str(ms)

    def __hash__(self):
        return hash((self.net, self.shapes))

    def __eq__(self, other: object) -> bool:
        if isinstance(other, MaskShapesSubLayout):
            return (self.net == other.net) and (self.shapes == other.shapes)
        else:
            return False


class _InstanceSubLayout(_SubLayout):
    """Internal `_Layout` support class"""
    def __init__(self, *,
        inst: ckt._CellInstance, origin: geo.Point,
        layoutname: Optional[str], rotation: geo.Rotation,
    ):
        self.inst = inst
        self.origin = origin
        self.rotation = rotation
        cell = inst.cell

        if layoutname is None:
            try:
                # Create default layout
                cell.layout
            except:
                raise ValueError(
                    f"Cell '{cell.name}' has no default layout and no layoutname"
                    " was specified"
                )
        else:
            if layoutname not in cell.layouts.keys():
                raise ValueError(
                    f"Cell '{cell.name}' has no layout named '{layoutname}'"
                )
        self.layoutname = layoutname
        # layout is a property and will only be looked up the first time it is accessed.
        # This is to support cell with delayed layout generation.
        self._layout = None

    @property
    def layout(self) -> "_Layout":
        if self._layout is None:
            l: "_Layout" = (
                self.inst.cell.layouts[self.layoutname]
                if self.layoutname is not None
                else self.inst.cell.layout
            )
            self._layout = l.rotated(rotation=self.rotation).moved(dxy=self.origin)

        return self._layout

    @property
    def boundary(self) -> Optional[geo._Rectangular]:
        l = (
            self.inst.cell.layouts[self.layoutname]
            if self.layoutname is not None
            else self.inst.cell.layout
        )
        if l.boundary is None:
            return None
        else:
            return l.boundary.rotated(rotation=self.rotation) + self.origin

    @property
    def polygons(self) -> Generator[geo.MaskShape, None, None]:
        yield from self.layout.polygons

    def dup(self):
        return self

    def move(self, *,
        dxy: geo.Point, move_context: Optional[geo.MoveContext]=None,
    ) -> None:
        self.origin += dxy
        self._layout = None

    def moved(self, *,
        dxy: geo.Point, move_context: Optional[geo.MoveContext]=None,
    ) -> "_InstanceSubLayout":
        orig = self.origin + dxy
        return _InstanceSubLayout(
            inst=self.inst, origin=orig, layoutname=self.layoutname, rotation=self.rotation,
        )

    def rotate(self, *,
        rotation: geo.Rotation, rot_context: Optional[geo.RotationContext]=None,
    ) -> None:
        self.origin = rotation*self.origin
        self.rotation *= rotation

    def rotated(self, *,
        rotation: geo.Rotation, rot_context: Optional[geo.RotationContext]=None,
    ) -> "_InstanceSubLayout":
        p = rotation*self.origin
        rot = rotation*self.rotation

        return _InstanceSubLayout(
            inst=self.inst, origin=p, layoutname=self.layoutname, rotation=rot,
        )

    @property
    def _hier_strs_(self) -> Generator[str, None, None]:
        yield f"_InstanceSubLayout inst={self.inst}, origin={self.origin}, rot={self.rotation}"
        for s in self.layout._hier_strs_:
            yield "  " + s


class SubLayouts(_util.TypedList[_SubLayout]):
    """Internal `_Layout` support class"""
    @property
    def _elem_type_(self):
        return _SubLayout

    def __init__(self, iterable: SingleOrMulti[_SubLayout].T=tuple()):
        if isinstance(iterable, _SubLayout):
            super().__init__((iterable,))
        else:
            super().__init__(iterable)

            nets = tuple(sl.net for sl in self.__iter_type__(MaskShapesSubLayout))
            if len(nets) != len(set(nets)):
                raise ValueError("Multiple `MaskShapesSubLayout` for same net")

    def dup(self) -> "SubLayouts":
        return SubLayouts(l.dup() for l in self)

    def __iadd__(self, other_: SingleOrMulti[_SubLayout].T) -> "SubLayouts":
        other: Iterable[_SubLayout]
        if isinstance(other_, _SubLayout):
            other = (other_,)
        else:
            other = tuple(other_)

        # Now try to add to other sublayouts
        def add2other(other_sublayout):
            if isinstance(other_sublayout, MaskShapesSubLayout):
                for sublayout in self.__iter_type__(MaskShapesSubLayout):
                    if sublayout.net == other_sublayout.net:
                        for shape in other_sublayout.shapes:
                            sublayout.add_shape(shape=shape)
                        return True
                else:
                    return False
            elif not isinstance(other_sublayout, _InstanceSubLayout): # pragma: no cover
                raise RuntimeError("Internal error")
        other = tuple(filter(lambda sl: not add2other(sl), other))

        if other:
            # Append remaining sublayouts
            self.extend(sl.dup() for sl in other)
        return self

    def __add__(self, other: SingleOrMulti[_SubLayout].T) -> "SubLayouts":
        ret = self.dup()
        ret += other
        return ret


class _Layout:
    """A `_Layout` object contains the shapes making up the layout of a design.
    Contrary to other EDA layout tools all shapes are put on a net or are netless.
    Netless are only allowed on mask derived from certain primitives.

    `LayoutFactory.new_layout()` needs to be used to generate new layouts.

    Attributes:
        fab: the factory with which this _layout is created
        sublayouts: the sublayouts making up this layout
        boundary: optional boundary of this layout
    """
    def __init__(self, *,
        fab: "LayoutFactory",
        sublayouts: SubLayouts, boundary: Optional[geo._Rectangular]=None,
    ):
        self.fab = fab
        self.sublayouts = sublayouts
        self.boundary = boundary

    @property
    def polygons(self) -> Iterable[geo.MaskShape]:
        """All the `MaskShape` polygons of this layout.

        Typically use case is exporting to a format that has no net information.
        """
        for sublayout in self.sublayouts:
                yield from sublayout.polygons

    def _net_sublayouts(self, *, net: net_.Net, depth: Optional[int]) -> Generator[
        MaskShapesSubLayout, None, None,
    ]:
        """Filter polygons; API to be fixed.
        see: https://gitlab.com/Chips4Makers/PDKMaster/-/issues/34
        """
        for sl in self.sublayouts:
            if isinstance(sl, _InstanceSubLayout): # pragma: no cover
                # TODO: add code coverage when finalizing API
                # see: https://gitlab.com/Chips4Makers/PDKMaster/-/issues/34
                assert isinstance(net, ckt._CircuitNet)
                if depth != 0:
                    for port in net.childports:
                        if (
                            isinstance(port, ckt._InstanceNet)
                            and (port.inst == sl.inst)
                        ):
                            yield from sl.layout._net_sublayouts(
                                net=port.net,
                                depth=(None if depth is None else (depth - 1)),
                            )
            elif isinstance(sl, MaskShapesSubLayout):
                if net == sl.net:
                    yield sl
            else: # pragma: no cover
                raise AssertionError("Internal error")

    def net_polygons(self, net: net_.Net, *, depth: Optional[int]=None) -> Generator[
        geo.MaskShape, None, None
    ]:
        """Filter polygons; API to be fixed.
        see: https://gitlab.com/Chips4Makers/PDKMaster/-/issues/34
        """
        for sl in self._net_sublayouts(net=net, depth=depth):
            yield from sl.shapes

    def filter_polygons(self, *,
        net: Optional[net_.Net]=None, mask: Optional[msk._Mask]=None,
        split: bool=False, depth: Optional[int]=None,
    ) -> Generator[geo.MaskShape, None, None]:
        """Filter polygons; API to be fixed.
        see: https://gitlab.com/Chips4Makers/PDKMaster/-/issues/34
        """
        if net is None:
            sls = self.sublayouts
        else:
            sls = self._net_sublayouts(net=net, depth=depth)
        for sl in sls:
            assert isinstance(sl, MaskShapesSubLayout)
            if mask is None:
                shapes = sl.shapes
            else:
                shapes = filter(lambda sh: sh.mask == mask, sl.shapes)
            if not split:
                yield from shapes
            else:
                for shape in shapes:
                    for shape2 in shape.shape.pointsshapes:
                        yield geo.MaskShape(mask=shape.mask, shape=shape2)

    def dup(self) -> "_Layout":
        """Create a duplication of a layout."""
        return _Layout(
            fab=self.fab,
            sublayouts=SubLayouts(sl.dup() for sl in self.sublayouts),
            boundary=self.boundary,
        )

    def bounds(self, *,
        mask: Optional[msk._Mask]=None, net: Optional[net_.Net]=None,
        depth: Optional[int]=None,
    ) -> geo.Rect:
        """Return the rectangle enclosing selected shapes; filtering of the
        shapes is done based on the given arguments.

        Arguments:
            mask: only shapes on this mask are selected
            net: only shapes on this net are selected
            depth: when specified only shapes until a certain hierarchy depth
                are selected.
        """
        if net is None:
            if depth is not None:
                raise TypeError(
                    f"depth has to 'None' if net is 'None'"
                )
            polygons = self.polygons
        else:
            polygons = self.net_polygons(net, depth=depth)
        mps = polygons if mask is None else filter(
            lambda mp: mp.mask == mask, polygons,
        )
        boundslist = tuple(mp.bounds for mp in mps)
        return geo.Rect(
            left=min(bds.left for bds in boundslist),
            bottom=min(bds.bottom for bds in boundslist),
            right=max(bds.right for bds in boundslist),
            top=max(bds.top for bds in boundslist),
        )

    def __iadd__(self, other: Union["_Layout", _SubLayout, SubLayouts]):
        if self.sublayouts._frozen_:
            raise ValueError("Can't add sublayouts to a frozen 'Layout' object")

        self.sublayouts += (
            other.sublayouts if isinstance(other, _Layout) else other
        )

        return self

    @overload
    def add_primitive(self, prim: prm._Primitive, *,
        origin: Optional[geo.Point]=None, x: None=None, y: None=None,
        rotation: geo.Rotation=geo.Rotation.R0,
        **prim_params,
    ) -> "_Layout":
        ... # pragma: no cover
    @overload
    def add_primitive(self, prim: prm._Primitive, *,
        origin: None=None, x: IntFloat, y: IntFloat,
        rotation: geo.Rotation=geo.Rotation.R0,
        **prim_params,
    ) -> "_Layout":
        ... # pragma: no cover
    def add_primitive(self, prim: prm._Primitive, *,
        origin: Optional[geo.Point]=None,
        x: Optional[IntFloat]=None, y: Optional[IntFloat]=None,
        rotation: geo.Rotation=geo.Rotation.R0,
        **prim_params,
    ) -> "_Layout":
        """Add the layout for a primitive to a layout. It uses the layout
        generated with `_Layout.layout_primitive()` and places it in the current
        layout at a specified location and with a specified rotation.

        Arguments:
            prim: the primitive for which the generate and place the layout
            prim_params: the parameters for the primitive
                This is passed to `_Layout.layout_primitive()`.
            origin or x, y: origin where to place the primitive layout
            rotation: the rotation to apply on the generated primitive layout
                before it is placed. By default no rotation is done.
        """
        if not (prim in self.fab.tech.primitives):
            raise ValueError(
                f"prim '{prim.name}' is not a primitive of technology"
                f" '{self.fab.tech.name}'"
            )
        # Translate possible x/y specification to origin
        if origin is None:
            x = 0.0 if x is None else _util.i2f(x)
            y = 0.0 if y is None else _util.i2f(y)
            origin = geo.Point(x=x, y=y)

        primlayout = self.fab.layout_primitive(prim, **prim_params)
        primlayout.rotate(rotation=rotation)
        primlayout.move(dxy=origin)
        self += primlayout
        return primlayout

    def add_maskshape(self, *, net: Optional[net_.Net]=None, maskshape: geo.MaskShape):
        """Add a geometry MaskShape to a _Layout

        This is a low-level layout manipulation method that does not do much checking.
        """
        for sl in self.sublayouts.__iter_type__(MaskShapesSubLayout):
            if sl.net == net:
                sl.add_shape(shape=maskshape)
                break
        else:
            self.sublayouts += MaskShapesSubLayout(
                net=net, shapes=geo.MaskShapes(maskshape),
            )

    def add_shape(self, *,
        prim: prm._DesignMaskPrimitive, net: Optional[net_.Net]=None, shape: geo._Shape,
    ):
        """Add a geometry _Shape to a _Layout

        This is a low-level layout manipulation method that does not do much checking.
        """
        self.add_maskshape(
            net=net,
            maskshape=geo.MaskShape(mask=cast(msk.DesignMask, prim.mask), shape=shape),
        )

    def move(self, *, dxy: geo.Point) -> None:
        """Move the shapes in the layout by the given displacement.
        This method changes the layout on which this method is called.

        Arguments:
            dxy: the displacement to apply to all the shapes in this layout
        """
        move_context = geo.MoveContext()
        for sl in self.sublayouts:
            sl.move(dxy=dxy, move_context=move_context)
        if self.boundary is not None:
            self.boundary += dxy

    def moved(self, *, dxy: geo.Point,
    ) -> "_Layout":
        """Return _Layout with all shapes moved by the given displacement.
        The original layout is not changed,

        Arguments:
            dxy: the displacement to apply to all the shapes in this layout
        """
        move_context = geo.MoveContext()

        if self.boundary is None:
            bound = None
        else:
            bound = self.boundary.moved(dxy=dxy, context=move_context)
        return _Layout(
            fab=self.fab, sublayouts=SubLayouts(
                sl.moved(dxy=dxy, move_context=move_context)
                for sl in self.sublayouts
            ),
            boundary=bound,
        )

    def rotate(self, *, rotation: geo.Rotation):
        """Rotate the shapes in the layout by the given rotation.
        This method changes the layout on which this method is called.

        Arguments:
            rotation: the rotation to apply to all the shapes in this layout
        """
        rot_context = geo.RotationContext()

        if self.boundary is not None:
            self.boundary = self.boundary.rotated(rotation=rotation, context=rot_context)
        self.sublayouts=SubLayouts(
            sl.rotated(rotation=rotation, rot_context=rot_context)
            for sl in self.sublayouts
        )

    def rotated(self, *, rotation: geo.Rotation):
        """Return _Layout with all shapes rotated by the given rotation.
        The original layout is not changed,

        Arguments:
            rotation: the rotation to apply to all the shapes in this layout
        """
        rot_context = geo.RotationContext()

        if self.boundary is None:
            bound = None
        else:
            bound = self.boundary.rotated(rotation=rotation, context=rot_context)
        return _Layout(
            fab=self.fab, sublayouts=SubLayouts(
                sl.rotated(rotation=rotation, rot_context=rot_context)
                for sl in self.sublayouts
            ),
            boundary=bound,
        )

    def freeze(self):
        """see: https://gitlab.com/Chips4Makers/PDKMaster/-/issues/37"""
        self.sublayouts._freeze_()

    @property
    def _hier_str_(self) -> str:
        """Return a string representing the full hierarchy of the layout.
        Indentation is used to represent the hierarchy.

        API Notes:
            This is for debuggin purposes only and user code should not depend
                on the exact format of this string.
        """
        return "\n  ".join(("layout:", *(s for s in self._hier_strs_)))

    @property
    def _hier_strs_(self) -> Generator[str, None, None]:
        for sl in self.sublayouts:
            yield from sl._hier_strs_

    def __eq__(self, other: Any):
        if isinstance(other, _Layout):
            return self.sublayouts == other.sublayouts
        else:
            return False


class _PrimitiveLayouter(dsp.PrimitiveDispatcher):
    """Support class to generate layout for a `_Primitive`.

    TODO: Proper docs after fixing the API.
    see https://gitlab.com/Chips4Makers/PDKMaster/-/issues/25

    API Notes:
        The API is not finalized yet; backwards incompatible changes are still
            expected.
    """
    def __init__(self, fab: "LayoutFactory"):
        self.fab = fab

    def __call__(self, prim: prm._Primitive, *args, **kwargs) -> _Layout:
        return super().__call__(prim, *args, **kwargs)

    @property
    def tech(self):
        return self.fab.tech

    # Dispatcher implementation
    def _Primitive(self, prim: prm._Primitive, **params):
        raise NotImplementedError(
            f"Don't know how to generate minimal layout for primitive '{prim.name}'\n"
            f"of type '{prim.__class__.__name__}'"
        )

    def Marker(self, prim: prm.Marker, **params) -> _Layout:
        if ("width" in params) and ("height" in params):
            return self._WidthSpacePrimitive(cast(prm._WidthSpacePrimitive, prim), **params)
        else:
            return super().Marker(prim, **params)

    def _WidthSpacePrimitive(self,
        prim: prm._WidthSpacePrimitive, **widthspace_params,
    ) -> _Layout:
        if len(prim.ports) != 0: # pragma: no cover
            raise NotImplementedError(
                f"Don't know how to generate minimal layout for primitive '{prim.name}'\n"
                f"of type '{prim.__class__.__name__}'"
            )
        width = widthspace_params["width"]
        height = widthspace_params["height"]
        r = geo.Rect.from_size(width=width, height=height)

        l = self.fab.new_layout()
        assert isinstance(prim, prm._DesignMaskPrimitive)
        l.add_shape(prim=prim, shape=r)
        return l

    def _WidthSpaceConductor(self,
        prim: prm._WidthSpaceConductor, **conductor_params,
    ) -> _Layout:
        assert (
            (len(prim.ports) == 1) and (prim.ports[0].name == "conn")
        ), "Internal error"
        width = conductor_params["width"]
        height = conductor_params["height"]
        r = geo.Rect.from_size(width=width, height=height)

        try:
            portnets = conductor_params["portnets"]
        except KeyError:
            net = prim.ports.conn
        else:
            net = portnets["conn"]

        layout = self.fab.new_layout()
        layout.add_shape(prim=prim, net=net, shape=r)
        pin = conductor_params.get("pin", None)
        if pin is not None:
            layout.add_shape(prim=pin, net=net, shape=r)

        return layout

    def WaferWire(self, prim: prm.WaferWire, **waferwire_params) -> _Layout:
        width = waferwire_params["width"]
        height = waferwire_params["height"]

        implant = waferwire_params.pop("implant")
        implant_enclosure = waferwire_params.pop("implant_enclosure")
        assert implant_enclosure is not None

        well = waferwire_params.pop("well", None)
        well_enclosure = waferwire_params.pop("well_enclosure", None)

        oxide = waferwire_params.pop("oxide", None)
        oxide_enclosure = waferwire_params.pop("oxide_enclosure", None)

        layout = self._WidthSpaceConductor(prim, **waferwire_params)
        layout.add_shape(prim=implant, shape=_rect(
            -0.5*width, -0.5*height, 0.5*width, 0.5*height,
            enclosure=implant_enclosure,
        ))
        if well is not None:
            try:
                well_net = waferwire_params["well_net"]
            except KeyError:
                raise TypeError(
                    f"No well_net given for WaferWire '{prim.name}' in well '{well.name}'"
                )
            layout.add_shape(prim=well, net=well_net, shape=_rect(
                -0.5*width, -0.5*height, 0.5*width, 0.5*height,
                enclosure=well_enclosure,
            ))
        if oxide is not None:
            layout.add_shape(prim=oxide, shape=_rect(
                -0.5*width, -0.5*height, 0.5*width, 0.5*height,
                enclosure=oxide_enclosure,
            ))
        return layout

    def MIMTop(self, prim: prm.MIMTop, **_):
        raise ValueError("No generation of MIMTop layer; use MIMCapacitor instead")

    def Via(self, prim: prm.Via, **via_params) -> _Layout:
        tech = self.tech

        try:
            portnets = via_params["portnets"]
        except KeyError:
            net = prim.ports["conn"]
        else:
            if set(portnets.keys()) != {"conn"}:
                raise ValueError(f"Via '{prim.name}' needs one net for the 'conn' port")
            net = portnets["conn"]

        bottom = via_params["bottom"]
        bottom_enc = via_params["bottom_enclosure"]
        if (bottom_enc is None) or isinstance(bottom_enc, str):
            idx = prim.bottom.index(bottom)
            enc = prim.min_bottom_enclosure[idx]
            if bottom_enc is None:
                bottom_enc = enc
            elif bottom_enc == "wide":
                bottom_enc = enc.wide()
            else:
                assert bottom_enc == "tall"
                bottom_enc = enc.tall()
        assert isinstance(bottom_enc, prp.Enclosure)
        bottom_enc_x = bottom_enc.spec[0]
        bottom_enc_y = bottom_enc.spec[1]

        top = via_params["top"]
        top_enc = via_params["top_enclosure"]
        if (top_enc is None) or isinstance(top_enc, str):
            idx = prim.top.index(top)
            enc = prim.min_top_enclosure[idx]
            if top_enc is None:
                top_enc = enc
            elif top_enc == "wide":
                top_enc = enc.wide()
            else:
                assert top_enc == "tall"
                top_enc = enc.tall()
        assert isinstance(top_enc, prp.Enclosure)
        top_enc_x = top_enc.spec[0]
        top_enc_y = top_enc.spec[1]

        width = prim.width
        space = via_params["space"]
        pitch = width + space

        rows = via_params["rows"]
        bottom_height = via_params["bottom_height"]
        top_height = via_params["top_height"]
        if rows is None:
            if bottom_height is None:
                assert top_height is not None
                rows = int(self.tech.on_grid(top_height - 2*top_enc_y - width)//pitch + 1)
                via_height = rows*pitch - space
                bottom_height = tech.on_grid(
                    via_height + 2*bottom_enc_y, mult=2, rounding="ceiling",
                )
            else:
                rows = int(self.tech.on_grid(bottom_height - 2*bottom_enc_y - width)//pitch + 1)
                if top_height is not None:
                    rows = min(
                        rows,
                        int(self.tech.on_grid(top_height - 2*top_enc_y - width)//pitch + 1),
                    )
                via_height = rows*pitch - space
                if top_height is None:
                    top_height = tech.on_grid(
                        via_height + 2*top_enc_y, mult=2, rounding="ceiling",
                    )
        else:
            assert (bottom_height is None) and (top_height is None)
            via_height = rows*pitch - space
            bottom_height = tech.on_grid(
                via_height + 2*bottom_enc_y, mult=2, rounding="ceiling",
            )
            top_height = tech.on_grid(
                via_height + 2*top_enc_y, mult=2, rounding="ceiling",
            )

        columns = via_params["columns"]
        bottom_width = via_params["bottom_width"]
        top_width = via_params["top_width"]
        if columns is None:
            if bottom_width is None:
                assert top_width is not None
                columns = int(self.tech.on_grid(top_width - 2*top_enc_x - width)//pitch + 1)
                via_width = columns*pitch - space
                bottom_width = tech.on_grid(
                    via_width + 2*bottom_enc_x, mult=2, rounding="ceiling",
                )
            else:
                columns = int(self.tech.on_grid(bottom_width - 2*bottom_enc_x - width)//pitch + 1)
                if top_width is not None:
                    columns = min(
                        columns,
                        int(self.tech.on_grid(top_width - 2*top_enc_x - width)//pitch + 1)
                    )
                via_width = columns*pitch - space
                if top_width is None:
                    top_width = tech.on_grid(
                        via_width + 2*top_enc_x, mult=2, rounding="ceiling",
                    )
        else:
            assert (bottom_width is None) and (top_width is None)
            via_width = columns*pitch - space
            bottom_width = tech.on_grid(
                via_width + 2*bottom_enc_x, mult=2, rounding="ceiling",
            )
            top_width = tech.on_grid(
                via_width + 2*top_enc_x, mult=2, rounding="ceiling",
            )

        bottom_left = tech.on_grid(-0.5*bottom_width, rounding="floor")
        bottom_bottom = tech.on_grid(-0.5*bottom_height, rounding="floor")
        bottom_right = bottom_left + bottom_width
        bottom_top = bottom_bottom + bottom_height
        bottom_rect = geo.Rect(
            left=bottom_left, bottom=bottom_bottom,
            right=bottom_right, top=bottom_top,
        )

        top_left = tech.on_grid(-0.5*top_width, rounding="floor")
        top_bottom = tech.on_grid(-0.5*top_height, rounding="floor")
        top_right = top_left + top_width
        top_top = top_bottom + top_height
        top_rect = geo.Rect(
            left=top_left, bottom=top_bottom,
            right=top_right, top=top_top,
        )

        via_bottom = tech.on_grid(-0.5*via_height)
        via_left = tech.on_grid(-0.5*via_width)

        layout = cast(_Layout, self.fab.new_layout())

        layout.add_shape(prim=bottom, net=net, shape=bottom_rect)
        layout.add_shape(prim=prim, net=net, shape=_via_array(
            via_left, via_bottom, width, pitch, rows, columns,
        ))
        layout.add_shape(prim=top, net=net, shape=top_rect)
        try:
            impl = via_params["bottom_implant"]
        except KeyError:
            impl = None
        else:
            if impl is not None:
                enc = cast(prp.Enclosure, via_params["bottom_implant_enclosure"])
                assert enc is not None, "Internal error"
                layout.add_shape(prim=impl, shape=geo.Rect.from_rect(
                    rect=bottom_rect, bias=enc,
                ))
        try:
            oxide = via_params["bottom_oxide"]
        except KeyError:
            oxide = None
        else:
            if oxide is not None:
                assert (
                    isinstance(bottom, prm.WaferWire) and (bottom.oxide is not None)
                    and (bottom.min_oxide_enclosure is not None)
                )
                enc = cast(prp.Enclosure, via_params["bottom_oxide_enclosure"])
                if enc is None:
                    idx = bottom.oxide.index(oxide)
                    enc = bottom.min_oxide_enclosure[idx]
                assert (enc is not None), "Unknown enclosure"
                layout.add_shape(prim=oxide, shape=geo.Rect.from_rect(
                    rect=bottom_rect, bias=enc,
                ))
        try:
            well = via_params["bottom_well"]
        except KeyError:
            well = None
        else:
            if well is not None:
                well_net = via_params.get("well_net", None)
                enc = via_params["bottom_well_enclosure"]
                assert enc is not None, "Internal error"
                if (impl is not None) and (impl.type_ == well.type_):
                    if well_net is not None:
                        if well_net != net:
                            raise ValueError(
                                f"Net '{well_net}' for well '{well.name}' of WaferWire"
                                f" {bottom.name} is different from net '{net}''\n"
                                f"\tbut implant '{impl.name}' is same type as the well"
                            )
                    else:
                        well_net = net
                elif well_net is None:
                    raise TypeError(
                        f"No well_net specified for WaferWire '{bottom.name}' in"
                        f" well '{well.name}'"
                    )
                layout.add_shape(prim=well, net=well_net, shape=geo.Rect.from_rect(
                    rect=bottom_rect, bias=enc,
                ))

        return layout

    def DeepWell(self, prim: prm.DeepWell, **deepwell_params) -> _Layout:
        raise NotImplementedError("layout generation for DeepWell primitive")

    def Resistor(self, prim: prm.Resistor, **resistor_params) -> _Layout:
        try:
            portnets = resistor_params["portnets"]
        except KeyError:
            port1 = prim.ports.port1
            port2 = prim.ports.port2
        else:
            if set(portnets.keys()) != {"port1", "port2"}:
                raise ValueError(
                    f"Resistor '{prim.name}' needs two port nets ('port1', 'port2')"
                )
            port1 = portnets["port1"]
            port2 = portnets["port2"]
        if prim.contact is None:
            raise NotImplementedError("Resistor layout without contact layer")

        res_width = resistor_params["width"]
        res_height = resistor_params["height"]

        wire = prim.wire

        cont = prim.contact
        cont_space = prim.min_contact_space
        assert cont_space is not None
        try:
            wire_idx = cont.bottom.index(wire)
        except ValueError: # pragma: no cover
            raise NotImplementedError("Resistor connected from the bottom")
            try:
                wire_idx = cont.top.index(wire)
            except ValueError:
                raise AssertionError("Internal error")
            else:
                cont_enc = cont.min_top_enclosure[wire_idx]
                cont_args = {"top": wire, "x": 0.0, "top_width": res_width}
        else:
            cont_enc = cont.min_bottom_enclosure[wire_idx]
            cont_args = {"bottom": wire, "x": 0.0, "bottom_width": res_width}
        if (prim.implant is not None) and isinstance(wire, prm.WaferWire):
            cont_args["bottom_implant"] = prim.implant
        cont_y1 = -0.5*res_height - cont_space - 0.5*cont.width
        cont_y2 = -cont_y1

        wire_ext = cont_space + cont.width + cont_enc.min()

        layout = self.fab.new_layout()

        # Draw indicator layers
        for idx, ind in enumerate(prim.indicator):
            ext = prim.min_indicator_extension[idx]
            layout += self(ind, width=(res_width + 2*ext), height=res_height)

        # Draw wire layer
        mp = geo.MultiPartShape(
            fullshape=geo.Rect.from_size(
                width=res_width, height=(res_height + 2*wire_ext),
            ),
            parts = (
                geo.Rect.from_floats(values=(
                    -0.5*res_width, -0.5*res_height - wire_ext,
                    0.5*res_width, -0.5*res_height,
                )),
                geo.Rect.from_floats(values=(
                    -0.5*res_width, -0.5*res_height,
                    0.5*res_width, 0.5*res_height,
                )),
                geo.Rect.from_floats(values=(
                    -0.5*res_width, 0.5*res_height,
                    0.5*res_width, 0.5*res_height + wire_ext,
                )),
            )
        )
        layout.add_shape(prim=wire, net=port1, shape=mp.parts[0])
        layout.add_shape(prim=wire, shape=mp.parts[1])
        layout.add_shape(prim=wire, net=port2, shape=mp.parts[2])

        # Draw contacts
        # Hack to make sure the bottom wire does not overlap with the resistor part
        # TODO: Should be fixed in MultiPartShape handling
        # layout.add_wire(net=port1, wire=cont, y=cont_y1, **cont_args)
        # layout.add_wire(net=port2, wire=cont, y=cont_y2, **cont_args)
        x = cont_args.pop("x")
        _l_cont = self.fab.layout_primitive(
            prim=cont, portnets={"conn": port1}, **cont_args
        )
        _l_cont.move(dxy=geo.Point(x=x, y=cont_y1))
        for sl in _l_cont.sublayouts:
            if isinstance(sl, MaskShapesSubLayout):
                for msl in sl.shapes:
                    if msl.mask == wire.mask:
                        assert isinstance(msl.shape, geo.Rect)
                        msl._shape = geo.Rect.from_rect(
                            rect=msl.shape, top=(-0.5*res_height - self.tech.grid)
                        )
        layout += _l_cont
        _l_cont = self.fab.layout_primitive(
            prim=cont, portnets={"conn": port2}, **cont_args
        )
        _l_cont.move(dxy=geo.Point(x=x, y=cont_y2))
        for sl in _l_cont.sublayouts:
            if isinstance(sl, MaskShapesSubLayout):
                for msl in sl.shapes:
                    if msl.mask == wire.mask:
                        assert isinstance(msl.shape, geo.Rect)
                        msl._shape = geo.Rect.from_rect(
                            rect=msl.shape, bottom=(0.5*res_height + self.tech.grid)
                        )
        layout += _l_cont

        if prim.implant is not None:
            impl = prim.implant
            try:
                enc = prim.min_implant_enclosure.max() # type: ignore
            except AttributeError:
                assert isinstance(wire, prm.WaferWire), "Internal error"
                idx = wire.implant.index(impl)
                enc = wire.min_implant_enclosure[idx].max()
            impl_width = res_width + 2*enc
            impl_height = res_height + 2*wire_ext + 2*enc
            layout.add_shape(prim=impl, shape=geo.Rect.from_size(width=impl_width, height=impl_height))

        return layout

    def MIMCapacitor(self, prim: prm.MIMCapacitor, **mimcapargs) -> _Layout:
        try:
            portnets = mimcapargs.pop("portnets")
        except KeyError:
            top = prim.ports.top
            bottom = prim.ports.bottom
        else:
            if set(portnets.keys()) != {"top", "bottom"}:
                raise ValueError(
                    f"MIMCapacitor '{prim.name}' needs two port nets ('top', 'bottom')"
                )
            top = portnets["top"]
            bottom = portnets["bottom"]

        via = prim.via

        # Params
        top_width = mimcapargs["width"]
        top_height = mimcapargs["height"]
        connect_up = mimcapargs["bottom_connect_up"]

        # TODO: Allow to specify top of the via layer
        upper_metal = via.top[0]
        assert isinstance(upper_metal, prm.MetalWire)
        assert upper_metal.pin is not None
        upper_pin = upper_metal.pin[0]

        # Compute dimensions
        if connect_up:
            bottomvia_outerwidth = (
                top_width + 2*prim.min_bottomvia_top_space + 2*via.width
            )
            bottomvia_outerheight = (
                top_height + 2*prim.min_bottomvia_top_space + 2*via.width
            )
            bottomvia_outerbound = geo.Rect.from_size(
                width=bottomvia_outerwidth, height=bottomvia_outerheight,
            )

            idx = via.bottom.index(prim.bottom)
            enc = via.min_bottom_enclosure[idx].max()
            bottom_width = bottomvia_outerwidth + 2*enc
            bottom_height = bottomvia_outerheight + 2*enc

            enc = via.min_top_enclosure[0].max()
            bottomupper_outerwidth = bottomvia_outerwidth + 2*enc
            bottomupper_outerheight = bottomvia_outerheight + 2*enc
            bottomupper_ringwidth = via.width + 2*enc

            topupper_width = (
                bottomupper_outerwidth - 2*bottomupper_ringwidth - 2*upper_metal.min_space
            )
            topupper_height = (
                bottomupper_outerheight - 2*bottomupper_ringwidth - 2*upper_metal.min_space
            )
        else:
            enc = prim.min_bottom_top_enclosure.max()
            bottom_width = top_width + 2*enc
            bottom_height = top_height + 2*enc

            topupper_width = None
            topupper_height = None

        # Draw the shapes
        layout = self.fab.new_layout()
        via_lay = layout.add_primitive(
            prim=via, bottom=prim.top, portnets={"conn": top},
            bottom_width=top_width, bottom_height=top_height,
            top_width=topupper_width, top_height=topupper_height,
            bottom_enclosure=prim.min_top_via_enclosure,
        )
        via_upmbb = via_lay.bounds(mask=upper_metal.mask)
        layout.add_shape(prim=upper_pin, net=top, shape=via_upmbb)

        shape = geo.Rect.from_size(width=bottom_width, height=bottom_height)
        layout.add_shape(prim=prim.bottom, net=bottom, shape=shape)

        if connect_up:
            shape = geo.RectRing(
                outer_bound=bottomvia_outerbound,
                rect_width=via.width, min_rect_space=via.min_space,
            )
            layout.add_shape(prim=via, net=bottom, shape=shape)

            shape = geo.Ring(
                outer_bound=geo.Rect.from_size(
                    width=bottomupper_outerwidth, height=bottomupper_outerheight,
                ),
                ring_width=bottomupper_ringwidth,
            )
            layout.add_shape(prim=upper_metal, net=bottom, shape=shape)
            layout.add_shape(prim=upper_pin, net=bottom, shape=shape)

        bottom_space = (
            prim.min_bottom_space
            if prim.min_bottom_space is not None
            else 0.0
        )
        layout.boundary = geo.Rect.from_size(
            width=(bottom_width + bottom_space),
            height=(bottom_height + bottom_space),
        )

        return layout

    def Diode(self, prim: prm.Diode, **diode_params) -> _Layout:
        try:
            portnets = diode_params.pop("portnets")
        except KeyError:
            an = prim.ports.anode
            cath = prim.ports.cathode
        else:
            if set(portnets.keys()) != {"anode", "cathode"}:
                raise ValueError(
                    f"Diode '{prim.name}' needs two port nets ('anode', 'cathode')"
                )
            an = portnets["anode"]
            cath = portnets["cathode"]

        wirenet_args = {
            "implant": prim.implant,
            "portnets": {"conn": an if prim.implant.type_ == "p" else cath},
        }
        if prim.min_implant_enclosure is not None:
            wirenet_args["implant_enclosure"] = prim.min_implant_enclosure
        if prim.well is not None:
            wirenet_args.update({
                "well": prim.well,
                "well_net": cath if prim.implant.type_ == "p" else an,
            })

        layout = self.fab.new_layout()
        layout.add_primitive(prim=prim.wire, **wirenet_args, **diode_params)
        wireact_bounds = layout.bounds(mask=prim.wire.mask)
        act_width = wireact_bounds.right - wireact_bounds.left
        act_height = wireact_bounds.top - wireact_bounds.bottom

        for i, ind in enumerate(prim.indicator):
            enc = prim.min_indicator_enclosure[i].max()
            layout += self(ind, width=(act_width + 2*enc), height=(act_height + 2*enc))

        return layout

    def MOSFET(self, prim: prm.MOSFET, **mos_params) -> _Layout:
        l = mos_params["l"]
        w = mos_params["w"]
        impl_enc = mos_params["activeimplant_enclosure"]
        gate_encs = mos_params["gateimplant_enclosures"]
        sdw = mos_params["sd_width"]

        try:
            portnets = cast(Mapping[str, net_.Net], mos_params["portnets"])
        except KeyError:
            portnets = prim.ports

        gate_left = -0.5*l
        gate_right = 0.5*l
        gate_top = 0.5*w
        gate_bottom = -0.5*w

        layout = self.fab.new_layout()

        active = prim.gate.active
        active_width = l + 2*sdw
        active_left = -0.5*active_width
        active_right = 0.5*active_width
        active_bottom = gate_bottom
        active_top = gate_top

        mps = geo.MultiPartShape(
            fullshape=geo.Rect.from_size(width=active_width, height=w),
            parts=(
                geo.Rect(
                    left=active_left, bottom=active_bottom,
                    right=gate_left, top=active_top,
                ),
                geo.Rect(
                    left=gate_left, bottom =active_bottom,
                    right=gate_right, top=active_top,
                ),
                geo.Rect(
                    left=gate_right, bottom =active_bottom,
                    right=active_right, top=active_top,
                ),
            )
        )
        layout.add_shape(prim=active, net=portnets["sourcedrain1"], shape=mps.parts[0])
        layout.add_shape(prim=active, net=portnets["bulk"], shape=mps.parts[1])
        layout.add_shape(prim=active, net=portnets["sourcedrain2"], shape=mps.parts[2])

        for impl in prim.implant:
            if impl in active.implant:
                layout.add_shape(prim=impl, shape=_rect(
                    active_left, active_bottom, active_right, active_top,
                    enclosure=impl_enc
                ))

        poly = prim.gate.poly
        ext = prim.computed.min_polyactive_extension
        poly_left = gate_left
        poly_bottom = gate_bottom - ext
        poly_right = gate_right
        poly_top = gate_top + ext
        layout.add_shape(prim=poly, net=portnets["gate"], shape=geo.Rect(
            left=poly_left, bottom=poly_bottom, right=poly_right, top=poly_top,
        ))

        if prim.well is not None:
            enc = active.min_well_enclosure[active.well.index(prim.well)]
            layout.add_shape(prim=prim.well, net=portnets["bulk"], shape=_rect(
                active_left, active_bottom, active_right, active_top, enclosure=enc,
            ))

        oxide = prim.gate.oxide
        if oxide is not None:
            assert (active.oxide is not None) and (active.min_oxide_enclosure is not None)
            enc = getattr(
                prim.gate, "min_gateoxide_enclosure", prp.Enclosure(self.tech.grid),
            )
            layout.add_shape(prim=oxide, shape=_rect(
                gate_left, gate_bottom, gate_right, gate_top, enclosure=enc,
            ))
            idx = active.oxide.index(oxide)
            enc = active.min_oxide_enclosure[idx]
            if enc is not None:
                layout.add_shape(prim=oxide, shape=_rect(
                    active_left, active_bottom, active_right, active_top,
                    enclosure=enc,
                ))
        if prim.gate.inside is not None:
            # TODO: Check is there is an enclosure rule from oxide around active
            # and apply the if so.
            for i, inside in enumerate(prim.gate.inside):
                enc = (
                    prim.gate.min_gateinside_enclosure[i]
                    if prim.gate.min_gateinside_enclosure is not None
                    else prp.Enclosure(self.tech.grid)
                )
                layout.add_shape(prim=inside, shape=_rect(
                    gate_left, gate_bottom, gate_right, gate_top, enclosure=enc,
                ))
        for i, impl in enumerate(prim.implant):
            enc = gate_encs[i]
            layout.add_shape(prim=impl, shape=_rect(
                gate_left, gate_bottom, gate_right, gate_top, enclosure=enc,
            ))

        return layout

    def Bipolar(self, prim: prm.Bipolar, **deepwell_params) -> _Layout:
        # Currently it is assumed that fixed layouts are provided by the
        # technology
        raise NotImplementedError("layout generation for Bipolar primitive")


class MOSFETInstSpec: # pragma: no cover
    """Class that provided the spec for the string of transistors generation.

    Used by `_CircuitLayouter.transistors_layout()`

    Arguments:
        inst: the transistor instance to generate layout for in the string.
            A ValueError will be raised in the it is not a MOSFET instance.
            The inst parameters like l, w, etc with determine the layout of the transistor.
        contact_left, contact_right: whether to place contacts left or right from the
            transistor. This value needs to be the same between two neighbours.

    API Notes:
        This class is deprecated and will be removed before v1.0.0. See also
        https://gitlab.com/Chips4Makers/PDKMaster/-/issues/25
    """
    def __init__(self, *,
        inst: ckt._PrimitiveInstance,
        contact_left: Optional[prm.Via], contact_right: Optional[prm.Via],
    ):
        self._inst = inst
        self._contact_left = contact_left
        self._contact_right = contact_right

        if not isinstance(inst.prim, prm.MOSFET):
            raise ValueError(f"inst is not a MOSFET instance")
        mosfet = inst.prim

        if contact_left is not None:
            if len(contact_left.top) != 1:
                raise NotImplementedError(
                    f"Multiple top layers for Via '{contact_left.name}'",
                )
        if contact_right is not None:
            if len(contact_right.top) != 1:
                raise NotImplementedError(
                    f"Multiple top layers for Via '{contact_right.name}'",
                )

        impls = tuple(filter(
            lambda impl: isinstance(impl, prm.Implant) and impl.type_ != "adjust",
            mosfet.implant,
        ))
        if len(impls) != 1:
            raise NotImplementedError(
                f"Multiple implant for MOSFET '{inst.prim.name}'",
            )
        self._implant = impls[0]

    @property
    def inst(self) -> ckt._PrimitiveInstance:
        return self._inst
    @property
    def contact_left(self) -> Optional[prm.Via]:
        return self._contact_left
    @property
    def contact_right(self) -> Optional[prm.Via]:
        return self._contact_right


class _CircuitLayouter: # pragma: no cover
    """_CircuitLayouter is deprecated class and undocumented.

    see https://gitlab.com/Chips4Makers/PDKMaster/-/issues/25 for development of
    replacement.

    API Notes:
        This class is deprecated and user code will fail in future.
    """
    def __init__(self, *,
        fab: "LayoutFactory", circuit: ckt._Circuit, boundary: Optional[geo._Rectangular]
    ):
        self.fab = fab
        self.circuit = circuit

        self.layout = l = fab.new_layout()
        l.boundary = boundary

    @property
    def tech(self) -> tch.Technology:
        return self.circuit.fab.tech

    def inst_layout(self, *,
        inst: ckt._Instance, layoutname: Optional[str]=None,
        rotation: geo.Rotation=geo.Rotation.R0,
    ) -> _Layout:
        if isinstance(inst, ckt._PrimitiveInstance):
            notfound = []
            portnets = {}
            for port in inst.ports:
                try:
                    net = self.circuit.net_lookup(port=port)
                except ValueError:
                    notfound.append(port.name)
                else:
                    portnets[port.name] = net
            if len(notfound) > 0:
                raise ValueError(
                    f"Unconnected port(s) {notfound}"
                    f" for inst '{inst.name}' of primitive '{inst.prim.name}'"
                )
            l = self.fab.layout_primitive(
                prim=inst.prim, portnets=portnets,
                **inst.params,
            )
            if rotation != geo.Rotation.R0:
                l.rotate(rotation=rotation)
            return l
        elif isinstance(inst, ckt._CellInstance):
            # TODO: propoer checking of nets for instance
            layout = None
            if layoutname is None:
                try:
                    circuitname = cast(Any, inst).circuitname
                    layout = inst.cell.layouts[circuitname]
                except:
                    layout = inst.cell.layout
                else:
                    layoutname = circuitname
            else:
                if not isinstance(layoutname, str):
                    raise TypeError(
                        "layoutname has to be 'None' or a string, not of type"
                        f" '{type(layoutname)}'"
                    )
                layout = inst.cell.layouts[layoutname]

            bb = None if layout.boundary is None else rotation*layout.boundary
            return _Layout(
                fab=self.fab,
                sublayouts=SubLayouts(_InstanceSubLayout(
                    inst=inst, origin=geo.origin, layoutname=layoutname,
                    rotation=rotation,
                )),
                boundary=bb,
            )
        else:
            raise AssertionError("Internal error")

    def wire_layout(self, *,
        net: ckt._CircuitNet, wire: prm._Primitive, **wire_params,
    ) -> _Layout:
        if net not in self.circuit.nets:
            raise ValueError(
                f"net '{net.name}' is not a net of circuit '{self.circuit.name}'"
            )
        if not (
            hasattr(wire, "ports")
            and (len(wire.ports) == 1)
            and (wire.ports[0].name == "conn")
        ):
            raise TypeError(
                f"Wire '{wire.name}' does not have exactly one port named 'conn'"
            )

        return self.fab.layout_primitive(
            wire, portnets={"conn": net}, **wire_params,
        )

    def transistors_layout(self, *,
        trans_specs: Iterable[MOSFETInstSpec]
    ) -> _Layout:
        """This method allows to generate a string of transistors.

        Arguments:
            trans_specs: the list of the spec for the transistors to generate. A
                `MOSFETInstSpec` object needs to be provided for each transistor of the
                striog. For more information refer to the `MOSFETInstSpec` reference.
                Some compatibility checks are done on the specification between the right
                specifation of a spec and the left specification of the next. Currently it
                is checked that whether to generata a contact is the same and if the active
                layer between the two transistors is the same.

        Results:
            The string of transistor according to the provided specs from left to right.
        """
        specs = tuple(trans_specs)

        # Check consistency of the specification
        for i, spec in enumerate(specs[:-1]):
            next_spec = specs[i+1]
            mosfet = cast(prm.MOSFET, spec.inst.prim)
            next_mosfet = cast(prm.MOSFET, next_spec.inst.prim)

            if spec.contact_right != next_spec.contact_left:
                raise ValueError(
                    f"Contact specification mismatch between transistor spec {i} and {i+1}",
                )
            if mosfet.gate.active != next_mosfet.gate.active:
                raise ValueError(
                    f"Active specification mismatch between transistor spec {i} and {i+1}",
                )

        # Create the layout

        layout = self.fab.new_layout()
        x = 0.0
        for i, spec in enumerate(specs):
            prev_spec = specs[i - 1] if (i > 0) else None
            next_spec = specs[i + 1] if (i < (len(specs) - 1)) else None
            mosfet = cast(prm.MOSFET, spec.inst.prim)

            # First generate, so the port net checks are run now.
            l_trans = self.inst_layout(inst=spec.inst)

            # Draw left sd
            if spec.contact_left is not None:
                w = spec.inst.params["w"]
                if prev_spec is not None:
                    w = min(w, prev_spec.inst.params["w"])
                if mosfet.well is None:
                    well_args = {}
                else:
                    well_args = {
                        "bottom_well": mosfet.well,
                        "well_net": spec.inst.ports["bulk"],
                    }
                if (i > 0):
                    # Add oxide layer on first contact
                    oxide_args = {}
                else:
                    oxide_args = {"bottom_oxide": mosfet.gate.oxide}
                l = self.wire_layout(
                    wire=spec.contact_left,
                    net=self.circuit.net_lookup(port=spec.inst.ports["sourcedrain1"]),
                    bottom_height=w, bottom=mosfet.gate.active,
                    bottom_implant=spec._implant, **oxide_args, **well_args,
                ).moved(dxy=geo.Point(x=x, y=0.0))
                layout += l
                x += (
                    0.5*spec.contact_left.width + spec.inst.params["contactgate_space"]
                    + 0.5*spec.inst.params["l"]
                )
            else:
                gate_space = spec.inst.params["gate_space"]
                if prev_spec is not None:
                    gate_space = max(gate_space, prev_spec.inst.params["gate_space"])
                x += 0.5*gate_space + 0.5*spec.inst.params["l"]

            # Remember trans position
            l_trans.move(dxy=geo.Point(x=x, y=0.0))
            layout += l_trans

            if spec.contact_right is not None:
                x += (
                    0.5*spec.inst.params["l"] + spec.inst.params["contactgate_space"]
                    + 0.5*spec.contact_right.width
                )
            else:
                gate_space = spec.inst.params["gate_space"]
                if next_spec is not None:
                    gate_space = max(gate_space, next_spec.inst.params["gate_space"])
                x += 0.5*spec.inst.params["l"] + 0.5*gate_space

        # Draw last contact if needed
        spec = specs[-1]
        if spec.contact_right is not None:
            mosfet = cast(prm.MOSFET, spec.inst.prim)
            if mosfet.well is None:
                well_args = {}
            else:
                well_args = {
                    "bottom_well": mosfet.well,
                    "well_net": spec.inst.ports["bulk"],
                }
            l = self.wire_layout(
                wire=spec.contact_right,
                net=self.circuit.net_lookup(port=spec.inst.ports["sourcedrain2"]),
                bottom_height=spec.inst.params["w"], bottom=mosfet.gate.active,
                bottom_implant=spec._implant, bottom_oxide=mosfet.gate.oxide, **well_args,
            ).moved(dxy=geo.Point(x=x, y=0.0))
            layout += l

        return layout

    @overload
    def place(self, object_: ckt._Instance, *,
        origin: geo.Point, x: None=None, y: None=None,
        layoutname: Optional[str]=None, rotation: geo.Rotation=geo.Rotation.R0,
    ) -> _Layout:
        ...
    @overload
    def place(self, object_: ckt._Instance, *,
        origin: None=None, x: IntFloat=0.0, y: IntFloat=0.0,
        layoutname: Optional[str]=None, rotation: geo.Rotation=geo.Rotation.R0,
    ) -> _Layout:
        ...
    @overload
    def place(self, object_: _Layout, *,
        origin: geo.Point, x: None=None, y: None=None,
        layoutname: Optional[str]=None, rotation: geo.Rotation=geo.Rotation.R0,
    ) -> _Layout:
        ...
    @overload
    def place(self, object_: _Layout, *,
        origin: None=None, x: IntFloat=0.0, y: IntFloat=0.0,
        layoutname: Optional[str]=None, rotation: geo.Rotation=geo.Rotation.R0,
    ) -> _Layout:
        ...
    def place(self, object_, *,
        origin=None, x: Optional[IntFloat]=None, y: Optional[IntFloat]=None,
        layoutname: Optional[str]=None, rotation: geo.Rotation=geo.Rotation.R0,
    ) -> _Layout:
        # Translate possible x/y specification to origin
        if origin is None:
            x = 0.0 if x is None else _util.i2f(x)
            y = 0.0 if y is None else _util.i2f(y)
            origin = geo.Point(x=x, y=y)

        if isinstance(object_, ckt._Instance):
            inst = object_
            if inst not in self.circuit.instances:
                raise ValueError(
                    f"inst '{inst.name}' is not part of circuit '{self.circuit.name}'"
                )

            if isinstance(inst, ckt._PrimitiveInstance):
                def _portnets():
                    for net in self.circuit.nets:
                        for port in net.childports:
                            if (inst == port.inst):
                                yield (port.name, net)
                portnets = dict(_portnets())
                portnames = set(inst.ports.keys())
                portnetnames = set(portnets.keys())
                if not (portnames == portnetnames):
                    raise ValueError(
                        f"Unconnected port(s) {portnames - portnetnames}"
                        f" for inst '{inst.name}' of primitive '{inst.prim.name}'"
                    )
                return self.layout.add_primitive(
                    prim=inst.prim, origin=origin, rotation=rotation,
                    portnets=portnets, **inst.params,
                )
            elif isinstance(inst, ckt._CellInstance):
                # TODO: propoer checking of nets for instance
                if (
                    (layoutname is None)
                    and inst.circuitname is not None
                    and (inst.circuitname in inst.cell.layouts.keys())
                ):
                    layoutname = inst.circuitname
                sl = _InstanceSubLayout(
                    inst=inst, origin=origin, layoutname=layoutname, rotation=rotation,
                )
                self.layout += sl

                return _Layout(
                    fab=self.fab, sublayouts=SubLayouts(sl), boundary=sl.boundary,
                )
            else:
                raise RuntimeError("Internal error: unsupported instance type")
        elif isinstance(object_, _Layout):
            layout = object_.rotated(rotation=rotation).moved(dxy=origin)
            self.layout += layout
            return layout
        else:
            raise AssertionError("Internal error")

    @overload
    def add_wire(self, *,
        net: net_.Net, wire: prm._Conductor, shape: Optional[geo._Shape]=None,
        origin: geo.Point, x: None=None, y: None=None,
        **wire_params,
    ) -> _Layout:
        ...
    @overload
    def add_wire(self, *,
        net: net_.Net, wire: prm._Conductor, shape: Optional[geo._Shape]=None,
        origin: None=None, x: Optional[IntFloat]=None, y: Optional[IntFloat]=None,
        **wire_params,
    ) -> _Layout:
        ...
    def add_wire(self, *,
        net: net_.Net, wire: prm._Conductor, shape: Optional[geo._Shape]=None,
        origin: Optional[geo.Point]=None, x: Optional[IntFloat]=None, y: Optional[IntFloat]=None,
        **wire_params,
    ) -> _Layout:
        if net not in self.circuit.nets:
            raise ValueError(
                f"net '{net.name}' is not a net of circuit '{self.circuit.name}'"
            )

        if origin is None:
            x = 0.0 if x is None else _util.i2f(x)
            y = 0.0 if y is None else _util.i2f(y)
            origin = geo.Point(x=x, y=y)

        if isinstance(wire, prm.Via):
            if shape is not None:
                raise ValueError(
                    "shape paramter may not be provided for a Via object"
                )
            return self._add_viawire(net=net, via=wire, origin=origin, **wire_params)

        layout = self.layout

        if (shape is None) or isinstance(shape, geo.Rect):
            if shape is not None:
                # TODO: Add support in _PrimitiveLayouter for shape argument,
                # e.g. non-rectangular shapes
                origin += shape.center
                wire_params.update({
                    "width": shape.width, "height": shape.height,
                })
            return layout.add_primitive(
                portnets={"conn": net}, prim=wire, origin=origin,
                **wire_params,
            )
        else: # (shape is not None) and not a Rect
            pin = wire_params.pop("pin", None)
            if len(wire_params) != 0:
                raise TypeError(
                    f"params {wire_params.keys()} not supported for shape not of type 'Rect'",
                )
            l = self.fab.new_layout()
            layout.add_shape(net=net, prim=wire, shape=shape)
            l.add_shape(net=net, prim=wire, shape=shape)
            if pin is not None:
                layout.add_shape(net=net, prim=pin, shape=shape)
                l.add_shape(net=net, prim=pin, shape=shape)
            return l

    def _add_viawire(self, *,
        net: net_.Net, via: prm.Via, origin: geo.Point, **via_params,
    ) -> _Layout:
        # For a Via allow to specify bottom and/or top edges
        has_rows = "rows" in via_params
        has_columns = "columns" in via_params

        def pop_param(name: str, type_, *, keep: bool=False):
            if keep:
                param = via_params.get(name, None)
            else:
                param = via_params.pop(name, None)
            return cast(Optional[type_], param)

        # Get bottom paramter specification
        bottom_left = pop_param("bottom_left", float)
        bottom_bottom = pop_param("bottom_bottom", float)
        bottom_right = pop_param("bottom_right", float)
        bottom_top = pop_param("bottom_top", float)
        has_bottomedge = (
            (bottom_left is not None) or (bottom_bottom is not None)
            or (bottom_right is not None) or (bottom_top is not None)
        )

        bottom_shape = pop_param("bottom_shape", geo._Shape)
        if bottom_shape is not None:
            if has_bottomedge:
                raise ValueError(
                    "Both bottom_shape and at least one of bottom_left, bottom_bottom"
                    ", bottom_rigth or bottom_top specified"
                )
            if not isinstance(bottom_shape, geo.Rect):
                raise NotImplementedError(
                    f"bottom_shape not a 'Rect' but of type '{type(bottom_shape)}'"
                )

            bottom_left = bottom_shape.left
            bottom_bottom = bottom_shape.bottom
            bottom_right = bottom_shape.right
            bottom_top = bottom_shape.top
            has_bottomedge = True

        bottom = pop_param("bottom", prm.ViaBottom, keep=True)
        if bottom is None:
            bottom = via.bottom[0]
        assert not isinstance(bottom, prm.Resistor), "Unimplemented"

        bottom_enc = pop_param(
            "bottom_enclosure", Union[str, float, prp.Enclosure], keep=True,
        )
        if isinstance(bottom_enc, float):
            bottom_enc = prp.Enclosure(bottom_enc)
        if (bottom_enc is None) or isinstance(bottom_enc, str):
            idx = via.bottom.index(bottom)
            enc = via.min_bottom_enclosure[idx]
            if bottom_enc is None:
                bottom_enc = enc
            elif bottom_enc == "wide":
                bottom_enc = enc.wide()
            else:
                assert bottom_enc == "tall"
                bottom_enc = enc.tall()
        bottom_henc = bottom_enc.first
        bottom_venc = bottom_enc.second

        # Get bottom paramter specification
        top = pop_param("top", prm.ViaBottom, keep=True)
        if top is None:
            top = via.top[0]
        assert not isinstance(top, prm.Resistor), "Unimplemented"

        top_left = pop_param("top_left", float)
        top_bottom = pop_param("top_bottom", float)
        top_right = pop_param("top_right", float)
        top_top = pop_param("top_top", float)
        has_topedge = (
            (top_left is not None) or (top_bottom is not None)
            or (top_right is not None) or (top_top is not None)
        )

        top_shape = pop_param("top_shape", geo._Shape)
        if top_shape is not None:
            if has_topedge:
                raise ValueError(
                    "Both top_shape and at least one of top_left, top_bottom"
                    ", top_rigth or top_top specified"
                )
            if not isinstance(top_shape, geo.Rect):
                raise NotImplementedError(
                    f"top_shape not a 'Rect' but of type '{type(top_shape)}'"
                )

            top_left = top_shape.left
            top_bottom = top_shape.bottom
            top_right = top_shape.right
            top_top = top_shape.top
            has_topedge = True

        top_enc = pop_param(
            "top_enclosure", Union[str, float, prp.Enclosure], keep=True,
        )
        if isinstance(top_enc, float):
            top_enc = prp.Enclosure(top_enc)
        if (top_enc is None) or isinstance(top_enc, str):
            idx = via.top.index(top)
            enc = via.min_top_enclosure[idx]
            if top_enc is None:
                top_enc = enc
            elif top_enc == "wide":
                top_enc = enc.wide()
            else:
                assert top_enc == "tall"
                top_enc = enc.tall()
        top_henc = top_enc.first
        top_venc = top_enc.second

        if has_bottomedge or has_topedge:
            width = via.width
            space = pop_param("space", float, keep=True)
            if space is None:
                space = via.min_space
            pitch = width + space

            # Compute number of rows/columns and placement
            if bottom_left is not None:
                if top_left is not None:
                    via_left = max(bottom_left + bottom_henc, top_left + top_henc)
                else:
                    via_left = bottom_left + bottom_henc
            else:
                if top_left is not None:
                    via_left = top_left + top_henc
                else:
                    via_left = None
            if bottom_bottom is not None:
                if top_bottom is not None:
                    via_bottom = max(bottom_bottom + bottom_venc, top_bottom + top_venc)
                else:
                    via_bottom = bottom_bottom + bottom_henc
            else:
                if top_bottom is not None:
                    via_bottom = top_bottom + top_venc
                else:
                    via_bottom = None
            if bottom_right is not None:
                if top_right is not None:
                    via_right = min(bottom_right - bottom_henc, top_right - top_henc)
                else:
                    via_right = bottom_right - bottom_henc
            else:
                if top_right is not None:
                    via_right = top_right + top_henc
                else:
                    via_right = None
            if bottom_top is not None:
                if top_top is not None:
                    via_top = min(bottom_top - bottom_venc, top_top - top_venc)
                else:
                    via_top = bottom_top - bottom_venc
            else:
                if top_top is not None:
                    via_top = top_top + top_venc
                else:
                    via_top = None

            if (via_left is None) != (via_right is None):
                raise NotImplementedError(
                    "left or right edge specification of Via but not both"
                )
            if (via_bottom is None) != (via_top is None):
                raise NotImplementedError(
                    "bottom or top edge specification of Via but not both"
                )

            via_x = 0.0
            if (via_left is not None) and (via_right is not None):
                if has_columns:
                    raise ValueError(
                        "Via left/right edge together with columns specifcation"
                    )
                w = self.tech.on_grid(via_right - via_left, mult=2)
                columns = int((w - width)/pitch) + 1
                if columns < 1:
                    raise ValueError("Not enough width for fitting one column")
                via_x = self.tech.on_grid((via_left + via_right)/2.0)
                via_params["columns"] = columns

            via_y = 0.0
            if (via_bottom is not None) and (via_top is not None):
                if has_rows:
                    raise ValueError(
                        "Via bottom/top edge together with rows specifcation"
                    )
                h = self.tech.on_grid(via_top - via_bottom, mult=2)
                rows = int((h - width)/pitch) + 1
                if rows < 1:
                    raise ValueError("Not enough height for fitting one row")
                via_y =  self.tech.on_grid((via_bottom + via_top)/2.0)
                via_params["rows"] = rows

            origin += geo.Point(x=via_x, y=via_y)

        via_lay = self.fab.layout_primitive(
            portnets={"conn": net}, prim=via, **via_params,
        )
        via_lay.move(dxy=origin)

        draw = False
        shape = via_lay.bounds(mask=top.mask)
        if top_left is not None:
            shape = geo.Rect.from_rect(rect=shape, left=top_left)
            draw = True
        if top_bottom is not None:
            shape = geo.Rect.from_rect(rect=shape, bottom=top_bottom)
            draw = True
        if top_right is not None:
            shape = geo.Rect.from_rect(rect=shape, right=top_right)
            draw = True
        if top_top is not None:
            shape = geo.Rect.from_rect(rect=shape, top=top_top)
            draw = True
        if draw:
            via_lay.add_shape(prim=top, net=net, shape=shape)
        self.layout += via_lay

        draw = False
        shape = via_lay.bounds(mask=bottom.mask)
        if bottom_left is not None:
            shape = geo.Rect.from_rect(rect=shape, left=bottom_left)
            draw = True
        if bottom_bottom is not None:
            shape = geo.Rect.from_rect(rect=shape, bottom=bottom_bottom)
            draw = True
        if bottom_right is not None:
            shape = geo.Rect.from_rect(rect=shape, right=bottom_right)
            draw = True
        if bottom_top is not None:
            shape = geo.Rect.from_rect(rect=shape, top=bottom_top)
            draw = True
        if draw:
            kwargs = {}
            if "bottom_implant" in via_params:
                kwargs["implant"] = via_params["bottom_implant"]
            if "bottom_well" in via_params:
                kwargs["well"] = via_params["bottom_well"]
                kwargs["well_net"] = via_params["well_net"]
            l = self.add_wire(wire=bottom, net=net, shape=shape, **kwargs)
            via_lay += l

        return via_lay

    def add_portless(self, *,
        prim: prm._DesignMaskPrimitive, shape: Optional[geo._Shape]=None, **prim_params,
    ):
        if len(prim.ports) > 0:
            raise ValueError(
                f"prim '{prim.name}' should not have any port"
            )

        if shape is None:
            return self.layout.add_primitive(prim=prim, **prim_params)
        else:
            if len(prim_params) != 0:
                raise ValueError(
                    f"Parameters '{tuple(prim_params.keys())}' not supported for shape not 'None'",
                )
            self.layout.add_shape(prim=prim, net=None, shape=shape)


class LayoutFactory:
    """The user facing class for creating layouts. This class is also a base
    class on which own factory classes can be built with specific extensions.

    Parameters:
        tech: the technology for which to create circuits. Created layout may
            only contain shapes on masks defined by the technology.

    API Notes:
        The contract for making subclasses has not been finaziled. Backwards
            incompatible changes are still expected for subclasses of this class.
    """
    def __init__(self, *, tech: tch.Technology):
        self.tech = tech
        self.gen_primlayout = _PrimitiveLayouter(self)

    def new_layout(self, *,
        sublayouts: Optional[Union[_SubLayout, SubLayouts]]=None,
        boundary: Optional[geo._Rectangular]=None,
    ):
        """Create a new layout.

        Arguments:
            sublayouts: optional list of sublayouts to add to this new layout
            boundary: optional boundary of the new layout
        """
        if sublayouts is None:
            sublayouts = SubLayouts()
        if isinstance(sublayouts, _SubLayout):
            sublayouts = SubLayouts(sublayouts)

        return _Layout(fab=self, sublayouts=sublayouts, boundary=boundary)

    def layout_primitive(self, prim: prm._Primitive, **prim_params) -> _Layout:
        """Create the layout of a `_Primitive` object.

        This will generate a default layout for a given primitive with the
        provided paramters. This is a default layout

        Arguments:
            prim: the primitive to create a layout for
            prim_params: the parameters for the primitive

        API Notes:
            User code can't depend on the exact layout generated for a certain
                primitive. Future improvements to the layout generation code
                may change the resulting layout.
        """
        prim_params = prim.cast_params(prim_params)
        return self.gen_primlayout(prim, **prim_params)

    def new_circuitlayouter(self, *,
        circuit:ckt._Circuit, boundary: Optional[geo._Rectangular],
    ) -> _CircuitLayouter:
        """Helper class to generate layout corresponding to a given `_Circuit`.
        The returned layouter will start with an empty layout with optionally a
        provided boundary. The layouter API can then be used to build up the
        layout for the circuit.

        Arguments:
            circuit: the circuit for which to create a layouter
            boundary: optional boundary of the created layout

        API Notes:
            The API of the returned layouter is not fixed yet and backwards
            incompatible changes are still expected.
        """
        return _CircuitLayouter(fab=self, circuit=circuit, boundary=boundary)
