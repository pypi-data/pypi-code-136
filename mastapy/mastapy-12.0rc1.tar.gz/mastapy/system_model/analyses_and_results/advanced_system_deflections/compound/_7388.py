"""_7388.py

GearCompoundAdvancedSystemDeflection
"""


from typing import List

from mastapy.gears.rating import _352
from mastapy._internal import constructor, conversion
from mastapy.gears.rating.worm import _366
from mastapy._internal.cast_exception import CastException
from mastapy.gears.rating.face import _439
from mastapy.gears.rating.cylindrical import _449
from mastapy.gears.rating.conical import _531
from mastapy.gears.rating.concept import _541
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7257
from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7407
from mastapy._internal.python_net import python_net_import

_GEAR_COMPOUND_ADVANCED_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections.Compound', 'GearCompoundAdvancedSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('GearCompoundAdvancedSystemDeflection',)


class GearCompoundAdvancedSystemDeflection(_7407.MountableComponentCompoundAdvancedSystemDeflection):
    """GearCompoundAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _GEAR_COMPOUND_ADVANCED_SYSTEM_DEFLECTION

    def __init__(self, instance_to_wrap: 'GearCompoundAdvancedSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def gear_duty_cycle_rating(self) -> '_352.GearDutyCycleRating':
        """GearDutyCycleRating: 'GearDutyCycleRating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearDutyCycleRating

        if temp is None:
            return None

        if _352.GearDutyCycleRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_duty_cycle_rating to GearDutyCycleRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_duty_cycle_rating_of_type_worm_gear_duty_cycle_rating(self) -> '_366.WormGearDutyCycleRating':
        """WormGearDutyCycleRating: 'GearDutyCycleRating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearDutyCycleRating

        if temp is None:
            return None

        if _366.WormGearDutyCycleRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_duty_cycle_rating to WormGearDutyCycleRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_duty_cycle_rating_of_type_face_gear_duty_cycle_rating(self) -> '_439.FaceGearDutyCycleRating':
        """FaceGearDutyCycleRating: 'GearDutyCycleRating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearDutyCycleRating

        if temp is None:
            return None

        if _439.FaceGearDutyCycleRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_duty_cycle_rating to FaceGearDutyCycleRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_duty_cycle_rating_of_type_cylindrical_gear_duty_cycle_rating(self) -> '_449.CylindricalGearDutyCycleRating':
        """CylindricalGearDutyCycleRating: 'GearDutyCycleRating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearDutyCycleRating

        if temp is None:
            return None

        if _449.CylindricalGearDutyCycleRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_duty_cycle_rating to CylindricalGearDutyCycleRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_duty_cycle_rating_of_type_conical_gear_duty_cycle_rating(self) -> '_531.ConicalGearDutyCycleRating':
        """ConicalGearDutyCycleRating: 'GearDutyCycleRating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearDutyCycleRating

        if temp is None:
            return None

        if _531.ConicalGearDutyCycleRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_duty_cycle_rating to ConicalGearDutyCycleRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_duty_cycle_rating_of_type_concept_gear_duty_cycle_rating(self) -> '_541.ConceptGearDutyCycleRating':
        """ConceptGearDutyCycleRating: 'GearDutyCycleRating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearDutyCycleRating

        if temp is None:
            return None

        if _541.ConceptGearDutyCycleRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_duty_cycle_rating to ConceptGearDutyCycleRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_analysis_cases(self) -> 'List[_7257.GearAdvancedSystemDeflection]':
        """List[GearAdvancedSystemDeflection]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases_ready(self) -> 'List[_7257.GearAdvancedSystemDeflection]':
        """List[GearAdvancedSystemDeflection]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value
