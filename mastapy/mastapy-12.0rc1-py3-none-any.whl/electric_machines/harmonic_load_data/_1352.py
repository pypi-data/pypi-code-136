"""_1352.py

StatorToothLoadInterpolator
"""


from typing import List

from mastapy._internal import constructor, conversion
from mastapy.math_utility import _1484
from mastapy import _0
from mastapy._internal.python_net import python_net_import

_STATOR_TOOTH_LOAD_INTERPOLATOR = python_net_import('SMT.MastaAPI.ElectricMachines.HarmonicLoadData', 'StatorToothLoadInterpolator')


__docformat__ = 'restructuredtext en'
__all__ = ('StatorToothLoadInterpolator',)


class StatorToothLoadInterpolator(_0.APIBase):
    """StatorToothLoadInterpolator

    This is a mastapy class.
    """

    TYPE = _STATOR_TOOTH_LOAD_INTERPOLATOR

    def __init__(self, instance_to_wrap: 'StatorToothLoadInterpolator.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def spatial_force_absolute_tolerance(self) -> 'float':
        """float: 'SpatialForceAbsoluteTolerance' is the original name of this property."""

        temp = self.wrapped.SpatialForceAbsoluteTolerance

        if temp is None:
            return 0.0

        return temp

    @spatial_force_absolute_tolerance.setter
    def spatial_force_absolute_tolerance(self, value: 'float'):
        self.wrapped.SpatialForceAbsoluteTolerance = float(value) if value else 0.0

    @property
    def spatial_force_relative_tolerance(self) -> 'float':
        """float: 'SpatialForceRelativeTolerance' is the original name of this property."""

        temp = self.wrapped.SpatialForceRelativeTolerance

        if temp is None:
            return 0.0

        return temp

    @spatial_force_relative_tolerance.setter
    def spatial_force_relative_tolerance(self, value: 'float'):
        self.wrapped.SpatialForceRelativeTolerance = float(value) if value else 0.0

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

    def multiple_fourier_series_interpolator_for(self, node_index: 'int') -> '_1484.MultipleFourierSeriesInterpolator':
        """ 'MultipleFourierSeriesInterpolatorFor' is the original name of this method.

        Args:
            node_index (int)

        Returns:
            mastapy.math_utility.MultipleFourierSeriesInterpolator
        """

        node_index = int(node_index)
        method_result = self.wrapped.MultipleFourierSeriesInterpolatorFor(node_index if node_index else 0)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

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
