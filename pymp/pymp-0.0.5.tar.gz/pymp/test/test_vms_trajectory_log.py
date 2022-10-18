# -*- coding: utf-8 -*-
"""
Copyright (c) 2015 Michael J Tallhamer

Varian Trajectory Log Definitions
Field definitions for Varian trajectory logs as layed out in the "TrueBeam 2.7MR2 Trajectory Log File Specification"
found on the myvarian site (https://varian.force.com/)

@author: Michael J Tallhamer M.Sc DABR (mike.tallhamer@pm.me)
"""

import os
import io

import numpy as np
import pandas as pd
import pytest

# import pymp.vms.log.trajectory as tlog
# from pymp.vms.log.trajectory import VMSTrajectoryLog
# from pymp.vms.log.subbeam import VMSTrajectoryLogSubbeam
# from pymp.vms.log.header import (VMSTrajectoryLogHeader,
#                                  VMSTrajectoryLogSubbeamHeader)
# from pymp.vms.log.definitions import (SPECIFICATION_MAP, Axis, AXIS, MLC,
#                                       AXIS_SCALE, MetaData)

from TLogParam.trajectory import VMSTrajectoryLog
from TLogParam.subbeam import VMSTrajectoryLogSubbeam
from TLogParam.header import VMSTrajectoryLogHeader, VMSTrajectoryLogSubbeamHeader, MetaData

## START: GLOBALS ##
RESOURCES_IN = 'resources'

ROOT_DIR = os.path.split(os.getcwd())[0]  # Directory of test file
RESOURCE_DIR = ROOT_DIR + os.path.sep + RESOURCES_IN + os.path.sep

# v3.0 trajectory log with associated .txt file (not truncated)
V3_BIN_FILE = RESOURCE_DIR + 'PHY25MR2_TestPlan_01_20150604142614.bin'
V3_TXT_FILE = RESOURCE_DIR + 'PHY25MR2_TestPlan_01_20150604142614.txt'
# LOGv3 = VMSTrajectoryLog(V3_BIN_FILE)

# v3.0 trajectory log with no associated .txt file (not truncated)
V3_NO_TXT_FILE = RESOURCE_DIR + 'PHY25MR2_TestPlan_02_20150604142614.bin'

# v3.0 trajectory txt file with no associated .bin file (not truncated)
V3_NO_BIN_FILE = RESOURCE_DIR + 'PHY25MR2_TestPlan_01a_20150604142614.txt'

# Uncomment for v4 testing
V4_BIN_FILE  = RESOURCE_DIR + 'PHY27MR2_TestPlan_03_20180830154128.bin'

## END: GLOBALS ##

########################################################################################################################
# START: Helper functions for checking state                                                                           #
########################################################################################################################

def bin_params_no_txt_params(tlog):
    # Overall Log
    assert type(tlog) is VMSTrajectoryLog
    assert tlog.readonly is True
    assert tlog.autoload is False

    ## Check bin parameters
    assert tlog.bin_source is None
    assert type(tlog.header) is VMSTrajectoryLogHeader

    # Check version specific items
    if tlog.header.version == 3:
        assert tlog.bin_path == V3_BIN_FILE
        assert tlog.header.metadata is None
    if tlog.header.version == 4:
        assert tlog.bin_path == V4_BIN_FILE
        assert type(tlog.header.metadata) is MetaData

    assert tlog.index_map is not None
    assert tlog.snapshots is not None
    assert tlog.recarray is not None
    assert tlog.dataframe is not None

    assert tlog.subbeams is not None
    for beam in tlog.subbeams:
        assert type(beam) is VMSTrajectoryLogSubbeam
        assert type(beam.header) is VMSTrajectoryLogSubbeamHeader

    assert tlog.crc is not None

    ## Check txt parameters
    assert tlog.txt_source is None
    assert tlog.txt_path == ''
    assert tlog.txt_properties is None

