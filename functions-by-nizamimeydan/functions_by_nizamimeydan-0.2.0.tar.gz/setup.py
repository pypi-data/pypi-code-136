# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['functions_by_nizamimeydan']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'functions-by-nizamimeydan',
    'version': '0.2.0',
    'description': '',
    'long_description': '# Operation:\n multiplication(NUMBER1,NUMBER2)\n division(NUMBER1,NUMBER2)\n addition(NUMBER1,NUMBER2)\n substraction(NUMBER1,NUMBER2)\n\n returns results\n\n Example:\n print(multiplication(67,45))',
    'author': 'Meydan52',
    'author_email': 'nizamimeydan@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
