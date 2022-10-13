"""
Tomado prestado de lidar_processing.lidar_processing.helper_functions
"""
from typing import Any

import numpy as np
import pandas as pd
import xarray as xr
import scipy
from scipy import interpolate

from gfatpy.constants import k_b

# Scattering parameters according to Freudenthaler V., 2015.
Fk = {
    308: 1.05574,
    351: 1.05307,
    354.717: 1.05209,
    355: 1.05288,
    386.890: 1.05166,
    400: 1.05125,
    407.558: 1.05105,
    510.6: 1.04922,
    532: 1.04899,
    532.075: 1.04899,
    607.435: 1.04839,
    710: 1.04790,
    800: 1.04763,
    1064: 1.04721,
    1064.150: 1.04721,
}

epsilon = {
    308: 0.25083,
    351: 0.238815,
    354.717: 0.234405,
    355: 0.23796,
    386.890: 0.23247,
    400: 0.230625,
    407.558: 0.229725,
    510.6: 0.22149,
    532: 0.220455,
    532.075: 0.220455,
    607.435: 0.217755,
    710: 0.21555,
    800: 0.214335,
    1064: 0.212445,
    1064.150: 0.212445,
}

Cs = {
    308: 3.6506e-5,  # K/hPa/m
    351: 2.0934e-5,
    354.717: 2.0024e-5,
    355: 1.9957e-5,
    386.890: 1.3942e-5,
    400: 1.2109e-5,
    407.558: 1.1202e-5,
    510.6: 4.4221e-6,
    532: 3.7382e-6,
    532.075: 3.7361e-6,
    607.435: 2.1772e-6,
    710: 1.1561e-6,
    800: 7.1364e-7,
    1064: 2.2622e-7,
    1064.150: 2.2609e-7,
}

BsT = {
    308: 4.2886e-6,
    351: 2.4610e-6,
    354.717: 2.3542e-6,
    355: 2.3463e-6,
    400: 1.4242e-6,
    510.6: 5.2042e-7,
    532: 4.3997e-7,
    532.075: 4.3971e-7,
    710: 1.3611e-7,
    800: 8.4022e-8,
    1064: 2.6638e-8,
    1064.150: 2.6623e-8,
}

BsC = {
    308: 4.1678e-6,
    351: 2.3949e-6,
    354.717: 2.2912e-6,
    355: 2.2835e-6,
    400: 1.3872e-6,
    510.6: 5.0742e-7,
    532: 4.2903e-7,
    532.075: 4.2878e-7,
    710: 1.3280e-7,
    800: 8.1989e-8,
    1064: 2.5999e-8,
    1064.150: 2.5984e-8,
}

BsC_parallel = {
    308: 4.15052184e-6,
    351: 2.38547616e-06,
    354.717: 2.28368241e-06,
    355: 2.27451222e-06,
    400: 1.38198631e-06,
    510.6: 5.05563542e-07,
    532: 4.27459520e-07,
    532.075: 4.27219387e-07,
    710: 1.32322062e-07,
    800: 8.16989147e-08,
    1064: 2.59074156e-08,
    1064.150: 2.58925276e-08,
}

BsC_perpendicular = {
    308: 1.72550768e-08,
    351: 9.44466863e-09,
    354.717: 8.87554356e-09,
    355: 8.97326485e-09,
    400: 5.28492464e-09,
    510.6: 1.85714694e-09,
    532: 1.56293632e-09,
    532.075: 1.56205831e-09,
    710: 4.73100855e-10,
    800: 2.90465461e-10,
    1064: 9.13006514e-11,
    1064.150: 9.12481844e-11,
}

KbwT = {
    308: 1.01610,
    351: 1.01535,
    354.717: 1.01530,
    355: 1.01530,
    400: 1.01484,
    510.6: 1.01427,
    532: 1.01421,
    532.075: 1.01421,
    710: 1.01390,
    800: 1.01383,
    1064: 1.01371,
    1064.150: 1.01371,
}

KbwC = {
    308: 1.04554,
    351: 1.04338,
    354.717: 1.04324,
    355: 1.04323,
    400: 1.04191,
    510.6: 1.04026,
    532: 1.04007,
    532.075: 1.04007,
    710: 1.03919,
    800: 1.03897,
    1064: 1.03863,
    1064.150: 1.03863,
}

