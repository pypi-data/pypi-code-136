import os
import sys
import glob
import shutil
import subprocess
import pathlib

import datetime as dt
import pandas as pd
import xarray as xr
from loguru import logger

from gfatpy.lidar.types import MeasurementType, LidarName

# TODO: Separate input from output dir in case NAS is not writable

# Source Code Dir
MODULE_DN = pathlib.Path(__file__)

""" MEASUREMENT TYPES
"""

# TODO: Use LIDAR_INFO yaml
MEASUREMENT_TYPES_DAYLIKE = ["RS", "OT", "HF"]
MEASUREMENT_TYPES_FOLDERLIKE = ["DC", "TC", "DP"]
MEASUREMENT_TYPES_FOLDERLIKE.extend(["TC-uv", "TC-vnir", "DP-pol", "DP-rot"])
MEASUREMENT_TYPES = MEASUREMENT_TYPES_DAYLIKE + MEASUREMENT_TYPES_FOLDERLIKE
MEASUREMENT_SUBTYPES = {
    "TC": ["N", "E", "S", "W", "N2"],
    "TC-uv": ["N", "E", "S", "W", "N2"],
    "TC-vnir": ["N", "E", "S", "W", "N2"],
    "DP": ["P45", "N45"],
    "DP-rot": ["P45", "N45"],
    "DP-pol": ["P45", "N45"],
}

""" LIDAR INFO
"""
# TODO: incluir procesado de sd en alhambra cuando sepamos sus factores de conversion a magnitudes fisicas
ORIGINAL_RAW2L1_DIR = pathlib.Path(__file__).parent.absolute() / "raw2l1_gfat"
LIDAR_NAMES = ["VELETA", "MULHACEN", "ALHAMBRA"]
LIDAR_INFO = {
    "MULHACEN": {"nick": "mhc", "conf_labels": ["rs_xf"]},
    "VELETA": {"nick": "vlt", "conf_labels": ["rs_xf"]},
    "ALHAMBRA": {
        "nick": "alh",
        "conf_labels": ["rs_ff", "rs_nf"]
        #'conf_labels': ['pd', 'rs_ff', 'rs_nf', 'sd_ff', 'sd_nf']
    },
}

""" Functions """


def check_dir(dir_name):
    """
    Check if a directory exists and is writable
    """
    return os.access(dir_name, os.W_OK)


def check_measurement_type(meas_type):
    """
    Check Measurement Type
    """

    if meas_type not in MEASUREMENT_TYPES:
        logger.error("%s not a measurement type. Exit" % meas_type)
        sys.exit()
    # return True if meas_type in meas_types else False


def read_config(config_fn):
    """
    Read Configuration File for lidar_raw2l1
    If none is given, default config is read

    """

    config = {}
    if config_fn is None:
        config_fn = MODULE_DN / "config" / "config_default.yaml"
    else:
        logger.error("File %s does not exist. Exit" % config_fn)
        sys.exit()

    return config


def setup_lidar(
    lidar_name,
    data_dn,
    lidar_config_prod_fn=None,
    lidar_raw_iletter=None,
    lidar_config_dn=None,
):
    """Setup of Lidar Information

    Args:
        lidar_name ([type]): [description]
        data_dn ([type]): [description]
        lidar_config_fn ([type], optional): [description]. Defaults to None.
        lidar_raw_iletter ([type], optional): [description]. Defaults to None.
        lidar_config_dn ([type], optional): [description]. Defaults to None.
    """

    if lidar_name in LIDAR_NAMES:
        lidar_setup = {}

        # nicklidar and config labels
        lidar_setup["lidar_name"] = lidar_name
        lidar_setup["nicklidar"] = LIDAR_INFO[lidar_name]["nick"]
        lidar_setup["configs"] = {}
        # raw data directory
        lidar_setup["raw_data_dn"] = os.path.join(data_dn, lidar_name, "0a")
        if not check_dir(lidar_setup["raw_data_dn"]):
            logger.error(
                "Folder %s does not exist or not writable. Exit"
                % lidar_setup["raw_data_dn"]
            )
            sys.exit(1)
        # L1 data directory
        lidar_setup["l1_data_dn"] = os.path.join(data_dn, lidar_name, "1a")
        if not check_dir(lidar_setup["l1_data_dn"]):
            logger.error(
                "Folder %s does not exist or not writable. Exit"
                % lidar_setup["l1_data_dn"]
            )
            sys.exit(1)
        # Lidar Config Ini File
        if lidar_config_prod_fn is None:  # READ DEAFULT VALUES
            if lidar_config_dn is not None:
                for cl in LIDAR_INFO[lidar_name]["conf_labels"]:
                    if lidar_name == "ALHAMBRA":
                        clfn = os.path.join(
                            lidar_config_dn, "conf_prod_%s_%s.ini" % (lidar_name, cl)
                        )
                    else:
                        clfn = os.path.join(
                            lidar_config_dn, "conf_prod_%s.ini" % lidar_name
                        )
                    if os.path.isfile(clfn):
                        lidar_setup["configs"][cl] = clfn
                    else:
                        logger.error("Lidar Config File %s does not exist. Exit" % clfn)
                        sys.exit(1)
            else:
                logger.error(
                    "Directory of Lidar Config File cannot be None. Exit"
                    % lidar_config_dn
                )
                sys.exit(1)
        else:  # USER-DEFINED
            if os.path.isfile(lidar_config_prod_fn):
                lidar_setup["configs"]["user-defined"] = lidar_config_prod_fn
            else:
                logger.error(
                    "Lidar Config File %s does not exist. Exit" % lidar_config_prod_fn
                )
                sys.exit(1)
        # Initial Letter for Raw Files
        if lidar_raw_iletter is None:
            lidar_setup["lidar_raw_iletter"] = "R"
    else:
        logger.error("Lidar %s does not exist. Exit" % lidar_name)
        sys.exit()

    return lidar_setup


