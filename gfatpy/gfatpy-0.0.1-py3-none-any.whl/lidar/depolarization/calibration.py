from pathlib import Path
from pdb import set_trace
import numpy as np
import xarray as xr
from scipy import stats
from datetime import datetime

from gfatpy import DATA_DN
from gfatpy.lidar import file_manager
from gfatpy.lidar.utils import LIDAR_INFO

from gfatpy.lidar.preprocessing.lidar_preprocessing import preprocess


def retrieve_eta_star_profile(
    signal_T_plus45: xr.DataArray,
    signal_T_minus45: xr.DataArray,
    signal_R_plus45: xr.DataArray,
    signal_R_minus45: xr.DataArray,
    transmittance_extra_filter: float,
) -> xr.DataArray:
    """Calculate the calibration constant [eta_star] in a lidar system that is able to
    detect the T-to-R depolarization ratio.

    Args:
        signal_T_plus45 (xr.DataArray): The input vertical profile from the T channel. Calibrator angle phi=45.
        signal_T_minus45 (xr.DataArray): The input vertical profile from the R channel. Calibrator angle phi=45.
        signal_R_plus45 (xr.DataArray): The input vertical profile from the T channel. Calibrator angle phi=-45.
        signal_R_minus45 (xr.DataArray): The input vertical profile from the R channel. Calibrator angle phi=-45.
        kwargs (dict): transmittance_extra_filter [float] is the transmittance of the extra filter during depol. calibration.

    Returns:
        xr.DataArray: eta star profile.

    Notes:
        The calibration constant is calculated by the following formula:
    .. math::
        \\eta^* = \\left( \\frac{signal(T,+45)}{signal(R,+45)}\\frac{signal(T,-45)}{signal(R,-45)} \\right)^{0.5}

    References:
    Freudenthaler, V. 2016. https://doi.org/10.5194/amt-9-4181-2016
    """

    # Remove effect of the possible extra filter to avoid saturation of the s-channel.
    signal_T_plus45_with_extra_filter = signal_T_plus45
    signal_T_plus45 = signal_T_plus45_with_extra_filter / transmittance_extra_filter
    signal_T_minus45_with_extra_filter = signal_T_minus45
    signal_T_minus45 = signal_T_minus45_with_extra_filter / transmittance_extra_filter

    #   Calculate the signal ratio for the +45 position.
    delta_v45_plus = (signal_T_plus45 / signal_R_plus45).mean("time")

    #   Calculate the signal ratio for the -45 position.
    delta_v45_minus = (signal_T_minus45 / signal_R_minus45).mean("time")

    #   Calculate the calibration constant vertical profile.
    v_star_profile = (delta_v45_plus * delta_v45_minus) ** 0.5
    return v_star_profile


def eta_star_mean_std(
    eta_star_profile: xr.DataArray, min_range: float, max_range: float
) -> tuple[float, float]:
    """Calculate the mean calibration constant and its standard error of the mean, from the calibration constant profile.

    Args:
    c_profile: vector
       The vertical profile of the calibration constant.
    kwargs (dict): min_range [float] is the lower vertical limit for the calculation in meters. max_range [float] is the upper vertical limit for the calculation in meters.

    Returns:
    c_mean: float
       Calibration constant's mean value (vertical axis).
    c_sem: float
       Calibration constant's standard error of the mean (vertical axis).
    """

    if "time" in eta_star_profile.dims:
        raise ValueError("eta_star_profile should have only `range` dimension.")

    #   Select the area of interest.
    eta_star_mean = (
        eta_star_profile.sel(range=slice(min_range, max_range))
        .mean("range")
        .values.item()
    )
    eta_star_std = (
        eta_star_profile.sel(range=slice(min_range, max_range))
        .std("range")
        .values.item()
    )

    #   Return the statistics.
    return eta_star_mean, eta_star_std


