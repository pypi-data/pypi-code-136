#!/usr/bin/env python
import os
import glob
import pathlib
import warnings

import datetime as dt
import numpy as np
import xarray as xr
from loguru import logger

from gfatpy import utils
from gfatpy.lidar.utils import LIDAR_INFO, get_lidar_name_from_filename

warnings.filterwarnings("ignore")


__author__ = "Bravo-Aranda, Juan Antonio"
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Bravo-Aranda, Juan Antonio"
__email__ = "jabravo@ugr.es"
__status__ = "Production"

""" DEFAULT AUXILIAR INFO
"""
# Root Directory (in NASGFAT)  according to operative system


def reader_xarray(
    filelist: list[str] | str,
    date_ini: str | None = None,
    date_end: str | None = None,
    ini_range: float | None = None,
    end_range: float | None = None,
    percentage_required: int = 80,
    channels: list[str] = [],
) -> xr.Dataset:
    """
    Lidar data reader using xarray module.
    Inputs:
    - filelist: String with pattern for create a List of lidar files (i.e, '/drives/c/*.nc') (str)
                List of lidar files (list)
    - date_ini: 'yyyymmddThhmmss'
    - date_end: 'yyyymmddThhmmss'
    - ini_range: int/float (m)
    - end_range: int/float (m)
    - percentage_required= percentage of the time period required to continue the process. Default 80%  (int)
    - channels: list of channel number (e.g., [0, 1, 5]) or [] to load all of them
    Output:
    - lidar: dictionary or 'None' in case of error.
    """

    """ Aux Functions
    """

    def add_required_channels(
        lidar_name: str,
        channels: list | np.ndarray,
    ) -> list:

        if isinstance(channels, np.ndarray):
            channels = channels.tolist()

        required_channels = channels.copy()
        for channel_ in channels:
            if channel_ in LIDAR_INFO["lidars"][lidar_name]["product_channels"].keys():
                required_channels = required_channels + [
                    *LIDAR_INFO["lidars"][lidar_name]["product_channels"][channel_]
                ]
        unique_channels = np.unique(np.array(required_channels)).tolist()
        return unique_channels

    def select_channels(dataset: xr.Dataset, channels: list | str) -> xr.Dataset:
        """select_channels function creates a new dataset with 'signal_CHANNEL' defined in 'channels' (list).

        Args:
            dataset (xr.Dataset): lidar dataset
            channels (list | str): list of lidar channel names

        Returns:
            xr.Dataset: lidar dataset
        """

        if len(channels) > 0:
            if isinstance(channels, str):
                channels = [channels]
            if isinstance(channels, np.ndarray):
                channels = channels.tolist()

            # find variables: signal related to channel
            _vars = ["signal"]
            real_channels = []
            for _channel in dataset["channel"].values.tolist():
                if _channel not in channels:
                    for _var in _vars:
                        varname = "%s_%s" % (_var, _channel)
                        dataset = dataset.drop_vars(varname)
                else:
                    real_channels.append(_channel)
            dataset = dataset.sel(channel=real_channels)
            dataset = dataset.assign_coords(channel=real_channels)
        return dataset

    def check_minimum_profiles(
        times: np.ndarray,
        date_ini: dt.datetime,
        date_end: dt.datetime,
        percentage_required: float,
    ) -> bool:
        """Check Lidar Data has enough profiles

        Args:
            times ([type]): [description]
            date_ini ([type]): [description]
            date_end ([type]): [description]
            percentage_required ([type]): [description]
        """

        check = True
        time_resolution = float(
            np.median(np.diff(times)) / np.timedelta64(1, "s")
        )  # FIXME: typing error
        interval_duration = (date_end - date_ini).total_seconds()
        Nt = np.round(
            interval_duration / time_resolution
        )  # Theoretical Number of profiles
        Nm = (percentage_required / 100) * Nt  # Minimum number of profiles
        Np = len(times)  # Number of actual profiles
        if Np > Nm:
            logger.info(
                f"Data loaded from {date_ini.isoformat()} to {date_end.isoformat()}"
            )
        else:
            logger.warning(
                f"Not enough data found ({Np}<{Nm}) in the user-required period ({interval_duration} s.)"
            )
            check = False

        return check

    """ The Reader
        The Reader does:
        1. concatenate along time dimension
        2. merge channels comming from different telescopes (ALHAMBRA), assuming same range coordinate
    """
    logger.info("Start Reader ...")

    # Find Files to Read
    try:
        if isinstance(filelist, str):
            filelist = [filelist]
        elif isinstance(filelist, pathlib.Path):
            filelist = [str(filelist.absolute())]
        files2load = []
        for i_file in filelist:
            files2load.extend(glob.glob(i_file))
    except Exception as e:
        files2load = []
        logger.warning(str(e))
        logger.warning(f"Files in {filelist} not found.")
    if len(files2load) > 0:
        logger.info(files2load)
        lidartemp = None

        lidar_nick = get_lidar_name_from_filename(files2load[0])
        if lidar_nick is None:
            logger.critical("Lidar nick not in lidar systems availables.")

        try:
            # Get lidar name
            lidar_name = LIDAR_INFO["metadata"]["nick2name"][lidar_nick]

            # Add required channels to the channel list to obtain product channel:
            channels = add_required_channels(lidar_name, channels)
            # Loop over modules: 1) concat time; 2) merge module
            for module in LIDAR_INFO["lidars"][lidar_name]["modules"]:
                module_fns = [x for x in files2load if module in x]
                lidarmod = None
                if len(module_fns) > 0:
                    for fn in module_fns:
                        with xr.open_dataset(
                            fn, chunks={}
                        ) as _dx:  # chunks={"time": 600, "range": 1000})
                            _dx = select_channels(_dx, channels)
                        if not lidarmod:
                            lidarmod = _dx
                        else:
                            # concat only variables that have "time" dimension.
                            # rest of variables keep values from first dataset
                            try:
                                lidarmod = xr.concat(
                                    [lidarmod, _dx],
                                    dim="time",
                                    data_vars="minimal",
                                    coords="minimal",
                                    compat="override",
                                )
                            except Exception as e:
                                logger.critical("Dataset in {fn} not concatenated")
                                raise e
                    # Sort Dataset by Time
                    if lidarmod is not None:
                        lidarmod = lidarmod.sortby(lidarmod["time"])
                    else:
                        raise ValueError("lidarmod is None.")
                    # Merge Module
                    if not lidartemp:
                        lidartemp = lidarmod
                    else:
                        try:
                            lidartemp = xr.merge([lidartemp, lidarmod])
                        except Exception as e:
                            logger.critical(f"{e}")
                            logger.critical(f"Dataset from module {module} not merged")
                            raise e
                del lidarmod
        except Exception as e:
            logger.critical(f"{e}")
            logger.critical("Files not concatenated")
            raise e

        if lidartemp:
            # Selection time window and Check Enough Profiles
            if np.logical_and(date_ini is not None, date_end is not None):
                if np.logical_and(isinstance(date_ini, str), isinstance(date_end, str)):
                    # Times Formatting

                    date_ini_dt = utils.utils.str_to_datetime(date_ini)  # type: ignore
                    date_end_dt = utils.utils.str_to_datetime(date_end)  # type: ignore

                    # Time Selection
                    min_time_resol = dt.timedelta(seconds=0.1)
                    lidar = lidartemp.sel(
                        time=slice(
                            date_ini_dt - min_time_resol, date_end_dt + min_time_resol
                        )
                    )

                    # Check selection
                    ok = check_minimum_profiles(
                        lidar["time"].values,
                        date_ini_dt,
                        date_end_dt,
                        percentage_required,
                    )
                    if not ok:
                        lidar = None
                else:
                    lidar = lidartemp
            else:
                lidar = lidartemp
            del lidartemp

            # Complete lidar dataset
            if lidar:
                # Range Clip
                if ini_range is not None and end_range is not None:
                    if end_range > ini_range:
                        lidar = lidar.sel(range=slice(ini_range, end_range))
                    else:
                        raise ValueError("ini_range is larger than end_range.")

                # add background ranges
                if "BCK_MIN_ALT" not in lidar.attrs.keys():
                    lidar.attrs["BCK_MIN_ALT"] = 75000
                if "BCK_MAX_ALT" not in lidar.attrs.keys():
                    lidar.attrs["BCK_MAX_ALT"] = 105000

                # Extract information from filename
                try:
                    lidar.attrs["lidarNick"] = os.path.basename(files2load[0]).split(
                        "_"
                    )[0]
                    lidar.attrs["dataversion"] = os.path.basename(files2load[0]).split(
                        "_"
                    )[1]
                except:
                    lidar.attrs["lidarNick"] = "Unknown"
                    lidar.attrs["dataversion"] = "Unknown"

            else:
                lidar = None
        else:
            logger.error("Impossible to load found files.")
            lidar = None
    else:
        logger.error("Files not found.")
        lidar = None

    if lidar is None:
        # set_trace()
        logger.error("No dataset created.")
        raise RuntimeError("No dataset created.")

    logger.info("End Reader")
    return lidar
