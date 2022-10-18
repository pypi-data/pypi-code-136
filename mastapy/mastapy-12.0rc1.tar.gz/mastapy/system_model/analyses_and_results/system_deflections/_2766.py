"""_2766.py

StraightBevelSunGearSystemDeflection
"""


from mastapy.system_model.part_model.gears import _2501
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.power_flows import _4091
from mastapy.system_model.analyses_and_results.system_deflections import _2761
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_SUN_GEAR_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections', 'StraightBevelSunGearSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('StraightBevelSunGearSystemDeflection',)


class StraightBevelSunGearSystemDeflection(_2761.StraightBevelDiffGearSystemDeflection):
    """StraightBevelSunGearSystemDeflection

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_SUN_GEAR_SYSTEM_DEFLECTION

    def __init__(self, instance_to_wrap: 'StraightBevelSunGearSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2501.StraightBevelSunGear':
        """StraightBevelSunGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def power_flow_results(self) -> '_4091.StraightBevelSunGearPowerFlow':
        """StraightBevelSunGearPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None
