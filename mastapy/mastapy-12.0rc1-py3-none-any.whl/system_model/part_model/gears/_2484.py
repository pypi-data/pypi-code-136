"""_2484.py

GearSetConfiguration
"""


from typing import List, Optional

from mastapy.gears import _322, _323
from mastapy._internal import constructor, conversion
from mastapy.system_model.part_model.gears import (
    _2475, _2477, _2488, _2503
)
from mastapy.system_model.analyses_and_results.static_loads import _6731
from mastapy.gears.analysis import _1217
from mastapy.system_model.analyses_and_results.load_case_groups import _5596
from mastapy._internal.python_net import python_net_import
from mastapy import _0

_STATIC_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'StaticLoadCase')
_GEAR_SET_MODES = python_net_import('SMT.MastaAPI.Gears', 'GearSetModes')
_BOOLEAN = python_net_import('System', 'Boolean')
_ABSTRACT_STATIC_LOAD_CASE_GROUP = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.LoadCaseGroups', 'AbstractStaticLoadCaseGroup')
_GEAR_SET_CONFIGURATION = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'GearSetConfiguration')


__docformat__ = 'restructuredtext en'
__all__ = ('GearSetConfiguration',)


class GearSetConfiguration(_0.APIBase):
    """GearSetConfiguration

    This is a mastapy class.
    """

    TYPE = _GEAR_SET_CONFIGURATION

    def __init__(self, instance_to_wrap: 'GearSetConfiguration.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def gear_set_design_group(self) -> '_322.GearSetDesignGroup':
        """GearSetDesignGroup: 'GearSetDesignGroup' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearSetDesignGroup

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def conical_gear_sets(self) -> 'List[_2475.ConicalGearSet]':
        """List[ConicalGearSet]: 'ConicalGearSets' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConicalGearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cylindrical_gear_sets(self) -> 'List[_2477.CylindricalGearSet]':
        """List[CylindricalGearSet]: 'CylindricalGearSets' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CylindricalGearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def klingelnberg_cyclo_palloid_gear_sets(self) -> 'List[_2488.KlingelnbergCycloPalloidConicalGearSet]':
        """List[KlingelnbergCycloPalloidConicalGearSet]: 'KlingelnbergCycloPalloidGearSets' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.KlingelnbergCycloPalloidGearSets

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def worm_gear_sets(self) -> 'List[_2503.WormGearSet]':
        """List[WormGearSet]: 'WormGearSets' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WormGearSets

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

    def implementation_detail_results_for(self, analysis_case: '_6731.StaticLoadCase', gear_set_mode: '_323.GearSetModes', run_all_planetary_meshes: 'bool') -> '_1217.GearSetGroupDutyCycle':
        """ 'ImplementationDetailResultsFor' is the original name of this method.

        Args:
            analysis_case (mastapy.system_model.analyses_and_results.static_loads.StaticLoadCase)
            gear_set_mode (mastapy.gears.GearSetModes)
            run_all_planetary_meshes (bool)

        Returns:
            mastapy.gears.analysis.GearSetGroupDutyCycle
        """

        gear_set_mode = conversion.mp_to_pn_enum(gear_set_mode)
        run_all_planetary_meshes = bool(run_all_planetary_meshes)
        method_result = self.wrapped.ImplementationDetailResultsFor.Overloads[_STATIC_LOAD_CASE, _GEAR_SET_MODES, _BOOLEAN](analysis_case.wrapped if analysis_case else None, gear_set_mode, run_all_planetary_meshes if run_all_planetary_meshes else False)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def implementation_detail_results_for_group(self, analysis_case: '_5596.AbstractStaticLoadCaseGroup', gear_set_mode: '_323.GearSetModes', run_all_planetary_meshes: 'bool') -> '_1217.GearSetGroupDutyCycle':
        """ 'ImplementationDetailResultsFor' is the original name of this method.

        Args:
            analysis_case (mastapy.system_model.analyses_and_results.load_case_groups.AbstractStaticLoadCaseGroup)
            gear_set_mode (mastapy.gears.GearSetModes)
            run_all_planetary_meshes (bool)

        Returns:
            mastapy.gears.analysis.GearSetGroupDutyCycle
        """

        gear_set_mode = conversion.mp_to_pn_enum(gear_set_mode)
        run_all_planetary_meshes = bool(run_all_planetary_meshes)
        method_result = self.wrapped.ImplementationDetailResultsFor.Overloads[_ABSTRACT_STATIC_LOAD_CASE_GROUP, _GEAR_SET_MODES, _BOOLEAN](analysis_case.wrapped if analysis_case else None, gear_set_mode, run_all_planetary_meshes if run_all_planetary_meshes else False)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def perform_implementation_detail_analysis(self, static_load: '_6731.StaticLoadCase', gear_set_mode: '_323.GearSetModes', run_all_planetary_meshes: Optional['bool'] = True, perform_system_analysis_if_not_ready: Optional['bool'] = True):
        """ 'PerformImplementationDetailAnalysis' is the original name of this method.

        Args:
            static_load (mastapy.system_model.analyses_and_results.static_loads.StaticLoadCase)
            gear_set_mode (mastapy.gears.GearSetModes)
            run_all_planetary_meshes (bool, optional)
            perform_system_analysis_if_not_ready (bool, optional)
        """

        gear_set_mode = conversion.mp_to_pn_enum(gear_set_mode)
        run_all_planetary_meshes = bool(run_all_planetary_meshes)
        perform_system_analysis_if_not_ready = bool(perform_system_analysis_if_not_ready)
        self.wrapped.PerformImplementationDetailAnalysis.Overloads[_STATIC_LOAD_CASE, _GEAR_SET_MODES, _BOOLEAN, _BOOLEAN](static_load.wrapped if static_load else None, gear_set_mode, run_all_planetary_meshes if run_all_planetary_meshes else False, perform_system_analysis_if_not_ready if perform_system_analysis_if_not_ready else False)

    def perform_implementation_detail_analysis_group(self, static_load_case_group: '_5596.AbstractStaticLoadCaseGroup', gear_set_mode: '_323.GearSetModes', run_all_planetary_meshes: Optional['bool'] = True, perform_system_analysis_if_not_ready: Optional['bool'] = True):
        """ 'PerformImplementationDetailAnalysis' is the original name of this method.

        Args:
            static_load_case_group (mastapy.system_model.analyses_and_results.load_case_groups.AbstractStaticLoadCaseGroup)
            gear_set_mode (mastapy.gears.GearSetModes)
            run_all_planetary_meshes (bool, optional)
            perform_system_analysis_if_not_ready (bool, optional)
        """

        gear_set_mode = conversion.mp_to_pn_enum(gear_set_mode)
        run_all_planetary_meshes = bool(run_all_planetary_meshes)
        perform_system_analysis_if_not_ready = bool(perform_system_analysis_if_not_ready)
        self.wrapped.PerformImplementationDetailAnalysis.Overloads[_ABSTRACT_STATIC_LOAD_CASE_GROUP, _GEAR_SET_MODES, _BOOLEAN, _BOOLEAN](static_load_case_group.wrapped if static_load_case_group else None, gear_set_mode, run_all_planetary_meshes if run_all_planetary_meshes else False, perform_system_analysis_if_not_ready if perform_system_analysis_if_not_ready else False)

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
