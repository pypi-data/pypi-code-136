"""_1327.py

ElectricMachineLoadCaseBase
"""


from typing import List

from mastapy._internal import constructor, conversion
from mastapy.electric_machines.load_cases_and_analyses import _1345, _1321, _1328
from mastapy.electric_machines import _1252
from mastapy import _0
from mastapy._internal.python_net import python_net_import

_ELECTRIC_MACHINE_LOAD_CASE_BASE = python_net_import('SMT.MastaAPI.ElectricMachines.LoadCasesAndAnalyses', 'ElectricMachineLoadCaseBase')


__docformat__ = 'restructuredtext en'
__all__ = ('ElectricMachineLoadCaseBase',)


class ElectricMachineLoadCaseBase(_0.APIBase):
    """ElectricMachineLoadCaseBase

    This is a mastapy class.
    """

    TYPE = _ELECTRIC_MACHINE_LOAD_CASE_BASE

    def __init__(self, instance_to_wrap: 'ElectricMachineLoadCaseBase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def folder_path(self) -> 'str':
        """str: 'FolderPath' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FolderPath

        if temp is None:
            return ''

        return temp

    @property
    def name(self) -> 'str':
        """str: 'Name' is the original name of this property."""

        temp = self.wrapped.Name

        if temp is None:
            return ''

        return temp

    @name.setter
    def name(self, value: 'str'):
        self.wrapped.Name = str(value) if value else ''

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
    def analyses(self) -> 'List[_1321.ElectricMachineAnalysis]':
        """List[ElectricMachineAnalysis]: 'Analyses' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Analyses

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

    def edit_folder_path(self):
        """ 'EditFolderPath' is the original name of this method."""

        self.wrapped.EditFolderPath()

    def analysis_for(self, setup: '_1252.ElectricMachineSetup') -> '_1321.ElectricMachineAnalysis':
        """ 'AnalysisFor' is the original name of this method.

        Args:
            setup (mastapy.electric_machines.ElectricMachineSetup)

        Returns:
            mastapy.electric_machines.load_cases_and_analyses.ElectricMachineAnalysis
        """

        method_result = self.wrapped.AnalysisFor(setup.wrapped if setup else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def copy_to(self, another_group: '_1328.ElectricMachineLoadCaseGroup') -> 'ElectricMachineLoadCaseBase':
        """ 'CopyTo' is the original name of this method.

        Args:
            another_group (mastapy.electric_machines.load_cases_and_analyses.ElectricMachineLoadCaseGroup)

        Returns:
            mastapy.electric_machines.load_cases_and_analyses.ElectricMachineLoadCaseBase
        """

        method_result = self.wrapped.CopyTo(another_group.wrapped if another_group else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def remove_analysis(self, electric_machine_analysis: '_1321.ElectricMachineAnalysis'):
        """ 'RemoveAnalysis' is the original name of this method.

        Args:
            electric_machine_analysis (mastapy.electric_machines.load_cases_and_analyses.ElectricMachineAnalysis)
        """

        self.wrapped.RemoveAnalysis(electric_machine_analysis.wrapped if electric_machine_analysis else None)

    def remove_analysis_for(self, setup: '_1252.ElectricMachineSetup'):
        """ 'RemoveAnalysisFor' is the original name of this method.

        Args:
            setup (mastapy.electric_machines.ElectricMachineSetup)
        """

        self.wrapped.RemoveAnalysisFor(setup.wrapped if setup else None)

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
