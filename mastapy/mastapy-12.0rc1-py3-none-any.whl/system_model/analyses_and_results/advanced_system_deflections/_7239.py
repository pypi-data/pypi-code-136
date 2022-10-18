"""_7239.py

CVTBeltConnectionAdvancedSystemDeflection
"""


from mastapy.system_model.connections_and_sockets import _2225
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7206
from mastapy._internal.python_net import python_net_import

_CVT_BELT_CONNECTION_ADVANCED_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections', 'CVTBeltConnectionAdvancedSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('CVTBeltConnectionAdvancedSystemDeflection',)


class CVTBeltConnectionAdvancedSystemDeflection(_7206.BeltConnectionAdvancedSystemDeflection):
    """CVTBeltConnectionAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _CVT_BELT_CONNECTION_ADVANCED_SYSTEM_DEFLECTION

    def __init__(self, instance_to_wrap: 'CVTBeltConnectionAdvancedSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self) -> '_2225.CVTBeltConnection':
        """CVTBeltConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None
