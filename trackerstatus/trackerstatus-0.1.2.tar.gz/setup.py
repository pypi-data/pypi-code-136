# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['trackerstatus']

package_data = \
{'': ['*']}

install_requires = \
['requests>=2.28.1,<3.0.0']

setup_kwargs = {
    'name': 'trackerstatus',
    'version': '0.1.2',
    'description': 'A python library for gathering data from the trackerstatus.info website',
    'long_description': '# trackerstatus\n\n[![PyPI](https://img.shields.io/pypi/v/trackerstatus.svg)](https://pypi.org/project/trackerstatus/)\n[![Python Version](https://img.shields.io/pypi/pyversions/trackerstatus.svg)](https://github.com/mauvehed/yourIP/actions/workflows/main.yml)\n[![CodeQL](https://github.com/mauvehed/trackerstatus/actions/workflows/codeql-analysis.yml/badge.svg)](https://github.com/mauvehed/trackerstatus/actions/workflows/codeql-analysis.yml)\n[![Pylint](https://github.com/mauvehed/trackerstatus/actions/workflows/pylint.yml/badge.svg)](https://github.com/mauvehed/trackerstatus/actions/workflows/pylint.yml)\n\nA python library for gathering data from the [https://trackerstatus.info](https://trackerstatus.info) website\n\n## Install via Pip\n\n```pip install trackerstatus```\n\n## Resources\n\n* Github repo: [https://github.com/mauvehed/trackerstatus/](https://github.com/mauvehed/trackerstatus/)\n* Pip package: [https://pypi.org/project/trackerstatus/](https://pypi.org/project/trackerstatus/)\n',
    'author': 'mauvehed',
    'author_email': 'mh@mvh.dev',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/mauvehed/trackerstatus',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
