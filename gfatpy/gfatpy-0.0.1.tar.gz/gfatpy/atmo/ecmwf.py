import datetime as dt

import requests
import numpy as np
import pandas as pd
import xarray as xr
from netCDF4 import Dataset  # type: ignore
from scipy.interpolate import interp1d

from gfatpy.utils.utils import parse_datetime

API_URL = "https://cloudnet.fmi.fi/api"
BASE_QUERY_PARAMS = {"site": "granada"}


def get_ecmwf_day(
    date: dt.datetime | str, times: np.ndarray, heights: np.ndarray
) -> xr.Dataset:
    """Fetches the ECMWF API to retrieve temperature and pressure data

    Args:
        date (dt.datetime | str): A data, hour doesn't affect

    Raises:
        FileNotFoundError: There is no available data in the ECMWF data

    Returns:
        xr.Dataset: x array dataset with variables: ["pressure", "temperature", "height", "time"]
    """
    _date = parse_datetime(date)
    response_filename = requests.get(
        f"{API_URL}/model-files",
        params={**BASE_QUERY_PARAMS, "date": _date.date().isoformat()},
    ).json()

    if len(response_filename) == 0:
        raise FileNotFoundError("No data found for the given day")

    file = requests.get(response_filename[0]["downloadUrl"])
    nc = Dataset("ecmwf.nc", memory=file.content)
    dataset = xr.open_dataset(xr.backends.NetCDF4DataStore(nc))  # type: ignore

    if heights is None:
        heights = np.arange(2666) * 7.5

    d_height = np.tile(heights, (25, 1))
    pressure = np.empty_like(d_height)
    temperature = np.empty_like(d_height)

    hours = np.arange(25)

    for hour in hours:
        pressure[hour, :] = np.interp(
            heights, nc["height"][hour, :], nc["pressure"][hour, :]
        )
        temperature[hour, :] = np.interp(
            heights, nc["height"][hour, :], nc["temperature"][hour, :]
        )

    pressure = np.apply_along_axis(
        lambda row: np.interp(
            times.astype("float64"), dataset.time.values.astype("float64"), row
        ).T,
        0,
        pressure,
    )

    temperature = np.apply_along_axis(
        lambda row: np.interp(
            times.astype("float64"), dataset.time.values.astype("float64"), row
        ).T,
        0,
        temperature,
    )

    return xr.Dataset(
        {
            "temperature": (["time", "range"], temperature),
            "pressure": (["time", "range"], pressure),
        },
        coords={"range": heights, "time": times},
    )  # type: ignore


def get_ecmwf_temperature_preasure(
    date: dt.datetime | str,
    hour: int | None = None,
    heights: np.ndarray | list | None = None,
) -> pd.DataFrame:
    """Fetch the ecmwf API and downloads temperature and pressure for a given hour date and hour (optional and default to 12:00). Returns the information in a DataFrame

    Args:
        date (dt.datetime | str): datetime or str datetime
        hour (int | None, optional): If need an specific time for the data retieval. Defaults to None.
        heights (np.ndarray | list | None, optional): A heights profile . Defaults to None.

    Raises:
        FileNotFoundError: If ecmwf model doesn't have data available for that date
        ValueError: Raises in case ranges input array shape is not as expected

    Returns:
        pd.DataFrame: DataFrame with three columns: height, temperature, pressure
    """

    _date = parse_datetime(date)

    if hour is None:
        _date = _date.replace(hour=12)
    else:
        _date = _date.replace(hour=hour)

    hour_int: int = _date.hour

    response_filename = requests.get(
        f"{API_URL}/model-files",
        params={**BASE_QUERY_PARAMS, "date": _date.date().isoformat()},
    ).json()

    if len(response_filename) == 0:
        raise FileNotFoundError("No data found for the given day")

    file = requests.get(response_filename[0]["downloadUrl"])
    nc = Dataset("ecmwf.nc", memory=file.content)

    height = nc.variables["height"][hour_int]
    temperature = nc.variables["temperature"][hour_int]
    pressure = nc.variables["pressure"][hour_int]

    if heights is None:
        return pd.DataFrame(
            {"height": height, "temperature": temperature, "pressure": pressure}
        )

    if np.ndim(heights) != 1:
        raise ValueError("heights must be 1-dimensinal")

    # interpolations, case when range doesn't match API heights
    temperature_fn = interp1d(
        height, temperature, bounds_error=False, fill_value="extrapolate"  # type: ignore
    )
    pressure_fn = interp1d(
        height, pressure, bounds_error=False, fill_value="extrapolate"  # type: ignore
    )

    return pd.DataFrame(
        {
            "height": heights,
            "temperature": temperature_fn(heights),
            "pressure": pressure_fn(heights),
        }
    )

    # return xr.open_dataarray(file.content)


all = ["get_ecmwf_day", "get_ecmwf_temperature_preasure"]
