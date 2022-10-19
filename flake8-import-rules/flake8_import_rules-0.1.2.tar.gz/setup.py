# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['flake8_import_rules']
entry_points = \
{'flake8.extension': ['I013 = flake8_import_rules:ImportRulesChecker']}

setup_kwargs = {
    'name': 'flake8-import-rules',
    'version': '0.1.2',
    'description': '',
    'long_description': "Helps to prevent import of certain modules from certain modules.\n\nIt's useful if you have many modules in your project and want to keep them kind of\nisolated.\n\nAfter installing just add `import-rules` option to your `setup.cfg` file.\n\n```\n[flake8]\n...\nimport-rules= \n\t# yaml format here\n\tmodule_one:\n\t\t- allow module_two\n\t\t- deny any\n\tmodule_two:\n\t\t- deny module_one.sub.submodule\n\tmodule_two.sumbodule:\n\t\t- deny module_one\n\tmodule_three: allow any\n\n\t# this will prevent any import everywhere\n\tany:\n\t\t- deny any\n\n\t# default behaviour is\n\tany:\n\t\t- allow any\n\n...\n```\n\n",
    'author': 'VL',
    'author_email': '1844144@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'py_modules': modules,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
