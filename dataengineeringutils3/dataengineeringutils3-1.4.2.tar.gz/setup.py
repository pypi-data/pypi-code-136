# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['dataengineeringutils3']

package_data = \
{'': ['*']}

install_requires = \
['Deprecated>=1.2.12,<2.0.0', 'PyYAML>=6.0,<7.0', 'boto3>=1.24.11,<2.0.0']

setup_kwargs = {
    'name': 'dataengineeringutils3',
    'version': '1.4.2',
    'description': 'Data engineering utils Python 3 version',
    'long_description': '[![Coverage Status](https://coveralls.io/repos/github/moj-analytical-services/dataengineeringutils3/badge.svg?branch=master)](https://coveralls.io/github/moj-analytical-services/dataengineeringutils3?branch=master)\n\n# Data engineering utils - Python 3\n\nFully unit tested utility functions for data engineering. Python 3 only.  \n\n\n## Installation\n\n```bash\npip install dataengineeringutils3\n```\n\n\n## Testing\n\n```bash\npytest --cov-report term-missing --cov=dataengineeringutils3 tests/\n```\n',
    'author': 'Data Engineering',
    'author_email': 'dataengineering@digital.justice.gov.uk',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/moj-analytical-services/dataengineeringutils3',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4',
}


setup(**setup_kwargs)
