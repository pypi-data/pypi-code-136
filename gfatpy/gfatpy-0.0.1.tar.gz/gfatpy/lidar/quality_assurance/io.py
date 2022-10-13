from pathlib import Path

from datetime import datetime
import xarray as xr
import numpy as np

from gfatpy import DATA_DN
from gfatpy.lidar.utils import LIDAR_INFO
from gfatpy.lidar.file_manager import channel2info


def rayleigh2earlinet(dataset: xr.Dataset, output_dir: Path | None):

    # info from dataset
    date = datetime.strptime(
        dataset.attrs["datetime_ini"], dataset.attrs["datetime_format"]
    )
    date_str = datetime.strftime(date, "%d.%m.%Y, %HUTC")
    lidar_name: str = dataset.attrs["lidar_name"].upper()
    lidar_location: str = dataset.attrs["lidar_location"]
    lidar_id: str = dataset.attrs["lidar_id"]
    channel: str = dataset.attrs["channel"]
    year: str = f"{date.year}"
    month: str = f"{date.month:02d}"
    day: str = f"{date.day:02d}"
    detection_mode: str = dataset["detection_mode"].values.item()
    if detection_mode == "a":
        dark_subtracted_str: str = dataset.attrs["dark_subtracted"]
    else:
        dark_subtracted_str: str = ""
    duration = float(dataset.attrs["duration"])
    wavelength, _, polarization_, mode_ = channel2info(channel)
    radiosonde_location = dataset.attrs["radiosonde_location"]
    radiosonde_wmo_id = dataset.attrs["radiosonde_wmo_id"]
    radiosonde_date = datetime.strptime(
        dataset.attrs["radiosonde_datetime"], "%Y-%m-%dT%H-%M-%S"
    )
    pol_str = LIDAR_INFO["metadata"]["code_polarization_str2long_name"][polarization_]
    mode_str = LIDAR_INFO["metadata"]["code_mode_str2long_name"][mode_]
    z_min, z_max = dataset.attrs["rayleigh_height_limits"]

    # create output_dir
    if output_dir is None:
        if DATA_DN is None:
            raise ValueError("DATA_DN is None.")
        else:
            output_dir = DATA_DN

    if not output_dir.exists():
        raise NotADirectoryError(f"{output_dir} not found.")

    output_dir = output_dir / lidar_name / "QA" / "rayleigh_fit" / year / month / day

    output_dir.mkdir(parents=True, exist_ok=True)

    rf_nc_fn = output_dir / f"{lidar_id}RayleighFit{channel}.nc"
    dataset.to_netcdf(rf_nc_fn)

    # # Filename
    rf_fn = output_dir / f"{lidar_id}RayleighFit{channel}.csv"

    # Select Columns to write
    cols = ["BCS", "RCS"]
    if detection_mode == "a":  # (if analog)
        cols.append("DC")
    rf_df = dataset[cols].to_dataframe()
    rf_df.columns = [dataset[col].attrs["name"] for col in cols]

    # Write File Earlinet Format
    with open(rf_fn, "w") as f:
        f.write(f"station ID = {lidar_id} ({lidar_location})\n")
        f.write(f"system = {lidar_name}\n")
        f.write(
            f"signal = {wavelength}, {pol_str}, {mode_str}, {dark_subtracted_str}\n"
        )
        f.write(
            f"date of measurement, time, duration of measurement= {date_str}, {duration:.1f} s\n"
        )
        f.write(
            f"location, WMO radiosonde station ID, date of radiosonde = {radiosonde_location}, {radiosonde_wmo_id}, {radiosonde_date}\n"
        )
        f.write(
            f"lower and upper Rayleigh height limits = {np.round(z_min)}, {np.round(z_max)}\n"
        )
    f.close()

    # write in the same file the rest of information
    rf_df.index = rf_df.index.map(lambda x: "%.4f" % x)
    rf_df.to_csv(rf_fn, mode="a", header=True, na_rep="NaN", float_format="%.4e")
    return rf_nc_fn, rf_fn
