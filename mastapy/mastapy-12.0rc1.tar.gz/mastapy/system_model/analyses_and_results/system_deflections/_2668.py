"""_2668.py

ConceptGearSystemDeflection
"""


from mastapy.system_model.part_model.gears import _2472
from mastapy._internal import constructor
from mastapy.gears.rating.concept import _544
from mastapy.system_model.analyses_and_results.static_loads import _6767
from mastapy.system_model.analyses_and_results.power_flows import _4006
from mastapy.system_model.analyses_and_results.system_deflections import _2707
from mastapy._internal.python_net import python_net_import

_CONCEPT_GEAR_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections', 'ConceptGearSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('ConceptGearSystemDeflection',)


class ConceptGearSystemDeflection(_2707.GearSystemDeflection):
    """ConceptGearSystemDeflection

    This is a mastapy class.
    """

    TYPE = _CONCEPT_GEAR_SYSTEM_DEFLECTION

    def __init__(self, instance_to_wrap: 'ConceptGearSystemDeflection.TYPE'):
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
    def power_flow_results(self) -> '_4006.ConceptGearPowerFlow':
        """ConceptGearPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None
