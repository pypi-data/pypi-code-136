import pandas as pd
import numpy as np
from numba import njit

from swe2hs import __version__

__author__ = "Johannes Aschauer"
__license__ = "GPL-3.0-or-later"

ONE_HOUR = np.timedelta64(1, 'h')

UNIT_FACTORS = {
    'mm': 1e-3,
    'cm': 1e-2,
    'dm': 1e-1,
    'm': 1,
    'km': 1e3,
}

def _get_unit_conversion_factor(
    input_unit,
    required_unit,
):
    """
    Multiply input unit with the returned factor in order to get 
    the required unit.
    """
    return UNIT_FACTORS[input_unit] / UNIT_FACTORS[required_unit]


@njit
def continuous_timedeltas(dr):
    """
    Check for continuity on dates
    
    Parameters
    ----------
    dr : 1D :class:`numpy.ndarray` with :class:`numpy.datetime64`  dtype
        Input date range.
    
    Returns
    -------
    continuous : bool
        Whether the datetime array is evenly spaced.
    resolution : float
        The time resolution in hours.
    """
    if len(dr) <= 1:
        continuous = True
        resolution = 24.0  # hard coded resolution in case of only 1 day length
    else:
        # np.gradient not working in numba
        tdeltas = np.zeros(len(dr)-1, dtype='timedelta64[ns]')
        for i in range(len(dr)-1):
            tdeltas[i] = dr[i+1]-dr[i]

        # check if all deltas are equal
        continuous = np.all(tdeltas == tdeltas[0])
        # get time resolution in hours.
        # one hour timedelta has to be moved outside numba, see this issue for
        # reference: https://github.com/numba/numba/issues/1750
        resolution = tdeltas[0] / ONE_HOUR

    return continuous, resolution


@njit
def continuous_timedeltas_in_nonzero_chunks(
    dr,
    start_idxs,
    stop_idxs
):
    """
    Check that every non-zero data chunk has continuous dates and same resolution.
    
    Parameters
    ----------
    dr : 1D :class:`numpy.ndarray` with :class:`numpy.datetime64`  dtype
        Input date range.
    start_idxs: 1D :class:`numpy.ndarray`
        Indices where a nonzero chunk begins.
    stop_idxs: 1D :class:`numpy.ndarray`
        Indices where a nonzero chunk ends.
    
    Returns
    -------
    continuous : bool
        Whether the chunks are evenly spaced with equal resolution.
    resolution : float
        The time resolution in hours.
    """

    cont = np.zeros(len(start_idxs), dtype='bool') # is chunk continuous
    res = np.zeros(len(start_idxs)) # chunk time resolutions
    for i, (start, stop) in enumerate(zip(start_idxs, stop_idxs)):
        cont[i], res[i] = continuous_timedeltas(dr[start:stop])

    continuous = np.all(np.array([np.all(cont), np.all(res==res[0])]))
    resolution = res[0]
    return continuous, resolution


@njit
def get_nonzero_chunk_idxs(arr):
    """
    Return start and stop indices of consecutive nonzero chunks in arr.
    A nonzero chunk is a slice in arr of values not zero. Nans are 
    treated as nonzeros. The slices which are retured from this function
    include one leading and one trailing zero since the func:`swe2hs_snowpack_evolution` 
    wants an input SWE array to start and end with zero. Exceptions
    are when arr does not start and/or end with zero (then the first start
    and/or last stop index is not pointing to a zero).
    Note that when you slice `arr` with `arr[start:stop]` the stop value is 
    non-inclusive (https://stackoverflow.com/a/509295).
    
    Parameters
    ----------
    arr : 1D :class:`numpy.ndarray` of floats
        input data
    Returns
    -------
    start_idxs: 1D :class:`numpy.ndarray`
        Indices where a nonzero chunk begins.
    stop_idxs: 1D :class:`numpy.ndarray`
        Indices where a nonzero chunk ends.
    """

    starts = []
    stops = []

    # if first value of arr is not zero, set 0 as first start_idx
    if arr[0] != 0:
        starts.append(0)

    for i in range(len(arr)):
        if i < len(arr)-1:
            if arr[i] == 0. and arr[i+1]!=0:
                starts.append(i)
        if i > 0:
            if arr[i] == 0. and arr[i-1]!=0:
                stops.append(i)

    # if last value not zero, set last idx of arr as last stop_idx
    if len(stops) < len(starts):
        stops.append(len(arr))

    # cast to numpy arrays:
    start_idxs = np.array(starts)
    stop_idxs = np.array(stops)

    # get length of the longest nonzero chunk:
    if len(stop_idxs) > 0:
        chunk_lengths = stop_idxs - start_idxs
        max_chunk_length = np.max(chunk_lengths)
    else:
        max_chunk_length = 0

    return start_idxs, stop_idxs, max_chunk_length


