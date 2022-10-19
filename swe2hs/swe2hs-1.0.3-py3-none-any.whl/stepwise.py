import logging

from numba import guvectorize
import xarray as xr
import numpy as np
import pandas as pd
import dask.array as da

from ._core import timestep_forward

from ._default_model_parameters import *

logger = logging.getLogger(__name__)


def _initialize_model_state(
    swe_dataarray: xr.DataArray,
    x_dim_name: str,
    y_dim_name: str,
    time_dim_name: str,
) -> xr.Dataset:
    """
    get dimensions from swe field
    create empty model state from these dimensions

    """
    input_dims = swe_dataarray.dims

    for dim in [x_dim_name, y_dim_name]:
        if dim not in input_dims:
            raise ValueError(("swe2hs: you assigned the dimension name "
                              f"'{dim}' which is \nnot in the dimensions "
                              "of the SWE input DataArray."))

    nx_ = swe_dataarray.sizes[x_dim_name]
    ny_ = swe_dataarray.sizes[y_dim_name]

    coords = {}
    for d in swe_dataarray.coords:
        if d != time_dim_name:
            coords[d] = swe_dataarray[d].values
    coords['layers'] = np.array([])
    # we initialize model state at the day before
    coords['date'] = swe_dataarray[time_dim_name].values - np.timedelta64(1, 'D')

    initial_model_state = xr.Dataset(
        data_vars={
            'swe_layers': ((x_dim_name, y_dim_name, 'layers'), np.zeros((nx_, ny_, 0))),
            'rho_layers': ((x_dim_name, y_dim_name, 'layers'), np.zeros((nx_, ny_, 0))),
            'rho_max_layers': ((x_dim_name, y_dim_name, 'layers'), np.zeros((nx_, ny_, 0))),
        },
        coords=coords,
    )
    return initial_model_state


def _pad_dask_or_numpy(array, pad_width, **kwargs):
    if isinstance(array, np.ndarray):
        padded = np.pad(array, pad_width, **kwargs)
    elif isinstance(array, da.core.Array):
        padded = da.pad(array, pad_width, **kwargs)
    return padded


def _pad_model_state_with_zero(
    model_state: xr.Dataset,
    x_dim_name: str,
    y_dim_name: str,
) -> xr.Dataset:
    """
    Add a layer with zeros at the end of each model state variable. Index of
    layers is increasing by 1.

    Parameters
    ----------
    model_state : xr.Dataset
        model state object
    x_dim_name : str
        name of x dimension
    y_dim_name : str
        name of y dimension

    Returns
    -------
    xr.Dataset
        padded model state object
    """
    swe = _pad_dask_or_numpy(model_state['swe_layers'].data, ((0, 0), (0, 0), (0, 1)))
    rho = _pad_dask_or_numpy(model_state['rho_layers'].data, ((0, 0), (0, 0), (0, 1)))
    rho_max = _pad_dask_or_numpy(
        model_state['rho_max_layers'].data, ((0, 0), (0, 0), (0, 1)))

    if len(model_state['layers']) == 0:
        layer_index = _pad_dask_or_numpy(model_state['layers'].data, (0, 1))
    else:
        layer_index = _pad_dask_or_numpy(
            model_state['layers'].data,
            (0, 1),
            mode='linear_ramp',
            end_values=model_state['layers'].data[-1]+1)

    coords = {}
    for d in model_state.coords:
        if d != 'layers':
            coords[d] = model_state[d].values
    coords['layers'] = layer_index

    padded_model_state = xr.Dataset(
        data_vars={
            'swe_layers': ((x_dim_name, y_dim_name, 'layers'), swe),
            'rho_layers': ((x_dim_name, y_dim_name, 'layers'), rho),
            'rho_max_layers': ((x_dim_name, y_dim_name, 'layers'), rho_max),
        },
        coords=coords,
    )
    return padded_model_state


@guvectorize(
    ['f8[:], f8[:], f8[:], f8, f8, f8, f8, f8, f8, f8, f8[:], f8[:], f8[:]'],
    '(n),(n),(n),(),(),(),(),(),(),()->(n),(n),(n)',
    nopython=True
)
def _timestep_forward_gufunc(
    swe_layers_in,
    rho_layers_in,
    rho_max_layers_in,
    delta_swe,
    rho_new,
    rho_max_init,
    rho_max_end,
    R,
    sigma_max,
    v_melt,
    swe_layers_out,
    rho_layers_out,
    rho_max_layers_out
):
    """
    Vectorized numba version of :func:`core.timestep_forward`
    """
    # output arrays require padding of 1 zero at the end beforehand
    swe_layers_out[:], rho_layers_out[:], rho_max_layers_out[:] = timestep_forward(
        delta_swe,
        swe_layers_in,
        rho_layers_in,
        rho_max_layers_in,
        rho_new,
        rho_max_init,
        rho_max_end,
        R,
        sigma_max,
        v_melt,
    )


