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
['arkitekt>=0.3.7,<0.4.0', 'koil==0.2.6']

entry_points = \
{'console_scripts': ['mikro-napari = mikro_napari.run:main'],
 'napari.manifest': ['mikro-napari = mikro_napari:napari.yaml']}

setup_kwargs = {
    'name': 'mikro-napari',
    'version': '0.1.44',
    'description': '',
    'long_description': 'None',
    'author': 'jhnnsrs',
    'author_email': 'jhnnsrs@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
