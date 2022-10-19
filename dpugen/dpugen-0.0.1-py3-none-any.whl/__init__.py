from __future__ import unicode_literals
import logging

# Logging configuration
log = logging.getLogger(__name__)  # noqa
log.addHandler(logging.NullHandler())  # noqa

import sys

__version__ = "0.0.1"
PY_MAJ_VER = 3
PY_MIN_VER = 8
MIN_PYTHON_VER = "3.8"


# Make sure user is using a valid Python version (for DpuGen)
def check_python_version():  # type: ignore
    python_snake = "\U0001F40D"

    # Use old-school .format() method in case someone tries to use DpuGen with very old Python
    msg = """DpuGen Version {net_ver} requires Python Version {py_ver} or higher.""".format(net_ver=__version__, py_ver=MIN_PYTHON_VER)
    if sys.version_info.major != PY_MAJ_VER:
        raise ValueError(msg)
    elif sys.version_info.minor < PY_MIN_VER:
        # Why not :-)
        msg = msg.rstrip() + " {snake}\n\n".format(snake=python_snake)
        raise ValueError(msg)


check_python_version()  # type: ignore



from dpugen.confbase import ConfBase

__all__ = (
    "ConfBase",
)
