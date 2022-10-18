"""_168.py

ElmerResultsViewable
"""


from typing import List

from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy._internal.implicit import enum_with_selected_value
from mastapy.math_utility import _1490
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.nodal_analysis.elmer import _169
from mastapy import _0
from mastapy._internal.python_net import python_net_import

_ELMER_RESULTS_VIEWABLE = python_net_import('SMT.MastaAPI.NodalAnalysis.Elmer', 'ElmerResultsViewable')


__docformat__ = 'restructuredtext en'
__all__ = ('ElmerResultsViewable',)


class ElmerResultsViewable(_0.APIBase):
    """ElmerResultsViewable

    This is a mastapy class.
    """

    TYPE = _ELMER_RESULTS_VIEWABLE

    def __init__(self, instance_to_wrap: 'ElmerResultsViewable.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def current_index(self) -> 'int':
        """int: 'CurrentIndex' is the original name of this property."""

        temp = self.wrapped.CurrentIndex

        if temp is None:
            return 0

        return temp

    @current_index.setter
    def current_index(self, value: 'int'):
        self.wrapped.CurrentIndex = int(value) if value else 0

    @property
    def degree_of_freedom(self) -> 'enum_with_selected_value.EnumWithSelectedValue_ResultOptionsFor3DVector':
        """enum_with_selected_value.EnumWithSelectedValue_ResultOptionsFor3DVector: 'DegreeOfFreedom' is the original name of this property."""

        temp = self.wrapped.DegreeOfFreedom

        if temp is None:
            return None

        value = enum_with_selected_value.EnumWithSelectedValue_ResultOptionsFor3DVector.wrapped_type()
        return enum_with_selected_value_runtime.create(temp, value) if temp is not None else None

    @degree_of_freedom.setter
    def degree_of_freedom(self, value: 'enum_with_selected_value.EnumWithSelectedValue_ResultOptionsFor3DVector.implicit_type()'):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = enum_with_selected_value.EnumWithSelectedValue_ResultOptionsFor3DVector.implicit_type()
        value = conversion.mp_to_pn_enum(value)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.DegreeOfFreedom = value

    @property
    def result_type(self) -> 'enum_with_selected_value.EnumWithSelectedValue_ElmerResultType':
        """enum_with_selected_value.EnumWithSelectedValue_ElmerResultType: 'ResultType' is the original name of this property."""

        temp = self.wrapped.ResultType

        if temp is None:
            return None

        value = enum_with_selected_value.EnumWithSelectedValue_ElmerResultType.wrapped_type()
        return enum_with_selected_value_runtime.create(temp, value) if temp is not None else None

    @result_type.setter
    def result_type(self, value: 'enum_with_selected_value.EnumWithSelectedValue_ElmerResultType.implicit_type()'):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = enum_with_selected_value.EnumWithSelectedValue_ElmerResultType.implicit_type()
        value = conversion.mp_to_pn_enum(value)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.ResultType = value

    @property
    def show_contour_range_for_all_parts(self) -> 'bool':
        """bool: 'ShowContourRangeForAllParts' is the original name of this property."""

        temp = self.wrapped.ShowContourRangeForAllParts

        if temp is None:
            return False

        return temp

    @show_contour_range_for_all_parts.setter
    def show_contour_range_for_all_parts(self, value: 'bool'):
        self.wrapped.ShowContourRangeForAllParts = bool(value) if value else False

    @property
    def show_contour_range_for_all_steps(self) -> 'bool':
        """bool: 'ShowContourRangeForAllSteps' is the original name of this property."""

        temp = self.wrapped.ShowContourRangeForAllSteps

        if temp is None:
            return False

        return temp

    @show_contour_range_for_all_steps.setter
    def show_contour_range_for_all_steps(self, value: 'bool'):
        self.wrapped.ShowContourRangeForAllSteps = bool(value) if value else False

    @property
    def show_full_model(self) -> 'bool':
        """bool: 'ShowFullModel' is the original name of this property."""

        temp = self.wrapped.ShowFullModel

        if temp is None:
            return False

        return temp

    @show_full_model.setter
    def show_full_model(self, value: 'bool'):
        self.wrapped.ShowFullModel = bool(value) if value else False

    @property
    def show_in_3d(self) -> 'bool':
        """bool: 'ShowIn3D' is the original name of this property."""

        temp = self.wrapped.ShowIn3D

        if temp is None:
            return False

        return temp

    @show_in_3d.setter
    def show_in_3d(self, value: 'bool'):
        self.wrapped.ShowIn3D = bool(value) if value else False

    @property
    def show_mesh(self) -> 'bool':
        """bool: 'ShowMesh' is the original name of this property."""

        temp = self.wrapped.ShowMesh

        if temp is None:
            return False

        return temp

    @show_mesh.setter
    def show_mesh(self, value: 'bool'):
        self.wrapped.ShowMesh = bool(value) if value else False

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
