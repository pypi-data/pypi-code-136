"""_4490.py

StraightBevelDiffGearCompoundParametricStudyTool
"""


from typing import List

from mastapy.system_model.part_model.gears import _2496, _2500, _2501
from mastapy._internal import constructor, conversion
from mastapy._internal.cast_exception import CastException
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4362
from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4401
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_DIFF_GEAR_COMPOUND_PARAMETRIC_STUDY_TOOL = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.Compound', 'StraightBevelDiffGearCompoundParametricStudyTool')


__docformat__ = 'restructuredtext en'
__all__ = ('StraightBevelDiffGearCompoundParametricStudyTool',)


class StraightBevelDiffGearCompoundParametricStudyTool(_4401.BevelGearCompoundParametricStudyTool):
    """StraightBevelDiffGearCompoundParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_DIFF_GEAR_COMPOUND_PARAMETRIC_STUDY_TOOL

    def __init__(self, instance_to_wrap: 'StraightBevelDiffGearCompoundParametricStudyTool.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2496.StraightBevelDiffGear':
        """StraightBevelDiffGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2496.StraightBevelDiffGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to StraightBevelDiffGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_analysis_cases_ready(self) -> 'List[_4362.StraightBevelDiffGearParametricStudyTool]':
        """List[StraightBevelDiffGearParametricStudyTool]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases(self) -> 'List[_4362.StraightBevelDiffGearParametricStudyTool]':
        """List[StraightBevelDiffGearParametricStudyTool]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value
