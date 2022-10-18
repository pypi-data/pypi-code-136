"""_6958.py

ClutchHalfAdvancedTimeSteppingAnalysisForModulation
"""


from mastapy.system_model.part_model.couplings import _2530
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6760
from mastapy.system_model.analyses_and_results.system_deflections import _2658
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _6974
from mastapy._internal.python_net import python_net_import

_CLUTCH_HALF_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation', 'ClutchHalfAdvancedTimeSteppingAnalysisForModulation')


__docformat__ = 'restructuredtext en'
__all__ = ('ClutchHalfAdvancedTimeSteppingAnalysisForModulation',)


class ClutchHalfAdvancedTimeSteppingAnalysisForModulation(_6974.CouplingHalfAdvancedTimeSteppingAnalysisForModulation):
    """ClutchHalfAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _CLUTCH_HALF_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION

    def __init__(self, instance_to_wrap: 'ClutchHalfAdvancedTimeSteppingAnalysisForModulation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2530.ClutchHalf':
        """ClutchHalf: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_load_case(self) -> '_6760.ClutchHalfLoadCase':
        """ClutchHalfLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results(self) -> '_2658.ClutchHalfSystemDeflection':
        """ClutchHalfSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None
