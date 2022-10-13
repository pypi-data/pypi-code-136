""" Retrievals of backscatter and extinction based on Raman measurements

.. warning::
   These functions have not been tested!
"""
import numpy as np

from scipy.integrate import cumtrapz
from scipy.signal import savgol_filter

from gfatpy.atmo.atmo import molecular_extinction, number_density_at_pt


def _integrate_from_reference(integral_argument, index_reference, bin_length):
    """_summary_

    Args:
        integral_argument (np.ndarray): The argument to integrate
        index_reference (int): The index of the reference height. (bins)
        bin_length (float): The vertical bin length. (m)

    Returns:
        tau_integral (np.ndarray): The cumulative integral from the reference point.
    """
    """
    Calculate the cumulative integral the `integral_argument` from and below the reference point.

    Parameters
    ----------
    integral_argument : array_like
       The argument to integrate
    index_reference : integer
       The index of the reference height. (bins)
    bin_length : float
       The vertical bin length. (m)

    Returns
    -------
    tau_integral : array_like
       The cumulative integral from the reference point.
    """
    # Integrate from the reference point towards the beginning
    tau_integral_below = cumtrapz(
        integral_argument[: index_reference + 1][::-1], dx=-bin_length
    )[::-1]

    # Integrate from the reference point towards the end
    tau_integral_above = cumtrapz(integral_argument[index_reference:], dx=bin_length)

    # Join the arrays and set a 0 value for the reference point.
    tau_integral = np.concatenate([tau_integral_below, np.zeros(1), tau_integral_above])

    return tau_integral


def raman_extinction(
    signal: np.ndarray,
    dz: float,
    emission_wavelength: float,
    raman_wavelength: float,
    temperature: np.ndarray,
    pressure: np.ndarray,
    window_size_m: float = 100.0,
    order: int = 1,
    angstrom_aerosol: float = 1,
) -> np.ndarray | None:
    """Calculates the aerosol extinction coefficient based on pre-processed Raman signals and molecular profiles.
    The derivative is calculated using a Savitzky-Golay filter.

    Args:
    signal : (M,) array
       The range_corrected molecular signal. Should be 1D array of size M.
    dz : float
       Altitude step, used in the derivative [m]
    emission_wavelength, raman_wavelength : float
       The emission and detection wavelengths [nm]
    angstrom_aerosol : float
       The aerosol Angstrom exponent.
    temperature : (M,) array
       Atmospheric temperature profile, same shape as the lidar signal [Kelvin]
    pressure : (M,) array
       Atmospheric pressure profile, same shape as the lidar signal [Pa]
    window_size : int
       the length of the smoothing window. Must be an odd integer number.
    order : int
       The order of the polynomial used in the filtering.
       Must be less then `window_size` - 1.

    Returns:
    alpha_aer : arrays
       The aerosol extinction coefficient [m-1]

    Notes:
    The aerosol extinction coefficient is given by the formula:

    .. math::
       \alpha_{aer}(R,\lambda_0) = \frac{\frac{d}{dR}ln[\frac{N_{Ra}(R)}
       {S(R,\lambda_{Ra})}] - \alpha_{mol}(R,\lambda_0) - \alpha_{mol}(R,\lambda_{Ra})}
       {[1 + (\frac{\lambda_0}{\lambda_{Ra}})^{\alpha(R)}]}

    References
    ----------
    Ansmann, A. et al. Independent measurement of extinction and backscatter profiles
    in cirrus clouds by using a combined Raman elastic-backscatter lidar.
    Applied Optics Vol. 31, Issue 33, pp. 7113-7131 (1992)
    """
    # Calculate profiles of molecular extinction

    # pressure_pa = pressure * 100  # From hPa to Pa

    alpha_molecular_emission = molecular_extinction(
        emission_wavelength, pressure, temperature
    )
    alpha_molecular_raman = molecular_extinction(
        raman_wavelength, pressure, temperature
    )

    # Calculate number density of the target molecule
    number_density = number_density_at_pt(pressure, temperature)

    alpha_aer = retrieve_raman_extinction(
        signal,
        dz,
        emission_wavelength,
        raman_wavelength,
        alpha_molecular_emission,
        alpha_molecular_raman,
        number_density,
        window_size_m=window_size_m,
        order=order,
        angstrom_aerosol=angstrom_aerosol,
    )

    return alpha_aer


