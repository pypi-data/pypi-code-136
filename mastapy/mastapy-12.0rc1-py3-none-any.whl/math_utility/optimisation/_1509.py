"""_1509.py

OptimizationVariable
"""


from typing import List

from mastapy.utility.units_and_measurements import _1570
from mastapy._internal import constructor, conversion
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
from mastapy import _0
from mastapy._internal.python_net import python_net_import

_OPTIMIZATION_VARIABLE = python_net_import('SMT.MastaAPI.MathUtility.Optimisation', 'OptimizationVariable')


__docformat__ = 'restructuredtext en'
__all__ = ('OptimizationVariable',)


class OptimizationVariable(_0.APIBase):
    """OptimizationVariable

    This is a mastapy class.
    """

    TYPE = _OPTIMIZATION_VARIABLE

    def __init__(self, instance_to_wrap: 'OptimizationVariable.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def measurement(self) -> '_1570.MeasurementBase':
        """MeasurementBase: 'Measurement' is the original name of this property."""

        temp = self.wrapped.Measurement

        if temp is None:
            return None

        if _1570.MeasurementBase.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast measurement to MeasurementBase. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @measurement.setter
    def measurement(self, value: '_1570.MeasurementBase'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_acceleration(self) -> '_1577.Acceleration':
        """Acceleration: 'Measurement' is the original name of this property."""

        temp = self.wrapped.Measurement

        if temp is None:
            return None

        if _1577.Acceleration.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast measurement to Acceleration. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @measurement_of_type_acceleration.setter
    def measurement_of_type_acceleration(self, value: '_1577.Acceleration'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_angle(self) -> '_1578.Angle':
        """Angle: 'Measurement' is the original name of this property."""

        temp = self.wrapped.Measurement

        if temp is None:
            return None

        if _1578.Angle.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast measurement to Angle. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @measurement_of_type_angle.setter
    def measurement_of_type_angle(self, value: '_1578.Angle'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_angle_per_unit_temperature(self) -> '_1579.AnglePerUnitTemperature':
        """AnglePerUnitTemperature: 'Measurement' is the original name of this property."""

        temp = self.wrapped.Measurement

        if temp is None:
            return None

        if _1579.AnglePerUnitTemperature.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast measurement to AnglePerUnitTemperature. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @measurement_of_type_angle_per_unit_temperature.setter
    def measurement_of_type_angle_per_unit_temperature(self, value: '_1579.AnglePerUnitTemperature'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_angle_small(self) -> '_1580.AngleSmall':
        """AngleSmall: 'Measurement' is the original name of this property."""

        temp = self.wrapped.Measurement

        if temp is None:
            return None

        if _1580.AngleSmall.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast measurement to AngleSmall. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @measurement_of_type_angle_small.setter
    def measurement_of_type_angle_small(self, value: '_1580.AngleSmall'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_angle_very_small(self) -> '_1581.AngleVerySmall':
        """AngleVerySmall: 'Measurement' is the original name of this property."""

        temp = self.wrapped.Measurement

        if temp is None:
            return None

        if _1581.AngleVerySmall.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast measurement to AngleVerySmall. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @measurement_of_type_angle_very_small.setter
    def measurement_of_type_angle_very_small(self, value: '_1581.AngleVerySmall'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_angular_acceleration(self) -> '_1582.AngularAcceleration':
        """AngularAcceleration: 'Measurement' is the original name of this property."""

        temp = self.wrapped.Measurement

        if temp is None:
            return None

        if _1582.AngularAcceleration.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast measurement to AngularAcceleration. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @measurement_of_type_angular_acceleration.setter
    def measurement_of_type_angular_acceleration(self, value: '_1582.AngularAcceleration'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_angular_compliance(self) -> '_1583.AngularCompliance':
        """AngularCompliance: 'Measurement' is the original name of this property."""

        temp = self.wrapped.Measurement

        if temp is None:
            return None

        if _1583.AngularCompliance.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast measurement to AngularCompliance. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @measurement_of_type_angular_compliance.setter
    def measurement_of_type_angular_compliance(self, value: '_1583.AngularCompliance'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_angular_jerk(self) -> '_1584.AngularJerk':
        """AngularJerk: 'Measurement' is the original name of this property."""

        temp = self.wrapped.Measurement

        if temp is None:
            return None

        if _1584.AngularJerk.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast measurement to AngularJerk. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @measurement_of_type_angular_jerk.setter
    def measurement_of_type_angular_jerk(self, value: '_1584.AngularJerk'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_angular_stiffness(self) -> '_1585.AngularStiffness':
        """AngularStiffness: 'Measurement' is the original name of this property."""

        temp = self.wrapped.Measurement

        if temp is None:
            return None

        if _1585.AngularStiffness.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast measurement to AngularStiffness. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @measurement_of_type_angular_stiffness.setter
    def measurement_of_type_angular_stiffness(self, value: '_1585.AngularStiffness'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_angular_velocity(self) -> '_1586.AngularVelocity':
        """AngularVelocity: 'Measurement' is the original name of this property."""

        temp = self.wrapped.Measurement

        if temp is None:
            return None

        if _1586.AngularVelocity.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast measurement to AngularVelocity. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @measurement_of_type_angular_velocity.setter
    def measurement_of_type_angular_velocity(self, value: '_1586.AngularVelocity'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_area(self) -> '_1587.Area':
        """Area: 'Measurement' is the original name of this property."""

        temp = self.wrapped.Measurement

        if temp is None:
            return None

        if _1587.Area.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast measurement to Area. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @measurement_of_type_area.setter
    def measurement_of_type_area(self, value: '_1587.Area'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_area_small(self) -> '_1588.AreaSmall':
        """AreaSmall: 'Measurement' is the original name of this property."""

        temp = self.wrapped.Measurement

        if temp is None:
            return None

        if _1588.AreaSmall.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast measurement to AreaSmall. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @measurement_of_type_area_small.setter
    def measurement_of_type_area_small(self, value: '_1588.AreaSmall'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_carbon_emission_factor(self) -> '_1589.CarbonEmissionFactor':
        """CarbonEmissionFactor: 'Measurement' is the original name of this property."""

        temp = self.wrapped.Measurement

        if temp is None:
            return None

        if _1589.CarbonEmissionFactor.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast measurement to CarbonEmissionFactor. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @measurement_of_type_carbon_emission_factor.setter
    def measurement_of_type_carbon_emission_factor(self, value: '_1589.CarbonEmissionFactor'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_current_density(self) -> '_1590.CurrentDensity':
        """CurrentDensity: 'Measurement' is the original name of this property."""

        temp = self.wrapped.Measurement

        if temp is None:
            return None

        if _1590.CurrentDensity.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast measurement to CurrentDensity. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @measurement_of_type_current_density.setter
    def measurement_of_type_current_density(self, value: '_1590.CurrentDensity'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_current_per_length(self) -> '_1591.CurrentPerLength':
        """CurrentPerLength: 'Measurement' is the original name of this property."""

        temp = self.wrapped.Measurement

        if temp is None:
            return None

        if _1591.CurrentPerLength.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast measurement to CurrentPerLength. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @measurement_of_type_current_per_length.setter
    def measurement_of_type_current_per_length(self, value: '_1591.CurrentPerLength'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_cycles(self) -> '_1592.Cycles':
        """Cycles: 'Measurement' is the original name of this property."""

        temp = self.wrapped.Measurement

        if temp is None:
            return None

        if _1592.Cycles.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast measurement to Cycles. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @measurement_of_type_cycles.setter
    def measurement_of_type_cycles(self, value: '_1592.Cycles'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_damage(self) -> '_1593.Damage':
        """Damage: 'Measurement' is the original name of this property."""

        temp = self.wrapped.Measurement

        if temp is None:
            return None

        if _1593.Damage.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast measurement to Damage. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @measurement_of_type_damage.setter
    def measurement_of_type_damage(self, value: '_1593.Damage'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_damage_rate(self) -> '_1594.DamageRate':
        """DamageRate: 'Measurement' is the original name of this property."""

        temp = self.wrapped.Measurement

        if temp is None:
            return None

        if _1594.DamageRate.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast measurement to DamageRate. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @measurement_of_type_damage_rate.setter
    def measurement_of_type_damage_rate(self, value: '_1594.DamageRate'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_data_size(self) -> '_1595.DataSize':
        """DataSize: 'Measurement' is the original name of this property."""

        temp = self.wrapped.Measurement

        if temp is None:
            return None

        if _1595.DataSize.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast measurement to DataSize. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @measurement_of_type_data_size.setter
    def measurement_of_type_data_size(self, value: '_1595.DataSize'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_decibel(self) -> '_1596.Decibel':
        """Decibel: 'Measurement' is the original name of this property."""

        temp = self.wrapped.Measurement

        if temp is None:
            return None

        if _1596.Decibel.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast measurement to Decibel. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @measurement_of_type_decibel.setter
    def measurement_of_type_decibel(self, value: '_1596.Decibel'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_density(self) -> '_1597.Density':
        """Density: 'Measurement' is the original name of this property."""

        temp = self.wrapped.Measurement

        if temp is None:
            return None

        if _1597.Density.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast measurement to Density. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @measurement_of_type_density.setter
    def measurement_of_type_density(self, value: '_1597.Density'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_electrical_resistance(self) -> '_1598.ElectricalResistance':
        """ElectricalResistance: 'Measurement' is the original name of this property."""

        temp = self.wrapped.Measurement

        if temp is None:
            return None

        if _1598.ElectricalResistance.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast measurement to ElectricalResistance. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @measurement_of_type_electrical_resistance.setter
    def measurement_of_type_electrical_resistance(self, value: '_1598.ElectricalResistance'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_electrical_resistivity(self) -> '_1599.ElectricalResistivity':
        """ElectricalResistivity: 'Measurement' is the original name of this property."""

        temp = self.wrapped.Measurement

        if temp is None:
            return None

        if _1599.ElectricalResistivity.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast measurement to ElectricalResistivity. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @measurement_of_type_electrical_resistivity.setter
    def measurement_of_type_electrical_resistivity(self, value: '_1599.ElectricalResistivity'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_electric_current(self) -> '_1600.ElectricCurrent':
        """ElectricCurrent: 'Measurement' is the original name of this property."""

        temp = self.wrapped.Measurement

        if temp is None:
            return None

        if _1600.ElectricCurrent.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast measurement to ElectricCurrent. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @measurement_of_type_electric_current.setter
    def measurement_of_type_electric_current(self, value: '_1600.ElectricCurrent'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_energy(self) -> '_1601.Energy':
        """Energy: 'Measurement' is the original name of this property."""

        temp = self.wrapped.Measurement

        if temp is None:
            return None

        if _1601.Energy.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast measurement to Energy. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @measurement_of_type_energy.setter
    def measurement_of_type_energy(self, value: '_1601.Energy'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_energy_per_unit_area(self) -> '_1602.EnergyPerUnitArea':
        """EnergyPerUnitArea: 'Measurement' is the original name of this property."""

        temp = self.wrapped.Measurement

        if temp is None:
            return None

        if _1602.EnergyPerUnitArea.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast measurement to EnergyPerUnitArea. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @measurement_of_type_energy_per_unit_area.setter
    def measurement_of_type_energy_per_unit_area(self, value: '_1602.EnergyPerUnitArea'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_energy_per_unit_area_small(self) -> '_1603.EnergyPerUnitAreaSmall':
        """EnergyPerUnitAreaSmall: 'Measurement' is the original name of this property."""

        temp = self.wrapped.Measurement

        if temp is None:
            return None

        if _1603.EnergyPerUnitAreaSmall.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast measurement to EnergyPerUnitAreaSmall. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @measurement_of_type_energy_per_unit_area_small.setter
    def measurement_of_type_energy_per_unit_area_small(self, value: '_1603.EnergyPerUnitAreaSmall'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_energy_small(self) -> '_1604.EnergySmall':
        """EnergySmall: 'Measurement' is the original name of this property."""

        temp = self.wrapped.Measurement

        if temp is None:
            return None

        if _1604.EnergySmall.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast measurement to EnergySmall. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @measurement_of_type_energy_small.setter
    def measurement_of_type_energy_small(self, value: '_1604.EnergySmall'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_enum(self) -> '_1605.Enum':
        """Enum: 'Measurement' is the original name of this property."""

        temp = self.wrapped.Measurement

        if temp is None:
            return None

        if _1605.Enum.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast measurement to Enum. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @measurement_of_type_enum.setter
    def measurement_of_type_enum(self, value: '_1605.Enum'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_flow_rate(self) -> '_1606.FlowRate':
        """FlowRate: 'Measurement' is the original name of this property."""

        temp = self.wrapped.Measurement

        if temp is None:
            return None

        if _1606.FlowRate.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast measurement to FlowRate. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @measurement_of_type_flow_rate.setter
    def measurement_of_type_flow_rate(self, value: '_1606.FlowRate'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_force(self) -> '_1607.Force':
        """Force: 'Measurement' is the original name of this property."""

        temp = self.wrapped.Measurement

        if temp is None:
            return None

        if _1607.Force.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast measurement to Force. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @measurement_of_type_force.setter
    def measurement_of_type_force(self, value: '_1607.Force'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_force_per_unit_length(self) -> '_1608.ForcePerUnitLength':
        """ForcePerUnitLength: 'Measurement' is the original name of this property."""

        temp = self.wrapped.Measurement

        if temp is None:
            return None

        if _1608.ForcePerUnitLength.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast measurement to ForcePerUnitLength. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @measurement_of_type_force_per_unit_length.setter
    def measurement_of_type_force_per_unit_length(self, value: '_1608.ForcePerUnitLength'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_force_per_unit_pressure(self) -> '_1609.ForcePerUnitPressure':
        """ForcePerUnitPressure: 'Measurement' is the original name of this property."""

        temp = self.wrapped.Measurement

        if temp is None:
            return None

        if _1609.ForcePerUnitPressure.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast measurement to ForcePerUnitPressure. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @measurement_of_type_force_per_unit_pressure.setter
    def measurement_of_type_force_per_unit_pressure(self, value: '_1609.ForcePerUnitPressure'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_force_per_unit_temperature(self) -> '_1610.ForcePerUnitTemperature':
        """ForcePerUnitTemperature: 'Measurement' is the original name of this property."""

        temp = self.wrapped.Measurement

        if temp is None:
            return None

        if _1610.ForcePerUnitTemperature.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast measurement to ForcePerUnitTemperature. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @measurement_of_type_force_per_unit_temperature.setter
    def measurement_of_type_force_per_unit_temperature(self, value: '_1610.ForcePerUnitTemperature'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_fraction_measurement_base(self) -> '_1611.FractionMeasurementBase':
        """FractionMeasurementBase: 'Measurement' is the original name of this property."""

        temp = self.wrapped.Measurement

        if temp is None:
            return None

        if _1611.FractionMeasurementBase.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast measurement to FractionMeasurementBase. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @measurement_of_type_fraction_measurement_base.setter
    def measurement_of_type_fraction_measurement_base(self, value: '_1611.FractionMeasurementBase'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_fraction_per_temperature(self) -> '_1612.FractionPerTemperature':
        """FractionPerTemperature: 'Measurement' is the original name of this property."""

        temp = self.wrapped.Measurement

        if temp is None:
            return None

        if _1612.FractionPerTemperature.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast measurement to FractionPerTemperature. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @measurement_of_type_fraction_per_temperature.setter
    def measurement_of_type_fraction_per_temperature(self, value: '_1612.FractionPerTemperature'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_frequency(self) -> '_1613.Frequency':
        """Frequency: 'Measurement' is the original name of this property."""

        temp = self.wrapped.Measurement

        if temp is None:
            return None

        if _1613.Frequency.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast measurement to Frequency. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @measurement_of_type_frequency.setter
    def measurement_of_type_frequency(self, value: '_1613.Frequency'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_fuel_consumption_engine(self) -> '_1614.FuelConsumptionEngine':
        """FuelConsumptionEngine: 'Measurement' is the original name of this property."""

        temp = self.wrapped.Measurement

        if temp is None:
            return None

        if _1614.FuelConsumptionEngine.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast measurement to FuelConsumptionEngine. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @measurement_of_type_fuel_consumption_engine.setter
    def measurement_of_type_fuel_consumption_engine(self, value: '_1614.FuelConsumptionEngine'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_fuel_efficiency_vehicle(self) -> '_1615.FuelEfficiencyVehicle':
        """FuelEfficiencyVehicle: 'Measurement' is the original name of this property."""

        temp = self.wrapped.Measurement

        if temp is None:
            return None

        if _1615.FuelEfficiencyVehicle.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast measurement to FuelEfficiencyVehicle. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @measurement_of_type_fuel_efficiency_vehicle.setter
    def measurement_of_type_fuel_efficiency_vehicle(self, value: '_1615.FuelEfficiencyVehicle'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_gradient(self) -> '_1616.Gradient':
        """Gradient: 'Measurement' is the original name of this property."""

        temp = self.wrapped.Measurement

        if temp is None:
            return None

        if _1616.Gradient.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast measurement to Gradient. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @measurement_of_type_gradient.setter
    def measurement_of_type_gradient(self, value: '_1616.Gradient'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_heat_conductivity(self) -> '_1617.HeatConductivity':
        """HeatConductivity: 'Measurement' is the original name of this property."""

        temp = self.wrapped.Measurement

        if temp is None:
            return None

        if _1617.HeatConductivity.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast measurement to HeatConductivity. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @measurement_of_type_heat_conductivity.setter
    def measurement_of_type_heat_conductivity(self, value: '_1617.HeatConductivity'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_heat_transfer(self) -> '_1618.HeatTransfer':
        """HeatTransfer: 'Measurement' is the original name of this property."""

        temp = self.wrapped.Measurement

        if temp is None:
            return None

        if _1618.HeatTransfer.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast measurement to HeatTransfer. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @measurement_of_type_heat_transfer.setter
    def measurement_of_type_heat_transfer(self, value: '_1618.HeatTransfer'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_heat_transfer_coefficient_for_plastic_gear_tooth(self) -> '_1619.HeatTransferCoefficientForPlasticGearTooth':
        """HeatTransferCoefficientForPlasticGearTooth: 'Measurement' is the original name of this property."""

        temp = self.wrapped.Measurement

        if temp is None:
            return None

        if _1619.HeatTransferCoefficientForPlasticGearTooth.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast measurement to HeatTransferCoefficientForPlasticGearTooth. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @measurement_of_type_heat_transfer_coefficient_for_plastic_gear_tooth.setter
    def measurement_of_type_heat_transfer_coefficient_for_plastic_gear_tooth(self, value: '_1619.HeatTransferCoefficientForPlasticGearTooth'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_heat_transfer_resistance(self) -> '_1620.HeatTransferResistance':
        """HeatTransferResistance: 'Measurement' is the original name of this property."""

        temp = self.wrapped.Measurement

        if temp is None:
            return None

        if _1620.HeatTransferResistance.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast measurement to HeatTransferResistance. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @measurement_of_type_heat_transfer_resistance.setter
    def measurement_of_type_heat_transfer_resistance(self, value: '_1620.HeatTransferResistance'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_impulse(self) -> '_1621.Impulse':
        """Impulse: 'Measurement' is the original name of this property."""

        temp = self.wrapped.Measurement

        if temp is None:
            return None

        if _1621.Impulse.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast measurement to Impulse. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @measurement_of_type_impulse.setter
    def measurement_of_type_impulse(self, value: '_1621.Impulse'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_index(self) -> '_1622.Index':
        """Index: 'Measurement' is the original name of this property."""

        temp = self.wrapped.Measurement

        if temp is None:
            return None

        if _1622.Index.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast measurement to Index. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @measurement_of_type_index.setter
    def measurement_of_type_index(self, value: '_1622.Index'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_inductance(self) -> '_1623.Inductance':
        """Inductance: 'Measurement' is the original name of this property."""

        temp = self.wrapped.Measurement

        if temp is None:
            return None

        if _1623.Inductance.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast measurement to Inductance. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @measurement_of_type_inductance.setter
    def measurement_of_type_inductance(self, value: '_1623.Inductance'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_integer(self) -> '_1624.Integer':
        """Integer: 'Measurement' is the original name of this property."""

        temp = self.wrapped.Measurement

        if temp is None:
            return None

        if _1624.Integer.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast measurement to Integer. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @measurement_of_type_integer.setter
    def measurement_of_type_integer(self, value: '_1624.Integer'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_inverse_short_length(self) -> '_1625.InverseShortLength':
        """InverseShortLength: 'Measurement' is the original name of this property."""

        temp = self.wrapped.Measurement

        if temp is None:
            return None

        if _1625.InverseShortLength.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast measurement to InverseShortLength. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @measurement_of_type_inverse_short_length.setter
    def measurement_of_type_inverse_short_length(self, value: '_1625.InverseShortLength'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_inverse_short_time(self) -> '_1626.InverseShortTime':
        """InverseShortTime: 'Measurement' is the original name of this property."""

        temp = self.wrapped.Measurement

        if temp is None:
            return None

        if _1626.InverseShortTime.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast measurement to InverseShortTime. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @measurement_of_type_inverse_short_time.setter
    def measurement_of_type_inverse_short_time(self, value: '_1626.InverseShortTime'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_jerk(self) -> '_1627.Jerk':
        """Jerk: 'Measurement' is the original name of this property."""

        temp = self.wrapped.Measurement

        if temp is None:
            return None

        if _1627.Jerk.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast measurement to Jerk. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @measurement_of_type_jerk.setter
    def measurement_of_type_jerk(self, value: '_1627.Jerk'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_kinematic_viscosity(self) -> '_1628.KinematicViscosity':
        """KinematicViscosity: 'Measurement' is the original name of this property."""

        temp = self.wrapped.Measurement

        if temp is None:
            return None

        if _1628.KinematicViscosity.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast measurement to KinematicViscosity. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @measurement_of_type_kinematic_viscosity.setter
    def measurement_of_type_kinematic_viscosity(self, value: '_1628.KinematicViscosity'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_length_long(self) -> '_1629.LengthLong':
        """LengthLong: 'Measurement' is the original name of this property."""

        temp = self.wrapped.Measurement

        if temp is None:
            return None

        if _1629.LengthLong.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast measurement to LengthLong. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @measurement_of_type_length_long.setter
    def measurement_of_type_length_long(self, value: '_1629.LengthLong'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_length_medium(self) -> '_1630.LengthMedium':
        """LengthMedium: 'Measurement' is the original name of this property."""

        temp = self.wrapped.Measurement

        if temp is None:
            return None

        if _1630.LengthMedium.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast measurement to LengthMedium. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @measurement_of_type_length_medium.setter
    def measurement_of_type_length_medium(self, value: '_1630.LengthMedium'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_length_per_unit_temperature(self) -> '_1631.LengthPerUnitTemperature':
        """LengthPerUnitTemperature: 'Measurement' is the original name of this property."""

        temp = self.wrapped.Measurement

        if temp is None:
            return None

        if _1631.LengthPerUnitTemperature.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast measurement to LengthPerUnitTemperature. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @measurement_of_type_length_per_unit_temperature.setter
    def measurement_of_type_length_per_unit_temperature(self, value: '_1631.LengthPerUnitTemperature'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_length_short(self) -> '_1632.LengthShort':
        """LengthShort: 'Measurement' is the original name of this property."""

        temp = self.wrapped.Measurement

        if temp is None:
            return None

        if _1632.LengthShort.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast measurement to LengthShort. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @measurement_of_type_length_short.setter
    def measurement_of_type_length_short(self, value: '_1632.LengthShort'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_length_to_the_fourth(self) -> '_1633.LengthToTheFourth':
        """LengthToTheFourth: 'Measurement' is the original name of this property."""

        temp = self.wrapped.Measurement

        if temp is None:
            return None

        if _1633.LengthToTheFourth.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast measurement to LengthToTheFourth. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @measurement_of_type_length_to_the_fourth.setter
    def measurement_of_type_length_to_the_fourth(self, value: '_1633.LengthToTheFourth'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_length_very_long(self) -> '_1634.LengthVeryLong':
        """LengthVeryLong: 'Measurement' is the original name of this property."""

        temp = self.wrapped.Measurement

        if temp is None:
            return None

        if _1634.LengthVeryLong.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast measurement to LengthVeryLong. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @measurement_of_type_length_very_long.setter
    def measurement_of_type_length_very_long(self, value: '_1634.LengthVeryLong'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_length_very_short(self) -> '_1635.LengthVeryShort':
        """LengthVeryShort: 'Measurement' is the original name of this property."""

        temp = self.wrapped.Measurement

        if temp is None:
            return None

        if _1635.LengthVeryShort.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast measurement to LengthVeryShort. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @measurement_of_type_length_very_short.setter
    def measurement_of_type_length_very_short(self, value: '_1635.LengthVeryShort'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_length_very_short_per_length_short(self) -> '_1636.LengthVeryShortPerLengthShort':
        """LengthVeryShortPerLengthShort: 'Measurement' is the original name of this property."""

        temp = self.wrapped.Measurement

        if temp is None:
            return None

        if _1636.LengthVeryShortPerLengthShort.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast measurement to LengthVeryShortPerLengthShort. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @measurement_of_type_length_very_short_per_length_short.setter
    def measurement_of_type_length_very_short_per_length_short(self, value: '_1636.LengthVeryShortPerLengthShort'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_linear_angular_damping(self) -> '_1637.LinearAngularDamping':
        """LinearAngularDamping: 'Measurement' is the original name of this property."""

        temp = self.wrapped.Measurement

        if temp is None:
            return None

        if _1637.LinearAngularDamping.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast measurement to LinearAngularDamping. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @measurement_of_type_linear_angular_damping.setter
    def measurement_of_type_linear_angular_damping(self, value: '_1637.LinearAngularDamping'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_linear_angular_stiffness_cross_term(self) -> '_1638.LinearAngularStiffnessCrossTerm':
        """LinearAngularStiffnessCrossTerm: 'Measurement' is the original name of this property."""

        temp = self.wrapped.Measurement

        if temp is None:
            return None

        if _1638.LinearAngularStiffnessCrossTerm.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast measurement to LinearAngularStiffnessCrossTerm. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @measurement_of_type_linear_angular_stiffness_cross_term.setter
    def measurement_of_type_linear_angular_stiffness_cross_term(self, value: '_1638.LinearAngularStiffnessCrossTerm'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_linear_damping(self) -> '_1639.LinearDamping':
        """LinearDamping: 'Measurement' is the original name of this property."""

        temp = self.wrapped.Measurement

        if temp is None:
            return None

        if _1639.LinearDamping.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast measurement to LinearDamping. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @measurement_of_type_linear_damping.setter
    def measurement_of_type_linear_damping(self, value: '_1639.LinearDamping'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_linear_flexibility(self) -> '_1640.LinearFlexibility':
        """LinearFlexibility: 'Measurement' is the original name of this property."""

        temp = self.wrapped.Measurement

        if temp is None:
            return None

        if _1640.LinearFlexibility.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast measurement to LinearFlexibility. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @measurement_of_type_linear_flexibility.setter
    def measurement_of_type_linear_flexibility(self, value: '_1640.LinearFlexibility'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_linear_stiffness(self) -> '_1641.LinearStiffness':
        """LinearStiffness: 'Measurement' is the original name of this property."""

        temp = self.wrapped.Measurement

        if temp is None:
            return None

        if _1641.LinearStiffness.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast measurement to LinearStiffness. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @measurement_of_type_linear_stiffness.setter
    def measurement_of_type_linear_stiffness(self, value: '_1641.LinearStiffness'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_magnetic_field_strength(self) -> '_1642.MagneticFieldStrength':
        """MagneticFieldStrength: 'Measurement' is the original name of this property."""

        temp = self.wrapped.Measurement

        if temp is None:
            return None

        if _1642.MagneticFieldStrength.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast measurement to MagneticFieldStrength. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @measurement_of_type_magnetic_field_strength.setter
    def measurement_of_type_magnetic_field_strength(self, value: '_1642.MagneticFieldStrength'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_magnetic_flux(self) -> '_1643.MagneticFlux':
        """MagneticFlux: 'Measurement' is the original name of this property."""

        temp = self.wrapped.Measurement

        if temp is None:
            return None

        if _1643.MagneticFlux.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast measurement to MagneticFlux. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @measurement_of_type_magnetic_flux.setter
    def measurement_of_type_magnetic_flux(self, value: '_1643.MagneticFlux'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_magnetic_flux_density(self) -> '_1644.MagneticFluxDensity':
        """MagneticFluxDensity: 'Measurement' is the original name of this property."""

        temp = self.wrapped.Measurement

        if temp is None:
            return None

        if _1644.MagneticFluxDensity.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast measurement to MagneticFluxDensity. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @measurement_of_type_magnetic_flux_density.setter
    def measurement_of_type_magnetic_flux_density(self, value: '_1644.MagneticFluxDensity'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_magnetic_vector_potential(self) -> '_1645.MagneticVectorPotential':
        """MagneticVectorPotential: 'Measurement' is the original name of this property."""

        temp = self.wrapped.Measurement

        if temp is None:
            return None

        if _1645.MagneticVectorPotential.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast measurement to MagneticVectorPotential. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @measurement_of_type_magnetic_vector_potential.setter
    def measurement_of_type_magnetic_vector_potential(self, value: '_1645.MagneticVectorPotential'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_magnetomotive_force(self) -> '_1646.MagnetomotiveForce':
        """MagnetomotiveForce: 'Measurement' is the original name of this property."""

        temp = self.wrapped.Measurement

        if temp is None:
            return None

        if _1646.MagnetomotiveForce.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast measurement to MagnetomotiveForce. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @measurement_of_type_magnetomotive_force.setter
    def measurement_of_type_magnetomotive_force(self, value: '_1646.MagnetomotiveForce'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_mass(self) -> '_1647.Mass':
        """Mass: 'Measurement' is the original name of this property."""

        temp = self.wrapped.Measurement

        if temp is None:
            return None

        if _1647.Mass.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast measurement to Mass. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @measurement_of_type_mass.setter
    def measurement_of_type_mass(self, value: '_1647.Mass'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_mass_per_unit_length(self) -> '_1648.MassPerUnitLength':
        """MassPerUnitLength: 'Measurement' is the original name of this property."""

        temp = self.wrapped.Measurement

        if temp is None:
            return None

        if _1648.MassPerUnitLength.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast measurement to MassPerUnitLength. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @measurement_of_type_mass_per_unit_length.setter
    def measurement_of_type_mass_per_unit_length(self, value: '_1648.MassPerUnitLength'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_mass_per_unit_time(self) -> '_1649.MassPerUnitTime':
        """MassPerUnitTime: 'Measurement' is the original name of this property."""

        temp = self.wrapped.Measurement

        if temp is None:
            return None

        if _1649.MassPerUnitTime.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast measurement to MassPerUnitTime. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @measurement_of_type_mass_per_unit_time.setter
    def measurement_of_type_mass_per_unit_time(self, value: '_1649.MassPerUnitTime'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_moment_of_inertia(self) -> '_1650.MomentOfInertia':
        """MomentOfInertia: 'Measurement' is the original name of this property."""

        temp = self.wrapped.Measurement

        if temp is None:
            return None

        if _1650.MomentOfInertia.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast measurement to MomentOfInertia. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @measurement_of_type_moment_of_inertia.setter
    def measurement_of_type_moment_of_inertia(self, value: '_1650.MomentOfInertia'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_moment_of_inertia_per_unit_length(self) -> '_1651.MomentOfInertiaPerUnitLength':
        """MomentOfInertiaPerUnitLength: 'Measurement' is the original name of this property."""

        temp = self.wrapped.Measurement

        if temp is None:
            return None

        if _1651.MomentOfInertiaPerUnitLength.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast measurement to MomentOfInertiaPerUnitLength. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @measurement_of_type_moment_of_inertia_per_unit_length.setter
    def measurement_of_type_moment_of_inertia_per_unit_length(self, value: '_1651.MomentOfInertiaPerUnitLength'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_moment_per_unit_pressure(self) -> '_1652.MomentPerUnitPressure':
        """MomentPerUnitPressure: 'Measurement' is the original name of this property."""

        temp = self.wrapped.Measurement

        if temp is None:
            return None

        if _1652.MomentPerUnitPressure.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast measurement to MomentPerUnitPressure. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @measurement_of_type_moment_per_unit_pressure.setter
    def measurement_of_type_moment_per_unit_pressure(self, value: '_1652.MomentPerUnitPressure'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_number(self) -> '_1653.Number':
        """Number: 'Measurement' is the original name of this property."""

        temp = self.wrapped.Measurement

        if temp is None:
            return None

        if _1653.Number.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast measurement to Number. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @measurement_of_type_number.setter
    def measurement_of_type_number(self, value: '_1653.Number'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_percentage(self) -> '_1654.Percentage':
        """Percentage: 'Measurement' is the original name of this property."""

        temp = self.wrapped.Measurement

        if temp is None:
            return None

        if _1654.Percentage.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast measurement to Percentage. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @measurement_of_type_percentage.setter
    def measurement_of_type_percentage(self, value: '_1654.Percentage'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_power(self) -> '_1655.Power':
        """Power: 'Measurement' is the original name of this property."""

        temp = self.wrapped.Measurement

        if temp is None:
            return None

        if _1655.Power.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast measurement to Power. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @measurement_of_type_power.setter
    def measurement_of_type_power(self, value: '_1655.Power'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_power_per_small_area(self) -> '_1656.PowerPerSmallArea':
        """PowerPerSmallArea: 'Measurement' is the original name of this property."""

        temp = self.wrapped.Measurement

        if temp is None:
            return None

        if _1656.PowerPerSmallArea.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast measurement to PowerPerSmallArea. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @measurement_of_type_power_per_small_area.setter
    def measurement_of_type_power_per_small_area(self, value: '_1656.PowerPerSmallArea'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_power_per_unit_time(self) -> '_1657.PowerPerUnitTime':
        """PowerPerUnitTime: 'Measurement' is the original name of this property."""

        temp = self.wrapped.Measurement

        if temp is None:
            return None

        if _1657.PowerPerUnitTime.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast measurement to PowerPerUnitTime. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @measurement_of_type_power_per_unit_time.setter
    def measurement_of_type_power_per_unit_time(self, value: '_1657.PowerPerUnitTime'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_power_small(self) -> '_1658.PowerSmall':
        """PowerSmall: 'Measurement' is the original name of this property."""

        temp = self.wrapped.Measurement

        if temp is None:
            return None

        if _1658.PowerSmall.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast measurement to PowerSmall. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @measurement_of_type_power_small.setter
    def measurement_of_type_power_small(self, value: '_1658.PowerSmall'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_power_small_per_area(self) -> '_1659.PowerSmallPerArea':
        """PowerSmallPerArea: 'Measurement' is the original name of this property."""

        temp = self.wrapped.Measurement

        if temp is None:
            return None

        if _1659.PowerSmallPerArea.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast measurement to PowerSmallPerArea. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @measurement_of_type_power_small_per_area.setter
    def measurement_of_type_power_small_per_area(self, value: '_1659.PowerSmallPerArea'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_power_small_per_mass(self) -> '_1660.PowerSmallPerMass':
        """PowerSmallPerMass: 'Measurement' is the original name of this property."""

        temp = self.wrapped.Measurement

        if temp is None:
            return None

        if _1660.PowerSmallPerMass.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast measurement to PowerSmallPerMass. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @measurement_of_type_power_small_per_mass.setter
    def measurement_of_type_power_small_per_mass(self, value: '_1660.PowerSmallPerMass'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_power_small_per_unit_area_per_unit_time(self) -> '_1661.PowerSmallPerUnitAreaPerUnitTime':
        """PowerSmallPerUnitAreaPerUnitTime: 'Measurement' is the original name of this property."""

        temp = self.wrapped.Measurement

        if temp is None:
            return None

        if _1661.PowerSmallPerUnitAreaPerUnitTime.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast measurement to PowerSmallPerUnitAreaPerUnitTime. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @measurement_of_type_power_small_per_unit_area_per_unit_time.setter
    def measurement_of_type_power_small_per_unit_area_per_unit_time(self, value: '_1661.PowerSmallPerUnitAreaPerUnitTime'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_power_small_per_unit_time(self) -> '_1662.PowerSmallPerUnitTime':
        """PowerSmallPerUnitTime: 'Measurement' is the original name of this property."""

        temp = self.wrapped.Measurement

        if temp is None:
            return None

        if _1662.PowerSmallPerUnitTime.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast measurement to PowerSmallPerUnitTime. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @measurement_of_type_power_small_per_unit_time.setter
    def measurement_of_type_power_small_per_unit_time(self, value: '_1662.PowerSmallPerUnitTime'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_power_small_per_volume(self) -> '_1663.PowerSmallPerVolume':
        """PowerSmallPerVolume: 'Measurement' is the original name of this property."""

        temp = self.wrapped.Measurement

        if temp is None:
            return None

        if _1663.PowerSmallPerVolume.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast measurement to PowerSmallPerVolume. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @measurement_of_type_power_small_per_volume.setter
    def measurement_of_type_power_small_per_volume(self, value: '_1663.PowerSmallPerVolume'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_pressure(self) -> '_1664.Pressure':
        """Pressure: 'Measurement' is the original name of this property."""

        temp = self.wrapped.Measurement

        if temp is None:
            return None

        if _1664.Pressure.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast measurement to Pressure. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @measurement_of_type_pressure.setter
    def measurement_of_type_pressure(self, value: '_1664.Pressure'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_pressure_per_unit_time(self) -> '_1665.PressurePerUnitTime':
        """PressurePerUnitTime: 'Measurement' is the original name of this property."""

        temp = self.wrapped.Measurement

        if temp is None:
            return None

        if _1665.PressurePerUnitTime.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast measurement to PressurePerUnitTime. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @measurement_of_type_pressure_per_unit_time.setter
    def measurement_of_type_pressure_per_unit_time(self, value: '_1665.PressurePerUnitTime'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_pressure_velocity_product(self) -> '_1666.PressureVelocityProduct':
        """PressureVelocityProduct: 'Measurement' is the original name of this property."""

        temp = self.wrapped.Measurement

        if temp is None:
            return None

        if _1666.PressureVelocityProduct.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast measurement to PressureVelocityProduct. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @measurement_of_type_pressure_velocity_product.setter
    def measurement_of_type_pressure_velocity_product(self, value: '_1666.PressureVelocityProduct'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_pressure_viscosity_coefficient(self) -> '_1667.PressureViscosityCoefficient':
        """PressureViscosityCoefficient: 'Measurement' is the original name of this property."""

        temp = self.wrapped.Measurement

        if temp is None:
            return None

        if _1667.PressureViscosityCoefficient.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast measurement to PressureViscosityCoefficient. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @measurement_of_type_pressure_viscosity_coefficient.setter
    def measurement_of_type_pressure_viscosity_coefficient(self, value: '_1667.PressureViscosityCoefficient'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_price(self) -> '_1668.Price':
        """Price: 'Measurement' is the original name of this property."""

        temp = self.wrapped.Measurement

        if temp is None:
            return None

        if _1668.Price.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast measurement to Price. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @measurement_of_type_price.setter
    def measurement_of_type_price(self, value: '_1668.Price'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_price_per_unit_mass(self) -> '_1669.PricePerUnitMass':
        """PricePerUnitMass: 'Measurement' is the original name of this property."""

        temp = self.wrapped.Measurement

        if temp is None:
            return None

        if _1669.PricePerUnitMass.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast measurement to PricePerUnitMass. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @measurement_of_type_price_per_unit_mass.setter
    def measurement_of_type_price_per_unit_mass(self, value: '_1669.PricePerUnitMass'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_quadratic_angular_damping(self) -> '_1670.QuadraticAngularDamping':
        """QuadraticAngularDamping: 'Measurement' is the original name of this property."""

        temp = self.wrapped.Measurement

        if temp is None:
            return None

        if _1670.QuadraticAngularDamping.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast measurement to QuadraticAngularDamping. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @measurement_of_type_quadratic_angular_damping.setter
    def measurement_of_type_quadratic_angular_damping(self, value: '_1670.QuadraticAngularDamping'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_quadratic_drag(self) -> '_1671.QuadraticDrag':
        """QuadraticDrag: 'Measurement' is the original name of this property."""

        temp = self.wrapped.Measurement

        if temp is None:
            return None

        if _1671.QuadraticDrag.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast measurement to QuadraticDrag. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @measurement_of_type_quadratic_drag.setter
    def measurement_of_type_quadratic_drag(self, value: '_1671.QuadraticDrag'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_rescaled_measurement(self) -> '_1672.RescaledMeasurement':
        """RescaledMeasurement: 'Measurement' is the original name of this property."""

        temp = self.wrapped.Measurement

        if temp is None:
            return None

        if _1672.RescaledMeasurement.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast measurement to RescaledMeasurement. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @measurement_of_type_rescaled_measurement.setter
    def measurement_of_type_rescaled_measurement(self, value: '_1672.RescaledMeasurement'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_rotatum(self) -> '_1673.Rotatum':
        """Rotatum: 'Measurement' is the original name of this property."""

        temp = self.wrapped.Measurement

        if temp is None:
            return None

        if _1673.Rotatum.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast measurement to Rotatum. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @measurement_of_type_rotatum.setter
    def measurement_of_type_rotatum(self, value: '_1673.Rotatum'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_safety_factor(self) -> '_1674.SafetyFactor':
        """SafetyFactor: 'Measurement' is the original name of this property."""

        temp = self.wrapped.Measurement

        if temp is None:
            return None

        if _1674.SafetyFactor.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast measurement to SafetyFactor. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @measurement_of_type_safety_factor.setter
    def measurement_of_type_safety_factor(self, value: '_1674.SafetyFactor'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_specific_acoustic_impedance(self) -> '_1675.SpecificAcousticImpedance':
        """SpecificAcousticImpedance: 'Measurement' is the original name of this property."""

        temp = self.wrapped.Measurement

        if temp is None:
            return None

        if _1675.SpecificAcousticImpedance.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast measurement to SpecificAcousticImpedance. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @measurement_of_type_specific_acoustic_impedance.setter
    def measurement_of_type_specific_acoustic_impedance(self, value: '_1675.SpecificAcousticImpedance'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_specific_heat(self) -> '_1676.SpecificHeat':
        """SpecificHeat: 'Measurement' is the original name of this property."""

        temp = self.wrapped.Measurement

        if temp is None:
            return None

        if _1676.SpecificHeat.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast measurement to SpecificHeat. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @measurement_of_type_specific_heat.setter
    def measurement_of_type_specific_heat(self, value: '_1676.SpecificHeat'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_square_root_of_unit_force_per_unit_area(self) -> '_1677.SquareRootOfUnitForcePerUnitArea':
        """SquareRootOfUnitForcePerUnitArea: 'Measurement' is the original name of this property."""

        temp = self.wrapped.Measurement

        if temp is None:
            return None

        if _1677.SquareRootOfUnitForcePerUnitArea.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast measurement to SquareRootOfUnitForcePerUnitArea. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @measurement_of_type_square_root_of_unit_force_per_unit_area.setter
    def measurement_of_type_square_root_of_unit_force_per_unit_area(self, value: '_1677.SquareRootOfUnitForcePerUnitArea'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_stiffness_per_unit_face_width(self) -> '_1678.StiffnessPerUnitFaceWidth':
        """StiffnessPerUnitFaceWidth: 'Measurement' is the original name of this property."""

        temp = self.wrapped.Measurement

        if temp is None:
            return None

        if _1678.StiffnessPerUnitFaceWidth.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast measurement to StiffnessPerUnitFaceWidth. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @measurement_of_type_stiffness_per_unit_face_width.setter
    def measurement_of_type_stiffness_per_unit_face_width(self, value: '_1678.StiffnessPerUnitFaceWidth'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_stress(self) -> '_1679.Stress':
        """Stress: 'Measurement' is the original name of this property."""

        temp = self.wrapped.Measurement

        if temp is None:
            return None

        if _1679.Stress.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast measurement to Stress. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @measurement_of_type_stress.setter
    def measurement_of_type_stress(self, value: '_1679.Stress'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_temperature(self) -> '_1680.Temperature':
        """Temperature: 'Measurement' is the original name of this property."""

        temp = self.wrapped.Measurement

        if temp is None:
            return None

        if _1680.Temperature.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast measurement to Temperature. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @measurement_of_type_temperature.setter
    def measurement_of_type_temperature(self, value: '_1680.Temperature'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_temperature_difference(self) -> '_1681.TemperatureDifference':
        """TemperatureDifference: 'Measurement' is the original name of this property."""

        temp = self.wrapped.Measurement

        if temp is None:
            return None

        if _1681.TemperatureDifference.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast measurement to TemperatureDifference. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @measurement_of_type_temperature_difference.setter
    def measurement_of_type_temperature_difference(self, value: '_1681.TemperatureDifference'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_temperature_per_unit_time(self) -> '_1682.TemperaturePerUnitTime':
        """TemperaturePerUnitTime: 'Measurement' is the original name of this property."""

        temp = self.wrapped.Measurement

        if temp is None:
            return None

        if _1682.TemperaturePerUnitTime.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast measurement to TemperaturePerUnitTime. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @measurement_of_type_temperature_per_unit_time.setter
    def measurement_of_type_temperature_per_unit_time(self, value: '_1682.TemperaturePerUnitTime'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_text(self) -> '_1683.Text':
        """Text: 'Measurement' is the original name of this property."""

        temp = self.wrapped.Measurement

        if temp is None:
            return None

        if _1683.Text.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast measurement to Text. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @measurement_of_type_text.setter
    def measurement_of_type_text(self, value: '_1683.Text'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_thermal_contact_coefficient(self) -> '_1684.ThermalContactCoefficient':
        """ThermalContactCoefficient: 'Measurement' is the original name of this property."""

        temp = self.wrapped.Measurement

        if temp is None:
            return None

        if _1684.ThermalContactCoefficient.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast measurement to ThermalContactCoefficient. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @measurement_of_type_thermal_contact_coefficient.setter
    def measurement_of_type_thermal_contact_coefficient(self, value: '_1684.ThermalContactCoefficient'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_thermal_expansion_coefficient(self) -> '_1685.ThermalExpansionCoefficient':
        """ThermalExpansionCoefficient: 'Measurement' is the original name of this property."""

        temp = self.wrapped.Measurement

        if temp is None:
            return None

        if _1685.ThermalExpansionCoefficient.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast measurement to ThermalExpansionCoefficient. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @measurement_of_type_thermal_expansion_coefficient.setter
    def measurement_of_type_thermal_expansion_coefficient(self, value: '_1685.ThermalExpansionCoefficient'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_thermo_elastic_factor(self) -> '_1686.ThermoElasticFactor':
        """ThermoElasticFactor: 'Measurement' is the original name of this property."""

        temp = self.wrapped.Measurement

        if temp is None:
            return None

        if _1686.ThermoElasticFactor.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast measurement to ThermoElasticFactor. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @measurement_of_type_thermo_elastic_factor.setter
    def measurement_of_type_thermo_elastic_factor(self, value: '_1686.ThermoElasticFactor'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_time(self) -> '_1687.Time':
        """Time: 'Measurement' is the original name of this property."""

        temp = self.wrapped.Measurement

        if temp is None:
            return None

        if _1687.Time.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast measurement to Time. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @measurement_of_type_time.setter
    def measurement_of_type_time(self, value: '_1687.Time'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_time_short(self) -> '_1688.TimeShort':
        """TimeShort: 'Measurement' is the original name of this property."""

        temp = self.wrapped.Measurement

        if temp is None:
            return None

        if _1688.TimeShort.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast measurement to TimeShort. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @measurement_of_type_time_short.setter
    def measurement_of_type_time_short(self, value: '_1688.TimeShort'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_time_very_short(self) -> '_1689.TimeVeryShort':
        """TimeVeryShort: 'Measurement' is the original name of this property."""

        temp = self.wrapped.Measurement

        if temp is None:
            return None

        if _1689.TimeVeryShort.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast measurement to TimeVeryShort. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @measurement_of_type_time_very_short.setter
    def measurement_of_type_time_very_short(self, value: '_1689.TimeVeryShort'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_torque(self) -> '_1690.Torque':
        """Torque: 'Measurement' is the original name of this property."""

        temp = self.wrapped.Measurement

        if temp is None:
            return None

        if _1690.Torque.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast measurement to Torque. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @measurement_of_type_torque.setter
    def measurement_of_type_torque(self, value: '_1690.Torque'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_torque_converter_inverse_k(self) -> '_1691.TorqueConverterInverseK':
        """TorqueConverterInverseK: 'Measurement' is the original name of this property."""

        temp = self.wrapped.Measurement

        if temp is None:
            return None

        if _1691.TorqueConverterInverseK.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast measurement to TorqueConverterInverseK. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @measurement_of_type_torque_converter_inverse_k.setter
    def measurement_of_type_torque_converter_inverse_k(self, value: '_1691.TorqueConverterInverseK'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_torque_converter_k(self) -> '_1692.TorqueConverterK':
        """TorqueConverterK: 'Measurement' is the original name of this property."""

        temp = self.wrapped.Measurement

        if temp is None:
            return None

        if _1692.TorqueConverterK.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast measurement to TorqueConverterK. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @measurement_of_type_torque_converter_k.setter
    def measurement_of_type_torque_converter_k(self, value: '_1692.TorqueConverterK'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_torque_per_current(self) -> '_1693.TorquePerCurrent':
        """TorquePerCurrent: 'Measurement' is the original name of this property."""

        temp = self.wrapped.Measurement

        if temp is None:
            return None

        if _1693.TorquePerCurrent.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast measurement to TorquePerCurrent. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @measurement_of_type_torque_per_current.setter
    def measurement_of_type_torque_per_current(self, value: '_1693.TorquePerCurrent'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_torque_per_square_root_of_power(self) -> '_1694.TorquePerSquareRootOfPower':
        """TorquePerSquareRootOfPower: 'Measurement' is the original name of this property."""

        temp = self.wrapped.Measurement

        if temp is None:
            return None

        if _1694.TorquePerSquareRootOfPower.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast measurement to TorquePerSquareRootOfPower. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @measurement_of_type_torque_per_square_root_of_power.setter
    def measurement_of_type_torque_per_square_root_of_power(self, value: '_1694.TorquePerSquareRootOfPower'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_torque_per_unit_temperature(self) -> '_1695.TorquePerUnitTemperature':
        """TorquePerUnitTemperature: 'Measurement' is the original name of this property."""

        temp = self.wrapped.Measurement

        if temp is None:
            return None

        if _1695.TorquePerUnitTemperature.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast measurement to TorquePerUnitTemperature. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @measurement_of_type_torque_per_unit_temperature.setter
    def measurement_of_type_torque_per_unit_temperature(self, value: '_1695.TorquePerUnitTemperature'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_velocity(self) -> '_1696.Velocity':
        """Velocity: 'Measurement' is the original name of this property."""

        temp = self.wrapped.Measurement

        if temp is None:
            return None

        if _1696.Velocity.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast measurement to Velocity. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @measurement_of_type_velocity.setter
    def measurement_of_type_velocity(self, value: '_1696.Velocity'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_velocity_small(self) -> '_1697.VelocitySmall':
        """VelocitySmall: 'Measurement' is the original name of this property."""

        temp = self.wrapped.Measurement

        if temp is None:
            return None

        if _1697.VelocitySmall.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast measurement to VelocitySmall. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @measurement_of_type_velocity_small.setter
    def measurement_of_type_velocity_small(self, value: '_1697.VelocitySmall'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_viscosity(self) -> '_1698.Viscosity':
        """Viscosity: 'Measurement' is the original name of this property."""

        temp = self.wrapped.Measurement

        if temp is None:
            return None

        if _1698.Viscosity.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast measurement to Viscosity. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @measurement_of_type_viscosity.setter
    def measurement_of_type_viscosity(self, value: '_1698.Viscosity'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_voltage(self) -> '_1699.Voltage':
        """Voltage: 'Measurement' is the original name of this property."""

        temp = self.wrapped.Measurement

        if temp is None:
            return None

        if _1699.Voltage.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast measurement to Voltage. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @measurement_of_type_voltage.setter
    def measurement_of_type_voltage(self, value: '_1699.Voltage'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_voltage_per_angular_velocity(self) -> '_1700.VoltagePerAngularVelocity':
        """VoltagePerAngularVelocity: 'Measurement' is the original name of this property."""

        temp = self.wrapped.Measurement

        if temp is None:
            return None

        if _1700.VoltagePerAngularVelocity.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast measurement to VoltagePerAngularVelocity. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @measurement_of_type_voltage_per_angular_velocity.setter
    def measurement_of_type_voltage_per_angular_velocity(self, value: '_1700.VoltagePerAngularVelocity'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_volume(self) -> '_1701.Volume':
        """Volume: 'Measurement' is the original name of this property."""

        temp = self.wrapped.Measurement

        if temp is None:
            return None

        if _1701.Volume.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast measurement to Volume. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @measurement_of_type_volume.setter
    def measurement_of_type_volume(self, value: '_1701.Volume'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_wear_coefficient(self) -> '_1702.WearCoefficient':
        """WearCoefficient: 'Measurement' is the original name of this property."""

        temp = self.wrapped.Measurement

        if temp is None:
            return None

        if _1702.WearCoefficient.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast measurement to WearCoefficient. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @measurement_of_type_wear_coefficient.setter
    def measurement_of_type_wear_coefficient(self, value: '_1702.WearCoefficient'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def measurement_of_type_yank(self) -> '_1703.Yank':
        """Yank: 'Measurement' is the original name of this property."""

        temp = self.wrapped.Measurement

        if temp is None:
            return None

        if _1703.Yank.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast measurement to Yank. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @measurement_of_type_yank.setter
    def measurement_of_type_yank(self, value: '_1703.Yank'):
        value = value.wrapped if value else None
        self.wrapped.Measurement = value

    @property
    def results(self) -> 'List[float]':
        """List[float]: 'Results' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Results

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, float)
        return value
