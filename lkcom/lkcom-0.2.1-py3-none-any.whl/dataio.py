"""lkcom - a Python library of useful routines.

This module contains data input and output utilities.

Copyright 2015-2022 Lukas Kontenis
Contact: dse.ssd@gmail.com
"""
import os
import sys
import zipfile
import glob
from pathlib import Path
import json
import time
import datetime

import numpy as np

from lkcom.util import isarray
from lkcom.string import check_lstr_in_str, strip_whitespace, strip_nonnum


def get_file_sz(FileName):
    return os.path.getsize(FileName)


def get_file_creation_date(file_name):
    return os.path.getctime(file_name)


def get_file_creation_date_str(file_name):
    return time.strftime(
        "%Y-%m-%d",
        time.gmtime(get_file_creation_date(file_name)))


def parse_csv_header(file_name, key):
    """Find a value for a given key in the header of a CSV file.

    The expected CSV file format is:
    # Comments, key1: value1, key2: value2, ...
    # Var1 (Unit1), Var2 (Unit2)
    [Data]

    """
    with open(file_name) as file_h:
        for line in file_h:
            if line[0] != '#':
                break
            if line.find(key) != -1:
                return line.split(key)[1].split(',')[0]


def read_json(file_name_arg):
    """Read a JSON file.

    If 'file_name_arg' is a single file name the file is parsed as json and an
    exception is raised if hat fails. If 'file_name_arg' is a list list of file
    names the files are read until one of them is successfully parsed as a
    JSON.
    """
    if isarray(file_name_arg):
        for file_name in file_name_arg:
            if check_file_exists(file_name):
                return json.load(open(file_name))
        return None
    else:
        file_name = file_name_arg
        return json.load(open(file_name))


def json_multiget(data, key_arg, default_val=None):
    """Get a JSON value from multiple keys."""
    if isarray(key_arg):
        for key in key_arg:
            val = data.get(key)
            if val:
                return val
        return default_val
    else:
        return data.get(key_arg, default_val)


def check_file_exists(file_path):
    """Check if a file exists."""
    try:
        return os.path.isfile(file_path)
    except FileNotFoundError:
        return False


def read_bin_file(file_name):
    """Read a serialized 3D array.

    Read a binary file containting a serialized 3D array of uint32 values. The
    first three words of the array are the original 3D array dimmensions.

    Btw, this is the default way that LabVIEW writes binary data.
    """
    if Path(file_name).suffix == '.zip':
        # Look for DAT files inside the ZIP archive
        zip_contents = zipfile.ZipFile(file_name).namelist()
        for zip_file_name in zip_contents:
            if Path(zip_file_name).suffix == '.dat':
                # Seems like numpy cannot read binary data from a ZIP file
                # using fromfile() if the file handle is provided using
                # zipfile. This is due to the fact that fromfile() relies on
                # fileno which is not provided by the zipfile.ZipFile object.
                # A workaround is to use ZipFile.read() to read the raw byte
                # array from the ZIP archive and then frombuffer to parse the
                # byte array into a numpy array.
                serdata = np.frombuffer(
                    zipfile.ZipFile(file_name).read(zip_file_name),
                    dtype='uint32')
                break
    else:
        serdata = np.fromfile(file_name, dtype='uint32')

    serdata = serdata.newbyteorder()

    num_pages = serdata[0]
    num_rows = serdata[1]
    num_col = serdata[2]
    page_sz = num_rows*num_col

    serdata = serdata[3:]

    data = np.ndarray([num_rows, num_col, num_pages], dtype='uint32')

    for ind_pg in range(num_pages):
        data[:, :, ind_pg] = np.reshape(
            serdata[ind_pg*page_sz:(ind_pg+1)*page_sz], [num_rows, num_col])

    return data


def list_files_with_extension(
        path=None, ext="dat",
        name_exclude_filter=None, name_include_filter=None):
    """List files that have a specific extension."""

    if ext[0] == '.':
        print("Specify extension as 'txt', do not include the dot")

    if path is None:
        path = '.\\'

    List = os.listdir(path)

    Paths = []

    for FileName in List:
        filter_hit = False
        if name_exclude_filter:
            if isarray(name_exclude_filter):
                for name_exclude_filter1 in name_exclude_filter:
                    if(FileName.find(name_exclude_filter1) != -1):
                        filter_hit = True
                        break
            else:
                if(FileName.find(name_exclude_filter1) != -1):
                    filter_hit = True
                    break

        if name_include_filter:
            if(FileName.find(name_include_filter) == -1):
                filter_hit = True
                continue

        if not filter_hit:
            ext_ind = FileName.rfind(".")
            if(ext_ind != -1 and FileName[ext_ind+1:] == ext):
                Paths.append(str(Path(path).joinpath(FileName)))

    return Paths


def list_files_with_filter(filter_str="*"):
    return glob.glob(filter_str)


def list_dirs(path):
    dir_names = []
    with os.scandir(path) as it:
        for entry in it:
            if entry.is_dir():
                dir_names.append(entry.name)

    return dir_names


