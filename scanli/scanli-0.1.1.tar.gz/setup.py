# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['scanli']
install_requires = \
['cache-to-disk>=2.0.0,<3.0.0',
 'requests>=2.28.1,<3.0.0',
 'requirements-parser>=0.5.0,<0.6.0',
 'rich>=12.6.0,<13.0.0']

entry_points = \
{'console_scripts': ['scanli = scanli:main']}

setup_kwargs = {
    'name': 'scanli',
    'version': '0.1.1',
    'description': 'CLI tool which scans project dependencies for OSS licenses.',
    'long_description': '# Scanli\n\nOSS license detection and reporting.',
    'author': 'Chris Lawlor',
    'author_email': 'lawlor.chris@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/chrislawlor/scanli',
    'py_modules': modules,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
