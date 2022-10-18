"""_4064.py

PowerFlow
"""


from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.system_deflections import _2778
from mastapy.system_model.analyses_and_results.analysis_cases import _7474
from mastapy._internal.python_net import python_net_import

_POWER_FLOW = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows', 'PowerFlow')


__docformat__ = 'restructuredtext en'
__all__ = ('PowerFlow',)


class PowerFlow(_7474.StaticLoadAnalysisCase):
    """PowerFlow

    This is a mastapy class.
    """

    TYPE = _POWER_FLOW

    def __init__(self, instance_to_wrap: 'PowerFlow.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def ratio(self) -> 'float':
        """float: 'Ratio' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Ratio

        if temp is None:
            return 0.0

        return temp

    @property
    def torsional_system_deflection(self) -> '_2778.TorsionalSystemDeflection':
        """TorsionalSystemDeflection: 'TorsionalSystemDeflection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TorsionalSystemDeflection

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None
