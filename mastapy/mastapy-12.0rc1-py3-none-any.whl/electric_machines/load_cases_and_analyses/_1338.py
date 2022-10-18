"""_1338.py

SlotDetailForAnalysis
"""


from typing import List

from mastapy._internal import constructor, conversion
from mastapy.electric_machines import _1279
from mastapy import _0
from mastapy._internal.python_net import python_net_import

_SLOT_DETAIL_FOR_ANALYSIS = python_net_import('SMT.MastaAPI.ElectricMachines.LoadCasesAndAnalyses', 'SlotDetailForAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('SlotDetailForAnalysis',)


class SlotDetailForAnalysis(_0.APIBase):
    """SlotDetailForAnalysis

    This is a mastapy class.
    """

    TYPE = _SLOT_DETAIL_FOR_ANALYSIS

    def __init__(self, instance_to_wrap: 'SlotDetailForAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def d_axis_current_density_conductors(self) -> 'float':
        """float: 'DAxisCurrentDensityConductors' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DAxisCurrentDensityConductors

        if temp is None:
            return 0.0

        return temp

    @property
    def d_axis_current_density_slot(self) -> 'float':
        """float: 'DAxisCurrentDensitySlot' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DAxisCurrentDensitySlot

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
    def peak_current_density_conductors(self) -> 'float':
        """float: 'PeakCurrentDensityConductors' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PeakCurrentDensityConductors

        if temp is None:
            return 0.0

        return temp

    @property
    def peak_current_density_slot(self) -> 'float':
        """float: 'PeakCurrentDensitySlot' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PeakCurrentDensitySlot

        if temp is None:
            return 0.0

        return temp

    @property
    def q_axis_current_density_conductors(self) -> 'float':
        """float: 'QAxisCurrentDensityConductors' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.QAxisCurrentDensityConductors

        if temp is None:
            return 0.0

        return temp

    @property
    def q_axis_current_density_slot(self) -> 'float':
        """float: 'QAxisCurrentDensitySlot' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.QAxisCurrentDensitySlot

        if temp is None:
            return 0.0

        return temp

    @property
    def rms_current_density_conductors(self) -> 'float':
        """float: 'RMSCurrentDensityConductors' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RMSCurrentDensityConductors

        if temp is None:
            return 0.0

        return temp

    @property
    def rms_current_density_slot(self) -> 'float':
        """float: 'RMSCurrentDensitySlot' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RMSCurrentDensitySlot

        if temp is None:
            return 0.0

        return temp

    @property
    def slot_section_details(self) -> '_1279.SlotSectionDetail':
        """SlotSectionDetail: 'SlotSectionDetails' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SlotSectionDetails

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