# Create interpolation function once, to avoid re-calculation (does it matter?)
f_ext = interpolate.interp1d(list(Cs.keys()), list(Cs.values()), kind="cubic")
f_bst = interpolate.interp1d(list(BsT.keys()), list(BsT.values()), kind="cubic")
f_bsc = interpolate.interp1d(list(BsC.keys()), list(BsC.values()), kind="cubic")
f_bsc_parallel = interpolate.interp1d(
    list(BsC_parallel.keys()), list(BsC_parallel.values()), kind="cubic"
)
f_bsc_perpendicular = interpolate.interp1d(
    list(BsC_perpendicular.keys()), list(BsC_perpendicular.values()), kind="cubic"
)

# Splines introduce arifacts due to limited input resolution
f_kbwt = interpolate.interp1d(list(KbwT.keys()), list(KbwT.values()), kind="linear")
f_kbwc = interpolate.interp1d(list(KbwC.keys()), list(KbwC.values()), kind="linear")


def standard_atmosphere(
    altitude: float,
    temperature_surface: float = 288.15,
    pressure_surface: float = 101325.0,
) -> tuple[float, float, float]:
    """
    Calculation of Temperature and Pressure Profiles in Standard Atmosphere.

    Parameters
    ----------
    altitude: float
       The altitude above sea level. (m)

    Returns
    -------
    pressure: float
       The atmospheric pressure. (N * m^-2 or Pa)
    temperature: float
       The atmospheric temperature. (K)
    density: float
       The air density. (kg * m^-3)

    References
    ----------
    http://home.anadolu.edu.tr/~mcavcar/common/ISAweb.pdf
    """

    # Dry air specific gas constant. (J * kg^-1 * K^-1)
    R = 287.058

    g = 9.8  # m/s^2

    # Temperature calculation.
    if altitude < 11000:
        temperature = temperature_surface - 6.5 * altitude / 1000.0
    else:
        temperature = temperature_surface - 6.5 * 11000 / 1000.0
    # Pressure calculation.
    if altitude < 11000:
        pressure = (
            pressure_surface * (1 - (0.0065 * altitude / temperature_surface)) ** 5.2561
        )
    else:
        # pressure = pressure_surface*((temperature/scaled_T[idx])**-5.2199))\
        #                       *np.exp((-0.034164*(_height - z_tmp))/scaled_T[idx])
        tropopause_pressure = (
            pressure_surface * (1 - (0.0065 * 11000 / temperature_surface)) ** 5.2561
        )
        tropopause_temperature = temperature
        pressure = tropopause_pressure * np.exp(
            -(altitude - 11000) * (g / (R * tropopause_temperature))
        )

    # Density calculation.
    density = pressure / (R * temperature)

    return pressure, temperature, density


def extend_meteo_profile(
    P: np.ndarray[Any, np.dtype[np.float64]],
    T: np.ndarray[Any, np.dtype[np.float64]],
    heights: np.ndarray[Any, np.dtype[np.float64]],
) -> pd.DataFrame:
    """If our Pressure and Temperature vectors are not the same size as our lidar data, then we include standard atmosphere values
    And if they are bigger than our data, we shorten them until they are the same size

    Args:
        P (np.ndarray[Any, np.dtype[np.float64]]): pressure vector
        T (np.ndarray[Any, np.dtype[np.float64]]): temperature vector
        heights (np.ndarray[Any, np.dtype[np.float64]]): range vector

    Returns:
        pd.DataFrame: pressure and temperature data
    """

    # standard atmosphere profile:
    Tsa = np.ones(heights.size) * np.nan
    Psa = np.ones(heights.size) * np.nan
    for i, _height in enumerate(heights):
        sa = standard_atmosphere(_height)
        Psa[i] = sa[0]
        Tsa[i] = sa[1]

    if P.size == Psa.size:  # if they are the same size, we leave them be
        extended_P = P
    elif (
        P.size > Psa.size
    ):  # If our pressure vector is bigger than 'heights', we make it the same size
        maxsa = Psa.size
        extended_P = np.ones(heights.size) * np.nan
        for i in range(maxsa):
            extended_P[i] = P[i]
    else:  # if we don't have enough data to make a full pressure profile
        extended_P = P
        maxh = P.size  # number of the last data
        for i in range(Psa.size - maxh):
            extended_P = np.append(
                extended_P, Psa[maxh + i]
            )  # we use standard atmosphere as our pressure profile

    if T.size == Tsa.size:  # if they are the same size, we leave them be
        extended_T = T
    elif (
        T.size > Tsa.size
    ):  # If our temperature vector is bigger than 'heights', we make it the same size
        maxsa = Tsa.size
        extended_T = np.ones(heights.size) * np.nan
        for i in range(maxsa):
            extended_T[i] = T[i]
    else:  # if we don't have enough data to make a full temperature profile
        extended_T = T
        maxh = T.size  # number of the last data
        for i in range(Tsa.size - maxh):
            extended_T = np.append(
                extended_T, Tsa[maxh + i]
            )  # we use standard atmosphere as our temperature profile

    # atmospheric_profiles = xr.Dataset(
    #     {"pressure": (["range"], extended_P), "temperature": (["range"], extended_T)},
    #     coords={"range": heights},
    # )
    atmospheric_profiles = pd.DataFrame(
        {
            "height": heights,
            "temperature": extended_T,
            "pressure": extended_P,
        }
    )

    return atmospheric_profiles


