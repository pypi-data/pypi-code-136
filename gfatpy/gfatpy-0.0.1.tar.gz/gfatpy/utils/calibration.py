from datetime import datetime

import numpy as np
import xarray as xr
import matplotlib.pyplot as plt

from gfatpy.utils import parse_datetime
from gfatpy.atmo.ecmwf import get_ecmwf_day
from gfatpy.atmo.atmo import molecular_properties


def molecular_properties_2d(
    date: datetime | str,
    heights: np.ndarray,
    times: np.ndarray,
    wavelength: float = 532,
) -> xr.Dataset:
    """A function that request ECMWF temperatures and presures for a whole day.
    Then, pipes them to `gfatpy.atmo.atmo.molecular_properties`

    Args:
        date (datetime | str): _description_
        heights (np.ndarray): _description_
        time (np.ndarray): _description_
        wavelength (float, optional): _description_. Defaults to 532.

    Returns:
        xr.Dataset: _description_
    """
    _date = parse_datetime(date)
    atmo_d = get_ecmwf_day(_date, heights=heights, times=times)

    mol_d = molecular_properties(
        wavelength,
        pressure=atmo_d.pressure.values,
        temperature=atmo_d.temperature.values,
        heights=atmo_d.range.values,
        # heights=atmo_d.time.values,
    )

    return mol_d


def iterative_fitting(
    rcs_profile: np.ndarray,
    attenuated_molecular_backscatter: np.ndarray,
    window_size_bins: int = 5,
    min_bin: int = 600,
    max_bin: int = 1000,
) -> np.ndarray:

    if rcs_profile.shape != attenuated_molecular_backscatter.shape:
        raise ValueError(f"RCS and Betta ranges must match")

    x_axis = np.arange(window_size_bins * 2)
    bool_matrix = np.full_like(rcs_profile, False, dtype=np.bool8)

    slope = []
    slope_mol = []

    for idx in np.arange(min_bin, max_bin):
        _rcs_norm = rcs_profile / rcs_profile[idx]
        _att_norm = (
            attenuated_molecular_backscatter / attenuated_molecular_backscatter[idx]
        )

        prof_slice = _rcs_norm[idx - window_size_bins : idx + window_size_bins]
        att_slice = _att_norm[idx - window_size_bins : idx + window_size_bins]

        coeff_prof = np.polyfit(np.arange(window_size_bins * 2), prof_slice, 1)
        coeff_att = np.polyfit(np.arange(window_size_bins * 2), att_slice, 1)

        slope.append(coeff_prof[0])
        slope_mol.append(coeff_att[0])

        # plt.scatter(x_axis, prof_slice, c="g")
        # plt.plot(x_axis, np.polyval(coeff_prof, x_axis), c="g")

        # plt.scatter(x_axis, att_slice, c="b")
        # plt.plot(x_axis, np.polyval(coeff_att, x_axis), c="b")

        # plt.show()

        att_data = np.polyval(coeff_att, x_axis)
        r2 = 1 - (
            ((prof_slice - att_data) ** 2).sum()
            / ((prof_slice - att_data.mean()) ** 2).sum()
        )

        # print(f'Mol m: {coeff_att[0]}')
        # print(f'Prof m: {coeff_prof[0]}')
        # if r2 > 0.25:
        #     print(f"R^2: {r2}")

    plt.plot(slope)
    plt.plot(slope_mol)

    return bool_matrix


def split_continous_measurements(
    time_array: np.ndarray, time_greater_than: float = 61
) -> list[np.ndarray]:
    """Groups times array into clusters with no more that `time_greater_than`

    Args:
        time_array (np.ndarray): _description_

    Returns:
        list[np.ndarray]: _description_
    """
    diffs = (time_array[1:] - time_array[0:-1]).astype("f") / 1e9  # type: ignore
    return np.split(time_array, np.where(diffs > time_greater_than)[0] + 1)
