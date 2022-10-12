# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['ustatus',
 'ustatus.components',
 'ustatus.components.drawing',
 'ustatus.components.modules',
 'ustatus.graphics',
 'ustatus.hooks',
 'ustatus.modules',
 'ustatus.utils']

package_data = \
{'': ['*']}

install_requires = \
['PyGObject>=3.42.0,<4.0.0',
 'dbus-next>=0.2.3,<0.3.0',
 'gbulb>=0.6.2,<0.7.0',
 'jsonschema>=4.4.0,<5.0.0',
 'psutil==5.8.0',
 'pulsectl-asyncio>=0.2.0,<0.3.0',
 'pulsectl>=22.3.2,<23.0.0',
 'python-dbus-system-api>=0.1.0,<0.2.0',
 'python-reactive-ui>=0.2.9,<0.3.0',
 'tomli>=1.2.2,<2.0.0']

entry_points = \
{'console_scripts': ['ustatus = ustatus.main:main',
                     'ustatus_docgen = ustatus.docgen:generate_docs']}

setup_kwargs = {
    'name': 'ustatus',
    'version': '0.1.8',
    'description': 'GTK-based status window for wayland shells.',
    'long_description': "# ustatus\n\n_NOTE: Previously named pystatus, renamed due to a PyPI project naming conflict\npreventing me from publishing the project._\n\nConfigurable status window and/or bar for wayland compositors with support for\nthe wlr-layer-shell protocol.\n\n![Screenshot closed](pystatus_closed.png)\n![Screenshot cpu meters](pystatus_cpu.png)\n![Screenshot power-profiles-daemon](pystatus_ppd.png)\n![Screenshot powermenu](pystatus_power.png)\n\n## Features\n\n- TOML configuration.\n  - Supports configuration of different bars, and choice of bar at startup with\n    commandline argument.\n- A variety of built-in modules:\n  - System tray module ([StatusNotifierItem protocol](https://www.freedesktop.org/wiki/Specifications/StatusNotifierItem/)), with Dbusmenu.\n  - Cpu monitor module, with usage graphs.\n  - MPRIS module.\n  - Battery module.\n  - Volume module.\n  - [power-profiles-daemon](https://gitlab.freedesktop.org/hadess/power-profiles-daemon) remote module.\n- Remote interface through dbus, currently allowing:\n  - Show/hide/toggle bar or status window.\n\n## Running without installing\n\nThe project is built using [Poetry](https://python-poetry.org/).\nTo run, clone the project\n\n```\ngit clone https://github.com/mbrea-c/ustatus.git\n```\n\nmove to the cloned directory\n\n```\ncd ustatus\n```\n\ninstall dependencies in a local venv with\n\n```\npoetry install\n```\n\nand run ustatus with\n\n```\npoetry run ustatus <bar name>\n```\n\n## User-wide installation from source\n\nThe project is built using [Poetry](https://python-poetry.org/).\n\nTo build\nlocally, clone the project\n\n```\ngit clone https://github.com/mbrea-c/ustatus.git\n```\n\nmove to the cloned directory\n\n```\ncd ustatus\n```\n\nand build\n\n```\npoetry build\n```\n\nThis will create two files in the `dist` directory,\n\n```\ndist/ustatus-<version_number>.tar.gz\ndist/ustatus-<version_number>-py3-none-any.whl\n```\n\nFor a user-wide installation, run\n\n```\ncd dist\npip install --upgrade ustatus-<version_number>.tar.gz\n```\n\n## Configuration\n\nSee the [configuration guide](CONFIGURATION.md) for details. An example configuration file can be\nfound in [examples/ustatus.toml](examples/ustatus.toml)\n\n## Is this in an usable state?\n\nI think so, I have used (and still use) this in my daily-driver machine for about 6 months.\nHowever, there are currently some limitations that some might consider deal\nbreaking:\n\n- The UI respects the system GTK theme, but it is not possible to do separate\n  custom theming at the moment. I'm thinking of adding some form of this soon though, as GTK\n  allows theming using CSS fairly easily.\n- In my daily driver setup I use a status window anchored to the right side of\n  the screen, so I haven't done a lot of testing with a horizontal status _bar_.\n  It is possible, but there might (will) be bugs and rough edges. I'm willing to\n  work on this if there is interest.\n",
    'author': 'Manuel Brea',
    'author_email': 'm.brea.carreras@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/mbrea-c/ustatus',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