@njit
def _get_split_indices_based_on_date(month_input, split_month, split_day):
    """
    Return split locations for a specific month-day combination on a 
    month daterange array.

    Numba does not yet allow to use np.datetime64 types in guvectorized functions.
    Therefore this function uses the months from a continuous daterange in order
    to get indices of split locations.

    Parameters
    ----------
    month_input : 1D :class:`numpy.ndarray` of ints
        months from a continuous daterange
    date : str
        Split date of the form 'MM-DD'

    Returns
    -------
    1D :class:`numpy.ndarray` of ints
        Indices where the array should be split.
    """
    month_history = np.zeros(split_day+1)

    split_idxs = []

    for i, month in enumerate(month_input):
        month_history[-1] = month  # last day in month_history is current day
        if i == 0 or (month_history[0] != split_month and np.all(month_history[1:] == split_month)):
            split_idxs.append(i)
        month_history = np.roll(month_history, -1)

    split_idxs.append(len(month_input))

    return np.array(split_idxs)


@njit
def get_zeropadded_gap_idxs(
    arr,
    require_leading_zero,
):
    """
    Get indices of Nan data-gaps in arr that are surrounded or followed by
    zeros.
    
    Parameters
    ----------
    arr : 1D :class:`numpy.ndarray` of floats
        input data
    require_leading_zero : bool
        Whether to include gaps that do not have a leading zero but have a 
        trailing zero.
    
    Returns
    -------
    zeropadded_gap_idxs : 1D :class:`numpy.ndarray` of bools
    """
    zeropadded_gap_idxs = np.zeros(len(arr), dtype='bool')

    start_idxs = []
    stop_idxs = []

    gap = False
    start = len(arr)
    for i in range(len(arr)):
        if i == 0 and np.isnan(arr[i]):
            start = i
            gap = True

        if i > 0:
            if require_leading_zero:
                if np.isnan(arr[i]) and arr[i-1] == 0:
                    start = i
                    gap = True
            else:
                if np.isnan(arr[i]) and not np.isnan(arr[i-1]):
                    start = i
                    gap = True

        if i < len(arr)-1:
            if np.isnan(arr[i]) and arr[i+1] == 0:
                if gap:
                    start_idxs.append(start)
                    stop_idxs.append(i+1)

        if not np.isnan(arr[i]):
            gap=False

    # if last value also nan, set last idx of arr as last stop_idx
    if gap:
        if len(start_idxs)>0 and start != start_idxs[-1]:
            start_idxs.append(start)
            stop_idxs.append(len(arr))
        elif start < len(arr):
            start_idxs.append(start)
            stop_idxs.append(len(arr))

    if len(start_idxs)>0:
        for start_i, stop_i in zip(start_idxs, stop_idxs):
            zeropadded_gap_idxs[start_i:stop_i] = True

    return zeropadded_gap_idxs


@njit
def get_small_gap_idxs(
    arr,
    dates,
    max_gap_length,
):
    """
    Create a boolean mask for valid small gaps.
    Gap needs to be surrounded by values
    Dates need to be continuous between day before gap and day after gap
    
    Parameters
    ----------
    arr : 1D :class:`numpy.ndarray` of floats
        input data
    dates : 1D :class:`numpy.ndarray` of :class:`numpy.datetime64`  dtype
        timestamps of the snow depth observations.
    max_gap_length : int
        Only gaps shorter or equal max_gap_length are valid.
    
    Returns
    -------
    small_gap_idxs : 1D :class:`numpy.ndarray` of bools
    """
    small_gap_idxs = np.zeros(len(arr), dtype='bool')

    start_idxs = []
    stop_idxs = []

    gapl = 0  # counter of active gap length
    active_gap = False
    valid_gap = False

    start = len(arr)
    for i in range(len(arr)):
        if active_gap:
            gapl = gapl+1

        if gapl > max_gap_length:
            valid_gap = False

        if i > 0:
            if not np.isnan(arr[i-1]) and np.isnan(arr[i]):
                start = i
                valid_gap=True
                active_gap = True

        if i < len(arr):
            if np.isnan(arr[i-1]) and not np.isnan(arr[i]):
                if valid_gap and continuous_timedeltas(dates[start-1:i+1])[0]:
                    start_idxs.append(start)
                    stop_idxs.append(i)

                gapl = 0
                active_gap = False
                valid_gap=False


    if len(start_idxs)>0:
        for start_i, stop_i in zip(start_idxs, stop_idxs):
            small_gap_idxs[start_i:stop_i] = True

    return small_gap_idxs


def fill_small_gaps(
    arr,
    dates,
    max_gap_length,
    method='linear'
):
    """
    Interpolate small gaps in arr.
    No extrapolation: data points before and after gap needed.
    Date continuity in the filled gaps + leading and trailing data point is
    ensured.

    Parameters
    ----------
    arr : 1D :class:`numpy.ndarray`
        Snow depth data.
    dates : 1D :class:`numpy.ndarray` of :class:`numpy.datetime64`  dtype
        timestamps of the snow depth observations.
    max_gap_length : int
        Only gaps shorter or equal max_gap_length are interpolated.
    method : str, optional
        Interpolation method which will be passed to 
        :func:`pandas.Series.interpolate`. The default is 'linear'.
    
    Returns
    -------
    arr_intepolated : 1D :class:`numpy.ndarray` 
        Snow depth data with filled gaps.
    """
    valid_gap_mask = get_small_gap_idxs(arr, dates, max_gap_length)
    interpolated = pd.Series(arr).interpolate(method=method).to_numpy()
    arr_interpolated = np.where(valid_gap_mask, interpolated, arr)
    return arr_interpolated