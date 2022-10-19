from datetime import datetime

import numpy as np
import xarray as xr
import dask.array as da
from numba import guvectorize

from . import __version__

from ._core import swe2hs_snowpack_evolution_return_no_layer_states
from .utils import (
    continuous_timedeltas,
    _get_split_indices_based_on_date,
    _get_unit_conversion_factor,
    UNIT_FACTORS,
)

from ._default_model_parameters import *


@guvectorize(
    ['void(float64[:], int64[:], float64, float64, float64, float64, float64, float64, int64, int64, float64[:])'],
    '(n),(n),(),(),(),(),(),(),(),()->(n)',
    nopython=True
)
def _swe2hs_gufunc_reset_day(
    swe_input,
    month_input,
    rho_new,
    rho_max_init,
    rho_max_end,
    R,
    sigma_max,
    v_melt,
    split_month,
    split_day,
    hs_out,
):
    """
    Numba gufunc which resets the snowpack when day and month both match the
    split_day and split_month arguments.
    """
    split_idxs = _get_split_indices_based_on_date(month_input, split_month, split_day)

    for start, stop in zip(split_idxs[:-1], split_idxs[1:]):
        hs_out[start:stop] = swe2hs_snowpack_evolution_return_no_layer_states(
            swe_input[start:stop],
            rho_new,
            rho_max_init,
            rho_max_end,
            R,
            sigma_max,
            v_melt,
        )


@guvectorize(
    ['void(float64[:], float64, float64, float64, float64, float64, float64, float64[:])'],
    '(n),(),(),(),(),(),()->(n)',
    nopython=True
)
def _swe2hs_gufunc_no_reset_day(
    swe_input,
    rho_new,
    rho_max_init,
    rho_max_end,
    R,
    sigma_max,
    v_melt,
    hs_out,
):
    """
    Numba gufunc which splits swe input into chunks of consecutive nonzeros and 
    calculates swe2hs on these chunks. 
    """
    hs_out[:] = swe2hs_snowpack_evolution_return_no_layer_states(
        swe_input,
        rho_new,
        rho_max_init,
        rho_max_end,
        R,
        sigma_max,
        v_melt,
    )


def _wrapped_swe2hs_gufunc_reset_day(
    swe_input,
    month_input,
    rho_new=RHO_NEW,
    rho_max_init=RHO_MAX_INIT,
    rho_max_end=RHO_MAX_END,
    R=R,
    sigma_max=SIGMA_MAX,
    v_melt=V_MELT,
    split_month=9,
    split_day=1,
):
    """
    Wrap the gufunc in order to accept keyword arguments.
    """
    # initialize output
    hs_out = np.zeros(len(swe_input), dtype=np.float64)

    with np.errstate(invalid='ignore'):
        # call vetorized function
        hs_out = _swe2hs_gufunc_reset_day(
            swe_input,
            month_input,
            rho_new,
            rho_max_init,
            rho_max_end,
            R,
            sigma_max,
            v_melt,
            split_month,
            split_day,
        )
    return hs_out


def _wrapped_swe2hs_gufunc_no_reset_day(
    swe_input,
    rho_new=RHO_NEW,
    rho_max_init=RHO_MAX_INIT,
    rho_max_end=RHO_MAX_END,
    R=R,
    sigma_max=SIGMA_MAX,
    v_melt=V_MELT,
):
    """
    Wrap the gufunc in order to accept keyword arguments.
    """
    # initialize output
    hs_out = np.zeros(len(swe_input), dtype=np.float64)
    # we have problems with nans for .core._calculate_hs_layers
    # see https://github.com/numba/numba/issues/4793#issuecomment-622323686
    with np.errstate(invalid='ignore'):
        # call vetorized function
        hs_out = _swe2hs_gufunc_no_reset_day(
            swe_input,
            rho_new,
            rho_max_init,
            rho_max_end,
            R,
            sigma_max,
            v_melt,
        )
    return hs_out


