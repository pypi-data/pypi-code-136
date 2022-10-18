"""_716.py

CutterShapeDefinition
"""


from typing import List

from mastapy._internal import constructor, conversion
from mastapy.gears.manufacturing.cylindrical.cutters import (
    _706, _700, _701, _702,
    _703, _705, _707, _708,
    _711
)
from mastapy._internal.cast_exception import CastException
from mastapy.gears.manufacturing.cylindrical.cutters.tangibles import _722
from mastapy import _0
from mastapy._internal.python_net import python_net_import

_CUTTER_SHAPE_DEFINITION = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Cylindrical.Cutters.Tangibles', 'CutterShapeDefinition')


__docformat__ = 'restructuredtext en'
__all__ = ('CutterShapeDefinition',)


class CutterShapeDefinition(_0.APIBase):
    """CutterShapeDefinition

    This is a mastapy class.
    """

    TYPE = _CUTTER_SHAPE_DEFINITION

    def __init__(self, instance_to_wrap: 'CutterShapeDefinition.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def normal_module(self) -> 'float':
        """float: 'NormalModule' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NormalModule

        if temp is None:
            return 0.0

        return temp

    @property
    def normal_pitch(self) -> 'float':
        """float: 'NormalPitch' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NormalPitch

        if temp is None:
            return 0.0

        return temp

    @property
    def normal_pressure_angle(self) -> 'float':
        """float: 'NormalPressureAngle' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NormalPressureAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def design(self) -> '_706.CylindricalGearRealCutterDesign':
        """CylindricalGearRealCutterDesign: 'Design' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Design

        if temp is None:
            return None

        if _706.CylindricalGearRealCutterDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast design to CylindricalGearRealCutterDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def design_of_type_cylindrical_gear_form_grinding_wheel(self) -> '_700.CylindricalGearFormGrindingWheel':
        """CylindricalGearFormGrindingWheel: 'Design' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Design

        if temp is None:
            return None

        if _700.CylindricalGearFormGrindingWheel.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast design to CylindricalGearFormGrindingWheel. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def design_of_type_cylindrical_gear_grinding_worm(self) -> '_701.CylindricalGearGrindingWorm':
        """CylindricalGearGrindingWorm: 'Design' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Design

        if temp is None:
            return None

        if _701.CylindricalGearGrindingWorm.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast design to CylindricalGearGrindingWorm. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def design_of_type_cylindrical_gear_hob_design(self) -> '_702.CylindricalGearHobDesign':
        """CylindricalGearHobDesign: 'Design' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Design

        if temp is None:
            return None

        if _702.CylindricalGearHobDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast design to CylindricalGearHobDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def design_of_type_cylindrical_gear_plunge_shaver(self) -> '_703.CylindricalGearPlungeShaver':
        """CylindricalGearPlungeShaver: 'Design' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Design

        if temp is None:
            return None

        if _703.CylindricalGearPlungeShaver.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast design to CylindricalGearPlungeShaver. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def design_of_type_cylindrical_gear_rack_design(self) -> '_705.CylindricalGearRackDesign':
        """CylindricalGearRackDesign: 'Design' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Design

        if temp is None:
            return None

        if _705.CylindricalGearRackDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast design to CylindricalGearRackDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def design_of_type_cylindrical_gear_shaper(self) -> '_707.CylindricalGearShaper':
        """CylindricalGearShaper: 'Design' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Design

        if temp is None:
            return None

        if _707.CylindricalGearShaper.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast design to CylindricalGearShaper. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def design_of_type_cylindrical_gear_shaver(self) -> '_708.CylindricalGearShaver':
        """CylindricalGearShaver: 'Design' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Design

        if temp is None:
            return None

        if _708.CylindricalGearShaver.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast design to CylindricalGearShaver. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def design_of_type_involute_cutter_design(self) -> '_711.InvoluteCutterDesign':
        """InvoluteCutterDesign: 'Design' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Design

        if temp is None:
            return None

        if _711.InvoluteCutterDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast design to InvoluteCutterDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def fillet_points(self) -> 'List[_722.NamedPoint]':
        """List[NamedPoint]: 'FilletPoints' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FilletPoints

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def main_blade_points(self) -> 'List[_722.NamedPoint]':
        """List[NamedPoint]: 'MainBladePoints' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MainBladePoints

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value
