"""_1571.py

MeasurementSettings
"""


from mastapy._internal import constructor, conversion
from mastapy._internal.implicit import list_with_selected_item, overridable
from mastapy.utility.units_and_measurements import _1570
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.utility.units_and_measurements.measurements import (
    _1577, _1578, _1579, _1580,
    _1581, _1582, _1583, _1584,
    _1585, _1586, _1587, _1588,
    _1589, _1590, _1591, _1592,
    _1593, _1594, _1595, _1596,
    _1597, _1598, _1599, _1600,
    _1601, _1602, _1603, _1604,
    _1605, _1606, _1607, _1608,
    _1609, _1610, _1611, _1612,
    _1613, _1614, _1615, _1616,
    _1617, _1618, _1619, _1620,
    _1621, _1622, _1623, _1624,
    _1625, _1626, _1627, _1628,
    _1629, _1630, _1631, _1632,
    _1633, _1634, _1635, _1636,
    _1637, _1638, _1639, _1640,
    _1641, _1642, _1643, _1644,
    _1645, _1646, _1647, _1648,
    _1649, _1650, _1651, _1652,
    _1653, _1654, _1655, _1656,
    _1657, _1658, _1659, _1660,
    _1661, _1662, _1663, _1664,
    _1665, _1666, _1667, _1668,
    _1669, _1670, _1671, _1672,
    _1673, _1674, _1675, _1676,
    _1677, _1678, _1679, _1680,
    _1681, _1682, _1683, _1684,
    _1685, _1686, _1687, _1688,
    _1689, _1690, _1691, _1692,
    _1693, _1694, _1695, _1696,
    _1697, _1698, _1699, _1700,
    _1701, _1702, _1703
)
from mastapy._internal.cast_exception import CastException
from mastapy.units_and_measurements import _7484
from mastapy.utility import _1559
from mastapy._internal.python_net import python_net_import

_MEASUREMENT_SETTINGS = python_net_import('SMT.MastaAPI.Utility.UnitsAndMeasurements', 'MeasurementSettings')


__docformat__ = 'restructuredtext en'
__all__ = ('MeasurementSettings',)


