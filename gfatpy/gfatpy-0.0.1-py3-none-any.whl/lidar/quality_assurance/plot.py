from pathlib import Path

import xarray as xr
from datetime import datetime
from matplotlib.axes import Axes
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib.colors as mcolors

from gfatpy import DATA_DN
from gfatpy.lidar.file_manager import channel2info


def plot_rayleigh_fit(
    filepath: Path,
    output_dir: Path | None = None,
    save_fig: bool = False,
) -> tuple[Figure | None, Axes | None]:

    if not filepath.exists():
        raise FileNotFoundError(f"{filepath} not found.")

    # read data
    dataset = xr.open_dataset(filepath)

    # info
    lidar_name: str = dataset.attrs["lidar_name"]
    channel = dataset.attrs["channel"]
    wavelength = (channel2info(channel))[0]
    z_min, z_max = dataset.attrs["rayleigh_height_limits"]
    initial_date = datetime.strptime(
        dataset.attrs["datetime_ini"], dataset.attrs["datetime_format"]
    )
    final_date = datetime.strptime(
        dataset.attrs["datetime_end"], dataset.attrs["datetime_format"]
    )
    year = str(initial_date.year)
    month = f"{initial_date.month:02d}"
    day = f"{initial_date.day:02d}"

    date4filename = datetime.strftime(initial_date, "%Y%m%d-%H%M")
    if initial_date.date() == final_date.date():
        date_str = datetime.strftime(initial_date, "%Y-%m-%d")
        initial_time = datetime.strftime(initial_date, "%H:%M")
        final_time = datetime.strftime(final_date, "%H:%M")
        show_datetime_as = f"{date_str} from {initial_time} to {final_time} UTC"
    else:
        initial_date = datetime.strftime(initial_date, "%H:%M %Y-%m-%d")
        final_date = datetime.strftime(final_date, "%H:%M %Y-%m-%d")
        show_datetime_as = f"{initial_date} to {initial_date}"

    """ FIGURE """
    fig_title = f"{lidar_name} Rayleigh fit - channel {channel} | {show_datetime_as} | Reference height: {z_min}-{z_max} km"
    fig_y_label = "Normalized attenuated backscatter, #"
    x_lim = (dataset.range.min(), dataset.range.max())
    y_lim = (1e-2, 50)

    raw_colors = {
        355: mcolors.CSS4_COLORS["aliceblue"],  # type: ignore
        532: mcolors.CSS4_COLORS["honeydew"],  # type: ignore
        1064: mcolors.CSS4_COLORS["seashell"],  # type: ignore
    }

    smooth_colors = {355: "b", 532: "g", 1064: "r"}
    if wavelength in smooth_colors:
        raw_color = raw_colors[wavelength]
        smooth_color = smooth_colors[wavelength]
    else:
        raw_color = mcolors.CSS4_COLORS["aliceblue"]  # type: ignore
        smooth_color = "b"

    fig = plt.figure(figsize=(15, 6))
    ax = fig.add_subplot(111)
    ax.grid(which="both", **{"lw": 1})
    dataset["RCS_norm"].plot(ax=ax, x="range", label="raw", color=raw_color)
    dataset["BCS_norm"].plot(
        ax=ax,
        x="range",
        label=r"$\beta_{att}^{mol}$",
        color="k",
        ls="dashed",
        linewidth=2,
    )
    dataset["RCS_smooth_norm"].plot(
        ax=ax, x="range", label="smoothed", color=smooth_color
    )
    ax.set_title(fig_title, fontsize="medium")
    ax.xaxis.get_label().set_fontsize("medium")
    ax.xaxis.set_minor_locator(ticker.MultipleLocator(1))
    ax.set_ylabel(fig_y_label, fontsize="medium")
    ax.set_xlabel("Range, km", fontsize="medium")
    ax.set_xlim(x_lim)
    ax.set_ylim(*y_lim)
    ax.set_yscale("log")
    leg = ax.legend(fontsize="medium")
    frame = leg.get_frame()
    frame.set_edgecolor("black")
    frame.set_facecolor("silver")

    if save_fig:
        # create output_dir
        if output_dir is None:
            if DATA_DN is None:
                raise ValueError("DATA_DN is None.")
            else:
                output_dir = DATA_DN

        if not output_dir.exists():
            raise NotADirectoryError(f"{output_dir} not found.")

        # Create file path
        output_dir = (
            output_dir / lidar_name / "QA" / "rayleigh_fit" / year / month / day
        )
        output_dir.mkdir(parents=True, exist_ok=True)
        fig_fn = output_dir / f"{lidar_name}_RF_{channel}_{date4filename}.png"

        plt.tight_layout()
        plt.savefig(fig_fn, dpi=300, bbox_inches="tight")
    else:
        fig, ax = None, None

    return fig, ax