def convert_2d(
    swe_data,
    rho_new=RHO_NEW,
    rho_max_init=RHO_MAX_INIT,
    rho_max_end=RHO_MAX_END,
    R=R,
    sigma_max=SIGMA_MAX,
    v_melt=V_MELT,
    time_dim_name='time',
    reset_day=None,
    swe_input_unit='m',
    hs_output_unit='m',
):
    """
    Distributed version of the swe2hs model. 

    Apply the model on a :class:`xarray.DataArray` which holds three
    dimensional SWE data (x dimension, y dimension and time dimension).

    This function calls a vectorized version (see :func:`numba.guvectorize`) of 
    the swe2hs core algorithm within :func:`xarray.apply_ufunc`. 

    Parameters
    ----------
    swe_data : :class:`xarray.DataArray`
        DataArray containing the SWE data.
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
        decrease, by default 0.13355554554152269
    time_dim_name : str, optional
        Name of the time dimension in the input SWE data, by default 'time'.
    reset_day : str or None, optional
        Day in the year where the model state is getting reset of the format 
        'MM-DD'. If set to None, the model state will never be reset. The
        default is None.
    swe_input_unit : {"m", "mm", "cm"}
        The unit of the input snow water equivalent, by default 'm'
    hs_output_unit : {"m", "mm", "cm"}
        The unit of the output snow depth, by default 'm'


    Returns
    -------
    :class:`xarray.DataArray`
        Calculated snow depth, same shape, coordinates and dimensions as 
        the input data.

    Raises
    ------
    ValueError
        If any of the constraints on the data are violated. 
    
    Notes
    -----
    If you pass a :class:`xarray.DataArray` containing Dask data arrays which
    are chunked in the x (lon) and y (lat) dimensions, this function will
    execute the model in parallel over the different chunks. If you additionally
    read and write from a netcdf file in chunks, you can process datasets which
    would normally not fit into memory 
    (see :ref:`this section <convert_2d_data_from_files>` in the example notebook).

    For converting one dimensional input series for single point data use 
    the :func:`~swe2hs.one_dimensional.convert_1d` function.

    Examples
    --------
    Please see the respective :ref:`example notebook <2d_example_notebook>` for 
    examples on how to use the function.

    """
    if not isinstance(swe_data, xr.DataArray):
        raise TypeError("swe2hs: swe data needs to be a xarray.DataArray.")

    input_dims = swe_data.dims

    if time_dim_name not in input_dims:
        raise ValueError(("swe2hs: you assigned the time dimension name "
                          f"'{time_dim_name}' which is \nnot in the dimensions "
                          "of the SWE input DataArray."))

    for unit in [swe_input_unit, hs_output_unit]:
        assert unit in UNIT_FACTORS.keys(), (f"swe2hs: {unit} has to be "
                                            "in {'mm', 'cm', 'm'}")

    # pass parameters to a dict for later reuse
    params = {
        'rho_new': rho_new,
        'rho_max_init': rho_max_init,
        'rho_max_end': rho_max_end,
        'R': R,
        'sigma_max': sigma_max,
        'v_melt': v_melt,
    }

    if reset_day is not None:
        contiuous, resolution = continuous_timedeltas(swe_data[time_dim_name].values)
        if not contiuous or resolution != 24:
            raise ValueError(
                (f"swe2hs: time dimension '{time_dim_name}' is not continuous "
                 "or does not have 1 day resolution.")
            )

        split_month = int(reset_day.split('-')[0])
        split_day = int(reset_day.split('-')[1])
        params.update({'split_month': split_month, 'split_day': split_day})

    if isinstance(swe_data.data, np.ndarray):
        if reset_day is None:
            hs = (xr
                .apply_ufunc(
                    _wrapped_swe2hs_gufunc_no_reset_day,
                    swe_data * _get_unit_conversion_factor(swe_input_unit, 'm'),
                    kwargs=params,
                    input_core_dims=[[time_dim_name]],
                    output_core_dims=[[time_dim_name]],
                )
            )
        else:
            hs = (xr
                .apply_ufunc(
                    _wrapped_swe2hs_gufunc_reset_day,
                    swe_data * _get_unit_conversion_factor(swe_input_unit, 'm'),
                    swe_data.coords[f'{time_dim_name}.month'],
                    kwargs=params,
                    input_core_dims=[[time_dim_name], [time_dim_name]],
                    output_core_dims=[[time_dim_name]],
                )
            )
    elif isinstance(swe_data.data, da.core.Array):
        if reset_day is None:
            hs = (xr
                .apply_ufunc(
                    _wrapped_swe2hs_gufunc_no_reset_day,
                    swe_data * _get_unit_conversion_factor(swe_input_unit, 'm'),
                    kwargs=params,
                    input_core_dims=[[time_dim_name]],
                    output_core_dims=[[time_dim_name]],
                    dask='parallelized',
                    output_dtypes=['float64']
                )
            )
        else:
            hs = (xr
                .apply_ufunc(
                    _wrapped_swe2hs_gufunc_reset_day,
                    swe_data * _get_unit_conversion_factor(swe_input_unit, 'm'),
                    swe_data.coords[f'{time_dim_name}.month'],
                    kwargs=params,
                    input_core_dims=[[time_dim_name], [time_dim_name]],
                    output_core_dims=[[time_dim_name]],
                    dask='parallelized',
                    output_dtypes=['float64']
                )
            )
    else:
        raise TypeError(("swe2hs: underlying data in the xr.DataArray needs to "
                         "be numpy.ndarray or dask array."))

    
    result = ((hs * _get_unit_conversion_factor('m', hs_output_unit))
        .transpose(input_dims[0], input_dims[1], input_dims[2])
        .rename('HS')
        .assign_attrs(
            title=('Snow depth (HS) calculated from snow water equivalent'
                ' with the SWE2HS model'),
            unit=hs_output_unit,
            source=f'swe2hs Python package v{__version__}',
            reference=('A conceptual model to calculate snow depth from daily '
                'snow water equivalent of the snow cover: SWE2HS 1.0'),
            creation_date=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        )
    )

    return result