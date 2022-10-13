# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['balcony', 'balcony.custom_nodes']

package_data = \
{'': ['*']}

install_requires = \
['boto3>=1.24.80,<2.0.0',
 'inflect>=6.0.0,<7.0.0',
 'jmespath>=1.0.1,<2.0.0',
 'rich>=12.5.1,<13.0.0',
 'typer>=0.6.1,<0.7.0']

entry_points = \
{'console_scripts': ['balcony = balcony.cli:run_app']}

setup_kwargs = {
    'name': 'balcony',
    'version': '0.0.19',
    'description': 'AWS API for humans',
    'long_description': '# balcony\nAWS API for humans\n\n\n## Installation\n\n```bash\npip3 install balcony\n```\n\n## Basic Usage\n\n\n```bash\nbalcony --help\n\n# list all available services\nbalcony aws ls \n\n# list resource nodes of a service\nbalcony aws ls iam\n\n# details about the resource node\nbalcony aws ls iam Policy\n\n# read a Resource Node from AWS API\nbalcony aws read iam Policy\n```',
    'author': 'Oguzhan Yilmaz',
    'author_email': 'oguzhanylmz271@gmail.com',
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
