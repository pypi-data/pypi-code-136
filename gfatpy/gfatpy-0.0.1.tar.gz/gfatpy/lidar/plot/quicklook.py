import pathlib

import matplotlib
import numpy as np
import xarray as xr
import pandas as pd
import datetime as dt
from loguru import logger
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

from gfatpy import DATA_DN
from gfatpy.lidar.utils import LIDAR_INFO, LIDAR_PLOT_INFO
from gfatpy.lidar.utils import signal_to_rcs
from gfatpy.lidar.preprocessing import preprocess
from gfatpy.utils import plot


""" PLOT LIDAR
"""


def plot_lidar_channels(
    filelist,
    channels2plot,
    dc_fl=None,
    plt_conf=None,
    figdirectory=None,
    data_dn=None,
    debugging: bool = False,
    colorbar_range: tuple[int, int] | None = None,
):
    """
    Quicklook maker of lidar measurements.
    Inputs:
    - filelist: regular expression of lidar files (str).
    - channels2plot: Array of string codes corresponding to the lidar channels (str).
    - dc_fl:  regular expression of DC lidar files (str).
    - plt_conf: dictionary with plot configuration (dict).
    - figdirectory: directory to save the figure. Date tree will be created (str).
    Outputs:
    - None

    # TODO: Implement PLOT_DEPO
    """

    # Font size of the letters in the figure
    matplotlib.rcParams.update({"font.size": 16})

    # Read the list of files to plot
    # --------------------------------------------------------------------
    if isinstance(filelist, str):
        filelist = [filelist]

    # Read and Preprocess Lidar Dataset
    lxarray = preprocess(
        filelist,
        dc_fl=dc_fl,
        deadtime_flag=False,
        channels=channels2plot,
        data_dn=data_dn,
    )

    if lxarray != None:

        # Lidar name
        lidar_name = lxarray.attrs["system"]

        # TODO: si el usuario facilita otros valores de Vmax para canales concretos, actualizar el diccionario Vmax

        # One figure per variable
        # --------------------------------------------------------------------
        if isinstance(channels2plot, str):
            channels2plot = [channels2plot]

        # time, altitude variables
        times = lxarray.time.values
        range_m = lxarray.range.values
        range_km = range_m / 1000.0

        for channel_ in channels2plot:
            if colorbar_range is None:
                Vmin = LIDAR_PLOT_INFO["limits"]["Vmin"][lidar_name]
                Vmax = LIDAR_PLOT_INFO["limits"]["Vmax"][lidar_name]
            else:
                Vmin = {channel_: colorbar_range[0]}
                Vmax = {channel_: colorbar_range[1]}
            print("Current plot %s" % channel_)
            try:
                print("Colorbar range: %f - %f" % (Vmin[channel_], Vmax[channel_]))
                # Create channel string
                channelstr = channel_

                # Lidar Signal (RCS) or LVD
                if "lvd" in channel_:
                    var_name = channel_
                    da_var = lxarray[var_name]
                    data2plot = da_var.values.T
                    var_label = r"Linear volume depolarization ratio"
                    v_label_format = "%.1f"
                    v_ticks = np.arange(2, 10, 2) * 0.1
                    v_ticks = np.insert(v_ticks, 0, 0)
                else:
                    var_name = "signal_%s" % channel_
                    da_var = lxarray[var_name]
                    data2plot = signal_to_rcs(da_var, range_m).values.T
                    var_label = r"Range corrected signal, $[a.u.]$"
                    v_label_format = "%.1e"
                    v_ticks = np.arange(2, 11, 2) * 1e6
                    v_ticks = np.insert(v_ticks, 0, 1e6)
                # Create Figure
                fig, axes = plt.subplots(figsize=(15, 5))

                # Color Map
                cmap = matplotlib.colormaps["jet"]
                bounds = np.linspace(Vmin[channel_], Vmax[channel_], 128)
                norm = matplotlib.colors.BoundaryNorm(boundaries=bounds, ncolors=cmap.N)

                # Plot
                q = axes.pcolormesh(times, range_km, data2plot, cmap=cmap, norm=norm)
                q.cmap.set_over("white")
                cb = plt.colorbar(
                    q, ax=axes, extend="max", format=v_label_format, ticks=v_ticks
                )

                # search for gaps in data
                # --------------------------------------------------------------------
                if plt_conf["gapsize"] == "default":
                    dif_time = times[1:] - times[0:-1]
                    GAP_SIZE = 2 * int(
                        np.ceil(
                            (
                                np.median(dif_time)
                                .astype("timedelta64[s]")
                                .astype("float")
                                / 60
                            )
                        )
                    )  # GAP_SIZE is defined as the median of the resolution fo the time array (in minutes)
                    logger.debug(
                        f"GAP_SIZE parameter automatically retrieved to be {GAP_SIZE}"
                    )
                else:
                    GAP_SIZE = int(plt_conf["gapsize"])
                    logger.debug("GAP_SIZE set by the user: {GAP_SIZE} (in minutes)")
                dttime = times.astype("M8[ms]").astype("O")
                plot.gapsizer(plt.gca(), dttime, range_m, GAP_SIZE, "#c7c7c7")

                # Setting axes
                # --------------------------------------------------------------------
                mf = matplotlib.ticker.FuncFormatter(plot.tmp_f)
                axes.xaxis.set_major_formatter(mf)
                hours = mdates.HourLocator(range(0, 25, 3))
                date_fmt = mdates.DateFormatter("%H")
                axes.xaxis.set_major_locator(hours)
                axes.xaxis.set_major_formatter(date_fmt)
                min_date = times.min()
                max_date = times.max()
                axes.set_xlim(
                    min_date.astype("datetime64[D]"),
                    max_date.astype("datetime64[D]") + np.timedelta64(1, "D"),
                )
                axes.set_ylim(
                    plt_conf["min_range"] / 1000, plt_conf["max_range"] / 1000
                )
                plt.grid(True)

                # Axes Labels
                # -----------------------------------------
                axes.set_xlabel(r"Time, $[UTC]$")
                axes.set_ylabel(r"Height, $[km, \, agl]$")
                cb.ax.set_ylabel(var_label)

                # title
                # ----------------------------------------------------------------------------
                datestr1 = times[1].astype("str").split("T")[0]
                datestr2 = times[-2].astype("str").split("T")[0]
                if datestr1 == datestr2:
                    datestr = datestr1
                else:
                    datestr = "%s -- %s" % (datestr1, datestr2)
                plt_conf["title1"] = "%s %s" % (
                    lxarray.attrs["instrument_id"],
                    channelstr,
                )
                plot.title1(plt_conf["title1"], plt_conf["title_size_coef"])
                plot.title2(datestr, plt_conf["title_size_coef"])
                plot.title3(
                    "{} ({:.1f}N, {:.1f}E)".format(
                        lxarray.attrs["site_location"],
                        float(lxarray.attrs["geospatial_lat_min"]),
                        float(lxarray.attrs["geospatial_lon_min"]),
                    ),
                    plt_conf["title_size_coef"],
                )

                # logo
                # ----------------------------------------------------------------------------
                plot.watermark(axes, zoom=0.3, alpha=0.6)

                # create output folder
                # --------------------------------------------------------------------
                year = datestr[0:4]
                fulldirpath = pathlib.Path(figdirectory) / channelstr / year
                fulldirpath.mkdir(parents=True, exist_ok=True)
                print("fulldirpath created: %s" % fulldirpath)
                figstr = "%s_%s_%s_%s.png" % (
                    lxarray.attrs["lidarNick"],
                    lxarray.attrs["dataversion"],
                    channelstr,
                    datestr.replace(" -- ", "_").replace("-", ""),
                )
                finalpath = fulldirpath / figstr

                try:
                    print("Saving %s" % finalpath)
                    plt.savefig(finalpath, dpi=400, bbox_inches="tight")
                except Exception as e:
                    print(str(e))
                if finalpath.is_file():
                    print("Saving %s...DONE!" % finalpath)
                else:
                    print("Saving %s... error!" % finalpath)

                if debugging:
                    plt.show()

                plt.close()

            except Exception as e:
                print(str(e))
                print("Quicklook for channel %s not plotted" % channel_)


