"""_1301.py

ElectricMachineResultsForOpenCircuitAndOnLoad
"""


from typing import List

from PIL.Image import Image

from mastapy._internal import constructor, conversion
from mastapy.utility_gui.charts import (
    _1827, _1813, _1820, _1822
)
from mastapy._internal.cast_exception import CastException
from mastapy.electric_machines.results import _1315, _1316
from mastapy import _0
from mastapy._internal.python_net import python_net_import

_ELECTRIC_MACHINE_RESULTS_FOR_OPEN_CIRCUIT_AND_ON_LOAD = python_net_import('SMT.MastaAPI.ElectricMachines.Results', 'ElectricMachineResultsForOpenCircuitAndOnLoad')


__docformat__ = 'restructuredtext en'
__all__ = ('ElectricMachineResultsForOpenCircuitAndOnLoad',)


class ElectricMachineResultsForOpenCircuitAndOnLoad(_0.APIBase):
    """ElectricMachineResultsForOpenCircuitAndOnLoad

    This is a mastapy class.
    """

    TYPE = _ELECTRIC_MACHINE_RESULTS_FOR_OPEN_CIRCUIT_AND_ON_LOAD

    def __init__(self, instance_to_wrap: 'ElectricMachineResultsForOpenCircuitAndOnLoad.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def apparent_d_axis_inductance(self) -> 'float':
        """float: 'ApparentDAxisInductance' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ApparentDAxisInductance

        if temp is None:
            return 0.0

        return temp

    @property
    def apparent_inductance_multiplied_by_current_d_axis(self) -> 'float':
        """float: 'ApparentInductanceMultipliedByCurrentDAxis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ApparentInductanceMultipliedByCurrentDAxis

        if temp is None:
            return 0.0

        return temp

    @property
    def apparent_inductance_multiplied_by_current_q_axis(self) -> 'float':
        """float: 'ApparentInductanceMultipliedByCurrentQAxis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ApparentInductanceMultipliedByCurrentQAxis

        if temp is None:
            return 0.0

        return temp

    @property
    def apparent_q_axis_inductance(self) -> 'float':
        """float: 'ApparentQAxisInductance' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ApparentQAxisInductance

        if temp is None:
            return 0.0

        return temp

    @property
    def average_alignment_torque_dq(self) -> 'float':
        """float: 'AverageAlignmentTorqueDQ' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AverageAlignmentTorqueDQ

        if temp is None:
            return 0.0

        return temp

    @property
    def average_reluctance_torque_dq(self) -> 'float':
        """float: 'AverageReluctanceTorqueDQ' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AverageReluctanceTorqueDQ

        if temp is None:
            return 0.0

        return temp

    @property
    def base_speed_dq(self) -> 'float':
        """float: 'BaseSpeedDQ' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BaseSpeedDQ

        if temp is None:
            return 0.0

        return temp

    @property
    def current_angle_for_maximum_torque_dq(self) -> 'float':
        """float: 'CurrentAngleForMaximumTorqueDQ' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentAngleForMaximumTorqueDQ

        if temp is None:
            return 0.0

        return temp

    @property
    def d_axis_armature_flux_linkage(self) -> 'float':
        """float: 'DAxisArmatureFluxLinkage' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DAxisArmatureFluxLinkage

        if temp is None:
            return 0.0

        return temp

    @property
    def electrical_constant(self) -> 'float':
        """float: 'ElectricalConstant' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ElectricalConstant

        if temp is None:
            return 0.0

        return temp

    @property
    def line_line_inductance(self) -> 'float':
        """float: 'LineLineInductance' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LineLineInductance

        if temp is None:
            return 0.0

        return temp

    @property
    def linear_dq_model_chart(self) -> '_1827.TwoDChartDefinition':
        """TwoDChartDefinition: 'LinearDQModelChart' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LinearDQModelChart

        if temp is None:
            return None

        if _1827.TwoDChartDefinition.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast linear_dq_model_chart to TwoDChartDefinition. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def load_angle_from_phasor(self) -> 'float':
        """float: 'LoadAngleFromPhasor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LoadAngleFromPhasor

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_speed_dq(self) -> 'float':
        """float: 'MaximumSpeedDQ' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumSpeedDQ

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_torque_achievable_dq(self) -> 'float':
        """float: 'MaximumTorqueAchievableDQ' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumTorqueAchievableDQ

        if temp is None:
            return 0.0

        return temp

    @property
    def mechanical_time_constant(self) -> 'float':
        """float: 'MechanicalTimeConstant' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MechanicalTimeConstant

        if temp is None:
            return 0.0

        return temp

    @property
    def permanent_magnet_flux_linkage(self) -> 'float':
        """float: 'PermanentMagnetFluxLinkage' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PermanentMagnetFluxLinkage

        if temp is None:
            return 0.0

        return temp

    @property
    def phase_reactive_voltage_drms(self) -> 'float':
        """float: 'PhaseReactiveVoltageDRMS' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PhaseReactiveVoltageDRMS

        if temp is None:
            return 0.0

        return temp

    @property
    def phase_reactive_voltage_qrms(self) -> 'float':
        """float: 'PhaseReactiveVoltageQRMS' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PhaseReactiveVoltageQRMS

        if temp is None:
            return 0.0

        return temp

    @property
    def phase_terminal_voltage_from_phasor_rms(self) -> 'float':
        """float: 'PhaseTerminalVoltageFromPhasorRMS' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PhaseTerminalVoltageFromPhasorRMS

        if temp is None:
            return 0.0

        return temp

    @property
    def phasor_diagram(self) -> 'Image':
        """Image: 'PhasorDiagram' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PhasorDiagram

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)
        return value

    @property
    def power_factor_angle_from_phasor(self) -> 'float':
        """float: 'PowerFactorAngleFromPhasor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFactorAngleFromPhasor

        if temp is None:
            return 0.0

        return temp

    @property
    def q_axis_armature_flux_linkage(self) -> 'float':
        """float: 'QAxisArmatureFluxLinkage' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.QAxisArmatureFluxLinkage

        if temp is None:
            return 0.0

        return temp

    @property
    def steady_state_short_circuit_current(self) -> 'float':
        """float: 'SteadyStateShortCircuitCurrent' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SteadyStateShortCircuitCurrent

        if temp is None:
            return 0.0

        return temp

    @property
    def on_load_results(self) -> '_1315.OnLoadElectricMachineResults':
        """OnLoadElectricMachineResults: 'OnLoadResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OnLoadResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def open_circuit_results(self) -> '_1316.OpenCircuitElectricMachineResults':
        """OpenCircuitElectricMachineResults: 'OpenCircuitResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OpenCircuitResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def all_on_load_results(self) -> 'List[_1315.OnLoadElectricMachineResults]':
        """List[OnLoadElectricMachineResults]: 'AllOnLoadResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AllOnLoadResults

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def all_open_circuit_results(self) -> 'List[_1316.OpenCircuitElectricMachineResults]':
        """List[OpenCircuitElectricMachineResults]: 'AllOpenCircuitResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AllOpenCircuitResults

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def on_load_results_for_slices(self) -> 'List[_1315.OnLoadElectricMachineResults]':
        """List[OnLoadElectricMachineResults]: 'OnLoadResultsForSlices' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OnLoadResultsForSlices

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def open_circuit_results_for_slices(self) -> 'List[_1316.OpenCircuitElectricMachineResults]':
        """List[OpenCircuitElectricMachineResults]: 'OpenCircuitResultsForSlices' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OpenCircuitResultsForSlices

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

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
