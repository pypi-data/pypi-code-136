"""_4688.py

ClutchCompoundModalAnalysis
"""


from typing import List

from mastapy.system_model.part_model.couplings import _2529
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses import _4537
from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4704
from mastapy._internal.python_net import python_net_import

_CLUTCH_COMPOUND_MODAL_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Compound', 'ClutchCompoundModalAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('ClutchCompoundModalAnalysis',)


class ClutchCompoundModalAnalysis(_4704.CouplingCompoundModalAnalysis):
    """ClutchCompoundModalAnalysis

    This is a mastapy class.
    """

    TYPE = _CLUTCH_COMPOUND_MODAL_ANALYSIS

    def __init__(self, instance_to_wrap: 'ClutchCompoundModalAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2529.Clutch':
        """Clutch: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_design(self) -> '_2529.Clutch':
        """Clutch: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_4537.ClutchModalAnalysis]':
        """List[ClutchModalAnalysis]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def assembly_analysis_cases(self) -> 'List[_4537.ClutchModalAnalysis]':
        """List[ClutchModalAnalysis]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value
