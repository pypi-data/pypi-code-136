"""_4000.py

CoaxialConnectionPowerFlow
"""


from mastapy.system_model.connections_and_sockets import _2221
from mastapy._internal import constructor
from mastapy.system_model.connections_and_sockets.cycloidal import _2287
from mastapy._internal.cast_exception import CastException
from mastapy.system_model.analyses_and_results.static_loads import _6762, _6784
from mastapy.system_model.analyses_and_results.power_flows import _4076
from mastapy._internal.python_net import python_net_import

_COAXIAL_CONNECTION_POWER_FLOW = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows', 'CoaxialConnectionPowerFlow')


__docformat__ = 'restructuredtext en'
__all__ = ('CoaxialConnectionPowerFlow',)


class CoaxialConnectionPowerFlow(_4076.ShaftToMountableComponentConnectionPowerFlow):
    """CoaxialConnectionPowerFlow

    This is a mastapy class.
    """

    TYPE = _COAXIAL_CONNECTION_POWER_FLOW

    def __init__(self, instance_to_wrap: 'CoaxialConnectionPowerFlow.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self) -> '_2221.CoaxialConnection':
        """CoaxialConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        if _2221.CoaxialConnection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast connection_design to CoaxialConnection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_load_case(self) -> '_6762.CoaxialConnectionLoadCase':
        """CoaxialConnectionLoadCase: 'ConnectionLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        if _6762.CoaxialConnectionLoadCase.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast connection_load_case to CoaxialConnectionLoadCase. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None
