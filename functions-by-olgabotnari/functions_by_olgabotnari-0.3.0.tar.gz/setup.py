# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['functions_by_olgabotnari']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'functions-by-olgabotnari',
    'version': '0.3.0',
    'description': 'This is our test project',
    'long_description': "# Instructions \n\n### This is our test project. \n### Please install this package\n'''\npip install functions_by_olgabotnari\n'''\n\n### You can also install older packages\n'''\npip install functions-by-olgabotnari==VERSION_NUMBER\n'''\n",
    'author': 'Olga Botnari',
    'author_email': 'olga.u.botnari@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
