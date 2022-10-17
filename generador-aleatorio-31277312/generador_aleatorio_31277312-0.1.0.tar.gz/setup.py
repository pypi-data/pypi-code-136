# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['generador_aleatorio']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'generador-aleatorio-31277312',
    'version': '0.1.0',
    'description': 'ttt',
    'long_description': '# Generador aletorio\nEsto es 1 prueba',
    'author': 'Conrado',
    'author_email': 'konrad.es@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
