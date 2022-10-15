# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['jaskier']

package_data = \
{'': ['*']}

install_requires = \
['jinja2>=3.1.2,<4.0.0']

extras_require = \
{':python_version < "3.11"': ['tomli>=2.0.1,<3.0.0']}

setup_kwargs = {
    'name': 'jaskier',
    'version': '0.1.0.post1',
    'description': '',
    'long_description': '# Jaskier \n\nThe herald of news, the teller of changes. \n\nInspired by [towncrier](https://github.com/twisted/towncrier), focused on simplicity and markdown support\n',
    'author': 'Bartek Sokorski',
    'author_email': 'b.sokorski@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.7,<3.12',
}


setup(**setup_kwargs)
