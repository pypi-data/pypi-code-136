"""Thermometer that receives a notification on when threshold is met
    via decreasing temperature.
"""
from thermometerb import Thermometer

temp_range = [99.0, 97.0, 98.0, 100.0, 101.5, 20.0, 5.0, 0.0, -10.0, -1.0, 0.0, 1.0]
thermometer = Thermometer(decrease=True)

for temp in temp_range:
    thermometer(temp)
    if thermometer.notification():
        notice = (
            f"{thermometer.notification()} {thermometer.current_temp()}ºC / "
            f"{thermometer.current_temp_fahrenheit()}ºF"
        )
        print(notice)
