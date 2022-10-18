"""_4316.py

KlingelnbergCycloPalloidHypoidGearSetParametricStudyTool
"""


from typing import List

from mastapy.system_model.part_model.gears import _2490
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6843
from mastapy.system_model.analyses_and_results.system_deflections import _2718
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4315, _4314, _4313
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_SET_PARAMETRIC_STUDY_TOOL = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools', 'KlingelnbergCycloPalloidHypoidGearSetParametricStudyTool')


__docformat__ = 'restructuredtext en'
__all__ = ('KlingelnbergCycloPalloidHypoidGearSetParametricStudyTool',)


class KlingelnbergCycloPalloidHypoidGearSetParametricStudyTool(_4313.KlingelnbergCycloPalloidConicalGearSetParametricStudyTool):
    """KlingelnbergCycloPalloidHypoidGearSetParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_SET_PARAMETRIC_STUDY_TOOL

    def __init__(self, instance_to_wrap: 'KlingelnbergCycloPalloidHypoidGearSetParametricStudyTool.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2490.KlingelnbergCycloPalloidHypoidGearSet':
        """KlingelnbergCycloPalloidHypoidGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_load_case(self) -> '_6843.KlingelnbergCycloPalloidHypoidGearSetLoadCase':
        """KlingelnbergCycloPalloidHypoidGearSetLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_system_deflection_results(self) -> 'List[_2718.KlingelnbergCycloPalloidHypoidGearSetSystemDeflection]':
        """List[KlingelnbergCycloPalloidHypoidGearSetSystemDeflection]: 'AssemblySystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblySystemDeflectionResults

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def klingelnberg_cyclo_palloid_hypoid_gears_parametric_study_tool(self) -> 'List[_4315.KlingelnbergCycloPalloidHypoidGearParametricStudyTool]':
        """List[KlingelnbergCycloPalloidHypoidGearParametricStudyTool]: 'KlingelnbergCycloPalloidHypoidGearsParametricStudyTool' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.KlingelnbergCycloPalloidHypoidGearsParametricStudyTool

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def klingelnberg_cyclo_palloid_hypoid_meshes_parametric_study_tool(self) -> 'List[_4314.KlingelnbergCycloPalloidHypoidGearMeshParametricStudyTool]':
        """List[KlingelnbergCycloPalloidHypoidGearMeshParametricStudyTool]: 'KlingelnbergCycloPalloidHypoidMeshesParametricStudyTool' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.KlingelnbergCycloPalloidHypoidMeshesParametricStudyTool

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value
