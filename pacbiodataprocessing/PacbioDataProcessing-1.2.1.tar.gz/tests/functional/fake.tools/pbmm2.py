#!/usr/bin/env python

#######################################################################
#
# Copyright (C) 2022 David Palao
#
# This file is part of PacBioDataProcessing.
#
#  PacBioDataProcessing is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  PacBio data processing is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with PacBioDataProcessing. If not, see <http://www.gnu.org/licenses/>.
#
#######################################################################

"""Template to create a fake version of 'pbmm2'.
"""

import sys
import shutil
from pathlib import Path, PosixPath  # noqa: F401
import time
from concurrent.futures import ProcessPoolExecutor
import os


datadir = _DATA_DIR_  # noqa: F821

files = {
    ('ccs.pbmm2.11mols.bam', '11mols.fasta'): datadir/'pbmm2.ccs.11mols.bam',
    ('ccs.blasr.11mols.bam', '11mols.fasta'): datadir/'pbmm2.ccs.11mols.bam',
    ('baseline.bam', '11mols.fasta'): datadir/'pbmm2.baseline.bam',
    ('baseline.bam', 'pi-shifted.11mols.fasta'): (
        datadir/'pi-shifted.pbmm2.baseline.bam'),
    ('ccs.baseline.bam', '11mols.fasta'): datadir/'pbmm2.ccs.baseline.bam',
    ('ccs.baseline.bam', 'pi-shifted.11mols.fasta'):
    datadir/'pi-shifted.pbmm2.ccs.baseline.bam',
    ('ccs.pbmm2.8mols.bam', 'pMA685.fa'): datadir/'pbmm2.ccs.pbmm2.8mols.bam',
    ('ccs.blasr.8mols.bam', 'pMA685.fa'): datadir/'pbmm2.ccs.pbmm2.8mols.bam',
    ('ccs.pbmm2.12mols.bam', '11mols.fasta'): (
        datadir/'pbmm2.ccs.pbmm2.12mols.bam'),
    ('ccs.blasr.12mols.bam', '11mols.fasta'): (
        datadir/'pbmm2.ccs.pbmm2.12mols.bam'),
    ('ccs.9mols.bam', 'pMA685.fa'): datadir/'pbmm2.ccs.9mols.bam',
    ('9mols.bam', 'pMA685.fa'): datadir/'pbmm2.9mols.bam',
    ('ccs.9mols.bam', 'pi-shifted.pMA685.fa'): (
        datadir/'pi-shifted.pbmm2.ccs.9mols.bam'),
    ('9mols.bam', 'pi-shifted.pMA685.fa'): (
        datadir/'pi-shifted.pbmm2.9mols.bam'),
    ('ccs.11mols.bam', 'pi-shifted.11mols.fasta'): (
        datadir/'pi-shifted.pbmm2.ccs.11mols.bam'),
}


def heavy_lifting():
    # To allow the FTs to detect the processes:
    # the sleep time must be >~ 0.2 to allow the process hunter function
    # "count_nprocs" to have a chance to find this process:
    pid = os.getpid()
    markerfile = Path(f".pbmm2.pid.{pid}")
    markerfile.touch()
    time.sleep(0.3)


def main(nprocs):
    if nprocs == 1:
        heavy_lifting()
    else:
        with ProcessPoolExecutor(max_workers=nprocs) as executor:
            for i in range(nprocs):
                executor.submit(heavy_lifting)


if __name__ == "__main__":
    inbam = Path(sys.argv[3])
    assert inbam.is_file()
    fasta = Path(sys.argv[2])
    # Trying 10 times to find the file, just in case (sometimes the timing
    # in the FTs is difficult):
    for i in range(10):
        if fasta.is_file():
            break
        time.sleep(0.1)
    else:
        assert fasta.is_file(), (
            f"Fasta file cannot be used: '{fasta}' (exists: {fasta.exists()})"
        )
    assert sys.argv[1] == "align"
    src = files[(inbam.name, fasta.name)]
    dst = sys.argv[-1]
    main(nprocs=1)
    shutil.copyfile(src, dst)