def _wrapped_timestep_forward_gufunc(
    swe_layers_in,
    rho_layers_in,
    rho_max_layers_in,
    delta_swe,
    rho_new=RHO_NEW,
    rho_max_init=RHO_MAX_INIT,
    rho_max_end=RHO_MAX_END,
    R=R,
    sigma_max=SIGMA_MAX,
    v_melt=V_MELT,
):
    """
    The numba gufunc :func:`_timestep_forward_gufunc` needs to be wrapped by an
    ordinary python function in order to work with :func:`xarray.apply_ufunc`
    correctly.
    """
    swe_layers_out = swe_layers_in.copy()
    rho_layers_out = rho_layers_in.copy()
    rho_max_layers_out = rho_max_layers_in.copy()

    _timestep_forward_gufunc(
        swe_layers_in,
        rho_layers_in,
        rho_max_layers_in,
        delta_swe,
        rho_new,
        rho_max_init,
        rho_max_end,
        R,
        sigma_max,
        v_melt,
        swe_layers_out,
        rho_layers_out,
        rho_max_layers_out
    )
    return swe_layers_out, rho_layers_out, rho_max_layers_out


def _apply_timestep_forward_to_model_state(
    model_state: xr.Dataset,
    delta_swe: xr.DataArray,
    rho_new,
    rho_max_init,
    rho_max_end,
    R,
    sigma_max,
    v_melt,
):
    params = {
        'rho_new': rho_new,
        'rho_max_init': rho_max_init,
        'rho_max_end': rho_max_end,
        'R': R,
        'sigma_max': sigma_max,
        'v_melt': v_melt,
    }

    if (any([isinstance(d.data, da.core.Array) for d in model_state.data_vars.values()])
            or isinstance(delta_swe.data, da.core.Array)):
        swe_layers, rho_layers, rho_max_layers = (xr
                                                  .apply_ufunc(
                                                      _wrapped_timestep_forward_gufunc,
                                                      model_state['swe_layers'],
                                                      model_state['rho_layers'],
                                                      model_state['rho_max_layers'],
                                                      delta_swe,
                                                      kwargs=params,
                                                      input_core_dims=(
                                                          ['layers'], ['layers'], ['layers'], []),
                                                      output_core_dims=(
                                                          ['layers'], ['layers'], ['layers'],),
                                                      dask='parallelized',
                                                      output_dtypes=[
                                                          'float64', 'float64', 'float64'],
                                                      # TODO get rid of 'allow_rechunk' in dask_gufunc_kwargs because
                                                      # it heavily increases memory usage. Somewhere chunking is
                                                      # messed up, probably in :func:`_pad_model_state_with_zero`
                                                      dask_gufunc_kwargs={
                                                          'allow_rechunk': True}
                                                  )
                                                  )

    else:  # only numpy arrays present in 'model_state' and 'delta_swe'.
        swe_layers, rho_layers, rho_max_layers = (xr
                                                  .apply_ufunc(
                                                      _wrapped_timestep_forward_gufunc,
                                                      model_state['swe_layers'],
                                                      model_state['rho_layers'],
                                                      model_state['rho_max_layers'],
                                                      delta_swe,
                                                      kwargs=params,
                                                      input_core_dims=(
                                                          ['layers'], ['layers'], ['layers'], []),
                                                      output_core_dims=(
                                                          ['layers'], ['layers'], ['layers'],),
                                                  )
                                                  )

    model_state['swe_layers'] = swe_layers
    model_state['rho_layers'] = rho_layers
    model_state['rho_max_layers'] = rho_max_layers

    return model_state


