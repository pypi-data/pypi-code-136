# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['onto_crawler']

package_data = \
{'': ['*']}

install_requires = \
['PyGithub>=1.55,<2.0', 'oaklib>=0.1.35,<0.2.0']

entry_points = \
{'console_scripts': ['ocrawl = onto_crawler.cli:main']}

setup_kwargs = {
    'name': 'onto-crawler',
    'version': '0.1.11',
    'description': 'Crawl github for ontology related issues.',
    'long_description': '<!--\n<p align="center">\n  <img src="https://github.com/hrshdhgd/onto-crawler/raw/main/docs/source/logo.png" height="150">\n</p>\n-->\n\nCrawl github for ontology specific issues.\n\n## Getting Started\n\n[Read the docs](https://hrshdhgd.github.io/onto-crawler/index.html)\n\n<!-- ## Installation -->\n\n<!-- Uncomment this section after first release\nThe most recent release can be installed from\n[PyPI](https://pypi.org/project/onto_crawler/) with:\n\n```bash\n$ pip install onto-crawler\n```\n-->\n\n<!-- The most recent code and data can be installed directly from GitHub with:\n\n```bash\n$ pip install git+https://github.com/hrshdhgd/onto-crawler.git\n``` -->\n\n<!-- ## Contributing\n\nContributions, whether filing an issue, making a pull request, or forking, are appreciated. See\n[CONTRIBUTING.md](https://github.com/hrshdhgd/onto-crawler/blob/master/.github/CONTRIBUTING.md) for more information on getting involved. -->\n\n\n\n### License\n\nThe code in this package is licensed under the MIT License.\n',
    'author': 'Harshad Hegde',
    'author_email': 'hhegde@lbl.gov',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
