import pytest
import numpy as np
import pandas as pd
import xarray as xr

from swe2hs._core import (
    _pad_layer_arrays_with_zero,
    timestep_forward,
)


from swe2hs.stepwise import (
    _apply_timestep_forward_to_model_state,
    _initialize_model_state,
    _pad_model_state_with_zero,
    _process_timestep_on_xr_objects,
    process_timestep_from_nc_files,
)

from swe2hs.two_dimensional import (
    convert_2d,
)


@pytest.mark.parametrize(
    "model_state_ds",
    [
        ("model_state_dataset_numpy"),
        ("model_state_dataset_dask"),
    ],
)
def test_pad_model_state_with_zero(
    model_state_arrays,
    model_state_ds,
    request
):
    swe_layers_in, rho_layers_in, rho_max_layers_in = model_state_arrays
    swe_layers_out, rho_layers_out, rho_max_layers_out = _pad_layer_arrays_with_zero(
        swe_layers_in,
        rho_layers_in,
        rho_max_layers_in
    )

    model_state_in = request.getfixturevalue(model_state_ds)
    model_state_out = _pad_model_state_with_zero(model_state_in, 'lon', 'lat')

    assert type(model_state_in['swe_layers'].data) == type(
        model_state_out['swe_layers'].data)
    assert type(model_state_in['rho_layers'].data) == type(
        model_state_out['rho_layers'].data)
    assert type(model_state_in['rho_max_layers'].data) == type(
        model_state_out['rho_max_layers'].data)

    np.testing.assert_almost_equal(
        swe_layers_out,
        model_state_out['swe_layers'].isel(lon=0, lat=0).values)
    np.testing.assert_almost_equal(
        rho_max_layers_out,
        model_state_out['rho_max_layers'].isel(lon=0, lat=0).values)
    np.testing.assert_almost_equal(
        rho_layers_out,
        model_state_out['rho_layers'].isel(lon=0, lat=0).values)


@pytest.mark.parametrize(
    "model_state_ds",
    [
        ("model_state_dataset_numpy"),
        ("model_state_dataset_dask"),
    ],
)
@pytest.mark.parametrize(
    "delta_swe",
    [
        (0.1),
        (0.0),
        (-0.1),
        (-0.3),
        (-0.5),
        (+1.0),
    ],
)
def test_apply_timestep_forward_to_model_state(
    delta_swe,
    model_state_arrays,
    model_state_ds,
    default_swe2hs_params,
    request
):
    params = default_swe2hs_params
    swe_layers, rho_layers, rho_max_layers = model_state_arrays
    swe_layers_in, rho_layers_in, rho_max_layers_in = _pad_layer_arrays_with_zero(
        swe_layers,
        rho_layers,
        rho_max_layers
    )
    swe_layers_out, rho_layers_out, rho_max_layers_out = timestep_forward(
        delta_swe,
        swe_layers_in,
        rho_layers_in,
        rho_max_layers_in,
        params['rho_new'],
        params['rho_max_init'],
        params['rho_max_end'],
        params['R'],
        params['sigma_max'],
        params['v_melt'],
    )

    model_state_in = request.getfixturevalue(model_state_ds)
    model_state_in = _pad_model_state_with_zero(model_state_in, 'lon', 'lat')

    n_lon_ = model_state_in['lon'].size
    n_lat_ = model_state_in['lat'].size
    delta_swe_arr = xr.DataArray(
        np.tile(np.array([delta_swe]), (n_lon_, n_lat_)),
        coords={
            'lon': list(range(n_lon_)),
            'lat': list(range(n_lat_)),
        }
    )

    model_state_out = _apply_timestep_forward_to_model_state(
        model_state_in,
        delta_swe_arr,
        params['rho_new'],
        params['rho_max_init'],
        params['rho_max_end'],
        params['R'],
        params['sigma_max'],
        params['v_melt'],
    )

    np.testing.assert_almost_equal(
        swe_layers_out,
        model_state_out['swe_layers'].isel(lon=0, lat=0).values
    )

    np.testing.assert_almost_equal(
        rho_max_layers_out,
        model_state_out['rho_max_layers'].isel(lon=0, lat=0).values
    )

    np.testing.assert_almost_equal(
        rho_layers_out,
        model_state_out['rho_layers'].isel(lon=0, lat=0).values
    )


@pytest.mark.parametrize("swe_dataarray",
                         [
                             ("swe_data_2d_dataarray_numpy"),
                             ("swe_data_2d_dataarray_numpy_one_cell_nan"),
                             ("swe_data_2d_dataarray_numpy_nans_in_june"),
                             # ("swe_data_2d_dataarray_dask"),
                         ],
                         )
