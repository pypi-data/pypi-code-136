# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['functions_by_nizamimeydan']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'functions-by-nizamimeydan',
    'version': '0.3.0',
    'description': '',
    'long_description': '# Instructions:\n\n## Install\n```\npip install functions-by-nizamimeydan\n```\n## Intall older versions\n```\npip install functions-by-nizamimeydan=VERSION_NUMBER\n```\n\n## Operations:\n multiplication(NUMBER1,NUMBER2)\n\n division(NUMBER1,NUMBER2)\n\n addition(NUMBER1,NUMBER2)\n\n substraction(NUMBER1,NUMBER2)\n\n\n returns results\n\n ## Example:\n\n print(multiplication(67,45))',
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
