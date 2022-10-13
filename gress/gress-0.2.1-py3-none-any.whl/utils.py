#  Created byMartin.cz
#  Copyright (c) Martin Strohalm. All rights reserved.

import math
from .enums import *


def format_time(seconds, template=None, units=False):
    """Formats time according to given seconds."""
    
    # get days
    days = 0
    if template and "{d" in template:
        days = int(seconds / DAY)
        seconds %= DAY
    
    # get hours
    hours = 0
    if template and "{h" in template:
        hours = int(seconds / HOUR)
        seconds %= HOUR
    
    # get minutes
    minutes = 0
    if template and "{m" in template:
        minutes = int(seconds / MINUTE)
        seconds %= MINUTE
    
    # make template according to current range
    if not template:
        
        if days:
            template = TIME_DHMS_U if units else TIME_DHMS
        elif hours:
            template = TIME_HMS_U if units else TIME_HMS
        elif minutes:
            template = TIME_MS_U if units else TIME_MS
        else:
            template = TIME_S_U if units else TIME_S
    
    # format time
    return template.format(d=int(days), h=int(hours), m=int(minutes), s=int(seconds))


def format_power(value, template="{:.2f}", prefixes=PREFIXES, step=1000):
    """Formats value with prefixes according to value power."""
    
    # check prefixes
    if not prefixes:
        return template.format(value) if template else str(value)
    
    # init
    scaled = 0
    power = 0
    
    # scale value
    if value >= 2e-6:
        power = int(math.log(value, step))
        scaled = value / step**power
    
    # format value
    scaled = template.format(scaled) if template else scaled
    return "%s%s" % (scaled, prefixes[power])
