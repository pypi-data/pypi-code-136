"""_1286.py

ToothAndSlot
"""


from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy.electric_machines import _1287, _1234
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal.python_net import python_net_import

_TOOTH_AND_SLOT = python_net_import('SMT.MastaAPI.ElectricMachines', 'ToothAndSlot')


__docformat__ = 'restructuredtext en'
__all__ = ('ToothAndSlot',)


class ToothAndSlot(_1234.AbstractToothAndSlot):
    """ToothAndSlot

    This is a mastapy class.
    """

    TYPE = _TOOTH_AND_SLOT

    def __init__(self, instance_to_wrap: 'ToothAndSlot.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def full_round_at_slot_bottom(self) -> 'bool':
        """bool: 'FullRoundAtSlotBottom' is the original name of this property."""

        temp = self.wrapped.FullRoundAtSlotBottom

        if temp is None:
            return False

        return temp

    @full_round_at_slot_bottom.setter
    def full_round_at_slot_bottom(self, value: 'bool'):
        self.wrapped.FullRoundAtSlotBottom = bool(value) if value else False

    @property
    def has_wedges(self) -> 'bool':
        """bool: 'HasWedges' is the original name of this property."""

        temp = self.wrapped.HasWedges

        if temp is None:
            return False

        return temp

    @has_wedges.setter
    def has_wedges(self, value: 'bool'):
        self.wrapped.HasWedges = bool(value) if value else False

    @property
    def radius_of_curvature_at_slot_bottom(self) -> 'float':
        """float: 'RadiusOfCurvatureAtSlotBottom' is the original name of this property."""

        temp = self.wrapped.RadiusOfCurvatureAtSlotBottom

        if temp is None:
            return 0.0

        return temp

    @radius_of_curvature_at_slot_bottom.setter
    def radius_of_curvature_at_slot_bottom(self, value: 'float'):
        self.wrapped.RadiusOfCurvatureAtSlotBottom = float(value) if value else 0.0

    @property
    def slot_depth(self) -> 'float':
        """float: 'SlotDepth' is the original name of this property."""

        temp = self.wrapped.SlotDepth

        if temp is None:
            return 0.0

        return temp

    @slot_depth.setter
    def slot_depth(self, value: 'float'):
        self.wrapped.SlotDepth = float(value) if value else 0.0

    @property
    def slot_opening_length(self) -> 'float':
        """float: 'SlotOpeningLength' is the original name of this property."""

        temp = self.wrapped.SlotOpeningLength

        if temp is None:
            return 0.0

        return temp

    @slot_opening_length.setter
    def slot_opening_length(self, value: 'float'):
        self.wrapped.SlotOpeningLength = float(value) if value else 0.0

    @property
    def slot_width(self) -> 'float':
        """float: 'SlotWidth' is the original name of this property."""

        temp = self.wrapped.SlotWidth

        if temp is None:
            return 0.0

        return temp

    @slot_width.setter
    def slot_width(self, value: 'float'):
        self.wrapped.SlotWidth = float(value) if value else 0.0

    @property
    def tooth_asymmetric_length(self) -> 'float':
        """float: 'ToothAsymmetricLength' is the original name of this property."""

        temp = self.wrapped.ToothAsymmetricLength

        if temp is None:
            return 0.0

        return temp

    @tooth_asymmetric_length.setter
    def tooth_asymmetric_length(self, value: 'float'):
        self.wrapped.ToothAsymmetricLength = float(value) if value else 0.0

    @property
    def tooth_taper_depth(self) -> 'float':
        """float: 'ToothTaperDepth' is the original name of this property."""

        temp = self.wrapped.ToothTaperDepth

        if temp is None:
            return 0.0

        return temp

    @tooth_taper_depth.setter
    def tooth_taper_depth(self, value: 'float'):
        self.wrapped.ToothTaperDepth = float(value) if value else 0.0

    @property
    def tooth_tip_depth(self) -> 'float':
        """float: 'ToothTipDepth' is the original name of this property."""

        temp = self.wrapped.ToothTipDepth

        if temp is None:
            return 0.0

        return temp

    @tooth_tip_depth.setter
    def tooth_tip_depth(self, value: 'float'):
        self.wrapped.ToothTipDepth = float(value) if value else 0.0

    @property
    def tooth_width(self) -> 'float':
        """float: 'ToothWidth' is the original name of this property."""

        temp = self.wrapped.ToothWidth

        if temp is None:
            return 0.0

        return temp

    @tooth_width.setter
    def tooth_width(self, value: 'float'):
        self.wrapped.ToothWidth = float(value) if value else 0.0

    @property
    def tooth_width_at_slot_bottom(self) -> 'float':
        """float: 'ToothWidthAtSlotBottom' is the original name of this property."""

        temp = self.wrapped.ToothWidthAtSlotBottom

        if temp is None:
            return 0.0

        return temp

    @tooth_width_at_slot_bottom.setter
    def tooth_width_at_slot_bottom(self, value: 'float'):
        self.wrapped.ToothWidthAtSlotBottom = float(value) if value else 0.0

    @property
    def tooth_width_at_slot_top(self) -> 'float':
        """float: 'ToothWidthAtSlotTop' is the original name of this property."""

        temp = self.wrapped.ToothWidthAtSlotTop

        if temp is None:
            return 0.0

        return temp

    @tooth_width_at_slot_top.setter
    def tooth_width_at_slot_top(self, value: 'float'):
        self.wrapped.ToothWidthAtSlotTop = float(value) if value else 0.0

    @property
    def tooth_slot_style(self) -> '_1287.ToothSlotStyle':
        """ToothSlotStyle: 'ToothSlotStyle' is the original name of this property."""

        temp = self.wrapped.ToothSlotStyle

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp)
        return constructor.new_from_mastapy_type(_1287.ToothSlotStyle)(value) if value is not None else None

    @tooth_slot_style.setter
    def tooth_slot_style(self, value: '_1287.ToothSlotStyle'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.ToothSlotStyle = value

    @property
    def wedge_thickness(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'WedgeThickness' is the original name of this property."""

        temp = self.wrapped.WedgeThickness

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @wedge_thickness.setter
    def wedge_thickness(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.WedgeThickness = value
