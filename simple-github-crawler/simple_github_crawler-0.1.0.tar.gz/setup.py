# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['simple_github_crawler']

package_data = \
{'': ['*']}

install_requires = \
['beautifulsoup4>=4.11.1,<5.0.0']

setup_kwargs = {
    'name': 'simple-github-crawler',
    'version': '0.1.0',
    'description': '',
    'long_description': '',
    'author': 'JayJi',
    'author_email': 'ckj9014@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/JAY-Chan9yu/simple_github_crawler',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
