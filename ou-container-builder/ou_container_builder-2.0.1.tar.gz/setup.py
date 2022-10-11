# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ou_container_builder',
 'ou_container_builder.core',
 'ou_container_builder.packs']

package_data = \
{'': ['*'],
 'ou_container_builder': ['templates/*',
                          'templates/core/content/*',
                          'templates/core/services/*',
                          'templates/core/startup/*',
                          'templates/packs/mariadb/*',
                          'templates/packs/tutorial-server/*']}

install_requires = \
['cerberus>=1.3.3,<2.0.0',
 'click>=7.1.2,<8.0.0',
 'jinja2>=3.0.0,<4.0.0',
 'pyyaml>=5.4.1,<6.0.0']

entry_points = \
{'console_scripts': ['ou-container-builder = '
                     'ou_container_builder.__main__:main']}

setup_kwargs = {
    'name': 'ou-container-builder',
    'version': '2.0.1',
    'description': '',
    'long_description': 'None',
    'author': 'Mark Hall',
    'author_email': 'mark.hall@open.ac.uk',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
