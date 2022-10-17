

""""""# start delvewheel patch
def _delvewheel_init_patch_1_1_0():
    import os
    libs_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, 'shapely.libs'))
    os.add_dll_directory(libs_dir)


_delvewheel_init_patch_1_1_0()
del _delvewheel_init_patch_1_1_0
# end delvewheel patch

from .lib import GEOSException  # NOQA
from .lib import Geometry  # NOQA
from .lib import geos_version, geos_version_string  # NOQA
from .lib import geos_capi_version, geos_capi_version_string  # NOQA
from .errors import setup_signal_checks  # NOQA
from ._geometry import *  # NOQA
from .creation import *  # NOQA
from .constructive import *  # NOQA
from .predicates import *  # NOQA
from .measurement import *  # NOQA
from .set_operations import *  # NOQA
from .linear import *  # NOQA
from .coordinates import *  # NOQA
from .strtree import *  # NOQA
from .io import *  # NOQA

# Submodule always needs to be imported to ensure Geometry subclasses are registered
from shapely.geometry import (  # NOQA
    Point,
    LineString,
    Polygon,
    MultiPoint,
    MultiLineString,
    MultiPolygon,
    GeometryCollection,
    LinearRing,
)

from ._version import get_versions

__version__ = get_versions()["version"]
del get_versions

setup_signal_checks()
