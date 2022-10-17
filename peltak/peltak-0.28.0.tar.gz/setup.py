# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['cliform',
 'peltak',
 'peltak.commands',
 'peltak.core',
 'peltak.core.git',
 'peltak.core.scripts',
 'peltak.core.templates',
 'peltak.core.versioning',
 'peltak.testing']

package_data = \
{'': ['*'], 'peltak': ['templates/*']}

install_requires = \
['PyYAML>=6.0',
 'click>=7.0,<8.0',
 'jinja2>=2.12',
 'pygments>=2.7.4',
 'tomlkit>=0.7.0']

entry_points = \
{'console_scripts': ['peltak = peltak.main:root_cli']}

setup_kwargs = {
    'name': 'peltak',
    'version': '0.28.0',
    'description': 'A command line tool to help manage a project',
    'long_description': '######\npeltak\n######\n\n.. readme_about_start\n\n**peltak**\'s goal is to simplify day-to-day dev tasks that we all, as developers,\nhave to do. It does not try to be a build system or to replace any of the tools\nyou would normally use when developing project like test runners, linters, etc.\nThink of it rather as a replacement for the shell scripts that usually wrap\nthose tools. It actually started years ago as a collection of those shell\nscripts that with time evolved into a very flexible, extensible and easy to use\ncommand line app.\n\n.. readme_about_end\n\nUseful links\n============\n\n- `Documentation <https://novopl.github.io/peltak>`_\n    - `Installation <https://novopl.github.io/peltak/docs/html/guides/installation.html>`_\n    - `Quickstart <https://novopl.github.io/peltak/docs/html/guides/quickstart.html>`_\n    - `Dev Docs <https://novopl.github.io/peltak/docs/html/dev/_index.html>`_\n- `Source Code <https://github.com/novopl/peltak>`_\n- `CI Builds <https://circleci.com/gh/novopl/peltak>`_\n\n\nInstallation\n============\n\n.. readme_installation_start\n\n.. code-block:: shell\n\n    $ pip install peltak\n\nEnabling auto-completion\n------------------------\n**peltak** has a great auto-completion thanks to the underlying click library.\nThe steps to enable it vary slightly depending on what shell you are using\n\n**Bash users**\n\n    Either run this command or to make the change permanent add it to your\n    ``~/.bashrc``:\n\n    .. code-block:: shell\n\n        eval "$(_PELTAK_COMPLETE=source peltak)"\n\n**ZSH users**\n    Either run this command or to make the change permanent add it to your\n    ``~/.zshrc``:\n\n    .. code-block:: shell\n\n        eval "$(_PELTAK_COMPLETE=source_zsh peltak)"\n\n.. readme_installation_end\n',
    'author': 'Mateusz Klos',
    'author_email': 'novopl@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'http://novopl.github.com/peltak',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7.2,<4.0',
}


setup(**setup_kwargs)
