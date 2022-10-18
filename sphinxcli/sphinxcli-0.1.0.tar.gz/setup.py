# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['sphinxcli']

package_data = \
{'': ['*']}

modules = \
['py']
install_requires = \
['Sphinx>=5.1.1,<6.0.0',
 'click-repl>=0.2.0,<0.3.0',
 'click>=8.1.3,<9.0.0',
 'furo>=2022.9.15,<2023.0.0',
 'rich-click>=1.5.2,<2.0.0',
 'rich>=12.5.1,<13.0.0',
 'tomlkit>=0.11.4,<0.12.0',
 'typing-extensions>=4.3.0,<5.0.0',
 'xdg>=5.1.1,<6.0.0']

entry_points = \
{'console_scripts': ['sphinxcli = sphinxcli.__main__:cli']}

setup_kwargs = {
    'name': 'sphinxcli',
    'version': '0.1.0',
    'description': '',
    'long_description': '# SphinxCLI\n\nA CLI tool to ease the generation Sphinx documents by allowing for multiple builders and multiple languages to be built using a single command.\n\nThere are 2 ways of using the tool. As a REPL or as individual commands.\n\n```sh\nsphinxcli repl\nsphinxcli build\nsphinxcli build html\nsphinxcli build html:latex\nsphinxcli build html en\nsphinxcli build html en:fr\n```\n\n## REPL\n\nIf you don\'t use a command i.e. you jusrt call `sphinxcli` you\'ll be put into a REPL where the commands below\ncan be used one after another\n\n```\n$ sphinxcli\n\nsphinxcli> settings\nSphinxCLI Settings\n  source       = src/docs\n  target       = docs\n  builders     = [\'html\']\n  languages    = [\'en\']\n  config       = src/docs\n  doctree      = artifact/doctree\n  target_order = builder\n\nsphinxcli> set languages en:fr\n\nsphinxcli> set target build/docs\n\nsphinxcli> build\nBuild Settings\n  config  = /sphinxcli/src/docs\n  source  = /sphinxcli/src/docs\n  doctree = /sphinxcli/artifact/doctree\n\nBuilding html\n  language  = en\n  directory = /sphinxcli/docs/html/en\n\nBuilding html\n  language  = fr\n  directory = /sphinxcli/docs/html/fr\n\nsphinxcli> clean\nCleaning all generated files\n  Removed documents in docs...\n  Removed doctrees in artifact/doctree...\n\nsphinxcli> quit\n```\n\n\n## Commands\n\n### `help` or `?`\n\nUsing `help` or `?` displays a list of the available commands\n\n    Available commands:\n      ?        - Display this list of commands\n      build    - Build Sphinx the documents\n      clean    - Clean any generated files\n      exit     - Exit the REPL\n      get      - Get a configuration setting\n      help     - Display this list of commands\n      quit     - Quit the REPL\n      set      - Set a configuration setting\'s value\n      settings - Display the current values of all settings\n      version  - Display the version number of this tool\n\n### `exit` or `quit`\n\nExits the REPL\n\n### `build`\n\nTo run all builders and all languages defined in the config file use\n\n```sh\nsphinxcli build\n```\n\nTo run a specific builder specify it after the build command\n\n```sh\nsphinxcli build html\n```\n\nTo run multiple builders add them after the build command separated by `:` characters.\n\n```sh\nsphinxcli build "html:latex"\n```\n\nTo generate documents for specific languages specify them after the builders.\n\n```sh\nsphinxcli build html "en:fr"\n```\n\n### `clean`\n\nRemoves any built files (documents and doctrees)\n\n### `get`\n\nGet a setting\'s value\n\n### `set`\n\nSet a setting\'s value and update the `pyproject.toml` file.\n\n### `settings`\n\nDisplay a list of the current settings\n\n```text\nSphinxCLI Settings\n  source       = src/docs/source\n  target       = docs\n  builders     = [\'html\']\n  languages    = [\'en\']\n  config       = src/docs/source\n  doctree      = src/docs/build/doctree\n  target_order = builder\n```\n\n### version\n\nDisplays the version number of the tool\n\n## Configuration\n\nThe tool is configured within the `pyproject.toml` file.\n\nThe `builders` item defines which builders are run by default and can be specified as\n\n- a string with one builder e.g. `html`\n- a string with multiple builders separated by a `:` character e.g. `html:latex`\n- a list of builders e.g. `["html", "latex"]`\n\nThe `source` item defines the directory where the Sphinx source files (`.rst`/`.md`) can be found.\n\nThe `target` item specifies where the built files will be written\n\nThe `languages` specifies the default languages to be built and can be specified like the `builders` item.\n\nThe `config` item specifies the directory where the Sphinx `conf.py` can be found.\n\nThe `doctree` item specifies where the Sphinx environment files will be stored.\n\nThe `target_order` item specifies how the built files will be structured.\nIt can be either\n\n- `builder` which means the files will be written to the directory structure `target/builder/language`\n- `language` which means the files will be written to the directory structure `target/language/builder`\n\n```toml\n[tool.sphinxcli]\nbuilders = ["html"]\nsource = "src/docs/source"\ntarget = "docs"\nlanguages = ["en"]\nconfig = "src/docs/source"\ndoctree = "src/docs/build/doctree"\ntarget_order = "builder"\n```\n',
    'author': 'Simon Kennedy',
    'author_email': 'sffjunkie+code@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'py_modules': modules,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
