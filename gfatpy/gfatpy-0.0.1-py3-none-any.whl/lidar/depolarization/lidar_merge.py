#!/usr/bin/env python
import warnings
import numpy as np

import xarray as xr
from loguru import logger

from gfatpy.lidar.utils import LIDAR_INFO
from gfatpy.lidar import file_manager
from .utils import search_nereast_calib
from .depolarization_calibration_mhc import (
    create_calibration_dataframe_mhc,
)
from .depolarization_calibration_alh import (
    create_calibration_dataframe_alh,
)
from .depolarization_calibration_vlt import (
    create_calibration_dataframe_vlt,
)

warnings.filterwarnings("ignore")

__author__ = "Bravo-Aranda, Juan Antonio"
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Bravo-Aranda, Juan Antonio"
__email__ = "jabravo@ugr.es"
__status__ = "Production"


def parallel_perpendicular_merge(
    signal_R: np.ndarray,
    signal_T: np.ndarray,
    wavelength: int,
    detection_mode_code: str,
    range: np.ndarray,
    time: np.ndarray,
    eta: float = 1,
    HT: float = -1,
    HR: float = 1,
) -> xr.DataArray:

    merge_signal_ = np.abs(eta * HR * signal_T - HT * signal_R).astype(float)
    # Create DataArray
    merge_signal = xr.DataArray(
        merge_signal_,
        coords={"time": time, "range": range},
        dims=["time", "range"],
        attrs={
            "long_name": "Total (parallel+cross polarization components) signal",
            "detection_mode": LIDAR_INFO["metadata"]["code_mode_str2number"][
                detection_mode_code
            ],
            "wavelength": wavelength,
            "units": "$\\#$",
        },
    )

    return merge_signal


def apply_polarization_merge(dataset, depoCalib=None):
    """
    It merges the polarized channels and retrieve the Linear Volume Depolarization Ratio

    Parameters
    ----------
    dataset: xarray.Dataset from lidar.preprocessing() (xarray.Dataset)
    channels: str, list(str)
        list of channels (e.g., ['532xpa', '1064xta']) or [] to load all of them

    Returns
    -------
    dataset: xarray.Dataset with new varaibles ('signal%d_total' % wavelength_ ; 'LVDR%d' % wavelength_)
    """

    lidar_name = dataset.attrs["system"].upper()

    if depoCalib is None:
        if lidar_name == "MULHACEN":
            depoCalib = create_calibration_dataframe_mhc()
        elif lidar_name == "ALHAMBRA":
            depoCalib = create_calibration_dataframe_alh()
        elif lidar_name == "VELETA":
            depoCalib = create_calibration_dataframe_vlt()
        else:
            raise RuntimeError("`lidar_name` not recognized.")
    else:
        logger.info("Depolarization calibration provided by the user.")
        # TODO: check that the depoCalib dict has the correct format.

    # TODO: leer netcdf de /mnt/NASGFAT/datos/MULHACEN/QA/depolarization_calibration/YYYY/MM/DD/rotator_YYYYMMDD_HHMM/*rot*.nc
    # de momento, solo calibracion del rotador

    # TODO: INCLUIR LA INFO DE G, H, K EN dataset

    # Date of the current measurement
    current_date = dataset.time[0].min().values
    channels2add = []

    # Channels available to merge
    polarized_channels = list(filter(lambda c: c[-2] != "t", dataset.channel.values))

    _, telescope_, _, mode_ = file_manager.channel2info(
        dataset.channel[0].values.item()
    )

    # Possible products:
    product_channels = LIDAR_INFO["lidars"][lidar_name]["product_channels"].keys()

    for pchannel_ in product_channels:
        required_channels = LIDAR_INFO["lidars"][lidar_name]["product_channels"][
            pchannel_
        ]

        if not set(required_channels.keys()).issubset(polarized_channels):
            continue

        # Search nearest depolarization calibration
        calib = search_nereast_calib(depoCalib, pchannel_, current_date)

        # Special case gluing: #TODO: include a new calibration value 'eta_g'
        if mode_ == "g":
            calib[f"eta_{mode_}"] = calib[f"eta_p"]

        wavelength_, telescope_, _, mode_ = file_manager.channel2info(pchannel_)

        if None in [wavelength_, telescope_, mode_]:
            raise ValueError("Required information missing in product_channel.")

        channel_T = LIDAR_INFO["lidars"][f"{lidar_name}"]["polarized_channels"][
            telescope_
        ][wavelength_][mode_]["T"]

        channel_R = LIDAR_INFO["lidars"][f"{lidar_name}"]["polarized_channels"][
            telescope_
        ][wavelength_][mode_]["R"]

        signal_T = dataset["signal_%s" % channel_T]
        signal_R = dataset["signal_%s" % channel_R]

        if "lvd" not in pchannel_:
            # Calculate Total signal
            total_signal = parallel_perpendicular_merge(
                signal_R,
                signal_T,
                wavelength_,
                mode_,
                dataset.range.values,
                dataset.time.values,
                calib[f"eta_{mode_}"],
                calib["HT"],
                calib["HR"],
            )

            dataset[f"signal_{pchannel_}"] = total_signal

        else:
            # LVD
            lvdr_xr = lvdr(
                signal_R,
                signal_T,
                channel_R,
                channel_T,
                dataset.range.values,
                dataset.time.values,
                calib[f"eta_{mode_}"],
                calib["K"],
                calib["HT"],
                calib["HT"],
                calib["GR"],
                calib["HR"],
            )

            dataset[pchannel_] = lvdr_xr

        channels2add.append(pchannel_)

    # Add new products to coords of the xarray
    dataset = dataset.assign_coords(product_channel=channels2add)
    return dataset
