"""Basic Thermometer that prints out when it hits the
    default boiling and freezing points.
"""
from thermometerb import Thermometer

temp_range = [99.0, 97.0, 98.0, 100.0, 101.5, 20.0, 5.0, 0.0, -10.0]
thermometer = Thermometer()

for temp in temp_range:
    thermometer(temp)
    if thermometer.notification():
        print(thermometer.notification())
