# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['sql_cli', 'sql_cli.utils']

package_data = \
{'': ['*'], 'sql_cli': ['macros/*', 'templates/*']}

install_requires = \
['Jinja2>=2.10.1,<=3.1',
 'networkx>=2.8.7,<3.0.0',
 'python-frontmatter>=1.0.0,<2.0.0',
 'typer[all]>=0.6.1,<0.7.0']

entry_points = \
{'console_scripts': ['flow = sql_cli.__main__:app']}

setup_kwargs = {
    'name': 'astro-sql-cli',
    'version': '0.0.2',
    'description': 'Empower analysts to build workflows to transform data using SQL',
    'long_description': '# Astro SQL CLI\n\nEmpower analysts to build workflows to transform data using SQL.\n\n\n## Getting started\n\n### Install\n\n```bash\n    pip install astro-sql-cli\n```\n\n### Try it out\n\n```bash\n    flow version\n```\n\n\n## Development\n\nSetup your local environment:\n\n```bash\n    make setup\n```\n\nTry your own version of the SQL CLI locally:\n\n```bash\n    poetry run flow version\n```\n\nRun the tests:\n\n```bash\n    make test\n```\n',
    'author': 'Astronomer',
    'author_email': 'humans@astronomer.io',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0.0',
}


setup(**setup_kwargs)
