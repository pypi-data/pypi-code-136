"""_1298.py

ElectricMachineDQModel
"""


from typing import List

from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy.electric_machines import _1290
from mastapy import _0
from mastapy._internal.python_net import python_net_import

_ELECTRIC_MACHINE_DQ_MODEL = python_net_import('SMT.MastaAPI.ElectricMachines.Results', 'ElectricMachineDQModel')


__docformat__ = 'restructuredtext en'
__all__ = ('ElectricMachineDQModel',)


class ElectricMachineDQModel(_0.APIBase):
    """ElectricMachineDQModel

    This is a mastapy class.
    """

    TYPE = _ELECTRIC_MACHINE_DQ_MODEL

    def __init__(self, instance_to_wrap: 'ElectricMachineDQModel.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def current_angle_to_maximise_torque_at_maximum_current_at_reference_temperature(self) -> 'float':
        """float: 'CurrentAngleToMaximiseTorqueAtMaximumCurrentAtReferenceTemperature' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentAngleToMaximiseTorqueAtMaximumCurrentAtReferenceTemperature

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_peak_phase_current(self) -> 'float':
        """float: 'MaximumPeakPhaseCurrent' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumPeakPhaseCurrent

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_peak_phase_supply_voltage(self) -> 'float':
        """float: 'MaximumPeakPhaseSupplyVoltage' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumPeakPhaseSupplyVoltage

        if temp is None:
            return 0.0

        return temp

    @property
    def name(self) -> 'str':
        """str: 'Name' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Name

        if temp is None:
            return ''

        return temp

    @property
    def number_of_phases(self) -> 'int':
        """int: 'NumberOfPhases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NumberOfPhases

        if temp is None:
            return 0

        return temp

    @property
    def number_of_pole_pairs(self) -> 'int':
        """int: 'NumberOfPolePairs' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NumberOfPolePairs

        if temp is None:
            return 0

        return temp

    @property
    def permanent_magnet_flux_linkage_at_reference_temperature(self) -> 'float':
        """float: 'PermanentMagnetFluxLinkageAtReferenceTemperature' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PermanentMagnetFluxLinkageAtReferenceTemperature

        if temp is None:
            return 0.0

        return temp

    @property
    def phase_resistance_at_reference_temperature(self) -> 'float':
        """float: 'PhaseResistanceAtReferenceTemperature' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PhaseResistanceAtReferenceTemperature

        if temp is None:
            return 0.0

        return temp

    @property
    def steady_state_short_circuit_current_at_reference_temperature(self) -> 'float':
        """float: 'SteadyStateShortCircuitCurrentAtReferenceTemperature' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SteadyStateShortCircuitCurrentAtReferenceTemperature

        if temp is None:
            return 0.0

        return temp

    @property
    def temperature_coefficient_for_remanence(self) -> 'float':
        """float: 'TemperatureCoefficientForRemanence' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TemperatureCoefficientForRemanence

        if temp is None:
            return 0.0

        return temp

    @property
    def temperature_coefficient_for_winding_resistivity(self) -> 'float':
        """float: 'TemperatureCoefficientForWindingResistivity' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TemperatureCoefficientForWindingResistivity

        if temp is None:
            return 0.0

        return temp

    @property
    def winding_connection(self) -> '_1290.WindingConnection':
        """WindingConnection: 'WindingConnection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WindingConnection

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp)
        return constructor.new_from_mastapy_type(_1290.WindingConnection)(value) if value is not None else None

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
