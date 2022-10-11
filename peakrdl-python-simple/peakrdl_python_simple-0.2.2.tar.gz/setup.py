# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['peakrdl_python_simple', 'peakrdl_python_simple.regif']

package_data = \
{'': ['*']}

install_requires = \
['systemrdl-compiler>=1.23.0,<2.0.0']

extras_require = \
{'cli': ['peakrdl>=0.3.0,<0.4.0']}

entry_points = \
{'peakrdl.exporters': ['python-simple = '
                       'peakrdl_python_simple.__peakrdl__:Exporter']}

setup_kwargs = {
    'name': 'peakrdl-python-simple',
    'version': '0.2.2',
    'description': 'Export Python description from the systemrdl-compiler register model',
    'long_description': '[![Documentation Status](https://readthedocs.org/projects/peakrdl-python-simple/badge/?version=latest)](http://peakrdl-python-simple.readthedocs.io)\n[![build](https://github.com/MarekPikula/PeakRDL-Python-simple/workflows/build/badge.svg)](https://github.com/MarekPikula/PeakRDL-Python-simple/actions?query=workflow%3Abuild+branch%3Amain)\n[![Coverage Status](https://coveralls.io/repos/github/MarekPikula/PeakRDL-Python-simple/badge.svg?branch=main)](https://coveralls.io/github/MarekPikula/PeakRDL-Python-simple?branch=main)\n[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/peakrdl-python-simple.svg)](https://pypi.org/project/peakrdl-python-simple)\n\n# PeakRDL-Python\n\nThis package implements Python register abstraction layer export for the\nPeakRDL toolchain.\n\n- **Export:** Convert compiled SystemRDL input into Python register interface.\n\nFor the command line tool, see the [PeakRDL\nproject](https://peakrdl.readthedocs.io).\n\n## Usage\n\nPeakRDL project provides a standard CLI interface. It can be installed directly\nvia pip or by installing this package with `cli` extra:\n\n    $ pip install peakrdl-python-simple[cli]\n\nThen this package can be used with the following command:\n\n    $ peakrdl python-simple input_file.rdl -o output_interface.py\n\n## Documentation\n\nSee the [PeakRDL-Python-simple\nDocumentation](http://peakrdl-python-simple.readthedocs.io) for more details.\n',
    'author': 'Marek Pikuła',
    'author_email': 'marek.pikula@embevity.com',
    'maintainer': 'Marek Pikuła',
    'maintainer_email': 'marek.pikula@embevity.com',
    'url': 'https://github.com/MarekPikula/PeakRDL-Python-simple',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.7.2,<4.0.0',
}


setup(**setup_kwargs)
