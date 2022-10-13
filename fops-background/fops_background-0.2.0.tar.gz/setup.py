# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['background', 'background.dispatch', 'background.transport']

package_data = \
{'': ['*']}

install_requires = \
['boto3', 'pydantic>=1.10.2,<2.0.0', 'typing-extensions>=4.1.0,<5.0.0']

setup_kwargs = {
    'name': 'fops-background',
    'version': '0.2.0',
    'description': 'Background Tasks implementation, primarily targeting AWS Lambda',
    'long_description': 'None',
    'author': 'Anthony King',
    'author_email': 'anthony.king@fundingoptions.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/FundingOptions/background-tasks-python',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
