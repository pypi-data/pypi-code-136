import os
from pathlib import Path
from pdb import set_trace

import datetime
import numpy as np

from gfatpy import DATA_DN
from gfatpy.lidar import file_manager
from gfatpy.lidar.utils import LIDAR_INFO


def GHK_simulator(
    lidar_nick: str,
    calibrator: str,
    target_date: datetime.date,
    channel: str | None = None,
    out_dir: Path | None = None,
) -> list[Path]:

    lidar_name: str = LIDAR_INFO["metadata"]["nick2name"][lidar_nick]

    if channel is None:
        channels = LIDAR_INFO["lidars"][lidar_name]["GHK_channels"]
    else:
        channels = [channel]
    output_paths = []
    for channel_ in channels:
        # Ini file for each channel
        ini_filepath = find_GHK_ini_file(
            lidar_nick, channel_, target_date, calibrator=calibrator
        )

        if not ini_filepath.exists():
            raise FileNotFoundError(f"Ini file not found: {ini_filepath}.")

        if out_dir is None:
            if DATA_DN is not None:
                target_date_str = target_date.strftime("%Y%m%d_%H%M")
                out_dir = (
                    DATA_DN
                    / lidar_name
                    / "depolarization"
                    / "GHK"
                    / f"{target_date.year:04d}"
                    / f"{target_date.month:02d}"
                    / f"{target_date.day:02d}"
                    / target_date_str
                )
            else:
                raise NotADirectoryError("DATA_DN is None.")

        if not out_dir.exists():
            out_dir.mkdir(parents=True)
            # raise NotADirectoryError(f"{out_dir} not found.")

        output_path_ = run_GHK_simulator(ini_filepath, out_dir)
        if isinstance(output_path_, Path):
            output_paths.append(output_path_)

        # set_trace()
        # GHK_dict = ghk_output_reader(output_path)
    return output_paths


def find_GHK_ini_file(
    lidar_nick: str,
    channel: str,
    target_date: datetime.date,
    calibrator: str = "rot",
    ini_dir: Path | None = None,
) -> Path:

    if ini_dir is None:
        root_dir = Path(__file__).parent.absolute()
        ini_dir = root_dir / "GHK" / "system_settings"

        if not ini_dir.exists():
            raise NotADirectoryError("DATA_DN is None.")

    if not ini_dir.exists():
        raise NotADirectoryError(f"{ini_dir} not found.")
    candidates, dates = file_manager.extract_filenames_dates_from_wildcard(
        ini_dir, f"optic_input_{lidar_nick}_{calibrator}_{channel}*.py"
    )

    idx = np.abs(
        dates.astype("M8[ns]").astype(float)
        - np.array(target_date).astype("M8[ns]").astype(float).mean()
    ).argmin()
    ini_path = candidates[idx]

    return ini_path


def run_GHK_simulator(ini_path: Path, out_dir: Path) -> None:
    # run GHK: uses ghk_inp_fn as Input. Generates ghk_param_fn

    # if not ini_path.exists():
    #     raise FileNotFoundError('Ini path not found.')

    current_path = Path(__file__).parent.absolute()
    GHK_path = current_path / "GHK" / "GHK_0.9.8h_Py3.7.py"
    # os.chdir(current_path / "GHK")

    os.environ["GHK_FILE"] = str(ini_path)

    out_dir.mkdir(parents=True, exist_ok=True)
    set_trace()
    os.system(
        f"python {GHK_path} {ini_path} {out_dir.absolute()}"
    )  # FIXME: variables de entorno lo que quiera que sea eso
    os.chdir(current_path)
    (current_path / "GHK" / "output_files").rglob(f"*{ini_path}*.dat")
    # shutil.copyfile(ini_path, out_dir)
    # shutil.copyfile(output_files, out_dir)
    # return output_path