def daily_quicklook(
    filelist,
    dcfilelist,
    figdirectory,
    channels2plot="default",
    gapsize="default",
    min_range=100,
    max_range=14000,
    plot_depo=True,
    title_size_coef=2,
    data_dn=None,
    debugging=False,
    colorbar_range: tuple[int, int] | None = None,
):
    """
    Formatted daily quicklook of RPG Cloud Radar measurements.
    Inputs:
    - filelist: List of radar files (i.e, '/drives/c/*ZEN*.LC?') (str)
    - figdirectory: Array of numbers corresponding to the moment of the Doppler spectra. (integer)
    - gapsize
    - min_range
    - y_max
    - title_size_coef
    - kwargs:
      -key: dddsss value: maximum colorbar value (e.g., '532xta': 1e7)
    Outputs:
    - None
    """

    """ Get Input Arguments """
    if data_dn is None:
        data_dn = DATA_DN

    if isinstance(filelist, str):
        filelist = [filelist]

    plt_conf = {
        "gapsize": gapsize,
        "min_range": min_range,
        "max_range": max_range,
        "title_size_coef": title_size_coef,
        "Vmax": {},
    }

    plot_lidar_channels(
        filelist,
        channels2plot,
        dc_fl=dcfilelist,
        plt_conf=plt_conf,
        figdirectory=figdirectory,
        data_dn=data_dn,
        debugging=debugging,
        colorbar_range=colorbar_range,
    )


