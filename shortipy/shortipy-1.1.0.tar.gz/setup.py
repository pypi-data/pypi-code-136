# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['shortipy', 'shortipy.controllers', 'shortipy.services']

package_data = \
{'': ['*']}

install_requires = \
['flask-redis>=0.4.0,<0.5.0', 'flask>=2.2.2,<3.0.0']

setup_kwargs = {
    'name': 'shortipy',
    'version': '1.1.0',
    'description': 'Shortipy is a RESTful Web API, written in Python language and based on the Flask micro-framework, designed to manage shortened links.',
    'long_description': '![shortipy logo](https://github.com/CoffeePerry/shortipy/blob/main/art/shortipy.png?raw=true)\n\n![GitHub release (latest by date)](https://img.shields.io/github/v/release/CoffeePerry/shortipy)\n![PyPI](https://img.shields.io/pypi/v/shortipy?logo=PyPI&logoColor=white)\n![PyPI - Status](https://img.shields.io/pypi/status/shortipy)\n\n![PyPI - Python Version](https://img.shields.io/pypi/pyversions/shortipy?logo=Python&logoColor=white)\n![PyPI - Implementation](https://img.shields.io/pypi/implementation/shortipy)\n\n[![Flask](https://img.shields.io/badge/framework-Flask-black?logo=Flask&logoColor=white)](https://github.com/pallets/flask/)\n\n[![GitHub license](https://img.shields.io/github/license/CoffeePerry/shortipy)](https://github.com/CoffeePerry/shortipy/blob/master/LICENSE)\n\n[![GitHub issues](https://img.shields.io/github/issues/CoffeePerry/shortipy)](https://github.com/CoffeePerry/shortipy/issues)\n\n# shortipy\n\n**Shortipy** is a *RESTful Web API*, written in *Python* language and based on the *Flask* micro-framework, designed to manage shortened links. \n',
    'author': 'Simone Perini',
    'author_email': 'perinisimone98@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/CoffeePerry/shortipy',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
