"""Tests for the Thermometer class"""
import pytest
from src.thermometerb.thermometer import Thermometer


def test_thermometer_constants():
    """Test Thermometer class constants."""
    assert Thermometer.BOOL_DEFAULT is False
    assert Thermometer.HUNDRED_CELSIUS == 100.0
    assert Thermometer.ZERO_CELSIUS == 0.0


def test_thermometer_defaults(thermometer):
    """Test for Thermometer data attribute defaults being set on object instantiation."""
    assert isinstance(thermometer, Thermometer)
    assert thermometer.boil == 100.0
    assert thermometer.freeze == 0.0


def test_thermometer_keyword_boil():
    """Test of Thermometer keyword boil on object instantiation."""
    with pytest.raises(ValueError, match="Can not convert boil value"):
        Thermometer(boil="boil")
    gauge_boil_float = Thermometer(boil=2.0)
    gauge_boil_int = Thermometer(boil=3)
    gauge_boil_str = Thermometer(boil="4")
    assert gauge_boil_float.boil == 2.0
    assert gauge_boil_int.boil == 3.0
    assert gauge_boil_str.boil == 4.0


def test_thermometer_keyword_freeze():
    """Test of Thermometer keyword freeze on object instantiation."""
    with pytest.raises(ValueError, match="Can not convert freeze value"):
        Thermometer(freeze="freeze")
    gauge_freeze_float = Thermometer(freeze=1.0)
    gauge_freeze_int = Thermometer(freeze=2)
    gauge_freeze_str = Thermometer(freeze="3")
    assert gauge_freeze_float.freeze == 1.0
    assert gauge_freeze_int.freeze == 2.0
    assert gauge_freeze_str.freeze == 3.0


def test_thermometer_keyword_full_degree():
    """Test of Thermometer keyword full_degree on object instantiation."""
    gauge_full_degree = Thermometer(full_degree=True)
    gauge_full_degree_int = Thermometer(full_degree=1)
    gauge_full_degree_str = Thermometer(full_degree="true")
    assert gauge_full_degree.full_degree is True
    assert gauge_full_degree_int.full_degree is True
    assert gauge_full_degree_str.full_degree is True


def test_thermometer_keyword_increase():
    """Test of Thermometer keyword increase on object instantiation."""
    gauge_increase = Thermometer(increase=True)
    gauge_increase_int = Thermometer(increase=1)
    gauge_increase_str = Thermometer(increase="true")
    assert gauge_increase.increase is True
    assert gauge_increase_int.increase is True
    assert gauge_increase_str.increase is True


def test_thermometer_keyword_decrease():
    """Test of Thermometer keyword decrease on object instantiation."""
    gauge_decrease = Thermometer(decrease=True)
    gauge_decrease_int = Thermometer(decrease=1)
    gauge_decrease_str = Thermometer(decrease="true")
    assert gauge_decrease.decrease is True
    assert gauge_decrease_int.decrease is True
    assert gauge_decrease_str.decrease is True


def test_current_temp(thermometer):
    """Test of Thermometer method current_temp."""
    with pytest.raises(ValueError, match="Can not convert current_temp"):
        thermometer.current_temp("temp")

    assert thermometer.current_temp() == 0.0
    thermometer.current_temp(2.0)
    assert thermometer.current_temp() == 2.0
    thermometer.current_temp(3)
    assert thermometer.current_temp() == 3.0
    thermometer.current_temp("4")
    assert thermometer.current_temp() == 4.0
    thermometer.current_temp(-0.1)
    assert thermometer.current_temp() == -0.1
    thermometer.current_temp(100.0)
    assert thermometer.current_temp() == 100.0
    thermometer.current_temp(0.0)
    assert thermometer.current_temp() == 0.0


def test_previous_temp(thermometer):
    """Test of Thermometer method previous_temp."""
    assert thermometer.previous_temp() == 0.0
    thermometer.current_temp(1.0)
    thermometer.current_temp(2.0)
    assert thermometer.previous_temp() == 1.0


def test_current_temp_fahrenheit(thermometer):
    """Test of Thermometer method current_temp_fahrenheit."""
    assert thermometer.current_temp_fahrenheit() == 32.0
    thermometer.current_temp(10.0)
    assert thermometer.current_temp_fahrenheit() == 50.0


