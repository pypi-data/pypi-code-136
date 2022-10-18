"""_1812.py

DataLoggerWithCharts
"""


from typing import List

from mastapy.utility_gui import _1811
from mastapy._internal import constructor, conversion
from mastapy.math_utility.convergence import _1540
from mastapy._internal.python_net import python_net_import

_DATA_LOGGER_WITH_CHARTS = python_net_import('SMT.MastaAPI.UtilityGUI', 'DataLoggerWithCharts')


__docformat__ = 'restructuredtext en'
__all__ = ('DataLoggerWithCharts',)


class DataLoggerWithCharts(_1540.DataLogger):
    """DataLoggerWithCharts

    This is a mastapy class.
    """

    TYPE = _DATA_LOGGER_WITH_CHARTS

    def __init__(self, instance_to_wrap: 'DataLoggerWithCharts.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def logged_items(self) -> 'List[_1811.DataLoggerItem]':
        """List[DataLoggerItem]: 'LoggedItems' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LoggedItems

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value