@pytest.mark.parametrize("reset_day",
                         [
                             (None), ("08-01"), ("09-02")
                         ])
def test_process_timestep_on_xr_objects_against_convert_2d(
    swe_dataarray,
    reset_day,
    default_swe2hs_params,
    request,
):
    swe_in = request.getfixturevalue(swe_dataarray)
    hs_from_convert_2d_call = convert_2d(
        swe_data=swe_in,
        **default_swe2hs_params)

    hs_from_timesteps = []
    model_state = _initialize_model_state(
        swe_in.isel(time=0),
        'lon',
        'lat',
        'time',
    )
    for timestep in swe_in['time']:
        hs_step, model_state = _process_timestep_on_xr_objects(
            swe_in.sel(time=timestep),
            'lon',
            'lat',
            'time',
            model_state=model_state,
            reset_day=reset_day,
            **default_swe2hs_params
        )
        hs_from_timesteps.append(hs_step)

    hs_from_timesteps = (xr
                         .concat(hs_from_timesteps, dim='time')
                         .transpose('lon', 'lat', 'time')
                         )

    xr.testing.assert_allclose(hs_from_convert_2d_call, hs_from_timesteps)


@pytest.mark.parametrize(
    "swe_dataarray",
    [
        ("swe_data_2d_dataarray_numpy"),
        ("swe_data_2d_dataarray_numpy_one_cell_nan"),
        ("swe_data_2d_dataarray_numpy_nans_in_june"),
        # ("swe_data_2d_dataarray_dask"),
    ],
)
def test_timestep_from_nc_against_convert_2d(
    swe_dataarray,
    default_swe2hs_params,
    tmp_path,
    request,
):
    swe_in = request.getfixturevalue(swe_dataarray)

    hs_from_convert_2d_call = convert_2d(
        swe_data=swe_in,
        **default_swe2hs_params)

    indir = tmp_path / "input"
    outdir = tmp_path / "output"
    model_state_cachedir = tmp_path / "model_state_cache"
    indir.mkdir()
    outdir.mkdir()
    model_state_cachedir.mkdir()

    for timestep in swe_in['time']:
        # write input swe file to in_dir
        day = pd.to_datetime(timestep.values)
        swe_in.sel(time=timestep).to_netcdf(
            indir / f"swe_{day.strftime('%Y_%m_%d')}.nc")
        process_timestep_from_nc_files(
            indir / f"swe_{day.strftime('%Y_%m_%d')}.nc",
            outdir,
            'lon',
            'lat',
            'time',
            model_state_cachedir / "model_state.nc",
            reset_day='09-02',
            **default_swe2hs_params
        )

    hs_from_timesteps = xr.open_mfdataset(
        [f for f in outdir.glob('*.nc')],
        concat_dim="time",
        combine='nested',
    )['HS'].transpose('lon', 'lat', 'time').sortby('time')

    xr.testing.assert_allclose(hs_from_convert_2d_call, hs_from_timesteps)


@pytest.mark.parametrize("swe_dataarray",
                         [
                             ("swe_data_2d_dataarray_numpy"),
                             # ("swe_data_2d_dataarray_dask"),
                         ],
                         )
def test_date_inconsitency(
    swe_dataarray,
    default_swe2hs_params,
    request,
):
    swe_in = request.getfixturevalue(swe_dataarray)
    hs_from_convert_2d_call = convert_2d(
        swe_data=swe_in,
        **default_swe2hs_params)

    hs_from_timesteps = []
    model_state = _initialize_model_state(
        swe_in.isel(time=0),
        'lon',
        'lat',
        'time',
    )
    for timestep in swe_in['time']:
        if pd.to_datetime(timestep.values).strftime('%m-%d') == "12-30":
            # skip one day in the middle of the winter:
            continue
        else:
            hs_step, model_state = _process_timestep_on_xr_objects(
                swe_in.sel(time=timestep),
                'lon',
                'lat',
                'time',
                model_state=model_state,
                reset_day=None,
                **default_swe2hs_params
            )
            hs_from_timesteps.append(hs_step)

    hs_from_timesteps = (xr
                         .concat(hs_from_timesteps, dim='time')
                         .transpose('lon', 'lat', 'time').sortby('time')
                         )
    with pytest.raises(AssertionError):
        xr.testing.assert_allclose(hs_from_convert_2d_call, hs_from_timesteps)
