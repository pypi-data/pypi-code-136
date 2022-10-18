"""_6705.py

SpringDamperHalfCompoundCriticalSpeedAnalysis
"""


from typing import List

from mastapy.system_model.part_model.couplings import _2552
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6576
from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6640
from mastapy._internal.python_net import python_net_import

_SPRING_DAMPER_HALF_COMPOUND_CRITICAL_SPEED_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses.Compound', 'SpringDamperHalfCompoundCriticalSpeedAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('SpringDamperHalfCompoundCriticalSpeedAnalysis',)


class SpringDamperHalfCompoundCriticalSpeedAnalysis(_6640.CouplingHalfCompoundCriticalSpeedAnalysis):
    """SpringDamperHalfCompoundCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _SPRING_DAMPER_HALF_COMPOUND_CRITICAL_SPEED_ANALYSIS

    def __init__(self, instance_to_wrap: 'SpringDamperHalfCompoundCriticalSpeedAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2552.SpringDamperHalf':
        """SpringDamperHalf: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_analysis_cases_ready(self) -> 'List[_6576.SpringDamperHalfCriticalSpeedAnalysis]':
        """List[SpringDamperHalfCriticalSpeedAnalysis]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases(self) -> 'List[_6576.SpringDamperHalfCriticalSpeedAnalysis]':
        """List[SpringDamperHalfCriticalSpeedAnalysis]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value
