import numpy as np
from scipy.integrate import cumtrapz

from loguru import logger


def klett_rcs(
    rcs_profile: np.ndarray,
    range_profile: np.ndarray,
    beta_mol_profile: np.ndarray,
    lr_aer: float = 45,
    lr_mol: float = 8 * np.pi / 3,
    ymin: float = 8000,
    ymax: float = 8500,
    beta_aer_ref: int = 0,
) -> np.ndarray:
    """Classical Klett verified with Fernald,  F.  G.:, Appl. Opt., 23, 652-653, 1984

    Args:
        rcs_profile (np.ndarray): 1D signal profile
        range_profile (np.ndarray): 1D range profile with same shape as profile
        beta_mol_profile (np.ndarray): _description_
        lr_mol (float): _description_
        lr_aer (float, optional): _description_. Defaults to 45.
        ymin (float, optional): _description_. Defaults to 8000.
        ymax (float, optional): _description_. Defaults to 8500.
        beta_aer_ref (int, optional): Aerosol backscatter at reference given (ymin and ymax). Defaults to 0.

    Returns:
        np.ndarray: Aerosol backscattering (beta)
    """
    particle_beta = np.zeros(len(range_profile))

    ytop = (np.abs(range_profile - ymax)).argmin()

    range_resolution = np.median(np.diff(range_profile))

    idx_ref = np.logical_and(range_profile >= ymin, range_profile <= ymax)

    if idx_ref.any():
        calib = np.nanmean(
            rcs_profile[idx_ref] / (beta_mol_profile[idx_ref] + beta_aer_ref)
        )
        # Calculo de backscatter cuando i<Z0
        # integer1 = np.flip(-cumtrapz(np.flip(beta_mol_profile[:ytop]),dx=range_resolution,initial=0))
        integer1 = np.flip(
            -cumtrapz(np.flip(beta_mol_profile[:ytop]), dx=range_resolution, initial=0)
        )
        integrando = rcs_profile[:ytop] * np.exp(-2 * (lr_aer - lr_mol) * integer1)
        # integer3 = np.flip(-cumtrapz(np.flip(integrando),dx=range_resolution,initial=0))
        integer3 = np.flip(
            -cumtrapz(np.flip(integrando), dx=range_resolution, initial=0)
        )
        particle_beta[:ytop] = (
            rcs_profile[:ytop] * np.exp(-2 * (lr_aer - lr_mol) * integer1)
        ) / (calib - 2 * lr_aer * integer3) - beta_mol_profile[:ytop]

    else:
        logger.error("Range [ymin,ymax] out of rcs size.")
        raise ValueError("Range [ymin,ymax] out of rcs size.")
    return particle_beta


def klett_likely_bins(
    rcs_profile: np.ndarray,
    att_mol_beta: np.ndarray,
    heights: np.ndarray,
    min_height: float = 1000,
    max_height: float = 1010,
    window_size: int = 50,
    step: int = 1,
):
    window_size // 2
    i_bin, e_bin = np.searchsorted(heights, [min_height, max_height])

    for i in np.arange(i_bin, e_bin + 1):
        rcs_profile / rcs_profile

    # return rcs_profile
