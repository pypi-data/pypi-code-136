"""_2467.py

BevelDifferentialGearSet
"""


from typing import List

from mastapy.gears.gear_designs.bevel import _1172
from mastapy._internal import constructor, conversion
from mastapy.gears.gear_designs.zerol_bevel import _947
from mastapy._internal.cast_exception import CastException
from mastapy.gears.gear_designs.straight_bevel import _956
from mastapy.gears.gear_designs.straight_bevel_diff import _960
from mastapy.gears.gear_designs.spiral_bevel import _964
from mastapy.system_model.part_model.gears import _2470, _2471
from mastapy.system_model.connections_and_sockets.gears import _2255
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_GEAR_SET = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'BevelDifferentialGearSet')


__docformat__ = 'restructuredtext en'
__all__ = ('BevelDifferentialGearSet',)


class BevelDifferentialGearSet(_2471.BevelGearSet):
    """BevelDifferentialGearSet

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_GEAR_SET

    def __init__(self, instance_to_wrap: 'BevelDifferentialGearSet.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def conical_gear_set_design(self) -> '_1172.BevelGearSetDesign':
        """BevelGearSetDesign: 'ConicalGearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConicalGearSetDesign

        if temp is None:
            return None

        if _1172.BevelGearSetDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast conical_gear_set_design to BevelGearSetDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def conical_gear_set_design_of_type_zerol_bevel_gear_set_design(self) -> '_947.ZerolBevelGearSetDesign':
        """ZerolBevelGearSetDesign: 'ConicalGearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConicalGearSetDesign

        if temp is None:
            return None

        if _947.ZerolBevelGearSetDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast conical_gear_set_design to ZerolBevelGearSetDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def conical_gear_set_design_of_type_straight_bevel_gear_set_design(self) -> '_956.StraightBevelGearSetDesign':
        """StraightBevelGearSetDesign: 'ConicalGearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConicalGearSetDesign

        if temp is None:
            return None

        if _956.StraightBevelGearSetDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast conical_gear_set_design to StraightBevelGearSetDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def conical_gear_set_design_of_type_straight_bevel_diff_gear_set_design(self) -> '_960.StraightBevelDiffGearSetDesign':
        """StraightBevelDiffGearSetDesign: 'ConicalGearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConicalGearSetDesign

        if temp is None:
            return None

        if _960.StraightBevelDiffGearSetDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast conical_gear_set_design to StraightBevelDiffGearSetDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def conical_gear_set_design_of_type_spiral_bevel_gear_set_design(self) -> '_964.SpiralBevelGearSetDesign':
        """SpiralBevelGearSetDesign: 'ConicalGearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConicalGearSetDesign

        if temp is None:
            return None

        if _964.SpiralBevelGearSetDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast conical_gear_set_design to SpiralBevelGearSetDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bevel_gear_set_design(self) -> '_1172.BevelGearSetDesign':
        """BevelGearSetDesign: 'BevelGearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BevelGearSetDesign

        if temp is None:
            return None

        if _1172.BevelGearSetDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast bevel_gear_set_design to BevelGearSetDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bevel_gear_set_design_of_type_zerol_bevel_gear_set_design(self) -> '_947.ZerolBevelGearSetDesign':
        """ZerolBevelGearSetDesign: 'BevelGearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BevelGearSetDesign

        if temp is None:
            return None

        if _947.ZerolBevelGearSetDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast bevel_gear_set_design to ZerolBevelGearSetDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bevel_gear_set_design_of_type_straight_bevel_gear_set_design(self) -> '_956.StraightBevelGearSetDesign':
        """StraightBevelGearSetDesign: 'BevelGearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BevelGearSetDesign

        if temp is None:
            return None

        if _956.StraightBevelGearSetDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast bevel_gear_set_design to StraightBevelGearSetDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bevel_gear_set_design_of_type_straight_bevel_diff_gear_set_design(self) -> '_960.StraightBevelDiffGearSetDesign':
        """StraightBevelDiffGearSetDesign: 'BevelGearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BevelGearSetDesign

        if temp is None:
            return None

        if _960.StraightBevelDiffGearSetDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast bevel_gear_set_design to StraightBevelDiffGearSetDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bevel_gear_set_design_of_type_spiral_bevel_gear_set_design(self) -> '_964.SpiralBevelGearSetDesign':
        """SpiralBevelGearSetDesign: 'BevelGearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BevelGearSetDesign

        if temp is None:
            return None

        if _964.SpiralBevelGearSetDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast bevel_gear_set_design to SpiralBevelGearSetDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bevel_gears(self) -> 'List[_2470.BevelGear]':
        """List[BevelGear]: 'BevelGears' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BevelGears

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def bevel_meshes(self) -> 'List[_2255.BevelGearMesh]':
        """List[BevelGearMesh]: 'BevelMeshes' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BevelMeshes

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value
