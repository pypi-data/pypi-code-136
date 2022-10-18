"""_7011.py

MassDiscAdvancedTimeSteppingAnalysisForModulation
"""


from typing import List

from mastapy.system_model.part_model import _2414
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6847
from mastapy.system_model.analyses_and_results.system_deflections import _2725
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7058
from mastapy._internal.python_net import python_net_import

_MASS_DISC_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation', 'MassDiscAdvancedTimeSteppingAnalysisForModulation')


__docformat__ = 'restructuredtext en'
__all__ = ('MassDiscAdvancedTimeSteppingAnalysisForModulation',)


class MassDiscAdvancedTimeSteppingAnalysisForModulation(_7058.VirtualComponentAdvancedTimeSteppingAnalysisForModulation):
    """MassDiscAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _MASS_DISC_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION

    def __init__(self, instance_to_wrap: 'MassDiscAdvancedTimeSteppingAnalysisForModulation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2414.MassDisc':
        """MassDisc: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_load_case(self) -> '_6847.MassDiscLoadCase':
        """MassDiscLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results(self) -> '_2725.MassDiscSystemDeflection':
        """MassDiscSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def planetaries(self) -> 'List[MassDiscAdvancedTimeSteppingAnalysisForModulation]':
        """List[MassDiscAdvancedTimeSteppingAnalysisForModulation]: 'Planetaries' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value
