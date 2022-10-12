# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['functions_by_vladalt']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'functions-by-vladalt',
    'version': '0.3.0',
    'description': 'This is our testproject',
    'long_description': '# Instructions \n\n### Please install this package\n\n```\npip install functions-by-vladalt\n```\n\n### You can also install older package\n\n```\npip install functions-by-vladalt=VERSION_NUMBER\n```',
    'author': 'Vladyslav Altyok',
    'author_email': 'vladyslav.altyok@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
