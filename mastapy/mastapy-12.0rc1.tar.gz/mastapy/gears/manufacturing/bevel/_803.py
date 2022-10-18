"""_803.py

PinionRoughMachineSetting
"""


from mastapy._internal import constructor
from mastapy.gears.gear_designs.conical import _1146
from mastapy.gears.gear_designs.zerol_bevel import _947
from mastapy._internal.cast_exception import CastException
from mastapy.gears.gear_designs.straight_bevel import _956
from mastapy.gears.gear_designs.straight_bevel_diff import _960
from mastapy.gears.gear_designs.spiral_bevel import _964
from mastapy.gears.gear_designs.klingelnberg_spiral_bevel import _968
from mastapy.gears.gear_designs.klingelnberg_hypoid import _972
from mastapy.gears.gear_designs.klingelnberg_conical import _976
from mastapy.gears.gear_designs.hypoid import _980
from mastapy.gears.gear_designs.bevel import _1172
from mastapy.gears.gear_designs.agma_gleason_conical import _1185
from mastapy.gears.manufacturing.bevel import _781
from mastapy import _0
from mastapy._internal.python_net import python_net_import

_PINION_ROUGH_MACHINE_SETTING = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Bevel', 'PinionRoughMachineSetting')


__docformat__ = 'restructuredtext en'
__all__ = ('PinionRoughMachineSetting',)


