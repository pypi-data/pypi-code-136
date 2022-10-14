"""Tests for .helper functions."""
import geopandas as gpd
import numpy as np
import pandas as pd
import pytest
import xarray as xr

from gdptools.gdp_data_class import CatGrids
from gdptools.gdp_data_class import CatParams
from gdptools.helpers import calculate_weights
from gdptools.helpers import finalize
from gdptools.helpers import get_data_subset_catalog
from gdptools.helpers import run_weights


@pytest.fixture()
def get_gdf() -> gpd.GeoDataFrame:
    """Create GeoDataFrame."""
    return gpd.read_file("./tests/data/hru_1210_epsg5070.shp")


@pytest.fixture()
def get_xarray() -> xr.Dataset:
    """Create xarray Dataset."""
    # return xr.open_dataset("./tests/data/cape_cod_tmax.nc")
    return xr.open_dataset(
        "http://thredds.northwestknowledge.net:8080/thredds/dodsC/agg_met_tmmx_1979_CurrentYear_CONUS.nc"
    )


@pytest.fixture()
def get_file_path(tmp_path):
    """Get temp file path."""
    return tmp_path / "test.csv"


@pytest.fixture()
def get_out_path(tmp_path):
    """Get temp file output path."""
    return tmp_path


data_crs = 4326
x_coord = "lon"
y_coord = "lat"
t_coord = "day"
sdate = "1979-01-01"
edate = "1979-01-07"
var = "daily_maximum_temperature"
shp_crs = 5070
shp_poly_idx = "hru_id_nat"
wght_gen_crs = 6931


def test_calculate_weights(get_xarray, get_gdf, get_file_path, get_out_path):
    """Test calculate weights."""
    wghts, ds_ss = calculate_weights(
        data_file=get_xarray,
        data_crs=data_crs,
        x_coord=x_coord,
        y_coord=y_coord,
        t_coord=t_coord,
        sdate=sdate,
        edate=edate,
        var=var,
        shp_file=get_gdf,
        shp_crs=shp_crs,
        shp_poly_idx=shp_poly_idx,
        wght_gen_file=get_file_path,
        wght_gen_crs=wght_gen_crs,
    )

    assert isinstance(wghts, pd.DataFrame)
    ngdf, vals = run_weights(
        var=var,
        t_name=t_coord,
        ds=ds_ss,
        wght_file=wghts,
        shp=get_gdf,
        geom_id=shp_poly_idx,
    )
    vallist = [vals]
    gdflist = [ngdf]
    assert isinstance(ngdf, gpd.GeoDataFrame)
    assert isinstance(vals, np.ndarray)

    var_dict = {
        var: {
            "long_name": ds_ss[var].long_name,
            "units": ds_ss[var].units,
            "varname": var,
            "standard_name": ds_ss[var].standard_name,
        }
    }
    dict_new = {
        "dims": {"feature": "nhru", "time": "time", "x": "lon", "y": "lat"},
        "feature": {
            "varname": "nhru",
            "long_name": "local model Hydrologic Response Unit ID (HRU)",
        },
        "lat": {
            "varname": "lat",
            "long_name": "Latitude of HRU centroid",
            "units": "degree_north",
            "standard_name": "latitude",
        },
        "lon": {
            "varname": "lon",
            "long_name": "Longitude of HRU centroid",
            "units": "degree_east",
            "standard_name": "longitude",
        },
        "daily_maximum_temperature": {
            "varname": "tmax",
            "long_name": "Daily maximum temperature",
            "standard_name": "maximum_daily_air_temperature",
            "convert": True,
            "native_unit": "degC",
            "convert_unit": "degF",
        },
    }

    fres = finalize(
        gdf=gdflist,
        vals=vallist,
        p_opath=get_out_path,
        prefix="gm_tmax",
        start_date=sdate,
        time_interval=1,
        time_type="days",
        var_dict=var_dict,
        use_opt_dict=True,
        work_dict=dict_new,
    )

    assert fres


@pytest.fixture(scope="module")
def catparam() -> CatParams:
    """Return parameter json."""
    param_json = "https://mikejohnson51.github.io/opendap.catalog/cat_params.json"
    params = pd.read_json(param_json)
    _id = "terraclim"  # noqa
    _varname = "aet"  # noqa
    tc = params.query("id == @_id & varname == @_varname")
    return CatParams(**tc.to_dict("records")[0])


@pytest.fixture(scope="module")
def catgrid(catparam) -> CatGrids:
    """Return grid json."""
    grid_json = "https://mikejohnson51.github.io/opendap.catalog/cat_grids.json"
    grids = pd.read_json(grid_json)
    _gridid = catparam.grid_id  # noqa
    tc = grids.query("grid_id == @_gridid")
    return CatGrids(**tc.to_dict("records")[0])


@pytest.fixture(scope="module")
def get_gdf_world() -> gpd.GeoDataFrame:
    """Get gdf file with country testing."""
    return gpd.read_file(
        "./tests/data/TM_WORLD_BORDERS_SIMPL-0.3/TM_WORLD_BORDERS_SIMPL-0.3.shp"
    )


@pytest.fixture(scope="module")
def get_begin_date() -> str:
    """Get begin date."""
    return "2005-01-01"


@pytest.fixture(scope="module")
def get_end_date() -> str:
    """Get end date."""
    return "2005-02-01"


@pytest.mark.parametrize(
    "cp,cg,gdf,sd,ed,name",
    [
        (
            "catparam",
            "catgrid",
            "get_gdf_world",
            "get_begin_date",
            "get_end_date",
            "Chile",
        ),
        (
            "catparam",
            "catgrid",
            "get_gdf_world",
            "get_begin_date",
            "get_end_date",
            "Netherlands",
        ),
        (
            "catparam",
            "catgrid",
            "get_gdf_world",
            "get_begin_date",
            "get_end_date",
            "Kenya",
        ),
        (
            "catparam",
            "catgrid",
            "get_gdf_world",
            "get_begin_date",
            "get_end_date",
            "Samoa",
        ),
        (
            "catparam",
            "catgrid",
            "get_gdf_world",
            "get_begin_date",
            "get_end_date",
            "Fiji",
        ),
    ],
)
def test_get_data_subset_catalog(cp, cg, gdf, sd, ed, name, request):
    """Test subset catalog."""
    ds = get_data_subset_catalog(
        params_json=request.getfixturevalue(cp),
        grid_json=request.getfixturevalue(cg),
        shp_file=request.getfixturevalue(gdf).query("NAME == @name"),
        begin_date=request.getfixturevalue(sd),
        end_date=request.getfixturevalue(ed),
    )

    assert isinstance(ds, xr.DataArray)
