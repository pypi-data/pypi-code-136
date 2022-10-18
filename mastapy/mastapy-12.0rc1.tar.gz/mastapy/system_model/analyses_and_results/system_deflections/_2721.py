"""_2721.py

KlingelnbergCycloPalloidSpiralBevelGearSetSystemDeflection
"""


from typing import List

from mastapy.system_model.part_model.gears import _2492
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6846
from mastapy.gears.rating.klingelnberg_spiral_bevel import _401
from mastapy.system_model.analyses_and_results.power_flows import _4051
from mastapy.system_model.analyses_and_results.system_deflections import _2722, _2720, _2715
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_SET_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections', 'KlingelnbergCycloPalloidSpiralBevelGearSetSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('KlingelnbergCycloPalloidSpiralBevelGearSetSystemDeflection',)


class KlingelnbergCycloPalloidSpiralBevelGearSetSystemDeflection(_2715.KlingelnbergCycloPalloidConicalGearSetSystemDeflection):
    """KlingelnbergCycloPalloidSpiralBevelGearSetSystemDeflection

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_SET_SYSTEM_DEFLECTION

    def __init__(self, instance_to_wrap: 'KlingelnbergCycloPalloidSpiralBevelGearSetSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2492.KlingelnbergCycloPalloidSpiralBevelGearSet':
        """KlingelnbergCycloPalloidSpiralBevelGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_load_case(self) -> '_6846.KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase':
        """KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def rating(self) -> '_401.KlingelnbergCycloPalloidSpiralBevelGearSetRating':
        """KlingelnbergCycloPalloidSpiralBevelGearSetRating: 'Rating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Rating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_detailed_analysis(self) -> '_401.KlingelnbergCycloPalloidSpiralBevelGearSetRating':
        """KlingelnbergCycloPalloidSpiralBevelGearSetRating: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDetailedAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def power_flow_results(self) -> '_4051.KlingelnbergCycloPalloidSpiralBevelGearSetPowerFlow':
        """KlingelnbergCycloPalloidSpiralBevelGearSetPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gears_system_deflection(self) -> 'List[_2722.KlingelnbergCycloPalloidSpiralBevelGearSystemDeflection]':
        """List[KlingelnbergCycloPalloidSpiralBevelGearSystemDeflection]: 'KlingelnbergCycloPalloidSpiralBevelGearsSystemDeflection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.KlingelnbergCycloPalloidSpiralBevelGearsSystemDeflection

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_meshes_system_deflection(self) -> 'List[_2720.KlingelnbergCycloPalloidSpiralBevelGearMeshSystemDeflection]':
        """List[KlingelnbergCycloPalloidSpiralBevelGearMeshSystemDeflection]: 'KlingelnbergCycloPalloidSpiralBevelMeshesSystemDeflection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.KlingelnbergCycloPalloidSpiralBevelMeshesSystemDeflection

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value
