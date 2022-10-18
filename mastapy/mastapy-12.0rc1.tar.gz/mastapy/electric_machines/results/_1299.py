"""_1299.py

ElectricMachineResults
"""


from typing import List

from mastapy._internal import constructor, conversion
from mastapy.utility_gui.charts import (
    _1827, _1813, _1820, _1822
)
from mastapy._internal.cast_exception import CastException
from mastapy.electric_machines import (
    _1249, _1235, _1259, _1267,
    _1270, _1283, _1285, _1252
)
from mastapy.electric_machines.results import _1306, _1300, _1302
from mastapy import _0
from mastapy._internal.python_net import python_net_import

_ELECTRIC_MACHINE_RESULTS = python_net_import('SMT.MastaAPI.ElectricMachines.Results', 'ElectricMachineResults')


__docformat__ = 'restructuredtext en'
__all__ = ('ElectricMachineResults',)


class ElectricMachineResults(_0.APIBase):
    """ElectricMachineResults

    This is a mastapy class.
    """

    TYPE = _ELECTRIC_MACHINE_RESULTS

    def __init__(self, instance_to_wrap: 'ElectricMachineResults.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def average_d_axis_flux_linkage(self) -> 'float':
        """float: 'AverageDAxisFluxLinkage' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AverageDAxisFluxLinkage

        if temp is None:
            return 0.0

        return temp

    @property
    def average_flux_linkage(self) -> 'float':
        """float: 'AverageFluxLinkage' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AverageFluxLinkage

        if temp is None:
            return 0.0

        return temp

    @property
    def average_q_axis_flux_linkage(self) -> 'float':
        """float: 'AverageQAxisFluxLinkage' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AverageQAxisFluxLinkage

        if temp is None:
            return 0.0

        return temp

    @property
    def average_torque_mst(self) -> 'float':
        """float: 'AverageTorqueMST' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AverageTorqueMST

        if temp is None:
            return 0.0

        return temp

    @property
    def eddy_current_loss_rotor(self) -> 'float':
        """float: 'EddyCurrentLossRotor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.EddyCurrentLossRotor

        if temp is None:
            return 0.0

        return temp

    @property
    def eddy_current_loss_stator(self) -> 'float':
        """float: 'EddyCurrentLossStator' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.EddyCurrentLossStator

        if temp is None:
            return 0.0

        return temp

    @property
    def eddy_current_loss_total(self) -> 'float':
        """float: 'EddyCurrentLossTotal' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.EddyCurrentLossTotal

        if temp is None:
            return 0.0

        return temp

    @property
    def excess_loss_rotor(self) -> 'float':
        """float: 'ExcessLossRotor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ExcessLossRotor

        if temp is None:
            return 0.0

        return temp

    @property
    def excess_loss_stator(self) -> 'float':
        """float: 'ExcessLossStator' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ExcessLossStator

        if temp is None:
            return 0.0

        return temp

    @property
    def excess_loss_total(self) -> 'float':
        """float: 'ExcessLossTotal' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ExcessLossTotal

        if temp is None:
            return 0.0

        return temp

    @property
    def flux_density_in_air_gap_chart_at_time_0(self) -> '_1827.TwoDChartDefinition':
        """TwoDChartDefinition: 'FluxDensityInAirGapChartAtTime0' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FluxDensityInAirGapChartAtTime0

        if temp is None:
            return None

        if _1827.TwoDChartDefinition.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast flux_density_in_air_gap_chart_at_time_0 to TwoDChartDefinition. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def force_density_in_air_gap_mst_chart_at_time_0(self) -> '_1827.TwoDChartDefinition':
        """TwoDChartDefinition: 'ForceDensityInAirGapMSTChartAtTime0' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ForceDensityInAirGapMSTChartAtTime0

        if temp is None:
            return None

        if _1827.TwoDChartDefinition.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast force_density_in_air_gap_mst_chart_at_time_0 to TwoDChartDefinition. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def hysteresis_loss_rotor(self) -> 'float':
        """float: 'HysteresisLossRotor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HysteresisLossRotor

        if temp is None:
            return 0.0

        return temp

    @property
    def hysteresis_loss_stator(self) -> 'float':
        """float: 'HysteresisLossStator' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HysteresisLossStator

        if temp is None:
            return 0.0

        return temp

    @property
    def hysteresis_loss_total(self) -> 'float':
        """float: 'HysteresisLossTotal' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HysteresisLossTotal

        if temp is None:
            return 0.0

        return temp

    @property
    def hysteresis_loss_fundamental_rotor(self) -> 'float':
        """float: 'HysteresisLossFundamentalRotor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HysteresisLossFundamentalRotor

        if temp is None:
            return 0.0

        return temp

    @property
    def hysteresis_loss_fundamental_stator(self) -> 'float':
        """float: 'HysteresisLossFundamentalStator' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HysteresisLossFundamentalStator

        if temp is None:
            return 0.0

        return temp

    @property
    def hysteresis_loss_minor_loop_rotor(self) -> 'float':
        """float: 'HysteresisLossMinorLoopRotor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HysteresisLossMinorLoopRotor

        if temp is None:
            return 0.0

        return temp

    @property
    def hysteresis_loss_minor_loop_stator(self) -> 'float':
        """float: 'HysteresisLossMinorLoopStator' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HysteresisLossMinorLoopStator

        if temp is None:
            return 0.0

        return temp

    @property
    def magnet_loss_build_factor(self) -> 'float':
        """float: 'MagnetLossBuildFactor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MagnetLossBuildFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def torque_ripple_mst(self) -> 'float':
        """float: 'TorqueRippleMST' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TorqueRippleMST

        if temp is None:
            return 0.0

        return temp

    @property
    def total_core_losses(self) -> 'float':
        """float: 'TotalCoreLosses' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TotalCoreLosses

        if temp is None:
            return 0.0

        return temp

    @property
    def total_magnet_losses(self) -> 'float':
        """float: 'TotalMagnetLosses' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TotalMagnetLosses

        if temp is None:
            return 0.0

        return temp

    @property
    def total_power_loss(self) -> 'float':
        """float: 'TotalPowerLoss' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TotalPowerLoss

        if temp is None:
            return 0.0

        return temp

    @property
    def total_rotor_core_losses(self) -> 'float':
        """float: 'TotalRotorCoreLosses' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TotalRotorCoreLosses

        if temp is None:
            return 0.0

        return temp

    @property
    def total_stator_core_losses(self) -> 'float':
        """float: 'TotalStatorCoreLosses' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TotalStatorCoreLosses

        if temp is None:
            return 0.0

        return temp

    @property
    def electric_machine_detail(self) -> '_1249.ElectricMachineDetail':
        """ElectricMachineDetail: 'ElectricMachineDetail' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ElectricMachineDetail

        if temp is None:
            return None

        if _1249.ElectricMachineDetail.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast electric_machine_detail to ElectricMachineDetail. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def electric_machine_detail_of_type_cad_electric_machine_detail(self) -> '_1235.CADElectricMachineDetail':
        """CADElectricMachineDetail: 'ElectricMachineDetail' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ElectricMachineDetail

        if temp is None:
            return None

        if _1235.CADElectricMachineDetail.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast electric_machine_detail to CADElectricMachineDetail. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def electric_machine_detail_of_type_interior_permanent_magnet_machine(self) -> '_1259.InteriorPermanentMagnetMachine':
        """InteriorPermanentMagnetMachine: 'ElectricMachineDetail' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ElectricMachineDetail

        if temp is None:
            return None

        if _1259.InteriorPermanentMagnetMachine.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast electric_machine_detail to InteriorPermanentMagnetMachine. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def electric_machine_detail_of_type_non_cad_electric_machine_detail(self) -> '_1267.NonCADElectricMachineDetail':
        """NonCADElectricMachineDetail: 'ElectricMachineDetail' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ElectricMachineDetail

        if temp is None:
            return None

        if _1267.NonCADElectricMachineDetail.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast electric_machine_detail to NonCADElectricMachineDetail. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def electric_machine_detail_of_type_permanent_magnet_assisted_synchronous_reluctance_machine(self) -> '_1270.PermanentMagnetAssistedSynchronousReluctanceMachine':
        """PermanentMagnetAssistedSynchronousReluctanceMachine: 'ElectricMachineDetail' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ElectricMachineDetail

        if temp is None:
            return None

        if _1270.PermanentMagnetAssistedSynchronousReluctanceMachine.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast electric_machine_detail to PermanentMagnetAssistedSynchronousReluctanceMachine. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def electric_machine_detail_of_type_surface_permanent_magnet_machine(self) -> '_1283.SurfacePermanentMagnetMachine':
        """SurfacePermanentMagnetMachine: 'ElectricMachineDetail' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ElectricMachineDetail

        if temp is None:
            return None

        if _1283.SurfacePermanentMagnetMachine.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast electric_machine_detail to SurfacePermanentMagnetMachine. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def electric_machine_detail_of_type_synchronous_reluctance_machine(self) -> '_1285.SynchronousReluctanceMachine':
        """SynchronousReluctanceMachine: 'ElectricMachineDetail' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ElectricMachineDetail

        if temp is None:
            return None

        if _1285.SynchronousReluctanceMachine.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast electric_machine_detail to SynchronousReluctanceMachine. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def setup(self) -> '_1252.ElectricMachineSetup':
        """ElectricMachineSetup: 'Setup' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Setup

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def results_timesteps(self) -> 'List[_1306.ElectricMachineResultsTimeStep]':
        """List[ElectricMachineResultsTimeStep]: 'ResultsTimesteps' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ResultsTimesteps

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def results_for_line_to_line(self) -> 'List[_1300.ElectricMachineResultsForLineToLine]':
        """List[ElectricMachineResultsForLineToLine]: 'ResultsForLineToLine' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ResultsForLineToLine

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def results_for_phases(self) -> 'List[_1302.ElectricMachineResultsForPhase]':
        """List[ElectricMachineResultsForPhase]: 'ResultsForPhases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ResultsForPhases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def results_for_this_and_slices(self) -> 'List[ElectricMachineResults]':
        """List[ElectricMachineResults]: 'ResultsForThisAndSlices' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ResultsForThisAndSlices

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
