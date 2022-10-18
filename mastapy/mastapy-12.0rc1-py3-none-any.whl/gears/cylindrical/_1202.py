"""_1202.py

GearLTCAContactChartDataAsTextFile
"""


from typing import List

from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.python_net import python_net_import

_GEAR_LTCA_CONTACT_CHART_DATA_AS_TEXT_FILE = python_net_import('SMT.MastaAPI.Gears.Cylindrical', 'GearLTCAContactChartDataAsTextFile')


__docformat__ = 'restructuredtext en'
__all__ = ('GearLTCAContactChartDataAsTextFile',)


class GearLTCAContactChartDataAsTextFile(_0.APIBase):
    """GearLTCAContactChartDataAsTextFile

    This is a mastapy class.
    """

    TYPE = _GEAR_LTCA_CONTACT_CHART_DATA_AS_TEXT_FILE

    def __init__(self, instance_to_wrap: 'GearLTCAContactChartDataAsTextFile.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

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

    def depth_of_max_shear_stress(self):
        """ 'DepthOfMaxShearStress' is the original name of this method."""

        self.wrapped.DepthOfMaxShearStress()

    def force_per_unit_length(self):
        """ 'ForcePerUnitLength' is the original name of this method."""

        self.wrapped.ForcePerUnitLength()

    def gap_between_loaded_flanks_transverse(self):
        """ 'GapBetweenLoadedFlanksTransverse' is the original name of this method."""

        self.wrapped.GapBetweenLoadedFlanksTransverse()

    def hertzian_contact_half_width(self):
        """ 'HertzianContactHalfWidth' is the original name of this method."""

        self.wrapped.HertzianContactHalfWidth()

    def max_pressure(self):
        """ 'MaxPressure' is the original name of this method."""

        self.wrapped.MaxPressure()

    def max_shear_stress(self):
        """ 'MaxShearStress' is the original name of this method."""

        self.wrapped.MaxShearStress()

    def total_deflection_for_mesh(self):
        """ 'TotalDeflectionForMesh' is the original name of this method."""

        self.wrapped.TotalDeflectionForMesh()

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
