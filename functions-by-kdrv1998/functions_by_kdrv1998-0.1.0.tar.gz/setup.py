# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['functions_by_kdrv1998']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'functions-by-kdrv1998',
    'version': '0.1.0',
    'description': 'This is our test project',
    'long_description': '',
    'author': 'Zhaniya Kadyrova',
    'author_email': 'kdrv.jn@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
