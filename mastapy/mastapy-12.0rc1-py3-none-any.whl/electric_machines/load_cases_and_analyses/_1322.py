"""_1322.py

ElectricMachineBasicMechanicalLossSettings
"""


from typing import List

from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.python_net import python_net_import

_ELECTRIC_MACHINE_BASIC_MECHANICAL_LOSS_SETTINGS = python_net_import('SMT.MastaAPI.ElectricMachines.LoadCasesAndAnalyses', 'ElectricMachineBasicMechanicalLossSettings')


__docformat__ = 'restructuredtext en'
__all__ = ('ElectricMachineBasicMechanicalLossSettings',)


class ElectricMachineBasicMechanicalLossSettings(_0.APIBase):
    """ElectricMachineBasicMechanicalLossSettings

    This is a mastapy class.
    """

    TYPE = _ELECTRIC_MACHINE_BASIC_MECHANICAL_LOSS_SETTINGS

    def __init__(self, instance_to_wrap: 'ElectricMachineBasicMechanicalLossSettings.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def friction_loss_exponent(self) -> 'float':
        """float: 'FrictionLossExponent' is the original name of this property."""

        temp = self.wrapped.FrictionLossExponent

        if temp is None:
            return 0.0

        return temp

    @friction_loss_exponent.setter
    def friction_loss_exponent(self, value: 'float'):
        self.wrapped.FrictionLossExponent = float(value) if value else 0.0

    @property
    def friction_losses_at_reference_speed(self) -> 'float':
        """float: 'FrictionLossesAtReferenceSpeed' is the original name of this property."""

        temp = self.wrapped.FrictionLossesAtReferenceSpeed

        if temp is None:
            return 0.0

        return temp

    @friction_losses_at_reference_speed.setter
    def friction_losses_at_reference_speed(self, value: 'float'):
        self.wrapped.FrictionLossesAtReferenceSpeed = float(value) if value else 0.0

    @property
    def include_basic_mechanical_losses_calculation(self) -> 'bool':
        """bool: 'IncludeBasicMechanicalLossesCalculation' is the original name of this property."""

        temp = self.wrapped.IncludeBasicMechanicalLossesCalculation

        if temp is None:
            return False

        return temp

    @include_basic_mechanical_losses_calculation.setter
    def include_basic_mechanical_losses_calculation(self, value: 'bool'):
        self.wrapped.IncludeBasicMechanicalLossesCalculation = bool(value) if value else False

    @property
    def reference_speed_for_mechanical_losses(self) -> 'float':
        """float: 'ReferenceSpeedForMechanicalLosses' is the original name of this property."""

        temp = self.wrapped.ReferenceSpeedForMechanicalLosses

        if temp is None:
            return 0.0

        return temp

    @reference_speed_for_mechanical_losses.setter
    def reference_speed_for_mechanical_losses(self, value: 'float'):
        self.wrapped.ReferenceSpeedForMechanicalLosses = float(value) if value else 0.0

    @property
    def windage_loss_exponent(self) -> 'float':
        """float: 'WindageLossExponent' is the original name of this property."""

        temp = self.wrapped.WindageLossExponent

        if temp is None:
            return 0.0

        return temp

    @windage_loss_exponent.setter
    def windage_loss_exponent(self, value: 'float'):
        self.wrapped.WindageLossExponent = float(value) if value else 0.0

    @property
    def windage_loss_at_reference_speed(self) -> 'float':
        """float: 'WindageLossAtReferenceSpeed' is the original name of this property."""

        temp = self.wrapped.WindageLossAtReferenceSpeed

        if temp is None:
            return 0.0

        return temp

    @windage_loss_at_reference_speed.setter
    def windage_loss_at_reference_speed(self, value: 'float'):
        self.wrapped.WindageLossAtReferenceSpeed = float(value) if value else 0.0

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
