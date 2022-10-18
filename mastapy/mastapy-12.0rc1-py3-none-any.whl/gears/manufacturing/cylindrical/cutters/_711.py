"""_711.py

InvoluteCutterDesign
"""


from mastapy.gears import _327
from mastapy._internal import enum_with_selected_value_runtime, constructor, conversion
from mastapy.gears.gear_designs.cylindrical import (
    _1078, _1038, _1058, _1077
)
from mastapy._internal.cast_exception import CastException
from mastapy.gears.manufacturing.cylindrical.cutters import _706
from mastapy._internal.python_net import python_net_import

_INVOLUTE_CUTTER_DESIGN = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Cylindrical.Cutters', 'InvoluteCutterDesign')


__docformat__ = 'restructuredtext en'
__all__ = ('InvoluteCutterDesign',)


class InvoluteCutterDesign(_706.CylindricalGearRealCutterDesign):
    """InvoluteCutterDesign

    This is a mastapy class.
    """

    TYPE = _INVOLUTE_CUTTER_DESIGN

    def __init__(self, instance_to_wrap: 'InvoluteCutterDesign.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def hand(self) -> '_327.Hand':
        """Hand: 'Hand' is the original name of this property."""

        temp = self.wrapped.Hand

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp)
        return constructor.new_from_mastapy_type(_327.Hand)(value) if value is not None else None

    @hand.setter
    def hand(self, value: '_327.Hand'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.Hand = value

    @property
    def helix_angle(self) -> 'float':
        """float: 'HelixAngle' is the original name of this property."""

        temp = self.wrapped.HelixAngle

        if temp is None:
            return 0.0

        return temp

    @helix_angle.setter
    def helix_angle(self, value: 'float'):
        self.wrapped.HelixAngle = float(value) if value else 0.0

    @property
    def number_of_teeth(self) -> 'float':
        """float: 'NumberOfTeeth' is the original name of this property."""

        temp = self.wrapped.NumberOfTeeth

        if temp is None:
            return 0.0

        return temp

    @number_of_teeth.setter
    def number_of_teeth(self, value: 'float'):
        self.wrapped.NumberOfTeeth = float(value) if value else 0.0

    @property
    def tooth_thickness(self) -> '_1078.ToothThicknessSpecificationBase':
        """ToothThicknessSpecificationBase: 'ToothThickness' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ToothThickness

        if temp is None:
            return None

        if _1078.ToothThicknessSpecificationBase.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast tooth_thickness to ToothThicknessSpecificationBase. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def tooth_thickness_of_type_finish_tooth_thickness_design_specification(self) -> '_1038.FinishToothThicknessDesignSpecification':
        """FinishToothThicknessDesignSpecification: 'ToothThickness' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ToothThickness

        if temp is None:
            return None

        if _1038.FinishToothThicknessDesignSpecification.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast tooth_thickness to FinishToothThicknessDesignSpecification. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def tooth_thickness_of_type_readonly_tooth_thickness_specification(self) -> '_1058.ReadonlyToothThicknessSpecification':
        """ReadonlyToothThicknessSpecification: 'ToothThickness' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ToothThickness

        if temp is None:
            return None

        if _1058.ReadonlyToothThicknessSpecification.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast tooth_thickness to ReadonlyToothThicknessSpecification. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def tooth_thickness_of_type_tooth_thickness_specification(self) -> '_1077.ToothThicknessSpecification':
        """ToothThicknessSpecification: 'ToothThickness' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ToothThickness

        if temp is None:
            return None

        if _1077.ToothThicknessSpecification.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast tooth_thickness to ToothThicknessSpecification. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None
