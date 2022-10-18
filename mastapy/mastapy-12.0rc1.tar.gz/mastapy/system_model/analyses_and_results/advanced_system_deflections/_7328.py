"""_7328.py

ZerolBevelGearMeshAdvancedSystemDeflection
"""


from typing import List

from mastapy.gears.rating.zerol_bevel import _363
from mastapy._internal import constructor, conversion
from mastapy.system_model.connections_and_sockets.gears import _2283
from mastapy.system_model.analyses_and_results.static_loads import _6912
from mastapy.system_model.analyses_and_results.system_deflections import _2785
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7214
from mastapy._internal.python_net import python_net_import

_ZEROL_BEVEL_GEAR_MESH_ADVANCED_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections', 'ZerolBevelGearMeshAdvancedSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('ZerolBevelGearMeshAdvancedSystemDeflection',)


class ZerolBevelGearMeshAdvancedSystemDeflection(_7214.BevelGearMeshAdvancedSystemDeflection):
    """ZerolBevelGearMeshAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _ZEROL_BEVEL_GEAR_MESH_ADVANCED_SYSTEM_DEFLECTION

    def __init__(self, instance_to_wrap: 'ZerolBevelGearMeshAdvancedSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_detailed_analysis(self) -> '_363.ZerolBevelGearMeshRating':
        """ZerolBevelGearMeshRating: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDetailedAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_design(self) -> '_2283.ZerolBevelGearMesh':
        """ZerolBevelGearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_load_case(self) -> '_6912.ZerolBevelGearMeshLoadCase':
        """ZerolBevelGearMeshLoadCase: 'ConnectionLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_system_deflection_results(self) -> 'List[_2785.ZerolBevelGearMeshSystemDeflection]':
        """List[ZerolBevelGearMeshSystemDeflection]: 'ConnectionSystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionSystemDeflectionResults

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value
