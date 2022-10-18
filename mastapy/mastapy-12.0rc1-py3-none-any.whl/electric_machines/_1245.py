"""_1245.py

CoreLossCoefficients
"""


from typing import List

from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.python_net import python_net_import

_CORE_LOSS_COEFFICIENTS = python_net_import('SMT.MastaAPI.ElectricMachines', 'CoreLossCoefficients')


__docformat__ = 'restructuredtext en'
__all__ = ('CoreLossCoefficients',)


class CoreLossCoefficients(_0.APIBase):
    """CoreLossCoefficients

    This is a mastapy class.
    """

    TYPE = _CORE_LOSS_COEFFICIENTS

    def __init__(self, instance_to_wrap: 'CoreLossCoefficients.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def c_coefficient_eddy(self) -> 'float':
        """float: 'CCoefficientEddy' is the original name of this property."""

        temp = self.wrapped.CCoefficientEddy

        if temp is None:
            return 0.0

        return temp

    @c_coefficient_eddy.setter
    def c_coefficient_eddy(self, value: 'float'):
        self.wrapped.CCoefficientEddy = float(value) if value else 0.0

    @property
    def c_coefficient_excess(self) -> 'float':
        """float: 'CCoefficientExcess' is the original name of this property."""

        temp = self.wrapped.CCoefficientExcess

        if temp is None:
            return 0.0

        return temp

    @c_coefficient_excess.setter
    def c_coefficient_excess(self, value: 'float'):
        self.wrapped.CCoefficientExcess = float(value) if value else 0.0

    @property
    def c_coefficient_hysteresis(self) -> 'float':
        """float: 'CCoefficientHysteresis' is the original name of this property."""

        temp = self.wrapped.CCoefficientHysteresis

        if temp is None:
            return 0.0

        return temp

    @c_coefficient_hysteresis.setter
    def c_coefficient_hysteresis(self, value: 'float'):
        self.wrapped.CCoefficientHysteresis = float(value) if value else 0.0

    @property
    def field_exponent_eddy(self) -> 'float':
        """float: 'FieldExponentEddy' is the original name of this property."""

        temp = self.wrapped.FieldExponentEddy

        if temp is None:
            return 0.0

        return temp

    @field_exponent_eddy.setter
    def field_exponent_eddy(self, value: 'float'):
        self.wrapped.FieldExponentEddy = float(value) if value else 0.0

    @property
    def field_exponent_excess(self) -> 'float':
        """float: 'FieldExponentExcess' is the original name of this property."""

        temp = self.wrapped.FieldExponentExcess

        if temp is None:
            return 0.0

        return temp

    @field_exponent_excess.setter
    def field_exponent_excess(self, value: 'float'):
        self.wrapped.FieldExponentExcess = float(value) if value else 0.0

    @property
    def field_exponent_hysteresis(self) -> 'float':
        """float: 'FieldExponentHysteresis' is the original name of this property."""

        temp = self.wrapped.FieldExponentHysteresis

        if temp is None:
            return 0.0

        return temp

    @field_exponent_hysteresis.setter
    def field_exponent_hysteresis(self, value: 'float'):
        self.wrapped.FieldExponentHysteresis = float(value) if value else 0.0

    @property
    def frequency_exponent_eddy(self) -> 'float':
        """float: 'FrequencyExponentEddy' is the original name of this property."""

        temp = self.wrapped.FrequencyExponentEddy

        if temp is None:
            return 0.0

        return temp

    @frequency_exponent_eddy.setter
    def frequency_exponent_eddy(self, value: 'float'):
        self.wrapped.FrequencyExponentEddy = float(value) if value else 0.0

    @property
    def frequency_exponent_excess(self) -> 'float':
        """float: 'FrequencyExponentExcess' is the original name of this property."""

        temp = self.wrapped.FrequencyExponentExcess

        if temp is None:
            return 0.0

        return temp

    @frequency_exponent_excess.setter
    def frequency_exponent_excess(self, value: 'float'):
        self.wrapped.FrequencyExponentExcess = float(value) if value else 0.0

    @property
    def frequency_exponent_hysteresis(self) -> 'float':
        """float: 'FrequencyExponentHysteresis' is the original name of this property."""

        temp = self.wrapped.FrequencyExponentHysteresis

        if temp is None:
            return 0.0

        return temp

    @frequency_exponent_hysteresis.setter
    def frequency_exponent_hysteresis(self, value: 'float'):
        self.wrapped.FrequencyExponentHysteresis = float(value) if value else 0.0

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