def date_quicklook(
    dateini,
    dateend=None,
    daily=True,
    dc_correction=False,
    lidar_name="MULHACEN",
    channels2plot: list[str] | str = "default",
    path1a: pathlib.Path | str = "GFATserver",
    figpath: pathlib.Path | str = "GFATserver",
    debugging: bool = False,
    colorbar_range: tuple[float, float] | None = None,
):
    """
    Formatted daily quicklook of lidar measurements for hierarchy GFAT data.
    Inputs:
    - daily: daily quicklook (1 quicklook per day). If False, quicklook of the period
    - path1a: path where 1a-level data are located.
    - figpath: path where figures are saved.
    - Initial date [yyyy-mm-dd] (str).
    - Final date [yyyy-mm-dd] (str).

    Outputs:
    - None
    """
    # Function for building pattern file
    def filepattern(lidar_name, ftype, current_date):  # TODO: To lidar utils
        """
        lidar_name: lidar name
        ftype: rs, dc
        """
        filename = "%s_1a_P%s_rs*%s*.nc" % (
            LIDAR_INFO["metadata"]["name2nick"][lidar_name.upper()],
            ftype,
            dt.datetime.strftime(current_date, "%y%m%d"),
        )
        return filename

    # Inputs
    if dateend is None:
        dateend = dateini

    if channels2plot == "default":
        channels2plot = LIDAR_PLOT_INFO["plot_default"][lidar_name]
    else:
        if isinstance(channels2plot, list):
            channels2plot = np.asarray(channels2plot)
    if path1a == "GFATserver":
        path1a = pathlib.Path(DATA_DN) / f"{lidar_name.upper()}" / "1a"
    else:
        path1a = pathlib.Path(path1a)

    if figpath == "GFATserver":
        figpath = pathlib.Path(DATA_DN) / f"{lidar_name.upper()}" / "quicklooks"
    else:
        figpath = pathlib.Path(figpath)

    # Loop over days
    inidate = dt.datetime.strptime(dateini, "%Y%m%d")
    enddate = dt.datetime.strptime(dateend, "%Y%m%d")
    if daily:
        for _day in pd.date_range(inidate, enddate):
            print(_day)
            current_date = _day
            filename = filepattern(lidar_name, "rs", current_date)
            filelist = (
                path1a
                / f"{current_date.year:d}"
                / f"{current_date.month:02d}"
                / f"{current_date.day:02d}"
                / filename
            )
            if dc_correction:
                dcfilename = filepattern(lidar_name, "dc", current_date)
                dcfilelist = (
                    path1a
                    / f"{current_date.year:d}"
                    / f"{current_date.month:02d}"
                    / f"{current_date.day:02d}"
                    / dcfilename
                )
            else:
                dcfilelist = None
            daily_quicklook(
                filelist,
                dcfilelist,
                figpath,
                channels2plot=channels2plot,
                data_dn=path1a,
                debugging=debugging,
                colorbar_range=colorbar_range,
            )
    else:
        filelist = []
        dcfilelist = []
        for _day in pd.date_range(inidate, enddate):
            print(_day)
            current_date = _day
            filename = filepattern(lidar_name, "rs", current_date)
            dcfilename = filepattern(lidar_name, "dc", current_date)
            filelist.append(
                path1a
                / "%d"
                % current_date.year
                / "%02d"
                % current_date.month
                / "02d"
                % current_date.day
                / filename
            )
            dcfilelist.append(
                path1a
                / "%d"
                % current_date.year
                / "%02d"
                % current_date.month
                / "02d"
                % current_date.day
                / dcfilename
            )
        daily_quicklook(
            filelist,
            dcfilelist,
            figpath,
            channels2plot=channels2plot,
            lidar=lidar_name,
            data_dn=path1a,
            debugging=debugging,
            colorbar_range=colorbar_range,
        )


