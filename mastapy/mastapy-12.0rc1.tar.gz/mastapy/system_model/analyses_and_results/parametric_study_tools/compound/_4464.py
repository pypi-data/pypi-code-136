"""_4464.py

PartCompoundParametricStudyTool
"""


from typing import List

from mastapy.utility_gui import _1812
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4335
from mastapy.system_model.analyses_and_results.analysis_cases import _7470
from mastapy._internal.python_net import python_net_import

_PART_COMPOUND_PARAMETRIC_STUDY_TOOL = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.Compound', 'PartCompoundParametricStudyTool')


__docformat__ = 'restructuredtext en'
__all__ = ('PartCompoundParametricStudyTool',)


class PartCompoundParametricStudyTool(_7470.PartCompoundAnalysis):
    """PartCompoundParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _PART_COMPOUND_PARAMETRIC_STUDY_TOOL

    def __init__(self, instance_to_wrap: 'PartCompoundParametricStudyTool.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def data_logger(self) -> '_1812.DataLoggerWithCharts':
        """DataLoggerWithCharts: 'DataLogger' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DataLogger

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_analysis_cases(self) -> 'List[_4335.PartParametricStudyTool]':
        """List[PartParametricStudyTool]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases_ready(self) -> 'List[_4335.PartParametricStudyTool]':
        """List[PartParametricStudyTool]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value
