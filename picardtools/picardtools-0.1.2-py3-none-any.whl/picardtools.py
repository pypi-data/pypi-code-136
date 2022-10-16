#!/usr/bin/env python3
#===============================================================================
# picardtools.py
#===============================================================================

# Imports ======================================================================

import os
import os.path
import subprocess
import tempfile

from math import floor

from picardtools.env import JAR




# Classes ======================================================================

class MarkDuplicates():
    """Remove duplicates with Picard's MarkDuplicates
    
    Attributes
    ----------
    jar : str
        path to the picard.jar file
    memory_gb : float
        max memory usage in gigabytes
    assume_sorted : bool
        if true, assume the BAM file is sorted
    metrics_file
        file object to which metrics will be written
    remove_duplicates : bool
        if false, mark duplicates but do not remove them
    validation_stringency : str
        validation stringency setting for picard MarkDuplicates
    """
    
    def __init__(
        self,
        jar=JAR,
        memory_gb=1,
        assume_sorted=False,
        metrics_file=os.devnull,
        remove_duplicates=True,
        validation_stringency='LENIENT',
        temp_dir=tempfile.gettempdir()
    ):
        """Collect parameter settings

        Parameters
        ----------
        jar : str
            path to the picard.jar file
        memory_gb : float
            max memory usage in gigabytes
        assume_sorted : bool
            if true, assume the BAM file is sorted
        metrics_file
            file object to which metrics will be written
        remove_duplicates : bool
            if false, mark duplicates but do not remove them
        validation_stringency : str
            validation stringency setting for picard MarkDuplicates
        """

        self.jar = jar
        self.memory_gb = floor(memory_gb)
        self.assume_sorted = assume_sorted
        self.metrics_file = metrics_file
        self.remove_duplicates = remove_duplicates
        self.validation_stringency = validation_stringency
        self.temp_dir = temp_dir
    
    def __call__(self, bam, log=None):
        """De-duplicate the input BAM file

        Parameters
        ----------
        bam : bytes
            the BAM file
        log
            file object to which stderr will be written
        """

        with tempfile.NamedTemporaryFile(dir=self.temp_dir) as temp_bam:
            temp_bam.write(bam)
            with subprocess.Popen(
                (
                    'java',
                    '-Xmx{}G'.format(self.memory_gb),
                    '-jar', self.jar, 'MarkDuplicates',
                    'INPUT={}'.format(temp_bam.name),
                    'OUTPUT=/dev/stdout',
                    'QUIET=true',
                    'ASSUME_SORTED={}'.format(
                        'true' if self.assume_sorted else 'false'
                    ),
                    'METRICS_FILE={}'.format(self.metrics_file),
                    'REMOVE_DUPLICATES={}'.format(
                        'true' if self.remove_duplicates else 'false'
                    ),
                    'VALIDATION_STRINGENCY={}'.format(
                        self.validation_stringency
                    ),
                    'TMP_DIR={}'.format(self.temp_dir)
                ),
                stdout=subprocess.PIPE,
                stderr=log
            ) as mark_duplicates:
                return mark_duplicates.communicate()[0]
