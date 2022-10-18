"""_2261.py

CylindricalGearMesh
"""


from typing import List

from mastapy._internal import constructor, conversion
from mastapy.math_utility.measured_ranges import _1529
from mastapy.gears.gear_designs.cylindrical import _1011
from mastapy.system_model.part_model.gears import _2477, _2493, _2476
from mastapy._internal.cast_exception import CastException
from mastapy.system_model.connections_and_sockets.gears import _2265
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_MESH = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears', 'CylindricalGearMesh')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearMesh',)


class CylindricalGearMesh(_2265.GearMesh):
    """CylindricalGearMesh

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_MESH

    def __init__(self, instance_to_wrap: 'CylindricalGearMesh.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def centre_distance_with_normal_module_adjustment_by_scaling_entire_model(self) -> 'float':
        """float: 'CentreDistanceWithNormalModuleAdjustmentByScalingEntireModel' is the original name of this property."""

        temp = self.wrapped.CentreDistanceWithNormalModuleAdjustmentByScalingEntireModel

        if temp is None:
            return 0.0

        return temp

    @centre_distance_with_normal_module_adjustment_by_scaling_entire_model.setter
    def centre_distance_with_normal_module_adjustment_by_scaling_entire_model(self, value: 'float'):
        self.wrapped.CentreDistanceWithNormalModuleAdjustmentByScalingEntireModel = float(value) if value else 0.0

    @property
    def is_centre_distance_ready_to_change(self) -> 'bool':
        """bool: 'IsCentreDistanceReadyToChange' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.IsCentreDistanceReadyToChange

        if temp is None:
            return False

        return temp

    @property
    def centre_distance_range(self) -> '_1529.ShortLengthRange':
        """ShortLengthRange: 'CentreDistanceRange' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CentreDistanceRange

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def active_gear_mesh_design(self) -> '_1011.CylindricalGearMeshDesign':
        """CylindricalGearMeshDesign: 'ActiveGearMeshDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ActiveGearMeshDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cylindrical_gear_mesh_design(self) -> '_1011.CylindricalGearMeshDesign':
        """CylindricalGearMeshDesign: 'CylindricalGearMeshDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CylindricalGearMeshDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cylindrical_gear_set(self) -> '_2477.CylindricalGearSet':
        """CylindricalGearSet: 'CylindricalGearSet' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CylindricalGearSet

        if temp is None:
            return None

        if _2477.CylindricalGearSet.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast cylindrical_gear_set to CylindricalGearSet. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cylindrical_gears(self) -> 'List[_2476.CylindricalGear]':
        """List[CylindricalGear]: 'CylindricalGears' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CylindricalGears

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value
