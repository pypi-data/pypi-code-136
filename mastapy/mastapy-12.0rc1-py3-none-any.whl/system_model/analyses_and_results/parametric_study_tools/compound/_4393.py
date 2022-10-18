"""_4393.py

BearingCompoundParametricStudyTool
"""


from typing import List

from mastapy.bearings.bearing_results import _1908, _1916, _1919
from mastapy._internal import constructor, conversion
from mastapy._internal.cast_exception import CastException
from mastapy.bearings.bearing_results.rolling import (
    _1948, _1955, _1963, _1979,
    _2002
)
from mastapy.system_model.part_model import _2392
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4246
from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4421
from mastapy._internal.python_net import python_net_import

_BEARING_COMPOUND_PARAMETRIC_STUDY_TOOL = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.Compound', 'BearingCompoundParametricStudyTool')


__docformat__ = 'restructuredtext en'
__all__ = ('BearingCompoundParametricStudyTool',)


class BearingCompoundParametricStudyTool(_4421.ConnectorCompoundParametricStudyTool):
    """BearingCompoundParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _BEARING_COMPOUND_PARAMETRIC_STUDY_TOOL

    def __init__(self, instance_to_wrap: 'BearingCompoundParametricStudyTool.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def bearing_duty_cycle_results(self) -> '_1908.LoadedBearingDutyCycle':
        """LoadedBearingDutyCycle: 'BearingDutyCycleResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BearingDutyCycleResults

        if temp is None:
            return None

        if _1908.LoadedBearingDutyCycle.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast bearing_duty_cycle_results to LoadedBearingDutyCycle. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design(self) -> '_2392.Bearing':
        """Bearing: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_analysis_cases_ready(self) -> 'List[_4246.BearingParametricStudyTool]':
        """List[BearingParametricStudyTool]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def planetaries(self) -> 'List[BearingCompoundParametricStudyTool]':
        """List[BearingCompoundParametricStudyTool]: 'Planetaries' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases(self) -> 'List[_4246.BearingParametricStudyTool]':
        """List[BearingParametricStudyTool]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value
