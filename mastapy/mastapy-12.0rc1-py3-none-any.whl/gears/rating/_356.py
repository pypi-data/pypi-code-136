"""_356.py

GearSetDutyCycleRating
"""


from typing import List

from mastapy._internal import constructor, conversion
from mastapy.gears.gear_designs import _943
from mastapy.gears.gear_designs.zerol_bevel import _947
from mastapy._internal.cast_exception import CastException
from mastapy.gears.gear_designs.worm import _952
from mastapy.gears.gear_designs.straight_bevel import _956
from mastapy.gears.gear_designs.straight_bevel_diff import _960
from mastapy.gears.gear_designs.spiral_bevel import _964
from mastapy.gears.gear_designs.klingelnberg_spiral_bevel import _968
from mastapy.gears.gear_designs.klingelnberg_hypoid import _972
from mastapy.gears.gear_designs.klingelnberg_conical import _976
from mastapy.gears.gear_designs.hypoid import _980
from mastapy.gears.gear_designs.face import _988
from mastapy.gears.gear_designs.cylindrical import _1021, _1033
from mastapy.gears.gear_designs.conical import _1146
from mastapy.gears.gear_designs.concept import _1168
from mastapy.gears.gear_designs.bevel import _1172
from mastapy.gears.gear_designs.agma_gleason_conical import _1185
from mastapy.gears.rating import _352, _359, _349
from mastapy._internal.python_net import python_net_import

_GEAR_SET_DUTY_CYCLE_RATING = python_net_import('SMT.MastaAPI.Gears.Rating', 'GearSetDutyCycleRating')


__docformat__ = 'restructuredtext en'
__all__ = ('GearSetDutyCycleRating',)


