"""_1258.py

InteriorPermanentMagnetAndSynchronousReluctanceRotor
"""


from typing import List

from mastapy.electric_machines import (
    _1256, _1277, _1242, _1269,
    _1288, _1289, _1271
)
from mastapy._internal import enum_with_selected_value_runtime, constructor, conversion
from mastapy._internal.python_net import python_net_import

_INTERIOR_PERMANENT_MAGNET_AND_SYNCHRONOUS_RELUCTANCE_ROTOR = python_net_import('SMT.MastaAPI.ElectricMachines', 'InteriorPermanentMagnetAndSynchronousReluctanceRotor')


__docformat__ = 'restructuredtext en'
__all__ = ('InteriorPermanentMagnetAndSynchronousReluctanceRotor',)


class InteriorPermanentMagnetAndSynchronousReluctanceRotor(_1271.PermanentMagnetRotor):
    """InteriorPermanentMagnetAndSynchronousReluctanceRotor

    This is a mastapy class.
    """

    TYPE = _INTERIOR_PERMANENT_MAGNET_AND_SYNCHRONOUS_RELUCTANCE_ROTOR

    def __init__(self, instance_to_wrap: 'InteriorPermanentMagnetAndSynchronousReluctanceRotor.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def flux_barrier_style(self) -> '_1256.FluxBarrierStyle':
        """FluxBarrierStyle: 'FluxBarrierStyle' is the original name of this property."""

        temp = self.wrapped.FluxBarrierStyle

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp)
        return constructor.new_from_mastapy_type(_1256.FluxBarrierStyle)(value) if value is not None else None

    @flux_barrier_style.setter
    def flux_barrier_style(self, value: '_1256.FluxBarrierStyle'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.FluxBarrierStyle = value

    @property
    def number_of_cooling_duct_layers(self) -> 'int':
        """int: 'NumberOfCoolingDuctLayers' is the original name of this property."""

        temp = self.wrapped.NumberOfCoolingDuctLayers

        if temp is None:
            return 0

        return temp

    @number_of_cooling_duct_layers.setter
    def number_of_cooling_duct_layers(self, value: 'int'):
        self.wrapped.NumberOfCoolingDuctLayers = int(value) if value else 0

    @property
    def number_of_magnet_flux_barrier_layers(self) -> 'int':
        """int: 'NumberOfMagnetFluxBarrierLayers' is the original name of this property."""

        temp = self.wrapped.NumberOfMagnetFluxBarrierLayers

        if temp is None:
            return 0

        return temp

    @number_of_magnet_flux_barrier_layers.setter
    def number_of_magnet_flux_barrier_layers(self, value: 'int'):
        self.wrapped.NumberOfMagnetFluxBarrierLayers = int(value) if value else 0

    @property
    def number_of_notch_specifications(self) -> 'int':
        """int: 'NumberOfNotchSpecifications' is the original name of this property."""

        temp = self.wrapped.NumberOfNotchSpecifications

        if temp is None:
            return 0

        return temp

    @number_of_notch_specifications.setter
    def number_of_notch_specifications(self, value: 'int'):
        self.wrapped.NumberOfNotchSpecifications = int(value) if value else 0

    @property
    def rotor_type(self) -> '_1277.RotorType':
        """RotorType: 'RotorType' is the original name of this property."""

        temp = self.wrapped.RotorType

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp)
        return constructor.new_from_mastapy_type(_1277.RotorType)(value) if value is not None else None

    @rotor_type.setter
    def rotor_type(self, value: '_1277.RotorType'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.RotorType = value

    @property
    def cooling_duct_layers(self) -> 'List[_1242.CoolingDuctLayerSpecification]':
        """List[CoolingDuctLayerSpecification]: 'CoolingDuctLayers' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CoolingDuctLayers

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def notch_specifications(self) -> 'List[_1269.NotchSpecification]':
        """List[NotchSpecification]: 'NotchSpecifications' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NotchSpecifications

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def u_shape_layers(self) -> 'List[_1288.UShapedLayerSpecification]':
        """List[UShapedLayerSpecification]: 'UShapeLayers' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.UShapeLayers

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def v_shape_magnet_layers(self) -> 'List[_1289.VShapedMagnetLayerSpecification]':
        """List[VShapedMagnetLayerSpecification]: 'VShapeMagnetLayers' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.VShapeMagnetLayers

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value
