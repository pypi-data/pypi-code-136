# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['simple_plugin_loader']

package_data = \
{'': ['*']}

install_requires = \
['simple-classproperty>=3.0']

setup_kwargs = {
    'name': 'simple-plugin-loader',
    'version': '2.2.7',
    'description': 'Dynamically load other python modules to your project.',
    'long_description': '# Simple Python Plugin Loader\n\n![PyPI package](https://github.com/mammo0/py-simple-plugin-loader/workflows/PyPI%20package/badge.svg)\n[![PyPI version](https://badge.fury.io/py/simple-plugin-loader.svg)](https://badge.fury.io/py/simple-plugin-loader)\n\nThis module provides a simple way to dynamically load other Python modules as Plugins to your current project.\n\n\n### Install\n\nYou can install this python module via **pip**:\n```shell\npip install simple-plugin-loader\n```\n\nOtherwise the module can be downloaded from PyPI: https://pypi.org/project/simple-plugin-loader/\n\n\n### Usage\n\n1. Import the module:\n    ```python\n    from simple_plugin_loader import Loader\n    ```\n2. Load your plugins/modules:\n    ```python\n    # initialize the loader\n    loader = Loader()\n\n    # load your plugins\n    plugins = loader.load_plugins(<plugin_path>, <plugin_base_class>, <specific_plugins>, <recursive>)\n    ```\n3. **(Optional)** The already loaded plugins/modules can be accessed via the `plugins` property of the loader instance:\n   ```python\n   plugins = loader.plugins\n   ``` \n\n### `load_plugins(...)` Method\nThis method does the actual plugin loading.\n\nIt loads only Python modules that can be executed in the current environment. For every successfully loaded module a message is populated through the Python `logging` library (log level: `INFO`).\n\nIf a module e.g. contains syntax errors or depends on other not installed Python modules, it will be skipped. So the main program does not fail completely. An error message is populated through the Python `logging` library (log level: `ERROR`).\n\n##### Arguments\n\n- `<plugin_path>`: _str_</br>\n  This string represents the path (relative or absolute) to the directory from where the plugins/modules should be loaded.\n- `<plugin_base_class>`: _class_ (Default: `SamplePlugin`)</br>\n  The Loader does not load all found modules that are in the above directory. It only loads classes that are **sub-classes** of the here specified class.</br>\n  The default value of this argument is the `SamplePlugin` class. You can use this class as the base class for your plugins:\n  ```python\n  from simple_plugin_loader.sample_plugin import SamplePlugin\n\n  class YourPlugin(SamplePlugin):\n      pass\n  ```\n- `<specific_plugins>`: _List[str]_ (Default: `[]`)</br>\n  This list can contain **case sensitive** class names, that should be loaded. Then no other plugins will be loaded. The argument `<plugin_base_class>` will also be ignored, so any class can be loaded.\n- `<recursive>`: _bool_ (Default: `False`)</br>\n  Set this flag to `True` if you wish to load plugins/modules recursively to the above directory.\n\n##### Return value\n\nThe method returns a dictionary that has the following structure:\n\n- **Key**: The name of the plugin/module. This name is the module name of the module that contains the plugin class.\n- **Value**: The plugin class. Not an instance!\n',
    'author': 'Marc Ammon',
    'author_email': 'marc.ammon@hotmail.de',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/mammo0/py-simple-plugin-loader',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7',
}


setup(**setup_kwargs)
