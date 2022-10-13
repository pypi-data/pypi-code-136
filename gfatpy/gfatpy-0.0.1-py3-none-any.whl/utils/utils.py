#!/usr/bin/env python
# -*- coding: utf8 -*-

"""
various utilities
"""

from __future__ import print_function
from __future__ import division
from __future__ import absolute_import

import re
import os
import sys
from typing import Callable


import scipy as sp
import numpy as np
import pandas as pd
import datetime as dt
from scipy import stats
from loguru import logger


"""
"""


""" NUMERICAL
"""


def normalize(x):  # , exclude_inf=True):
    """Normalize data in a 1-D array: [0, 1]

    Args:
        x ([type]): [description]
        exclude_inf (bool, optional): [description]. Defaults to True.

    Returns:
        [type]: [description]
    """

    n = np.zeros(len(x)) * np.nan
    try:
        idx_fin = np.logical_and(x != -np.inf, x != np.inf)
        x0 = x[idx_fin]
        n[idx_fin] = (x0 - np.nanmin(x0)) / (np.nanmax(x0) - np.nanmin(x0))
    except Exception as e:
        print("ERROR in normalize. %s" % str(e))

    return n


def interp_nan(y, last_value=0):
    """

    Parameters
    ----------
    y: array
        1d array with nans

    Returns
    -------
    y: array
        interpolated array

    """
    # interpolation fails if values at extreme of array are nan
    if np.isnan(y[-1]):
        y[-1] = last_value
    if np.isnan(y[0]):
        y[0] = last_value

    # bool of nans
    nans = np.isnan(y)
    # funcion lambda que genera un vector de indices a partir de un array logico
    x = lambda z: z.nonzero()[0]
    # def interpolate function
    f = sp.interpolate.interp1d(x(~nans), y[~nans], kind="cubic")
    # do interpolation
    y[nans] = f(x(nans))

    return y


def linear_regression(x, y):
    """
    y = a*x + b

    :param x: abscisa. 1-D array.
    :param y: ordenada. 1-D array.
    :return:
    """
    try:
        x = np.asarray(x)
        y = np.asarray(y)

        # Clean data
        idx = np.logical_and(~np.isnan(x), ~np.isnan(y))
        x_train = x[idx]
        y_train = y[idx]

        # Regression
        lr = stats.linregress(x_train, y_train)
        slope = float(lr.slope)
        intercept = float(lr.intercept)
        rvalue = float(lr.rvalue)
    except Exception as e:
        print("ERROR. In linear_regression. %s" % str(e))
        slope = np.nan
        intercept = np.nan
        rvalue = np.nan

    return slope, intercept, rvalue


def linrest(x, y):
    n = len(y)
    dofreedom = n - 2
    z, _ = np.polyfit(x, y, 1, cov=True)
    p = np.poly1d(z)
    yp = p(x)  # predicted y values based on fit
    slope = z[0]
    intercept = z[1]
    r2 = np.corrcoef(x, y)[0][1] ** 2
    # regression_ss = np.sum( (yp-np.mean(y))**2)
    residual_ss = np.sum((y - yp) ** 2)
    slope_pm = np.sqrt(residual_ss / (dofreedom * np.sum((x - np.mean(x)) ** 2)))
    intercept_pm = slope_pm * np.sqrt(np.sum(x**2) / n)
    # s = np.sqrt(residual_ss/dofreedom)
    # F = regression_ss/s**2

    return slope, slope_pm, intercept, intercept_pm, r2


def residuals(meas, pred):
    """
    Residuals: J = (1/n)*sum{ [(meas-pred)/std(meas)]**2 }

    :param meas: 1-D array. measurement
    :param pred: 1-D array. prediction
    :return:
    """
    n = len(meas)
    try:
        sigma = np.nanstd(meas)
        J = np.nansum(((meas - pred) / sigma) ** 2) / n
    except Exception as e:
        print("ERROR. In cost_function %s" % str(e))
        J = np.nan
    return J


"""
ARRAYS
"""


def unique(array):
    """
    Get unique and non-nan values of a 1D array
    :param array:
    :return: array of unique values
    """
    try:
        unq = np.unique(array[~np.isnan(array)])
    except Exception as e:
        unq = np.nan
        print("Error: getting unique values of an array. %s" % str(e))

    return unq


def find_nearest_1d(array, value):  # TODO: Isn't this the same as np.searchsorted?
    """
    Find nearest value in a 1-D array
    :param array:
    :param value:
    :return:
    """
    array = np.asarray(array)
    if np.logical_and(~np.isnan(value), ~np.isnan(array).all()):
        idx = (np.abs(array - value)).argmin()
        nearest = array[idx]
    else:
        idx = np.nan
        nearest = np.nan

    return idx, nearest


"""
OTHERS
"""


def check_dir(dir_name):
    """
    Check if a directory exists and is writable
    """

    return os.access(dir_name, os.W_OK)


def welcome(prog_name, prog_version):
    """print informations about the code"""

    print("starting {} v{}".format(prog_name, prog_version))
    print()


