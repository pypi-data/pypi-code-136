"""_7326.py

WormGearSetAdvancedSystemDeflection
"""


from typing import List

from mastapy.system_model.part_model.gears import _2503
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6910
from mastapy.gears.rating.worm import _370
from mastapy.system_model.analyses_and_results.system_deflections import _2783
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7324, _7325, _7259
from mastapy._internal.python_net import python_net_import

_WORM_GEAR_SET_ADVANCED_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections', 'WormGearSetAdvancedSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('WormGearSetAdvancedSystemDeflection',)


class WormGearSetAdvancedSystemDeflection(_7259.GearSetAdvancedSystemDeflection):
    """WormGearSetAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _WORM_GEAR_SET_ADVANCED_SYSTEM_DEFLECTION

    def __init__(self, instance_to_wrap: 'WormGearSetAdvancedSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2503.WormGearSet':
        """WormGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_load_case(self) -> '_6910.WormGearSetLoadCase':
        """WormGearSetLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def rating(self) -> '_370.WormGearSetRating':
        """WormGearSetRating: 'Rating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Rating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_detailed_analysis(self) -> '_370.WormGearSetRating':
        """WormGearSetRating: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDetailedAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_system_deflection_results(self) -> 'List[_2783.WormGearSetSystemDeflection]':
        """List[WormGearSetSystemDeflection]: 'AssemblySystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblySystemDeflectionResults

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def worm_gears_advanced_system_deflection(self) -> 'List[_7324.WormGearAdvancedSystemDeflection]':
        """List[WormGearAdvancedSystemDeflection]: 'WormGearsAdvancedSystemDeflection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WormGearsAdvancedSystemDeflection

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def worm_meshes_advanced_system_deflection(self) -> 'List[_7325.WormGearMeshAdvancedSystemDeflection]':
        """List[WormGearMeshAdvancedSystemDeflection]: 'WormMeshesAdvancedSystemDeflection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WormMeshesAdvancedSystemDeflection

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value
