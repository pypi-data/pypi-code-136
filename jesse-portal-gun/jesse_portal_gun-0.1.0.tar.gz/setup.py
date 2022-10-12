# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['jesse_portal_gun']

package_data = \
{'': ['*']}

install_requires = \
['typer[all]>=0.6.1,<0.7.0']

entry_points = \
{'console_scripts': ['jesse-portal-gun = jesse_portal_gun.main:app']}

setup_kwargs = {
    'name': 'jesse-portal-gun',
    'version': '0.1.0',
    'description': '',
    'long_description': '',
    'author': 'Jesse Hartman',
    'author_email': 'jesse@xample.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