def retrieve_raman_extinction(
    signal: np.ndarray,
    dz: float,
    emission_wavelength: float,
    raman_wavelength: float,
    alpha_molecular_emission: np.ndarray,
    alpha_molecular_raman: np.ndarray,
    number_density: np.ndarray,
    window_size_m: float = 100.0,
    order: int = 1,
    angstrom_aerosol: float = 1,
) -> np.ndarray | None:
    """Calculates the aerosol extinction coefficient based on pre-processed Raman signals and molecular profiles.

    The derivative is calculated using a Savitzky-Golay filter.

    Parameters
    ----------
    signal : (M,) array
       The range-corrected molecular signal. Should be 1D array of size M.
    dz : float
       Altitude step, used in the derivative [m]
    emission_wavelength, raman_wavelength : float
       The emission and detection wavelength [nm]
    alpha_molecular_emission, alpha_molecular_raman : (M,) array
       The molecular extinction coefficient at each point of the signal profile for emission and Raman wavelength.
    number_density : (M,) array
       The number density of the scattering molecule. E.g. the number density of N2 particles for typical Raman systems.
    angstrom_aerosol: float
       The aerosol Angstrom exponent.
    window_size : int
       the length of the smoothing window. Must be an odd integer number.
    order : int
       The order of the polynomial used in the filtering.
       Must be less then `window_size` - 1.

    Returns
    -------
    alpha_aer: arrays
       The aerosol extinction coefficient [m-1]
    """

    # Ratio to apply derivative
    number_density = number_density.astype(float)
    signal = signal.astype(float)
    valid_idx = np.logical_and(number_density > 0, signal > 0)
    ratio = np.nan * np.ones(len(signal))
    ratio[valid_idx] = np.ma.log(number_density[valid_idx] / signal[valid_idx])

    window_size_bin = np.floor(window_size_m / dz).astype(int)
    derivative = savgol_filter(
        ratio, window_size_bin, order, deriv=1, delta=dz, mode="nearest", cval=np.nan
    )  # Calculate 1st derivative
    alpha_aer = (derivative - alpha_molecular_emission - alpha_molecular_raman) / (
        1 + (emission_wavelength / float(raman_wavelength)) ** angstrom_aerosol
    )

    return alpha_aer


def raman_backscatter(
    signal_raman,
    signal_emission,
    reference_idx,
    dz,
    backscatter_molecules,
    alpha_aerosol_emission,
    emission_wavelength,
    raman_wavelength,
    angstrom_aerosol,
    pressure,
    temperature,
    beta_aer_ref=0,
):
    r"""
    Calculates the aerosol backscatter coefficient based on:
    * Preprocessed elastic & raman signals.
    * The retrieved aerosol extinction coefficient.

    Parameters
    ----------
    signal_raman : (M,) array
       The range-corrected Raman signal. Should be 1D array of size M.
    signal_emission : (M, ) array
        The range-corrected elastic signal (at the emission wavelength). Should be 1D array of size M.
    reference_idx : int
        It is the index of the reference altitude to find into arrays the quantity (for example the signal) at the
        reference altitude.
    dz : float
        Altitude step, used in the integrals calculations [m]
    alpha_aerosol_emission, alpha_aer_raman : (M,) array
        The aerosol extinction coefficient at each point of the signal profile for emission and raman wavelength.
    alpha_molecular_emission, alpha_mol_raman : (M,) array
        The molecular extinction coefficient at each point of the signal profile for emission and raman wavelength.
    backscatter_molecules : (M, ) array
        The altitude range depended backscatter coefficient from molecules. Units -> [m-1]
    alpha_molecular_emission, alpha_mol_raman : (M,) array
       The molecular extinction coefficient at each point of the signal profile for emission and raman wavelength.
    pressure : (M, ) array
        Atmosphere pressure profile, same as shape as the lidar signal [Pa]
    temperature : (M, ) array
        Atmosphere temperature profile, same as shape as the lidar signal [K]
    beta_aer_ref : float
        The molecular backscatter coefficient at reference altitude.


    Returns
    -------
    backscatter_raman_aer : arrays
        The aerosol  backscatter coefficient [m-1]

    Notes
    -----
    The aerosol backscatter coefficient is given by the formula:

    .. math::
       \beta_{aer}(R,\lambda_0) = [\beta_{aer}(R_0,\lambda_0) + \beta_{mol}(R_0,\lambda_0)]
       \cdot \frac{P(R_0,\lambda_{Ra}) \cdot P(R,\lambda_0)}{P(R_0,\lambda_0) \cdot P(R,\lambda_{Ra})}
       \cdot \frac{e^{-\int_{R_0}^{R} [\alpha_{aer}(r,\lambda_{Ra}) + \alpha_{mol}(r,\lambda_{Ra})]dr}}
       {e^{-\int_{R_0}^{R} [\alpha_{aer}(r,\lambda_0) + \alpha_{mol}(r,\lambda_0)]dr}} - \beta_{mol}(R,\lambda_0)

    References
    ----------
    Ansmann, A. et al. Independent measurement of extinction and backscatter profiles
    in cirrus clouds by using a combined Raman elastic-backscatter lidar.
    Applied Optics Vol. 31, Issue 33, pp. 7113-7131 (1992)
    """

    # Calculate profiles of molecular extinction
    alpha_mol_emmision = molecular_extinction(
        emission_wavelength, pressure, temperature
    )
    alpha_mol_raman = molecular_extinction(raman_wavelength, pressure, temperature)

    alpha_aer_raman = (
        alpha_aerosol_emission
        * (raman_wavelength / emission_wavelength) ** -angstrom_aerosol
    )

    N = number_density_at_pt(pressure, temperature)

    signal_ratio = (
        signal_raman[reference_idx]
        * signal_emission
        * N
        / (signal_emission[reference_idx] * signal_raman * N[reference_idx])
    )

    alpha_tot_emission = alpha_mol_emmision + alpha_aerosol_emission
    alpha_tot_raman = alpha_mol_raman + alpha_aer_raman

    integral_raman = _integrate_from_reference(alpha_tot_raman, reference_idx, dz)
    integral_emission = _integrate_from_reference(alpha_tot_emission, reference_idx, dz)

    transmission_ratio = np.exp(-integral_raman) / np.exp(-integral_emission)

    parameter = beta_aer_ref + backscatter_molecules[reference_idx]

    backscatter_aer = -backscatter_molecules + (
        parameter * signal_ratio * transmission_ratio
    )

    return backscatter_aer
