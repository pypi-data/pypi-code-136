# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['quick',
 'quick.commands',
 'quick_client',
 'quick_client.api',
 'quick_client.models']

package_data = \
{'': ['*'], 'quick_client': ['docs/*']}

install_requires = \
['PyYAML>=5.3,<6.0',
 'isodate>=0.6.0,<0.7.0',
 'python-dateutil>=2.5.0,<3.0.0',
 'requests>=2.0.0,<3.0.0',
 'six>=1.12.0,<2.0.0',
 'urllib3>=1.0,<2.0']

entry_points = \
{'console_scripts': ['quick = quick.__main__:main']}

setup_kwargs = {
    'name': 'quick-cli',
    'version': '0.8.0',
    'description': 'The CLI to control your quick cluster.',
    'long_description': "# Quick CLI\n\n![Tests](https://github.com/bakdata/quick-cli/workflows/Test%20quick-cli/badge.svg)\n![Code Quality](https://github.com/bakdata/quick-cli/workflows/Code%20Quality/badge.svg)\n[![PyPI Version](https://img.shields.io/pypi/v/quick-cli?color=blue&label=PyPi%20Version)](https://pypi.org/project/quick-cli/)\n\n\nThe Quick CLI lets you manage your Quick instance.\nFor more information on how to work with it, see our [user guide](https://bakdata.github.io/quick/dev/user/).\n\n## Set up\n\nThe CLI is a Python project and you can install via pip:\n```shell\npip install quick-cli\n```\n\nThe first step after installing the CLI is creating a new context.\nOur [user guide](https://bakdata.github.io/quick/dev/user/getting-started/setup-cli/) provides further information.\n\n## Reference\n\nThere is a [list of all commands](https://bakdata.github.io/quick/dev/user/reference/cli-commands/) as a reference.\nAdditionally, you can run all commands with `-h` or `--help` to display a help message.\n\n## Contributing\n\nThe [CLI's developer guide](https://bakdata.github.io/quick/dev/developer/cli/) provides more information on how to setup the project and the project's layout.\nFor general information, check out out the [contributing guide](https://bakdata.github.io/quick/dev/developer/contributing/).\n",
    'author': 'd9p',
    'author_email': 'contact@d9p.io',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://d9p.io/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
