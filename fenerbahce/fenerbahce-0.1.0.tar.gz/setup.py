# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['fenerbahce']

package_data = \
{'': ['*']}

install_requires = \
['bs4>=0.0.1,<0.0.2',
 'click>=8.1.3,<9.0.0',
 'coverage>=6.5.0,<7.0.0',
 'lxml>=4.9.1,<5.0.0',
 'pytest>=7.1.3,<8.0.0',
 'requests>=2.28.1,<3.0.0']

entry_points = \
{'console_scripts': ['fenerbahce = fenerbahce.interface:interface']}

setup_kwargs = {
    'name': 'fenerbahce',
    'version': '0.1.0',
    'description': '',
    'long_description': "# Fenerbahce\n\nfenerbahce is a command line tool to fetch information past and future games of Fenerbahçe's Professional Football Team\n\nCurrently, only the last and the next game information can be shown. In the future I will integrate live scores, and pip packaging.\n\n## Installation\n\nInstall with pip:\n\n```pip install fenerbahce```\n\n\n## Commands\n\n`fenerbahce next` -> Fetches next match information\n\n`fenerbahce last` -> Fetches last match information\n\n## Dependencies\n\nfenerbahce depends on the following packages:\n\n- BeautifulSoup4\n- lxml\n- click\n- requests\n- pytest\n- coverage.py\n\n## Running locally\n\nThe project is built by using poetry and Python3. So to be able to run this project locally, make sure you have a running Python3 instance and a working poetry distribution.\n\nIn order to run the project locally, after cloning the repository, use the command:\n\n```\npoetry run fenerbahce\n```\n\nCommands described above can also be executed, but with little caveats:\n\n`poetry run fenerbahce next` -> Fetches next match information\n\n`poetry run fenerbahce last` -> Fetches last match information\n\n## Testing\n\nTo run tests, run the command:\n```\npoetry run pytest\n```\n\nTo calculate coverage, run these commands consecutively:\n```\npoetry run coverage run -m pytest\npoetry run coverage report\n```\n\nAlternatively, an HTML report can also be generated:\n```\npoetry run coverage run -m pytest\npoetry run coverage html\n```",
    'author': 'mehmet',
    'author_email': 'mehmetccm@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
