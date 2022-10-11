# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['valtypes',
 'valtypes.error',
 'valtypes.error.parsing',
 'valtypes.error.parsing.type',
 'valtypes.parsing',
 'valtypes.parsing.factory',
 'valtypes.parsing.parser',
 'valtypes.parsing.rule',
 'valtypes.type',
 'valtypes.util']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'valtypes',
    'version': '6.0.0',
    'description': 'Parsing in Python has never been easier',
    'long_description': '<p align="center">\n  <img src="https://raw.githubusercontent.com/LeeeeT/valtypes/main/docs/logo.svg" />\n</p>\n\n<p align="center">\n    <em>Nothing (almost) should ever be <b>any str</b> or <b>any int</b></em>\n</p>\n\n<p align="center">\n    <a href="https://pypi.org/project/valtypes">\n        <img src="https://img.shields.io/pypi/v/valtypes" />\n    </a>\n    <a href="https://python.org/downloads">\n        <img src="https://img.shields.io/pypi/pyversions/valtypes.svg" />\n    </a>\n    <a href="https://pepy.tech/project/valtypes">\n        <img src="https://img.shields.io/pypi/dm/valtypes" />\n    </a>\n    <a href="https://github.com/LeeeeT/valtypes/actions/workflows/ci.yaml">\n        <img src="https://img.shields.io/github/workflow/status/LeeeeT/valtypes/CI" />\n    </a>\n    <a href="https://valtypes.readthedocs.io/en/latest/?badge=latest">\n        <img src="https://img.shields.io/readthedocs/valtypes" />\n    </a>\n    <a href="https://codecov.io/gh/LeeeeT/valtypes">\n        <img src="https://img.shields.io/codecov/c/github/LeeeeT/valtypes" />\n    </a>\n</p>\n\n---\n\n## What is valtypes\n\n**Valtypes** is a flexible data parsing library which will help you make illegal states unrepresentable and enable you to practice ["Parse, don’t validate"][parse-dont-validate] in Python. It has many features that might interest you, so let\'s dive into some examples.\n\n## Examples\n\nCreate constrained types:\n\n```python\nfrom valtypes.type.str import NonEmpty, MaximumLength\n\n\nclass Name(NonEmpty, MaximumLength):\n    __maximum_length__ = 20\n\n    \ndef initials(name: Name) -> str:\n    # name is guaranteed to be a non-empty string of maximum length 20\n    return f"{name[0]}."\n\n\ninitials(Name("Fred"))  # passes\ninitials(Name(""))  # parsing error\ninitials("")  # fails at static type checking\n```\n\nParse complex data structures:\n\n```python\nfrom dataclasses import dataclass\n\n\nfrom valtypes import parse\nfrom valtypes.type import int, list, str\n\n\n@dataclass\nclass User:\n    id: int.Positive\n    name: Name\n    hobbies: list.NonEmpty[str.NonEmpty]\n\n    \nraw = {"id": 1, "name": "Fred", "hobbies": ["origami", "curling", "programming"]}\n\nprint(parse(User, raw))\n```\n\n```\nUser(id=1, name=\'Fred\', hobbies=[\'origami\', \'curling\', \'programming\'])\n```\n\n## Installation\n\nInstall from [PyPI][pypi]:\n\n```console\npip install valtypes\n```\n\nBuild the latest version from [source][source]:\n\n```console\npip install git+https://github.com/LeeeeT/valtypes\n```\n\n[parse-dont-validate]: https://lexi-lambda.github.io/blog/2019/11/05/parse-don-t-validate\n\n[pypi]: https://pypi.org/project/valtypes\n\n[source]: https://github.com/LeeeeT/valtypes\n',
    'author': 'LeeeeT',
    'author_email': 'leeeet@inbox.ru',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/LeeeeT/valtypes',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
