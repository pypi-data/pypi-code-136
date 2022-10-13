import os
from pathlib import Path
from typing import overload
import numpy as np
from datetime import datetime

from scipy.signal import savgol_filter
from scipy.integrate import cumulative_trapezoid
import xarray as xr

from .types import ParamsDict, LidarInfoType
from gfatpy.atmo import atmo, ecmwf
from gfatpy.utils.io import read_yaml

""" MODULE For General Lidar Utilities
"""

# LIDAR SYSTEM INFO
INFO_FILE = Path(__file__).parent.absolute() / "info.yml"
LIDAR_INFO: LidarInfoType = read_yaml(INFO_FILE)

INFO_PLOT_FILE = Path(__file__).parent.absolute() / "plot" / "info.yml"
LIDAR_PLOT_INFO = read_yaml(INFO_PLOT_FILE)


@overload
def signal_to_rcs(signal: xr.DataArray, ranges: xr.DataArray) -> xr.DataArray:
    ...


@overload
def signal_to_rcs(signal: np.ndarray, ranges: np.ndarray) -> np.ndarray:
    ...


def signal_to_rcs(signal, ranges):
    return signal * ranges**2


@overload
def rcs_to_signal(rcs: xr.DataArray, ranges: xr.DataArray) -> xr.DataArray:
    ...


@overload
def rcs_to_signal(rcs: np.ndarray, ranges: np.ndarray) -> np.ndarray:
    ...


def rcs_to_signal(rcs, ranges):
    return rcs / ranges**2


def smooth_signal(signal, method="savgol", savgol_kwargs: dict | None = None):
    """Smooth Lidar Signal

    Args:
        signal ([type]): [description]
        method (str, optional): [description]. Defaults to 'savgol'.
    """

    if method == "savgol":
        if savgol_kwargs is None:
            savgol_kwargs = {"window_length": 21, "polyorder": 2}
        smoothed_signal = savgol_filter(signal, **savgol_kwargs)
    else:
        raise NotImplementedError(f"{method} has not been implemented yet")

    return smoothed_signal


def estimate_snr(signal, window=5):
    """[summary]

    Args:
        signal ([type]): [description]
    """

    # ventana: numero impar
    if window % 2 == 0:
        window += 1
    subw = window // 2

    n = len(signal)
    avg = np.zeros(n) * np.nan
    std = np.zeros(n) * np.nan

    for i in range(n):
        ind_delta_min = i - subw if i - subw >= 0 else 0
        ind_delta_max = i + subw if i + subw < n else n - 1

        si = signal[ind_delta_min : (ind_delta_max + 1)]
        avg[i] = np.nanmean(si)
        std[i] = np.nanstd(si)

        # print("%i, %i, %i" % (i, ind_delta_min, ind_delta_max + 1))
        # print(signal[ind_delta_min:(ind_delta_max+1)])
    snr = avg / std

    return snr, avg, std


def get_lidar_name_from_filename(fn):
    """Get Lidar System Name from L1a File Name
    Args:
        fn (function): [description]
    """
    lidar_nick = os.path.basename(fn).split("_")[0]
    if lidar_nick in LIDAR_INFO["metadata"]["nick2name"].keys():
        lidar = lidar_nick
    else:
        lidar = None
    return lidar


def sigmoid(x, x0, k, coeff: float = 1, offset: float = 0):
    y = 1 / (1 + np.exp(-k * (x - x0)))
    return (coeff * y) + offset


def extrapolate_beta_with_angstrom(
    beta_ref: np.ndarray,
    wavelength_ref: float,
    wavelength_target: float,
    angstrom_exponent: float | np.ndarray,
) -> np.ndarray:
    return beta_ref * (wavelength_target / wavelength_ref) ** -angstrom_exponent


def generate_particle_backscatter(
    ranges: np.ndarray,
    wavelength: float,
    fine_ae: float,
    coarse_ae: float,
    fine_beta532: float = 2.5e-6,
    coarse_beta532: float = 2.0e-6,
) -> np.ndarray:
    """_summary_

    Args:
        ranges (np.ndarray): _description_
        wavelength (float): _description_
        fine_ae (float): _description_
        coarse_ae (float): _description_
        fine_beta532 (float, optional): _description_. Defaults to 2.5e-6.
        coarse_beta532 (float, optional): _description_. Defaults to 2.0e-6.

    Returns:
        np.ndarray: _description_
    """

    beta_part_fine = sigmoid(
        ranges, 2500, 1 / 60, coeff=-fine_beta532, offset=fine_beta532
    )
    beta_part_coarse = sigmoid(
        ranges, 5000, 1 / 60, coeff=-coarse_beta532, offset=coarse_beta532
    )

    beta_part_fine = extrapolate_beta_with_angstrom(
        beta_part_fine, 532, wavelength, 1.5
    )

    return beta_part_fine + beta_part_coarse