def binary_bin_params_no_txt_params(tlog):
    assert tlog.bin_source is None
    assert tlog.bin_path == ''
    assert tlog.txt_source is None
    assert tlog.txt_path == ''

    assert type(tlog.header) is VMSTrajectoryLogHeader
    if tlog.header is not None:
        if tlog.header.version == 3:
            assert tlog.header.metadata is None
        elif tlog.header.version == 4:
            assert type(tlog.header.metadata) is MetaData

    assert tlog.index_map is not None
    assert tlog.snapshots is not None
    assert tlog.recarray is not None
    assert tlog.dataframe is not None

    assert tlog.subbeams is not None
    for beam in tlog.subbeams:
        assert type(beam) is VMSTrajectoryLogSubbeam
        assert type(beam.header) is VMSTrajectoryLogSubbeamHeader

    assert tlog.txt_properties is None
    assert tlog.crc is not None
    assert tlog.readonly is True
    assert tlog.autoload is False

def bin_params_no_txt_params_autoload(tlog):
    # Overall Log
    assert type(tlog) is VMSTrajectoryLog
    assert tlog.readonly is True
    assert tlog.autoload is True

    ## Check bin parameters
    assert tlog.bin_source is None
    assert type(tlog.header) is VMSTrajectoryLogHeader

    # Check version specific items
    if tlog.header.version == 3:
        assert tlog.bin_path == V3_BIN_FILE
        assert tlog.header.metadata is None
    if tlog.header.version == 4:
        assert tlog.bin_path == V4_BIN_FILE
        assert type(tlog.header.metadata) is MetaData

    assert tlog.index_map is not None
    assert tlog.snapshots is not None
    assert tlog.recarray is not None
    assert tlog.dataframe is not None

    assert tlog.subbeams is not None
    for beam in tlog.subbeams:
        assert type(beam) is VMSTrajectoryLogSubbeam
        assert type(beam.header) is VMSTrajectoryLogSubbeamHeader

    assert tlog.crc is not None

    ## Check txt parameters
    assert tlog.txt_source is None
    assert tlog.txt_path == ''
    assert tlog.txt_properties is None

def binary_bin_params_no_txt_params_autoload(tlog):
    assert tlog.bin_source is None
    assert tlog.bin_path == ''
    assert tlog.txt_source is None
    assert tlog.txt_path == ''

    assert type(tlog.header) is VMSTrajectoryLogHeader
    if tlog.header is not None:
        if tlog.header.version == 3:
            assert tlog.header.metadata is None
        elif tlog.header.version == 4:
            assert type(tlog.header.metadata) is MetaData

    assert tlog.index_map is not None
    assert tlog.snapshots is not None
    assert tlog.recarray is not None
    assert tlog.dataframe is not None

    assert tlog.subbeams is not None
    for beam in tlog.subbeams:
        assert type(beam) is VMSTrajectoryLogSubbeam
        assert type(beam.header) is VMSTrajectoryLogSubbeamHeader

    assert tlog.txt_properties is None
    assert tlog.crc is not None
    assert tlog.readonly is True
    assert tlog.autoload is True

def bin_params_and_txt_params(tlog):
    # Overall Log
    assert type(tlog) is VMSTrajectoryLog
    assert tlog.readonly is True
    assert tlog.autoload is False

    ## Check bin parameters
    assert tlog.bin_source is None
    assert type(tlog.header) is VMSTrajectoryLogHeader

    # Check version specific items
    if tlog.header.version == 3:
        assert tlog.bin_path == V3_BIN_FILE
        assert tlog.header.metadata is None
    if tlog.header.version == 4:
        assert tlog.bin_path == V4_BIN_FILE
        assert type(tlog.header.metadata) is MetaData

    assert tlog.index_map is not None
    assert tlog.snapshots is not None
    assert tlog.recarray is not None
    assert tlog.dataframe is not None

    assert tlog.subbeams is not None
    for beam in tlog.subbeams:
        assert type(beam) is VMSTrajectoryLogSubbeam
        assert type(beam.header) is VMSTrajectoryLogSubbeamHeader

    assert tlog.crc is not None

    ## Check txt parameters
    if tlog.header.version == 3:
        assert tlog.txt_source is None
        assert tlog.txt_path == V3_TXT_FILE
        assert tlog.txt_properties is not None
    if tlog.header.version == 4:
        assert tlog.txt_source is None
        assert tlog.txt_path == ''
        assert tlog.txt_properties is None

