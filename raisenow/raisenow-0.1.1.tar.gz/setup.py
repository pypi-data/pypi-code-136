# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['raisenow']

package_data = \
{'': ['*']}

install_requires = \
['urllib3>=1.26.12,<2.0.0']

setup_kwargs = {
    'name': 'raisenow',
    'version': '0.1.1',
    'description': 'A python library to interact with the RaiseNow API',
    'long_description': '# A python library to interact with the RaiseNow API',
    'author': 'Martin Mohnhaupt',
    'author_email': 'm.mohnhaupt@bluewin.ch',
    'maintainer': 'Martin Mohnhaupt',
    'maintainer_email': 'm.mohnhaupt@bluewin.ch',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
