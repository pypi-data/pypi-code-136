# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['docstring_generator']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.1.3,<9.0.0',
 'strongtyping-pyoverload>=0.3.0,<0.4.0',
 'strongtyping>=3.9.2,<4.0.0']

entry_points = \
{'console_scripts': ['gendocs = docstring_generator.__main__:main']}

setup_kwargs = {
    'name': 'docstring-generator',
    'version': '0.2.2',
    'description': 'Auto generate docstring from type-hints.',
    'long_description': '# docstring_generator\nAuto generate docstring from type-hints\n\n## How to use it\n```shell\ngendocs file.py\n```\n\n```shell\ngendocs mydir/\n```\n\n## Options\n\n### style\n- `--style`\n- Docstring style [numpy, rest].  [default: numpy]\n\n### ignore-classes\n- `--ignore-classes`\n- when used then no class will be modified\n\n### ignore-functions\n- `--ignore-functions`\n- when used then no function will be modified this\n- __!important__ class methods are no functions in this context\n\n\n### Add additional information before running `gendocs` \n- when adding `$<num>` into your docstring these will then be replaced with parameter at this index\n- Example:\n```python\nfrom typing import List\n\n\ndef foo(val_a: int, val_b: List[int]):\n    """\n    Lorem ipsum dolor sit amet, consetetur sadipscing elitr,\n    sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam\n\n    $1 Lorem ipsum dolor sit amet\n    $2 nonumy eirmod tempor invidun\n    """\n```\nwill become (here with numpy style)\n```python\nfrom typing import List\n\n\ndef foo(val_a: int, val_b: List[int]):\n    """\n    Lorem ipsum dolor sit amet, consetetur sadipscing elitr,\n    sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam\n    \n    Parameters\n    ----------\n    val_a : argument of type int\n        Lorem ipsum dolor sit amet\n    val_b : argument of type List(int)\n        nonumy eirmod tempor invidun\n\n    """\n```\n\n## Examples\n- An example can be found under examples\n\n### Installing\n\n- pip install docstring-generator\n\n#### Versioning\n- For the versions available, see the tags on this repository.\n\n### Authors\n- Felix Eisenmenger\n\n### License\n- This project is licensed under the MIT License - see the LICENSE.md file for details\n',
    'author': 'FelixTheC',
    'author_email': 'felixeisenmenger@gmx.net',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/FelixTheC/docstring_generator',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<=3.11',
}


setup(**setup_kwargs)