def test_previous_temp_fahrenheit(thermometer):
    """Test of Thermometer method previous_temp_fahrenheit."""
    assert thermometer.previous_temp_fahrenheit() == 32.0
    thermometer.current_temp(10.0)
    thermometer.current_temp(11.0)
    assert thermometer.previous_temp_fahrenheit() == 50.0


def test_notification_temperature_threshold_boil(thermometer):
    """Test of Thermometer boil threshold notification."""
    # Reaching should notify
    thermometer(100.0)
    assert thermometer.notification() == "You have reached the boiling point."


def test_notification_temperature_threshold_boil_exceed(thermometer):
    """Exceeding should not notify"""
    thermometer(0.0)
    thermometer(100.1)
    assert thermometer.notification() is None


def test_notification_temperature_threshold_boil_decrease(thermometer):
    """Reaching based on decrease should notify"""
    thermometer(120.0)
    thermometer(100.0, decrease=True)
    assert thermometer.notification() == "You have reached the boiling point."


def test_notification_temperature_threshold_boil_increase(thermometer):
    """Reaching based on increase should notify"""
    thermometer(99.0, increase=True)
    thermometer(100.0)
    assert thermometer.notification() == "You have reached the boiling point."


def test_notification_temperature_threshold_boil_decrease_expect_increase(thermometer):
    """Reaching based on decrease with increase True should not notify"""
    thermometer(199.0, decrease=False, increase=True)
    thermometer(100.0)
    assert thermometer.notification() is None


def test_notification_temperature_threshold_boil_increase_expect_decrease(thermometer):
    """Reaching based on increase with decrease True should not notify"""
    thermometer(99.0, decrease=True, increase=False)
    thermometer(100.0)
    assert thermometer.notification() is None


def test_notification_temperature_threshold_boil_full_degree_increase(thermometer):
    """Reaching based on full degree increase should notify"""
    thermometer(99.0, full_degree=True)
    thermometer(100.0)
    assert thermometer.notification() == "You have reached the boiling point."


def test_notification_temperature_threshold_boil_full_degree_increase_expected_increase(
    thermometer,
):
    """Reaching based on full degree with expected increase should notify"""
    thermometer(99.0, decrease=False, increase=True, full_degree=True)
    thermometer(100.0)
    assert thermometer.notification() == "You have reached the boiling point."


def test_notification_temperature_threshold_boil_full_degree_increase_expected_decrease(
    thermometer,
):
    """Reaching based on full degree increase with expected decrease should not notify"""
    thermometer(98.0)
    thermometer(99.0, decrease=True, increase=False, full_degree=True)
    thermometer(100.0)
    assert thermometer.notification() is None


def test_notification_temperature_threshold_boil_full_degree_increase_expected_decrease_flux(
    thermometer,
):
    """Reaching based on full degree increase with expected decrease with temperature flux should
    not notify"""
    thermometer(101.0)
    thermometer(99.0, decrease=True, increase=False, full_degree=True)
    thermometer(100.0)
    assert thermometer.notification() is None


def test_notification_temperature_threshold_boil_full_degree_decrease_expected_increase(
    thermometer,
):
    """Reaching based on full degree decrease with expected increase should not notify"""
    thermometer(102.0)
    thermometer(101.0, decrease=False, increase=True, full_degree=True)
    thermometer(100.0)
    assert thermometer.notification() is None


def test_notification_temperature_threshold_boil_full_degree_decrease_expected_increase_flux(
    thermometer,
):
    """Reaching based on full degree decrease with expected increase with temperature flux should
    not notify"""
    thermometer(0.0)
    thermometer(101.0, decrease=False, increase=True, full_degree=True)
    thermometer(100.0)
    assert thermometer.notification() is None


def test_notification_temperature_threshold_boil_full_degree_decrease(thermometer):
    """Reaching based on full degree decrease should notify"""
    thermometer(101.0, full_degree=True)
    thermometer(100.0)
    assert thermometer.notification() == "You have reached the boiling point."

    # Reaching based on decimal degree decrease should not notify
    thermometer(100.1, full_degree=True)
    thermometer(100.0)
    assert thermometer.notification() is None


