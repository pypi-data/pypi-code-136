"""_5929.py

UnbalancedMassCompoundHarmonicAnalysis
"""


from typing import List

from mastapy.system_model.part_model import _2429
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5765
from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5930
from mastapy._internal.python_net import python_net_import

_UNBALANCED_MASS_COMPOUND_HARMONIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.Compound', 'UnbalancedMassCompoundHarmonicAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('UnbalancedMassCompoundHarmonicAnalysis',)


class UnbalancedMassCompoundHarmonicAnalysis(_5930.VirtualComponentCompoundHarmonicAnalysis):
    """UnbalancedMassCompoundHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _UNBALANCED_MASS_COMPOUND_HARMONIC_ANALYSIS

    def __init__(self, instance_to_wrap: 'UnbalancedMassCompoundHarmonicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2429.UnbalancedMass':
        """UnbalancedMass: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_analysis_cases_ready(self) -> 'List[_5765.UnbalancedMassHarmonicAnalysis]':
        """List[UnbalancedMassHarmonicAnalysis]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases(self) -> 'List[_5765.UnbalancedMassHarmonicAnalysis]':
        """List[UnbalancedMassHarmonicAnalysis]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value