# def extend_scaled_meteo_profiles(radiosonde, heights):
#     """
#     If maximum radiosonde height is below the lidar range,
#     scaled standard atmosphere is used to fulfill the profiles.

#     Parameters
#     ----------
#     radiosonde: xarray.Dataset
#         from grawmet_reader (xarray.Dataset)
#     heights: array
#         lidar ranges (m)

#     Returns
#     -------
#     atmospheric_profiles: xarray.Dataset
#         pressure and temperature data (xarray dataset)
#     """

#     # standard atmosphere profile:
#     Tsa = np.ones(heights.size) * np.nan
#     Psa = np.ones(heights.size) * np.nan
#     for i, _height in enumerate(heights):
#         sa = atmo.standard_atmosphere(_height)
#         Psa[i] = sa[0]
#         Tsa[i] = sa[1]
#     max_sonde_idx = np.squeeze(
#         np.where(np.max(radiosonde["range"].values) == radiosonde["range"].values)
#     )

#     # Reindex Sonde Heights to Lidar Ranges
#     meteo_profiles = radiosonde.interp(
#         range=heights, kwargs={"fill_value": "extrapolate"}
#     )
#     interp_sonde_range = meteo_profiles["range"].values
#     top_pressure_idx = np.squeeze(
#         np.where(
#             abs(interp_sonde_range - radiosonde["range"].values[max_sonde_idx])
#             == abs(interp_sonde_range - radiosonde["range"].values[max_sonde_idx]).min()
#         )[0]
#     )
#     top_pressure_val = np.squeeze(
#         interp_sonde_range[
#             abs(interp_sonde_range - radiosonde["range"].values[max_sonde_idx])
#             == abs(interp_sonde_range - radiosonde["range"].values[max_sonde_idx]).min()
#         ]
#     )
#     top_temperature_val = meteo_profiles["temperature"].values[top_pressure_idx]

#     # Radiosonde data:
#     bottom_T = meteo_profiles["temperature"].values[0:top_pressure_idx]
#     bottom_P = (
#         meteo_profiles["pressure"].values[0:top_pressure_idx] * 100
#     )  # Convert to Pa

#     # Extended profile with scaled standard atmosphere:
#     extension_Tsa = Tsa[top_pressure_idx:]
#     extension_Psa = Psa[top_pressure_idx:]
#     up_T = bottom_T[-1] * (extension_Tsa / Tsa[top_pressure_idx])
#     up_P = bottom_P[-1] * (extension_Psa / Psa[top_pressure_idx])

#     extended_T = np.concatenate([bottom_T, up_T])
#     extended_P = np.concatenate([bottom_P, up_P])

#     atmospheric_profiles = xr.Dataset(
#         {"pressure": (["range"], extended_P), "temperature": (["range"], extended_T)},
#         coords={"range": heights},
#     )
#     return atmospheric_profiles


def transmittance(
    alpha: np.ndarray[Any, np.dtype[np.float64]],
    heights: np.ndarray[Any, np.dtype[np.float64]],
) -> np.ndarray[Any, np.dtype[np.float64]]:
    """
    Transmittance = exp[-integral{alpha*dz}_[0,z]]

    Parameters
    ----------
    alpha: array
        extinction profile
    heights: array
        heights profile

    Returns
    -------
    transmittance: array
         transmittance

    """

    delta_height = np.median(np.diff(heights))
    integrated_extinction = scipy.integrate.cumtrapz(alpha, initial=0, dx=delta_height)
    return np.exp(-integrated_extinction)


