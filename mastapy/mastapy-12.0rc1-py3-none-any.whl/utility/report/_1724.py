"""_1724.py

CustomReportColumns
"""


from mastapy._internal import constructor
from mastapy.utility.report import _1730, _1723
from mastapy._internal.python_net import python_net_import

_CUSTOM_REPORT_COLUMNS = python_net_import('SMT.MastaAPI.Utility.Report', 'CustomReportColumns')


__docformat__ = 'restructuredtext en'
__all__ = ('CustomReportColumns',)


class CustomReportColumns(_1730.CustomReportItemContainerCollection['_1723.CustomReportColumn']):
    """CustomReportColumns

    This is a mastapy class.
    """

    TYPE = _CUSTOM_REPORT_COLUMNS

    def __init__(self, instance_to_wrap: 'CustomReportColumns.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def number_of_columns(self) -> 'int':
        """int: 'NumberOfColumns' is the original name of this property."""

        temp = self.wrapped.NumberOfColumns

        if temp is None:
            return 0

        return temp

    @number_of_columns.setter
    def number_of_columns(self, value: 'int'):
        self.wrapped.NumberOfColumns = int(value) if value else 0

    @property
    def show_adjustable_column_divider(self) -> 'bool':
        """bool: 'ShowAdjustableColumnDivider' is the original name of this property."""

        temp = self.wrapped.ShowAdjustableColumnDivider

        if temp is None:
            return False

        return temp

    @show_adjustable_column_divider.setter
    def show_adjustable_column_divider(self, value: 'bool'):
        self.wrapped.ShowAdjustableColumnDivider = bool(value) if value else False
