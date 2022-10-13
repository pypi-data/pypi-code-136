# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['paises']

package_data = \
{'': ['*'], 'paises': ['cache/*', 'cache/backup/*', 'cache/groups/*']}

install_requires = \
['jupyter>=1.0.0,<2.0.0',
 'pandas>=1.5.0,<2.0.0',
 'setuptools>=65.4.1,<66.0.0',
 'texttable>=1.6.4,<2.0.0',
 'twine>=4.0.1,<5.0.0',
 'wheel>=0.37.1,<0.38.0']

setup_kwargs = {
    'name': 'paises',
    'version': '0.1.0',
    'description': '',
    'long_description': 'geo\n',
    'author': 'Tomas',
    'author_email': 'tomasgonz@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