def list_files_by_pattern(path, match_pattern=None, excl_pattern=None,
                          with_path=False):
    """List files that include a given pattern.

    List file names in the given path that conntain all strings in the pattern
    list.
    """
    file_names = os.listdir(path)
    matched_file_names = []
    for file_name in file_names:
        if match_pattern:
            match_result = check_lstr_in_str(file_name, match_pattern)
        else:
            match_result = [False]
        if excl_pattern:
            excl_result = [not elem for elem in
                           check_lstr_in_str(file_name, excl_pattern)]
        else:
            excl_result = [True]
        if all(elem is True for elem in match_result) \
                and all(elem is True for elem in excl_result):
            matched_file_names.append(file_name)

    if with_path:
        return [Path(path).joinpath(Path(file_name)) for
                file_name in matched_file_names]
    else:
        return matched_file_names


def check_file_exists(file_path):
    try:
        return os.path.isfile(file_path)
    except FileNotFoundError:
        return False


def read_big_file(FileName, max_row=None):
    f_sz = get_file_sz(FileName)

    fin = open(FileName, 'r')
    line = ' '
    ind = 0
    try:
        while(1):
            line = fin.readline()

            if(line == ''):
                break

            l_data = line.split('\t')

            if(ind == 0):
                l_sz = len(line)
                num_row = int(np.ceil(f_sz/l_sz))
                f_num_row = num_row
                if max_row is not None and num_row > max_row:
                    num_row = max_row
                num_col = len(l_data)

                D = np.ndarray([num_row, num_col])

            for indC in range(0, num_col):
                D[ind, indC] = float(l_data[indC])

            ind = ind + 1

            if ind % 1E5 == 0:
                print("{:d}k lines read, {:.3f} of chunk, {:.3f} "
                      "of file".format(ind/1E3, ind/num_row, ind/f_num_row))

            if max_row is not None and ind >= max_row:
                break
    except Exception:
        print("Error while reading")

    fin.close()

    return np.resize(D, [ind, num_col])


def read_starlab_file(FileName, max_row=None):
    """
    Read a text log file produced by StarLab.
    """
    f_sz = get_file_sz(FileName)

    fin = open(FileName, 'r')
    line = ''
    ind = 0
    try:
        with open(FileName) as fin:
            for line in fin:
                if line == '' or line[0] == ';' or line[0] == '!' \
                        or line == '\n':
                    continue

                if line.find('Timestamp') != -1:
                    continue

                l_data = line.strip().split('\t')

                if ind == 0:
                    l_sz = len(line)
                    num_row = int(np.ceil(f_sz/l_sz))
                    f_num_row = num_row
                    if max_row is not None and num_row > max_row:
                        num_row = max_row
                    num_col = len(l_data)

                    D = np.ndarray([num_row, num_col])

                for indC in range(0, num_col):
                    D[ind, indC] = float(l_data[indC])

                ind = ind + 1

                if ind % 1E5 == 0:
                    print("{:d}k lines read, {:.3f} of chunk, {:.3f} of "
                          "file".format(ind/1E3, ind/num_row, ind/f_num_row))

                if max_row is not None and ind >= max_row:
                    break

    except Exception:
        print("Error while reading file")
        exc_type, _, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno)

    fin.close()

    D = np.resize(D, [ind, num_col])

    return D


def read_text_sa_file(file_name):
    """Read a generic text file containing spectrum analyzer data."""
    data = np.loadtxt(file_name, delimiter=',')

    rbw = None
    attn = None
    with open(file_name) as file_h:
        for line in file_h:
            if line[0] != '#':
                break
            if line.find('bw:') != -1:
                rbw = float(line.split('bw: ')[1].split(',')[0])

    cfg = {'RBW': rbw, 'Attenuation': attn}

    return data, cfg


def read_rigol_sa_csv(file_name):
    with open(file_name) as f:
        cfg = {}
        for line in f:
            if line.find('DATA,') >= 0:
                break
            param, val = line.split(',')
            val = strip_whitespace(val)
            if len(strip_nonnum(val)) > 0:
                if val.find('.') >= 0 or val.find('e') > 0:
                    cfg[param] = float(val)
                else:
                    cfg[param] = int(val)
    return [np.loadtxt(file_name, skiprows=32, delimiter=','), cfg]


def read_power_meter_data(file_name=None):
    """Read PowerMeter data with timestamps."""
    if file_name is None:
        file_name = list_files_with_extension(
            ext='dat', name_include_filter='powerData')[0]

    print("Loading PowerMeter data from {:}...".format(file_name))
    pwr_log_data = np.loadtxt(
        file_name, skiprows=2, delimiter='\t', usecols=[0, 3])

    pwr_log = dict()
    pwr_log['t0'] = datetime.datetime.strptime(
        str(np.loadtxt(
            file_name, delimiter='\t',
            skiprows=2, usecols=2, max_rows=1, dtype='str')),
        "%y%m%d %H:%M:%S.%f")

    pwr_log['tarr'] = pwr_log_data[:, 0]
    pwr_log['vals'] = pwr_log_data[:, 1]

    return pwr_log


