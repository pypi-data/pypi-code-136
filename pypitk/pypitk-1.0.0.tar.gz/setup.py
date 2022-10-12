# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['pypitk', 'pypitk.pypipackage']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'pypitk',
    'version': '1.0.0',
    'description': 'pypi toolkit to build, publish and update pypi packages',
    'long_description': '# pypi toolkit to build, publish and update pypi packages',
    'author': 'wayfaring-stranger',
    'author_email': 'zw6p226m@duck.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
