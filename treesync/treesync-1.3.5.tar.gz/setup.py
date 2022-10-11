# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['treesync',
 'treesync.bin',
 'treesync.bin.treesync',
 'treesync.bin.treesync.commands',
 'treesync.configuration']

package_data = \
{'': ['*']}

install_requires = \
['pathlib-tree>=2,<3']

entry_points = \
{'console_scripts': ['treesync = treesync.bin.treesync.main:main']}

setup_kwargs = {
    'name': 'treesync',
    'version': '1.3.5',
    'description': 'Utilitiies to use rsync for multiple targets',
    'long_description': "![Unit Tests](https://github.com/hile/treesync/actions/workflows/unittest.yml/badge.svg)\n![Style Checks](https://github.com/hile/treesync/actions/workflows/lint.yml/badge.svg)\n\n# Tree synchronization utility\n\nThis utility allows configuring regularly repeated rsync commands and sharing\nof configuration flags per server. Configured *sync targets* can be called\nwith `treesync pull` and `treesync push` commands to avoid mistakes in repeated\nlong and complex rsync arguments.\n\n\n# Example usage\n\nFollowing example commands show how to use the tool for listing and syncing multiple targets.\n\nThese example commands match the example configuration shown below.\n\n```bash\n# List all targets\n> treesync list\nlaptop:music\nnas:documents\nnas:music\n\n# Lists targets where host or target name starts with letter s or m\n> treesync list s* m*\nlaptop:music\nnas:music\n\n# Pull documents files from nas server\n> treesync pull nas-server:documents\n\n# Push music to bot nas-server and laptop\n> treesync push music\n\n# Push all files to nas-server\n> treesync push nas-server\n```\n\n# Installing\n\nInstall latest version from *pypi*:\n\n```bash\npip install treesync\n```\n\n# Configuration file\n\nConfiguration file for treesync tool is `~/.config/treesync.yml`. The file suppports defining sync targets in two formats. Both formats can be mixed in same configuration file.\n\nIf same target name is defined in both formats, the `sources and hosts` declaration is used.\n\n## Sources and hosts format\n\nThe `sources` and `hosts` format contains two sections:\n\n- `sources` list of dictionaries with `name` and  `path` elements and with optional `excludes_file`\n   option\n- `hosts` list of dictionaries with at least `name` and `targets` options and with optional\n  `iconv`, `rsync_path` and `flags` options\n\nThis format is suitable to use when same source is pushed to multiple target servers: the format\ndefines source path and excludes file in one place and avoids copypaste errors.\n\nExample configuration with all supported flags:\n\n```yaml\nhosts:\n  # macOS laptop with 'rsync 3' from homebrew\n  - name: laptop\n    # Defines the rsync command path on remote host (from macOS homebrew)\n    rsync_path: /usr/local/bin/rsync\n    targets:\n      # Listed as laptop:music\n      - source: music\n        # The laptop is also a Mac, so no iconv is needed\n        destination: mylaptop:/Users/myname/Music\n  # Demo host with Linux or FreeBSD, requiring the 'iconv' config\n  - name: nas\n    # This is rsync flag to push from macOS to Linux/BSD\n    iconv: UTF-8-MAC,UTF-8\n    # Remove server will have different username\n    flags:\n      - --usermap=localuser:nasuser\n      - --groupmap=localgroup:nasgroup\n    targets:\n      # The source field refers to 'sources' section name field\n      # Listed as nas:documents\n      - source: documents\n        # Destination is full rsync command remote path without any special quoting\n        destination: nas-server:/backups/My Documents\n      # Listed as nas:music\n      - source: music\n        destination: nas-server:/shared/Music\nsources:\n  - name: documents\n    path: /Users/myname/Documents\n    excludes_file: /Users/myname/Documents/.rsync_exclude\n  - name: music\n    path: /Users/myname/Music\n    excludes_file: /Users/myname/.music-excluded\n```\n\n## Targets format\n\nThe `targets` format defines sync targets with `targets` with a single configuration section\nand server specific settings with `servers` section. In this format, the excludes_file must be\nrepeated for each 'source' and source paths are repeated if pushed to multiple servers.\n\nThis format is suitable for cases where the same source is not pushed to multiple targets.\n\nServer name to get server settings from `servers`section is recognized from the `destination`\nfield path by separating the path from first `:` letter.\n\n```yaml\nservers:\n  laptop:\n    # Defines the rsync command path on remote host\n    rsync_path: /usr/local/bin/rsync\n  nas-server:\n    # This is rsync flag to push from macOS to Linux/BSD\n    iconv: UTF-8-MAC,UTF-8\n    # Remove server will have different username\n    flags:\n      - --usermap=localuser:remoteuser\n      - --groupmap=localgroup:users\ntargets:\n  nas:documents:\n    source: /Users/localuser/Documents\n    destination: nas-server:/shared/Music\n    excludes_file: /home/localuser/Documents/.rsync_exclude\n  nas:music:\n    source: /Users/localuser/Music\n    destination: nas-server:/shared/Music\n    excludes_file: /Users/myname/.music-excluded\n  laptop:music:\n    source: /Users/localuser/Music\n    destination: nas-server:/shared/Music\n    excludes_file: /Users/myname/.music-excluded\n```\n\nExamples of valid configuration files can be also seen in unit test data:\n\n* [sources and hosts configuration](tests/mock/host_sources.yml)\n* [old format target list configuration](tests/mock/old_format_servers.yml)\n",
    'author': 'Ilkka Tuohela',
    'author_email': 'hile@iki.fi',
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
