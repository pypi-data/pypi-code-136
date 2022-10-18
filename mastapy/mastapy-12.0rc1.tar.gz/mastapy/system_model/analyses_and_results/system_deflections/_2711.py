"""_2711.py

HypoidGearSystemDeflection
"""


from mastapy.system_model.part_model.gears import _2485
from mastapy._internal import constructor
from mastapy.gears.rating.hypoid import _433
from mastapy.system_model.analyses_and_results.static_loads import _6831
from mastapy.system_model.analyses_and_results.power_flows import _4040
from mastapy.system_model.analyses_and_results.system_deflections import _2642
from mastapy._internal.python_net import python_net_import

_HYPOID_GEAR_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections', 'HypoidGearSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('HypoidGearSystemDeflection',)


class HypoidGearSystemDeflection(_2642.AGMAGleasonConicalGearSystemDeflection):
    """HypoidGearSystemDeflection

    This is a mastapy class.
    """

    TYPE = _HYPOID_GEAR_SYSTEM_DEFLECTION

    def __init__(self, instance_to_wrap: 'HypoidGearSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2485.HypoidGear':
        """HypoidGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_detailed_analysis(self) -> '_433.HypoidGearRating':
        """HypoidGearRating: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDetailedAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_load_case(self) -> '_6831.HypoidGearLoadCase':
        """HypoidGearLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def power_flow_results(self) -> '_4040.HypoidGearPowerFlow':
        """HypoidGearPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None