def set_raw_file_pttn(lidar_raw_iletter, date_str):
    """
    Build Raw File Pattern
    """

    yyyy = date_str[:4]
    yy = date_str[2:4]
    mm = date_str[4:6]
    mx = format(int(mm), "X")
    dd = date_str[6:8]
    return "%s*%s%s%s??.*" % (lidar_raw_iletter, yy, mx, dd)


def set_meas_folder_pttn(meas_type, date_str):
    """
    Build Measurement Folder Pattern
    """
    yyyy = date_str[:4]
    mm = date_str[4:6]
    dd = date_str[6:8]
    return "%s_%s%s%s_*" % (meas_type, yyyy, mm, dd)


def set_raw_file_fullpath_pttn(raw_data_dn, date_str, meas_dir_pttn, raw_file_pttn):
    """
    Build Full Path for Raw Files Pattern
    """
    yyyy = date_str[:4]
    mm = date_str[4:6]
    dd = date_str[6:8]
    return os.path.join(raw_data_dn, yyyy, mm, dd, meas_dir_pttn, raw_file_pttn)


def set_dir_fullpath_pttn(raw_data_dn, date_str, meas_dir_pttn):
    """
    Build Full Path for Raw Files Pattern
    """
    yyyy = date_str[:4]
    mm = date_str[4:6]
    dd = date_str[6:8]
    return os.path.join(raw_data_dn, yyyy, mm, dd, meas_dir_pttn)


def get_meas_dir_date(meas_dir):
    """
    Get Date (str) YYYYMMDD_HHMM from measurement folder
    Assumed format: MEASTYPE_YYYYMMDD_HHMM
    """

    if meas_dir[-1] == "/":
        meas_dir = meas_dir[:-1]

    return "_".join(os.path.basename(meas_dir).split("_")[1:])


def prepare_L1a_output(nc_fullpath, overwrite):
    """ """
    nc_dn = os.path.dirname(nc_fullpath)
    nc_fn = os.path.basename(nc_fullpath)
    # Create folder if it does not exist
    if not check_dir(nc_dn):
        os.makedirs(nc_dn)
    # Remove 1a Netcdf if overwrite
    if os.path.isfile(nc_fullpath):
        logger.info(f"Writes file {nc_fn}")
        if overwrite:
            os.remove(nc_fullpath)
        else:
            logger.info("Keeps old version file")
            shutil.copyfile(
                nc_fullpath,
                "%s.%s" % (nc_fullpath, dt.datetime.utcnow().strftime("%Y%m%d_%H%M")),
            )


