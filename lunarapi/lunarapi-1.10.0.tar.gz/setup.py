# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['lunarapi']

package_data = \
{'': ['*']}

install_requires = \
['Pillow>=9.2.0,<10.0.0',
 'aiohttp>=3.6.0,<3.8.0',
 'python-dotenv>=0.20.0,<0.21.0']

extras_require = \
{':python_version >= "3.8" and python_version < "3.9"': ['typing-extensions>=4.1.0,<4.3.0']}

setup_kwargs = {
    'name': 'lunarapi',
    'version': '1.10.0',
    'description': 'Wrapper for the Lunar API',
    'long_description': 'Lunar API\n_____\n\nA fast, asynchronous and simple API wrapper for the Lunar API\n\nDocs: https://docs.lunardev.group/\n',
    'author': 'WinterFe',
    'author_email': 'winter@lunardev.group',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://pypi.org/project/lunarapi/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
