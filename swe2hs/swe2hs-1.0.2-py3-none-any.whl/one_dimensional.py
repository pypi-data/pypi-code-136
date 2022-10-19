import numpy as np
import pandas as pd
import xarray as xr
from numba import njit

from ._core import swe2hs_snowpack_evolution

from .utils import (
    continuous_timedeltas_in_nonzero_chunks,
    fill_small_gaps,
    get_nonzero_chunk_idxs,
    get_zeropadded_gap_idxs,
    _get_unit_conversion_factor,
    UNIT_FACTORS,
    )

from ._default_model_parameters import *

from swe2hs import __version__

__author__ = "Johannes Aschauer"
__license__ = "GPL-3.0-or-later"


def _raise_nans_error_message(
    ignore_zeropadded_gaps,
    ignore_zerofollowed_gaps,
    interpolate_small_gaps,
    max_gap_length
):
    if (any([ignore_zeropadded_gaps, ignore_zerofollowed_gaps])
            and not interpolate_small_gaps):
        raise ValueError(("swe2hs: your data contains NaNs surrounded "
                          "or followed by non-zeros."))
    elif (any([ignore_zeropadded_gaps, ignore_zerofollowed_gaps])
            and interpolate_small_gaps):
        raise ValueError(("swe2hs: your data contains gaps of NaNs "
                          "that are either:\n"
                          "    - at the the end or beginning of your series\n"
                          f"    - longer than {max_gap_length} timesteps and "
                          "not surrounded or followed by nonzeros\n"
                          f"    - shorter than {max_gap_length} timestep(s) "
                          "but with breaks in the date index"))
    elif (interpolate_small_gaps 
            and not any([ignore_zeropadded_gaps, ignore_zerofollowed_gaps])):
        raise ValueError(("swe2hs: your data contains gaps of NaNs "
                          "that are either:\n"
                          "    - at the the end or beginning of your series\n"
                          f"    - longer than {max_gap_length} timestep(s)\n"
                          f"    - shorter than {max_gap_length} timestep(s) "
                          "but with breaks in the date index"))
    else:
        raise ValueError("swe2hs: snow depth data must not be NaN.")


@njit
def _swe2hs_on_nonzero_chunks(
    swe_input,
    start_idxs,
    stop_idxs,
    rho_new,
    rho_max_init,
    rho_max_end,
    R,
    sigma_max,
    v_melt,
    hs_out,
    layers_hs_out,
    layers_rho_out,
    layers_rho_max_out,
):
    for start, stop in zip(start_idxs, stop_idxs):
        chunk_len = stop-start
        hs_chunk, layers_hs_chunk, layers_rho_chunk, layers_rho_max_chunk = swe2hs_snowpack_evolution(
            swe_input[start:stop],
            rho_new,
            rho_max_init,
            rho_max_end,
            R,
            sigma_max,
            v_melt,
            )
        
        hs_out[start:stop] = hs_chunk
        layers_hs_out[:chunk_len, start:stop] = layers_hs_chunk
        layers_rho_out[:chunk_len, start:stop] = layers_rho_chunk
        layers_rho_max_out[:chunk_len, start:stop] = layers_rho_max_chunk

    return hs_out, layers_hs_out, layers_rho_out, layers_rho_max_out


