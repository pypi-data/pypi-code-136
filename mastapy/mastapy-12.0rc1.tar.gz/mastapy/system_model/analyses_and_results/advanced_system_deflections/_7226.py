"""_7226.py

ConceptGearAdvancedSystemDeflection
"""


from typing import List

from mastapy.system_model.part_model.gears import _2472
from mastapy._internal import constructor, conversion
from mastapy.gears.rating.concept import _544
from mastapy.system_model.analyses_and_results.static_loads import _6767
from mastapy.system_model.analyses_and_results.system_deflections import _2668
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7257
from mastapy._internal.python_net import python_net_import

_CONCEPT_GEAR_ADVANCED_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections', 'ConceptGearAdvancedSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('ConceptGearAdvancedSystemDeflection',)


class ConceptGearAdvancedSystemDeflection(_7257.GearAdvancedSystemDeflection):
    """ConceptGearAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _CONCEPT_GEAR_ADVANCED_SYSTEM_DEFLECTION

    def __init__(self, instance_to_wrap: 'ConceptGearAdvancedSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2472.ConceptGear':
        """ConceptGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_detailed_analysis(self) -> '_544.ConceptGearRating':
        """ConceptGearRating: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDetailedAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_load_case(self) -> '_6767.ConceptGearLoadCase':
        """ConceptGearLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_system_deflection_results(self) -> 'List[_2668.ConceptGearSystemDeflection]':
        """List[ConceptGearSystemDeflection]: 'ComponentSystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentSystemDeflectionResults

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value
