"""_1822.py

ScatterChartDefinition
"""


from typing import List

from mastapy._internal import constructor, conversion
from mastapy.utility_gui.charts import _1827
from mastapy._internal.python_net import python_net_import

_SCATTER_CHART_DEFINITION = python_net_import('SMT.MastaAPI.UtilityGUI.Charts', 'ScatterChartDefinition')


__docformat__ = 'restructuredtext en'
__all__ = ('ScatterChartDefinition',)


class ScatterChartDefinition(_1827.TwoDChartDefinition):
    """ScatterChartDefinition

    This is a mastapy class.
    """

    TYPE = _SCATTER_CHART_DEFINITION

    def __init__(self, instance_to_wrap: 'ScatterChartDefinition.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def x_values(self) -> 'List[float]':
        """List[float]: 'XValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.XValues

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, float)
        return value

    @property
    def y_values(self) -> 'List[float]':
        """List[float]: 'YValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.YValues

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, float)
        return value

    @property
    def z_axis_title(self) -> 'str':
        """str: 'ZAxisTitle' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ZAxisTitle

        if temp is None:
            return ''

        return temp

    @property
    def z_values(self) -> 'List[float]':
        """List[float]: 'ZValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ZValues

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, float)
        return value