def binary_bin_params_and_txt_params(tlog):
    assert tlog.bin_source is None
    assert tlog.bin_path == ''
    assert tlog.txt_source is None
    assert tlog.txt_path == ''

    assert type(tlog.header) is VMSTrajectoryLogHeader
    if tlog.header is not None:
        if tlog.header.version == 3:
            assert tlog.header.metadata is None
        elif tlog.header.version == 4:
            assert type(tlog.header.metadata) is MetaData

    assert tlog.index_map is not None
    assert tlog.snapshots is not None
    assert tlog.recarray is not None
    assert tlog.dataframe is not None

    assert tlog.subbeams is not None
    for beam in tlog.subbeams:
        assert type(beam) is VMSTrajectoryLogSubbeam
        assert type(beam.header) is VMSTrajectoryLogSubbeamHeader

    assert tlog.txt_properties is not None
    assert tlog.crc is not None
    assert tlog.readonly is True
    assert tlog.autoload is False

def bin_params_and_txt_params_autoload(tlog):
    # Overall Log
    assert type(tlog) is VMSTrajectoryLog
    assert tlog.readonly is True
    assert tlog.autoload is True

    ## Check bin parameters
    assert tlog.bin_source is None
    assert type(tlog.header) is VMSTrajectoryLogHeader

    # Check version specific items
    if tlog.header.version == 3:
        assert tlog.bin_path == V3_BIN_FILE
        assert tlog.header.metadata is None
    if tlog.header.version == 4:
        assert tlog.bin_path == V4_BIN_FILE
        assert type(tlog.header.metadata) is MetaData

    assert tlog.index_map is not None
    assert tlog.snapshots is not None
    assert tlog.recarray is not None
    assert tlog.dataframe is not None

    assert tlog.subbeams is not None
    for beam in tlog.subbeams:
        assert type(beam) is VMSTrajectoryLogSubbeam
        assert type(beam.header) is VMSTrajectoryLogSubbeamHeader

    assert tlog.crc is not None

    ## Check txt parameters
    if tlog.header.version == 3:
        assert tlog.txt_source is None
        assert tlog.txt_path == V3_TXT_FILE
        assert tlog.txt_properties is not None
    if tlog.header.version == 4:
        assert tlog.txt_source is None
        assert tlog.txt_path == ''
        assert tlog.txt_properties is None

def txt_params_no_bin_params(tlog, _file):
    # Overall Log
    assert type(tlog) is VMSTrajectoryLog
    assert tlog.readonly is True
    assert tlog.autoload is False

    ## Check bin parameters
    assert tlog.bin_source is None
    assert tlog.bin_path == ''
    assert tlog.header is None

    assert tlog.index_map is None
    assert tlog.snapshots is None
    assert tlog.recarray is None
    assert tlog.dataframe is None

    assert tlog.subbeams == []

    assert tlog.crc is None

    ## Check txt parameters
    assert tlog.txt_source is None
    assert tlog.txt_path == _file
    assert tlog.txt_properties is not None

def binary_txt_params_no_bin_params(tlog):
    assert tlog.bin_source is None
    assert tlog.bin_path == ''
    assert tlog.txt_source is None
    assert tlog.txt_path == ''

    assert tlog.header is None

    assert tlog.index_map is None
    assert tlog.snapshots is None
    assert tlog.recarray is None
    assert tlog.dataframe is None

    assert tlog.subbeams == []

    assert tlog.txt_properties is not None
    assert tlog.crc is None
    assert tlog.readonly is True
    assert tlog.autoload is False

def txt_params_no_bin_params_autoload(tlog, _file):
    # Overall Log
    assert type(tlog) is VMSTrajectoryLog
    assert tlog.readonly is True
    assert tlog.autoload is True

    ## Check bin parameters
    assert tlog.bin_source is None
    assert tlog.bin_path == ''
    assert tlog.header is None

    assert tlog.index_map is None
    assert tlog.snapshots is None
    assert tlog.recarray is None
    assert tlog.dataframe is None

    assert tlog.subbeams == []

    assert tlog.crc is None

    ## Check txt parameters
    assert tlog.txt_source is None
    assert tlog.txt_path == _file
    assert tlog.txt_properties is not None

def binary_txt_params_no_bin_params_autoload(tlog):
    assert tlog.bin_source is None
    assert tlog.bin_path == ''
    assert tlog.txt_source is None
    assert tlog.txt_path == ''

    assert tlog.header is None

    assert tlog.index_map is None
    assert tlog.snapshots is None
    assert tlog.recarray is None
    assert tlog.dataframe is None

    assert tlog.subbeams == []

    assert tlog.txt_properties is not None
    assert tlog.crc is None
    assert tlog.readonly is True
    assert tlog.autoload is True

