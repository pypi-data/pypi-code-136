# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['wiztype', 'wiztype.memory']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.1.3,<9.0.0', 'memobj>=0.8.1,<0.9.0']

entry_points = \
{'console_scripts': ['wiztype = wiztype.__main__:main']}

setup_kwargs = {
    'name': 'wiztype',
    'version': '0.1.0',
    'description': 'A type dumper for wizard101',
    'long_description': '# wiztype\nA type dumper for wizard101\n\n## usage\nan instance of wizard101 must be open for all commands\n\n```shell\n# generate a normal dump in the current directory named after the current revision\n$ wiztype\n# generate a dump with indent level 4 (for human reading)\n$ wiztype --indent 4\n# generate a version 1 dump (wizwalker)\n$ wiztype --version 1 --indent 4\n```\n\n\n## json spec\n\n```json5\n{\n  "version": 2,\n  "classes": {\n    "class hash (as string)": {\n      "bases": ["class base classes"],\n      "name": "class name",\n      "singleton": true,\n      "properties": {\n        "property name": {\n          "type": "property type",\n          "id": 123,\n          "offset": 123,\n          "flags": 123,\n          "container": "container name",\n          "dynamic": true,\n          "pointer": true,\n          "hash": 123,\n          "enum_options": {\n            "option name": 123,\n            // __DEFAULT is a string\n            "__DEFAULT": "option name",\n            // __BASECLASS is a string\n            "__BASECLASS": "option name",\n          }\n        }\n      }\n    }\n  }\n}\n```\n',
    'author': 'StarrFox',
    'author_email': 'starrfox6312@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/StarrFox/wiztype',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