def print_progress(iteration, total, prefix="", suffix="", decimals=2, bar_length=100):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : number of decimals in percent complete (Int)
        bar_length  - Optional  : character length of bar (Int)
    """

    filled_length = int(round(bar_length * iteration / float(total)))
    percents = round(100.00 * (iteration / float(total)), decimals)
    progress_bar = "*" * filled_length + "-" * (bar_length - filled_length)
    sys.stdout.write(
        "\r%s |%s| %s%s %s" % (prefix, progress_bar, percents, "%", suffix)
    )
    sys.stdout.flush()
    if iteration == total:
        sys.stdout.write("\n")
        sys.stdout.flush()


def numpy_to_datetime(numpy_date):
    """
    Converts a numpy datetime64 object to a python datetime object
    Input:
      date - a np.datetime64 object
    Output:
      DATE - a python datetime object
    """
    # timestamp = ((date - np.datetime64('1970-01-01T00:00:00'))
    #             / np.timedelta64(1, 's'))

    try:
        timestamp = dt.datetime.utcfromtimestamp(numpy_date.tolist() / 1e9)
    except Exception as e:
        timestamp = None
        print(str(e))

    return timestamp


def datetime_np2dt(numpy_date):
    """
    Converts a numpy datetime64 object to a python datetime object
    Input:
      date - a np.datetime64 object
    Output:
      DATE - a python datetime object
    """
    # timestamp = ((date - np.datetime64('1970-01-01T00:00:00'))
    #             / np.timedelta64(1, 's'))

    try:
        timestamp = pd.Timestamp(numpy_date).to_pydatetime()
    except Exception as e:
        timestamp = None
        logger.error(str(e))
        raise e
    return timestamp


def str_to_datetime(date_str: str) -> dt.datetime:
    """

    Parameters
    ----------
    date_str: str
        date in string format (see possible formats below)

    Returns
    -------

    """
    assert isinstance(date_str, str), "date_str must be String Type"

    formats = [
        (r"\d{4}\d{2}\d{2}T\d{2}\d{2}\d{2}", "%Y%m%dT%H%M%S"),
        (r"\d{4}\d{2}\d{2}_\d{2}\d{2}\d{2}", "%Y%m%d_%H%M%S"),
        (r"\d{4}\d{2}\d{2}T\d{2}\d{2}", "%Y%m%dT%H%M"),
        (r"\d{4}\d{2}\d{2}_\d{2}\d{2}", "%Y%m%d_%H%M"),
        (r"\d{4}\d{2}\d{2}T\d{2}", "%Y%m%dT%H"),
        (r"\d{4}\d{2}\d{2}_\d{2}", "%Y%m%d_%H"),
        (r"\d{4}\d{2}\d{2}", "%Y%m%d"),
        (r"\d{4}\d{2}", "%Y%m"),
        (r"\d{4}", "%Y"),
    ]

    i = 0
    match = False
    date_format = ""
    date_dt = None
    while not match:
        if i < len(formats):
            candidate = re.search(formats[i][0], date_str)
            if candidate is not None:
                date_format = formats[i][1]
                match = True
            else:
                i += 1
        else:
            match = True
    if date_format is not None:
        try:
            date_dt = dt.datetime.strptime(date_str, date_format)
        except Exception as e:
            print(f"{date_str} has more complex format than found ({date_format})")
            raise NotImplementedError(e.with_traceback)
    else:
        raise RuntimeError(f"Cannot understand the format of {date_str}")

    return date_dt


def datetime_pytom(d, t):
    """
    Input
        d   Date as an instance of type datetime.date
        t   Time as an instance of type datetime.time
    Output
        The fractional day count since 0-Jan-0000 (proleptic ISO calendar)
        This is the 'datenum' datatype in matlab
    Notes on day counting
        matlab: day one is 1 Jan 0000
        python: day one is 1 Jan 0001
        hence an increase of 366 days, for year 0 AD was a leap year
    """
    dd = d.toordinal() + 366
    tt = dt.timedelta(hours=t.hour, minutes=t.minute, seconds=t.second)
    tt = dt.timedelta.total_seconds(tt) / 86400
    return dd + tt


def datetime_mtopy(datenum):
    """
    Input
        The fractional day count according to datenum datatype in matlab
    Output
        The date and time as a instance of type datetime in python
    Notes on day counting
        matlab: day one is 1 Jan 0000
        python: day one is 1 Jan 0001
        hence a reduction of 366 days, for year 0 AD was a leap year
    """
    ii = dt.datetime.fromordinal(int(datenum) - 366)
    ff = dt.timedelta(days=datenum % 1)
    return ii + ff


def parse_datetime(date: dt.datetime | dt.date | str) -> dt.datetime:
    """The general way to cast strigs or datetimes to datetime python type

    Args:
        date (dt.datetime | str): This could be one of the supported formats.
        The recommended one is ISO8601.

    Returns:
        dt.datetime: Python datetime format.
    """

    if isinstance(date, dt.datetime):
        return date
    elif isinstance(date, dt.date):
        return dt.datetime(date.year, date.month, date.day)
    elif isinstance(date, str):
        try:
            return dt.datetime.fromisoformat(date)
        except ValueError:
            return str_to_datetime(date)
    else:
        raise ValueError(f"{date} is not a valid date")


# Plot 1:1 line
# axes.plot(axes.xaxis.axes.get_xlim(),axes.xaxis.axes.get_xlim())
def create_linear_interpolator(
    x: np.ndarray, y: np.ndarray
) -> Callable[[np.ndarray], np.ndarray]:
    def interpolator(_x):
        return np.interp(_x, x, y)

    return interpolator


def moving_average(a: np.ndarray, window_size: int = 3) -> np.ndarray:
    return sp.ndimage.uniform_filter(a, size=(window_size, 1), mode="nearest")
