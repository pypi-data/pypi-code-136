"""_4789.py

VirtualComponentCompoundModalAnalysis
"""


from typing import List

from mastapy.system_model.analyses_and_results.modal_analyses import _4645
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4744
from mastapy._internal.python_net import python_net_import

_VIRTUAL_COMPONENT_COMPOUND_MODAL_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Compound', 'VirtualComponentCompoundModalAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('VirtualComponentCompoundModalAnalysis',)


class VirtualComponentCompoundModalAnalysis(_4744.MountableComponentCompoundModalAnalysis):
    """VirtualComponentCompoundModalAnalysis

    This is a mastapy class.
    """

    TYPE = _VIRTUAL_COMPONENT_COMPOUND_MODAL_ANALYSIS

    def __init__(self, instance_to_wrap: 'VirtualComponentCompoundModalAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(self) -> 'List[_4645.VirtualComponentModalAnalysis]':
        """List[VirtualComponentModalAnalysis]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases_ready(self) -> 'List[_4645.VirtualComponentModalAnalysis]':
        """List[VirtualComponentModalAnalysis]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value