class GearSetDutyCycleRating(_349.AbstractGearSetRating):
    """GearSetDutyCycleRating

    This is a mastapy class.
    """

    TYPE = _GEAR_SET_DUTY_CYCLE_RATING

    def __init__(self, instance_to_wrap: 'GearSetDutyCycleRating.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def duty_cycle_name(self) -> 'str':
        """str: 'DutyCycleName' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DutyCycleName

        if temp is None:
            return ''

        return temp

    @property
    def name(self) -> 'str':
        """str: 'Name' is the original name of this property."""

        temp = self.wrapped.Name

        if temp is None:
            return ''

        return temp

    @name.setter
    def name(self, value: 'str'):
        self.wrapped.Name = str(value) if value else ''

    @property
    def total_duty_cycle_gear_set_reliability(self) -> 'float':
        """float: 'TotalDutyCycleGearSetReliability' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TotalDutyCycleGearSetReliability

        if temp is None:
            return 0.0

        return temp

    @property
    def gear_set_design(self) -> '_943.GearSetDesign':
        """GearSetDesign: 'GearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearSetDesign

        if temp is None:
            return None

        if _943.GearSetDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_set_design to GearSetDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_set_design_of_type_zerol_bevel_gear_set_design(self) -> '_947.ZerolBevelGearSetDesign':
        """ZerolBevelGearSetDesign: 'GearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearSetDesign

        if temp is None:
            return None

        if _947.ZerolBevelGearSetDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_set_design to ZerolBevelGearSetDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_set_design_of_type_worm_gear_set_design(self) -> '_952.WormGearSetDesign':
        """WormGearSetDesign: 'GearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearSetDesign

        if temp is None:
            return None

        if _952.WormGearSetDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_set_design to WormGearSetDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_set_design_of_type_straight_bevel_gear_set_design(self) -> '_956.StraightBevelGearSetDesign':
        """StraightBevelGearSetDesign: 'GearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearSetDesign

        if temp is None:
            return None

        if _956.StraightBevelGearSetDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_set_design to StraightBevelGearSetDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_set_design_of_type_straight_bevel_diff_gear_set_design(self) -> '_960.StraightBevelDiffGearSetDesign':
        """StraightBevelDiffGearSetDesign: 'GearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearSetDesign

        if temp is None:
            return None

        if _960.StraightBevelDiffGearSetDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_set_design to StraightBevelDiffGearSetDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_set_design_of_type_spiral_bevel_gear_set_design(self) -> '_964.SpiralBevelGearSetDesign':
        """SpiralBevelGearSetDesign: 'GearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearSetDesign

        if temp is None:
            return None

        if _964.SpiralBevelGearSetDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_set_design to SpiralBevelGearSetDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_set_design_of_type_klingelnberg_cyclo_palloid_spiral_bevel_gear_set_design(self) -> '_968.KlingelnbergCycloPalloidSpiralBevelGearSetDesign':
        """KlingelnbergCycloPalloidSpiralBevelGearSetDesign: 'GearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearSetDesign

        if temp is None:
            return None

        if _968.KlingelnbergCycloPalloidSpiralBevelGearSetDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_set_design to KlingelnbergCycloPalloidSpiralBevelGearSetDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_set_design_of_type_klingelnberg_cyclo_palloid_hypoid_gear_set_design(self) -> '_972.KlingelnbergCycloPalloidHypoidGearSetDesign':
        """KlingelnbergCycloPalloidHypoidGearSetDesign: 'GearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearSetDesign

        if temp is None:
            return None

        if _972.KlingelnbergCycloPalloidHypoidGearSetDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_set_design to KlingelnbergCycloPalloidHypoidGearSetDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_set_design_of_type_klingelnberg_conical_gear_set_design(self) -> '_976.KlingelnbergConicalGearSetDesign':
        """KlingelnbergConicalGearSetDesign: 'GearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearSetDesign

        if temp is None:
            return None

        if _976.KlingelnbergConicalGearSetDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_set_design to KlingelnbergConicalGearSetDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_set_design_of_type_hypoid_gear_set_design(self) -> '_980.HypoidGearSetDesign':
        """HypoidGearSetDesign: 'GearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearSetDesign

        if temp is None:
            return None

        if _980.HypoidGearSetDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_set_design to HypoidGearSetDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_set_design_of_type_face_gear_set_design(self) -> '_988.FaceGearSetDesign':
        """FaceGearSetDesign: 'GearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearSetDesign

        if temp is None:
            return None

        if _988.FaceGearSetDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_set_design to FaceGearSetDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_set_design_of_type_cylindrical_gear_set_design(self) -> '_1021.CylindricalGearSetDesign':
        """CylindricalGearSetDesign: 'GearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearSetDesign

        if temp is None:
            return None

        if _1021.CylindricalGearSetDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_set_design to CylindricalGearSetDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_set_design_of_type_cylindrical_planetary_gear_set_design(self) -> '_1033.CylindricalPlanetaryGearSetDesign':
        """CylindricalPlanetaryGearSetDesign: 'GearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearSetDesign

        if temp is None:
            return None

        if _1033.CylindricalPlanetaryGearSetDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_set_design to CylindricalPlanetaryGearSetDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_set_design_of_type_conical_gear_set_design(self) -> '_1146.ConicalGearSetDesign':
        """ConicalGearSetDesign: 'GearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearSetDesign

        if temp is None:
            return None

        if _1146.ConicalGearSetDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_set_design to ConicalGearSetDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_set_design_of_type_concept_gear_set_design(self) -> '_1168.ConceptGearSetDesign':
        """ConceptGearSetDesign: 'GearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearSetDesign

        if temp is None:
            return None

        if _1168.ConceptGearSetDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_set_design to ConceptGearSetDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_set_design_of_type_bevel_gear_set_design(self) -> '_1172.BevelGearSetDesign':
        """BevelGearSetDesign: 'GearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearSetDesign

        if temp is None:
            return None

        if _1172.BevelGearSetDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_set_design to BevelGearSetDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_set_design_of_type_agma_gleason_conical_gear_set_design(self) -> '_1185.AGMAGleasonConicalGearSetDesign':
        """AGMAGleasonConicalGearSetDesign: 'GearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearSetDesign

        if temp is None:
            return None

        if _1185.AGMAGleasonConicalGearSetDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_set_design to AGMAGleasonConicalGearSetDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_ratings(self) -> 'List[_352.GearDutyCycleRating]':
        """List[GearDutyCycleRating]: 'GearRatings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearRatings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def gear_duty_cycle_ratings(self) -> 'List[_352.GearDutyCycleRating]':
        """List[GearDutyCycleRating]: 'GearDutyCycleRatings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearDutyCycleRatings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def gear_mesh_ratings(self) -> 'List[_359.MeshDutyCycleRating]':
        """List[MeshDutyCycleRating]: 'GearMeshRatings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearMeshRatings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def gear_mesh_duty_cycle_ratings(self) -> 'List[_359.MeshDutyCycleRating]':
        """List[MeshDutyCycleRating]: 'GearMeshDutyCycleRatings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearMeshDutyCycleRatings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    def set_face_widths_for_specified_safety_factors(self):
        """ 'SetFaceWidthsForSpecifiedSafetyFactors' is the original name of this method."""

        self.wrapped.SetFaceWidthsForSpecifiedSafetyFactors()
