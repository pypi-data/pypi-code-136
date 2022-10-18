# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['datapac',
 'datapac.package',
 'datapac.rcave',
 'datapac.rcave.services',
 'datapac.rcave.sources',
 'datapac.rcave.sources.postgres',
 'datapac.rcave.sources.s3',
 'datapac.rcave.utils',
 'datapac.utils']

package_data = \
{'': ['*']}

install_requires = \
['Jinja2>=3.1.2,<4.0.0',
 'PyYAML>=6.0,<7.0',
 'boto3>=1.24.81,<2.0.0',
 'click>=8.1.3,<9.0.0',
 'psycopg2>=2.9.3,<3.0.0',
 'pydantic>=1.10.2,<2.0.0']

entry_points = \
{'console_scripts': ['datapac = datapac.cli:cli']}

setup_kwargs = {
    'name': 'datapac',
    'version': '0.1.2',
    'description': '',
    'long_description': '# datapac\n',
    'author': 'Jerguš Lejko',
    'author_email': 'jergus.lejko@gmail.com',
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