# TODO esto es lo que dijo Juan Diego. Quicklook compatible con Jupyter
# def plot_RCS_quicklook(files_list, y_min = 0, y_max = 10000, ini_time = None, end_time = None, c_min = 0, c_max = 2e6):
#     altitude, time, beta_mol, delta_vol, RCS, z_station, RCS_filter = read_variables(files_list)

#     fig = plt.figure(figsize=(10, 5))
#     axes = fig.add_subplot(111)
#     axes.set_ylim(y_min, y_max)
#     if ini_time and end_time:
#         user_ini_time = datetime.datetime(int(ini_time[0:4]), int(ini_time[4:6]), int(ini_time[6:8]), int(ini_time[9:11]), int(ini_time[12:14]), int(ini_time[15:16]))
#         user_end_time = datetime.datetime(int(end_time[0:4]), int(end_time[4:6]), int(end_time[6:8]), int(end_time[9:11]), int(end_time[12:14]), int(end_time[15:16]))
#         axes.set_xlim(user_ini_time, user_end_time)
#     plt.grid(True)
#     axes.set_xlabel('Time [UTC]')
#     axes.set_ylabel('Altitude [m asl]')
#     colormap = cm.jet
#     axes.set_title(format(time[0].day, '02d') + '/' + format(time[0].month, '02d') + '/' + str(time[0].year) + r', daily RCS at 532 nm')
#     m = axes.pcolormesh(time, altitude, RCS.T, cmap = colormap, vmin = c_min, vmax = c_max)
#     cbar = fig.colorbar(m, label = 'RCS [a.u.]')
#     cbar.formatter.set_powerlimits((0, 0))
#     cbar.ax.yaxis.set_offset_position('right')
#     cbar.update_ticks()
#     hours = mdates.HourLocator(interval = 1)
#     h_fmt = mdates.DateFormatter('%H:%M')
#     axes.xaxis.set_major_locator(hours)
#     axes.xaxis.set_major_formatter(h_fmt)
#     plt.fill_between([min(time),max(time)], [0,0], [z_station,z_station], alpha = 0.7, color = 'black')
#     plt.show()

# TODO verificar si el VLDR está considerado en el quicklook ya montado.
# def plot_volumdepol_quicklook(files_list, y_min = 0, y_max = 10000, ini_time = None, end_time = None, c_min = 0, c_max = 0.4):

#     altitude, time, beta_mol, delta_vol, RCS, z_station, RCS_filter = read_variables(files_list)

