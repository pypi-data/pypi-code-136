# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['jsonref', 'proxytypes']
setup_kwargs = {
    'name': 'jsonref',
    'version': '1.0.0b1',
    'description': 'jsonref is a library for automatic dereferencing of JSON Reference objects for Python.',
    'long_description': '# jsonref\n\n[![image](https://github.com/gazpachoking/jsonref/actions/workflows/test.yml/badge.svg?branch=master)](https://github.com/gazpachoking/jsonref/actions/workflows/test.yml?query=branch%3Amaster)\n[![image](https://readthedocs.org/projects/jsonref/badge/?version=latest)](https://jsonref.readthedocs.io/en/latest/)\n[![image](https://coveralls.io/repos/gazpachoking/jsonref/badge.png?branch=master)](https://coveralls.io/r/gazpachoking/jsonref)\n[![image](https://img.shields.io/pypi/v/jsonref?color=%2334D058&label=pypi%20package)](https://pypi.org/project/jsonref)\n\n`jsonref` is a library for automatic dereferencing of [JSON\nReference](https://datatracker.ietf.org/doc/html/draft-pbryan-zyp-json-ref-03)\nobjects for Python (supporting Python 3.3+).\n\nThis library lets you use a data structure with JSON reference objects,\nas if the references had been replaced with the referent data.\n\n```python console\n>>> from pprint import pprint\n>>> import jsonref\n\n>>> # An example json document\n>>> json_str = """{"real": [1, 2, 3, 4], "ref": {"$ref": "#/real"}}"""\n>>> data = jsonref.loads(json_str)\n>>> pprint(data)  # Reference is not evaluated until here\n{\'real\': [1, 2, 3, 4], \'ref\': [1, 2, 3, 4]}\n```\n\n# Features\n\n-   References are evaluated lazily. Nothing is dereferenced until it is\n    used.\n-   Recursive references are supported, and create recursive python data\n    structures.\n\nReferences objects are actually replaced by lazy lookup proxy objects\nwhich are almost completely transparent.\n\n```python console\n>>> data = jsonref.loads(\'{"real": [1, 2, 3, 4], "ref": {"$ref": "#/real"}}\')\n>>> # You can tell it is a proxy by using the type function\n>>> type(data["real"]), type(data["ref"])\n(<class \'list\'>, <class \'jsonref.JsonRef\'>)\n>>> # You have direct access to the referent data with the __subject__\n>>> # attribute\n>>> type(data["ref"].__subject__)\n<class \'list\'>\n>>> # If you need to get at the reference object\n>>> data["ref"].__reference__\n{\'$ref\': \'#/real\'}\n>>> # Other than that you can use the proxy just like the underlying object\n>>> ref = data["ref"]\n>>> isinstance(ref, list)\nTrue\n>>> data["real"] == ref\nTrue\n>>> ref.append(5)\n>>> del ref[0]\n>>> # Actions on the reference affect the real data (if it is mutable)\n>>> pprint(data)\n{\'real\': [2, 3, 4, 5], \'ref\': [2, 3, 4, 5]}\n```\n',
    'author': 'Chase Sterling',
    'author_email': 'chase.sterling@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'py_modules': modules,
    'python_requires': '>=3.3,<4.0',
}


setup(**setup_kwargs)
