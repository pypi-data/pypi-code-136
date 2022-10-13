from pathlib import Path

import numpy as np
import xarray as xr
from datetime import datetime

from gfatpy.config import get_system_and_data_dn
from gfatpy.lidar import file_manager
from gfatpy.lidar.utils import LIDAR_INFO

from gfatpy.lidar.depolarization.calibration import calibration_factor_files

SYSTEM_DN, DATA_DN = get_system_and_data_dn()


def search_nereast_calib(
    depoCalib: dict, channel: str, current_date: np.datetime64
) -> dict:

    wavelength_, telescope_, *_ = file_manager.channel2info(channel)

    # Search the last calibration performed the current measurement
    idx = depoCalib[telescope_]["%0d" % wavelength_].index.get_indexer(
        [current_date], method="pad"
    )  # 'pad': search the nearest lower; 'nearest': search the absolute nearest.

    calib = depoCalib[telescope_]["%0d" % wavelength_].iloc[idx].to_dict("records")[0]

    return calib


def search_nereast_eta_star_from_file(
    lidar_name: str, channel: str, target_date: datetime, calib_dir=Path | None
) -> tuple[float, float]:

    if calib_dir is None:
        if DATA_DN is not None:
            calib_dir = DATA_DN / lidar_name / "QA" / "depolarization"
        else:
            raise NotADirectoryError("DATA_DN is None.")

    candidates, dates = file_manager.extract_filenames_dates_from_wildcard(calib_dir, "*eta-star*")  # type: ignore

    idx = np.abs(
        dates.astype("M8[ns]").astype(float)
        - np.array(target_date).astype("M8[ns]").astype(float).mean()
    ).argmin()

    calib_path = candidates[idx]

    calib = xr.open_dataset(calib_path)

    et_star = calib[f"eta_star_mean_{channel}"].values.item()
    std_et_star = calib[f"eta_star_mean_{channel}"].values.item()
    return et_star, std_et_star

    
    
    # TODO : Y:\datos\MULHACEN\QA\depolarization_calibration\2021\05\18\depolcal_20210518_2135_rot
    # TODO: GHK: dict = GHK_from_file(fn: Path)


def ghk_from_file(filepath: Path) -> dict:
    ...
