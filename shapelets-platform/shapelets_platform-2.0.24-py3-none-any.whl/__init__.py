# Copyright (c) 2022 Shapelets.io
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from __future__ import annotations


from ._version import version as __version__
# from . import relations
from . import data 

from .shapelets import (
    Shapelets,
    init_session,
    close_session,
    start_shapelet_processes,
    stop_shapelet_processes,
    update_password
)

from . import uom
from .uom import *

from . import dsl
from . import model
from . import services

from . import svr

__all__ = ["__version__", "svr", "data"]
__all__ += uom.__all__
