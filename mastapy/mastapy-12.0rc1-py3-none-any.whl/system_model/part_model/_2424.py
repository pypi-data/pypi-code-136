"""_2424.py

PowerLoad
"""


from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy._internal.implicit import list_with_selected_item, enum_with_selected_value, overridable
from mastapy.electric_machines import (
    _1249, _1235, _1259, _1267,
    _1270, _1283, _1285
)
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.system_model.part_model import _2401, _2433, _2431
from mastapy.math_utility.measured_data import _1530
from mastapy.system_model import _2174
from mastapy._internal.cast_exception import CastException
from mastapy.materials.efficiency import _292
from mastapy._internal.python_net import python_net_import

_POWER_LOAD = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'PowerLoad')


__docformat__ = 'restructuredtext en'
__all__ = ('PowerLoad',)


class PowerLoad(_2431.VirtualComponent):
    """PowerLoad

    This is a mastapy class.
    """

    TYPE = _POWER_LOAD

    def __init__(self, instance_to_wrap: 'PowerLoad.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def effective_length_of_stator(self) -> 'float':
        """float: 'EffectiveLengthOfStator' is the original name of this property."""

        temp = self.wrapped.EffectiveLengthOfStator

        if temp is None:
            return 0.0

        return temp

    @effective_length_of_stator.setter
    def effective_length_of_stator(self, value: 'float'):
        self.wrapped.EffectiveLengthOfStator = float(value) if value else 0.0

    @property
    def electric_machine_detail_selector(self) -> 'list_with_selected_item.ListWithSelectedItem_ElectricMachineDetail':
        """list_with_selected_item.ListWithSelectedItem_ElectricMachineDetail: 'ElectricMachineDetailSelector' is the original name of this property."""

        temp = self.wrapped.ElectricMachineDetailSelector

        if temp is None:
            return None

        return constructor.new_from_mastapy_type(list_with_selected_item.ListWithSelectedItem_ElectricMachineDetail)(temp) if temp is not None else None

    @electric_machine_detail_selector.setter
    def electric_machine_detail_selector(self, value: 'list_with_selected_item.ListWithSelectedItem_ElectricMachineDetail.implicit_type()'):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_ElectricMachineDetail.wrapper_type()
        enclosed_type = list_with_selected_item.ListWithSelectedItem_ElectricMachineDetail.implicit_type()
        value = wrapper_type[enclosed_type](value.wrapped if value is not None else None)
        self.wrapped.ElectricMachineDetailSelector = value

    @property
    def electric_machine_search_region_specification_method(self) -> '_2401.ElectricMachineSearchRegionSpecificationMethod':
        """ElectricMachineSearchRegionSpecificationMethod: 'ElectricMachineSearchRegionSpecificationMethod' is the original name of this property."""

        temp = self.wrapped.ElectricMachineSearchRegionSpecificationMethod

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp)
        return constructor.new_from_mastapy_type(_2401.ElectricMachineSearchRegionSpecificationMethod)(value) if value is not None else None

    @electric_machine_search_region_specification_method.setter
    def electric_machine_search_region_specification_method(self, value: '_2401.ElectricMachineSearchRegionSpecificationMethod'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.ElectricMachineSearchRegionSpecificationMethod = value

    @property
    def engine_fuel_consumption_grid(self) -> '_1530.GriddedSurfaceAccessor':
        """GriddedSurfaceAccessor: 'EngineFuelConsumptionGrid' is the original name of this property."""

        temp = self.wrapped.EngineFuelConsumptionGrid

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @engine_fuel_consumption_grid.setter
    def engine_fuel_consumption_grid(self, value: '_1530.GriddedSurfaceAccessor'):
        value = value.wrapped if value else None
        self.wrapped.EngineFuelConsumptionGrid = value

    @property
    def engine_torque_grid(self) -> '_1530.GriddedSurfaceAccessor':
        """GriddedSurfaceAccessor: 'EngineTorqueGrid' is the original name of this property."""

        temp = self.wrapped.EngineTorqueGrid

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @engine_torque_grid.setter
    def engine_torque_grid(self, value: '_1530.GriddedSurfaceAccessor'):
        value = value.wrapped if value else None
        self.wrapped.EngineTorqueGrid = value

    @property
    def include_in_torsional_stiffness_calculation(self) -> 'bool':
        """bool: 'IncludeInTorsionalStiffnessCalculation' is the original name of this property."""

        temp = self.wrapped.IncludeInTorsionalStiffnessCalculation

        if temp is None:
            return False

        return temp

    @include_in_torsional_stiffness_calculation.setter
    def include_in_torsional_stiffness_calculation(self, value: 'bool'):
        self.wrapped.IncludeInTorsionalStiffnessCalculation = bool(value) if value else False

    @property
    def inner_diameter_of_stator_teeth(self) -> 'float':
        """float: 'InnerDiameterOfStatorTeeth' is the original name of this property."""

        temp = self.wrapped.InnerDiameterOfStatorTeeth

        if temp is None:
            return 0.0

        return temp

    @inner_diameter_of_stator_teeth.setter
    def inner_diameter_of_stator_teeth(self, value: 'float'):
        self.wrapped.InnerDiameterOfStatorTeeth = float(value) if value else 0.0

    @property
    def number_of_wheels(self) -> 'int':
        """int: 'NumberOfWheels' is the original name of this property."""

        temp = self.wrapped.NumberOfWheels

        if temp is None:
            return 0

        return temp

    @number_of_wheels.setter
    def number_of_wheels(self, value: 'int'):
        self.wrapped.NumberOfWheels = int(value) if value else 0

    @property
    def number_of_blades(self) -> 'int':
        """int: 'NumberOfBlades' is the original name of this property."""

        temp = self.wrapped.NumberOfBlades

        if temp is None:
            return 0

        return temp

    @number_of_blades.setter
    def number_of_blades(self, value: 'int'):
        self.wrapped.NumberOfBlades = int(value) if value else 0

    @property
    def number_of_slots(self) -> 'int':
        """int: 'NumberOfSlots' is the original name of this property."""

        temp = self.wrapped.NumberOfSlots

        if temp is None:
            return 0

        return temp

    @number_of_slots.setter
    def number_of_slots(self, value: 'int'):
        self.wrapped.NumberOfSlots = int(value) if value else 0

    @property
    def positive_is_forwards(self) -> 'bool':
        """bool: 'PositiveIsForwards' is the original name of this property."""

        temp = self.wrapped.PositiveIsForwards

        if temp is None:
            return False

        return temp

    @positive_is_forwards.setter
    def positive_is_forwards(self, value: 'bool'):
        self.wrapped.PositiveIsForwards = bool(value) if value else False

    @property
    def power_load_type(self) -> 'enum_with_selected_value.EnumWithSelectedValue_PowerLoadType':
        """enum_with_selected_value.EnumWithSelectedValue_PowerLoadType: 'PowerLoadType' is the original name of this property."""

        temp = self.wrapped.PowerLoadType

        if temp is None:
            return None

        value = enum_with_selected_value.EnumWithSelectedValue_PowerLoadType.wrapped_type()
        return enum_with_selected_value_runtime.create(temp, value) if temp is not None else None

    @power_load_type.setter
    def power_load_type(self, value: 'enum_with_selected_value.EnumWithSelectedValue_PowerLoadType.implicit_type()'):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = enum_with_selected_value.EnumWithSelectedValue_PowerLoadType.implicit_type()
        value = conversion.mp_to_pn_enum(value)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.PowerLoadType = value

    @property
    def torsional_stiffness(self) -> 'float':
        """float: 'TorsionalStiffness' is the original name of this property."""

        temp = self.wrapped.TorsionalStiffness

        if temp is None:
            return 0.0

        return temp

    @torsional_stiffness.setter
    def torsional_stiffness(self, value: 'float'):
        self.wrapped.TorsionalStiffness = float(value) if value else 0.0

    @property
    def tyre_rolling_radius(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'TyreRollingRadius' is the original name of this property."""

        temp = self.wrapped.TyreRollingRadius

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @tyre_rolling_radius.setter
    def tyre_rolling_radius(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.TyreRollingRadius = value

    @property
    def width_for_drawing(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'WidthForDrawing' is the original name of this property."""

        temp = self.wrapped.WidthForDrawing

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @width_for_drawing.setter
    def width_for_drawing(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.WidthForDrawing = value

    @property
    def electric_machine_detail(self) -> '_1249.ElectricMachineDetail':
        """ElectricMachineDetail: 'ElectricMachineDetail' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ElectricMachineDetail

        if temp is None:
            return None

        if _1249.ElectricMachineDetail.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast electric_machine_detail to ElectricMachineDetail. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def electric_machine_detail_of_type_cad_electric_machine_detail(self) -> '_1235.CADElectricMachineDetail':
        """CADElectricMachineDetail: 'ElectricMachineDetail' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ElectricMachineDetail

        if temp is None:
            return None

        if _1235.CADElectricMachineDetail.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast electric_machine_detail to CADElectricMachineDetail. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def electric_machine_detail_of_type_interior_permanent_magnet_machine(self) -> '_1259.InteriorPermanentMagnetMachine':
        """InteriorPermanentMagnetMachine: 'ElectricMachineDetail' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ElectricMachineDetail

        if temp is None:
            return None

        if _1259.InteriorPermanentMagnetMachine.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast electric_machine_detail to InteriorPermanentMagnetMachine. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def electric_machine_detail_of_type_non_cad_electric_machine_detail(self) -> '_1267.NonCADElectricMachineDetail':
        """NonCADElectricMachineDetail: 'ElectricMachineDetail' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ElectricMachineDetail

        if temp is None:
            return None

        if _1267.NonCADElectricMachineDetail.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast electric_machine_detail to NonCADElectricMachineDetail. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def electric_machine_detail_of_type_permanent_magnet_assisted_synchronous_reluctance_machine(self) -> '_1270.PermanentMagnetAssistedSynchronousReluctanceMachine':
        """PermanentMagnetAssistedSynchronousReluctanceMachine: 'ElectricMachineDetail' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ElectricMachineDetail

        if temp is None:
            return None

        if _1270.PermanentMagnetAssistedSynchronousReluctanceMachine.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast electric_machine_detail to PermanentMagnetAssistedSynchronousReluctanceMachine. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def electric_machine_detail_of_type_surface_permanent_magnet_machine(self) -> '_1283.SurfacePermanentMagnetMachine':
        """SurfacePermanentMagnetMachine: 'ElectricMachineDetail' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ElectricMachineDetail

        if temp is None:
            return None

        if _1283.SurfacePermanentMagnetMachine.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast electric_machine_detail to SurfacePermanentMagnetMachine. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def electric_machine_detail_of_type_synchronous_reluctance_machine(self) -> '_1285.SynchronousReluctanceMachine':
        """SynchronousReluctanceMachine: 'ElectricMachineDetail' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ElectricMachineDetail

        if temp is None:
            return None

        if _1285.SynchronousReluctanceMachine.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast electric_machine_detail to SynchronousReluctanceMachine. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def oil_pump_detail(self) -> '_292.OilPumpDetail':
        """OilPumpDetail: 'OilPumpDetail' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OilPumpDetail

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def single_blade_details(self) -> '_2433.WindTurbineSingleBladeDetails':
        """WindTurbineSingleBladeDetails: 'SingleBladeDetails' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SingleBladeDetails

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None
