# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['simple_github_crawler']

package_data = \
{'': ['*']}

install_requires = \
['beautifulsoup4>=4.11.1,<5.0.0',
 'lxml>=4.9.1,<5.0.0',
 'requests>=2.28.1,<3.0.0']

setup_kwargs = {
    'name': 'simple-github-crawler',
    'version': '0.2.1',
    'description': '',
    'long_description': "simple-github-crawler Documentation\n============================\nThis is github-crawler package. You can crawl the count of consecutive commits.\n\nQuick Start\n===========\n```\nfrom simple_github_crawler import commit\n\nis_complted, streak = commit.get_streak(username='JAY-Chan9yu')\nprint(streak)\n```\n",
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
