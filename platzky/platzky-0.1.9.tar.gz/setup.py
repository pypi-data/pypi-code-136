# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['platzky',
 'platzky.blog',
 'platzky.db',
 'platzky.plugins.redirections',
 'platzky.seo']

package_data = \
{'': ['*'], 'platzky': ['static/*', 'templates/*']}

install_requires = \
['Flask-Babel>=2.0.0,<3.0.0',
 'Flask-Markdown>=0.3,<0.4',
 'Flask-Minify>=0.39,<0.40',
 'Flask-WTF>=1.0.1,<2.0.0',
 'Flask>=2.2.2,<3.0.0',
 'PyYAML>=6.0,<7.0',
 'aiohttp>=3.8.3,<4.0.0',
 'gql>=3.4.0,<4.0.0',
 'humanize>=4.3.0,<5.0.0']

setup_kwargs = {
    'name': 'platzky',
    'version': '0.1.9',
    'description': 'Another blog in python',
    'long_description': '# platzky\n\nBlog engine in python \n',
    'author': 'None',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