def read_pharos_log(file_name=None):
    """Read sensor data from PHAROS log files.

    Currently only temperature and humidity sensors are supported.
    """
    log_data = np.loadtxt(
        file_name, delimiter='\t',
        dtype={'names': ('hours', 'timestamp', 'val'),
               'formats': ('float', datetime.datetime, 'float')})

    if file_name.find('temp') != -1:
        file_name_fmt = "Ambient temperature %Y-%m-%d %H-%M.dat"
    elif file_name.find('humidity') != -1:
        file_name_fmt = "Ambient humidity %Y-%m-%d %H-%M.dat"
    else:
        print("Can't determine sensor type from file name")
        return None

    # PHAROS1 log files do not have datestamps, only hours. File names contain
    # the full timestamp or approximately the last datapoint. Therefore,
    # timestamps for all datapoints can be restored by counting back from the
    # last datapoint.

    # Full timestamp of the last datapoint from file name
    ts1 = datetime.datetime.strptime(file_name, file_name_fmt)

    # Timestamp of the last datapoint from the data log, without the date
    ts2 = datetime.datetime.strptime(log_data[-1][1], "%H:%M:%S.%f")

    # Replace the year month and day of the data log timestamp with the one
    # from the file name
    ts2 = ts2.replace(year=ts1.year, month=ts1.month, day=ts1.day)

    log = dict()
    log['t0'] = ts2 - datetime.timedelta(seconds=log_data[-1][0])
    log['tarr'] = np.array([entry[0]/60/60 for entry in log_data])
    log['vals'] = np.array([entry[2] for entry in log_data])

    return log


def read_ezlog(file_name):
    """Read temperature and RH data from EZ logger CSV file."""
    log_data = np.loadtxt(
        file_name, skiprows=11, delimiter=',', usecols=[1, 2, 3],
        dtype={'names': ('date', 'temp', 'rh'),
               'formats': (datetime.datetime, 'float', 'float')})

    log = dict()
    log['t0'] = datetime.datetime.strptime(log_data[0][0], "%Y/%m/%d %H:%M:%S")

    log['tarr'] = [(datetime.datetime.strptime(entry[0], "%Y/%m/%d %H:%M:%S") -
                   log['t0']).total_seconds()/60/60 for entry in log_data]
    log['temp'] = [entry[1] for entry in log_data]
    log['rh'] = [entry[2] for entry in log_data]
    return log


def read_beam_steering_log():
    """Read T4 beam steering positioning log."""
    signal_names = [
        'A Motor X', 'A Motor Y', 'B Motor X', 'B Motor Y',
        'A Measured X', 'A Measured Y', 'B Measured X', 'B Measured Y']
    pos_log = [dict() for signal in signal_names]

    for ind, signal in enumerate(signal_names):
        pos_log[ind]['tarr'] = np.array([])
        pos_log[ind]['val'] = np.array([])
        pos_log[ind]['signal_names'] = signal_names

    for dir_name_month in list_dirs('positioning'):
        for dir_name_day in list_dirs('positioning/' + dir_name_month):
            for ind, signal in enumerate(signal_names):
                file_name = 'positioning/' + dir_name_month + '/' + \
                    dir_name_day + '/{:s}.txt'.format(signal)
                print("Reading file ", file_name)
                try:
                    pos_log_data = np.loadtxt(
                        file_name, delimiter=',', usecols=[0, 2],
                        dtype={'names': ('date', 'pos'),
                               'formats': (datetime.datetime, 'float')})

                    if pos_log[ind].get('t0') is None:
                        pos_log[ind]['t0'] = datetime.datetime.strptime(
                            pos_log_data[0][0], "%Y-%m-%d %H:%M:%S.%f")

                    pos_log[ind]['tarr'] = np.append(
                        pos_log[ind]['tarr'],
                        np.array([(datetime.datetime.strptime(entry[0],
                                   "%Y-%m-%d %H:%M:%S.%f")
                                   - pos_log[ind]['t0']).total_seconds()/60/60
                                  for entry in pos_log_data]))

                    pos_log[ind]['val'] = np.append(
                        pos_log[ind]['val'],
                        np.array([entry[1] for entry in pos_log_data]))

                except Exception as excpt:
                    print("Failed to read log file with exception", excpt)
                    print("Retrying line-by-line")
                    file = open(file_name)
                    for line in file:
                        col_data = line.split(',')

                        # Make sure there are exacly three columns in the line
                        if len(col_data) != 3:
                            continue

                        # Parse the timestamp and do some sanity checks
                        try:
                            data_ts = datetime.datetime.strptime(
                                col_data[0], "%Y-%m-%d %H:%M:%S.%f")
                            if data_ts.year < 1990 or data_ts.year > 2100:
                                continue

                            data_val = float(col_data[2])
                            if np.abs(data_val) > 1000:
                                continue
                        except Exception:
                            continue

                        if pos_log[ind].get('t0') is None:
                            pos_log[ind]['t0'] = data_ts

                        pos_log[ind]['tarr'] = np.append(
                            pos_log[ind]['tarr'],
                            float((data_ts -
                                   pos_log[ind]['t0']).total_seconds()/60/60))

                        pos_log[ind]['val'] = np.append(
                            pos_log[ind]['val'],
                            data_val)

    return pos_log
