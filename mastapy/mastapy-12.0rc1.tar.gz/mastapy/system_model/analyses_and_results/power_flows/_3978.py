"""_3978.py

AbstractShaftPowerFlow
"""


from mastapy.system_model.part_model import _2388
from mastapy._internal import constructor
from mastapy.system_model.part_model.shaft_model import _2434
from mastapy._internal.cast_exception import CastException
from mastapy.system_model.part_model.cycloidal import _2520
from mastapy.system_model.analyses_and_results.power_flows import _3977
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_POWER_FLOW = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows', 'AbstractShaftPowerFlow')


__docformat__ = 'restructuredtext en'
__all__ = ('AbstractShaftPowerFlow',)


class AbstractShaftPowerFlow(_3977.AbstractShaftOrHousingPowerFlow):
    """AbstractShaftPowerFlow

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_POWER_FLOW

    def __init__(self, instance_to_wrap: 'AbstractShaftPowerFlow.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2388.AbstractShaft':
        """AbstractShaft: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2388.AbstractShaft.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to AbstractShaft. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_shaft(self) -> '_2434.Shaft':
        """Shaft: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2434.Shaft.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to Shaft. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_cycloidal_disc(self) -> '_2520.CycloidalDisc':
        """CycloidalDisc: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2520.CycloidalDisc.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to CycloidalDisc. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None
