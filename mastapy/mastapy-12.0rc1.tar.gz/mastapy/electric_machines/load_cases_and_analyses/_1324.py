"""_1324.py

ElectricMachineEfficiencyMapSettings
"""


from typing import List

from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.python_net import python_net_import

_ELECTRIC_MACHINE_EFFICIENCY_MAP_SETTINGS = python_net_import('SMT.MastaAPI.ElectricMachines.LoadCasesAndAnalyses', 'ElectricMachineEfficiencyMapSettings')


__docformat__ = 'restructuredtext en'
__all__ = ('ElectricMachineEfficiencyMapSettings',)


class ElectricMachineEfficiencyMapSettings(_0.APIBase):
    """ElectricMachineEfficiencyMapSettings

    This is a mastapy class.
    """

    TYPE = _ELECTRIC_MACHINE_EFFICIENCY_MAP_SETTINGS

    def __init__(self, instance_to_wrap: 'ElectricMachineEfficiencyMapSettings.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def maximum_speed(self) -> 'float':
        """float: 'MaximumSpeed' is the original name of this property."""

        temp = self.wrapped.MaximumSpeed

        if temp is None:
            return 0.0

        return temp

    @maximum_speed.setter
    def maximum_speed(self, value: 'float'):
        self.wrapped.MaximumSpeed = float(value) if value else 0.0

    @property
    def minimum_speed(self) -> 'float':
        """float: 'MinimumSpeed' is the original name of this property."""

        temp = self.wrapped.MinimumSpeed

        if temp is None:
            return 0.0

        return temp

    @minimum_speed.setter
    def minimum_speed(self, value: 'float'):
        self.wrapped.MinimumSpeed = float(value) if value else 0.0

    @property
    def minimum_torque(self) -> 'float':
        """float: 'MinimumTorque' is the original name of this property."""

        temp = self.wrapped.MinimumTorque

        if temp is None:
            return 0.0

        return temp

    @minimum_torque.setter
    def minimum_torque(self, value: 'float'):
        self.wrapped.MinimumTorque = float(value) if value else 0.0

    @property
    def number_of_speed_values(self) -> 'int':
        """int: 'NumberOfSpeedValues' is the original name of this property."""

        temp = self.wrapped.NumberOfSpeedValues

        if temp is None:
            return 0

        return temp

    @number_of_speed_values.setter
    def number_of_speed_values(self, value: 'int'):
        self.wrapped.NumberOfSpeedValues = int(value) if value else 0

    @property
    def number_of_torque_values(self) -> 'int':
        """int: 'NumberOfTorqueValues' is the original name of this property."""

        temp = self.wrapped.NumberOfTorqueValues

        if temp is None:
            return 0

        return temp

    @number_of_torque_values.setter
    def number_of_torque_values(self, value: 'int'):
        self.wrapped.NumberOfTorqueValues = int(value) if value else 0

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
