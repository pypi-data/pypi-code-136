# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['helpjuice', 'helpjuice.api']

package_data = \
{'': ['*']}

install_requires = \
['importlib-metadata>=5.0.0,<6.0.0', 'requests>=2.28.1,<3.0.0']

setup_kwargs = {
    'name': 'helpjuice',
    'version': '3.0.2',
    'description': 'Python Helpjuice API Wrapper.',
    'long_description': '# helpjuice\n\n## A Python wrapper of the Helpjuice API\n\n[![Version](https://img.shields.io/pypi/v/helpjuice?style=for-the-badge&logo=pypi&logoColor=fff)](https://pypi.org/project/helpjuice/)\n[![Python](https://img.shields.io/pypi/pyversions/helpjuice?style=for-the-badge&logo=python&logoColor=fff)](https://pypi.org/project/helpjuice/)\n[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg?style=for-the-badge&logo=gnu&logoColor=fff)](https://www.gnu.org/licenses/gpl-3.0)\n[![Tests](https://img.shields.io/github/workflow/status/samamorgan/helpjuice/Python%20%F0%9F%90%8D%20package%20%F0%9F%93%A6%20test?style=for-the-badge&logo=githubactions&logoColor=fff&label=Tests)](https://github.com/samamorgan/helpjuice/actions)\n[![Codecov](https://img.shields.io/codecov/c/gh/samamorgan/helpjuice?logo=codecov&logoColor=fff&style=for-the-badge)](https://codecov.io/gh/samamorgan/helpjuice)\n[![Docs](https://img.shields.io/readthedocs/helpjuice?logo=readthedocs&logoColor=fff&style=for-the-badge)](https://helpjuice.readthedocs.io/)\n\nThis package allows Python developers to write software that makes use of the Helpjuice API. Functions available in the API are mirrored in this package as closely as possible, translating JSON responses to Python objects. You can find the current documentation for the Helpjuice API here:\n\n[Helpjuice API Documentation](https://help.helpjuice.com/en_US/api-v3/)\n\n### Installing\n\n```\npip install helpjuice\n```\n\n### Quick Start\n\n```python\nfrom helpjuice import Client\n\nhelpjuice = Client(account="your-account", api_key="ffb722a62e8**********************")\n\n# Get a single article\narticle = helpjuice.Article(id=1).get()\n\n# Search for articles with pagination\nfor question in helpjuice.Search().get(query="foo", limit=1000, paginate=True):\n    print(question)\n```\n',
    'author': 'Sam Morgan',
    'author_email': 'sam@samamorgan.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/samamorgan/helpjuice',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
