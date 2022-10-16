"""Python3 interface with [Picard Tools](https://broadinstitute.github.io/picard/)
from Broad institute.

Classes
-------
MarkDuplicates
    wrapper for picard's MarkDuplicates, compatable with seqalign
"""

from picardtools.env import JAR
from picardtools.picardtools import MarkDuplicates
