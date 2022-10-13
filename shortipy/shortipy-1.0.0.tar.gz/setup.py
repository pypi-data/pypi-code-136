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
    'version': '1.0.0',
    'description': 'Shortipy is a RESTful Web API, written in Python language and based on the Flask micro-framework, designed to manage shortened links.',
    'long_description': '# shortipy\n\n**Shortipy** is a *RESTful Web API*, written in *Python* language and based on the *Flask* micro-framework, designed to manage shortened links. \n',
    'author': 'Simone Perini',
    'author_email': 'perinisimone98@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