class PinionRoughMachineSetting(_0.APIBase):
    """PinionRoughMachineSetting

    This is a mastapy class.
    """

    TYPE = _PINION_ROUGH_MACHINE_SETTING

    def __init__(self, instance_to_wrap: 'PinionRoughMachineSetting.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def absolute_increment_in_machine_centre_to_back(self) -> 'float':
        """float: 'AbsoluteIncrementInMachineCentreToBack' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AbsoluteIncrementInMachineCentreToBack

        if temp is None:
            return 0.0

        return temp

    @property
    def blank_offset(self) -> 'float':
        """float: 'BlankOffset' is the original name of this property."""

        temp = self.wrapped.BlankOffset

        if temp is None:
            return 0.0

        return temp

    @blank_offset.setter
    def blank_offset(self, value: 'float'):
        self.wrapped.BlankOffset = float(value) if value else 0.0

    @property
    def cone_distance_of_reference_point(self) -> 'float':
        """float: 'ConeDistanceOfReferencePoint' is the original name of this property."""

        temp = self.wrapped.ConeDistanceOfReferencePoint

        if temp is None:
            return 0.0

        return temp

    @cone_distance_of_reference_point.setter
    def cone_distance_of_reference_point(self, value: 'float'):
        self.wrapped.ConeDistanceOfReferencePoint = float(value) if value else 0.0

    @property
    def height_of_reference_point(self) -> 'float':
        """float: 'HeightOfReferencePoint' is the original name of this property."""

        temp = self.wrapped.HeightOfReferencePoint

        if temp is None:
            return 0.0

        return temp

    @height_of_reference_point.setter
    def height_of_reference_point(self, value: 'float'):
        self.wrapped.HeightOfReferencePoint = float(value) if value else 0.0

    @property
    def increment_of_pinion_workpiece_mounting_distance(self) -> 'float':
        """float: 'IncrementOfPinionWorkpieceMountingDistance' is the original name of this property."""

        temp = self.wrapped.IncrementOfPinionWorkpieceMountingDistance

        if temp is None:
            return 0.0

        return temp

    @increment_of_pinion_workpiece_mounting_distance.setter
    def increment_of_pinion_workpiece_mounting_distance(self, value: 'float'):
        self.wrapped.IncrementOfPinionWorkpieceMountingDistance = float(value) if value else 0.0

    @property
    def minimum_allowed_finish_stock(self) -> 'float':
        """float: 'MinimumAllowedFinishStock' is the original name of this property."""

        temp = self.wrapped.MinimumAllowedFinishStock

        if temp is None:
            return 0.0

        return temp

    @minimum_allowed_finish_stock.setter
    def minimum_allowed_finish_stock(self, value: 'float'):
        self.wrapped.MinimumAllowedFinishStock = float(value) if value else 0.0

    @property
    def spiral_angle_at_reference_point(self) -> 'float':
        """float: 'SpiralAngleAtReferencePoint' is the original name of this property."""

        temp = self.wrapped.SpiralAngleAtReferencePoint

        if temp is None:
            return 0.0

        return temp

    @spiral_angle_at_reference_point.setter
    def spiral_angle_at_reference_point(self, value: 'float'):
        self.wrapped.SpiralAngleAtReferencePoint = float(value) if value else 0.0

    @property
    def gear_set(self) -> '_1146.ConicalGearSetDesign':
        """ConicalGearSetDesign: 'GearSet' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearSet

        if temp is None:
            return None

        if _1146.ConicalGearSetDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_set to ConicalGearSetDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_set_of_type_zerol_bevel_gear_set_design(self) -> '_947.ZerolBevelGearSetDesign':
        """ZerolBevelGearSetDesign: 'GearSet' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearSet

        if temp is None:
            return None

        if _947.ZerolBevelGearSetDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_set to ZerolBevelGearSetDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_set_of_type_straight_bevel_gear_set_design(self) -> '_956.StraightBevelGearSetDesign':
        """StraightBevelGearSetDesign: 'GearSet' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearSet

        if temp is None:
            return None

        if _956.StraightBevelGearSetDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_set to StraightBevelGearSetDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_set_of_type_straight_bevel_diff_gear_set_design(self) -> '_960.StraightBevelDiffGearSetDesign':
        """StraightBevelDiffGearSetDesign: 'GearSet' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearSet

        if temp is None:
            return None

        if _960.StraightBevelDiffGearSetDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_set to StraightBevelDiffGearSetDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_set_of_type_spiral_bevel_gear_set_design(self) -> '_964.SpiralBevelGearSetDesign':
        """SpiralBevelGearSetDesign: 'GearSet' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearSet

        if temp is None:
            return None

        if _964.SpiralBevelGearSetDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_set to SpiralBevelGearSetDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_set_of_type_klingelnberg_cyclo_palloid_spiral_bevel_gear_set_design(self) -> '_968.KlingelnbergCycloPalloidSpiralBevelGearSetDesign':
        """KlingelnbergCycloPalloidSpiralBevelGearSetDesign: 'GearSet' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearSet

        if temp is None:
            return None

        if _968.KlingelnbergCycloPalloidSpiralBevelGearSetDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_set to KlingelnbergCycloPalloidSpiralBevelGearSetDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_set_of_type_klingelnberg_cyclo_palloid_hypoid_gear_set_design(self) -> '_972.KlingelnbergCycloPalloidHypoidGearSetDesign':
        """KlingelnbergCycloPalloidHypoidGearSetDesign: 'GearSet' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearSet

        if temp is None:
            return None

        if _972.KlingelnbergCycloPalloidHypoidGearSetDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_set to KlingelnbergCycloPalloidHypoidGearSetDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_set_of_type_klingelnberg_conical_gear_set_design(self) -> '_976.KlingelnbergConicalGearSetDesign':
        """KlingelnbergConicalGearSetDesign: 'GearSet' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearSet

        if temp is None:
            return None

        if _976.KlingelnbergConicalGearSetDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_set to KlingelnbergConicalGearSetDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_set_of_type_hypoid_gear_set_design(self) -> '_980.HypoidGearSetDesign':
        """HypoidGearSetDesign: 'GearSet' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearSet

        if temp is None:
            return None

        if _980.HypoidGearSetDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_set to HypoidGearSetDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_set_of_type_bevel_gear_set_design(self) -> '_1172.BevelGearSetDesign':
        """BevelGearSetDesign: 'GearSet' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearSet

        if temp is None:
            return None

        if _1172.BevelGearSetDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_set to BevelGearSetDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_set_of_type_agma_gleason_conical_gear_set_design(self) -> '_1185.AGMAGleasonConicalGearSetDesign':
        """AGMAGleasonConicalGearSetDesign: 'GearSet' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearSet

        if temp is None:
            return None

        if _1185.AGMAGleasonConicalGearSetDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_set to AGMAGleasonConicalGearSetDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def pinion_config(self) -> '_781.ConicalPinionManufacturingConfig':
        """ConicalPinionManufacturingConfig: 'PinionConfig' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PinionConfig

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None