def _process_timestep_on_xr_objects(
    swe_of_day,
    x_dim_name,
    y_dim_name,
    time_dim_name,
    model_state,
    reset_day=None,
    rho_new=RHO_NEW,
    rho_max_init=RHO_MAX_INIT,
    rho_max_end=RHO_MAX_END,
    R=R,
    sigma_max=SIGMA_MAX,
    v_melt=V_MELT,
):
    """


    Parameters
    ----------
    swe_of_day : :class:`xarray.DataArray`
        Three dimensional snow water equivalent (SWE) field of the day that is 
        processed. Time dimesnion must be of size 1.
    x_dim_name : str
        Name of the x-coordinate in the input SWE field (e.g. 'easting' or 
        'lon').
    y_dim_name : str
        Name of the y-coordinate in the input SWE field (e.g. 'northing' or 
        'lat').
    time_dim_name : str
        Name of the time dimension in the input SWE field.
    model_state : :class:`xarray.Dataset`
        Model state object as created with :func:`_initialize_model_state`.
    reset_day : str or None, optional
        Day in the year where the model state is getting reset of the format 
        'MM-DD'. If set to None, the model state will never be reset. The
        default is None.
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

    Returns
    -------
    tuple
        Tuple of `(hs, model_state_new)` where `hs` is a :class:`xarray.DataArray`
        object and `model_state_new` is a :class:`xarray.Dataset` object.
    """
    processing_date = pd.to_datetime(swe_of_day[time_dim_name].values)
    reset_model_state = False
    if reset_day is not None:
        if processing_date.strftime('%m-%d') == reset_day:
            logger.info(("Resetting model state at date "
                         f"{processing_date.strftime('%Y-%m-%d')}."))
            reset_model_state = True

    if model_state['date'].values + np.timedelta64(1, 'D') != swe_of_day[time_dim_name].values:
        logger.warning(("Date inconsistency before date "
                        f"{processing_date.strftime('%Y-%m-%d')}. "
                        "Resetting model state."))
        reset_model_state = True

    if reset_model_state:
        model_state = _initialize_model_state(
            swe_of_day,
            x_dim_name,
            y_dim_name,
            time_dim_name,
        )

    model_state_padded = _pad_model_state_with_zero(
        model_state,
        x_dim_name,
        y_dim_name,
    )

    delta_swe = swe_of_day - model_state['swe_layers'].sum(dim='layers')
    # the following line is necessary to get rid of floating point inaccurracies
    delta_swe = xr.where((np.abs(delta_swe) > 1e-15), delta_swe, 0.)

    model_state_new = _apply_timestep_forward_to_model_state(
        model_state_padded,
        delta_swe,
        rho_new,
        rho_max_init,
        rho_max_end,
        R,
        sigma_max,
        v_melt,
    ).drop_vars(time_dim_name)

    model_state_new['date'] = swe_of_day[time_dim_name].values

    hs = (
        ((model_state_new['swe_layers']*1000) / model_state_new['rho_layers'])
        .drop_vars('date')  # dtae from model state gets dragged along
        .sum(dim='layers', skipna=True)
    )

    hs = xr.where(swe_of_day == 0, 0, hs)
    hs = xr.where(np.isnan(swe_of_day), np.nan, hs)

    hs.name = 'HS'
    return hs, model_state_new


def process_timestep_from_nc_files(
    swe_of_day_ncfile,
    hs_out_directory,
    x_dim_name,
    y_dim_name,
    time_dim_name,
    model_state_cache_path,
    reset_day='09-02',
    rho_new=RHO_NEW,
    rho_max_init=RHO_MAX_INIT,
    rho_max_end=RHO_MAX_END,
    R=R,
    sigma_max=SIGMA_MAX,
    v_melt=V_MELT,
):
    """Process a timestep from netcdf files.
    
    This function reads a netcdf file of daily SWE and cached model state from 
    disk and calculate HS for that day. The calculated HS will be saved to a 
    user specified directory with the filename 'hs_YYYY_MM_DD.nc'. The evolved 
    model state is saved to the user specified `model_state_cache_path`.

    Parameters
    ----------
    swe_of_day_ncfile : str or path object
        Netcdf file of the day that has to be processed.
    hs_out_directory : str or path object
        Directory where the processed file will be written to.
    x_dim_name : str
        Name of the x dimension of the gridded data.
    y_dim_name : str
        Name of the y dimension of the gridded data.
    time_dim_name : str
        Name of the time dimension of the gridded data.
    model_state_cache_path : _type_
        _description_
    reset_day : str, optional
        _description_, by default '09-02'
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

    Returns
    -------
    None
        Model state and HS will be stored on disk as netcdf files.
    """
    # TODO list:

    #    - get dask working efficiently

    swe_of_day = xr.open_dataarray(
        swe_of_day_ncfile,
        engine='netcdf4',
        # chunks={x_dim_name: 15, y_dim_name:15, time_dim_name:-1}
    )

    # day as pd.Timestap object
    current_day = pd.to_datetime(swe_of_day[time_dim_name].values)

    try:
        model_state = xr.open_dataset(
            model_state_cache_path,
            engine='netcdf4',
            # chunks={x_dim_name: 15, y_dim_name:15, 'layers':-1}
        )
    except FileNotFoundError:
        logger.info("Failed to load model state, initializing swe2hs model.")
        model_state = _initialize_model_state(
            swe_of_day,
            x_dim_name,
            y_dim_name,
            time_dim_name,
        )

    hs, model_state_new = _process_timestep_on_xr_objects(
        swe_of_day,
        x_dim_name,
        y_dim_name,
        time_dim_name,
        model_state,
        reset_day=reset_day,
        rho_new=rho_new,
        rho_max_init=rho_max_init,
        rho_max_end=rho_max_end,
        R=R,
        sigma_max=sigma_max,
        v_melt=v_melt,
    )

    model_state.close()
    model_state_new.to_netcdf(model_state_cache_path)

    hs.to_netcdf(hs_out_directory / f"hs_{current_day.strftime('%Y_%m_%d')}.nc")

    return None
