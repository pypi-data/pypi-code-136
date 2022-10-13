import datetime as dt
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd
import xarray as xr
from scipy.signal import savgol_filter

from gfatpy.utils import utils
from gfatpy.atmo import atmo, ecmwf
from gfatpy.lidar.preprocessing import preprocess
from gfatpy.lidar.file_manager import channel2info
from gfatpy.lidar.utils import LIDAR_INFO, signal_to_rcs
from gfatpy.lidar.quality_assurance.io import rayleigh2earlinet
from gfatpy.lidar.quality_assurance.plot import plot_rayleigh_fit

lidar_id = "gr"
lidar_location = "Granada"

""" Types of Lidar Measurements """
measurement_types = {
    "RS": "Prs",
    "DC": "Pdc",
    "OT": "Pot",
    "DP-P45": "Pdp-45",
    "DP-N45": "Pdp-N45",
}


def get_meteo(
    date: dt.datetime,
    range: np.ndarray[Any, np.dtype[np.float64]],
    meteorology_source: str,
) -> tuple[pd.DataFrame, dict]:
    # get T and P
    info = {}
    info["radiosonde_datetime"] = date.strftime(
        "%Y-%m-%dT%H-%M-%S"
    )  # FIXME: change if other methods are implemented.

    if meteorology_source == "ecmwf":  # TODO: implement other methods
        meteo_profiles = None
        meteo_profiles = ecmwf.get_ecmwf_temperature_preasure(date, heights=range)
        if meteo_profiles is None:
            pressure_prf = np.array(938.0)
            temperature_prf = np.array(25.0)
            meteo_profiles = atmo.extend_meteo_profile(
                pressure_prf, temperature_prf, range
            )
            info["radiosonde_wmo_id"] = None
            info["radiosonde_location"] = "Granada"
            info["radiosonde_source"] = "scaled standard atmosphere"
            raise Warning(
                "ECMWF data not available. Using scaled standard atmosphere with (T, P) = (25, 938)"
            )
        else:
            info["radiosonde_wmo_id"] = "ecmwf"
            info["radiosonde_location"] = "Granada"
            info["radiosonde_source"] = "ECMWF"
    else:
        raise ValueError("only ecmwf method is currently implemented.")
    return meteo_profiles, info