def run_raw2l1_daylike(lidar_setup, meas_type, date_str, overwrite=False):
    """
    Run Raw2L1 for daylike measurements: RS, OT, HF
    """

    logger.info("Start Run Raw2l1 for Daylike Measurement")

    # L1a Output Directory:
    nc_dn = os.path.join(
        lidar_setup["l1_data_dn"], date_str[:4], date_str[4:6], date_str[6:8]
    )

    # Build Raw File Pattern
    raw_file_pttn = set_raw_file_pttn(lidar_setup["lidar_raw_iletter"], date_str)

    """ Loop over Configs
    """
    for lc in lidar_setup["configs"]:
        # Conf Prod Ini File
        conf_prod_fn = lidar_setup["configs"][lc]
        logger.info("Config File: {}".format(conf_prod_fn))

        """ Fullpath for Netcdf (1a) """
        nc_fn = "{}_1a_P{}_{}_{}.nc".format(
            lidar_setup["nicklidar"], meas_type.lower(), lc, date_str
        )
        nc_fullpath = os.path.join(nc_dn, nc_fn)

        """ List of raw files """
        # Loop over [day - 1, day]
        date_dt = dt.datetime.strptime(date_str, "%Y%m%d")
        date_range = pd.date_range(date_dt + dt.timedelta(days=-1), date_dt)
        raw_files_list = []
        for i_date in date_range:
            i_date_str = i_date.strftime("%Y%m%d")
            logger.info("Search files at %s" % i_date_str)
            # Build Pattern for Measurement Folder
            meas_dir_pttn = set_meas_folder_pttn(meas_type, i_date_str)
            # Build Full Pattern
            full_path_pttn = set_raw_file_fullpath_pttn(
                lidar_setup["raw_data_dn"], i_date_str, meas_dir_pttn, raw_file_pttn
            )
            raw_files_list.extend(sorted(glob.glob(full_path_pttn)))

        """ Exe Raw2l1 """
        if len(raw_files_list) > 0:
            # Prepare L1a output
            prepare_L1a_output(nc_fullpath, overwrite)
            # Exe RAW2L1
            exe_raw2l1(date_str, conf_prod_fn, raw_files_list, nc_fullpath)
        else:
            logger.error("No Raw Files for %s and %s. Exit" % (meas_type, date_str))

    # Delete *part* files
    try:
        xx = glob.glob(os.path.join(nc_dn, "*part*"))
        for x in xx:
            os.remove(x)
    except:
        logger.warning("part files not deleted.")

    logger.info("End Run Raw2l1 for Daylike Measurement")


