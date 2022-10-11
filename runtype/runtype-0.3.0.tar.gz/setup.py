# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['runtype']

package_data = \
{'': ['*']}

extras_require = \
{':python_version >= "3.6" and python_version < "3.7"': ['dataclasses']}

setup_kwargs = {
    'name': 'runtype',
    'version': '0.3.0',
    'description': 'Type dispatch and validation for run-time Python',
    'long_description': '![alt text](logo.png "Logo")\n\n\nRuntype is a collection of run-time type utilities for Python.\n\nIt is:\n\n:runner: Fast! Uses an internal typesystem for maximum performance.\n\n:brain: Smart! Supports `typing`, forward-references, constraints, auto-casting, and more.\n\n:gear: Configurative! Write your own type system, and use it with *dataclass* and *dispatch*.\n\n------\n\n### Modules\n\n- :star: [**validation**](https://runtype.readthedocs.io/en/latest/validation.html) - Provides a smarter alternative to `isinstance` and `issubclass`, with support for the `typing` module, and type constraints.\n\n- :star: [**dataclass**](https://runtype.readthedocs.io/en/latest/dataclass.html) - Adds run-time type validation to the built-in dataclass.\n\n    - Improves dataclass ergonomics.\n    - Supports most mypy constructs, like `typing` and forward-references (`foo: \'Bar\'`).\n    - Supports automatic value casting, Pydantic-style. (Optional, off by default)\n    - Supports types with constraints. (e.g. `String(max_length=10)`)\n    - Supports optional sampling for faster validation of big lists and dicts.\n    - Twice faster than Pydantic ([read here](https://runtype.readthedocs.io/en/latest/dataclass.html#compared-to-pydantic))\n\n- :star: [**dispatch**](https://runtype.readthedocs.io/en/latest/dispatch.html) - Provides fast multiple-dispatch for functions and methods, via a decorator.\n\n    - Inspired by Julia.\n\n- :star: [**type utilities**](https://runtype.readthedocs.io/en/latest/types.html) - Provides a set of classes to implement your own type-system.\n\n    - Used by runtype itself, to emulate the Python type-system.\n\n\n## Docs\n\nRead the docs here: https://runtype.readthedocs.io/\n\n## Install\n\n```bash\npip install runtype\n```\n\nNo dependencies.\n\nRequires Python 3.6 or up.\n\n[![Build Status](https://travis-ci.org/erezsh/runtype.svg?branch=master)](https://travis-ci.org/erezsh/runtype)\n[![codecov](https://codecov.io/gh/erezsh/runtype/branch/master/graph/badge.svg)](https://codecov.io/gh/erezsh/runtype)\n\n## Examples\n\n### Validation (Isa & Subclass)\n\n```python\nfrom typing import Dict, Mapping\nfrom runtype import isa, issubclass\n\nprint( isa({\'a\': 1}, Dict[str, int]) )\n#> True\nprint( isa({\'a\': \'b\'}, Dict[str, int]) )\n#> False\n\nprint( issubclass(Dict[str, int], Mapping[str, int]) )\n#> True\nprint( issubclass(Dict[str, int], Mapping[int, str]) )\n#> False\n```\n\n### Dataclasses\n\n```python\nfrom typing import List\nfrom datetime import datetime\nfrom runtype import dataclass\n\n@dataclass(check_types=\'cast\')  # Cast values to the target type, when applicable\nclass Person:\n    name: str\n    birthday: datetime = None   # Optional\n    interests: List[str] = []   # The list is copied for each instance\n\n\nprint( Person("Beetlejuice") )\n#> Person(name=\'Beetlejuice\', birthday=None, interests=[])\nprint( Person("Albert", "1955-04-18T00:00", [\'physics\']) )\n#> Person(name=\'Albert\', birthday=datetime.datetime(1955, 4, 18, 0, 0), interests=[\'physics\'])\nprint( Person("Bad", interests=[\'a\', 1]) )\n# Traceback (most recent call last):\n#   ...\n# TypeError: [Person] Attribute \'interests\' expected value of type list[str]. Instead got [\'a\', 1]\n\n#     Failed on item: 1, expected type str\n\n```\n\n### Multiple Dispatch\n\n```python\nfrom runtype import Dispatch\ndp = Dispatch()\n\n@dp\ndef append(a: list, b):\n    return a + [b]\n\n@dp\ndef append(a: tuple, b):\n    return a + (b,)\n\n@dp\ndef append(a: str, b: str):\n    return a + b\n\n\nprint( append([1, 2, 3], 4) )\n#> [1, 2, 3, 4]\nprint( append((1, 2, 3), 4) )\n#> (1, 2, 3, 4)\nprint( append(\'foo\', \'bar\') )\n#> foobar\nprint( append(\'foo\', 4)     )\n# Traceback (most recent call last):\n#    ...\n# runtype.dispatch.DispatchError: Function \'append\' not found for signature (<class \'str\'>, <class \'int\'>)\n```\n\n\n## License\n\nRuntype uses the [MIT license](LICENSE).\n\n## Donate\n\nIf you like Runtype and want to show your appreciation, you can do so at my [patreon page](https://www.patreon.com/erezsh), or [ko-fi page](https://ko-fi.com/erezsh).\n',
    'author': 'Erez Shinan',
    'author_email': 'erezshin@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/erezsh/runtype',
    'packages': packages,
    'package_data': package_data,
    'extras_require': extras_require,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
