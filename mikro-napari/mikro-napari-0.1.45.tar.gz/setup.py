# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['mikro_napari',
 'mikro_napari.api',
 'mikro_napari.container',
 'mikro_napari.models',
 'mikro_napari.widgets',
 'mikro_napari.widgets.dialogs',
 'mikro_napari.widgets.sidebar']

package_data = \
{'': ['*']}

install_requires = \
['arkitekt>=0.3.7,<0.4.0', 'koil==0.2.8']

entry_points = \
{'console_scripts': ['mikro-napari = mikro_napari.run:main'],
 'napari.manifest': ['mikro-napari = mikro_napari:napari.yaml']}

setup_kwargs = {
    'name': 'mikro-napari',
    'version': '0.1.45',
    'description': 'A napari plugin to interact and provide functionality for a connected arkitekt server',
    'long_description': '# mikro-napari\n\n[![codecov](https://codecov.io/gh/jhnnsrs/mikro-napari/branch/master/graph/badge.svg?token=UGXEA2THBV)](https://codecov.io/gh/jhnnsrs/mikro-napari)\n[![PyPI version](https://badge.fury.io/py/mikro-napari.svg)](https://pypi.org/project/mikro-napari/)\n[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://pypi.org/project/mikro-napari/)\n![Maintainer](https://img.shields.io/badge/maintainer-jhnnsrs-blue)\n[![PyPI pyversions](https://img.shields.io/pypi/pyversions/mikro-napari.svg)](https://pypi.python.org/pypi/mikro-napari/)\n[![PyPI status](https://img.shields.io/pypi/status/mikro-napari.svg)](https://pypi.python.org/pypi/mikro-napari/)\n\nmikro napari enables napari on the mikro/arkitekt platform\n\n# DEVELOPMENT\n\n## Idea\n\nThis is a napari plugin, that provides a simple user interface to use napari with mikro you can view and annotate\ndata on the mikro platform (synchronised between all of your napari instances) and use napari within arkitekt workflows\n(can be extended with other plugins)\n\n## Install\n\nSimple install this plugin via naparis plugin-manager and enable it. \nLogin with your local mikro/arkitekt platform and start using it in workflows\n\nYou can also install mikro-napari directly in your enviroment \n\n```bash\npip install mikro-napari napari[pyqt5]\n```\n\n',
    'author': 'jhnnsrs',
    'author_email': 'jhnnsrs@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/jhnnsrs/mikro-napari',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
