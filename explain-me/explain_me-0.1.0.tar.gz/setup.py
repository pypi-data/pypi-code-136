# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['explain_me']

package_data = \
{'': ['*']}

install_requires = \
['pydantic>=1.10.2,<2.0.0']

setup_kwargs = {
    'name': 'explain-me',
    'version': '0.1.0',
    'description': 'package explain data concept python',
    'long_description': '# explain_me\n\n',
    'author': 'vaziria',
    'author_email': 'manorder123@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
