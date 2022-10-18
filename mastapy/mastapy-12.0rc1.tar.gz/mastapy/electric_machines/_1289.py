"""_1289.py

VShapedMagnetLayerSpecification
"""


from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.electric_machines import _1255, _1275
from mastapy._internal.python_net import python_net_import

_V_SHAPED_MAGNET_LAYER_SPECIFICATION = python_net_import('SMT.MastaAPI.ElectricMachines', 'VShapedMagnetLayerSpecification')


__docformat__ = 'restructuredtext en'
__all__ = ('VShapedMagnetLayerSpecification',)


class VShapedMagnetLayerSpecification(_1275.RotorInternalLayerSpecification):
    """VShapedMagnetLayerSpecification

    This is a mastapy class.
    """

    TYPE = _V_SHAPED_MAGNET_LAYER_SPECIFICATION

    def __init__(self, instance_to_wrap: 'VShapedMagnetLayerSpecification.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def distance_between_magnets(self) -> 'float':
        """float: 'DistanceBetweenMagnets' is the original name of this property."""

        temp = self.wrapped.DistanceBetweenMagnets

        if temp is None:
            return 0.0

        return temp

    @distance_between_magnets.setter
    def distance_between_magnets(self, value: 'float'):
        self.wrapped.DistanceBetweenMagnets = float(value) if value else 0.0

    @property
    def distance_to_v_shape(self) -> 'float':
        """float: 'DistanceToVShape' is the original name of this property."""

        temp = self.wrapped.DistanceToVShape

        if temp is None:
            return 0.0

        return temp

    @distance_to_v_shape.setter
    def distance_to_v_shape(self, value: 'float'):
        self.wrapped.DistanceToVShape = float(value) if value else 0.0

    @property
    def flux_barrier_length(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'FluxBarrierLength' is the original name of this property."""

        temp = self.wrapped.FluxBarrierLength

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @flux_barrier_length.setter
    def flux_barrier_length(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.FluxBarrierLength = value

    @property
    def has_flux_barriers(self) -> 'bool':
        """bool: 'HasFluxBarriers' is the original name of this property."""

        temp = self.wrapped.HasFluxBarriers

        if temp is None:
            return False

        return temp

    @has_flux_barriers.setter
    def has_flux_barriers(self, value: 'bool'):
        self.wrapped.HasFluxBarriers = bool(value) if value else False

    @property
    def lower_round_height(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'LowerRoundHeight' is the original name of this property."""

        temp = self.wrapped.LowerRoundHeight

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @lower_round_height.setter
    def lower_round_height(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.LowerRoundHeight = value

    @property
    def upper_flux_barrier_web_specification(self) -> '_1255.FluxBarrierOrWeb':
        """FluxBarrierOrWeb: 'UpperFluxBarrierWebSpecification' is the original name of this property."""

        temp = self.wrapped.UpperFluxBarrierWebSpecification

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp)
        return constructor.new_from_mastapy_type(_1255.FluxBarrierOrWeb)(value) if value is not None else None

    @upper_flux_barrier_web_specification.setter
    def upper_flux_barrier_web_specification(self, value: '_1255.FluxBarrierOrWeb'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.UpperFluxBarrierWebSpecification = value

    @property
    def upper_round_height(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'UpperRoundHeight' is the original name of this property."""

        temp = self.wrapped.UpperRoundHeight

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @upper_round_height.setter
    def upper_round_height(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.UpperRoundHeight = value

    @property
    def v_shaped_angle(self) -> 'float':
        """float: 'VShapedAngle' is the original name of this property."""

        temp = self.wrapped.VShapedAngle

        if temp is None:
            return 0.0

        return temp

    @v_shaped_angle.setter
    def v_shaped_angle(self, value: 'float'):
        self.wrapped.VShapedAngle = float(value) if value else 0.0

    @property
    def web_length(self) -> 'float':
        """float: 'WebLength' is the original name of this property."""

        temp = self.wrapped.WebLength

        if temp is None:
            return 0.0

        return temp

    @web_length.setter
    def web_length(self, value: 'float'):
        self.wrapped.WebLength = float(value) if value else 0.0

    @property
    def web_thickness(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'WebThickness' is the original name of this property."""

        temp = self.wrapped.WebThickness

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @web_thickness.setter
    def web_thickness(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.WebThickness = value
