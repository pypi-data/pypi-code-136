# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['poetry_plugin_pypi_mirror']

package_data = \
{'': ['*']}

install_requires = \
['poetry>=1.2.1,<2.0.0']

entry_points = \
{'poetry.plugin': ['demo = poetry_plugin_pypi_mirror.plugins:PyPIMirrorPlugin']}

setup_kwargs = {
    'name': 'poetry-plugin-pypi-mirror',
    'version': '0.1.0',
    'description': 'Poetry plugin that adds support for pypi.org mirrors and pull-through caches',
    'long_description': 'None',
    'author': 'Jacob Henner',
    'author_email': 'code@ventricle.us',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