#     fig = plt.figure(figsize=(10, 5))
#     axes = fig.add_subplot(111)
#     axes.set_ylim(y_min, y_max)
#     if ini_time and end_time:
#         user_ini_time = datetime.datetime(int(ini_time[0:4]), int(ini_time[4:6]), int(ini_time[6:8]), int(ini_time[9:11]), int(ini_time[12:14]), int(ini_time[15:16]))
#         user_end_time = datetime.datetime(int(end_time[0:4]), int(end_time[4:6]), int(end_time[6:8]), int(end_time[9:11]), int(end_time[12:14]), int(end_time[15:16]))
#         axes.set_xlim(user_ini_time, user_end_time)
#     plt.grid(True)
#     axes.set_xlabel('Time [UTC]')
#     axes.set_ylabel('Altitude [m asl]')
#     colormap = cm.jet
#     axes.set_title(format(time[0].day, '02d') + '/' + format(time[0].month, '02d') + '/' + str(time[0].year) + r', daily $\delta_{\rm vol}$ at 532 nm')
#     m = axes.pcolormesh(time, altitude, delta_vol.T, cmap = colormap, vmin = c_min, vmax = c_max)
#     fig.colorbar(m, label = r'$\delta_{\rm vol}$')
#     hours = mdates.HourLocator(interval = 1)
#     h_fmt = mdates.DateFormatter('%H:%M')
#     axes.xaxis.set_major_locator(hours)
#     axes.xaxis.set_major_formatter(h_fmt)
#     plt.fill_between([min(time),max(time)], [0,0], [z_station,z_station], alpha = 0.7, color = 'black')
#     plt.show()


def get_norm(
    rcs: np.ndarray,
    scale_bounds: tuple[float, float] | None = None,
    color_resolution: int = 128,
) -> matplotlib.colors.BoundaryNorm:
    if scale_bounds is not None:
        bounds = np.linspace(*scale_bounds, 128)
    else:
        bounds = np.linspace(0, rcs.max() * 0.6, 128)

    norm = matplotlib.colors.BoundaryNorm(boundaries=bounds, ncolors=2**8)
    logger.debug(f"Color bounds min - max: {bounds.min()} - {bounds.max()}")

    return norm


def apply_labels(ax: matplotlib.axes.Axes, data_array: xr.DataArray) -> None:  # type: ignore
    # TODO: Other titles will later be added with config param
    plot.title1(data_array.name, 2)
    plot.title2(np.atleast_1d(data_array.time.mean().dt.date.values)[0].isoformat(), 2)
    # plot.title3(
    #     "{} ({:.1f}N, {:.1f}E)".format(
    #         data_array.attrs.get("site_location"),
    #         float(data_array.attrs["geospatial_lat_min"]),
    #         float(data_array.attrs["geospatial_lon_min"]),
    #     ),
    #     2,
    # )

    plot.watermark(ax, zoom=0.6, alpha=0.6)


def apply_gap_size(ax: matplotlib.axes.Axes, data_array) -> None:  # type: ignore
    diff = data_array.time[1:].values - data_array.time[0:-1].values
    gap_size = 2 * int(
        np.ceil(
            np.median(np.median(diff).astype("timedelta64[s]").astype("float") / 60)
        )
    )

    plot.gapsizer(
        ax,
        data_array.time.values.astype("M8[ms]").astype("O"),
        data_array.range.values,
        gap_size,
        "#c7c7c7",
    )


# TODO: this should be the default implemetation rather than filelist argument
def quicklook_xarray(
    data_array: xr.DataArray,
    scale_bounds: tuple[float, float] | None = None,
    is_rcs: bool = True,
    color_resolution: int = 128,
    colormap: str | matplotlib.colors.Colormap = "jet",
):
    if not is_rcs:
        rcs = data_array.values * data_array.range.values**2
    else:
        rcs = data_array.values

    fig, ax = plt.subplots(figsize=(15, 5))
    norm = get_norm(rcs, scale_bounds)

    q = ax.pcolormesh(
        data_array.time, data_array.range, rcs.T, cmap=colormap, norm=norm
    )

    ax.set_xlabel(r"Time, $[UTC]$")
    ax.set_ylabel(r"Height, $[km, \, agl]$")
    ax.set_ylim(0)

    apply_labels(ax, data_array=data_array)
    apply_gap_size(ax, data_array=data_array)

    fig.colorbar(q)

    q.cmap.set_over("white")  # type: ignore
