"""_179.py

FEModel
"""


from typing import List

from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy.nodal_analysis.dev_tools_analyses import _194, _184
from mastapy.nodal_analysis.dev_tools_analyses.full_fe_reporting import (
    _204, _198, _199, _205,
    _206, _212, _203, _207,
    _208, _209, _210, _202,
    _213
)
from mastapy import _0
from mastapy._internal.python_net import python_net_import

_FE_MODEL = python_net_import('SMT.MastaAPI.NodalAnalysis.DevToolsAnalyses', 'FEModel')


__docformat__ = 'restructuredtext en'
__all__ = ('FEModel',)


class FEModel(_0.APIBase):
    """FEModel

    This is a mastapy class.
    """

    TYPE = _FE_MODEL

    def __init__(self, instance_to_wrap: 'FEModel.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def edge_angle_tolerance(self) -> 'float':
        """float: 'EdgeAngleTolerance' is the original name of this property."""

        temp = self.wrapped.EdgeAngleTolerance

        if temp is None:
            return 0.0

        return temp

    @edge_angle_tolerance.setter
    def edge_angle_tolerance(self, value: 'float'):
        self.wrapped.EdgeAngleTolerance = float(value) if value else 0.0

    @property
    def model_force_unit(self) -> 'str':
        """str: 'ModelForceUnit' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ModelForceUnit

        if temp is None:
            return ''

        return temp

    @property
    def model_length_unit(self) -> 'str':
        """str: 'ModelLengthUnit' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ModelLengthUnit

        if temp is None:
            return ''

        return temp

    @property
    def model_splitting_method(self) -> '_194.ModelSplittingMethod':
        """ModelSplittingMethod: 'ModelSplittingMethod' is the original name of this property."""

        temp = self.wrapped.ModelSplittingMethod

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp)
        return constructor.new_from_mastapy_type(_194.ModelSplittingMethod)(value) if value is not None else None

    @model_splitting_method.setter
    def model_splitting_method(self, value: '_194.ModelSplittingMethod'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.ModelSplittingMethod = value

    @property
    def number_of_elements(self) -> 'int':
        """int: 'NumberOfElements' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NumberOfElements

        if temp is None:
            return 0

        return temp

    @property
    def number_of_elements_with_negative_jacobian(self) -> 'int':
        """int: 'NumberOfElementsWithNegativeJacobian' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NumberOfElementsWithNegativeJacobian

        if temp is None:
            return 0

        return temp

    @property
    def number_of_elements_with_negative_size(self) -> 'int':
        """int: 'NumberOfElementsWithNegativeSize' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NumberOfElementsWithNegativeSize

        if temp is None:
            return 0

        return temp

    @property
    def number_of_nodes(self) -> 'int':
        """int: 'NumberOfNodes' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NumberOfNodes

        if temp is None:
            return 0

        return temp

    @property
    def original_file_path(self) -> 'str':
        """str: 'OriginalFilePath' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OriginalFilePath

        if temp is None:
            return ''

        return temp

    @property
    def use_simplified_normal_calculation_when_deformed(self) -> 'bool':
        """bool: 'UseSimplifiedNormalCalculationWhenDeformed' is the original name of this property."""

        temp = self.wrapped.UseSimplifiedNormalCalculationWhenDeformed

        if temp is None:
            return False

        return temp

    @use_simplified_normal_calculation_when_deformed.setter
    def use_simplified_normal_calculation_when_deformed(self, value: 'bool'):
        self.wrapped.UseSimplifiedNormalCalculationWhenDeformed = bool(value) if value else False

    @property
    def beam_element_properties(self) -> 'List[_204.ElementPropertiesBeam]':
        """List[ElementPropertiesBeam]: 'BeamElementProperties' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BeamElementProperties

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def contact_pairs(self) -> 'List[_198.ContactPairReporting]':
        """List[ContactPairReporting]: 'ContactPairs' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ContactPairs

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def coordinate_systems(self) -> 'List[_199.CoordinateSystemReporting]':
        """List[CoordinateSystemReporting]: 'CoordinateSystems' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CoordinateSystems

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def interface_element_properties(self) -> 'List[_205.ElementPropertiesInterface]':
        """List[ElementPropertiesInterface]: 'InterfaceElementProperties' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InterfaceElementProperties

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def mass_element_properties(self) -> 'List[_206.ElementPropertiesMass]':
        """List[ElementPropertiesMass]: 'MassElementProperties' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MassElementProperties

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def materials(self) -> 'List[_212.MaterialPropertiesReporting]':
        """List[MaterialPropertiesReporting]: 'Materials' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Materials

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def model_parts(self) -> 'List[_184.FEModelPart]':
        """List[FEModelPart]: 'ModelParts' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ModelParts

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def other_element_properties(self) -> 'List[_203.ElementPropertiesBase]':
        """List[ElementPropertiesBase]: 'OtherElementProperties' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OtherElementProperties

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def rigid_element_properties(self) -> 'List[_207.ElementPropertiesRigid]':
        """List[ElementPropertiesRigid]: 'RigidElementProperties' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RigidElementProperties

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def shell_element_properties(self) -> 'List[_208.ElementPropertiesShell]':
        """List[ElementPropertiesShell]: 'ShellElementProperties' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ShellElementProperties

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def solid_element_properties(self) -> 'List[_209.ElementPropertiesSolid]':
        """List[ElementPropertiesSolid]: 'SolidElementProperties' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SolidElementProperties

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def spring_dashpot_element_properties(self) -> 'List[_210.ElementPropertiesSpringDashpot]':
        """List[ElementPropertiesSpringDashpot]: 'SpringDashpotElementProperties' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SpringDashpotElementProperties

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

    def add_new_material(self):
        """ 'AddNewMaterial' is the original name of this method."""

        self.wrapped.AddNewMaterial()

    def change_interpolation_constraints_to_distributing(self):
        """ 'ChangeInterpolationConstraintsToDistributing' is the original name of this method."""

        self.wrapped.ChangeInterpolationConstraintsToDistributing()

    def delete_unused_element_properties(self):
        """ 'DeleteUnusedElementProperties' is the original name of this method."""

        self.wrapped.DeleteUnusedElementProperties()

    def delete_unused_materials(self):
        """ 'DeleteUnusedMaterials' is the original name of this method."""

        self.wrapped.DeleteUnusedMaterials()

    def get_all_element_details(self) -> '_202.ElementDetailsForFEModel':
        """ 'GetAllElementDetails' is the original name of this method.

        Returns:
            mastapy.nodal_analysis.dev_tools_analyses.full_fe_reporting.ElementDetailsForFEModel
        """

        method_result = self.wrapped.GetAllElementDetails()
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def get_all_node_details(self) -> '_213.NodeDetailsForFEModel':
        """ 'GetAllNodeDetails' is the original name of this method.

        Returns:
            mastapy.nodal_analysis.dev_tools_analyses.full_fe_reporting.NodeDetailsForFEModel
        """

        method_result = self.wrapped.GetAllNodeDetails()
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
