# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['sigparse']

package_data = \
{'': ['*']}

extras_require = \
{':python_version < "3.10"': ['forbiddenfruit>=0.1.4,<0.2.0']}

setup_kwargs = {
    'name': 'sigparse',
    'version': '2.0.0',
    'description': 'Backports python3.10 typing features into python 3.7 and newer.',
    'long_description': '# sigparse\n\nBackports python3.10 typing features into python 3.7, 3.8, and 3.9.\n\n## Example\n\n```python\nimport sigparse\n\ndef func(param_a: list[str], param_b: str | int, param_c: tuple[int | None]):\n    ...\n\n# This returns the same result in python 3.7, 3.8, 3.9, and 3.10!\nsigparse.sigparse(func)\n```\n\nSigparse also supports classes.\n\n```python\nimport sigparse\n\nclass MyClass:\n    a: list[str]\n    b: str | int\n    c: tuple[int | None]\n\nsigparse.classparse(MyClass)\n```\n\n\n### PEP604\nBy default PEP 604 (| for unions) is only enabled for `sigparse.sigparse`.\nTo enable globally:\n```python\nimport sigparse\nsigparse.global_PEP604()\n```\n\n## Notes\n### Inspect\n\nThis module uses inspect behind the scenes. For that reason:\n\n- `sigparse.Parameter.default` is `inspect._empty` when there is no default value.\n- `sigparse.Parameter.kind` is `inspect._ParameterKind`.\n- `sigparse.ClassVar.default` is `inspect._empty` when there is no default value to maintain consistency.\n\n\n### Annotated\n`typing.Annotated` will always be evaluated with `include_extras=True` in python3.9.\n',
    'author': 'Lunarmagpie',
    'author_email': 'bambolambo0@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/Lunarmagpie/sigparse',
    'packages': packages,
    'package_data': package_data,
    'extras_require': extras_require,
    'python_requires': '>=3.7',
}


setup(**setup_kwargs)
