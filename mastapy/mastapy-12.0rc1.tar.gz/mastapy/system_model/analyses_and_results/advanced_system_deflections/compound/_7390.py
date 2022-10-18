"""_7390.py

GearSetCompoundAdvancedSystemDeflection
"""


from typing import List

from mastapy.gears.rating import _356
from mastapy._internal import constructor, conversion
from mastapy.gears.rating.worm import _369
from mastapy._internal.cast_exception import CastException
from mastapy.gears.rating.face import _443
from mastapy.gears.rating.cylindrical import _457
from mastapy.gears.rating.conical import _534
from mastapy.gears.rating.concept import _545
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7259
from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7428
from mastapy._internal.python_net import python_net_import

_GEAR_SET_COMPOUND_ADVANCED_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections.Compound', 'GearSetCompoundAdvancedSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('GearSetCompoundAdvancedSystemDeflection',)


class GearSetCompoundAdvancedSystemDeflection(_7428.SpecialisedAssemblyCompoundAdvancedSystemDeflection):
    """GearSetCompoundAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _GEAR_SET_COMPOUND_ADVANCED_SYSTEM_DEFLECTION

    def __init__(self, instance_to_wrap: 'GearSetCompoundAdvancedSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def gear_duty_cycle_rating(self) -> '_356.GearSetDutyCycleRating':
        """GearSetDutyCycleRating: 'GearDutyCycleRating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearDutyCycleRating

        if temp is None:
            return None

        if _356.GearSetDutyCycleRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_duty_cycle_rating to GearSetDutyCycleRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_duty_cycle_rating_of_type_worm_gear_set_duty_cycle_rating(self) -> '_369.WormGearSetDutyCycleRating':
        """WormGearSetDutyCycleRating: 'GearDutyCycleRating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearDutyCycleRating

        if temp is None:
            return None

        if _369.WormGearSetDutyCycleRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_duty_cycle_rating to WormGearSetDutyCycleRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_duty_cycle_rating_of_type_face_gear_set_duty_cycle_rating(self) -> '_443.FaceGearSetDutyCycleRating':
        """FaceGearSetDutyCycleRating: 'GearDutyCycleRating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearDutyCycleRating

        if temp is None:
            return None

        if _443.FaceGearSetDutyCycleRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_duty_cycle_rating to FaceGearSetDutyCycleRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_duty_cycle_rating_of_type_cylindrical_gear_set_duty_cycle_rating(self) -> '_457.CylindricalGearSetDutyCycleRating':
        """CylindricalGearSetDutyCycleRating: 'GearDutyCycleRating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearDutyCycleRating

        if temp is None:
            return None

        if _457.CylindricalGearSetDutyCycleRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_duty_cycle_rating to CylindricalGearSetDutyCycleRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_duty_cycle_rating_of_type_conical_gear_set_duty_cycle_rating(self) -> '_534.ConicalGearSetDutyCycleRating':
        """ConicalGearSetDutyCycleRating: 'GearDutyCycleRating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearDutyCycleRating

        if temp is None:
            return None

        if _534.ConicalGearSetDutyCycleRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_duty_cycle_rating to ConicalGearSetDutyCycleRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_duty_cycle_rating_of_type_concept_gear_set_duty_cycle_rating(self) -> '_545.ConceptGearSetDutyCycleRating':
        """ConceptGearSetDutyCycleRating: 'GearDutyCycleRating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearDutyCycleRating

        if temp is None:
            return None

        if _545.ConceptGearSetDutyCycleRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_duty_cycle_rating to ConceptGearSetDutyCycleRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_analysis_cases(self) -> 'List[_7259.GearSetAdvancedSystemDeflection]':
        """List[GearSetAdvancedSystemDeflection]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_7259.GearSetAdvancedSystemDeflection]':
        """List[GearSetAdvancedSystemDeflection]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value
