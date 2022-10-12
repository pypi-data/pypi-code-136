# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['functions_by_rusnak']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'functions-by-rusnak',
    'version': '0.3.0',
    'description': 'This is our test project',
    'long_description': '#instructions\n\n#### This is our test project.\n#### Please install this package\n```\npip install functions-by-rusnak\n```\n\n#### You can also install older packages\n```\npip install functions-by-rusnak==VERSION_NUMBER\n```',
    'author': 'Kateryna Rusnak',
    'author_email': 'minipytka888@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