def run_raw2l1_folderlike(lidar_setup, meas_type, date_str, overwrite=False):
    """
    Run Raw2L1 for folderlike measurements: DC, TC, DP
    """

    logger.info(
        "Start Run Raw2l1 for Type {} (Folderlike Measurement)".format(meas_type)
    )

    # L1a Output Directory:
    nc_dn = os.path.join(
        lidar_setup["l1_data_dn"], date_str[:4], date_str[4:6], date_str[6:8]
    )

    # Build Raw File Pattern
    raw_file_pttn = set_raw_file_pttn(lidar_setup["lidar_raw_iletter"], date_str)
    logger.info("Search files at %s" % date_str)

    """ List of Folders within the date """
    # Build Full Pattern for Measurement Folder
    meas_dir_pttn = set_meas_folder_pttn(meas_type, date_str)
    full_path_dir_pttn = set_dir_fullpath_pttn(
        lidar_setup["raw_data_dn"], date_str, meas_dir_pttn
    )
    meas_dir_list = sorted(glob.glob(full_path_dir_pttn))
    if len(meas_dir_list) > 0:
        """Subtypes?"""
        if meas_type in MEASUREMENT_SUBTYPES.keys():
            sub_types = MEASUREMENT_SUBTYPES[meas_type]
        else:
            sub_types = []

        """ Loop over Raw Measurement Folders
        """
        for meas_dn in meas_dir_list:
            logger.info("Start Process Measurement Folder: {}".format(meas_dn))
            # YYYYMMDD_HHMM
            meas_datetime = get_meas_dir_date(meas_dn)

            """ Subtyping
            """
            if len(sub_types) > 0:  # subtypes (TC, DP)
                """Loop over Subtypes"""
                for sub_type in sub_types:
                    logger.info("Start Process Sub-Type {}".format(sub_type))
                    """ Loop Over Configs """
                    for lc in lidar_setup["configs"]:
                        # Conf Prod Ini File
                        conf_prod_fn = lidar_setup["configs"][lc]
                        logger.info("Config File: {}".format(conf_prod_fn))
                        """ Fullpath for Netcdf (1a) """
                        nc_fn = "{}_1a_P{}_{}_{}.nc".format(
                            lidar_setup["nicklidar"],
                            "%s-%s" % (meas_type.lower(), sub_type),
                            lc,
                            meas_datetime,
                        )
                        nc_fullpath = os.path.join(nc_dn, nc_fn)

                        """ List of raw files """
                        sub_meas_dn = os.path.join(meas_dn, sub_type)
                        if os.path.isdir(sub_meas_dn):
                            # Loop over [day - 1, day]
                            date_dt = dt.datetime.strptime(date_str, "%Y%m%d")
                            date_range = pd.date_range(
                                date_dt + dt.timedelta(days=-1), date_dt
                            )
                            raw_files_list = []
                            for i_date in date_range:
                                i_date_str = i_date.strftime("%Y%m%d")
                                logger.info("Search files at %s" % i_date_str)
                                # Build Full Pattern for Raw Files
                                raw_file_pttn = set_raw_file_pttn(
                                    lidar_setup["lidar_raw_iletter"], i_date_str
                                )
                                full_path_pttn = set_raw_file_fullpath_pttn(
                                    lidar_setup["raw_data_dn"],
                                    date_str,
                                    sub_meas_dn,
                                    raw_file_pttn,
                                )
                                raw_files_list.extend(sorted(glob.glob(full_path_pttn)))
                            if len(raw_files_list) > 0:
                                # Prepare L1a output
                                prepare_L1a_output(nc_fullpath, overwrite)
                                # Exe RAW2L1
                                exe_raw2l1(
                                    date_str, conf_prod_fn, raw_files_list, nc_fullpath
                                )
                            else:
                                logger.error(
                                    "No Raw Files for %s and %s" % (meas_type, date_str)
                                )
                        else:
                            logger.error(
                                "Subtype %s not found in measurement folder %s."
                                % (sub_type, meas_dn)
                            )
                    logger.info("End Process Sub-Type {}".format(sub_type))
            else:  # No subtypes (DC)
                """Loop Over Configs"""
                for lc in lidar_setup["configs"]:
                    # Conf Prod Ini File
                    conf_prod_fn = lidar_setup["configs"][lc]
                    logger.info("Config File: {}".format(conf_prod_fn))

                    """ Fullpath for Netcdf (1a) """
                    nc_fn = "{}_1a_P{}_{}_{}.nc".format(
                        lidar_setup["nicklidar"], meas_type.lower(), lc, meas_datetime
                    )
                    nc_fullpath = os.path.join(nc_dn, nc_fn)

                    """ List of raw files """
                    # Build Full Pattern for Raw Files
                    full_path_pttn = set_raw_file_fullpath_pttn(
                        lidar_setup["raw_data_dn"],
                        date_str,
                        os.path.basename(meas_dn),
                        raw_file_pttn,
                    )
                    raw_files_list = sorted(glob.glob(full_path_pttn))
                    if len(raw_files_list) > 0:
                        # Prepare L1a output
                        prepare_L1a_output(nc_fullpath, overwrite)
                        # Exe RAW2L1
                        exe_raw2l1(date_str, conf_prod_fn, raw_files_list, nc_fullpath)

                    else:

                        # Maybe there are binary files copied from other days
                        full_path_pttn = set_raw_file_fullpath_pttn(
                            lidar_setup["raw_data_dn"], date_str, meas_dn, "R*.*"
                        )
                        raw_files_list = sorted(glob.glob(full_path_pttn))
                        if len(raw_files_list) > 0:
                            # Prepare L1a output
                            prepare_L1a_output(nc_fullpath, overwrite)
                            # Exe RAW2L1
                            exe_raw2l1(
                                date_str, conf_prod_fn, raw_files_list, nc_fullpath
                            )
                        else:
                            logger.error(
                                "No Raw Files for %s and %s" % (meas_type, date_str)
                            )
            logger.info("End Process Measurement Folder: {}".format(meas_dn))
    else:
        logger.error("No Folder(s) for %s and %s. Exit" % (meas_type, date_str))

    # Delete *part* files
    try:
        xx = glob.glob(os.path.join(nc_dn, "*part*"))
        for x in xx:
            os.remove(x)
    except:
        logger.warning("part files not deleted.")

    logger.info("End Run Raw2l1 for Type {} (Folderlike Measurement)".format(meas_type))


def run_raw2l1(lidar_setup, meas_type, date_str, overwrite=False):
    """
    Run RAW2L1

    for a particular lidar
    for a measurement type
    for a date

    """

    """ RAW2L1 particularized to Measurement Types """
    if meas_type in MEASUREMENT_TYPES_DAYLIKE:
        run_raw2l1_daylike(lidar_setup, meas_type, date_str, overwrite=overwrite)
        run_raw2l1_folderlike(lidar_setup, "DC", date_str, overwrite=overwrite)
    elif meas_type in MEASUREMENT_TYPES_FOLDERLIKE:
        run_raw2l1_folderlike(lidar_setup, meas_type, date_str, overwrite=overwrite)
        if meas_type != "DC":
            run_raw2l1_folderlike(lidar_setup, "DC", date_str, overwrite=overwrite)
    else:
        logger.error("Meas. Type %s not recognized. Exit" % meas_type)


