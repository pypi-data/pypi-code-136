# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['swaml']

package_data = \
{'': ['*']}

install_requires = \
['pyyaml>=6.0,<7.0', 'typer[all]>=0.6.1,<0.7.0']

entry_points = \
{'console_scripts': ['swaml = swaml.main:app']}

setup_kwargs = {
    'name': 'swaml',
    'version': '0.1.1',
    'description': 'Populates those tedious package versions for your environment.yml.',
    'long_description': 'Populates those tedious package versions for your environment.yml.\n\n![swamling](doc/_static/swamling.gif)\n\n# Installation\nWith `pipx`\n```bash\npipx install swaml\n```\nWith `pip`\n```bash\npython -m pip install swaml\n```\n# How To Use\nActivate the `conda` environment you desire to populate.\n```bash\n$ conda activate <env>\n```\nMake sure your `environment.yml` file is in your current working directory. (Currently, it must also be named `environment.yml`.)\n```bash\n$ ls\n... environment.yml ...\n```\nRun with dry run to be sure of the changes. Otherwise, run without.\n```bash\nswaml run --dry-run\n```',
    'author': 'Your Name',
    'author_email': 'you@example.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
