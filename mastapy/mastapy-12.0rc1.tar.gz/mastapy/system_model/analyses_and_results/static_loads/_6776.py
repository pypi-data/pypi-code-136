"""_6776.py

ConnectorLoadCase
"""


from mastapy.system_model.part_model import _2399, _2392, _2418
from mastapy._internal import constructor
from mastapy._internal.cast_exception import CastException
from mastapy.system_model.part_model.couplings import _2549
from mastapy.system_model.analyses_and_results.static_loads import _6850
from mastapy._internal.python_net import python_net_import

_CONNECTOR_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'ConnectorLoadCase')


__docformat__ = 'restructuredtext en'
__all__ = ('ConnectorLoadCase',)


class ConnectorLoadCase(_6850.MountableComponentLoadCase):
    """ConnectorLoadCase

    This is a mastapy class.
    """

    TYPE = _CONNECTOR_LOAD_CASE

    def __init__(self, instance_to_wrap: 'ConnectorLoadCase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2399.Connector':
        """Connector: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2399.Connector.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to Connector. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_bearing(self) -> '_2392.Bearing':
        """Bearing: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2392.Bearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to Bearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_oil_seal(self) -> '_2418.OilSeal':
        """OilSeal: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2418.OilSeal.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to OilSeal. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_shaft_hub_connection(self) -> '_2549.ShaftHubConnection':
        """ShaftHubConnection: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2549.ShaftHubConnection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to ShaftHubConnection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None