def exe_raw2l1(date_str, lidar_config, raw_files_list, nc_output):
    """
    Python call to raw2l1
    """
    logger.info("Start Exe RAW2L1")

    pathlib.Path(__file__).parent.absolute()
    raw2l1_py = ORIGINAL_RAW2L1_DIR / "raw2l1" / "raw2l1.py"

    """ Split Raw2L1 process in 60-file packages """
    # Join Files List in a single string
    # raw_files_list = [x.replace(lidar_setup['raw_data_dn'], r".") for x in raw_files_list]
    nf = len(raw_files_list)
    step = 60
    nc_fns = []
    for i in range(0, nf, step):
        raw_files_list_str = " ".join(raw_files_list[i : (i + step)])
        nc_fn = "{}.part_{}".format(nc_output, i)
        # working_dn = os.getcwd()
        # os.chdir(lidar_setup['raw_data_dn'])
        # os.chdir(working_dn)
        python_exe = sys.executable
        cmd = "%s %s %s %s %s %s" % (
            python_exe,
            raw2l1_py,
            date_str,
            lidar_config,
            raw_files_list_str,
            nc_fn,
        )
        # print(cmd)
        # os.system(cmd)

        try:
            print(cmd)
            # os.system(cmd)
            p = subprocess.run(
                cmd,
                capture_output=True,
                shell=True,
            )
        except Exception as e:
            logger.error(e)
            raise RuntimeError("Raw2l1 command failed")

        if p.returncode != 0:
            logger.critical(f"Raw2l1 with args {p.args} resulted in error")
            raise subprocess.CalledProcessError(
                returncode=p.returncode, cmd=p.args, stderr=p.stderr, output=p.stdout
            )

        nc_fns.append(nc_fn)

        if os.path.isfile(nc_fn):
            logger.info(f"File {nc_fn} has been created.")
        else:
            logger.critical(f"File {nc_fn} NOT created.")
            raise RuntimeError(f"File {nc_fn} NOT created.")

    """ Concatenate Netcdf Files """
    if len(nc_fns) > 0:
        ds = None
        for nc_fn in nc_fns:
            if os.path.isfile(nc_fn):
                try:
                    with xr.open_dataset(nc_fn) as dsi:
                        if ds is None:
                            ds = dsi
                        else:
                            ds = xr.concat(
                                [ds, dsi],
                                dim="time",
                                data_vars="minimal",
                                coords="minimal",
                                compat="override",
                            )
                except:
                    logger.critical(f"File {nc_fn} not concatenated")
                    raise RuntimeError(f"File {nc_fn} not concatenated")
        if ds is not None:
            ds.to_netcdf(nc_output)
        else:
            logger.critical("Dataset is None. Netcdf File not generated")
            raise RuntimeError("Dataset is None. Netcdf File not generated")
    else:
        logger.critical("Dataset is None. Netcdf File not generated")
        raise RuntimeError("Dataset is None. Netcdf File not generated")

    logger.info("End Exe RAW2L1")


def lidar_raw2l1(
    lidar_name: LidarName | str,
    data_dir: pathlib.Path | str,
    measurement_type: MeasurementType | str,
    initial_date: dt.datetime,
    final_date: dt.datetime = None,
    overwrite: bool = False,
) -> None:
    """_summary_

    Args:
        lidar_name (LidarName | str): _description_
        data_dir (pathlib.Path | str): _description_
        measurement_type (MeasurementType | str): _description_
        initial_date (dt.datetime): _description_
        final_date (dt.datetime, optional): _description_. Defaults to None.
        overwrite (bool, optional): _description_. Defaults to False.
    """

    logger.info(f"Start RAW2L1")

    """ parse args """

    if final_date is None:
        final_date = initial_date

    if isinstance(measurement_type, MeasurementType):
        check_measurement_type(measurement_type.value)
        measurement_type = measurement_type.value
    else:
        check_measurement_type(measurement_type)

    if isinstance(lidar_name, LidarName):
        lidar_name = lidar_name.value

    lidar_config_dn = ORIGINAL_RAW2L1_DIR / "raw2l1" / "conf"
    lidar_setup = setup_lidar(
        lidar_name,
        data_dir,
        lidar_config_prod_fn=None,
        lidar_raw_iletter=None,  # TODO: I have no idea what this does
        lidar_config_dn=lidar_config_dn,
    )

    """ Run RAW2L1 """
    date_range = pd.date_range(initial_date, final_date)
    for i_date in date_range:
        i_date_str = i_date.strftime("%Y%m%d")
        run_raw2l1(lidar_setup, measurement_type, i_date_str, overwrite=overwrite)

    logger.info("End RAW2L1")


if __name__ == "__main__":
    lidar_raw2l1()
