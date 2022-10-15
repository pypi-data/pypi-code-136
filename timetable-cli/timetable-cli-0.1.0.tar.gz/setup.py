# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['timetable_cli']

package_data = \
{'': ['*']}

install_requires = \
['appdirs>=1.4.4,<2.0.0', 'click>=8.1.3,<9.0.0', 'rich>=12.6.0,<13.0.0']

entry_points = \
{'console_scripts': ['timetable-cli = timetable_cli.cli:commands']}

setup_kwargs = {
    'name': 'timetable-cli',
    'version': '0.1.0',
    'description': '',
    'long_description': '# timetable-cli\n## How to use\n```\nUsage: timetable-cli [OPTIONS] COMMAND [ARGS]...\n\nOptions:\n  --config TEXT                  [required]\n  --db TEXT                      [required]\n  --debug\n  -d, --global-timedelta TEXT\n  -c, --columns TEXT\n  --ignore-time-status\n  --combine-title-and-variation\n  --help                         Show this message and exit.\n\nCommands:\n  show\n  watch\n```\n',
    'author': '0djentd',
    'author_email': 'None',
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
