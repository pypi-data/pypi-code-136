# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['dimple']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'dimple',
    'version': '0.2.0',
    'description': '',
    'long_description': '# dimple\n\n',
    'author': 'noogie',
    'author_email': 'noogie.dev@nym.hush.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
