# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['concourseatom']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.1.3,<9.0.0',
 'pydantic-yaml>=0.8.0,<0.9.0',
 'ruamel.yaml>=0.17.21,<0.18.0']

entry_points = \
{'console_scripts': ['concmerge = concourseatom.tools:cli']}

setup_kwargs = {
    'name': 'concourseatom',
    'version': '0.1.0',
    'description': 'Read Concourse Pipelines and intelligently allowing pipelines to be built from snipits',
    'long_description': '# concourseatom\n\nThis project provides a merge funtion to intelligently merge concourse jobs together.\n',
    'author': 'Ben Greene',
    'author_email': 'BenJGreene@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/PolecatWorks/concourseatom',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
