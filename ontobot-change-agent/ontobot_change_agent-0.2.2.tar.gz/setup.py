# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['ontobot_change_agent']

package_data = \
{'': ['*']}

install_requires = \
['PyGithub>=1.55,<2.0', 'oaklib>=0.1.46,<0.2.0']

entry_points = \
{'console_scripts': ['ochange = ontobot_change_agent.cli:main']}

setup_kwargs = {
    'name': 'ontobot-change-agent',
    'version': '0.2.2',
    'description': 'Update ontologies using change language.',
    'long_description': '<!--\n<p align="center">\n  <img src="https://github.com/hrshdhgd/ontobot-change-agent/raw/main/docs/source/logo.png" height="150">\n</p>\n-->\n\nUpdate ontologies using change language.\n\n## Getting Started\n\n[Read the docs](https://hrshdhgd.github.io/ontobot-change-agent/index.html)\n\n<!-- ## Installation -->\n\n<!-- Uncomment this section after first release\nThe most recent release can be installed from\n[PyPI](https://pypi.org/project/ontobot_change_agent/) with:\n\n```bash\n$ pip install ontobot-change-agent\n```\n-->\n\n<!-- The most recent code and data can be installed directly from GitHub with:\n\n```bash\n$ pip install git+https://github.com/hrshdhgd/ontobot-change-agent.git\n``` -->\n\n<!-- ## Contributing\n\nContributions, whether filing an issue, making a pull request, or forking, are appreciated. See\n[CONTRIBUTING.md](https://github.com/hrshdhgd/ontobot-change-agent/blob/master/.github/CONTRIBUTING.md) for more information on getting involved. -->\n\n\n\n### License\n\nThe code in this package is licensed under the MIT License.\n',
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
    'python_requires': '>=3.9,<3.12',
}


setup(**setup_kwargs)
