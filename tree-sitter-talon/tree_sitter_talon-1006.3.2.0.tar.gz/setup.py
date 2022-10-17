# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['tree_sitter_talon', 'tree_sitter_talon.internal']

package_data = \
{'': ['*'],
 'tree_sitter_talon': ['data/tree-sitter-talon/*',
                       'data/tree-sitter-talon/.github/*',
                       'data/tree-sitter-talon/.github/workflows/*',
                       'data/tree-sitter-talon/bindings/node/*',
                       'data/tree-sitter-talon/bindings/rust/*',
                       'data/tree-sitter-talon/script/*',
                       'data/tree-sitter-talon/src/*',
                       'data/tree-sitter-talon/src/tree_sitter/*',
                       'data/tree-sitter-talon/test/*',
                       'data/tree-sitter-talon/test/corpus/*',
                       'data/tree-sitter-talon/test/corpus/andreas-talon/*',
                       'data/tree-sitter-talon/test/corpus/knausj_talon/*',
                       'data/tree-sitter-talon/test/corpus/talon-axkit/*']}

install_requires = \
['dataclasses-json>=0.5.7,<0.6.0',
 'parsec>=3.14,<4.0',
 'setuptools<65.6.0',
 'tree-sitter-type-provider>=2.1.18,<3.0.0',
 'tree-sitter>=0.20.0,<0.21.0']

extras_require = \
{'test': ['bumpver',
          'mypy>=0.971,<0.972',
          'pytest>=7.1.2,<8.0.0',
          'pytest-golden>=0.2.2,<0.3.0']}

setup_kwargs = {
    'name': 'tree-sitter-talon',
    'version': '1006.3.2.0',
    'description': 'Parser for Talon files in Python.',
    'long_description': '# Parser for Talon files in Python\n\n[![GitHub Workflow Status](https://github.com/wenkokke/py-tree-sitter-talon/actions/workflows/build.yml/badge.svg)](https://github.com/wenkokke/py-tree-sitter-talon/actions/workflows/build.yml) ![GitHub tag (latest by date)](https://img.shields.io/github/v/tag/wenkokke/py-tree-sitter-talon) ![PyPI](https://img.shields.io/pypi/v/tree-sitter-talon)\n',
    'author': 'Wen Kokke',
    'author_email': 'wenkokke@users.noreply.github.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/wenkokke/py-tree-sitter-talon',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.7.1,<4.0.0',
}
from build import *
build(setup_kwargs)

setup(**setup_kwargs)
