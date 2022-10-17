"""Thermometer that receives a notification on when threshold is met
    via a full degree temperature change.
"""
from thermometerb import Thermometer

temp_range = [1.5, 1.0, 0.5, 0.0, -0.5, 0.0, -0.5, 0.0, 0.5, 0.0]
thermometer = Thermometer(full_degree=True)

for temp in temp_range:
    notice_dict = thermometer(temp)
    if thermometer.notification():
        notice = (
            f"{notice_dict['notification']} {notice_dict['celsius']}ºC / "
            f"{notice_dict['fahrenheit']}ºF"
        )
        print(notice)
