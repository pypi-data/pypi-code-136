# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['pygeofun']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'pygeofun',
    'version': '0.0.8',
    'description': 'Geographic Functions: geodesics and rhumblines, orthodromes and loxodromes',
    'long_description': "GeoFun\n======\n\nLibrary for doing geographic calculations like distance, azimuth and\nposition determination for geodesics and rhumb lines, orthodromes and\nloxodromes, respectively.\n\nThis version makes use of GeographicLib for doing most of the\ncalculations.\n\nThis is a C++ package that uses pybind11 to wrap the C++ version of\nGeographicLib, which makes it faster (~100x) than the pure python\nversion of\n`geographiclib <https://geographiclib.sourceforge.io/html/python/index.html>`__.\n\nCompare:\n\n.. code:: python\n\n   In [1]: from geofun import geodesic_inverse\n\n   In [2]: %timeit geodesic_inverse(52, 4, 28, -16.6)\n   1.17 µs ± 37 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)\n\n   In [3]: from geographiclib.geodesic import Geodesic\n\n   In [4]: %timeit Geodesic.WGS84.Inverse(52, 4, 28, -16.6)\n   107 µs ± 170 ns per loop (mean ± std. dev. of 7 runs, 10000 loops each)\n\n   In [5]: geodesic_inverse(52, 4, 28, -16.6)\n   Out[5]: (-139.28471885516532, 3168557.154495447, -152.90624110350674)\n\n   In [6]: Geodesic.WGS84.Inverse(52, 4, 28, -16.6)\n   Out[6]:\n   {'lat1': 52,\n    'lon1': 4.0,\n    'lat2': 28,\n    'lon2': -16.6,\n    'a12': 28.519118381735783,\n    's12': 3168557.1544954455,\n    'azi1': -139.28471885516532,\n    'azi2': -152.90624110350674}\n\nBuilding\n--------\n\n-  Get\n   `poetry <https://python-poetry.org/docs/master/#installing-with-the-official-installer>`__\n   if you don't have it\n\n-  Check out the source code:\n   ``git clone https://github.com/jrversteegh/geofun.git --recurse-submodules``\n\n-  Execute ``poetry build`` to build the package or ``poetry install``\n   to get a virtual environment to work in. Both require a working\n   modern C++ compiler. GCC 9.4 and MSVC 14.3 were tested. Others may\n   work.\n\nExamples\n--------\n\nSome operator abuse was used to mark the difference between geodesic and\nmercator based operations. ``+`` and ``-`` are addition and subtraction\nin the mercator projection (loxodromes) and ``*`` and ``/`` are addition\nand subtraction on geodesics (orthodromes). If you object to this,\nyou’re probably right. Any suggestions for a better way are quite\nwelcome.\n\n.. code:: python\n\n   from geofun import Position, Vector\n\n   # Just off Hoek van Holland\n   org = Position(52.0, 4.0)\n   nm95 = 95 * 1852.0\n\n   # Go west 95 nm to Felixstowe\n   rmbv = Vector(270.0, nm95)\n   pos1 = org + rmbv\n\n   # Go to the same point using great circle line\n   gcv = pos1 / org\n   pos2 = org * gcv\n\n   # We should end up at the same location\n   assert pos1 == pos2\n\n   # How disappointing: we managed to gain just 9m by crossing the\n   # North sea using a great circle :p\n   assert nm95 - gcv.length == 9.101067085022805, f'Unexpected: {gcv.length}'\n\n   print(f'From {org} to {pos1}')\n   print(f'Rhumb: {rmbv}')\n   print(f'Great circle: {gcv}')\n\n   # Another verification\n   assert pos1 - org == rmbv\n   assert pos1 / org == gcv\n\nClasses\n-------\n\n**Position**\n  - latitude\n  - longitude\n\n``Position(latitude: int, longitude: int) -> Position`` Position in arc seconds.\n\n``Position(latitude: float, longitude: float) -> Position`` Position in arc degrees.\n\n**Vector**\n  - azimuth \n  - length\n\n``Vector(azimuth: float, length: float) -> Vector`` Polar vector in arc degrees and meters.\n\n**Point**\n  - x \n  - y\n\n``Point(x: float, y: float) -> Point`` Point on locally flat coordinate system, x pointing north, y pointing east.\n\nFunctions\n---------\n\n``get_version() -> str``\n\nGet the library version\n\n``geodesic_direct(latitude: float, longitude: float, azimuth: float, distance: float) -> tuple``\n\nGet position and final azimuth after moving distance along great circle\nwith starting azimuth\n\n``geodesic_inverse(latitude1: float, longitude1: float, latitude2: float, longitude2: float) -> tuple``\n\nGet starting azimuth, distance and ending azimuth of great circle\nbetween positions\n\n``rhumb_direct(latitude: float, longitude: float, azimuth: float, distance: float) -> tuple``\n\nGet position and final azimuth after moving distance from starting\nposition at fixed azimuth/along rhumb line\n\n``rhumb_inverse(latitude1: float, longitude1: float, latitude2: float, longitude2: float) -> tuple``\n\nGet rhumb line azimuth, distance and final azimuth between positions\n\n``angle_diff(arg0: numpy.ndarray[numpy.float64], arg1: numpy.ndarray[numpy.float64]) -> object``\n\nSigned difference between to angles\n\n``angle_mod(arg0: numpy.ndarray[numpy.float64]) -> object``\n\nReturn angle bound to [0.0, 360.0>\n\n``angle_mod_signed(arg0: numpy.ndarray[numpy.float64]) -> object``\n\nReturn angle bound to [-180.0, 180.0>\n",
    'author': 'Jaap Versteegh',
    'author_email': 'j.r.versteegh@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/jrversteegh/geofun',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}
from build import *
build(setup_kwargs)

setup(**setup_kwargs)
