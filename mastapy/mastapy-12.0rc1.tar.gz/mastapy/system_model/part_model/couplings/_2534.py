"""_2534.py

Coupling
"""


from typing import List

from mastapy._internal import constructor, conversion
from mastapy.system_model.part_model.couplings import (
    _2535, _2530, _2533, _2538,
    _2540, _2541, _2547, _2552,
    _2555, _2556, _2557, _2559,
    _2561
)
from mastapy._internal.cast_exception import CastException
from mastapy.system_model.part_model import _2428
from mastapy._internal.python_net import python_net_import

_COUPLING = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Couplings', 'Coupling')


__docformat__ = 'restructuredtext en'
__all__ = ('Coupling',)


class Coupling(_2428.SpecialisedAssembly):
    """Coupling

    This is a mastapy class.
    """

    TYPE = _COUPLING

    def __init__(self, instance_to_wrap: 'Coupling.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def axial_stiffness(self) -> 'float':
        """float: 'AxialStiffness' is the original name of this property."""

        temp = self.wrapped.AxialStiffness

        if temp is None:
            return 0.0

        return temp

    @axial_stiffness.setter
    def axial_stiffness(self, value: 'float'):
        self.wrapped.AxialStiffness = float(value) if value else 0.0

    @property
    def radial_stiffness(self) -> 'float':
        """float: 'RadialStiffness' is the original name of this property."""

        temp = self.wrapped.RadialStiffness

        if temp is None:
            return 0.0

        return temp

    @radial_stiffness.setter
    def radial_stiffness(self, value: 'float'):
        self.wrapped.RadialStiffness = float(value) if value else 0.0

    @property
    def tilt_stiffness(self) -> 'float':
        """float: 'TiltStiffness' is the original name of this property."""

        temp = self.wrapped.TiltStiffness

        if temp is None:
            return 0.0

        return temp

    @tilt_stiffness.setter
    def tilt_stiffness(self, value: 'float'):
        self.wrapped.TiltStiffness = float(value) if value else 0.0

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
    def halves(self) -> 'List[_2535.CouplingHalf]':
        """List[CouplingHalf]: 'Halves' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Halves

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def half_a(self) -> '_2535.CouplingHalf':
        """CouplingHalf: 'HalfA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HalfA

        if temp is None:
            return None

        if _2535.CouplingHalf.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast half_a to CouplingHalf. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def half_a_of_type_clutch_half(self) -> '_2530.ClutchHalf':
        """ClutchHalf: 'HalfA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HalfA

        if temp is None:
            return None

        if _2530.ClutchHalf.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast half_a to ClutchHalf. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def half_a_of_type_concept_coupling_half(self) -> '_2533.ConceptCouplingHalf':
        """ConceptCouplingHalf: 'HalfA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HalfA

        if temp is None:
            return None

        if _2533.ConceptCouplingHalf.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast half_a to ConceptCouplingHalf. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def half_a_of_type_cvt_pulley(self) -> '_2538.CVTPulley':
        """CVTPulley: 'HalfA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HalfA

        if temp is None:
            return None

        if _2538.CVTPulley.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast half_a to CVTPulley. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def half_a_of_type_part_to_part_shear_coupling_half(self) -> '_2540.PartToPartShearCouplingHalf':
        """PartToPartShearCouplingHalf: 'HalfA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HalfA

        if temp is None:
            return None

        if _2540.PartToPartShearCouplingHalf.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast half_a to PartToPartShearCouplingHalf. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def half_a_of_type_pulley(self) -> '_2541.Pulley':
        """Pulley: 'HalfA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HalfA

        if temp is None:
            return None

        if _2541.Pulley.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast half_a to Pulley. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def half_a_of_type_rolling_ring(self) -> '_2547.RollingRing':
        """RollingRing: 'HalfA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HalfA

        if temp is None:
            return None

        if _2547.RollingRing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast half_a to RollingRing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def half_a_of_type_spring_damper_half(self) -> '_2552.SpringDamperHalf':
        """SpringDamperHalf: 'HalfA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HalfA

        if temp is None:
            return None

        if _2552.SpringDamperHalf.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast half_a to SpringDamperHalf. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def half_a_of_type_synchroniser_half(self) -> '_2555.SynchroniserHalf':
        """SynchroniserHalf: 'HalfA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HalfA

        if temp is None:
            return None

        if _2555.SynchroniserHalf.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast half_a to SynchroniserHalf. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def half_a_of_type_synchroniser_part(self) -> '_2556.SynchroniserPart':
        """SynchroniserPart: 'HalfA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HalfA

        if temp is None:
            return None

        if _2556.SynchroniserPart.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast half_a to SynchroniserPart. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def half_a_of_type_synchroniser_sleeve(self) -> '_2557.SynchroniserSleeve':
        """SynchroniserSleeve: 'HalfA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HalfA

        if temp is None:
            return None

        if _2557.SynchroniserSleeve.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast half_a to SynchroniserSleeve. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def half_a_of_type_torque_converter_pump(self) -> '_2559.TorqueConverterPump':
        """TorqueConverterPump: 'HalfA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HalfA

        if temp is None:
            return None

        if _2559.TorqueConverterPump.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast half_a to TorqueConverterPump. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def half_a_of_type_torque_converter_turbine(self) -> '_2561.TorqueConverterTurbine':
        """TorqueConverterTurbine: 'HalfA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HalfA

        if temp is None:
            return None

        if _2561.TorqueConverterTurbine.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast half_a to TorqueConverterTurbine. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def half_b(self) -> '_2535.CouplingHalf':
        """CouplingHalf: 'HalfB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HalfB

        if temp is None:
            return None

        if _2535.CouplingHalf.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast half_b to CouplingHalf. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def half_b_of_type_clutch_half(self) -> '_2530.ClutchHalf':
        """ClutchHalf: 'HalfB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HalfB

        if temp is None:
            return None

        if _2530.ClutchHalf.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast half_b to ClutchHalf. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def half_b_of_type_concept_coupling_half(self) -> '_2533.ConceptCouplingHalf':
        """ConceptCouplingHalf: 'HalfB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HalfB

        if temp is None:
            return None

        if _2533.ConceptCouplingHalf.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast half_b to ConceptCouplingHalf. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def half_b_of_type_cvt_pulley(self) -> '_2538.CVTPulley':
        """CVTPulley: 'HalfB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HalfB

        if temp is None:
            return None

        if _2538.CVTPulley.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast half_b to CVTPulley. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def half_b_of_type_part_to_part_shear_coupling_half(self) -> '_2540.PartToPartShearCouplingHalf':
        """PartToPartShearCouplingHalf: 'HalfB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HalfB

        if temp is None:
            return None

        if _2540.PartToPartShearCouplingHalf.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast half_b to PartToPartShearCouplingHalf. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def half_b_of_type_pulley(self) -> '_2541.Pulley':
        """Pulley: 'HalfB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HalfB

        if temp is None:
            return None

        if _2541.Pulley.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast half_b to Pulley. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def half_b_of_type_rolling_ring(self) -> '_2547.RollingRing':
        """RollingRing: 'HalfB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HalfB

        if temp is None:
            return None

        if _2547.RollingRing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast half_b to RollingRing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def half_b_of_type_spring_damper_half(self) -> '_2552.SpringDamperHalf':
        """SpringDamperHalf: 'HalfB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HalfB

        if temp is None:
            return None

        if _2552.SpringDamperHalf.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast half_b to SpringDamperHalf. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def half_b_of_type_synchroniser_half(self) -> '_2555.SynchroniserHalf':
        """SynchroniserHalf: 'HalfB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HalfB

        if temp is None:
            return None

        if _2555.SynchroniserHalf.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast half_b to SynchroniserHalf. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def half_b_of_type_synchroniser_part(self) -> '_2556.SynchroniserPart':
        """SynchroniserPart: 'HalfB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HalfB

        if temp is None:
            return None

        if _2556.SynchroniserPart.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast half_b to SynchroniserPart. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def half_b_of_type_synchroniser_sleeve(self) -> '_2557.SynchroniserSleeve':
        """SynchroniserSleeve: 'HalfB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HalfB

        if temp is None:
            return None

        if _2557.SynchroniserSleeve.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast half_b to SynchroniserSleeve. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def half_b_of_type_torque_converter_pump(self) -> '_2559.TorqueConverterPump':
        """TorqueConverterPump: 'HalfB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HalfB

        if temp is None:
            return None

        if _2559.TorqueConverterPump.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast half_b to TorqueConverterPump. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def half_b_of_type_torque_converter_turbine(self) -> '_2561.TorqueConverterTurbine':
        """TorqueConverterTurbine: 'HalfB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HalfB

        if temp is None:
            return None

        if _2561.TorqueConverterTurbine.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast half_b to TorqueConverterTurbine. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None
