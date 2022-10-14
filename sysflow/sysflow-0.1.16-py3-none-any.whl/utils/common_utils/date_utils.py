# -*- coding: utf-8 -*-
# File              : date_utils.py
# Author            : Jiahao Yao
# Email             : jiahaoyao.math@gmail.com
# Date              : 10.13.2022
# Last Modified Date: 10.13.2022
# Last Modified By  : Jiahao Yao
#
# This file is part of the VCML codebase
# Distributed under MIT license
#
# selecting functions

from datetime import datetime

def get_difference_between_dates(date1, date2):
    """the difference between two dates in days

    Args:
        date1 (datetime): the first date
        date2 (datetime): the second date

    Returns:
        str: the difference between two dates in years/months/days
    """
    date_diff = abs(date1-date2)
    avgyear = 365.2425        # pedants definition of a year length with leap years
    avgmonth = 365.2425/12.0  # even leap years have 12 months
    years, remainder = divmod(date_diff.days, avgyear)
    years, months = int(years), int(remainder // avgmonth)
    days = int(remainder - avgmonth * months)
    
    year_str = f'{years} year' if years == 1 else f'{years} years'
    month_str = f'{months} month' if months == 1 else f'{months} months'
    day_str = f'{days} day' if days == 1 else f'{days} days'
    
    if years > 0:
       out = f'{year_str} {month_str} {day_str}'
    elif months > 0:
        out = f'{month_str} {day_str}'
    else:
        out = f'{day_str}'
    return out 
