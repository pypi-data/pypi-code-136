# SPDX-License-Identifier: GPL-2.0-or-later OR AGPL-3.0-or-later OR CERN-OHL-S-2.0+
import os, site
from pathlib import Path

from doit import get_var

import pdkmaster


### Config


DOIT_CONFIG = {
    "default_tasks": ["install"],
}


### support functions


def get_var_env(name, default=None):
    """Uses get_var to get a command line variable, also checks
    environment variables for default value

    If os.environ[name.upper()] exists that value will override the
    default value given.
    """
    try:
        default = os.environ[name.upper()]
    except:
        # Keep the specified default
        pass
    return get_var(name, default=default)


### globals


pip = get_var_env("pip", default="pip")
python = get_var_env("python", default="python")

top_dir = Path(__file__).parent

c4m_local_dir = top_dir.joinpath("c4m")
c4m_py_files = tuple(c4m_local_dir.rglob("*.py"))

pdkmaster_inst_dir = Path(pdkmaster.__file__).parent
# Don't use local module for c4m
c4m_inst_dir = Path(site.getsitepackages()[0]).joinpath("c4m")
flexio_inst_dir = c4m_inst_dir.joinpath("flexio")
flexio_local_dir = top_dir.joinpath("c4m")
dist_dir = top_dir.joinpath("dist")

flexio_py_files = tuple(flexio_local_dir.rglob("*.py"))


### main tasks


#
# dist
def task_dist():
    """Create distributable python module"""

    return {
        "title": lambda _: "Creating wheel",
        "file_dep": (top_dir.joinpath("setup.py"), *flexio_py_files),
        "targets": (dist_dir,),
        "actions": (f"{python} -m build",)
    }


#
# install
def task_install():
    """Install the python module"""

    return {
        "title": lambda _: "Installing python module",
        "file_dep": c4m_py_files,
        "targets": (flexio_inst_dir,),
        "actions": (
            f"{pip} install {top_dir}",
        ),
    }
