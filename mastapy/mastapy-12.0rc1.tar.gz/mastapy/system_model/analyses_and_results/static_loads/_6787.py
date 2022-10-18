"""_6787.py

CylindricalGearLoadCase
"""


from typing import List

from mastapy._internal import constructor, conversion
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.system_model.part_model.gears import _2476, _2478
from mastapy._internal.cast_exception import CastException
from mastapy.system_model.analyses_and_results.static_loads import _6788, _6816
from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1093, _1092, _1096
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'CylindricalGearLoadCase')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearLoadCase',)


class CylindricalGearLoadCase(_6816.GearLoadCase):
    """CylindricalGearLoadCase

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_LOAD_CASE

    def __init__(self, instance_to_wrap: 'CylindricalGearLoadCase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def axial_reaction_force(self) -> 'float':
        """float: 'AxialReactionForce' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AxialReactionForce

        if temp is None:
            return 0.0

        return temp

    @property
    def lateral_reaction_force(self) -> 'float':
        """float: 'LateralReactionForce' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LateralReactionForce

        if temp is None:
            return 0.0

        return temp

    @property
    def lateral_reaction_moment(self) -> 'float':
        """float: 'LateralReactionMoment' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LateralReactionMoment

        if temp is None:
            return 0.0

        return temp

    @property
    def override_micro_geometry(self) -> 'bool':
        """bool: 'OverrideMicroGeometry' is the original name of this property."""

        temp = self.wrapped.OverrideMicroGeometry

        if temp is None:
            return False

        return temp

    @override_micro_geometry.setter
    def override_micro_geometry(self, value: 'bool'):
        self.wrapped.OverrideMicroGeometry = bool(value) if value else False

    @property
    def power(self) -> 'float':
        """float: 'Power' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Power

        if temp is None:
            return 0.0

        return temp

    @property
    def reversed_bending_factor(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'ReversedBendingFactor' is the original name of this property."""

        temp = self.wrapped.ReversedBendingFactor

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @reversed_bending_factor.setter
    def reversed_bending_factor(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.ReversedBendingFactor = value

    @property
    def speed(self) -> 'float':
        """float: 'Speed' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Speed

        if temp is None:
            return 0.0

        return temp

    @property
    def torque(self) -> 'float':
        """float: 'Torque' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Torque

        if temp is None:
            return 0.0

        return temp

    @property
    def vertical_reaction_force(self) -> 'float':
        """float: 'VerticalReactionForce' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.VerticalReactionForce

        if temp is None:
            return 0.0

        return temp

    @property
    def vertical_reaction_moment(self) -> 'float':
        """float: 'VerticalReactionMoment' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.VerticalReactionMoment

        if temp is None:
            return 0.0

        return temp

    @property
    def component_design(self) -> '_2476.CylindricalGear':
        """CylindricalGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        if _2476.CylindricalGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to CylindricalGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_manufacture_errors(self) -> '_6788.CylindricalGearManufactureError':
        """CylindricalGearManufactureError: 'GearManufactureErrors' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearManufactureErrors

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def overridden_micro_geometry(self) -> '_1093.CylindricalGearMicroGeometryBase':
        """CylindricalGearMicroGeometryBase: 'OverriddenMicroGeometry' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OverriddenMicroGeometry

        if temp is None:
            return None

        if _1093.CylindricalGearMicroGeometryBase.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast overridden_micro_geometry to CylindricalGearMicroGeometryBase. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def overridden_micro_geometry_of_type_cylindrical_gear_micro_geometry(self) -> '_1092.CylindricalGearMicroGeometry':
        """CylindricalGearMicroGeometry: 'OverriddenMicroGeometry' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OverriddenMicroGeometry

        if temp is None:
            return None

        if _1092.CylindricalGearMicroGeometry.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast overridden_micro_geometry to CylindricalGearMicroGeometry. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def overridden_micro_geometry_of_type_cylindrical_gear_micro_geometry_per_tooth(self) -> '_1096.CylindricalGearMicroGeometryPerTooth':
        """CylindricalGearMicroGeometryPerTooth: 'OverriddenMicroGeometry' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OverriddenMicroGeometry

        if temp is None:
            return None

        if _1096.CylindricalGearMicroGeometryPerTooth.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast overridden_micro_geometry to CylindricalGearMicroGeometryPerTooth. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def planetaries(self) -> 'List[CylindricalGearLoadCase]':
        """List[CylindricalGearLoadCase]: 'Planetaries' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value
