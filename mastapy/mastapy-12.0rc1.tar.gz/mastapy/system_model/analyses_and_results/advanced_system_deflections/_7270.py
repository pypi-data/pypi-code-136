"""_7270.py

KlingelnbergCycloPalloidHypoidGearSetAdvancedSystemDeflection
"""


from typing import List

from mastapy.system_model.part_model.gears import _2490
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6843
from mastapy.gears.rating.klingelnberg_hypoid import _404
from mastapy.system_model.analyses_and_results.system_deflections import _2718
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7268, _7269, _7267
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_SET_ADVANCED_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections', 'KlingelnbergCycloPalloidHypoidGearSetAdvancedSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('KlingelnbergCycloPalloidHypoidGearSetAdvancedSystemDeflection',)


class KlingelnbergCycloPalloidHypoidGearSetAdvancedSystemDeflection(_7267.KlingelnbergCycloPalloidConicalGearSetAdvancedSystemDeflection):
    """KlingelnbergCycloPalloidHypoidGearSetAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_SET_ADVANCED_SYSTEM_DEFLECTION

    def __init__(self, instance_to_wrap: 'KlingelnbergCycloPalloidHypoidGearSetAdvancedSystemDeflection.TYPE'):
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
    def rating(self) -> '_404.KlingelnbergCycloPalloidHypoidGearSetRating':
        """KlingelnbergCycloPalloidHypoidGearSetRating: 'Rating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Rating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_detailed_analysis(self) -> '_404.KlingelnbergCycloPalloidHypoidGearSetRating':
        """KlingelnbergCycloPalloidHypoidGearSetRating: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDetailedAnalysis

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
    def klingelnberg_cyclo_palloid_hypoid_gears_advanced_system_deflection(self) -> 'List[_7268.KlingelnbergCycloPalloidHypoidGearAdvancedSystemDeflection]':
        """List[KlingelnbergCycloPalloidHypoidGearAdvancedSystemDeflection]: 'KlingelnbergCycloPalloidHypoidGearsAdvancedSystemDeflection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.KlingelnbergCycloPalloidHypoidGearsAdvancedSystemDeflection

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def klingelnberg_cyclo_palloid_hypoid_meshes_advanced_system_deflection(self) -> 'List[_7269.KlingelnbergCycloPalloidHypoidGearMeshAdvancedSystemDeflection]':
        """List[KlingelnbergCycloPalloidHypoidGearMeshAdvancedSystemDeflection]: 'KlingelnbergCycloPalloidHypoidMeshesAdvancedSystemDeflection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.KlingelnbergCycloPalloidHypoidMeshesAdvancedSystemDeflection

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value
