"""_1819.py

NDChartDefinition
"""


from mastapy._internal import constructor
from mastapy.utility.report import _1708, _1713
from mastapy._internal.python_net import python_net_import

_ND_CHART_DEFINITION = python_net_import('SMT.MastaAPI.UtilityGUI.Charts', 'NDChartDefinition')


__docformat__ = 'restructuredtext en'
__all__ = ('NDChartDefinition',)


class NDChartDefinition(_1713.ChartDefinition):
    """NDChartDefinition

    This is a mastapy class.
    """

    TYPE = _ND_CHART_DEFINITION

    def __init__(self, instance_to_wrap: 'NDChartDefinition.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def specify_shared_chart_settings(self) -> 'bool':
        """bool: 'SpecifySharedChartSettings' is the original name of this property."""

        temp = self.wrapped.SpecifySharedChartSettings

        if temp is None:
            return False

        return temp

    @specify_shared_chart_settings.setter
    def specify_shared_chart_settings(self, value: 'bool'):
        self.wrapped.SpecifySharedChartSettings = bool(value) if value else False

    @property
    def x_axis(self) -> '_1708.AxisSettings':
        """AxisSettings: 'XAxis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.XAxis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def y_axis(self) -> '_1708.AxisSettings':
        """AxisSettings: 'YAxis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.YAxis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None
