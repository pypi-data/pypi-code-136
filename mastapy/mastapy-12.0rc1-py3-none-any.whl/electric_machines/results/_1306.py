"""_1306.py

ElectricMachineResultsTimeStep
"""


from typing import List

from mastapy._internal import constructor, conversion
from mastapy.utility_gui.charts import (
    _1827, _1813, _1820, _1822
)
from mastapy._internal.cast_exception import CastException
from mastapy.electric_machines.results import (
    _1304, _1307, _1305, _1303
)
from mastapy._math.vector_2d import Vector2D
from mastapy import _0
from mastapy._internal.python_net import python_net_import

_ELECTRIC_MACHINE_RESULTS_TIME_STEP = python_net_import('SMT.MastaAPI.ElectricMachines.Results', 'ElectricMachineResultsTimeStep')


__docformat__ = 'restructuredtext en'
__all__ = ('ElectricMachineResultsTimeStep',)


class ElectricMachineResultsTimeStep(_0.APIBase):
    """ElectricMachineResultsTimeStep

    This is a mastapy class.
    """

    TYPE = _ELECTRIC_MACHINE_RESULTS_TIME_STEP

    def __init__(self, instance_to_wrap: 'ElectricMachineResultsTimeStep.TYPE'):
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
    def d_axis_flux_linkage(self) -> 'float':
        """float: 'DAxisFluxLinkage' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DAxisFluxLinkage

        if temp is None:
            return 0.0

        return temp

    @property
    def d_axis_reactive_voltages(self) -> 'float':
        """float: 'DAxisReactiveVoltages' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DAxisReactiveVoltages

        if temp is None:
            return 0.0

        return temp

    @property
    def d_axis_resistive_voltage(self) -> 'float':
        """float: 'DAxisResistiveVoltage' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DAxisResistiveVoltage

        if temp is None:
            return 0.0

        return temp

    @property
    def d_axis_terminal_voltages(self) -> 'float':
        """float: 'DAxisTerminalVoltages' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DAxisTerminalVoltages

        if temp is None:
            return 0.0

        return temp

    @property
    def electrical_angle(self) -> 'float':
        """float: 'ElectricalAngle' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ElectricalAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def flux_density_in_air_gap_chart(self) -> '_1827.TwoDChartDefinition':
        """TwoDChartDefinition: 'FluxDensityInAirGapChart' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FluxDensityInAirGapChart

        if temp is None:
            return None

        if _1827.TwoDChartDefinition.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast flux_density_in_air_gap_chart to TwoDChartDefinition. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def force_density_in_air_gap_mst_chart(self) -> '_1827.TwoDChartDefinition':
        """TwoDChartDefinition: 'ForceDensityInAirGapMSTChart' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ForceDensityInAirGapMSTChart

        if temp is None:
            return None

        if _1827.TwoDChartDefinition.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast force_density_in_air_gap_mst_chart to TwoDChartDefinition. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def mechanical_angle(self) -> 'float':
        """float: 'MechanicalAngle' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MechanicalAngle

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
    def q_axis_flux_linkage(self) -> 'float':
        """float: 'QAxisFluxLinkage' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.QAxisFluxLinkage

        if temp is None:
            return 0.0

        return temp

    @property
    def q_axis_reactive_voltages(self) -> 'float':
        """float: 'QAxisReactiveVoltages' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.QAxisReactiveVoltages

        if temp is None:
            return 0.0

        return temp

    @property
    def q_axis_resistive_voltage(self) -> 'float':
        """float: 'QAxisResistiveVoltage' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.QAxisResistiveVoltage

        if temp is None:
            return 0.0

        return temp

    @property
    def q_axis_terminal_voltages(self) -> 'float':
        """float: 'QAxisTerminalVoltages' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.QAxisTerminalVoltages

        if temp is None:
            return 0.0

        return temp

    @property
    def rotor_resultant_x_force_mst_single_contour(self) -> 'float':
        """float: 'RotorResultantXForceMSTSingleContour' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RotorResultantXForceMSTSingleContour

        if temp is None:
            return 0.0

        return temp

    @property
    def rotor_resultant_y_force_mst_single_contour(self) -> 'float':
        """float: 'RotorResultantYForceMSTSingleContour' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RotorResultantYForceMSTSingleContour

        if temp is None:
            return 0.0

        return temp

    @property
    def time(self) -> 'float':
        """float: 'Time' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Time

        if temp is None:
            return 0.0

        return temp

    @property
    def time_index(self) -> 'int':
        """int: 'TimeIndex' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TimeIndex

        if temp is None:
            return 0

        return temp

    @property
    def torque_from_stator_tooth_tangential_forces(self) -> 'float':
        """float: 'TorqueFromStatorToothTangentialForces' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TorqueFromStatorToothTangentialForces

        if temp is None:
            return 0.0

        return temp

    @property
    def torque_mst_single_contour(self) -> 'float':
        """float: 'TorqueMSTSingleContour' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TorqueMSTSingleContour

        if temp is None:
            return 0.0

        return temp

    @property
    def torque_mst(self) -> 'float':
        """float: 'TorqueMST' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TorqueMST

        if temp is None:
            return 0.0

        return temp

    @property
    def results_for_stator_teeth(self) -> 'List[_1304.ElectricMachineResultsForStatorToothAtTimeStep]':
        """List[ElectricMachineResultsForStatorToothAtTimeStep]: 'ResultsForStatorTeeth' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ResultsForStatorTeeth

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def results_at_locations(self) -> 'List[_1307.ElectricMachineResultsTimeStepAtLocation]':
        """List[ElectricMachineResultsTimeStepAtLocation]: 'ResultsAtLocations' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ResultsAtLocations

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def results_for_line_to_line(self) -> 'List[_1305.ElectricMachineResultsLineToLineAtTimeStep]':
        """List[ElectricMachineResultsLineToLineAtTimeStep]: 'ResultsForLineToLine' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ResultsForLineToLine

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def results_for_phases(self) -> 'List[_1303.ElectricMachineResultsForPhaseAtTimeStep]':
        """List[ElectricMachineResultsForPhaseAtTimeStep]: 'ResultsForPhases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ResultsForPhases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def elemental_flux_densities(self) -> 'List[Vector2D]':
        """List[Vector2D]: 'ElementalFluxDensities' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ElementalFluxDensities

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def magnetic_vector_potential(self) -> 'List[float]':
        """List[float]: 'MagneticVectorPotential' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MagneticVectorPotential

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, float)
        return value

    @property
    def nodal_positions(self) -> 'List[Vector2D]':
        """List[Vector2D]: 'NodalPositions' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NodalPositions

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

    def elements_node_id_for(self, node_number: 'int') -> 'List[int]':
        """ 'ElementsNodeIDFor' is the original name of this method.

        Args:
            node_number (int)

        Returns:
            List[int]
        """

        node_number = int(node_number)
        return conversion.pn_to_mp_objects_in_list(self.wrapped.ElementsNodeIDFor(node_number if node_number else 0), int)

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
