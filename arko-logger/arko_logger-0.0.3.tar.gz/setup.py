# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['arkologger']

package_data = \
{'': ['*']}

install_requires = \
['pydantic>=1.10.2,<2.0.0', 'rich>=12.6.0,<13.0.0']

setup_kwargs = {
    'name': 'arko-logger',
    'version': '0.0.3',
    'description': 'A logger.',
    'long_description': '# arko-logger\n\n一个 logger ， 用于 ArkoClub 的项目',
    'author': 'Karako',
    'author_email': 'karakohear@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
