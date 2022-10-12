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

import numpy as np

from lkcom.util import isarray
from lkcom.string import check_lstr_in_str

def get_file_sz(FileName):
    return os.path.getsize(FileName)

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


def list_files_by_pattern(path, match_pattern=None, excl_pattern=None, with_path=False):
    """List file names that conntain all strings in the pattern list."""
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
        return [Path(path).joinpath(Path(file_name)) for file_name in matched_file_names]
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
