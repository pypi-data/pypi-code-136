"""_1297.py

EfficiencyResults
"""


from typing import List

from mastapy.utility_gui.charts import _1825
from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.python_net import python_net_import

_EFFICIENCY_RESULTS = python_net_import('SMT.MastaAPI.ElectricMachines.Results', 'EfficiencyResults')


__docformat__ = 'restructuredtext en'
__all__ = ('EfficiencyResults',)


class EfficiencyResults(_0.APIBase):
    """EfficiencyResults

    This is a mastapy class.
    """

    TYPE = _EFFICIENCY_RESULTS

    def __init__(self, instance_to_wrap: 'EfficiencyResults.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def current_angle(self) -> '_1825.ThreeDChartDefinition':
        """ThreeDChartDefinition: 'CurrentAngle' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentAngle

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def d_axis_current(self) -> '_1825.ThreeDChartDefinition':
        """ThreeDChartDefinition: 'DAxisCurrent' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DAxisCurrent

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def d_axis_flux_linkage(self) -> '_1825.ThreeDChartDefinition':
        """ThreeDChartDefinition: 'DAxisFluxLinkage' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DAxisFluxLinkage

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def dc_winding_loss(self) -> '_1825.ThreeDChartDefinition':
        """ThreeDChartDefinition: 'DCWindingLoss' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DCWindingLoss

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def efficiency_map(self) -> '_1825.ThreeDChartDefinition':
        """ThreeDChartDefinition: 'EfficiencyMap' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.EfficiencyMap

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def input_power(self) -> '_1825.ThreeDChartDefinition':
        """ThreeDChartDefinition: 'InputPower' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InputPower

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def magnet_loss(self) -> '_1825.ThreeDChartDefinition':
        """ThreeDChartDefinition: 'MagnetLoss' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MagnetLoss

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def output_power(self) -> '_1825.ThreeDChartDefinition':
        """ThreeDChartDefinition: 'OutputPower' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OutputPower

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def peak_phase_current_magnitude(self) -> '_1825.ThreeDChartDefinition':
        """ThreeDChartDefinition: 'PeakPhaseCurrentMagnitude' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PeakPhaseCurrentMagnitude

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def peak_phase_voltage_magnitude(self) -> '_1825.ThreeDChartDefinition':
        """ThreeDChartDefinition: 'PeakPhaseVoltageMagnitude' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PeakPhaseVoltageMagnitude

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def q_axis_current(self) -> '_1825.ThreeDChartDefinition':
        """ThreeDChartDefinition: 'QAxisCurrent' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.QAxisCurrent

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def q_axis_flux_linkage(self) -> '_1825.ThreeDChartDefinition':
        """ThreeDChartDefinition: 'QAxisFluxLinkage' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.QAxisFluxLinkage

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def rotor_eddy_current_loss(self) -> '_1825.ThreeDChartDefinition':
        """ThreeDChartDefinition: 'RotorEddyCurrentLoss' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RotorEddyCurrentLoss

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def rotor_excess_loss(self) -> '_1825.ThreeDChartDefinition':
        """ThreeDChartDefinition: 'RotorExcessLoss' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RotorExcessLoss

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def rotor_hysteresis_loss(self) -> '_1825.ThreeDChartDefinition':
        """ThreeDChartDefinition: 'RotorHysteresisLoss' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RotorHysteresisLoss

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def stator_eddy_current_loss(self) -> '_1825.ThreeDChartDefinition':
        """ThreeDChartDefinition: 'StatorEddyCurrentLoss' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StatorEddyCurrentLoss

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def stator_excess_loss(self) -> '_1825.ThreeDChartDefinition':
        """ThreeDChartDefinition: 'StatorExcessLoss' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StatorExcessLoss

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def stator_hysteresis_loss(self) -> '_1825.ThreeDChartDefinition':
        """ThreeDChartDefinition: 'StatorHysteresisLoss' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StatorHysteresisLoss

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def total_loss(self) -> '_1825.ThreeDChartDefinition':
        """ThreeDChartDefinition: 'TotalLoss' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TotalLoss

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
