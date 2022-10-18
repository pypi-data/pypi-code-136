# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['pygments_onehalf']

package_data = \
{'': ['*']}

install_requires = \
['Pygments>=2.10.0,<3.0.0']

entry_points = \
{'pygments.styles': ['onehalf-dark = pygments_onehalf:OneHalfDark',
                     'onehalf-light = pygments_onehalf:OneHalfLight']}

setup_kwargs = {
    'name': 'pygments-onehalf',
    'version': '1.0.0',
    'description': 'One Half color scheme for Pygments.',
    'long_description': '# pygments-onehalf\n\n[![python: 3.6 | 3.7 | 3.8 | 3.9](https://img.shields.io/badge/python-3.6%20%7C%203.7%20%7C%203.8%20%7C%203.9-blue)](https://www.python.org/)\n[![license: MIT](https://img.shields.io/badge/license-MIT-blueviolet.svg)](https://opensource.org/licenses/MIT)\n[![PyPI](https://img.shields.io/pypi/v/pygments-onehalf)](https://pypi.org/project/pygments-onehalf/)\n[![PyPI - Downloads](https://img.shields.io/pypi/dm/pygments-onehalf)](https://pypistats.org/packages/pygments-onehalf)\n[![ci status](https://gitlab.com/tomwatson1024/pygments-onehalf/badges/master/pipeline.svg)](https://gitlab.com/tomwatson1024/pygments-onehalf/commits/master)\n[![Checked with mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)\n[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)\n\n\nOne Half color scheme for Pygments.\n\nBased on https://github.com/sonph/onehalf, used under the MIT license.\n\n## Installation\n\n### Using Poetry\n\n```\npoetry add pygments-onehalf\n```\n\n### Using Pip\n\n```\npip install pygments-onehalf\n```\n\n## Usage\n\nProvides two pygments styles:\n- `onehalf-dark`\n- `onehalf-light`\n',
    'author': 'Tom W',
    'author_email': '796618-tomwatson1024@users.noreply.gitlab.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://gitlab.com/tomwatson1024/pygments-onehalf',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
