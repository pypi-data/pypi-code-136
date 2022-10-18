"""_2164.py

ElectricMachineGroup
"""


from typing import List, Optional

from mastapy.electric_machines import _1249, _1253, _1267
from mastapy._internal import constructor, conversion
from mastapy.electric_machines.load_cases_and_analyses import _1328
from mastapy import _0
from mastapy._internal.python_net import python_net_import

_ELECTRIC_MACHINE_GROUP = python_net_import('SMT.MastaAPI.SystemModel', 'ElectricMachineGroup')


__docformat__ = 'restructuredtext en'
__all__ = ('ElectricMachineGroup',)


class ElectricMachineGroup(_0.APIBase):
    """ElectricMachineGroup

    This is a mastapy class.
    """

    TYPE = _ELECTRIC_MACHINE_GROUP

    def __init__(self, instance_to_wrap: 'ElectricMachineGroup.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def electric_machine_details(self) -> 'List[_1249.ElectricMachineDetail]':
        """List[ElectricMachineDetail]: 'ElectricMachineDetails' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ElectricMachineDetails

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def electric_machine_load_case_groups(self) -> 'List[_1328.ElectricMachineLoadCaseGroup]':
        """List[ElectricMachineLoadCaseGroup]: 'ElectricMachineLoadCaseGroups' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ElectricMachineLoadCaseGroups

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    def add_electric_machine_detail(self, type_: '_1253.ElectricMachineType', name: Optional['str'] = 'Motor') -> '_1267.NonCADElectricMachineDetail':
        """ 'AddElectricMachineDetail' is the original name of this method.

        Args:
            type_ (mastapy.electric_machines.ElectricMachineType)
            name (str, optional)

        Returns:
            mastapy.electric_machines.NonCADElectricMachineDetail
        """

        type_ = conversion.mp_to_pn_enum(type_)
        name = str(name)
        method_result = self.wrapped.AddElectricMachineDetail(type_, name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def add_load_case_group(self, name: Optional['str'] = 'New Load Case Group') -> '_1328.ElectricMachineLoadCaseGroup':
        """ 'AddLoadCaseGroup' is the original name of this method.

        Args:
            name (str, optional)

        Returns:
            mastapy.electric_machines.load_cases_and_analyses.ElectricMachineLoadCaseGroup
        """

        name = str(name)
        method_result = self.wrapped.AddLoadCaseGroup(name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def duplicate_electric_machine_detail(self, detail: '_1249.ElectricMachineDetail') -> '_1249.ElectricMachineDetail':
        """ 'DuplicateElectricMachineDetail' is the original name of this method.

        Args:
            detail (mastapy.electric_machines.ElectricMachineDetail)

        Returns:
            mastapy.electric_machines.ElectricMachineDetail
        """

        method_result = self.wrapped.DuplicateElectricMachineDetail(detail.wrapped if detail else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def electric_machine_detail_named(self, name: 'str', has_non_linear_dq_model: 'bool') -> '_1249.ElectricMachineDetail':
        """ 'ElectricMachineDetailNamed' is the original name of this method.

        Args:
            name (str)
            has_non_linear_dq_model (bool)

        Returns:
            mastapy.electric_machines.ElectricMachineDetail
        """

        name = str(name)
        has_non_linear_dq_model = bool(has_non_linear_dq_model)
        method_result = self.wrapped.ElectricMachineDetailNamed(name if name else '', has_non_linear_dq_model if has_non_linear_dq_model else False)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def load_case_group_named(self, load_case_group_name: 'str') -> '_1328.ElectricMachineLoadCaseGroup':
        """ 'LoadCaseGroupNamed' is the original name of this method.

        Args:
            load_case_group_name (str)

        Returns:
            mastapy.electric_machines.load_cases_and_analyses.ElectricMachineLoadCaseGroup
        """

        load_case_group_name = str(load_case_group_name)
        method_result = self.wrapped.LoadCaseGroupNamed(load_case_group_name if load_case_group_name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def remove_all_electric_machine_details(self):
        """ 'RemoveAllElectricMachineDetails' is the original name of this method."""

        self.wrapped.RemoveAllElectricMachineDetails()

    def remove_all_load_case_groups(self):
        """ 'RemoveAllLoadCaseGroups' is the original name of this method."""

        self.wrapped.RemoveAllLoadCaseGroups()

    def remove_electric_machine_detail(self, motor: '_1249.ElectricMachineDetail') -> 'bool':
        """ 'RemoveElectricMachineDetail' is the original name of this method.

        Args:
            motor (mastapy.electric_machines.ElectricMachineDetail)

        Returns:
            bool
        """

        method_result = self.wrapped.RemoveElectricMachineDetail(motor.wrapped if motor else None)
        return method_result

    def remove_electric_machine_detail_named(self, name: 'str', has_non_linear_dq_model: 'bool') -> 'bool':
        """ 'RemoveElectricMachineDetailNamed' is the original name of this method.

        Args:
            name (str)
            has_non_linear_dq_model (bool)

        Returns:
            bool
        """

        name = str(name)
        has_non_linear_dq_model = bool(has_non_linear_dq_model)
        method_result = self.wrapped.RemoveElectricMachineDetailNamed(name if name else '', has_non_linear_dq_model if has_non_linear_dq_model else False)
        return method_result

    def remove_load_case_group_named(self, name: 'str') -> 'bool':
        """ 'RemoveLoadCaseGroupNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            bool
        """

        name = str(name)
        method_result = self.wrapped.RemoveLoadCaseGroupNamed(name if name else '')
        return method_result

    def try_remove_load_case_group(self, load_case_group: '_1328.ElectricMachineLoadCaseGroup') -> 'bool':
        """ 'TryRemoveLoadCaseGroup' is the original name of this method.

        Args:
            load_case_group (mastapy.electric_machines.load_cases_and_analyses.ElectricMachineLoadCaseGroup)

        Returns:
            bool
        """

        method_result = self.wrapped.TryRemoveLoadCaseGroup(load_case_group.wrapped if load_case_group else None)
        return method_result
