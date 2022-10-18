"""_1183.py

AGMAGleasonConicalGearDesign
"""


from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy.gears.gear_designs.conical import (
    _1154, _1147, _1148, _1143,
    _1153, _1144
)
from mastapy._internal.implicit import enum_with_selected_value
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal.python_net import python_net_import
from mastapy.gears import _308
from mastapy.gears.gear_designs.cylindrical.accuracy_and_tolerances import _1126, _1130, _1135
from mastapy._internal.cast_exception import CastException
from mastapy.gears.gear_designs.agma_gleason_conical import _1182
from mastapy.gears.materials import (
    _587, _576, _578, _580,
    _584, _590, _594, _596
)
from mastapy.gears.manufacturing.bevel.cutters import (
    _806, _807, _808, _809
)

_DATABASE_WITH_SELECTED_ITEM = python_net_import('SMT.MastaAPI.UtilityGUI.Databases', 'DatabaseWithSelectedItem')
_AGMA_GLEASON_CONICAL_GEAR_DESIGN = python_net_import('SMT.MastaAPI.Gears.GearDesigns.AGMAGleasonConical', 'AGMAGleasonConicalGearDesign')


__docformat__ = 'restructuredtext en'
__all__ = ('AGMAGleasonConicalGearDesign',)


class AGMAGleasonConicalGearDesign(_1144.ConicalGearDesign):
    """AGMAGleasonConicalGearDesign

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_DESIGN

    def __init__(self, instance_to_wrap: 'AGMAGleasonConicalGearDesign.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def allowable_bending_stress(self) -> 'float':
        """float: 'AllowableBendingStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AllowableBendingStress

        if temp is None:
            return 0.0

        return temp

    @property
    def allowable_contact_stress(self) -> 'float':
        """float: 'AllowableContactStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AllowableContactStress

        if temp is None:
            return 0.0

        return temp

    @property
    def face_width(self) -> 'float':
        """float: 'FaceWidth' is the original name of this property."""

        temp = self.wrapped.FaceWidth

        if temp is None:
            return 0.0

        return temp

    @face_width.setter
    def face_width(self, value: 'float'):
        self.wrapped.FaceWidth = float(value) if value else 0.0

    @property
    def front_end_type(self) -> '_1154.FrontEndTypes':
        """FrontEndTypes: 'FrontEndType' is the original name of this property."""

        temp = self.wrapped.FrontEndType

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp)
        return constructor.new_from_mastapy_type(_1154.FrontEndTypes)(value) if value is not None else None

    @front_end_type.setter
    def front_end_type(self, value: '_1154.FrontEndTypes'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.FrontEndType = value

    @property
    def machine_setting_calculation_method(self) -> 'enum_with_selected_value.EnumWithSelectedValue_ConicalMachineSettingCalculationMethods':
        """enum_with_selected_value.EnumWithSelectedValue_ConicalMachineSettingCalculationMethods: 'MachineSettingCalculationMethod' is the original name of this property."""

        temp = self.wrapped.MachineSettingCalculationMethod

        if temp is None:
            return None

        value = enum_with_selected_value.EnumWithSelectedValue_ConicalMachineSettingCalculationMethods.wrapped_type()
        return enum_with_selected_value_runtime.create(temp, value) if temp is not None else None

    @machine_setting_calculation_method.setter
    def machine_setting_calculation_method(self, value: 'enum_with_selected_value.EnumWithSelectedValue_ConicalMachineSettingCalculationMethods.implicit_type()'):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = enum_with_selected_value.EnumWithSelectedValue_ConicalMachineSettingCalculationMethods.implicit_type()
        value = conversion.mp_to_pn_enum(value)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.MachineSettingCalculationMethod = value

    @property
    def manufacture_method(self) -> 'enum_with_selected_value.EnumWithSelectedValue_ConicalManufactureMethods':
        """enum_with_selected_value.EnumWithSelectedValue_ConicalManufactureMethods: 'ManufactureMethod' is the original name of this property."""

        temp = self.wrapped.ManufactureMethod

        if temp is None:
            return None

        value = enum_with_selected_value.EnumWithSelectedValue_ConicalManufactureMethods.wrapped_type()
        return enum_with_selected_value_runtime.create(temp, value) if temp is not None else None

    @manufacture_method.setter
    def manufacture_method(self, value: 'enum_with_selected_value.EnumWithSelectedValue_ConicalManufactureMethods.implicit_type()'):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = enum_with_selected_value.EnumWithSelectedValue_ConicalManufactureMethods.implicit_type()
        value = conversion.mp_to_pn_enum(value)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.ManufactureMethod = value

    @property
    def material(self) -> 'str':
        """str: 'Material' is the original name of this property."""

        temp = self.wrapped.Material.SelectedItemName

        if temp is None:
            return ''

        return temp

    @material.setter
    def material(self, value: 'str'):
        self.wrapped.Material.SetSelectedItem(str(value) if value else '')

    @property
    def accuracy_grades(self) -> '_308.AccuracyGrades':
        """AccuracyGrades: 'AccuracyGrades' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AccuracyGrades

        if temp is None:
            return None

        if _308.AccuracyGrades.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast accuracy_grades to AccuracyGrades. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def accuracy_grades_of_type_agma20151_accuracy_grades(self) -> '_1126.AGMA20151AccuracyGrades':
        """AGMA20151AccuracyGrades: 'AccuracyGrades' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AccuracyGrades

        if temp is None:
            return None

        if _1126.AGMA20151AccuracyGrades.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast accuracy_grades to AGMA20151AccuracyGrades. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def accuracy_grades_of_type_cylindrical_accuracy_grades(self) -> '_1130.CylindricalAccuracyGrades':
        """CylindricalAccuracyGrades: 'AccuracyGrades' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AccuracyGrades

        if temp is None:
            return None

        if _1130.CylindricalAccuracyGrades.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast accuracy_grades to CylindricalAccuracyGrades. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def accuracy_grades_of_type_iso1328_accuracy_grades(self) -> '_1135.ISO1328AccuracyGrades':
        """ISO1328AccuracyGrades: 'AccuracyGrades' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AccuracyGrades

        if temp is None:
            return None

        if _1135.ISO1328AccuracyGrades.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast accuracy_grades to ISO1328AccuracyGrades. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def accuracy_grades_of_type_agma_gleason_conical_accuracy_grades(self) -> '_1182.AGMAGleasonConicalAccuracyGrades':
        """AGMAGleasonConicalAccuracyGrades: 'AccuracyGrades' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AccuracyGrades

        if temp is None:
            return None

        if _1182.AGMAGleasonConicalAccuracyGrades.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast accuracy_grades to AGMAGleasonConicalAccuracyGrades. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bevel_gear_material(self) -> '_587.GearMaterial':
        """GearMaterial: 'BevelGearMaterial' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BevelGearMaterial

        if temp is None:
            return None

        if _587.GearMaterial.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast bevel_gear_material to GearMaterial. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bevel_gear_material_of_type_agma_cylindrical_gear_material(self) -> '_576.AGMACylindricalGearMaterial':
        """AGMACylindricalGearMaterial: 'BevelGearMaterial' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BevelGearMaterial

        if temp is None:
            return None

        if _576.AGMACylindricalGearMaterial.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast bevel_gear_material to AGMACylindricalGearMaterial. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bevel_gear_material_of_type_bevel_gear_iso_material(self) -> '_578.BevelGearISOMaterial':
        """BevelGearISOMaterial: 'BevelGearMaterial' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BevelGearMaterial

        if temp is None:
            return None

        if _578.BevelGearISOMaterial.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast bevel_gear_material to BevelGearISOMaterial. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bevel_gear_material_of_type_bevel_gear_material(self) -> '_580.BevelGearMaterial':
        """BevelGearMaterial: 'BevelGearMaterial' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BevelGearMaterial

        if temp is None:
            return None

        if _580.BevelGearMaterial.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast bevel_gear_material to BevelGearMaterial. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bevel_gear_material_of_type_cylindrical_gear_material(self) -> '_584.CylindricalGearMaterial':
        """CylindricalGearMaterial: 'BevelGearMaterial' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BevelGearMaterial

        if temp is None:
            return None

        if _584.CylindricalGearMaterial.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast bevel_gear_material to CylindricalGearMaterial. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bevel_gear_material_of_type_iso_cylindrical_gear_material(self) -> '_590.ISOCylindricalGearMaterial':
        """ISOCylindricalGearMaterial: 'BevelGearMaterial' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BevelGearMaterial

        if temp is None:
            return None

        if _590.ISOCylindricalGearMaterial.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast bevel_gear_material to ISOCylindricalGearMaterial. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bevel_gear_material_of_type_klingelnberg_cyclo_palloid_conical_gear_material(self) -> '_594.KlingelnbergCycloPalloidConicalGearMaterial':
        """KlingelnbergCycloPalloidConicalGearMaterial: 'BevelGearMaterial' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BevelGearMaterial

        if temp is None:
            return None

        if _594.KlingelnbergCycloPalloidConicalGearMaterial.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast bevel_gear_material to KlingelnbergCycloPalloidConicalGearMaterial. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bevel_gear_material_of_type_plastic_cylindrical_gear_material(self) -> '_596.PlasticCylindricalGearMaterial':
        """PlasticCylindricalGearMaterial: 'BevelGearMaterial' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BevelGearMaterial

        if temp is None:
            return None

        if _596.PlasticCylindricalGearMaterial.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast bevel_gear_material to PlasticCylindricalGearMaterial. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cutter(self) -> '_1143.ConicalGearCutter':
        """ConicalGearCutter: 'Cutter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Cutter

        if temp is None:
            return None

        if _1143.ConicalGearCutter.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast cutter to ConicalGearCutter. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cutter_of_type_pinion_finish_cutter(self) -> '_806.PinionFinishCutter':
        """PinionFinishCutter: 'Cutter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Cutter

        if temp is None:
            return None

        if _806.PinionFinishCutter.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast cutter to PinionFinishCutter. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cutter_of_type_pinion_rough_cutter(self) -> '_807.PinionRoughCutter':
        """PinionRoughCutter: 'Cutter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Cutter

        if temp is None:
            return None

        if _807.PinionRoughCutter.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast cutter to PinionRoughCutter. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cutter_of_type_wheel_finish_cutter(self) -> '_808.WheelFinishCutter':
        """WheelFinishCutter: 'Cutter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Cutter

        if temp is None:
            return None

        if _808.WheelFinishCutter.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast cutter to WheelFinishCutter. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cutter_of_type_wheel_rough_cutter(self) -> '_809.WheelRoughCutter':
        """WheelRoughCutter: 'Cutter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Cutter

        if temp is None:
            return None

        if _809.WheelRoughCutter.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast cutter to WheelRoughCutter. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cutter_of_type_dummy_conical_gear_cutter(self) -> '_1153.DummyConicalGearCutter':
        """DummyConicalGearCutter: 'Cutter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Cutter

        if temp is None:
            return None

        if _1153.DummyConicalGearCutter.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast cutter to DummyConicalGearCutter. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None
