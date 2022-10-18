"""_6833.py

HypoidGearSetLoadCase
"""


from typing import List

from mastapy.system_model.part_model.gears import _2486
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6831, _6832, _6742
from mastapy._internal.python_net import python_net_import

_HYPOID_GEAR_SET_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'HypoidGearSetLoadCase')


__docformat__ = 'restructuredtext en'
__all__ = ('HypoidGearSetLoadCase',)


class HypoidGearSetLoadCase(_6742.AGMAGleasonConicalGearSetLoadCase):
    """HypoidGearSetLoadCase

    This is a mastapy class.
    """

    TYPE = _HYPOID_GEAR_SET_LOAD_CASE

    def __init__(self, instance_to_wrap: 'HypoidGearSetLoadCase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2486.HypoidGearSet':
        """HypoidGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gears(self) -> 'List[_6831.HypoidGearLoadCase]':
        """List[HypoidGearLoadCase]: 'Gears' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Gears

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def hypoid_gears_load_case(self) -> 'List[_6831.HypoidGearLoadCase]':
        """List[HypoidGearLoadCase]: 'HypoidGearsLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HypoidGearsLoadCase

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def hypoid_meshes_load_case(self) -> 'List[_6832.HypoidGearMeshLoadCase]':
        """List[HypoidGearMeshLoadCase]: 'HypoidMeshesLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HypoidMeshesLoadCase

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value
