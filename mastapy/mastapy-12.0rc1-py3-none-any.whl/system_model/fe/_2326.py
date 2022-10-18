"""_2326.py

ElectricMachineDynamicLoadData
"""


from typing import List

from mastapy._internal.implicit import list_with_selected_item
from mastapy.electric_machines import _1276
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import constructor, conversion
from mastapy.system_model.fe import _2325
from mastapy.electric_machines.results import _1310
from mastapy import _0
from mastapy._internal.python_net import python_net_import

_ELECTRIC_MACHINE_DYNAMIC_LOAD_DATA = python_net_import('SMT.MastaAPI.SystemModel.FE', 'ElectricMachineDynamicLoadData')


__docformat__ = 'restructuredtext en'
__all__ = ('ElectricMachineDynamicLoadData',)


class ElectricMachineDynamicLoadData(_0.APIBase):
    """ElectricMachineDynamicLoadData

    This is a mastapy class.
    """

    TYPE = _ELECTRIC_MACHINE_DYNAMIC_LOAD_DATA

    def __init__(self, instance_to_wrap: 'ElectricMachineDynamicLoadData.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def slice(self) -> 'list_with_selected_item.ListWithSelectedItem_RotorSkewSlice':
        """list_with_selected_item.ListWithSelectedItem_RotorSkewSlice: 'Slice' is the original name of this property."""

        temp = self.wrapped.Slice

        if temp is None:
            return None

        return constructor.new_from_mastapy_type(list_with_selected_item.ListWithSelectedItem_RotorSkewSlice)(temp) if temp is not None else None

    @slice.setter
    def slice(self, value: 'list_with_selected_item.ListWithSelectedItem_RotorSkewSlice.implicit_type()'):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_RotorSkewSlice.wrapper_type()
        enclosed_type = list_with_selected_item.ListWithSelectedItem_RotorSkewSlice.implicit_type()
        value = wrapper_type[enclosed_type](value.wrapped if value is not None else None)
        self.wrapped.Slice = value

    @property
    def electric_machine_data_sets(self) -> 'List[_2325.ElectricMachineDataSet]':
        """List[ElectricMachineDataSet]: 'ElectricMachineDataSets' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ElectricMachineDataSets

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

    def add_electric_machine_data_set(self, name: 'str') -> '_2325.ElectricMachineDataSet':
        """ 'AddElectricMachineDataSet' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.fe.ElectricMachineDataSet
        """

        name = str(name)
        method_result = self.wrapped.AddElectricMachineDataSet(name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def add_electric_machine_data_set_from_masta_dynamic_force_analysis(self, analysis: '_1310.IHaveDynamicForceResults', slice_index: 'int') -> '_2325.ElectricMachineDataSet':
        """ 'AddElectricMachineDataSetFromMASTADynamicForceAnalysis' is the original name of this method.

        Args:
            analysis (mastapy.electric_machines.results.IHaveDynamicForceResults)
            slice_index (int)

        Returns:
            mastapy.system_model.fe.ElectricMachineDataSet
        """

        slice_index = int(slice_index)
        method_result = self.wrapped.AddElectricMachineDataSetFromMASTADynamicForceAnalysis(analysis.wrapped if analysis else None, slice_index if slice_index else 0)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def delete_all_data_sets(self):
        """ 'DeleteAllDataSets' is the original name of this method."""

        self.wrapped.DeleteAllDataSets()

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
