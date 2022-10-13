# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ostatslib',
 'ostatslib.features_extractor',
 'ostatslib.features_extractor.extract_functions']

package_data = \
{'': ['*']}

install_requires = \
['numpy>=1.23.4,<2.0.0', 'pandas>=1.5.0,<2.0.0']

setup_kwargs = {
    'name': 'ostatslib',
    'version': '0.1.0',
    'description': 'Open Statistical Analysis Agent Library',
    'long_description': '# ostatslib\nOpen Statistics Library\n\n[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=OStatsAA_ostatslib&metric=coverage)](https://sonarcloud.io/summary/new_code?id=OStatsAA_ostatslib)\n[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=OStatsAA_ostatslib&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=OStatsAA_ostatslib)\n',
    'author': 'Guilherme',
    'author_email': 'g.lisboa.oliveira@outlook.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
