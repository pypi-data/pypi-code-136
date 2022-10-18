"""_4025.py

CylindricalGearPowerFlow
"""


from mastapy.system_model.part_model.gears import _2476, _2478
from mastapy._internal import constructor
from mastapy._internal.cast_exception import CastException
from mastapy.gears.rating.cylindrical import _454
from mastapy.system_model.analyses_and_results.static_loads import _6787, _6792
from mastapy.system_model.analyses_and_results.power_flows import _4036
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_POWER_FLOW = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows', 'CylindricalGearPowerFlow')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearPowerFlow',)


class CylindricalGearPowerFlow(_4036.GearPowerFlow):
    """CylindricalGearPowerFlow

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_POWER_FLOW

    def __init__(self, instance_to_wrap: 'CylindricalGearPowerFlow.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2476.CylindricalGear':
        """CylindricalGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2476.CylindricalGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to CylindricalGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_detailed_analysis(self) -> '_454.CylindricalGearRating':
        """CylindricalGearRating: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDetailedAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_load_case(self) -> '_6787.CylindricalGearLoadCase':
        """CylindricalGearLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        if _6787.CylindricalGearLoadCase.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_load_case to CylindricalGearLoadCase. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None
