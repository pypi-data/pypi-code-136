# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['scope_cleaner']

package_data = \
{'': ['*']}

install_requires = \
['ipython>=8.5.0,<9.0.0']

setup_kwargs = {
    'name': 'scope-cleaner',
    'version': '0.1.0',
    'description': '',
    'long_description': '# Scope cleaner\n\nAn IPython cell magic to remove temporary variables.\nI wrote this package because I didn\'t like by global scope to be cluttered with variables I used in 1 cell only during EDA (Exploratory Data Analysis).\n\n## Installation\n\nToDo\n\n## Usage\n\nFirstly, one needs to import the package: `import scope_cleaner`.\nThen a new magic becomes available: `%%cleanup_temporary_vars <optional_prefix>`.\nOptional prefix is a parameter which helps to filter out the temporary variables introduced in current cell.\nIf it\'s not set, the prefix defaults to `_`.\n\nExample:\nConsider the following IPython cells:\n\n**Cell 2**\n```python\n%%cleanup_temporary_vars tmp\n\na = 10\nb = 15\n\ntmp_1 = 123\ntmp_2 = 234\n\nprint("tmp", tmp_1, tmp_2)  # Out: tmp 123 234\ntmp_1 + tmp_2  # Out: 357\n```\n\nSo all the variables from current cell work correctly.\n\n**Cell 3**\n```python\na + b  # Out: 25\ntmp_1  # Error: no such variable\n```\n\nAs we can see, the temporary variable was automatically deleted by `%%cleanup_temporary_vars` in the end of previous cell (because its name starts with `tmp`).\n\n',
    'author': 'Nikolay Chechulin',
    'author_email': 'nchechulin@protonmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
