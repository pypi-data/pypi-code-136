"""_1722.py

CustomReportChartItem
"""


from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy.utility.report import _1714, _1738
from mastapy._internal.python_net import python_net_import

_CUSTOM_REPORT_CHART_ITEM = python_net_import('SMT.MastaAPI.Utility.Report', 'CustomReportChartItem')


__docformat__ = 'restructuredtext en'
__all__ = ('CustomReportChartItem',)


class CustomReportChartItem(_1738.CustomReportPropertyItem):
    """CustomReportChartItem

    This is a mastapy class.
    """

    TYPE = _CUSTOM_REPORT_CHART_ITEM

    def __init__(self, instance_to_wrap: 'CustomReportChartItem.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def has_marker(self) -> 'bool':
        """bool: 'HasMarker' is the original name of this property."""

        temp = self.wrapped.HasMarker

        if temp is None:
            return False

        return temp

    @has_marker.setter
    def has_marker(self, value: 'bool'):
        self.wrapped.HasMarker = bool(value) if value else False

    @property
    def marker_size(self) -> 'float':
        """float: 'MarkerSize' is the original name of this property."""

        temp = self.wrapped.MarkerSize

        if temp is None:
            return 0.0

        return temp

    @marker_size.setter
    def marker_size(self, value: 'float'):
        self.wrapped.MarkerSize = float(value) if value else 0.0

    @property
    def point_shape(self) -> '_1714.SMTChartPointShape':
        """SMTChartPointShape: 'PointShape' is the original name of this property."""

        temp = self.wrapped.PointShape

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp)
        return constructor.new_from_mastapy_type(_1714.SMTChartPointShape)(value) if value is not None else None

    @point_shape.setter
    def point_shape(self, value: '_1714.SMTChartPointShape'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.PointShape = value

    @property
    def smooth_lines(self) -> 'bool':
        """bool: 'SmoothLines' is the original name of this property."""

        temp = self.wrapped.SmoothLines

        if temp is None:
            return False

        return temp

    @smooth_lines.setter
    def smooth_lines(self, value: 'bool'):
        self.wrapped.SmoothLines = bool(value) if value else False
