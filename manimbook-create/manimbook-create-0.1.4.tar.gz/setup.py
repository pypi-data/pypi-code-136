# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['manimbook_create']

package_data = \
{'': ['*'],
 'manimbook_create': ['templates/*',
                      'templates/reveal.js/*',
                      'templates/reveal.js/static/*']}

install_requires = \
['chanim>=1.3,<2.0',
 'manim-physics>=0.2.4,<0.3.0',
 'manim>=0.16.0.post0,<0.17.0',
 'nbconvert>=7.2.1,<8.0.0',
 'numpy>=1.23.3,<2.0.0']

entry_points = \
{'console_scripts': ['manimbook-create = manimbook_create.convert:main']}

setup_kwargs = {
    'name': 'manimbook-create',
    'version': '0.1.4',
    'description': 'Convert a Jupyter notebook to a ManimBook (compressed html documents)',
    'long_description': '',
    'author': 'Kush Patel',
    'author_email': 'kush@kush.in',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<3.11',
}


setup(**setup_kwargs)