def rayleigh_fit_channel(
    channel: str,
    rf_dataset: xr.Dataset,
    initial_date: dt.datetime,
    final_date: dt.datetime,
    meteo_profiles: pd.DataFrame,
    meteo_info: dict,
    min_reference_height: float,
    max_reference_height: float,
    smooth_window: float,
) -> xr.Dataset:

    wavelength, *_ = channel2info(channel)

    # Molecular Attenuated Backscatter
    temperature = np.array(meteo_profiles["temperature"])
    pressure = np.array(meteo_profiles["pressure"])
    range = np.array(meteo_profiles["height"])
    mol_properties = atmo.molecular_properties(wavelength, pressure, temperature, range)
    att_beta_mol = mol_properties["attenuated_molecular_beta"]

    wavelength, _, polarization, mode = channel2info(channel)

    # RCS
    signal = rf_dataset[f"signal_{channel}"]
    rcs = signal_to_rcs(signal, signal.range)

    # Smooth rcs
    """ Lidar Resolution, Smoothing Bins """
    resolution = np.median(np.diff(signal.range))
    smooth_bins = np.round((smooth_window / resolution)).astype(int)
    sm_rcs = xr.DataArray(
        savgol_filter(rcs, smooth_bins, 3),
        coords={"range": signal.range},
        dims=["range"],
    )

    # Normalize time-averaged RCS, BCS nd Smoothed Time-Averaged RCS
    n_rcs = rcs / rcs.sel(range=slice(min_reference_height, max_reference_height)).mean(
        "range"
    )

    n_sm_rcs = sm_rcs / sm_rcs.sel(
        range=slice(min_reference_height, max_reference_height)
    ).mean("range")

    n_att_beta_mol = att_beta_mol / att_beta_mol.sel(
        range=slice(min_reference_height, max_reference_height)
    ).mean("range")

    # output dataset will have height info in km
    ranges_km = range * 1e-3
    z_min_km = min_reference_height * 1e-3
    z_max_km = max_reference_height * 1e-3

    wavelength = xr.DataArray(data=wavelength, attrs={"str": f"{wavelength}"})
    polarization = xr.DataArray(
        data=polarization,
        dims=[],
        attrs={
            "long_name": LIDAR_INFO["metadata"][
                "code_polarization_str2long_name"
            ][  # FIXME: error de tipado
                polarization
            ],
            "id": LIDAR_INFO["metadata"]["code_polarization_number2str"],
        },
    )

    detection_mode = xr.DataArray(
        data=mode,
        dims=[],
        attrs={
            "long_name": LIDAR_INFO["metadata"]["code_mode_str2long_name"][
                mode
            ],  # FIXME: error de tipado
            "id": LIDAR_INFO["metadata"]["code_mode_str2number"][mode],
        },
    )

    rcs = xr.DataArray(
        data=rcs,
        dims=["range"],
        coords={"range": ranges_km},
        attrs={
            "name": "RangeCorrectedSignal",
            "long_name": "range corrected signal avg",
            "units": "a.u.",
        },
    )

    n_rcs = xr.DataArray(
        data=n_rcs,
        dims=["range"],
        coords={"range": ranges_km},
        attrs={
            "name": "RangeCorrectedSignal",
            "long_name": "normalized- range-corrected signal.",
            "units": "a.u.",
        },
    )

    smoothed_rcs = xr.DataArray(
        data=sm_rcs,
        dims=["range"],
        coords={"range": ranges_km},
        attrs={
            "name": "RangeCorrectedSignal",
            "long_name": "smoothed range corrected signal",
            "units": "a.u.",
        },
    )

    normalized_smoothed_rcs = xr.DataArray(
        data=n_sm_rcs,
        dims=["range"],
        coords={"range": ranges_km},
        attrs={
            "name": "RangeCorrectedSignal",
            "long_name": "normalized- smoothed- range-corrected signal.",
            "units": "a.u.",
        },
    )

    attenuated_molecular_backscatter = xr.DataArray(
        data=att_beta_mol,
        dims=["range"],
        coords={"range": ranges_km},
        attrs={
            "name": "attnRayleighBSC",
            "long_name": "attenuated molecular backscatter",
            "units": "a.u.",
        },
    )

    normalized_attenuated_molecular_backscatter = xr.DataArray(
        data=n_att_beta_mol,
        dims=["range"],
        coords={"range": ranges_km},
        attrs={
            "name": "attnRayleighBSC",
            "long_name": "attenuated molecular backscatter norm",
            "units": "a.u.",
        },
    )
    dataset = xr.Dataset(
        data_vars={
            "wavelength": wavelength,
            "detection_mode": detection_mode,
            "RCS": rcs,
            "RCS_smooth": smoothed_rcs,
            "RCS_norm": n_rcs,
            "RCS_smooth_norm": normalized_smoothed_rcs,
            "BCS": attenuated_molecular_backscatter,
            "BCS_norm": normalized_attenuated_molecular_backscatter,
        },
        coords={"range": ranges_km},
        attrs={
            "lidar_location": lidar_location,
            "lidar_id": lidar_id,
            "lidar_name": rf_dataset.attrs["system"],
            "channel": channel,
            "radiosonde_location": meteo_info["radiosonde_location"],
            "radiosonde_wmo_id": meteo_info["radiosonde_wmo_id"],
            "radiosonde_datetime": meteo_info["radiosonde_datetime"],
            "datetime_ini": initial_date.strftime(
                "%Y-%m-%dT%H:%M:%S"
            ),  # FIXME: Dejar como estaba o pasar a ISO 8601?. Estaba en formato 20220808T12, ahora en 2022-08-08T12:00:00
            "datetime_end": final_date.strftime("%Y-%m-%dT%H:%M:%S"),
            "datetime_format": "%Y-%m-%dT%H:%M:%S",
            # "timestamp": final_date - initial_date,
            "duration": (final_date - initial_date).total_seconds(),
            "duration_units": "seconds",
            "rayleigh_height_limits": [z_min_km, z_max_km],
        },
    )
    dataset["range"].attrs["units"] = "km"
    dataset["range"].attrs["long_name"] = "height"

    if channel[-1] == "a" and f"dc_{channel}" in [*rf_dataset.variables.keys()]:
        dc_signal = rf_dataset[f"dc_{channel}"]
        # Normalized dc
        n_dc_signal = dc_signal / dc_signal.sel(
            range=slice(min_reference_height, max_reference_height)
        ).mean("range")

        dataset["DC"] = xr.DataArray(
            data=dc_signal.values,
            dims=["range"],
            coords={"range": ranges_km},
            attrs={
                "name": "D",
                "long_name": "dark current avg",
                "units": "a.u.",
            },
        )
        dataset["DC_norm"] = xr.DataArray(
            data=n_dc_signal.values,
            dims=["range"],
            coords={"range": ranges_km},
            attrs={
                "name": "D",
                "long_name": "dark current avg norm",
                "units": "a.u.",
            },
        )

        dataset.attrs["dark_subtracted"] = "dark-subtracted"

    return dataset


