"""_4471.py

PointLoadCompoundParametricStudyTool
"""


from typing import List

from mastapy.system_model.part_model import _2423
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4342
from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4507
from mastapy._internal.python_net import python_net_import

_POINT_LOAD_COMPOUND_PARAMETRIC_STUDY_TOOL = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.Compound', 'PointLoadCompoundParametricStudyTool')


__docformat__ = 'restructuredtext en'
__all__ = ('PointLoadCompoundParametricStudyTool',)


class PointLoadCompoundParametricStudyTool(_4507.VirtualComponentCompoundParametricStudyTool):
    """PointLoadCompoundParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _POINT_LOAD_COMPOUND_PARAMETRIC_STUDY_TOOL

    def __init__(self, instance_to_wrap: 'PointLoadCompoundParametricStudyTool.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2423.PointLoad':
        """PointLoad: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_analysis_cases_ready(self) -> 'List[_4342.PointLoadParametricStudyTool]':
        """List[PointLoadParametricStudyTool]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases(self) -> 'List[_4342.PointLoadParametricStudyTool]':
        """List[PointLoadParametricStudyTool]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value
