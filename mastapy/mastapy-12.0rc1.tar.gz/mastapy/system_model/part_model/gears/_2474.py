"""_2474.py

ConicalGear
"""


from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy.system_model.part_model.gears import _2482, _2481
from mastapy.gears.gear_designs.conical import _1144
from mastapy.gears.gear_designs.zerol_bevel import _945
from mastapy._internal.cast_exception import CastException
from mastapy.gears.gear_designs.straight_bevel import _954
from mastapy.gears.gear_designs.straight_bevel_diff import _958
from mastapy.gears.gear_designs.spiral_bevel import _962
from mastapy.gears.gear_designs.klingelnberg_spiral_bevel import _966
from mastapy.gears.gear_designs.klingelnberg_hypoid import _970
from mastapy.gears.gear_designs.klingelnberg_conical import _974
from mastapy.gears.gear_designs.hypoid import _978
from mastapy.gears.gear_designs.bevel import _1170
from mastapy.gears.gear_designs.agma_gleason_conical import _1183
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'ConicalGear')


__docformat__ = 'restructuredtext en'
__all__ = ('ConicalGear',)


class ConicalGear(_2481.Gear):
    """ConicalGear

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR

    def __init__(self, instance_to_wrap: 'ConicalGear.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def length(self) -> 'float':
        """float: 'Length' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Length

        if temp is None:
            return 0.0

        return temp

    @property
    def orientation(self) -> '_2482.GearOrientations':
        """GearOrientations: 'Orientation' is the original name of this property."""

        temp = self.wrapped.Orientation

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp)
        return constructor.new_from_mastapy_type(_2482.GearOrientations)(value) if value is not None else None

    @orientation.setter
    def orientation(self, value: '_2482.GearOrientations'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.Orientation = value

    @property
    def active_gear_design(self) -> '_1144.ConicalGearDesign':
        """ConicalGearDesign: 'ActiveGearDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ActiveGearDesign

        if temp is None:
            return None

        if _1144.ConicalGearDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast active_gear_design to ConicalGearDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def active_gear_design_of_type_zerol_bevel_gear_design(self) -> '_945.ZerolBevelGearDesign':
        """ZerolBevelGearDesign: 'ActiveGearDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ActiveGearDesign

        if temp is None:
            return None

        if _945.ZerolBevelGearDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast active_gear_design to ZerolBevelGearDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def active_gear_design_of_type_straight_bevel_gear_design(self) -> '_954.StraightBevelGearDesign':
        """StraightBevelGearDesign: 'ActiveGearDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ActiveGearDesign

        if temp is None:
            return None

        if _954.StraightBevelGearDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast active_gear_design to StraightBevelGearDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def active_gear_design_of_type_straight_bevel_diff_gear_design(self) -> '_958.StraightBevelDiffGearDesign':
        """StraightBevelDiffGearDesign: 'ActiveGearDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ActiveGearDesign

        if temp is None:
            return None

        if _958.StraightBevelDiffGearDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast active_gear_design to StraightBevelDiffGearDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def active_gear_design_of_type_spiral_bevel_gear_design(self) -> '_962.SpiralBevelGearDesign':
        """SpiralBevelGearDesign: 'ActiveGearDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ActiveGearDesign

        if temp is None:
            return None

        if _962.SpiralBevelGearDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast active_gear_design to SpiralBevelGearDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def active_gear_design_of_type_klingelnberg_cyclo_palloid_spiral_bevel_gear_design(self) -> '_966.KlingelnbergCycloPalloidSpiralBevelGearDesign':
        """KlingelnbergCycloPalloidSpiralBevelGearDesign: 'ActiveGearDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ActiveGearDesign

        if temp is None:
            return None

        if _966.KlingelnbergCycloPalloidSpiralBevelGearDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast active_gear_design to KlingelnbergCycloPalloidSpiralBevelGearDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def active_gear_design_of_type_klingelnberg_cyclo_palloid_hypoid_gear_design(self) -> '_970.KlingelnbergCycloPalloidHypoidGearDesign':
        """KlingelnbergCycloPalloidHypoidGearDesign: 'ActiveGearDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ActiveGearDesign

        if temp is None:
            return None

        if _970.KlingelnbergCycloPalloidHypoidGearDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast active_gear_design to KlingelnbergCycloPalloidHypoidGearDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def active_gear_design_of_type_klingelnberg_conical_gear_design(self) -> '_974.KlingelnbergConicalGearDesign':
        """KlingelnbergConicalGearDesign: 'ActiveGearDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ActiveGearDesign

        if temp is None:
            return None

        if _974.KlingelnbergConicalGearDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast active_gear_design to KlingelnbergConicalGearDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def active_gear_design_of_type_hypoid_gear_design(self) -> '_978.HypoidGearDesign':
        """HypoidGearDesign: 'ActiveGearDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ActiveGearDesign

        if temp is None:
            return None

        if _978.HypoidGearDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast active_gear_design to HypoidGearDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def active_gear_design_of_type_bevel_gear_design(self) -> '_1170.BevelGearDesign':
        """BevelGearDesign: 'ActiveGearDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ActiveGearDesign

        if temp is None:
            return None

        if _1170.BevelGearDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast active_gear_design to BevelGearDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def active_gear_design_of_type_agma_gleason_conical_gear_design(self) -> '_1183.AGMAGleasonConicalGearDesign':
        """AGMAGleasonConicalGearDesign: 'ActiveGearDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ActiveGearDesign

        if temp is None:
            return None

        if _1183.AGMAGleasonConicalGearDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast active_gear_design to AGMAGleasonConicalGearDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def conical_gear_design(self) -> '_1144.ConicalGearDesign':
        """ConicalGearDesign: 'ConicalGearDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConicalGearDesign

        if temp is None:
            return None

        if _1144.ConicalGearDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast conical_gear_design to ConicalGearDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def conical_gear_design_of_type_zerol_bevel_gear_design(self) -> '_945.ZerolBevelGearDesign':
        """ZerolBevelGearDesign: 'ConicalGearDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConicalGearDesign

        if temp is None:
            return None

        if _945.ZerolBevelGearDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast conical_gear_design to ZerolBevelGearDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def conical_gear_design_of_type_straight_bevel_gear_design(self) -> '_954.StraightBevelGearDesign':
        """StraightBevelGearDesign: 'ConicalGearDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConicalGearDesign

        if temp is None:
            return None

        if _954.StraightBevelGearDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast conical_gear_design to StraightBevelGearDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def conical_gear_design_of_type_straight_bevel_diff_gear_design(self) -> '_958.StraightBevelDiffGearDesign':
        """StraightBevelDiffGearDesign: 'ConicalGearDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConicalGearDesign

        if temp is None:
            return None

        if _958.StraightBevelDiffGearDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast conical_gear_design to StraightBevelDiffGearDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def conical_gear_design_of_type_spiral_bevel_gear_design(self) -> '_962.SpiralBevelGearDesign':
        """SpiralBevelGearDesign: 'ConicalGearDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConicalGearDesign

        if temp is None:
            return None

        if _962.SpiralBevelGearDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast conical_gear_design to SpiralBevelGearDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def conical_gear_design_of_type_klingelnberg_cyclo_palloid_spiral_bevel_gear_design(self) -> '_966.KlingelnbergCycloPalloidSpiralBevelGearDesign':
        """KlingelnbergCycloPalloidSpiralBevelGearDesign: 'ConicalGearDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConicalGearDesign

        if temp is None:
            return None

        if _966.KlingelnbergCycloPalloidSpiralBevelGearDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast conical_gear_design to KlingelnbergCycloPalloidSpiralBevelGearDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def conical_gear_design_of_type_klingelnberg_cyclo_palloid_hypoid_gear_design(self) -> '_970.KlingelnbergCycloPalloidHypoidGearDesign':
        """KlingelnbergCycloPalloidHypoidGearDesign: 'ConicalGearDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConicalGearDesign

        if temp is None:
            return None

        if _970.KlingelnbergCycloPalloidHypoidGearDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast conical_gear_design to KlingelnbergCycloPalloidHypoidGearDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def conical_gear_design_of_type_klingelnberg_conical_gear_design(self) -> '_974.KlingelnbergConicalGearDesign':
        """KlingelnbergConicalGearDesign: 'ConicalGearDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConicalGearDesign

        if temp is None:
            return None

        if _974.KlingelnbergConicalGearDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast conical_gear_design to KlingelnbergConicalGearDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def conical_gear_design_of_type_hypoid_gear_design(self) -> '_978.HypoidGearDesign':
        """HypoidGearDesign: 'ConicalGearDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConicalGearDesign

        if temp is None:
            return None

        if _978.HypoidGearDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast conical_gear_design to HypoidGearDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def conical_gear_design_of_type_bevel_gear_design(self) -> '_1170.BevelGearDesign':
        """BevelGearDesign: 'ConicalGearDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConicalGearDesign

        if temp is None:
            return None

        if _1170.BevelGearDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast conical_gear_design to BevelGearDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def conical_gear_design_of_type_agma_gleason_conical_gear_design(self) -> '_1183.AGMAGleasonConicalGearDesign':
        """AGMAGleasonConicalGearDesign: 'ConicalGearDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConicalGearDesign

        if temp is None:
            return None

        if _1183.AGMAGleasonConicalGearDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast conical_gear_design to AGMAGleasonConicalGearDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None
