# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['michaniskin_pypi_test']

package_data = \
{'': ['*']}

install_requires = \
['typer[all]>=0.6.1,<0.7.0']

entry_points = \
{'console_scripts': ['pypi-test = michaniskin_pypi_test.main:app']}

setup_kwargs = {
    'name': 'michaniskin-pypi-test',
    'version': '0.1.0',
    'description': '',
    'long_description': '# asdf\n',
    'author': 'Micha Niskin',
    'author_email': 'micha.niskin@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
