"""_3880.py

CouplingHalfCompoundStabilityAnalysis
"""


from typing import List

from mastapy.system_model.analyses_and_results.stability_analyses import _3747
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3918
from mastapy._internal.python_net import python_net_import

_COUPLING_HALF_COMPOUND_STABILITY_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound', 'CouplingHalfCompoundStabilityAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('CouplingHalfCompoundStabilityAnalysis',)


class CouplingHalfCompoundStabilityAnalysis(_3918.MountableComponentCompoundStabilityAnalysis):
    """CouplingHalfCompoundStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _COUPLING_HALF_COMPOUND_STABILITY_ANALYSIS

    def __init__(self, instance_to_wrap: 'CouplingHalfCompoundStabilityAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(self) -> 'List[_3747.CouplingHalfStabilityAnalysis]':
        """List[CouplingHalfStabilityAnalysis]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases_ready(self) -> 'List[_3747.CouplingHalfStabilityAnalysis]':
        """List[CouplingHalfStabilityAnalysis]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value
