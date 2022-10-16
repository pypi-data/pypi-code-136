# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['pineline']

package_data = \
{'': ['*']}

install_requires = \
['eko>=0.10.2,<0.11.0', 'pineappl>=0.5.7,<0.6.0', 'pineko>=0.2.5,<0.3.0']

setup_kwargs = {
    'name': 'pineline',
    'version': '0.0.2',
    'description': 'Theory predictions for PDF fitting',
    'long_description': '# Pineline\n',
    'author': 'Alessandro Candido',
    'author_email': 'candido.ale@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<3.11',
}


setup(**setup_kwargs)