def molecular_properties(
    wavelength: float,
    pressure: np.ndarray[Any, np.dtype[np.float64]],
    temperature: np.ndarray[Any, np.dtype[np.float64]],
    heights: np.ndarray[Any, np.dtype[np.float64]],
    component: str = "total",
) -> xr.Dataset:
    """
    Molecular Attenuated  Backscatter: beta_mol_att = beta_mol * Transmittance**2

    Parameters
    ----------
    wavelength: int, float
        wavelength of our desired beta molecular attenuated
    pressure: array
        pressure profile
    temperature: array
        temperature profile
    heights: array
        heights profile

    Returns
    -------
    beta_molecular_att: array
        molecular attenuated backscatter profile
    """

    """ molecular backscatter and extinction """
    beta_mol = molecular_backscatter(
        wavelength, pressure, temperature, component=component
    )
    alfa_mol = molecular_extinction(wavelength, pressure, temperature)
    lr_mol = molecular_lidar_ratio(wavelength)

    """ transmittance """
    transmittance_array = transmittance(alfa_mol, heights)

    """ attenuated molecular backscatter """
    att_beta_mol = attenuated_backscatter(beta_mol, transmittance_array)

    mol_properties = xr.Dataset(
        {
            "molecular_beta": (["range"], beta_mol),
            "molecular_alpha": (["range"], alfa_mol),
            "attenuated_molecular_beta": (["range"], att_beta_mol),
            "molecular_lidar_ratio": lr_mol,
        },
        coords={"range": heights},
    )

    return mol_properties


def molecular_backscatter(
    wavelength: float,
    pressure: np.ndarray[Any, np.dtype[np.float64]],
    temperature: np.ndarray[Any, np.dtype[np.float64]],
    component: str = "total",
) -> np.ndarray[Any, np.dtype[np.float64]]:
    """
    Molecular backscatter calculation.

    Parameters
    ----------
    wavelength : float
       The wavelength of the radiation in air. From 308 to 1064.15
    pressure : float
       The atmospheric pressure. (Pa)
    temperature : float
       The atmospheric temperature. (K)
    component : str
       One of 'total' or 'cabannes'.

    Returns
    -------
    beta_molecular: float
       The molecular backscatter coefficient. (m^-1 * sr^-1)

    References
    ----------
    Freudenthaler, V. Rayleigh scattering coefficients and linear depolarization
    ratios at several EARLINET lidar wavelengths. p.6-7 (2015)
    """
    if component not in [
        "total",
        "cabannes",
        "cabannes_parallel",
        "cabannes_perpendicular",
    ]:
        raise ValueError(
            "Molecular backscatter available only for 'total' or 'cabannes' component."
        )

    if component == "total":
        bs_function = f_bst
    elif component == "cabannes":
        bs_function = f_bsc
    elif component == "cabannes_parallel":
        bs_function = f_bsc_parallel
    elif component == "cabannes_perpendicular":
        bs_function = f_bsc_perpendicular
    else:
        raise ValueError(f"{component} not found.")

    Bs = bs_function(wavelength)

    # Convert pressure to correct units for calculation. (Pa to hPa)
    pressure = pressure / 100.0

    # Calculate the molecular backscatter coefficient.
    beta_molecular = Bs * pressure / temperature

    return beta_molecular


def molecular_lidar_ratio(wavelength: float, component: str = "total") -> float:
    """
    Molecular lidar ratio.

    Parameters
    ----------
    wavelength : float
       The wavelength of the radiation in air. From 308 to 1064.15
    component : str
       One of 'total' or 'cabannes'.

    Returns
    -------
    lidar_ratio_molecular : float
       The molecular backscatter coefficient. (m^-1 * sr^-1)

    References
    ----------
    Freudenthaler, V. Rayleigh scattering coefficients and linear depolarization
    ratios at several EARLINET lidar wavelengths. p.6-7 (2015)
    """
    if component not in ["total", "cabannes"]:
        raise ValueError(
            "Molecular lidar ratio available only for 'total' or 'cabannes' component."
        )

    if component == "total":
        k_function = f_kbwt
    else:
        k_function = f_kbwc

    Kbw = k_function(wavelength)

    lidar_ratio_molecular = 8 * np.pi / 3.0 * Kbw

    return lidar_ratio_molecular


