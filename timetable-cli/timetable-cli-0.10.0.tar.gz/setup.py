# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['timetable_cli']

package_data = \
{'': ['*']}

install_requires = \
['appdirs>=1.4.4,<2.0.0', 'click>=8.1.3,<9.0.0', 'rich>=12.6.0,<13.0.0']

entry_points = \
{'console_scripts': ['timetable-cli = timetable_cli.cli:command']}

setup_kwargs = {
    'name': 'timetable-cli',
    'version': '0.10.0',
    'description': '',
    'long_description': '# timetable-cli\n## How to use\n```\nUsage: timetable-cli [OPTIONS] [ACTIVITIES_SELECTOR]...\n\nOptions:\n  --config TEXT                  Config module\n  --db TEXT                      Database file.\n  --debug                        Show debug info.\n  --add-empty-lines\n  -d, --global-timedelta TEXT\n  -D, --show-date                Show current date and time.\n  -S, --show-status              Show info about current and next activities.\n  -A, --show-activities          Show activities table filtered by\n                                 activities_selectors.\n  --list-categories              Show activities categories when rendering\n                                 activities table.\n  -c, --columns TEXT             Columns to display when rendering activities\n                                 table.\n  --table-kwargs TEXT            Activities table kwargs (json)\n  --ignore-time-status\n  --combine-title-and-variation  Append activity variation to title when\n                                 rendering activities table.\n  -R, --show-rules               Show random rule.\n  -r, --rules-list               Show rules table instead of random rule.\n  -Q, --show-quotes              Show random quote.\n  -q, --quotes-list              Show quotes table instead of random quote.\n  -W, --watch\n  --watch-text TEXT\n  --watch-interval INTEGER\n  --watch-clear-screen\n  --watch-notification\n  --watch-notification-cmd TEXT\n  --watch-voice\n  --watch-voice-cmd TEXT\n  --watch-notify-eta TEXT\n  --help                         Show this message and exit.\n```\n',
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
