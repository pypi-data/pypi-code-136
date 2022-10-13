import numpy as np
import xarray as xr

from gfatpy.lidar.utils import LIDAR_INFO
from gfatpy.lidar import file_manager


def backscattering_ratio(
    molecular_backscatter: np.ndarray, particle_backscatter: np.ndarray
) -> np.ndarray:
    """Retrieves the backscattering ratio. Inputs must be in the same units.

    Args:
        molecular_backscatter (np.ndarray): Molecular backscatter coefficient.
        particle_backscatter (np.ndarray):  Particle backscatter coefficient.

    Returns:
        np.ndarray: backscattering ratio
    """

    return molecular_backscatter + particle_backscatter / molecular_backscatter


def linear_volume_depolarization_ratio(
    signal_R: np.ndarray,
    signal_T: np.ndarray,
    channel_R: str,
    channel_T: str,
    range: np.ndarray,
    time: np.ndarray,
    eta: float = 1,
    K: float = 1,
    GT: float = 1,
    HT: float = -1,
    GR: float = 1,
    HR: float = 1,
) -> xr.DataArray:
    """Calculate the linear volume depolarization ratio.

    Args:
        signal_R (np.ndarray): reflected signal in the polarizing beam splitter cube.
        signal_T (np.ndarray): transmitted signal in the polarizing beam splitter cube.
        channel_R (str): reflected channel in the polarizing beam splitter cube.
        channel_T (str): transmitted channel in the polarizing beam splitter cube.
        range (np.ndarray): range series of the signal.
        time (np.ndarray): time vector of the signal.
        eta (float, optional): calibration factor retrieved with Delta90 method. Defaults to 1.
        K (float, optional): K factor value simulated with Volker's algorithm. Defaults to 1.
        GT (float, optional): GT factor value simulated with Volker's algorithm. Defaults to 1.
        HT (float, optional): HT factor value simulated with Volker's algorithm. Defaults to -1.
        GR (float, optional): GR factor value simulated with Volker's algorithm. Defaults to 1.
        HR (float, optional): HR factor value simulated with Volker's algorithm. Defaults to 1.

    Raises:
        ValueError: Wavelength, telescope or mode does not fit raises 'Polarized channels to be merged not appropiated'.
        ValueError: polarization codes do not fit raises 'Polarized channels to be merged not appropiated'.

    Returns:
        xr.DataArray: linear_volume_depolarization_ratio
    """

    wavelengthR, telescopeR, polR, modeR = file_manager.channel2info(channel_R)
    wavelengthT, telescopeT, polT, modeT = file_manager.channel2info(channel_T)

    if wavelengthR != wavelengthT or telescopeR != telescopeT or modeR != modeT:
        raise ValueError("Polarized channels to be merged not appropiated.")

    if polT not in ["p", "c", "s"] or polR not in ["p", "c", "s"] and polR != polT:
        raise ValueError("Polarized channels to be merged not appropiated.")

    eta = eta / K
    ratio = (signal_R / signal_T) / eta
    lvdr_ = (((GT + HT) * ratio - (GR + HR)) / ((GR - HR) - (GT - HT) * ratio)).astype(
        float
    )

    # Create DataArray
    lvdr = xr.DataArray(
        lvdr_,
        coords={"time": time, "range": range},
        dims=["time", "range"],
        attrs={
            "long_name": "Linear Volume Depolarization Ratio",
            "detection_mode": LIDAR_INFO["metadata"]["code_mode_str2number"][modeR],
            "wavelength": wavelengthR,
            "units": "$\\#$",
        },
    )

    return lvdr


def particle_depolarization(
    linear_volume_depolarization_ratio: np.ndarray,
    backscattering_ratio: np.ndarray,
    molecular_depolarization: float,
    time: np.ndarray,
    range: np.ndarray,
) -> np.ndarray:
    """Calculate the linear particle depolarization ratio.

    Args:
        linear_volume_depolarization_ratio (np.ndarray): linear volume depolarization ratio
        backscattering_ratio (np.ndarray): _description_
        molecular_depolarization (float): molecular linear volume depolarization ratio
        time (np.ndarray): time vector of the signal.
        range (np.ndarray): range series of the signal.

    Returns:
        np.ndarray: linear particle depolarization ratio.

    Notes:
    The linear particle depolarization ratio is calculated by the formula:

    .. math::
       \delta^p = \frac{(1 + \delta^m)\delta^V \mathbf{R} - (1 + \delta^V)\delta^m}
       {(1 + \delta^m)\mathbf{R} - (1 + \delta^V)}


    References:
    Freudenthaler, V. et al. Depolarization ratio profiling at several wavelengths in pure
    Saharan dust during SAMUM 2006. Tellus, 61B, 165-179 (2008)
    """

    delta_p = (
        (1 + molecular_depolarization)
        * linear_volume_depolarization_ratio
        * backscattering_ratio
        - (1 + linear_volume_depolarization_ratio) * molecular_depolarization
    ) / (
        (1 + molecular_depolarization) * backscattering_ratio
        - (1 + linear_volume_depolarization_ratio)
    )

    # Create DataArray
    delta_p_xarray = xr.DataArray(
        delta_p,
        coords={"time": time, "range": range},
        dims=["time", "range"],
        attrs={
            "long_name": "Linear Volume Depolarization Ratio",
            "units": "$\\#$",
        },  # TODO: decide where the attributes should be included.
    )
    return delta_p_xarray