########################################################################################################################
# START: Empty instantiation with  of strings to the 'bin_source' and 'text_source' parameters and autoloading         #
########################################################################################################################

def test_instantiation_empty():
    tlog = VMSTrajectoryLog()
    assert type(tlog) is VMSTrajectoryLog

def test_instantiation_empty_asign_bin_source_str():
    """
        Test assigning to the VMSTrajectoryLog.bin_source parameter a str file path pointing to a version 3 '*.bin' file
        source. This should trigger the '_parse_bin' function automatically setting all the bin related parameters on
        the object. The 'autoload' parameter in this test is False so no properties should be pulled from a '*.txt' file
        if it is present and the 'txt_path' should be an empty string.
    """
    tlog = VMSTrajectoryLog()

    tlog.bin_source = V4_BIN_FILE
    bin_params_no_txt_params(tlog)

def test_instantiation_empty_asign_bin_source_str_autoload():
    """
        Test assigning to the VMSTrajectoryLog.bin_source parameter a str file path pointing to a version 3 '*.bin' file
        source. This should trigger the '_parse_bin' function automatically setting all the bin related parameters on
        the object. The 'autoload' parameter in this test is True so the properties should be pulled from a '*.txt' file
        if it is present and the 'txt_path' should be set to its file path.
    """
    tlog = VMSTrajectoryLog(autoload=True)


    tlog.bin_source = V3_BIN_FILE
    bin_params_and_txt_params_autoload(tlog)

def test_instantiation_empty_asign_bin_source_str_missing_txt_file_autoload():
    """
        Test assigning to the VMSTrajectoryLog.bin_source parameter a str file path pointing to a version 3 '*.bin' file
        source. This should trigger the '_parse_bin' function automatically setting all the bin related parameters on
        the object. The 'autoload' parameter in this test is True however the txt file is missing so the properties will
        be missing and the 'txt_path' should remain empty..
    """
    tlog = VMSTrajectoryLog(autoload=True)

    tlog.bin_source = V4_BIN_FILE
    bin_params_no_txt_params_autoload(tlog)

########################################################################################################################
# START: Instantiation with strings assigned to the 'bin_source' and 'text_source' parameters and autoloading          #
########################################################################################################################

def test_instantiation_bin_source_str():
    """
        Test instantiating the VMSTrajectoryLog object with a str file path pointing to a version 3 '*.bin' file
        source. The 'autoload' parameter in this test is False so no properties should be pulled from a '*.txt' file if
        it is present and the 'txt_path' should be an empty string.
    """
    # Version 3 file type - TODO: Delete this section when version 3 files are no longer supported
    tlog = VMSTrajectoryLog(bin_source=os.path.abspath(V3_BIN_FILE))
    bin_params_no_txt_params(tlog)

    # Version 4 file type
    tlog = VMSTrajectoryLog(bin_source=os.path.abspath(V4_BIN_FILE))
    bin_params_no_txt_params(tlog)

def test_instantiation_bin_source_str_autoload():
    """
        Test instantiating the VMSTrajectoryLog object with a str file path pointing to a version 3 '*.bin' file
        source. The 'autoload' parameter in this test is True so properties should be pulled from a '*.txt' file and
        the 'txt_path' should be set to the '*.txt' file's absolute file path if located int he same directory.
    """
    # TODO: Delete when version 3 files are no longer supported
    tlog = VMSTrajectoryLog(bin_source=os.path.abspath(V3_BIN_FILE), autoload=True)
    bin_params_and_txt_params_autoload(tlog)

def test_instantiation_bin_source_str_missing_txt_file_autoload():
    """
        Test instantiating the VMSTrajectoryLog object with a str file path pointing to a version 3 '*.bin' file
        source. The 'autoload' parameter in this test is True but the '*.txt' file is missing so no properties should be
        pulled from a '*.txt' file and the 'txt_path' should be an empty string.
    """
    tlog = VMSTrajectoryLog(bin_source=os.path.abspath(V4_BIN_FILE), autoload=True)
    bin_params_no_txt_params_autoload(tlog)

