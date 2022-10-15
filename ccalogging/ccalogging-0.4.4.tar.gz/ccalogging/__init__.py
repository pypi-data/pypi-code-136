#
# Copyright (c) 2018, Chris Allison
#
#     This file is part of ccalogging.
#
#     ccalogging is free software: you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation, either version 3 of the License, or
#     (at your option) any later version.
#
#     ccalogging is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.
#
#     You should have received a copy of the GNU General Public License
#     along with ccalogging.  If not, see <http://www.gnu.org/licenses/>.
#
"""python module for easy logging"""
from datetime import date, timedelta
import gzip
import logging
import os
import shutil
import sys


def setDebug():
    log.setLevel(logging.DEBUG)


def setInfo():
    log.setLevel(logging.INFO)


def setWarn():
    log.setLevel(logging.WARNING)


def setError():
    log.setLevel(logging.ERROR)


def setLogFile(
    fqfn,
    fformat="%(asctime)s [%(levelname)-5.5s]  %(message)s",
    datefmt="%d/%m/%Y %H:%M:%S",
    rotation=None,
):
    """
    sets log output to go to a file

    rotation argument if present, will cause the file to be rotated
    keeping the number of days specified in the argument
    """
    if rotation:
        doRotation(fqfn, rotation)
    ffmt = logging.Formatter(fformat, datefmt=datefmt)
    fileH = logging.FileHandler(fqfn)
    fileH.setFormatter(ffmt)
    log.addHandler(fileH)


def setConsoleOut(
    STDOUT=False,
    cformat="%(asctime)s [%(levelname)-5.5s]  %(message)s",
    datefmt="%d/%m/%Y %H:%M:%S",
):
    """
    sets log output to goto the console (stderr by default)
    """
    cfmt = logging.Formatter(cformat, datefmt=datefmt)
    if STDOUT:
        consH = logging.StreamHandler(sys.stdout)
    else:
        consH = logging.StreamHandler(sys.stderr)
    consH.setFormatter(cfmt)
    log.addHandler(consH)


def doRotation(fqfn, rotation):
    mtime = os.path.getmtime(fqfn)
    fdate = date.fromtimestamp(mtime)
    xdate = date.today()
    # rotate if existing log file is older than one day
    if fdate.day != xdate.day:
        home = os.path.expanduser("~/")
        logd = os.path.join(home, "log")
        based = logd if os.path.dirname(fqfn) == "" else os.path.dirname(fqfn)
        basefn = os.path.basename(fqfn)
        while rotation > 0:
            rotateNext(based, basefn, rotation)
            rotation -= 1
        # rotation should now be 0
        # all files will have 'moved up' by one
        # leaving {fqfn}.1.gz not existing
        # copy the fqfn file to {fqfn}.1.gz
        # compressing on the way through
        with open(fqfn, "rb") as ifn:
            with gzip.open(f"{fqfn}.1.gz", "wb") as ofn:
                shutil.copyfileobj(ifn, ofn)
        # now truncate the {fqfn} file
        with open(fqfn, "w") as ifn:
            pass


def rotateNext(logd, basefn, xnext):
    srcfn = os.path.join(logd, f"{basefn}.{xnext}.gz")
    if os.path.exists(srcfn):
        xnext = xnext + 1
        destfn = os.path.join(logd, f"{basefn}.{xnext}.gz")
        if os.path.exists(destfn):
            os.unlink(destfn)
        os.rename(srcfn, destfn)


log = logging.getLogger("ccalogging")
majorv = 0
minorv = 4
buildv = 4
__version__ = str(majorv) + "." + str(minorv) + "." + str(buildv)
__version_info__ = [majorv, minorv, buildv]