def convert_1d(
    data,
    rho_new=RHO_NEW,
    rho_max_init=RHO_MAX_INIT,
    rho_max_end=RHO_MAX_END,
    R=R,
    sigma_max=SIGMA_MAX,
    v_melt=V_MELT,
    swe_input_unit='m',
    hs_output_unit='m',
    ignore_zeropadded_gaps=False,
    ignore_zerofollowed_gaps=False,
    interpolate_small_gaps=False,
    max_gap_length=3,
    interpolation_method='linear',
    return_layers=False,
):
    """
    Calculate swe2hs for one dimensional input data series.

    Convert SWE station data or SWE as output from a single point model to HS. 
    The function performs some checks regarding missing data and inconsitencies 
    in the date index.

    Parameters
    ----------
    data : :class:`pandas.Series` with :class:`pandas.DatetimeIndex`
        Input snow water equivalent data.
    rho_new : float, optional
        New snow density in [kg/m^3], by default 85.9138139656343.
    rho_max_init : float, optional
        Initial value of the maximum snow density of a layer in [kg/m^3], by
        default 204.1345890849816.
    rho_max_end : float, optional
        End value of the maximum snow density of a layer in [kg/m^3], by 
        efault 427.1806327485636.
    R : float, optional
        Settling resistance, by default 5.922898941101872.
    sigma_max : float, optional
        Overburden where rho_max reaches rho_max,end. The unit is [mm w.e.]. 
        By default 226.9148577394744.
    v_melt : float, optional
        Speed of the transition towards rho_max,end in case of global SWE
        decrease, by default 0.13355554554152269.
    swe_input_unit : {"m", "mm", "cm"}
        The unit of the input snow water equivalent, by default 'm'
    hs_output_unit : {"m", "mm", "cm"}
        The unit of the output snow depth, by default 'm'
    ignore_zeropadded_gaps : bool
        Whether to ignore gaps that have leading and trailing zeros. The
        resulting HS series will contain NaNs at the same positions. These
        gaps are also ignored when you use `ignore_zerofollowed_gaps`. By 
        default False.
    ignore_zerofollowed_gaps : bool
        Less strict rule than `ignore_zeropadded_gaps`. Whether to ignore gaps
        that have trailing zeros. This can lead to sudden drops in HS in case
        missing SWE data is present. The resulting HS series will contain NaNs
        at the same positions. By default False.
    interpolate_small_gaps : bool
        Whether to interpolate small gaps in the input SWE data or not. Only gaps
        that are surrounded by data points and have continuous date spacing
        between the leading and trailing data point are interpolated. By default
        False.
    max_gap_length : int
        The maximum gap length of SWE data gaps that are interpolated if
        `interpolate_small_gaps` is True. The default is 3.
    interpolation_method : str
        Interpolation method for the small gaps which is passed to
        :meth:`pandas.Series.interpolate`. See its documentation for valid
        options. The default is 'linear'.
    return_layers : bool, optional
        Whether to return internal state variables of the model. If True, the
        return type of the function will change to :class:`xarray.Dataset`. By
        default False.

    Returns
    -------
    result : :class:`pandas.Series` :class:`xarray.Dataset`
        when `return_layers` is set to `True` an :class:`xarray.Dataset` is
        returned in which the layer state information is stored as data variables
        along with the snow depth.

    Raises
    ------
    ValueError
        When constraints on input data (missing values, incontinuous dates) are
        violated.

    Notes
    -----
    In order to convert two dimensional input grids, use the function
    :func:`~swe2hs.two_dimensional.convert_2d`.

    Examples
    --------
    Please see the respective :ref:`example notebook <1d_example_notebook>` for 
    examples on how to use the function.
    """

    for unit in [swe_input_unit, hs_output_unit]:
        assert unit in UNIT_FACTORS.keys(), (f"swe2hs: {unit} has to be "
                                            "in {'mm', 'cm', 'm'}")

    if not isinstance(data, pd.Series):
        raise ValueError("swe2hs: data must be pd.Series")

    if not isinstance(data.index, pd.DatetimeIndex):
        raise ValueError("swe2hs: data needs pd.DatetimeIndex as index.")

    swe = data.mul(_get_unit_conversion_factor(swe_input_unit, 'm')).to_numpy()
    dates = data.index.to_numpy()

    if ignore_zeropadded_gaps or ignore_zerofollowed_gaps:
        if ignore_zerofollowed_gaps:
            zeropadded_gap_idxs = get_zeropadded_gap_idxs(
                swe,
                require_leading_zero=False)
        else:  # ignore_zeropadded_gaps with zero in front and back
            zeropadded_gap_idxs = get_zeropadded_gap_idxs(
                swe,
                require_leading_zero=True)
        # replace the found gaps with zeros in swe in order to pass subsequent
        # checks. Nans will be restored after hs calculation.
        swe = np.where(zeropadded_gap_idxs, 0., swe)

    if np.any(np.isnan(swe)) and interpolate_small_gaps:
            swe = fill_small_gaps(
                swe,
                dates,
                max_gap_length,
                interpolation_method)

    # check for (remaining) missing values.
    if np.any(np.isnan(swe)):
        _raise_nans_error_message(
            ignore_zeropadded_gaps,
            ignore_zerofollowed_gaps,
            interpolate_small_gaps,
            max_gap_length,
        )

    if not np.all(swe >= 0):
        raise ValueError("swe2hs: swe data data must be positive")

    if not np.all(np.isreal(swe)):
        raise ValueError("swe2hs: swe data must be numeric")

    if swe[0] != 0:
        raise ValueError(("swe2hs: swe data must start "
                          "with 0 or the first non nan entry \nneeds to be "
                          "zero if you ignore zeropadded or zerofollowed gaps"))

    # start and stop indices of nonzero chunks.
    start_idxs, stop_idxs, max_chunk_length = get_nonzero_chunk_idxs(swe)

    # check for date continuity.
    continuous, resolution = continuous_timedeltas_in_nonzero_chunks(
        dates,
        start_idxs,
        stop_idxs)
    if not continuous:
        raise ValueError(("swe2hs: date column must be strictly "
                          "regular within \nchunks of consecutive nonzeros"))

    if resolution != 24.0:
        raise ValueError(("swe2hs: date resolution must be 24 hours within "
                          "chunks \nof consecutive nonzeros."))

    hs_allocation = np.zeros(len(swe))
    layers_hs_allocation = np.zeros((max_chunk_length, len(swe)))
    layers_rho_allocation = np.zeros((max_chunk_length, len(swe)))
    layers_rho_max_allocation = np.zeros((max_chunk_length, len(swe)))
    

    hs, layers_hs, layers_rho, layers_rho_max = _swe2hs_on_nonzero_chunks(
        swe,
        start_idxs,
        stop_idxs,
        rho_new,
        rho_max_init,
        rho_max_end,
        R,
        sigma_max,
        v_melt,
        hs_allocation,
        layers_hs_allocation,
        layers_rho_allocation,
        layers_rho_max_allocation
    )

    if ignore_zeropadded_gaps or ignore_zerofollowed_gaps:
        # restore nans in zeropadded gaps.
        hs = np.where(zeropadded_gap_idxs, np.nan, hs)
        layers_hs = np.where(zeropadded_gap_idxs, np.nan, layers_hs)
        layers_rho = np.where(zeropadded_gap_idxs, np.nan, layers_rho)
        layers_rho_max = np.where(zeropadded_gap_idxs, np.nan, layers_rho_max)

    if return_layers:
        result = xr.Dataset(
            data_vars={
                'time': dates,
                'layers': np.arange(max_chunk_length),
                'hs': ('time', hs * _get_unit_conversion_factor('m', hs_output_unit)),
                'layer_heights': (('layers','time'), layers_hs * _get_unit_conversion_factor('m', hs_output_unit)),
                'layer_densities': (('layers','time'), layers_rho),
                'layer_max_densities': (('layers','time'), layers_rho_max),
            }
        )

    else:
        result = pd.Series(
            data=hs * _get_unit_conversion_factor('m', hs_output_unit),
            index=data.index,
        )

    return result