def test_instantiation_txt_source_str():
    """
        Test instantiating the VMSTrajectoryLog object with a str file path pointing to a version 3 '*.txt' file
        source. The 'autoload' parameter in this test is False so the VMSTrajectoryLog object should only have
        properties in the 'txt_properties' parameter and the 'txt_path' should be set to the supplied path. All other
        log parameters should be empty or None.
    """
    # TODO: Delete when version 3 files are no longer supported
    tlog = VMSTrajectoryLog(txt_source=os.path.abspath(V3_TXT_FILE))
    txt_params_no_bin_params(tlog, V3_TXT_FILE)

def test_instantiation_txt_source_str_autoload():
    """
        Test instantiating the VMSTrajectoryLog object with a str file path pointing to a version 3 '*.txt' file
        source. The 'autoload' parameter in this test is True so all other VMSTrajectoryLog parameters should populate
        using the associated '*.bin' file if located in the same directory.
    """
    # TODO: Delete when version 3 files are no longer supported
    tlog = VMSTrajectoryLog(txt_source=os.path.abspath(V3_TXT_FILE), autoload=True)
    bin_params_and_txt_params_autoload(tlog)

def test_instantiation_txt_source_str_missing_bin_file_autoload():
    """
        Test instantiating the VMSTrajectoryLog object with a str file path pointing to a version 3 '*.txt' file
        source. The 'autoload' parameter in this test is True however, the '*.bin' file is missing so the resulting
        VMSTrajectoryLog object should only have properties in the 'txt_properties' parameter and the 'txt_path' should
        be set to the supplied path. All other log parameters should be empty or None.
    """
    # TODO: Delete when version 3 files are no longer supported
    tlog = VMSTrajectoryLog(txt_source=os.path.abspath(V3_NO_BIN_FILE), autoload=True)
    txt_params_no_bin_params_autoload(tlog, V3_NO_BIN_FILE)

def test_instantiation_bin_source_str_and_txt_source_str():
    """
        Test instantiating the VMSTrajectoryLog object with a str file path pointing to a version 3 '*.bin' file
        source and a str file path pointing to a version 3 '*.txt' file source. The 'autoload' parameter in this test is
        False. Properties should still be pulled from the '*.txt' file and the 'txt_path' should be set to the '*.txt'
        file path provided.
    """
    # TODO: Delete when version 3 files are no longer supported
    tlog = VMSTrajectoryLog(bin_source=os.path.abspath(V3_BIN_FILE),
                            txt_source=os.path.abspath(V3_TXT_FILE),
                            )

    bin_params_and_txt_params(tlog)

def test_instantiation_bin_source_str_and_txt_source_str_autoload():
    """
        Test instantiating the VMSTrajectoryLog object with a str file path pointing to a version 3 '*.bin' file
        source and a str file path pointing to a version 3 '*.txt' file source. The 'autoload' parameter in this test is
        True however the VMSTrajectoryLog __init__ method should detect this and set it to False (see docuentation on
        why). Properties should still be pulled from the '*.txt' file and the 'txt_path' should be set to the '*.txt'
        file path provided.
    """
    # TODO: Delete when version 3 files are no longer supported
    tlog = VMSTrajectoryLog(bin_source=os.path.abspath(V3_BIN_FILE),
                            txt_source=os.path.abspath(V3_TXT_FILE),
                            autoload=True # Should be set to False in __init__
                            )
    bin_params_and_txt_params(tlog)

########################################################################################################################
# START: Tests with assignment of file like objects to the 'bin_source' and 'text_source' parameters and autoloading   #
########################################################################################################################

def test_instantiation_bin_source_file():
    """
        Test instantiating the VMSTrajectoryLog object with a file like object representing a version 3 '*.bin' file
        source. The 'autoload' parameter in this test is False so no properties should be pulled from a '*.txt' file if
        it is present and the 'txt_path' should be an empty string. The 'bin_path' should be set to the correct file
        path used to open the file like object.
    """
    # Version 3 file type - TODO: Delete this section when version 3 files are no longer supported
    _file = open(os.path.abspath(V3_BIN_FILE), 'rb')
    tlog = VMSTrajectoryLog(bin_source=_file)
    bin_params_no_txt_params(tlog)

    # Version 4 file type
    _file = open(os.path.abspath(V4_BIN_FILE), 'rb')
    tlog = VMSTrajectoryLog(bin_source=_file)
    bin_params_no_txt_params(tlog)