def rayleigh_fit_from_filepath(
    filepath: Path,
    channels: list[str],
    initial_hour: int | None = None,
    duration: float = 30,
    min_reference_height: float = 7000,
    max_reference_height: float = 7500,
    smooth_window: float = 250,
    crop_ranges: tuple[float, float] = (0, 30000),
    meteorology_source: str = "ecmwf",
    pressure_profile: np.ndarray
    | list
    | None = [
        3,
        5,
    ],  # TODO: Implementar definiciones por usuario
    temperature_profile: np.ndarray
    | list
    | None = [
        3,
        5,
    ],  # TODO: Implementar definiciones por usuario
    output_dir: Path | None = None,
    # ecmwf_dir_1a: Optional[Path] = None,
    data_output_dir: Path | None = None,
    figure_output_dir: Path | None = None,
    save_fig: bool = False,
):

    # Lidar preprocess
    lidar_ds = preprocess(
        filepath,
        channels=channels,
        crop_ranges=crop_ranges,
        save_dc=True,
        save_bg=True,
    )

    # time in array
    times = lidar_ds["time"].values
    times = np.array([utils.numpy_to_datetime(xx) for xx in times])

    # ranges in array
    range = lidar_ds["range"].values

    # Define initial and final date
    initial_date = dt.datetime(
        times[0].date().year, times[0].date().month, times[0].date().day
    )
    if initial_hour is None:
        initial_hour = (times[-1] - dt.timedelta(minutes=60)).hour
    if initial_hour is not None:
        initial_date = initial_date.replace(hour=initial_hour)
    else:
        raise ValueError("initial_hour not found.")
    final_date = initial_date + dt.timedelta(minutes=duration)

    # Select of period:
    rf = lidar_ds.sel(time=slice(initial_date, final_date)).mean("time")
    rf.attrs = lidar_ds.attrs

    # Get meteo profiles
    meteo_profiles, meteo_info = get_meteo(initial_date, range, meteorology_source)

    # For channel
    for channel_ in channels:
        if channel_ in rf.channel.values:
            dataset = rayleigh_fit_channel(
                channel_,
                rf,
                initial_date,
                final_date,
                meteo_profiles,
                meteo_info,
                min_reference_height,
                max_reference_height,
                smooth_window,
            )

            filepath_nc, _ = rayleigh2earlinet(dataset, output_dir=data_output_dir)

            if save_fig:
                plot_rayleigh_fit(filepath_nc, output_dir=figure_output_dir)
