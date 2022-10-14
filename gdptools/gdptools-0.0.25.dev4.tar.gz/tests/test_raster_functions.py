"""Tests for raster functions."""
import geopandas as gpd
import pandas as pd
import pytest
import rioxarray as rxr
import xarray as xr

from gdptools.gdp_data_class import TiffAttributes
from gdptools.raster_intersection import tiff_intersection_by_feature


@pytest.fixture(scope="module")
def get_tiff_slope() -> xr.DataArray:
    """Get tiff slope file."""
    return rxr.open_rasterio("./tests/data/rasters/slope/slope.tif")


@pytest.fixture(scope="module")
def get_tiff_text() -> xr.DataArray:
    """Get tiff text_prms file."""
    return rxr.open_rasterio("./tests/data/rasters/TEXT_PRMS/TEXT_PRMS.tif")


@pytest.fixture(scope="module")
def get_gdf() -> gpd.GeoDataFrame:
    """Get gdf file."""
    return gpd.read_file("./tests/data/Oahu.shp")


@pytest.mark.parametrize(
    "vn,xn,yn,bd,bn,crs,cat,ds,gdf,fid",
    [
        (
            "slope",
            "x",
            "y",
            1,
            "band",
            26904,
            False,
            "get_tiff_slope",
            "get_gdf",
            "fid",
        ),
        (
            "TEXT_PRMS",
            "x",
            "y",
            1,
            "band",
            26904,
            True,
            "get_tiff_text",
            "get_gdf",
            "fid",
        ),
    ],
)
def test_cat_tiff_intersection(vn, xn, yn, bd, bn, crs, cat, ds, gdf, fid, request):
    """Test tiff intersection function."""
    tdata = TiffAttributes(
        varname=vn,
        xname=xn,
        yname=yn,
        band=bd,
        bname=bn,
        crs=crs,
        categorical=cat,
        ds=request.getfixturevalue(ds),
    )

    ngdf = tiff_intersection_by_feature(
        data=tdata, gdf=request.getfixturevalue(gdf), poly_idx=fid
    )

    assert isinstance(ngdf, pd.DataFrame)
