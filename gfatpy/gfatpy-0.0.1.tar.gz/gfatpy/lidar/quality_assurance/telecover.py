import os
import glob
import datetime as dt

import matplotlib
import numpy as np
import xarray as xr
from loguru import logger
import matplotlib.ticker as ticker
import matplotlib.pyplot as plt

from gfatpy import DATA_DN
from gfatpy.lidar.utils import LIDAR_INFO
from .common import select_dc
from gfatpy.utils import utils
from gfatpy.lidar.preprocessing import preprocess

pol_name = {0: "all", 1: "parallel", 2: "perpendicular"}
det_mod_name = {0: "analog", 1: "photoncounting", 2: "gluing"}


def telecover(lidar_name, date_str, **kwargs):
    """
    # TODO: Reformular como se ha hecho con rayleigh fit y depolarization calibration
    telecover
    Inputs:
    - lidar_name: mulhacen, veleta, alhambra
    - date_str: date ('yyyymmdd') (str)
    - zmin: minimum altitude we use as base for our rayleigh fit (float)
    - zmax: max altitude we use as base for our rayleigh fit (float)
    - savefig: it determines if we will save our plots (True) or not (False) (bool)
    - level_1a_dn: folder where telecover files are located.
    - rayleigh_fit_dn: folder where we want to save our figures.
    Outputs:
    - ascii files
    - figures
    """

    def plot_telecover_channel(tc_type, rf_ds, zmin, zmax, output_directory, savefig):
        logger.info(f"Creating figure: rf_ds.channel_code")
        """
        Inputs:
        - tc_type: Telecover for ultriviolet or visible/near-infrarred (uv or vnir) (str)
        - rf_dc: xarray dataset (xarray.Dataset)
        - savefig: it determines if we will save our plots (True) or not (False) (bool)
        - rayleigh_fit_dn: folder where we want to save our figures.
        Outputs:
        - figures
        """
        font = {"size": 12}
        matplotlib.rc("font", **font)
        # FIGURE
        # TODO: TO INFO YAML PLOT
        ydict_rcs = {
            "355xta": (0, 2e6),
            "355xtp": (0, 3e7),
            "532xpa": (0, 3e6),
            "532xpp": (0, 6e7),
            "532xcp": (0, 2e7),
            "532xca": (0, 1e6),
            "1064xta": (0, 7e6),
            "353xtp": (0, 3e6),
            "530xtp": (0, 5e7),
            "408xtp": (0, 2e8),
        }
        ydict_norm_rcs = {
            "355xta": (0, 10),
            "355xtp": (0, 10),
            "532xpa": (0, 8),
            "532xpp": (0, 5),
            "532xcp": (0, 4),
            "532xca": (0, 10),
            "1064xta": (0, 20),
            "353xtp": (0, 5),
            "530xtp": (0, 2),
            "408xtp": (0, 5),
        }
        lidar_system = LIDAR_INFO["metadata"]["nick2name"]
        x_lim = (0, 3000)
        colorbar = matplotlib.cm.get_cmap("jet", len(rf_ds.sectors))
        colors = colorbar(np.linspace(0, 1, len(rf_ds.sectors)))
        fig = plt.figure(figsize=(15, 10))
        fig_title = (
            "%s telecover - channel %s | %s | Reference height: %3.1f-%3.1f km"
            % (
                rf_ds.attrs["lidar_system"],
                rf_ds.channel_code,
                dt.datetime.strftime(rf_ds.datetime_ini, "%d.%m.%Y, %H:%MUTC"),
                zmin / 1000.0,
                zmax / 1000.0,
            )
        )
        # MEAN
        sectors = [sector_ for sector_ in rf_ds.sectors if sector_.find("2") == -1]
        sum_rcs = np.zeros(rf_ds.range.size)
        for sector_ in sectors:
            rcs = rf_ds[sector_]
            try:
                sum_rcs += rcs
            except:
                sum_rcs += rcs.compute()
        mean_rcs = sum_rcs / len(sectors)
        mean_rcs.name = "M"

        # Normalized
        for sector_ in rf_ds.sectors:
            rf_ds[f"n{sector_}"] = (
                rf_ds[sector_] / rf_ds[sector_].sel(range=slice(zmin, zmax)).mean()
            )
        norm_mean_rcs = mean_rcs / mean_rcs.sel(range=slice(zmin, zmax)).mean()
        norm_mean_rcs.name = "nM"

        # RAW RCS
        ax = fig.add_subplot(311)
        fig_y_label = "RCS, a.u."
        for iter_ in zip(rf_ds.sectors, colors):
            sector_ = iter_[0]
            color_ = iter_[1]
            rf_ds[sector_].plot(
                ax=ax, x="range", linewidth=2, label=sector_, color=color_
            )
        mean_rcs.plot(ax=ax, x="range", linewidth=2, label="M", color="k")
        ax.set_title(fig_title, fontsize="x-large", verticalalignment="baseline")
        ax.set_ylim(ydict_rcs[rf_ds.channel_code])
        plt.ticklabel_format(style="sci", axis="y", scilimits=(0, 1))
        ax.set_ylabel(fig_y_label, fontsize="large")
        plt.legend(loc=1, fontsize="large")

        # Normalized RCS
        ax = fig.add_subplot(312)
        fig_y_label = "Normalized RCS, a.u."
        for iter_ in zip(rf_ds.sectors, colors):
            sector_ = iter_[0]
            color_ = iter_[1]
            rf_ds[f"n{sector_}"].plot(
                ax=ax, x="range", linewidth=2, label=sector_, color=color_
            )
        norm_mean_rcs.plot(ax=ax, x="range", linewidth=2, label="nM", color="k")
        plt.ticklabel_format(style="sci", axis="y", scilimits=(0, 1))
        ax.set_ylim(ydict_norm_rcs[rf_ds.channel_code])
        ax.set_ylabel(fig_y_label, fontsize="large")
        plt.legend(loc=1, fontsize="large")

        # Diference
        ax = fig.add_subplot(313)
        fig_y_label = "normalized RCS\nrelative difference, %"

        for iter_ in zip(rf_ds.sectors, colors):
            sector_ = iter_[0]
            color_ = iter_[1]
            rf_ds["diff_%s" % sector_] = (
                100 * (rf_ds[f"n{sector_}"] - norm_mean_rcs) / norm_mean_rcs
            )
            rf_ds[f"diff_{sector_}"].plot(
                ax=ax, x="range", linewidth=2, label=sector_, color=color_
            )
        ax.xaxis.get_label().set_fontsize("large")
        ax.xaxis.set_minor_locator(ticker.MultipleLocator(125))
        ax.set_ylabel(fig_y_label, fontsize="large")
        ax.set_ylim(-100, 100)
        plt.legend(loc=1, fontsize="large")

        for ax in fig.get_axes():
            ax.tick_params(axis="both", labelsize=14)
            ax.set_xlim(x_lim)
            ax.grid()
            ax.label_outer()

        if save_fig:
            fig_fn = os.path.join(
                output_directory,
                "%s_TC%s_%s_%s.png"
                % (
                    lidar_system[rf_ds.lidar_system],
                    tc_type,
                    rf_ds.channel_code,
                    dt.datetime.strftime(rf_ds.datetime_ini, "%Y%m%d_%H%M"),
                ),
            )
            plt.savefig(fig_fn, dpi=200, bbox_inches="tight")
            if os.path.isfile(fig_fn):
                logger.info(
                    " %s telecover Figure succesfully saved!" % rf_ds.channel_code
                )

    logger.info("Start Telecover")

    """ Get Input Arguments """
    lidar_name = kwargs.get("lidar_name", "mulhacen")
    if lidar_name is None:
        lidar_name = "mulhacen"

    channels = kwargs.get("channels", "all")
    if channels is None:
        channels = "all"
    elif channels != "all":
        if not isinstance(channels, list):
            channels = [channels]

    z_min = kwargs.get("z_min", 2000)
    if z_min is None:
        z_min = 2000
    z_max = kwargs.get("z_max", 3000)
    if z_max is None:
        z_max = z_min + 1000
    smooth_range = kwargs.get("smooth_range", 250)
    if smooth_range is None:
        smooth_range = 250

    range_min = kwargs.get("range_min", 0)
    if range_min is None:
        range_min = 0
    range_max = kwargs.get("range_max", 30000)
    if range_max is None:
        range_max = 30000

    data_dn = kwargs.get("data_dn", None)
    if np.logical_or(data_dn is None, data_dn == "GFATserver"):
        data_dn = DATA_DN
    level_1a_dn = kwargs.get("level_1a_dn", None)
    if np.logical_or(level_1a_dn is None, level_1a_dn == "GFATserver"):
        level_1a_dn = os.path.join(data_dn, lidar_name.upper(), "1a")
    output_dn = kwargs.get("output_dn", None)

    darkcurrent_flag = kwargs.get("darkcurrent_flag", True)
    if darkcurrent_flag is None:
        darkcurrent_flag = True

    deadtime_flag = kwargs.get("deadtime_flag", True)
    if deadtime_flag is None:
        deadtime_flag = True

    zerobin_flag = kwargs.get("zerobin_flag", True)
    if zerobin_flag is None:
        zerobin_flag = True

    merge_flag = kwargs.get("merge_flag", True)
    if merge_flag is None:
        merge_flag = True

    save_fig = kwargs.get("save_fig", True)
    if save_fig is None:
        save_fig = True

    save_earlinet = kwargs.get("save_earlinet", True)
    if save_earlinet is None:
        save_earlinet = True

    """ Check Input Arguments """
    # TODO
    """
    assert isinstance(date_str, str), "date_str must be String Type"
    """

    """ Lidar Files, Date, Lidar Name, Measurement Type """
    if date_str is None:
        logger.error("%s not found. Exit" % rs_fl)
        return
    else:
        date_dt = utils.str_to_datetime(date_str)
        date_str = date_dt.strftime("%Y%m%d")  # just in case
    year_str, month_str, day_str = (
        "%04d" % date_dt.year,
        "%02d" % date_dt.month,
        "%02d" % date_dt.day,
    )

    """ Output Directory """
    if np.logical_or(output_dn is None, output_dn == "GFATserver"):
        output_dn = os.path.join(data_dn, lidar_name.upper(), "QA", "telecover")
    output_dn = os.path.join(output_dn, f"telecover_{date_str}")
    if not os.path.exists(output_dn):
        try:
            os.makedirs(output_dn, exist_ok=True)  # mkpath(output_dn)
        except Exception:
            logger.error(f"Output Directory Not Created. {output_dn}")
            output_dn = os.getcwd()

    # Dictionary telecover type
    tc_type = {"mulhacen": ("-uv", "-vnir"), "alhambra": (""), "alhambra": ("")}

    # Dictionary channels
    channels = {
        "mulhacen": {
            "-uv": ("355xta", "355xtp", "408xtp", "353xtp"),
            "-vnir": ("532xpa", "532xpp", "532xca", "532xcp", "530xtp", "1064xta"),
        },
        "alhambra": "all",
        "veleta": "all",
    }
    telecover = {}

    # Type of telecover: uv or vnir
    tc_dir = os.path.join(level_1a_dn, year_str, month_str, day_str)
    for tc_ in tc_type[lidar_name.lower()]:
        filelist = glob.glob(os.path.join(tc_dir, "*Ptc%s*.nc" % tc_))
        hours = list()  # to list different telecovers in the same day
        for file_ in filelist:
            hour_ = file_.split("_")[-1].split(".")[0]
            hours.append(hour_)
        hours = np.unique(hours)  # Number of telecovers of the same type
        for hour_ in hours:
            try:
                datetime_ini = dt.datetime.strptime(f"{date_str}{hour_}", "%Y%m%d%H%M")
            except:
                logger.error("Datetime conversion error.")
                return

            # Create output folder
            output_directory = os.path.join(
                output_dn, f"telecover{tc_}_{date_str}_{hour_}"
            )
            if not os.path.isdir(output_directory):
                os.makedirs(output_directory, exist_ok=True)

            # Search files of a given telecover tests, i.e., same tc_ and same hour_
            filepathformat = os.path.join(tc_dir, f"*Ptc{tc_}*{hour_}*.nc")  # TC files
            filelist = glob.glob(filepathformat)
            telecover[
                tc_
            ] = {}  # dictionary to save Datasets with all channels separated by sectors
            for file_ in filelist:
                sector_ = file_.split("_")[2].split("-")[-1]
                logger.info(f"Loading sector {sector_}")
                rs_fl = os.path.join(
                    tc_dir, f"*Ptc{tc_}-{sector_}_*{hour_}.nc"
                )  # TC files
                dc_fl = os.path.join(tc_dir, "*Pdc*.nc")  # TC files

                """ LIDAR preprocessing """
                telecover[tc_][sector_] = preprocess(rs_fl, dc_fl=dc_fl, save_dc=True)

            # Creating a Dataset [rf_ds] for each channel with all the sectors
            for channel_ in telecover[tc_][sector_].channel.values:
                # Wavelength, Detection Mode, Polarization
                wavelength = np.floor(
                    telecover[tc_][sector_].wavelength.sel(channel=channel_).values
                ).astype("int")
                detection_mode = int(
                    telecover[tc_][sector_].detection_mode.sel(channel=channel_).values
                )
                polarization = int(
                    telecover[tc_][sector_].polarization.sel(channel=channel_).values
                )
                # try:
                #    bool(telecover[tc_][sector_].sel(channel=channel_).active_channel.values.all())
                # except:
                #     pdb.set_trace()
                if bool(
                    telecover[tc_][sector_]
                    .sel(channel=channel_)
                    .active_channel.values.all()
                ):
                    if channel_ in channels[lidar_name][tc_]:
                        rf_ds = []
                        for idx, sector_ in enumerate(telecover[tc_].keys()):
                            # TELECOVER EARLINET DATA FORMAT
                            # TODO: sacar a una funcion
                            rcs = (
                                telecover[tc_][sector_][f"signal_{channel_}"].mean(
                                    dim="time", keep_attrs=True
                                )
                                * telecover[tc_][sector_]["range"] ** 2
                            )
                            rcs.name = sector_
                            if idx == 0:
                                rf_ds = []
                                rf_ds = rcs.copy()
                            else:
                                rf_ds = xr.merge(
                                    [rf_ds, rcs], combine_attrs="no_conflicts"
                                )
                            # TODO rf_ds = rf_ds.assign_coords({"range": rf_ds.range/1e3})

                            try:
                                dc, dark_subtracted_str = select_dc(
                                    telecover[tc_][sector_], channel_
                                )
                                if np.logical_and(
                                    dark_subtracted_str != None,
                                    len(dark_subtracted_str) > 0,
                                ):
                                    dc.name = "D"
                                    rf_ds = xr.merge([rf_ds, dc])
                            except:
                                dc = None
                                dark_subtracted_str = ""
                                logger.warning("dark measurement not found.")

                        # Attributes
                        rf_ds["range"].attrs["units"] = "m"
                        rf_ds["range"].attrs["long_name"] = "Height"
                        rf_ds = rf_ds.sel(range=slice(0, 30000))
                        # rf_ds = xr.merge([rf_ds, telecover[tc_][sector_].detection_mode.sel(channel=channel_),
                        #                         telecover[tc_][sector_].polarization.sel(channel=channel_),
                        #                         telecover[tc_][sector_].wavelength.sel(channel=channel_)])
                        rf_ds["wavelength"] = wavelength
                        rf_ds["wavelength"].attrs["value_str"] = str(wavelength)

                        # TODO: sacar la creacion de un dataset especifico para RF a una funcion
                        # Polarization
                        rf_ds["polarization"] = polarization
                        rf_ds["polarization"].attrs["meaning"] = pol_name[polarization]
                        rf_ds["polarization"].attrs["id"] = LIDAR_INFO["metadata"][
                            "code_polarization_number2str"
                        ][polarization]

                        # TODO: sacar esto a una funcion
                        # Detection mode
                        rf_ds["detection_mode"] = detection_mode
                        rf_ds["detection_mode"].attrs["meaning"] = det_mod_name[
                            detection_mode
                        ]
                        rf_ds["detection_mode"].attrs["id"] = LIDAR_INFO["metadata"][
                            "code_mode_number2str"
                        ][detection_mode]

                        rf_ds.attrs["sectors"] = list(telecover[tc_].keys())
                        rf_ds.attrs["lidar_location"] = "Granada"
                        rf_ds.attrs["lidar_id"] = "gr"
                        rf_ds.attrs["lidar_system"] = lidar_name.upper()
                        rf_ds.attrs["datetime_ini"] = datetime_ini
                        rf_ds.attrs["date_format"] = "%Y%m%dT%H:%M:%S.%f"
                        rf_ds.attrs["timestamp"] = date_str[0:8]
                        rf_ds.attrs["dark_subtracted"] = dark_subtracted_str
                        rf_ds.attrs["channel_code"] = channel_

                        # SAVE RF FILE
                        # TODO: sacar a una funcion el escribir este archivo con formato
                        cols = list(telecover[tc_].keys())
                        if detection_mode == 0:  # (if analog)
                            cols.append("D")
                            rf_ds = rf_ds.drop("ilu")

                        # Convert to pandas
                        rf_df = []
                        rf_df = rf_ds[cols].to_dataframe()

                        # Create file
                        rf_fn = os.path.join(
                            output_directory,
                            "%sTelecover%s.csv" % (rf_ds.attrs["lidar_id"], channel_),
                        )
                        with open(rf_fn, "w") as f:
                            f.write(
                                "station ID = %s (%s)\n"
                                % (
                                    rf_ds.attrs["lidar_id"],
                                    rf_ds.attrs["lidar_location"],
                                )
                            )
                            f.write("system = %s\n" % rf_ds.attrs["lidar_system"])
                            f.write(
                                "signal = %s, %s, %s, %s\n"
                                % (
                                    rf_ds["wavelength"].attrs["value_str"],
                                    rf_ds["polarization"].attrs["meaning"],
                                    rf_ds["detection_mode"].attrs["meaning"],
                                    rf_ds.attrs["dark_subtracted"],
                                )
                            )
                            f.write(
                                "date, time= %s\n"
                                % dt.datetime.strftime(
                                    rf_ds.attrs["datetime_ini"], "%d.%m.%Y, %HUTC"
                                )
                            )
                        f.close()
                        rf_df.index = rf_df.index.map(lambda x: "%.4f" % x)
                        rf_df.to_csv(
                            rf_fn,
                            mode="a",
                            header=True,
                            na_rep="NaN",
                            float_format="%.4e",
                        )
                        if os.path.isfile(rf_fn):
                            logger.info(
                                f"{tc_}-telecover {channel_} at {hour_} file done!"
                            )
                            # Plot Telecover for current channel
                            plot_telecover_channel(
                                tc_, rf_ds, z_min, z_max, output_directory, save_fig
                            )
                else:
                    logger.warning(
                        f"Telecover-{tc_}: channel {channel_} not found in measurements."
                    )