def generate_synthetic_signal(
    ranges: np.ndarray,
    wavelength: float = 532,
    wavelength_raman: float | None = None,
    overlap_midpoint: float = 600,
    k_lidar: float = 4e9,
    paralell_perpendicular_ratio: float = 0.33,
    particle_lr: float = 45,
    force_zero_aer_after_bin: int | None = None,
) -> tuple[np.ndarray, np.ndarray | None, ParamsDict]:
    """_summary_

    Args:
        ranges (np.ndarray): _description_
        wavelength (float, optional): _description_. Defaults to 532.
        overlap_midpoint (float, optional): _description_. Defaults to 600.
        k_lidar (float, optional): _description_. Defaults to 4e9.
        wavelength_raman (float | None, optional): _description_. Defaults to None.
        paralell_perpendicular_ratio (float, optional): _description_. Defaults to 0.33.
        particle_lratio (float, optional): _description_. Defaults to 45.
        force_zero_aer_after_bin (int | None, optional): _description_. Defaults to None.

    Returns:
        tuple[np.ndarray, ParamsDict]: _description_
    """

    z = ranges

    # Overlap
    overlap = sigmoid(
        z,
        overlap_midpoint,
        1 / 50,
        offset=0,
    )

    overlap[overlap < 9e-3] = 0
    overlap[overlap > 0.999] = 1

    # Molecular elastic
    ecmwf_data = ecmwf.get_ecmwf_temperature_preasure(datetime(2022, 9, 3), heights=z)
    atmo_data = atmo.molecular_properties(
        wavelength, ecmwf_data.pressure, ecmwf_data.temperature, heights=z
    )

    beta_mol = atmo_data["molecular_beta"].values
    alpha_mol = atmo_data["molecular_alpha"].values

    # Particle elastic
    # 0.33 para polvo desértico
    # 0.0034 para parte molecular
    # Calcular beta_part parallel = total*(1-0.33)
    # Calcular beta_part perpendicular = total*(0.33)
    # Análogo con otro coeficiente para la parte molecular

    fine_ae = 1.5
    coarse_ae = 0

    beta_part = generate_particle_backscatter(
        ranges, wavelength, fine_ae=fine_ae, coarse_ae=coarse_ae
    )
    alpha_part = particle_lr * beta_part

    part_accum_ext = cumulative_trapezoid(alpha_part, z, initial=0)
    mol_accum_ext = cumulative_trapezoid(alpha_mol, z, initial=0)
    # accumulated_extinction = cumulative_trapezoid(alpha_part + alpha_mol, z, initial=0) # TODO: separate part and mol
    T_elastic = np.exp(-part_accum_ext - mol_accum_ext)  # type: ignore

    P_elastic = k_lidar * (overlap / z**2) * (beta_part + beta_mol) * T_elastic**2

    params: ParamsDict = {
        "particle_alpha": alpha_part,
        "particle_beta": beta_part,
        "molecular_alpha": alpha_mol,
        "molecular_beta": beta_mol,
        "molecular_beta_att": atmo_data["attenuated_molecular_beta"].values,
        "particle_accum_ext": part_accum_ext,
        "molecular_accum_ext": mol_accum_ext,
        "transmittance": T_elastic,
        "overlap": overlap,
        "k_lidar": k_lidar,
        "angstrom_exponent_coarse": coarse_ae,
        "angstrom_exponent_fine": fine_ae,
    }

    if wavelength_raman is not None:
        atmo_data = atmo.molecular_properties(
            wavelength_raman, ecmwf_data.pressure, ecmwf_data.temperature, heights=z
        )
        beta_mol_raman = atmo_data["molecular_beta"]
        alpha_mol_raman = atmo_data["molecular_alpha"]

        beta_part_raman = generate_particle_backscatter(
            ranges, wavelength_raman, fine_ae=fine_ae, coarse_ae=coarse_ae
        )
        alpha_part_raman = particle_lr * beta_part_raman

        part_accum_ext_raman = cumulative_trapezoid(alpha_part_raman, z, initial=0)
        mol_accum_ext_raman = cumulative_trapezoid(alpha_mol_raman, z, initial=0)
        # accumulated_extinction = cumulative_trapezoid(alpha_part + alpha_mol, z, initial=0) # TODO: separate part and mol
        T_raman = np.exp(-part_accum_ext_raman - mol_accum_ext_raman)  # type: ignore

        P_raman = k_lidar * (overlap / z**2) * (beta_mol_raman) * T_elastic * T_raman

        params["particle_beta_raman"] = beta_part_raman
        params["particle_alpha_raman"] = alpha_part_raman
        params["molecular_alpha_raman"] = alpha_mol_raman.values
        params["molecular_beta_raman"] = beta_mol_raman.values
        params["particle_accum_ext_raman"] = part_accum_ext_raman
        params["molecular_accum_ext_raman"] = mol_accum_ext_raman
    else:
        P_raman = None

    if force_zero_aer_after_bin is not None:
        alpha_part[force_zero_aer_after_bin:] = 0
        beta_part[force_zero_aer_after_bin:] = 0

    return P_elastic, P_raman, params
