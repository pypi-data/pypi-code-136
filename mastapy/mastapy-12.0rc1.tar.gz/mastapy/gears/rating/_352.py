"""_352.py

GearDutyCycleRating
"""


from typing import List

from mastapy._internal import constructor, conversion
from mastapy.gears.rating import (
    _356, _353, _355, _348
)
from mastapy.gears.rating.worm import _369
from mastapy._internal.cast_exception import CastException
from mastapy.gears.rating.face import _443
from mastapy.gears.rating.cylindrical import _457, _450, _451
from mastapy.gears.rating.conical import _534
from mastapy.gears.rating.concept import _545
from mastapy._internal.python_net import python_net_import

_GEAR_DUTY_CYCLE_RATING = python_net_import('SMT.MastaAPI.Gears.Rating', 'GearDutyCycleRating')


__docformat__ = 'restructuredtext en'
__all__ = ('GearDutyCycleRating',)


class GearDutyCycleRating(_348.AbstractGearRating):
    """GearDutyCycleRating

    This is a mastapy class.
    """

    TYPE = _GEAR_DUTY_CYCLE_RATING

    def __init__(self, instance_to_wrap: 'GearDutyCycleRating.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def damage_bending(self) -> 'float':
        """float: 'DamageBending' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DamageBending

        if temp is None:
            return 0.0

        return temp

    @property
    def damage_contact(self) -> 'float':
        """float: 'DamageContact' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DamageContact

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_bending_stress(self) -> 'float':
        """float: 'MaximumBendingStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumBendingStress

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_contact_stress(self) -> 'float':
        """float: 'MaximumContactStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumContactStress

        if temp is None:
            return 0.0

        return temp

    @property
    def gear_set_design_duty_cycle(self) -> '_356.GearSetDutyCycleRating':
        """GearSetDutyCycleRating: 'GearSetDesignDutyCycle' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearSetDesignDutyCycle

        if temp is None:
            return None

        if _356.GearSetDutyCycleRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_set_design_duty_cycle to GearSetDutyCycleRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_set_design_duty_cycle_of_type_worm_gear_set_duty_cycle_rating(self) -> '_369.WormGearSetDutyCycleRating':
        """WormGearSetDutyCycleRating: 'GearSetDesignDutyCycle' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearSetDesignDutyCycle

        if temp is None:
            return None

        if _369.WormGearSetDutyCycleRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_set_design_duty_cycle to WormGearSetDutyCycleRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_set_design_duty_cycle_of_type_face_gear_set_duty_cycle_rating(self) -> '_443.FaceGearSetDutyCycleRating':
        """FaceGearSetDutyCycleRating: 'GearSetDesignDutyCycle' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearSetDesignDutyCycle

        if temp is None:
            return None

        if _443.FaceGearSetDutyCycleRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_set_design_duty_cycle to FaceGearSetDutyCycleRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_set_design_duty_cycle_of_type_cylindrical_gear_set_duty_cycle_rating(self) -> '_457.CylindricalGearSetDutyCycleRating':
        """CylindricalGearSetDutyCycleRating: 'GearSetDesignDutyCycle' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearSetDesignDutyCycle

        if temp is None:
            return None

        if _457.CylindricalGearSetDutyCycleRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_set_design_duty_cycle to CylindricalGearSetDutyCycleRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_set_design_duty_cycle_of_type_conical_gear_set_duty_cycle_rating(self) -> '_534.ConicalGearSetDutyCycleRating':
        """ConicalGearSetDutyCycleRating: 'GearSetDesignDutyCycle' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearSetDesignDutyCycle

        if temp is None:
            return None

        if _534.ConicalGearSetDutyCycleRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_set_design_duty_cycle to ConicalGearSetDutyCycleRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_set_design_duty_cycle_of_type_concept_gear_set_duty_cycle_rating(self) -> '_545.ConceptGearSetDutyCycleRating':
        """ConceptGearSetDutyCycleRating: 'GearSetDesignDutyCycle' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearSetDesignDutyCycle

        if temp is None:
            return None

        if _545.ConceptGearSetDutyCycleRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_set_design_duty_cycle to ConceptGearSetDutyCycleRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def left_flank_rating(self) -> '_353.GearFlankRating':
        """GearFlankRating: 'LeftFlankRating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LeftFlankRating

        if temp is None:
            return None

        if _353.GearFlankRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast left_flank_rating to GearFlankRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def right_flank_rating(self) -> '_353.GearFlankRating':
        """GearFlankRating: 'RightFlankRating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RightFlankRating

        if temp is None:
            return None

        if _353.GearFlankRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast right_flank_rating to GearFlankRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_ratings(self) -> 'List[_355.GearRating]':
        """List[GearRating]: 'GearRatings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearRatings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value