class MeasurementSettings(_1559.PerMachineSettings):
    """MeasurementSettings

    This is a mastapy class.
    """

    TYPE = _MEASUREMENT_SETTINGS

    def __init__(self, instance_to_wrap: 'MeasurementSettings.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def large_number_cutoff(self) -> 'float':
        """float: 'LargeNumberCutoff' is the original name of this property."""

        temp = self.wrapped.LargeNumberCutoff

        if temp is None:
            return 0.0

        return temp

    @large_number_cutoff.setter
    def large_number_cutoff(self, value: 'float'):
        self.wrapped.LargeNumberCutoff = float(value) if value else 0.0

    @property
    def number_decimal_separator(self) -> 'str':
        """str: 'NumberDecimalSeparator' is the original name of this property."""

        temp = self.wrapped.NumberDecimalSeparator

        if temp is None:
            return ''

        return temp

    @number_decimal_separator.setter
    def number_decimal_separator(self, value: 'str'):
        self.wrapped.NumberDecimalSeparator = str(value) if value else ''

    @property
    def number_group_separator(self) -> 'str':
        """str: 'NumberGroupSeparator' is the original name of this property."""

        temp = self.wrapped.NumberGroupSeparator

        if temp is None:
            return ''

        return temp

    @number_group_separator.setter
    def number_group_separator(self, value: 'str'):
        self.wrapped.NumberGroupSeparator = str(value) if value else ''

    @property
    def sample_input(self) -> 'str':
        """str: 'SampleInput' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SampleInput

        if temp is None:
            return ''

        return temp

    @property
    def sample_output(self) -> 'str':
        """str: 'SampleOutput' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SampleOutput

        if temp is None:
            return ''

        return temp

    @property
    def selected_measurement(self) -> 'list_with_selected_item.ListWithSelectedItem_MeasurementBase':
        """list_with_selected_item.ListWithSelectedItem_MeasurementBase: 'SelectedMeasurement' is the original name of this property."""

        temp = self.wrapped.SelectedMeasurement

        if temp is None:
            return None

        return constructor.new_from_mastapy_type(list_with_selected_item.ListWithSelectedItem_MeasurementBase)(temp) if temp is not None else None

    @selected_measurement.setter
    def selected_measurement(self, value: 'list_with_selected_item.ListWithSelectedItem_MeasurementBase.implicit_type()'):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_MeasurementBase.wrapper_type()
        enclosed_type = list_with_selected_item.ListWithSelectedItem_MeasurementBase.implicit_type()
        value = wrapper_type[enclosed_type](value.wrapped if value is not None else None)
        self.wrapped.SelectedMeasurement = value

    @property
    def show_trailing_zeros(self) -> 'bool':
        """bool: 'ShowTrailingZeros' is the original name of this property."""

        temp = self.wrapped.ShowTrailingZeros

        if temp is None:
            return False

        return temp

    @show_trailing_zeros.setter
    def show_trailing_zeros(self, value: 'bool'):
        self.wrapped.ShowTrailingZeros = bool(value) if value else False

    @property
    def small_number_cutoff(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'SmallNumberCutoff' is the original name of this property."""

        temp = self.wrapped.SmallNumberCutoff

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else 0.0

    @small_number_cutoff.setter
    def small_number_cutoff(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.SmallNumberCutoff = value

    @property
    def current_selected_measurement(self) -> '_1570.MeasurementBase':
        """MeasurementBase: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1570.MeasurementBase.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to MeasurementBase. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_acceleration(self) -> '_1577.Acceleration':
        """Acceleration: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1577.Acceleration.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to Acceleration. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_angle(self) -> '_1578.Angle':
        """Angle: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1578.Angle.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to Angle. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_angle_per_unit_temperature(self) -> '_1579.AnglePerUnitTemperature':
        """AnglePerUnitTemperature: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1579.AnglePerUnitTemperature.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to AnglePerUnitTemperature. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_angle_small(self) -> '_1580.AngleSmall':
        """AngleSmall: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1580.AngleSmall.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to AngleSmall. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_angle_very_small(self) -> '_1581.AngleVerySmall':
        """AngleVerySmall: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1581.AngleVerySmall.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to AngleVerySmall. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_angular_acceleration(self) -> '_1582.AngularAcceleration':
        """AngularAcceleration: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1582.AngularAcceleration.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to AngularAcceleration. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_angular_compliance(self) -> '_1583.AngularCompliance':
        """AngularCompliance: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1583.AngularCompliance.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to AngularCompliance. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_angular_jerk(self) -> '_1584.AngularJerk':
        """AngularJerk: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1584.AngularJerk.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to AngularJerk. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_angular_stiffness(self) -> '_1585.AngularStiffness':
        """AngularStiffness: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1585.AngularStiffness.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to AngularStiffness. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_angular_velocity(self) -> '_1586.AngularVelocity':
        """AngularVelocity: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1586.AngularVelocity.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to AngularVelocity. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_area(self) -> '_1587.Area':
        """Area: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1587.Area.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to Area. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_area_small(self) -> '_1588.AreaSmall':
        """AreaSmall: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1588.AreaSmall.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to AreaSmall. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_carbon_emission_factor(self) -> '_1589.CarbonEmissionFactor':
        """CarbonEmissionFactor: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1589.CarbonEmissionFactor.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to CarbonEmissionFactor. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_current_density(self) -> '_1590.CurrentDensity':
        """CurrentDensity: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1590.CurrentDensity.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to CurrentDensity. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_current_per_length(self) -> '_1591.CurrentPerLength':
        """CurrentPerLength: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1591.CurrentPerLength.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to CurrentPerLength. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_cycles(self) -> '_1592.Cycles':
        """Cycles: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1592.Cycles.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to Cycles. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_damage(self) -> '_1593.Damage':
        """Damage: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1593.Damage.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to Damage. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_damage_rate(self) -> '_1594.DamageRate':
        """DamageRate: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1594.DamageRate.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to DamageRate. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_data_size(self) -> '_1595.DataSize':
        """DataSize: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1595.DataSize.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to DataSize. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_decibel(self) -> '_1596.Decibel':
        """Decibel: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1596.Decibel.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to Decibel. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_density(self) -> '_1597.Density':
        """Density: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1597.Density.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to Density. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_electrical_resistance(self) -> '_1598.ElectricalResistance':
        """ElectricalResistance: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1598.ElectricalResistance.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to ElectricalResistance. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_electrical_resistivity(self) -> '_1599.ElectricalResistivity':
        """ElectricalResistivity: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1599.ElectricalResistivity.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to ElectricalResistivity. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_electric_current(self) -> '_1600.ElectricCurrent':
        """ElectricCurrent: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1600.ElectricCurrent.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to ElectricCurrent. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_energy(self) -> '_1601.Energy':
        """Energy: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1601.Energy.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to Energy. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_energy_per_unit_area(self) -> '_1602.EnergyPerUnitArea':
        """EnergyPerUnitArea: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1602.EnergyPerUnitArea.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to EnergyPerUnitArea. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_energy_per_unit_area_small(self) -> '_1603.EnergyPerUnitAreaSmall':
        """EnergyPerUnitAreaSmall: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1603.EnergyPerUnitAreaSmall.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to EnergyPerUnitAreaSmall. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_energy_small(self) -> '_1604.EnergySmall':
        """EnergySmall: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1604.EnergySmall.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to EnergySmall. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_enum(self) -> '_1605.Enum':
        """Enum: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1605.Enum.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to Enum. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_flow_rate(self) -> '_1606.FlowRate':
        """FlowRate: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1606.FlowRate.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to FlowRate. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_force(self) -> '_1607.Force':
        """Force: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1607.Force.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to Force. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_force_per_unit_length(self) -> '_1608.ForcePerUnitLength':
        """ForcePerUnitLength: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1608.ForcePerUnitLength.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to ForcePerUnitLength. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_force_per_unit_pressure(self) -> '_1609.ForcePerUnitPressure':
        """ForcePerUnitPressure: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1609.ForcePerUnitPressure.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to ForcePerUnitPressure. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_force_per_unit_temperature(self) -> '_1610.ForcePerUnitTemperature':
        """ForcePerUnitTemperature: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1610.ForcePerUnitTemperature.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to ForcePerUnitTemperature. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_fraction_measurement_base(self) -> '_1611.FractionMeasurementBase':
        """FractionMeasurementBase: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1611.FractionMeasurementBase.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to FractionMeasurementBase. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_fraction_per_temperature(self) -> '_1612.FractionPerTemperature':
        """FractionPerTemperature: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1612.FractionPerTemperature.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to FractionPerTemperature. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_frequency(self) -> '_1613.Frequency':
        """Frequency: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1613.Frequency.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to Frequency. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_fuel_consumption_engine(self) -> '_1614.FuelConsumptionEngine':
        """FuelConsumptionEngine: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1614.FuelConsumptionEngine.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to FuelConsumptionEngine. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_fuel_efficiency_vehicle(self) -> '_1615.FuelEfficiencyVehicle':
        """FuelEfficiencyVehicle: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1615.FuelEfficiencyVehicle.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to FuelEfficiencyVehicle. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_gradient(self) -> '_1616.Gradient':
        """Gradient: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1616.Gradient.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to Gradient. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_heat_conductivity(self) -> '_1617.HeatConductivity':
        """HeatConductivity: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1617.HeatConductivity.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to HeatConductivity. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_heat_transfer(self) -> '_1618.HeatTransfer':
        """HeatTransfer: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1618.HeatTransfer.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to HeatTransfer. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_heat_transfer_coefficient_for_plastic_gear_tooth(self) -> '_1619.HeatTransferCoefficientForPlasticGearTooth':
        """HeatTransferCoefficientForPlasticGearTooth: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1619.HeatTransferCoefficientForPlasticGearTooth.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to HeatTransferCoefficientForPlasticGearTooth. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_heat_transfer_resistance(self) -> '_1620.HeatTransferResistance':
        """HeatTransferResistance: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1620.HeatTransferResistance.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to HeatTransferResistance. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_impulse(self) -> '_1621.Impulse':
        """Impulse: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1621.Impulse.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to Impulse. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_index(self) -> '_1622.Index':
        """Index: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1622.Index.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to Index. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_inductance(self) -> '_1623.Inductance':
        """Inductance: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1623.Inductance.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to Inductance. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_integer(self) -> '_1624.Integer':
        """Integer: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1624.Integer.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to Integer. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_inverse_short_length(self) -> '_1625.InverseShortLength':
        """InverseShortLength: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1625.InverseShortLength.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to InverseShortLength. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_inverse_short_time(self) -> '_1626.InverseShortTime':
        """InverseShortTime: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1626.InverseShortTime.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to InverseShortTime. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_jerk(self) -> '_1627.Jerk':
        """Jerk: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1627.Jerk.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to Jerk. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_kinematic_viscosity(self) -> '_1628.KinematicViscosity':
        """KinematicViscosity: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1628.KinematicViscosity.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to KinematicViscosity. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_length_long(self) -> '_1629.LengthLong':
        """LengthLong: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1629.LengthLong.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to LengthLong. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_length_medium(self) -> '_1630.LengthMedium':
        """LengthMedium: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1630.LengthMedium.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to LengthMedium. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_length_per_unit_temperature(self) -> '_1631.LengthPerUnitTemperature':
        """LengthPerUnitTemperature: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1631.LengthPerUnitTemperature.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to LengthPerUnitTemperature. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_length_short(self) -> '_1632.LengthShort':
        """LengthShort: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1632.LengthShort.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to LengthShort. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_length_to_the_fourth(self) -> '_1633.LengthToTheFourth':
        """LengthToTheFourth: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1633.LengthToTheFourth.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to LengthToTheFourth. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_length_very_long(self) -> '_1634.LengthVeryLong':
        """LengthVeryLong: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1634.LengthVeryLong.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to LengthVeryLong. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_length_very_short(self) -> '_1635.LengthVeryShort':
        """LengthVeryShort: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1635.LengthVeryShort.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to LengthVeryShort. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_length_very_short_per_length_short(self) -> '_1636.LengthVeryShortPerLengthShort':
        """LengthVeryShortPerLengthShort: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1636.LengthVeryShortPerLengthShort.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to LengthVeryShortPerLengthShort. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_linear_angular_damping(self) -> '_1637.LinearAngularDamping':
        """LinearAngularDamping: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1637.LinearAngularDamping.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to LinearAngularDamping. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_linear_angular_stiffness_cross_term(self) -> '_1638.LinearAngularStiffnessCrossTerm':
        """LinearAngularStiffnessCrossTerm: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1638.LinearAngularStiffnessCrossTerm.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to LinearAngularStiffnessCrossTerm. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_linear_damping(self) -> '_1639.LinearDamping':
        """LinearDamping: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1639.LinearDamping.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to LinearDamping. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_linear_flexibility(self) -> '_1640.LinearFlexibility':
        """LinearFlexibility: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1640.LinearFlexibility.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to LinearFlexibility. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_linear_stiffness(self) -> '_1641.LinearStiffness':
        """LinearStiffness: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1641.LinearStiffness.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to LinearStiffness. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_magnetic_field_strength(self) -> '_1642.MagneticFieldStrength':
        """MagneticFieldStrength: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1642.MagneticFieldStrength.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to MagneticFieldStrength. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_magnetic_flux(self) -> '_1643.MagneticFlux':
        """MagneticFlux: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1643.MagneticFlux.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to MagneticFlux. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_magnetic_flux_density(self) -> '_1644.MagneticFluxDensity':
        """MagneticFluxDensity: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1644.MagneticFluxDensity.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to MagneticFluxDensity. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_magnetic_vector_potential(self) -> '_1645.MagneticVectorPotential':
        """MagneticVectorPotential: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1645.MagneticVectorPotential.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to MagneticVectorPotential. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_magnetomotive_force(self) -> '_1646.MagnetomotiveForce':
        """MagnetomotiveForce: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1646.MagnetomotiveForce.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to MagnetomotiveForce. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_mass(self) -> '_1647.Mass':
        """Mass: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1647.Mass.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to Mass. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_mass_per_unit_length(self) -> '_1648.MassPerUnitLength':
        """MassPerUnitLength: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1648.MassPerUnitLength.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to MassPerUnitLength. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_mass_per_unit_time(self) -> '_1649.MassPerUnitTime':
        """MassPerUnitTime: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1649.MassPerUnitTime.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to MassPerUnitTime. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_moment_of_inertia(self) -> '_1650.MomentOfInertia':
        """MomentOfInertia: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1650.MomentOfInertia.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to MomentOfInertia. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_moment_of_inertia_per_unit_length(self) -> '_1651.MomentOfInertiaPerUnitLength':
        """MomentOfInertiaPerUnitLength: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1651.MomentOfInertiaPerUnitLength.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to MomentOfInertiaPerUnitLength. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_moment_per_unit_pressure(self) -> '_1652.MomentPerUnitPressure':
        """MomentPerUnitPressure: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1652.MomentPerUnitPressure.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to MomentPerUnitPressure. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_number(self) -> '_1653.Number':
        """Number: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1653.Number.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to Number. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_percentage(self) -> '_1654.Percentage':
        """Percentage: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1654.Percentage.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to Percentage. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_power(self) -> '_1655.Power':
        """Power: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1655.Power.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to Power. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_power_per_small_area(self) -> '_1656.PowerPerSmallArea':
        """PowerPerSmallArea: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1656.PowerPerSmallArea.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to PowerPerSmallArea. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_power_per_unit_time(self) -> '_1657.PowerPerUnitTime':
        """PowerPerUnitTime: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1657.PowerPerUnitTime.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to PowerPerUnitTime. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_power_small(self) -> '_1658.PowerSmall':
        """PowerSmall: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1658.PowerSmall.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to PowerSmall. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_power_small_per_area(self) -> '_1659.PowerSmallPerArea':
        """PowerSmallPerArea: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1659.PowerSmallPerArea.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to PowerSmallPerArea. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_power_small_per_mass(self) -> '_1660.PowerSmallPerMass':
        """PowerSmallPerMass: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1660.PowerSmallPerMass.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to PowerSmallPerMass. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_power_small_per_unit_area_per_unit_time(self) -> '_1661.PowerSmallPerUnitAreaPerUnitTime':
        """PowerSmallPerUnitAreaPerUnitTime: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1661.PowerSmallPerUnitAreaPerUnitTime.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to PowerSmallPerUnitAreaPerUnitTime. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_power_small_per_unit_time(self) -> '_1662.PowerSmallPerUnitTime':
        """PowerSmallPerUnitTime: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1662.PowerSmallPerUnitTime.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to PowerSmallPerUnitTime. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_power_small_per_volume(self) -> '_1663.PowerSmallPerVolume':
        """PowerSmallPerVolume: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1663.PowerSmallPerVolume.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to PowerSmallPerVolume. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_pressure(self) -> '_1664.Pressure':
        """Pressure: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1664.Pressure.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to Pressure. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_pressure_per_unit_time(self) -> '_1665.PressurePerUnitTime':
        """PressurePerUnitTime: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1665.PressurePerUnitTime.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to PressurePerUnitTime. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_pressure_velocity_product(self) -> '_1666.PressureVelocityProduct':
        """PressureVelocityProduct: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1666.PressureVelocityProduct.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to PressureVelocityProduct. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_pressure_viscosity_coefficient(self) -> '_1667.PressureViscosityCoefficient':
        """PressureViscosityCoefficient: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1667.PressureViscosityCoefficient.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to PressureViscosityCoefficient. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_price(self) -> '_1668.Price':
        """Price: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1668.Price.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to Price. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_price_per_unit_mass(self) -> '_1669.PricePerUnitMass':
        """PricePerUnitMass: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1669.PricePerUnitMass.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to PricePerUnitMass. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_quadratic_angular_damping(self) -> '_1670.QuadraticAngularDamping':
        """QuadraticAngularDamping: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1670.QuadraticAngularDamping.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to QuadraticAngularDamping. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_quadratic_drag(self) -> '_1671.QuadraticDrag':
        """QuadraticDrag: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1671.QuadraticDrag.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to QuadraticDrag. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_rescaled_measurement(self) -> '_1672.RescaledMeasurement':
        """RescaledMeasurement: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1672.RescaledMeasurement.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to RescaledMeasurement. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_rotatum(self) -> '_1673.Rotatum':
        """Rotatum: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1673.Rotatum.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to Rotatum. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_safety_factor(self) -> '_1674.SafetyFactor':
        """SafetyFactor: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1674.SafetyFactor.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to SafetyFactor. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_specific_acoustic_impedance(self) -> '_1675.SpecificAcousticImpedance':
        """SpecificAcousticImpedance: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1675.SpecificAcousticImpedance.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to SpecificAcousticImpedance. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_specific_heat(self) -> '_1676.SpecificHeat':
        """SpecificHeat: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1676.SpecificHeat.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to SpecificHeat. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_square_root_of_unit_force_per_unit_area(self) -> '_1677.SquareRootOfUnitForcePerUnitArea':
        """SquareRootOfUnitForcePerUnitArea: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1677.SquareRootOfUnitForcePerUnitArea.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to SquareRootOfUnitForcePerUnitArea. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_stiffness_per_unit_face_width(self) -> '_1678.StiffnessPerUnitFaceWidth':
        """StiffnessPerUnitFaceWidth: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1678.StiffnessPerUnitFaceWidth.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to StiffnessPerUnitFaceWidth. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_stress(self) -> '_1679.Stress':
        """Stress: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1679.Stress.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to Stress. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_temperature(self) -> '_1680.Temperature':
        """Temperature: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1680.Temperature.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to Temperature. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_temperature_difference(self) -> '_1681.TemperatureDifference':
        """TemperatureDifference: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1681.TemperatureDifference.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to TemperatureDifference. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_temperature_per_unit_time(self) -> '_1682.TemperaturePerUnitTime':
        """TemperaturePerUnitTime: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1682.TemperaturePerUnitTime.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to TemperaturePerUnitTime. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_text(self) -> '_1683.Text':
        """Text: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1683.Text.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to Text. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_thermal_contact_coefficient(self) -> '_1684.ThermalContactCoefficient':
        """ThermalContactCoefficient: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1684.ThermalContactCoefficient.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to ThermalContactCoefficient. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_thermal_expansion_coefficient(self) -> '_1685.ThermalExpansionCoefficient':
        """ThermalExpansionCoefficient: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1685.ThermalExpansionCoefficient.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to ThermalExpansionCoefficient. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_thermo_elastic_factor(self) -> '_1686.ThermoElasticFactor':
        """ThermoElasticFactor: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1686.ThermoElasticFactor.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to ThermoElasticFactor. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_time(self) -> '_1687.Time':
        """Time: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1687.Time.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to Time. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_time_short(self) -> '_1688.TimeShort':
        """TimeShort: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1688.TimeShort.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to TimeShort. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_time_very_short(self) -> '_1689.TimeVeryShort':
        """TimeVeryShort: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1689.TimeVeryShort.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to TimeVeryShort. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_torque(self) -> '_1690.Torque':
        """Torque: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1690.Torque.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to Torque. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_torque_converter_inverse_k(self) -> '_1691.TorqueConverterInverseK':
        """TorqueConverterInverseK: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1691.TorqueConverterInverseK.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to TorqueConverterInverseK. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_torque_converter_k(self) -> '_1692.TorqueConverterK':
        """TorqueConverterK: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1692.TorqueConverterK.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to TorqueConverterK. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_torque_per_current(self) -> '_1693.TorquePerCurrent':
        """TorquePerCurrent: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1693.TorquePerCurrent.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to TorquePerCurrent. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_torque_per_square_root_of_power(self) -> '_1694.TorquePerSquareRootOfPower':
        """TorquePerSquareRootOfPower: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1694.TorquePerSquareRootOfPower.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to TorquePerSquareRootOfPower. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_torque_per_unit_temperature(self) -> '_1695.TorquePerUnitTemperature':
        """TorquePerUnitTemperature: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1695.TorquePerUnitTemperature.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to TorquePerUnitTemperature. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_velocity(self) -> '_1696.Velocity':
        """Velocity: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1696.Velocity.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to Velocity. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_velocity_small(self) -> '_1697.VelocitySmall':
        """VelocitySmall: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1697.VelocitySmall.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to VelocitySmall. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_viscosity(self) -> '_1698.Viscosity':
        """Viscosity: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1698.Viscosity.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to Viscosity. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_voltage(self) -> '_1699.Voltage':
        """Voltage: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1699.Voltage.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to Voltage. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_voltage_per_angular_velocity(self) -> '_1700.VoltagePerAngularVelocity':
        """VoltagePerAngularVelocity: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1700.VoltagePerAngularVelocity.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to VoltagePerAngularVelocity. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_volume(self) -> '_1701.Volume':
        """Volume: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1701.Volume.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to Volume. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_wear_coefficient(self) -> '_1702.WearCoefficient':
        """WearCoefficient: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1702.WearCoefficient.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to WearCoefficient. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_yank(self) -> '_1703.Yank':
        """Yank: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement

        if temp is None:
            return None

        if _1703.Yank.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to Yank. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    def default_to_imperial(self):
        """ 'DefaultToImperial' is the original name of this method."""

        self.wrapped.DefaultToImperial()

    def default_to_metric(self):
        """ 'DefaultToMetric' is the original name of this method."""

        self.wrapped.DefaultToMetric()

    def find_measurement_by_name(self, name: 'str') -> '_1570.MeasurementBase':
        """ 'FindMeasurementByName' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.utility.units_and_measurements.MeasurementBase
        """

        name = str(name)
        method_result = self.wrapped.FindMeasurementByName(name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def get_measurement(self, measurement_type: '_7484.MeasurementType') -> '_1570.MeasurementBase':
        """ 'GetMeasurement' is the original name of this method.

        Args:
            measurement_type (mastapy.units_and_measurements.MeasurementType)

        Returns:
            mastapy.utility.units_and_measurements.MeasurementBase
        """

        measurement_type = conversion.mp_to_pn_enum(measurement_type)
        method_result = self.wrapped.GetMeasurement(measurement_type)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None
