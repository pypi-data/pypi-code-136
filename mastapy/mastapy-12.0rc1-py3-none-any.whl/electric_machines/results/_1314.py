"""_1314.py

NonLinearDQModelSettings
"""


from typing import List

from mastapy._internal import constructor, conversion
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.electric_machines.load_cases_and_analyses import _1345
from mastapy import _0
from mastapy._internal.python_net import python_net_import

_NON_LINEAR_DQ_MODEL_SETTINGS = python_net_import('SMT.MastaAPI.ElectricMachines.Results', 'NonLinearDQModelSettings')


__docformat__ = 'restructuredtext en'
__all__ = ('NonLinearDQModelSettings',)


class NonLinearDQModelSettings(_0.APIBase):
    """NonLinearDQModelSettings

    This is a mastapy class.
    """

    TYPE = _NON_LINEAR_DQ_MODEL_SETTINGS

    def __init__(self, instance_to_wrap: 'NonLinearDQModelSettings.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def copy_all_setups(self) -> 'bool':
        """bool: 'CopyAllSetups' is the original name of this property."""

        temp = self.wrapped.CopyAllSetups

        if temp is None:
            return False

        return temp

    @copy_all_setups.setter
    def copy_all_setups(self, value: 'bool'):
        self.wrapped.CopyAllSetups = bool(value) if value else False

    @property
    def include_efficiency(self) -> 'bool':
        """bool: 'IncludeEfficiency' is the original name of this property."""

        temp = self.wrapped.IncludeEfficiency

        if temp is None:
            return False

        return temp

    @include_efficiency.setter
    def include_efficiency(self, value: 'bool'):
        self.wrapped.IncludeEfficiency = bool(value) if value else False

    @property
    def maximum_current_angle_for_map(self) -> 'float':
        """float: 'MaximumCurrentAngleForMap' is the original name of this property."""

        temp = self.wrapped.MaximumCurrentAngleForMap

        if temp is None:
            return 0.0

        return temp

    @maximum_current_angle_for_map.setter
    def maximum_current_angle_for_map(self, value: 'float'):
        self.wrapped.MaximumCurrentAngleForMap = float(value) if value else 0.0

    @property
    def maximum_peak_line_current_magnitude_for_map(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'MaximumPeakLineCurrentMagnitudeForMap' is the original name of this property."""

        temp = self.wrapped.MaximumPeakLineCurrentMagnitudeForMap

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @maximum_peak_line_current_magnitude_for_map.setter
    def maximum_peak_line_current_magnitude_for_map(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.MaximumPeakLineCurrentMagnitudeForMap = value

    @property
    def minimum_current_angle_for_map(self) -> 'float':
        """float: 'MinimumCurrentAngleForMap' is the original name of this property."""

        temp = self.wrapped.MinimumCurrentAngleForMap

        if temp is None:
            return 0.0

        return temp

    @minimum_current_angle_for_map.setter
    def minimum_current_angle_for_map(self, value: 'float'):
        self.wrapped.MinimumCurrentAngleForMap = float(value) if value else 0.0

    @property
    def minimum_peak_line_current_magnitude_for_map(self) -> 'float':
        """float: 'MinimumPeakLineCurrentMagnitudeForMap' is the original name of this property."""

        temp = self.wrapped.MinimumPeakLineCurrentMagnitudeForMap

        if temp is None:
            return 0.0

        return temp

    @minimum_peak_line_current_magnitude_for_map.setter
    def minimum_peak_line_current_magnitude_for_map(self, value: 'float'):
        self.wrapped.MinimumPeakLineCurrentMagnitudeForMap = float(value) if value else 0.0

    @property
    def non_linear_system_convergence_tolerance(self) -> 'float':
        """float: 'NonLinearSystemConvergenceTolerance' is the original name of this property."""

        temp = self.wrapped.NonLinearSystemConvergenceTolerance

        if temp is None:
            return 0.0

        return temp

    @non_linear_system_convergence_tolerance.setter
    def non_linear_system_convergence_tolerance(self, value: 'float'):
        self.wrapped.NonLinearSystemConvergenceTolerance = float(value) if value else 0.0

    @property
    def number_of_current_angle_points(self) -> 'int':
        """int: 'NumberOfCurrentAnglePoints' is the original name of this property."""

        temp = self.wrapped.NumberOfCurrentAnglePoints

        if temp is None:
            return 0

        return temp

    @number_of_current_angle_points.setter
    def number_of_current_angle_points(self, value: 'int'):
        self.wrapped.NumberOfCurrentAnglePoints = int(value) if value else 0

    @property
    def number_of_current_magnitude_points(self) -> 'int':
        """int: 'NumberOfCurrentMagnitudePoints' is the original name of this property."""

        temp = self.wrapped.NumberOfCurrentMagnitudePoints

        if temp is None:
            return 0

        return temp

    @number_of_current_magnitude_points.setter
    def number_of_current_magnitude_points(self, value: 'int'):
        self.wrapped.NumberOfCurrentMagnitudePoints = int(value) if value else 0

    @property
    def number_of_time_steps_for_half_electrical_period(self) -> 'int':
        """int: 'NumberOfTimeStepsForHalfElectricalPeriod' is the original name of this property."""

        temp = self.wrapped.NumberOfTimeStepsForHalfElectricalPeriod

        if temp is None:
            return 0

        return temp

    @number_of_time_steps_for_half_electrical_period.setter
    def number_of_time_steps_for_half_electrical_period(self, value: 'int'):
        self.wrapped.NumberOfTimeStepsForHalfElectricalPeriod = int(value) if value else 0

    @property
    def reference_speed(self) -> 'float':
        """float: 'ReferenceSpeed' is the original name of this property."""

        temp = self.wrapped.ReferenceSpeed

        if temp is None:
            return 0.0

        return temp

    @reference_speed.setter
    def reference_speed(self, value: 'float'):
        self.wrapped.ReferenceSpeed = float(value) if value else 0.0

    @property
    def temperatures(self) -> '_1345.Temperatures':
        """Temperatures: 'Temperatures' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Temperatures

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

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