def test_notification_temperature_threshold_boil_full_degree_decrease_expected_decrease(
    thermometer,
):
    """Reaching based on full degree decrease when expected decrease and full degree True should
    notify"""
    thermometer(101.0, decrease=True, increase=False, full_degree=True)
    thermometer(100.0)
    assert thermometer.notification() == "You have reached the boiling point."

    # Reaching based on decimal degree decrease when full degree True should not notify
    thermometer(100.1, decrease=True, increase=False, full_degree=True)
    thermometer(100.0)
    assert thermometer.notification() is None


def test_notification_temperature_threshold_freeze(thermometer):
    """Test of Thermometer freeze threshold notification."""
    thermometer(0.0)
    assert thermometer.notification() is None

    thermometer(1.0)
    thermometer(0.0)
    assert thermometer.notification() == "You have reached the freezing point."


def test_notification_temperature_threshold_freeze_exceed(thermometer):
    """Exceeding should not notify"""
    thermometer(1.0)
    thermometer(-0.1)
    assert thermometer.notification() is None


def test_notification_temperature_threshold_freeze_decrease(thermometer):
    """Reaching based on decrease should notify"""
    thermometer(10.0, decrease=True)
    thermometer(0.0)
    assert thermometer.notification() == "You have reached the freezing point."


def test_notification_temperature_threshold_freeze_increase(thermometer):
    """Reaching based on increase should notify"""
    thermometer(-1.0, increase=True)
    thermometer(0.0)
    assert thermometer.notification() == "You have reached the freezing point."


def test_notification_temperature_threshold_freeze_decrease_expect_increase(
    thermometer,
):
    """Reaching based on decrease with increase True should not notify"""
    thermometer(1.0, decrease=False, increase=True)
    thermometer(0.0)
    assert thermometer.notification() is None


def test_notification_temperature_threshold_freeze_increase_expect_decrease(
    thermometer,
):
    """Reaching based on increase with decrease True should not notify"""
    thermometer(-1.0, decrease=True, increase=False)
    thermometer(0.0)
    assert thermometer.notification() is None


def test_notification_temperature_threshold_freeze_full_degree_increase(thermometer):
    """Reaching based on full degree increase should notify"""
    thermometer(-1.0, full_degree=True)
    thermometer(0.0)
    assert thermometer.notification() == "You have reached the freezing point."

    # Reaching based on decimal degree increase when full degree True should not notify
    thermometer(-0.5)
    thermometer(0.0)
    assert thermometer.notification() is None


def test_notification_temperature_threshold_freeze_full_degree_decrease(
    thermometer,
):
    """Reaching based on full degree decrease should notify"""
    thermometer(1.0, full_degree=True)
    thermometer(0.0)
    assert thermometer.notification() == "You have reached the freezing point."

    # Reaching based on decimal degree decrease when full degree True should not notify
    thermometer(0.5)
    thermometer(0.0)
    assert thermometer.notification() is None

    # Reaching based on decimal degree decrease when full degree True where prior point was
    # full degree should notify
    thermometer(1.0, full_degree=True)
    thermometer(0.5)
    thermometer(0.0)
    assert thermometer.notification() == "You have reached the freezing point."


def test_notification_temperature_threshold_freeze_full_degree_decrease_expected_decrease(
    thermometer,
):
    """Reaching based on full degree decrease when expected decrease should notify"""
    thermometer(1.0, decrease=True, increase=False, full_degree=True)
    thermometer(0.0)
    assert thermometer.notification() == "You have reached the freezing point."

    # Reaching based on decimal degree decrease when expected decrease and full degree True should
    # not notify
    thermometer(0.5)
    thermometer(0.0)
    assert thermometer.notification() is None


def test_notification_temperature_threshold_freeze_full_degree_decrease_expected_increase(
    thermometer,
):
    """Reaching based on full degree decrease should notify"""
    thermometer(1.0, decrease=False, increase=True, full_degree=True)
    thermometer(0.0)
    assert thermometer.notification() is None

    # Reaching based on decimal degree decrease when full degree True should not notify
    thermometer(0.5)
    thermometer(0.0)
    assert thermometer.notification() is None
