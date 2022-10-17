# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['origami']

package_data = \
{'': ['*']}

install_requires = \
['Pygments>=2.12.0,<3.0.0',
 'Sphinx>=5.0.2,<6.0.0',
 'sphinx-copybutton>=0.5.0,<0.6.0']

entry_points = \
{'sphinx.html_themes': ['origami = origami']}

setup_kwargs = {
    'name': 'origami-theme',
    'version': '0.1.0',
    'description': 'Origami sphinx theme',
    'long_description': '',
    'author': 'Bartek Sokorski',
    'author_email': 'b.sokorski@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
