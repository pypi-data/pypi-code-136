# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['balconyapp', 'balconyapp.app']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'balconyapp',
    'version': '0.0.20',
    'description': 'Balcony App template package',
    'long_description': '# balcony-app-template\nA template repository for creating new Balcony Apps.\n',
    'author': 'Oguzhan Yilmaz',
    'author_email': 'oguzhanylmz271@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
