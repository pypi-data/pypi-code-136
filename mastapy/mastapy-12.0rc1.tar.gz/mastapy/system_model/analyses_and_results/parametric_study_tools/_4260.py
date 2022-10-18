"""_4260.py

ClutchHalfParametricStudyTool
"""


from typing import List

from mastapy.system_model.part_model.couplings import _2530
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6760
from mastapy.system_model.analyses_and_results.system_deflections import _2658
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4276
from mastapy._internal.python_net import python_net_import

_CLUTCH_HALF_PARAMETRIC_STUDY_TOOL = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools', 'ClutchHalfParametricStudyTool')


__docformat__ = 'restructuredtext en'
__all__ = ('ClutchHalfParametricStudyTool',)


class ClutchHalfParametricStudyTool(_4276.CouplingHalfParametricStudyTool):
    """ClutchHalfParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _CLUTCH_HALF_PARAMETRIC_STUDY_TOOL

    def __init__(self, instance_to_wrap: 'ClutchHalfParametricStudyTool.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2530.ClutchHalf':
        """ClutchHalf: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_load_case(self) -> '_6760.ClutchHalfLoadCase':
        """ClutchHalfLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_system_deflection_results(self) -> 'List[_2658.ClutchHalfSystemDeflection]':
        """List[ClutchHalfSystemDeflection]: 'ComponentSystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentSystemDeflectionResults

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value