def calibration_factor_files(
    P45_fn: Path,
    N45_fn: Path,
    calib_dir: Path | None,
    min_range: float = 1500,
    max_range: float = 3000,
    transmittance_extra_filter: float = 1.0,
) -> xr.Dataset:

    if not P45_fn.is_file():
        raise FileNotFoundError(f"{P45_fn} not found.")

    if not N45_fn.is_file():
        raise FileNotFoundError(f"{N45_fn} not found.")

    lidar_nick, _, _, _, telescope_, calib_date = file_manager.filename2info(
        P45_fn.name
    )
    lidar_name: str = LIDAR_INFO["metadata"]["nick2name"][lidar_nick]

    P45 = preprocess(P45_fn, **{"force_dc_in_session": False})
    N45 = preprocess(N45_fn, **{"force_dc_in_session": False})

    calib_dict = {}
    calib_dict[telescope_] = {}
    for wavelength_ in LIDAR_INFO["lidars"][f"{lidar_name}"]["polarized_channels"][
        telescope_
    ].keys():
        calib_dict[telescope_][wavelength_] = {}
        for mode_ in LIDAR_INFO["lidars"][f"{lidar_name}"]["polarized_channels"][
            telescope_
        ][wavelength_].keys():
            channel_T = LIDAR_INFO["lidars"][f"{lidar_name}"]["polarized_channels"][
                telescope_
            ][wavelength_][mode_]["T"]
            channel_R = LIDAR_INFO["lidars"][f"{lidar_name}"]["polarized_channels"][
                telescope_
            ][wavelength_][mode_]["R"]

            if (
                channel_T not in P45.channel.values
                or channel_R not in P45.channel.values
            ):
                continue

            if (
                channel_T not in N45.channel.values
                or channel_R not in N45.channel.values
            ):
                continue

            calib_dict[telescope_][wavelength_][mode_] = {}

            signal_R_P45 = P45[f"signal_{channel_R}"]
            signal_T_P45 = P45[f"signal_{channel_T}"]
            signal_R_N45 = N45[f"signal_{channel_R}"]
            signal_T_N45 = N45[f"signal_{channel_T}"]

            eta_star_profile = retrieve_eta_star_profile(
                signal_T_P45,
                signal_T_N45,
                signal_R_P45,
                signal_R_N45,
                transmittance_extra_filter=transmittance_extra_filter,
            )
            calib_dict[telescope_][wavelength_][mode_]["profile"] = eta_star_profile

            eta_star_mean, eta_star_std = eta_star_mean_std(
                eta_star_profile, min_range=min_range, max_range=max_range
            )
            calib_dict[telescope_][wavelength_][mode_]["values"] = [
                eta_star_mean,
                eta_star_std,
            ]
            
    # Create dataset
    calib_dataset = xr.Dataset()
    for wavelength_ in calib_dict[telescope_].keys():
        for mode_ in calib_dict[telescope_][wavelength_].keys():
            key_profile = f"eta_star_profile_{wavelength_}{telescope_[0]}{mode_}"
            calib_dataset[key_profile] = calib_dict[telescope_][wavelength_][mode_][
                "profile"
            ]

            eta_star_mean, eta_star_std = calib_dict[telescope_][wavelength_][mode_][
                "values"
            ]
            calib_dataset[
                f"eta_start_mean_{wavelength_}{telescope_[0]}{mode_}"
            ] = xr.DataArray(
                eta_star_mean,
                dims=[],
                attrs={
                    "long_name": f"range-average of {key_profile}",
                    "min_range_m": min_range,
                    "max_range_m": max_range,
                },
            )
            calib_dataset[
                f"eta_start_standard_deviation_{wavelength_}{telescope_[0]}{mode_}"
            ] = xr.DataArray(
                eta_star_std,
                dims=[],
                attrs={
                    "long_name": f"range standard-deviation of {key_profile}",
                    "min_range_m": min_range,
                    "max_range_m": max_range,
                },
            )
    set_trace()
    
    calib_datetime_str = datetime.strftime(calib_date, "%Y%m%d_%H%M")
    if calib_dir is None:
        if DATA_DN is not None:
            calib_dir = (
                DATA_DN
                / lidar_name
                / "QA"
                / "depolarization_calibration"
                / f"{calib_date.year:04d}"
                / f"{calib_date.month:02d}"
                / f"{calib_date.day:02d}"
                / f"{calib_datetime_str}"
            )
            calib_dir.mkdir(parents=True, exist_ok=True)
        else:
            raise NotADirectoryError("DATA_DN is None.")
    else:
        if not calib_dir.is_dir():
            raise FileNotFoundError(f"{calib_dir} not found.")

    calib_filename = f"mhc_eta-star_{calib_datetime_str}.nc"
    calib_dataset.to_netcdf(calib_dir / calib_filename)
    return calib_dataset
