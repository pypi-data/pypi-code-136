"""
Shared fixtures for all test files.
"""

import pytest
import pandas as pd
import numpy as np
import xarray as xr


@pytest.fixture
def valid_swe_sample_data():
    d = np.array([0, 0, 0, 0.01, 0.01, 0.02, 0.03, 0.05, 0.06, 0.06, 0.04,
                 0.03, 0.02, 0.01, 0.01, 0.005, 0.001, 0, 0, 0, 0, 0, 0.01, 0.01, 0]*50)
    i = pd.date_range(start='2000-01-01', periods=len(d), freq='D')
    return pd.Series(d, index=i)


@pytest.fixture
def default_swe2hs_params():
    return {
        'rho_new': 100.0,
        'rho_max_init': 300.0,
        'rho_max_end': 500.0,
        'R': 5.0,
        'sigma_max': 2.0,
        'v_melt': 0.5,
    }


@pytest.fixture
def swe_data_1d_series():
    """
    needs to have zeros at the 2nd September.
    """
    dates = pd.date_range(
        start='2000-07-01',
        end='2002-06-30',
        freq='D'
    )
    swe = np.zeros(len(dates))

    # insert an artificial SWE evolution from the first of November
    swe_winter = np.array([0.01]*10 + [0.02]*5 + [0.1]*10 + [0.15]*10 + np.linspace(
        0.15, 0.1, 10).tolist() + [0.25]*20 + [0.35]*15 + np.linspace(0.35, 0., 50).tolist() + [0.]*5 + [0.01]*7)
    first_novembers = np.nonzero(dates.strftime('%m-%d') == '11-01')[0]
    for fn in first_novembers:
        swe[fn:fn+len(swe_winter)] = swe_winter
    return pd.Series(swe, index=dates)


@pytest.fixture
def swe_data_1d_series_nans_in_june(swe_data_1d_series):
    swe_series = swe_data_1d_series
    swe_array = swe_series.to_numpy()
    first_junes = np.nonzero(swe_series.index.strftime('%m-%d') == '06-01')[0]
    nans = np.array([np.nan]*30)
    for fj in first_junes:
        swe_array[fj:fj+len(nans)] = nans
    return pd.Series(swe_array, index=swe_series.index)


@pytest.fixture
def swe_data_2d_dataarray_numpy(swe_data_1d_series):
    swe_series = swe_data_1d_series

    n_lon = 2
    n_lat = 3

    lon = list(range(n_lon))
    lat = list(range(n_lat))

    swe_2d = np.tile(swe_series.to_numpy(), (n_lon, n_lat, 1))

    d = xr.DataArray(
        data=swe_2d,
        coords={
            'lon': lon,
            'lat': lat,
            'time': swe_series.index.to_numpy()
        }
    )
    return d


@pytest.fixture
def swe_data_2d_dataarray_numpy_nans_in_june(swe_data_1d_series_nans_in_june):
    swe_series = swe_data_1d_series_nans_in_june

    n_lon = 2
    n_lat = 3

    lon = list(range(n_lon))
    lat = list(range(n_lat))

    swe_2d = np.tile(swe_series.to_numpy(), (n_lon, n_lat, 1))

    d = xr.DataArray(
        data=swe_2d,
        coords={
            'lon': lon,
            'lat': lat,
            'time': swe_series.index.to_numpy()
        }
    )
    return d


@pytest.fixture
def swe_data_2d_dataarray_numpy_one_cell_nan(swe_data_2d_dataarray_numpy):
    da = swe_data_2d_dataarray_numpy
    da = xr.where((da.coords["lon"] == 0) & (da.coords["lat"] == 0), np.nan, da)
    return da


@pytest.fixture
def swe_data_2d_dataarray_numpy_changed_dimorder(swe_data_2d_dataarray_numpy):
    """
    Identical data as in `swe_data_2d_dataarray_numpy` but with changed
    order of the dimensions.
    """
    return swe_data_2d_dataarray_numpy.transpose('lat', 'time', 'lon')


@pytest.fixture
def swe_data_2d_dataarray_dask(swe_data_2d_dataarray_numpy):
    """
    Identical data as in `swe_data_2d_dataarray_numpy` but the data within the
    :class:`xarray.DataArray` is stored in a chunked
    :class:`dask.array.core.Array`.
    """
    numpy_da = swe_data_2d_dataarray_numpy
    return numpy_da.chunk(chunks={'lon': 1, 'lat': 1, 'time': -1})


@pytest.fixture
def model_state_arrays():
    swe_layers = np.array([0., 0.1, 0.1, 0.2, 0., 0., 0., 0.1, 0., 0.])
    rho_layers = np.array([250., 220., 200., 190., 190., 180., 170., 140., 130., 120.])
    rho_max_layers = np.array(
        [350., 320., 300., 390., 390., 380., 370., 340., 330., 320.])
    assert len(swe_layers) == len(rho_layers) == len(rho_max_layers)
    return swe_layers, rho_layers, rho_max_layers


@pytest.fixture
def model_state_dataset_numpy(model_state_arrays):
    n_lon = 2
    n_lat = 3

    lon = list(range(n_lon))
    lat = list(range(n_lat))

    swe_layers, rho_layers, rho_max_layers = model_state_arrays
    model_state = xr.Dataset(
        data_vars={
            'swe_layers': (('lon', 'lat', 'layers'), np.tile(swe_layers, (n_lon, n_lat, 1))),
            'rho_layers': (('lon', 'lat', 'layers'), np.tile(rho_layers, (n_lon, n_lat, 1))),
            'rho_max_layers': (('lon', 'lat', 'layers'), np.tile(rho_max_layers, (n_lon, n_lat, 1))),
        },
        coords={
            'lon': lon,
            'lat': lat,
            'layers': list(range(len(swe_layers))),
        }
    )
    return model_state


@pytest.fixture
def model_state_dataset_dask(model_state_dataset_numpy):
    numpy_da = model_state_dataset_numpy
    return numpy_da.chunk(chunks={'lon': 1, 'lat': 1, 'layers': -1})
