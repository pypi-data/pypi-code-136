"""_5612.py

GearSetStaticLoadCaseGroup
"""


from typing import List, Generic, TypeVar

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.load_case_groups.design_entity_static_load_case_groups import _5609, _5610, _5613
from mastapy.system_model.part_model.gears import _2483, _2481
from mastapy.system_model.analyses_and_results.static_loads import _6816, _6818, _6821
from mastapy.system_model.connections_and_sockets.gears import _2265
from mastapy._internal.python_net import python_net_import

_GEAR_SET_STATIC_LOAD_CASE_GROUP = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.LoadCaseGroups.DesignEntityStaticLoadCaseGroups', 'GearSetStaticLoadCaseGroup')


__docformat__ = 'restructuredtext en'
__all__ = ('GearSetStaticLoadCaseGroup',)


TGearSet = TypeVar('TGearSet', bound='_2483.GearSet')
TGear = TypeVar('TGear', bound='_2481.Gear')
TGearStaticLoad = TypeVar('TGearStaticLoad', bound='_6816.GearLoadCase')
TGearMesh = TypeVar('TGearMesh', bound='_2265.GearMesh')
TGearMeshStaticLoad = TypeVar('TGearMeshStaticLoad', bound='_6818.GearMeshLoadCase')
TGearSetStaticLoad = TypeVar('TGearSetStaticLoad', bound='_6821.GearSetLoadCase')


class GearSetStaticLoadCaseGroup(_5613.PartStaticLoadCaseGroup, Generic[TGearSet, TGear, TGearStaticLoad, TGearMesh, TGearMeshStaticLoad, TGearSetStaticLoad]):
    """GearSetStaticLoadCaseGroup

    This is a mastapy class.

    Generic Types:
        TGearSet
        TGear
        TGearStaticLoad
        TGearMesh
        TGearMeshStaticLoad
        TGearSetStaticLoad
    """

    TYPE = _GEAR_SET_STATIC_LOAD_CASE_GROUP

    def __init__(self, instance_to_wrap: 'GearSetStaticLoadCaseGroup.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def part(self) -> 'TGearSet':
        """TGearSet: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Part

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_set(self) -> 'TGearSet':
        """TGearSet: 'GearSet' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearSet

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def part_load_cases(self) -> 'List[TGearSetStaticLoad]':
        """List[TGearSetStaticLoad]: 'PartLoadCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PartLoadCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def gear_set_load_cases(self) -> 'List[TGearSetStaticLoad]':
        """List[TGearSetStaticLoad]: 'GearSetLoadCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearSetLoadCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def gears_load_cases(self) -> 'List[_5609.ComponentStaticLoadCaseGroup[TGear, TGearStaticLoad]]':
        """List[ComponentStaticLoadCaseGroup[TGear, TGearStaticLoad]]: 'GearsLoadCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearsLoadCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def meshes_load_cases(self) -> 'List[_5610.ConnectionStaticLoadCaseGroup[TGearMesh, TGearMeshStaticLoad]]':
        """List[ConnectionStaticLoadCaseGroup[TGearMesh, TGearMeshStaticLoad]]: 'MeshesLoadCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MeshesLoadCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value
