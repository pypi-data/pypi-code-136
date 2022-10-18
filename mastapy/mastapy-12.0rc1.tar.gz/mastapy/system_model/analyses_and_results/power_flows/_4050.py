"""_4050.py

KlingelnbergCycloPalloidSpiralBevelGearPowerFlow
"""


from mastapy.system_model.part_model.gears import _2491
from mastapy._internal import constructor
from mastapy.gears.rating.klingelnberg_spiral_bevel import _400
from mastapy.system_model.analyses_and_results.static_loads import _6844
from mastapy.system_model.analyses_and_results.power_flows import _4044
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_POWER_FLOW = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows', 'KlingelnbergCycloPalloidSpiralBevelGearPowerFlow')


__docformat__ = 'restructuredtext en'
__all__ = ('KlingelnbergCycloPalloidSpiralBevelGearPowerFlow',)


class KlingelnbergCycloPalloidSpiralBevelGearPowerFlow(_4044.KlingelnbergCycloPalloidConicalGearPowerFlow):
    """KlingelnbergCycloPalloidSpiralBevelGearPowerFlow

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_POWER_FLOW

    def __init__(self, instance_to_wrap: 'KlingelnbergCycloPalloidSpiralBevelGearPowerFlow.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2491.KlingelnbergCycloPalloidSpiralBevelGear':
        """KlingelnbergCycloPalloidSpiralBevelGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_detailed_analysis(self) -> '_400.KlingelnbergCycloPalloidSpiralBevelGearRating':
        """KlingelnbergCycloPalloidSpiralBevelGearRating: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDetailedAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_load_case(self) -> '_6844.KlingelnbergCycloPalloidSpiralBevelGearLoadCase':
        """KlingelnbergCycloPalloidSpiralBevelGearLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None
