"""_1708.py

AxisSettings
"""


from typing import List

from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.python_net import python_net_import

_AXIS_SETTINGS = python_net_import('SMT.MastaAPI.Utility.Report', 'AxisSettings')


__docformat__ = 'restructuredtext en'
__all__ = ('AxisSettings',)


class AxisSettings(_0.APIBase):
    """AxisSettings

    This is a mastapy class.
    """

    TYPE = _AXIS_SETTINGS

    def __init__(self, instance_to_wrap: 'AxisSettings.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def end_value(self) -> 'float':
        """float: 'EndValue' is the original name of this property."""

        temp = self.wrapped.EndValue

        if temp is None:
            return 0.0

        return temp

    @end_value.setter
    def end_value(self, value: 'float'):
        self.wrapped.EndValue = float(value) if value else 0.0

    @property
    def hide_grid_lines(self) -> 'bool':
        """bool: 'HideGridLines' is the original name of this property."""

        temp = self.wrapped.HideGridLines

        if temp is None:
            return False

        return temp

    @hide_grid_lines.setter
    def hide_grid_lines(self, value: 'bool'):
        self.wrapped.HideGridLines = bool(value) if value else False

    @property
    def show_title(self) -> 'bool':
        """bool: 'ShowTitle' is the original name of this property."""

        temp = self.wrapped.ShowTitle

        if temp is None:
            return False

        return temp

    @show_title.setter
    def show_title(self, value: 'bool'):
        self.wrapped.ShowTitle = bool(value) if value else False

    @property
    def specify_range(self) -> 'bool':
        """bool: 'SpecifyRange' is the original name of this property."""

        temp = self.wrapped.SpecifyRange

        if temp is None:
            return False

        return temp

    @specify_range.setter
    def specify_range(self, value: 'bool'):
        self.wrapped.SpecifyRange = bool(value) if value else False

    @property
    def start_value(self) -> 'float':
        """float: 'StartValue' is the original name of this property."""

        temp = self.wrapped.StartValue

        if temp is None:
            return 0.0

        return temp

    @start_value.setter
    def start_value(self, value: 'float'):
        self.wrapped.StartValue = float(value) if value else 0.0

    @property
    def title(self) -> 'str':
        """str: 'Title' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Title

        if temp is None:
            return ''

        return temp

    @property
    def unit(self) -> 'str':
        """str: 'Unit' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Unit

        if temp is None:
            return ''

        return temp

    @property
    def custom_labels(self) -> 'List[str]':
        """List[str]: 'CustomLabels' is the original name of this property."""

        temp = self.wrapped.CustomLabels

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, str)
        return value

    @custom_labels.setter
    def custom_labels(self, value: 'List[str]'):
        value = value if value else None
        value = conversion.mp_to_pn_objects_in_list(value)
        self.wrapped.CustomLabels = value

    @property
    def report_names(self) -> 'List[str]':
        """List[str]: 'ReportNames' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ReportNames

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, str)
        return value

    def output_default_report_to(self, file_path: 'str'):
        """ 'OutputDefaultReportTo' is the original name of this method.

        Args:
            file_path (str)
        """

        file_path = str(file_path)
        self.wrapped.OutputDefaultReportTo(file_path if file_path else '')

    def get_default_report_with_encoded_images(self) -> 'str':
        """ 'GetDefaultReportWithEncodedImages' is the original name of this method.

        Returns:
            str
        """

        method_result = self.wrapped.GetDefaultReportWithEncodedImages()
        return method_result

    def output_active_report_to(self, file_path: 'str'):
        """ 'OutputActiveReportTo' is the original name of this method.

        Args:
            file_path (str)
        """

        file_path = str(file_path)
        self.wrapped.OutputActiveReportTo(file_path if file_path else '')

    def output_active_report_as_text_to(self, file_path: 'str'):
        """ 'OutputActiveReportAsTextTo' is the original name of this method.

        Args:
            file_path (str)
        """

        file_path = str(file_path)
        self.wrapped.OutputActiveReportAsTextTo(file_path if file_path else '')

    def get_active_report_with_encoded_images(self) -> 'str':
        """ 'GetActiveReportWithEncodedImages' is the original name of this method.

        Returns:
            str
        """

        method_result = self.wrapped.GetActiveReportWithEncodedImages()
        return method_result

    def output_named_report_to(self, report_name: 'str', file_path: 'str'):
        """ 'OutputNamedReportTo' is the original name of this method.

        Args:
            report_name (str)
            file_path (str)
        """

        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportTo(report_name if report_name else '', file_path if file_path else '')

    def output_named_report_as_masta_report(self, report_name: 'str', file_path: 'str'):
        """ 'OutputNamedReportAsMastaReport' is the original name of this method.

        Args:
            report_name (str)
            file_path (str)
        """

        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportAsMastaReport(report_name if report_name else '', file_path if file_path else '')

    def output_named_report_as_text_to(self, report_name: 'str', file_path: 'str'):
        """ 'OutputNamedReportAsTextTo' is the original name of this method.

        Args:
            report_name (str)
            file_path (str)
        """

        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportAsTextTo(report_name if report_name else '', file_path if file_path else '')

    def get_named_report_with_encoded_images(self, report_name: 'str') -> 'str':
        """ 'GetNamedReportWithEncodedImages' is the original name of this method.

        Args:
            report_name (str)

        Returns:
            str
        """

        report_name = str(report_name)
        method_result = self.wrapped.GetNamedReportWithEncodedImages(report_name if report_name else '')
        return method_result