def molecular_extinction(
    wavelength: float,
    pressure: np.ndarray[Any, np.dtype[np.float64]],
    temperature: np.ndarray[Any, np.dtype[np.float64]],
) -> np.ndarray[Any, np.dtype[np.float64]]:
    """
    Molecular extinction calculation.

    Parameters
    ----------
    wavelength : float
       The wavelength of the radiation in air. From 308 to 1064.15
    pressure : float
       The atmospheric pressure. (Pa)
    temperature : float
       The atmospheric temperature. (K)

    Returns
    -------
    alpha_molecular: float
       The molecular extinction coefficient. (m^-1)

    References
    ----------
    Freudenthaler, V. Rayleigh scattering coefficients and linear depolarization
    ratios at several EARLINET lidar wavelengths. p.6-7 (2015)
    """
    cs = f_ext(wavelength)

    # Convert pressure to correct units for calculation. (Pa to hPa)
    pressure = pressure / 100.0

    # Calculate the molecular backscatter coefficient.
    alpha_molecular = cs * pressure / temperature

    return alpha_molecular


def attenuated_backscatter(
    backscatter: np.ndarray[Any, np.dtype[np.float64]],
    transmittance: np.ndarray[Any, np.dtype[np.float64]],
) -> np.ndarray[Any, np.dtype[np.float64]]:
    """Calculate Attenuated Backscatter

    Args:
        backscatter ([type]): [description]
        transmittance ([type]): [description]
    """

    return backscatter * transmittance**2


def number_density_at_pt(
    pressure: float | np.ndarray, temperature: float | np.ndarray
) -> np.ndarray:
    """Calculate the number density for a given temperature and pressure.

    This method does not take into account the compressibility of air.

    Parameters
    ----------
    pressure: float or array
       Pressure in Pa
    temperature: float or array
       Temperature in K

    Returns
    -------
    n: array or array
       Number density of the atmosphere [m-3]
    """
    # p_pa = pressure * 100.  # Pressure in pascal

    n = pressure / (temperature * k_b)

    return n


def extrapolate_aod(
    wv1: float,
    wv2: float,
    aod2: np.ndarray[Any, np.dtype[np.float64]],
    ae: float,
) -> np.ndarray[Any, np.dtype[np.float64]]:
    """_summary_

    Extrapolates AOD at given wavelength using AOD at near wavelength and an appropriate Angstrom Exponent
    The Equation
    .. math::
        aod_{\\lambda_1} = aod_{\\lambda_2} \\cdot \\dfrac{\\lambda_1}{\\lambda_2} \\cdot AE(\\lambda_x - \\lambda_y)

    Args:
        wv1 (_type_): _description_
        wv2 (_type_): _description_
        aod2 (_type_): _description_
        ae (_type_): _description_
    """

    return aod2 * (wv1 / wv2) ** (-ae)


def interpolate_aod(
    wv_arr: float, aod_arr: np.ndarray[Any, np.dtype[np.float64]], wv0: float
) -> np.ndarray[Any, np.dtype[np.float64]]:
    """
    Fit log_wv, log_aod to 2nd-order Polynomial [O'Neill et al., 2001]

    Args:
        wv_arr (_type_): _description_
        aod_arr (_type_): _description_
        wv0 (_type_): _description_
    """

    y = np.log(aod_arr)
    x = np.log(wv_arr)

    coeff = np.polyfit(x, y, 2, full=True)
    # rr = np.sum( (y - np.polyval(coeff[0], x)) **2) # residuals
    if coeff[1][0].squeeze() < 0.1:
        aod0 = np.exp(np.polyval(coeff[0], np.log(wv0)))
    else:
        raise ValueError("Fit not appropiate.")

    return aod0


def calculate_angstrom_exponent(
    wv1: float, wv2: float, aod1: float | np.ndarray, aod2: float | np.ndarray
) -> float | np.ndarray:
    """Retrieve Ansgstrom exponent using:
    .. math::
        $aod_{\\lambda_1} = aod_{\\lambda_2} \\cdot \\dfrac{\\lambda_1}{\\lambda_2} \\cdot AE(\\lambda_x - \\lambda_y)$

    Args:
        wv1 (float): first wavelength
        wv2 (float): second wavelength
        aod1 (float | np.ndarray): AOD at first wavelength
        aod2 (float | np.ndarray): AOD at second wavelength

    Returns:
        float | np.ndarray: angstrom exponent coefficient
    """
    return -(np.log(aod1 / aod2)) / (np.log(wv1 / wv2))
