"""Various helper functions to manipulate timee-series data."""
import glob
import os
from datetime import datetime, timedelta
from typing import Any, Dict, List, Optional, Tuple

import numpy as np
import pandas as pd


def get_first_or_default(lst: List[Any], default: Any):
    """Return the first object in the given list or the given default value if the list is empty."""
    return next(iter(lst), default)


def add_weekdays(dataframe):
    """Add a column containing either `Working Day` or `Weekend`."""
    dataframe["day_type"] = np.where(dataframe.index.dayofweek >= 5, "Weekend", "Working Day")


def add_day_fraction(dataframe):
    """
    Add a column containing a float representation of the time-of-day.

    00:00:00 -> 0.0
    23:59:59 -> 1.0
    """
    dataframe["day_fraction"] = dataframe.index.to_series(keep_tz=True).apply(_day_fraction)


def _day_fraction(timestamp):
    start_of_day = timestamp.floor("D")
    diff = timestamp - start_of_day
    return diff.total_seconds() / (60 * 60 * 24)


def add_week_fraction(dataframe):
    """
    Add a column containing a float representation of the time-in-the-week.

    Monday 00:00:00 -> 0.0
    Sunday 23:59:59 -> 1.0
    """
    dataframe["week_fraction"] = _week_fraction(dataframe.index.to_series(keep_tz=True))


def _week_fraction(timestamp):
    start_of_week = timestamp - pd.to_timedelta(timestamp.dt.dayofweek, "D")
    start_of_week = start_of_week.dt.floor("D")
    diff = timestamp - start_of_week
    return diff.dt.total_seconds() / (60 * 60 * 24 * 7)


def add_year_fraction(dataframe):
    """
    Add a column containing a float representation of the time-in-the-year.

    1st January 00:00:00 -> 0.0
    31st December 23:59:59 -> 1.0
    """
    dataframe["year_fraction"] = _year_fraction(dataframe.index.to_series(keep_tz=True))


def _year_fraction(timestamp):
    start_of_year = timestamp - pd.to_timedelta(timestamp.dt.dayofyear - 1, "D")
    start_of_year = start_of_year.dt.floor("D")
    diff = timestamp - start_of_year
    result = diff.dt.total_seconds() / (60 * 60 * 24 * 365)
    result[timestamp.dt.is_leap_year] = diff.dt.total_seconds() / (60 * 60 * 24 * 366)
    return result


def load_mock_data(folder: str) -> List[Tuple[str, Optional[str]]]:
    """Load all **/*.json files in a folder as (url, text) tuples for use in requsts_mock."""
    mocks: List[Tuple[str, Optional[str]]] = []
    for file in glob.glob(folder + "/**/*.json", recursive=True):
        filename = os.path.basename(file)
        url = "https://" + filename.replace("|", "/").replace(".json", "")
        with open(file, "r", encoding="utf-8") as _f:
            text = _f.read()
            mocks.append((url, text))
    return mocks


def calculate_continuous_error_states(df: pd.DataFrame, window: timedelta, column: str = "err") -> pd.DataFrame:
    """
    Add a column based on the chosen column whith the value `1` if an error has persisted for longer than the given window.

    Parameters
    ----------
    df : pd.DataFrame
        The DataFrame with input data. Index must be DatetimeIndex.
    window : timedelta
        The time window for which an error has to persist to trigger.
    column : str
        The name of the column containing the error state, by default "err"

    Returns
    -------
    pd.DataFrame
        A copy of the original DataFrame with the new column.
    """
    assert isinstance(df.index, pd.core.indexes.datetimes.DatetimeIndex), "Index of dataframe must be of type DatetimeIndex."

    local_df = df.copy()
    result_col = column + "_continuous"
    local_df[result_col] = 0
    if len(local_df) < 2:
        return local_df
    err = (local_df[column] >= 0.5).astype(int)
    err_diff = err - err.shift(1)
    status_changes = err_diff[err_diff != 0][1:]
    if len(status_changes) == 0:
        if all(local_df[column]):  # All rows indicate error.
            if local_df.index.max() - local_df.index.min() >= window:
                local_df[result_col] = 1
        return local_df
    if status_changes[0] == -1:  # First rows indicate error
        start = local_df.index.min()
        end = status_changes.index.min()
        if end - start >= window:
            local_df.loc[start:end, result_col][:-1] = 1
        status_changes = status_changes[1:]
    for start, end in zip(status_changes.index[::2], status_changes.index[1::2]):  # Inervals indicating error
        if end - start >= window:
            local_df.loc[start:end, result_col][:-1] = 1
    if len(status_changes) % 2:  # Last rows indicate error
        start = status_changes.index.max()
        end = local_df.index.max()
        if end - start >= window:
            local_df.loc[start:end, result_col] = 1
    return local_df


