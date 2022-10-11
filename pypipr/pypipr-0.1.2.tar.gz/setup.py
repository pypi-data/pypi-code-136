# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pypipr']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'pypipr',
    'version': '0.1.2',
    'description': 'The Python Package Index Project',
    'long_description': '# Poetry\n`poetry new pypipr`\n\n`poetry add <pakage>`\n\n`poetry version <0.0.0>`\n\n`poetry build`\n\n`poetry install`\n\n`poetry config pypi-token.pypi <TOKEN>`\n\n`poetry publish`\n',
    'author': 'ufiapjj',
    'author_email': 'ufiapjj@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
