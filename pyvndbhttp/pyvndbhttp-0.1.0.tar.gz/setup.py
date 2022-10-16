# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

modules = \
['pyvndbhttp']
install_requires = \
['requests>=2.28.1,<3.0.0']

setup_kwargs = {
    'name': 'pyvndbhttp',
    'version': '0.1.0',
    'description': 'VNDB HTTPS API implementation',
    'long_description': '# pyvndbhttp\nPython implementation of VNDB HTTP API\n',
    'author': 'Konosprod',
    'author_email': 'konosprod@free.fr',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'py_modules': modules,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