def calculate_error_fraction(df: pd.DataFrame, column: str = "err") -> float:  # pylint: disable=R0914
    """Calculate the time-based fraction of error states in the given time-series DataFrame.

    Parameters
    ----------
    df : pd.DataFrame
        The DataFrame with input data.
    column : str, optional
        The name of the column containing the error state, by default "err"

    Returns
    -------
    float
        The time-based fraction of error states during the whole DataFrame period.
    """
    if len(df) == 0:
        return 0

    if len(df) == 1:
        return df[column][0]

    err = (df[column] >= 0.5).astype(int)
    status_changes = err - err.shift(1)
    status_changes = status_changes[status_changes != 0]

    if len(status_changes) == 1:
        return err[0]

    if status_changes[1] == -1:
        status_changes[0] = 1
    else:
        status_changes = status_changes[1:]

    if status_changes[-1] == 1:
        cumulative_error_time = (status_changes[1::2].index - status_changes[:-1:2].index).sum().total_seconds()
        cumulative_error_time += (df.index.max() - status_changes.index.max()).total_seconds()
    else:
        cumulative_error_time = (status_changes[1::2].index - status_changes[::2].index).sum().total_seconds()

    return cumulative_error_time / (df.index.max() - df.index.min()).total_seconds()


def non_null_duration(series: pd.Series) -> pd.Series:
    """Calculate the duration a given Series has been not null.

    Parameters
    ----------
    series : pd.Series
        The Series with input data.

    Returns
    -------
    pd.Series
        The Series with the duration the input as been not null. Resets after each null state.
    """
    values: Dict[datetime, float] = {}
    start: Optional[datetime] = None
    for timestamp, value in series.iteritems():
        current = value != 0
        if not start and current:
            start = timestamp
            values[timestamp] = 0.0
        if start and current:
            values[timestamp] = (timestamp - start).total_seconds()
        if not start and not current:
            values[timestamp] = 0.0
        if start and not current:
            values[timestamp] = (timestamp - start).total_seconds()
            start = None
    return pd.Series(values, name=f"{series.name}_nn_dur")


def non_null_fraction(series: pd.Series, window_length: timedelta) -> pd.Series:
    """Calculate the fraction a Series has been not null in a given rolling window.

    Parameters
    ----------
    series : pd.Series
        The input Series.
    window_length : timedelta
        The time-length of the window to analyse.

    Returns
    -------
    pd.Series
        The Series with the fraction the input Series has been not null during each rolling window.
    """
    values: Dict[datetime, float] = {}
    start: Optional[datetime] = None
    for timestamp, value in series.iteritems():
        current = value != 0
        if not start and current:
            start = timestamp
            values[timestamp] = 0.0
        if start and current:
            duration = (timestamp - start).total_seconds()
            if duration >= window_length.total_seconds():
                values[timestamp] = 1.0
            else:
                values[timestamp] = duration / window_length.total_seconds()
        if not start and not current:
            values[timestamp] = 0.0
        if start and not current:
            duration = (timestamp - start).total_seconds()
            if duration >= window_length.total_seconds():
                values[timestamp] = 1.0
            else:
                values[timestamp] = duration / window_length.total_seconds()
            start = None
    return pd.Series(values, name=f"{series.name}_nn_frac")


def count_errors(df: pd.DataFrame, column: str = "err") -> int:
    """Count the number of error occcurances in the given dataframe."""
    # counting distinct error states:
    # 000001111000110000111111110000 returns 3
    #      1      2     3
    mask0 = df[column].gt(0.5)
    mask2 = df[column].ne(df[column].shift(1))
    sum_of_errorstates = (mask2 & mask0).cumsum()[-1]
    return int(sum_of_errorstates)


def iso8601_duration(value: timedelta):
    """Convert a datetime.timedelta to a ISO8601 duration."""
    seconds = value.total_seconds()
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    days, hours, minutes = map(int, (days, hours, minutes))
    seconds = round(seconds, 6)

    formatted_string = "P"
    if days:
        formatted_string += f"{days}D"
    if any([hours, minutes, seconds]):
        formatted_string += "T"
        if hours:
            formatted_string += f"{hours}H"
        if minutes:
            formatted_string += f"{minutes}M"
        if seconds:
            formatted_string += f"{seconds}S"

    return formatted_string
