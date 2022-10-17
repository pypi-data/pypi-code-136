"""Setup basic Thermometer instance as a text fixture"""
import pytest
from src.thermometerb.thermometer import Thermometer


@pytest.fixture()
def thermometer():
    """Thermometer instance for testing"""
    return Thermometer()