def test_instantiation_bin_source_file_autoload():
    """
        Test instantiating the VMSTrajectoryLog object with a file like object representing a version 3 '*.bin' file
        source. The 'autoload' parameter in this test is True so properties should be pulled from a '*.txt' file and
        the 'txt_path' should be set to the '*.txt' file's absolute file path if located in the same directory. The
        'bin_path' should be set to the correct file path used to open the file like object.
    """
    # TODO: Delete when version 3 files are no longer supported
    _file = open(os.path.abspath(V3_BIN_FILE), 'rb')
    tlog = VMSTrajectoryLog(bin_source=_file, autoload=True)
    bin_params_and_txt_params_autoload(tlog)

def test_instantiation_bin_source_file_missing_txt_file_autoload():
    """
        Test instantiating the VMSTrajectoryLog object with a file like object representing a version 3 '*.bin' file
        source. The 'autoload' parameter in this test is True but the '*.txt' file is missing so no properties should be
        pulled from a '*.txt' file and the 'txt_path' should be an empty string. The 'bin_path' should be set to the
        correct file path used to open the file like object.
    """
    _file = open(os.path.abspath(V4_BIN_FILE), 'rb')
    tlog = VMSTrajectoryLog(bin_source=_file, autoload=True)
    bin_params_no_txt_params_autoload(tlog)

def test_instantiation_txt_source_file():
    """
        Test instantiating the VMSTrajectoryLog object with a file like object representing a version 3 '*.txt' file
        source. The 'autoload' parameter in this test is False so the VMSTrajectoryLog object should only have
        properties in the 'txt_properties' parameter and the 'txt_path' should be set to the file path. All other
        log parameters should be empty or None.
    """
    # TODO: Delete when version 3 files are no longer supported
    _file = open(os.path.abspath(V3_TXT_FILE), 'rb')
    tlog = VMSTrajectoryLog(txt_source=_file)
    txt_params_no_bin_params(tlog, V3_TXT_FILE)

def test_instantiation_txt_source_file_autoload():
    """
        Test instantiating the VMSTrajectoryLog object with a file like object representing a version 3 '*.txt' file
        source. The 'autoload' parameter in this test is True so all other VMSTrajectoryLog parameters should populate
        using the associated '*.bin' file if located in the same directory.
    """
    # TODO: Delete when version 3 files are no longer supported
    _file = open(os.path.abspath(V3_TXT_FILE), 'rb')
    tlog = VMSTrajectoryLog(txt_source=_file, autoload=True)
    bin_params_and_txt_params_autoload(tlog)

def test_instantiation_txt_source_file_missing_bin_file_autoload():
    """
        Test instantiating the VMSTrajectoryLog object with a file like object representing a version 3 '*.txt' file
        source. The 'autoload' parameter in this test is True however, the '*.bin' file is missing so the resulting
        VMSTrajectoryLog object should only have properties in the 'txt_properties' parameter and the 'txt_path' should
        be set to the path of the file like object. All other log parameters should be empty or None.
    """
    # TODO: Delete when version 3 files are no longer supported
    _file = open(os.path.abspath(V3_NO_BIN_FILE), 'rb')
    tlog = VMSTrajectoryLog(txt_source=_file, autoload=True)
    txt_params_no_bin_params_autoload(tlog, V3_NO_BIN_FILE)

def test_instantiation_bin_source_file_and_txt_source_file():
    """
        Test instantiating the VMSTrajectoryLog object with a file like object representing a version 3 '*.bin' file
        source and a file like object representing a version 3 '*.txt' file source. The 'autoload' parameter in this
        test is False. Properties should still be pulled from the '*.txt' file provided. The 'txt_path' and 'bin_path'
        parameters should be set to the file paths associated with the respective file like objects provided.
    """
    # TODO: Delete when version 3 files are no longer supported
    bin_file = open(os.path.abspath(V3_BIN_FILE), 'rb')
    txt_file = open(os.path.abspath(V3_TXT_FILE), 'rb')

    tlog = VMSTrajectoryLog(bin_source=bin_file, txt_source=txt_file)
    bin_params_and_txt_params(tlog)

