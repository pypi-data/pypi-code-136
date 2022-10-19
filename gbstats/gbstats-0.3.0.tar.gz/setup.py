# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['gbstats', 'gbstats.bayesian', 'tests']

package_data = \
{'': ['*']}

install_requires = \
['numpy>=1.23.4,<2.0.0', 'pandas>=1.5.1,<2.0.0', 'scipy>=1.9.2,<2.0.0']

setup_kwargs = {
    'name': 'gbstats',
    'version': '0.3.0',
    'description': 'Stats engine for GrowthBook, the open source feature flagging and A/B testing platform.',
    'long_description': '# GrowthBook Stats\n\nThe stats engine for GrowthBook, the open source A/B testing platform.\n\n## Installation\n\n```\npip install gbstats\n```\n\n## Usage\n\n```python\nimport gbstats\n```\n',
    'author': 'Jeremy Dorn',
    'author_email': 'jeremy@growthbook.io',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/growthbook/growthbook/tree/main/packages/stats',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
