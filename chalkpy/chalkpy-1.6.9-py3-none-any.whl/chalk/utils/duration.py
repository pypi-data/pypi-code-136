import datetime
from typing import Literal, Optional, Union

import numpy as np
import pandas as pd

# Duration is used to describe time periods in
# natural langauge. To specify using natural
# language, write the count of the unit you would
# like, followed by the representation of the unit.
#
# Chalk support the following units:
# | Signifier | Meaning  |
# | --------- | -------- |
# | w         | Weeks    |
# | d         | Days     |
# | h         | Hours    |
# | m         | Minutes  |
# | s         | Seconds  |
#
# Examples
# | Signifier   | Meaning                           |
# | ----------- | --------------------------------- |
# | "10h"       | 10 hours                          |
# | "1w 2m"     | 1 week and 2 minutes              |
# | "1h 10m 2s" | 1 hour, 10 minutes, and 2 seconds |
#
# Read more at https://docs.chalk.ai/docs/duration
Duration = str

# A schedule defined using the unix-cron
# string format (* * * * *).
# Values are given in the order below:
#
# | Field        | Values |
# | ------------ | ------ |
# | Minute       | 0-59   |
# | Hour         | 0-23   |
# | Day of Month | 1-31   |
# | Month        | 1-12   |
# | Day of Week  | 0-6    |
CronTab = str
ScheduleOptions = Optional[Union[CronTab, Duration, Literal[True]]]

_MAX_PD_DT = pd.to_datetime(np.datetime64(1 << 63 - 1, "ns"), utc=True)
_MIN_PD_DT = pd.to_datetime(np.datetime64(-(1 << 63 - 1), "ns"), utc=True)

_TIME_ZERO = datetime.datetime.utcfromtimestamp(0).replace(tzinfo=datetime.timezone.utc)


def convert_datetime_to_pd(dt: datetime.datetime):
    dt_as_utc = dt.astimezone(datetime.timezone.utc)
    try:
        return pd.to_datetime(dt_as_utc, utc=True)
    except ValueError:
        if dt > _TIME_ZERO:
            return _MAX_PD_DT
        else:
            return _MIN_PD_DT