def test_instantiation_bin_source_file_and_txt_source_file_autoload():
    """
        Test instantiating the VMSTrajectoryLog object with a file like object representing a version 3 '*.bin' file
        source and a file like object representing a version 3 '*.txt' file source. The 'autoload' parameter in this
        test is True however the VMSTrajectoryLog __init__ method should detect this and set it to False (see
        docuentation on why). Properties should still be pulled from the '*.txt' file provided. The 'txt_path' and
        'bin_path' parameters should be set to the file paths associated with the respective file like objects provided.
    """
    # TODO: Delete when version 3 files are no longer supported
    bin_file = open(os.path.abspath(V3_BIN_FILE), 'rb')
    txt_file = open(os.path.abspath(V3_NO_BIN_FILE), 'rb')

    tlog = VMSTrajectoryLog(bin_source=bin_file, txt_source=txt_file,
                            autoload=True # Should be set to False in __init__
                            )
    bin_params_and_txt_params(tlog)

########################################################################################################################
# START: Tests with assignment of binary blobs to the 'bin_source' and 'text_source' parameters and autoloading        #
########################################################################################################################

def test_instantiation_bin_source_binary():
    """
        Test instantiating the VMSTrajectoryLog object with a binary blob representing a version 3 '*.bin' file source.
        The 'autoload' parameter in this test is False so no properties should be pulled from a '*.txt' file if it is
        present and the 'txt_path' should be an empty string. The 'bin_path' should also be an empty string since there
        is no way to determine the file path where the binary blob was obtained.
    """
    # Version 3 file type - TODO: Delete this section when version 3 files are no longer supported
    _file = open(os.path.abspath(V3_BIN_FILE), 'rb').read()
    tlog = VMSTrajectoryLog(bin_source=_file)
    binary_bin_params_no_txt_params(tlog)

    # Version 4 file type
    _file = open(os.path.abspath(V4_BIN_FILE), 'rb').read()
    tlog = VMSTrajectoryLog(bin_source=_file)
    binary_bin_params_no_txt_params(tlog)

def test_instantiation_bin_source_binary_autoload():
    """
        Test instantiating the VMSTrajectoryLog object with a binary blob representing a version 3 '*.bin' file source.
        The 'autoload' parameter in this test is True however no properties should be pulled from a '*.txt' file and
        the 'txt_path' should be set to an empty string since there is no way to determine the '*.txt' file from the
        information in the binary blob provided. The 'bin_path' should also be an empty string since there is no way to
        determine the file path where the binary blob was obtained.
    """
    # TODO: Delete when version 3 files are no longer supported
    _file = open(os.path.abspath(V3_BIN_FILE), 'rb').read()
    tlog = VMSTrajectoryLog(bin_source=_file, autoload=True)
    binary_bin_params_no_txt_params_autoload(tlog)

def test_instantiation_txt_source_binary():
    """
        Test instantiating the VMSTrajectoryLog object with a binary blob representing a version 3 '*.txt' file source.
        The 'autoload' parameter in this test is False so the VMSTrajectoryLog object should only have properties in the
        'txt_properties' parameter. The 'txt_path' should be set to an empty string because there is no way to determine
        the file path from the binary blob provided. All other log parameters should be empty or None.
    """
    # TODO: Delete this section when version 3 files are no longer supported
    _file = open(os.path.abspath(V3_TXT_FILE), 'rb').read()
    tlog = VMSTrajectoryLog(txt_source=_file)
    binary_txt_params_no_bin_params(tlog)

def test_instantiation_txt_source_binary_autoload():
    """
        Test instantiating the VMSTrajectoryLog object with a binary blob representing a version 3 '*.txt' file source.
        The 'autoload' parameter in this test is True however all other VMSTrajectoryLog parameters should remain empty
        because there is no way to determine the location of the '*.bin' file source from the binary blob provided.
    """
    # TODO: Delete when version 3 files are no longer supported
    _file = open(os.path.abspath(V3_TXT_FILE), 'rb').read()
    tlog = VMSTrajectoryLog(txt_source=_file, autoload=True)
    binary_txt_params_no_bin_params_autoload(tlog)

def test_instantiation_bin_source_binary_and_txt_source_binary():
    """
        Test instantiating the VMSTrajectoryLog object with a binary blob representing a version 3 '*.bin' file source
        and a bonary blob representing a version 3 '*.txt' file source. The 'autoload' parameter in this test is False.
        Properties should still be pulled from the '*.txt' file however the 'txt_path' and 'bin_path' parameters should
        be set to empty strings since there is no way to tell where the binary blobs came from.
    """
    # TODO: Delete when version 3 files are no longer supported
    bin_file = open(os.path.abspath(V3_BIN_FILE), 'rb').read()
    txt_file = open(os.path.abspath(V3_TXT_FILE), 'rb').read()
    tlog = VMSTrajectoryLog(bin_source=bin_file, txt_source=txt_file)
    binary_bin_params_and_txt_params(tlog)

