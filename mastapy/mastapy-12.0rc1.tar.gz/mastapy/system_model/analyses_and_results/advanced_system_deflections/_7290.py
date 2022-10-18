"""_7290.py

RingPinsToDiscConnectionAdvancedSystemDeflection
"""


from typing import List

from mastapy._internal import constructor, conversion
from mastapy.system_model.connections_and_sockets.cycloidal import _2293
from mastapy.system_model.analyses_and_results.static_loads import _6870
from mastapy.system_model.analyses_and_results.system_deflections import _2741
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7264
from mastapy._internal.python_net import python_net_import

_RING_PINS_TO_DISC_CONNECTION_ADVANCED_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections', 'RingPinsToDiscConnectionAdvancedSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('RingPinsToDiscConnectionAdvancedSystemDeflection',)


class RingPinsToDiscConnectionAdvancedSystemDeflection(_7264.InterMountableComponentConnectionAdvancedSystemDeflection):
    """RingPinsToDiscConnectionAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _RING_PINS_TO_DISC_CONNECTION_ADVANCED_SYSTEM_DEFLECTION

    def __init__(self, instance_to_wrap: 'RingPinsToDiscConnectionAdvancedSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def average_number_of_pins_in_contact(self) -> 'float':
        """float: 'AverageNumberOfPinsInContact' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AverageNumberOfPinsInContact

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_contact_stress(self) -> 'float':
        """float: 'MaximumContactStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumContactStress

        if temp is None:
            return 0.0

        return temp

    @property
    def connection_design(self) -> '_2293.RingPinsToDiscConnection':
        """RingPinsToDiscConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_load_case(self) -> '_6870.RingPinsToDiscConnectionLoadCase':
        """RingPinsToDiscConnectionLoadCase: 'ConnectionLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_system_deflection_results(self) -> 'List[_2741.RingPinsToDiscConnectionSystemDeflection]':
        """List[RingPinsToDiscConnectionSystemDeflection]: 'ConnectionSystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionSystemDeflectionResults

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value
