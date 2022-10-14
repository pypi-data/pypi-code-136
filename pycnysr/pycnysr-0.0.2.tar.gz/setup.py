# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pycnysr']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.1.3,<9.0.0',
 'coverage[toml]>=6.5.0,<7.0.0',
 'loguru>=0.5.3,<0.6.0',
 'notify-py>=0.3.3,<0.4.0',
 'pydantic>=1.9.1,<2.0.0',
 'pytest-cov>=4.0.0,<5.0.0',
 'pyyaml>=6.0,<7.0',
 'temppathlib>=1.2.0,<2.0.0',
 'types-pyyaml>=6.0.12,<7.0.0',
 'watchdog>=2.1.9,<3.0.0']

entry_points = \
{'console_scripts': ['pycnysr = pycnysr:main']}

setup_kwargs = {
    'name': 'pycnysr',
    'version': '0.0.2',
    'description': 'a simple multi directory watcher and syncer',
    'long_description': '# pycnysr\n\nA simple directory watcher and syncer\n\n# usage\n\nBased on a YAML config file (see the [example configuration file](config.dist.yaml)), this module synchronizes a local directory to one or more local or remote directories, using [rsync](https://rsync.samba.org) as the underlying backend.\n\nIt uses two levels of exclusion and inclusion in order to avoid useless expensive rsync calls. At a first level, files that don\'t need to be monitored\ncan be excluded at a cheap cost. At a second level, only files that need to be\nreally rsynced can be configured and fine tuned.\n\nIt should be able to run on Windows, Linux and macOS and generate optional notifications.\n\n# in practice\n\n```yaml\nmy-repository:\n  destinations: [\n    "my-host:~/my-repository/"\n  ]\n  event_handler:\n    excludes: [\n      ".*tmp.*"\n    ]\n    includes: [\n      ".*/api/.*",\n      ".*/conf/.*",\n    ]\n  notify: true\n  rsync:\n    filters: [\n      "- ***/*.pyc",\n      "- ***/__pycache__/",\n      "+ api/***",\n      "+ conf/***",\n      "- *"\n    ]\n    options: [\n      \'--archive\',\n      \'--delete\',\n      \'--rsh=ssh\'\n    ]\n  source: ~/Sites/my-repository/\n```\n\nGiven this `config.yaml` file, changes in the source directory `~/Sites/my-repository/` will be propagated to `my-host:~/my-repository/` via SSH with options eventually passed in the `rsync.options` list.\n\nFirst, only files not excluded in the `event_handler.excludes` (by default: [])\nand included by the `event_handler.includes` (by default: [\'.*\']) will be\npassed to the rsync process.\n\nThen, rsync is called with the [filter rules](https://download.samba.org/pub/rsync/rsync.1) built from the `rsync.filters` list.\n\nTet\'s run the watcher:\n\n```console\n❯ pycnysr --config config.yaml\n2022-10-13 21:03:17 INFO set log level to INFO\n2022-10-13 21:03:17 INFO rsync binary is /opt/homebrew/bin/rsync\n2022-10-13 21:03:17 INFO using config /Users/laurent/Sites/pycnysr/config.yaml\n2022-10-13 21:03:17 INFO syncing repository named my-repository located in /Users/laurent/Sites/pycnysr to [\'/Users/laurent/Downloads/dest/\']\n2022-10-13 21:03:17 INFO observers all initialized\n````\n\nOn another console, create a file:\n\n```console\ntouch api/new-file.txt\n```\nSee the file synchronized:\n\n```console\n2022-10-13 21:03:23 INFO synchronizing /Users/laurent/Sites/pycnysr/new-file.txt\n```\n\n# warning\n\nUse with care. early development.\n\n# license\n\nThis project is licensed under the terms of the MIT license.\n',
    'author': 'Laurent Baillet',
    'author_email': 'laurent.baillet@gmail.com',
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