def test_instantiation_bin_source_binary_and_txt_source_binary_autoload():
    """
        Test instantiating the VMSTrajectoryLog object with a binary blob representing a version 3 '*.bin' file source
        and a binary blob representing a version 3 '*.txt' file source. The 'autoload' parameter in this test is True
        however the VMSTrajectoryLog __init__ method should detect this and set it to False (see docuentation on why).
        Properties should still be pulled from the '*.txt' file hoever the 'txt_path' and 'bin_path' parameters should
        be set to empty strings since there is no way to tell where the binary blobs came from.
    """
    # TODO: Delete when version 3 files are no longer supported
    bin_file = open(os.path.abspath(V3_BIN_FILE), 'rb').read()
    txt_file = open(os.path.abspath(V3_NO_BIN_FILE), 'rb').read()
    tlog = VMSTrajectoryLog(bin_source=bin_file, txt_source=txt_file,
                            autoload=True # Should be set to False in __init__
                            )
    binary_bin_params_and_txt_params(tlog)

########################################################################################################################
# START: Log feature checks                                                                                            #
########################################################################################################################

def test_readonly():
    """
        Tests editign values in place when manipulating the 'readonly' parameter.
    """

    tlog = VMSTrajectoryLog(bin_source=os.path.abspath(V3_BIN_FILE))

    # The 'readonly' parameter is True by default. This should raise a ValueError: assignment destination is read-only
    with pytest.raises(ValueError):
        tlog.snapshots[::, 0] = 9999

    # By setting the 'readonly' parameter to 'False' you should now be able to write to the array values
    tlog = VMSTrajectoryLog(bin_source=os.path.abspath(V3_BIN_FILE), readonly=False)
    tlog.snapshots[::, 0] = 9999

def test_data_views():
    """
        Tests to make sure the 'snapshots', 'recarray' and 'dataframe' parameters are just views of the same data in
        memory.
    """
    # By setting the 'readonly' parameter to 'False' you should now be able to write to the array values
    tlog = VMSTrajectoryLog(bin_source=os.path.abspath(V3_BIN_FILE), readonly=False)
    tlog.snapshots[::, 0] = 9999

    # Check master dataframe view
    assert np.all(tlog.dataframe.CollRtn.expected.values == 9999)

    # Check master recarray view
    assert np.all(tlog.recarray['CollRtn']['expected'] == 9999)

    # Check the views for each subbeam
    for beam in tlog.subbeams:
        assert np.all(beam.snapshots[::,0] == 9999)                     # snapshots view
        assert np.all(beam.dataframe.CollRtn.expected.values == 9999)   # dataframe view
        assert np.all(beam.recarray['CollRtn']['expected'] == 9999)     # recarray view 

########################################################################################################################
# START: Log feature checks                                                                                            #
########################################################################################################################
########################################################################################################################
# START: Log feature checks                                                                                            #
########################################################################################################################
########################################################################################################################
# START: Log feature checks                                                                                            #
########################################################################################################################
########################################################################################################################
# START: Log feature checks                                                                                            #
########################################################################################################################

# def test_resource_version_compatibility():
#     ''' Test to make sure the sample files are of equal or lesser version to the
#         VMSTrajectoryLog pakage to ensure support prior to testing.
#     '''
#
#     # Check and make sure the version is in the SPECIFICATION_MAP indicating
#     # support for this version. Then verify the version of the file is at or
#     # below the version package. Package version will mimic the Varian file
#     # version for clarity.
#
#     # v3.0 Test
#     assert float(LOGv3.header.version) == 3.0
#     assert float(LOGv3.header.version) in SPECIFICATION_MAP
#     assert float(LOGv3.header.version) <= float(tlog.__version__)
#
#     # v4.0 Test
#     assert float(LOGv4_NO_TXT.header.version) == 4.0
#     assert float(LOGv4_NO_TXT.header.version) in SPECIFICATION_MAP
#     assert float(LOGv4_NO_TXT.header.version) <= float(tlog.__version__)