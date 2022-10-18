# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pelican', 'pelican.plugins.pelican_feed_stylesheet']

package_data = \
{'': ['*']}

install_requires = \
['pelican>=4.5']

extras_require = \
{'markdown': ['markdown>=3.2']}

setup_kwargs = {
    'name': 'pelican-feed-stylesheet',
    'version': '0.0.1',
    'description': 'Enables use of xml stylesheets for human-readable feed generation.',
    'long_description': 'pelican-feed-stylesheet: A Plugin for Pelican\n====================================================\n\n[![Build Status](https://img.shields.io/github/workflow/status/pelican-plugins/pelican-feed-stylesheet/build)](https://github.com/andrlik/pelican-feed-stylesheet/actions)\n[![PyPI Version](https://img.shields.io/pypi/v/pelican-feed-stylesheet)](https://pypi.org/project/pelican-feed-stylesheet/)\n![License](https://img.shields.io/pypi/l/pelican-feed-stylesheet?color=blue)\n\nEnables use of xml stylesheets for human-readable feed generation.\n\nInstallation\n------------\n\nThis plugin can be installed via:\n\n    python -m pip install pelican-feed-stylesheet\n\nUsage\n-----\n\nAdd the following to settings to enable:\n\n```python\nFEED_STYLESHEET = "/YOUR_URL_HERE.xls"\n```\n\nContributing\n------------\n\nContributions are welcome and much appreciated. Every little bit helps. You can contribute by improving the documentation, adding missing features, and fixing bugs. You can also help out by reviewing and commenting on [existing issues][].\n\nTo start contributing to this plugin, review the [Contributing to Pelican][] documentation, beginning with the **Contributing Code** section.\n\n[existing issues]: https://github.com/andrlik/pelican-feed-stylesheet/issues\n[Contributing to Pelican]: https://docs.getpelican.com/en/latest/contribute.html\n\nLicense\n-------\n\nThis project is licensed under the BSD-3-Clause license.\n',
    'author': 'Daniel Andrlik',
    'author_email': 'daniel@andrlik.org',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/andrlik/pelican-feed-stylesheet',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.6.2,<4.0',
}


setup(**setup_kwargs)
