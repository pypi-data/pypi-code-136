# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['payroll_1c']
setup_kwargs = {
    'name': 'payroll-1c',
    'version': '0.3.2',
    'description': 'Parse 1C Payrolls XML file',
    'long_description': '1C Payrolls\n===========\n[![PyPI](https://img.shields.io/pypi/pyversions/payroll-1c.svg)](https://pypi.org/project/payroll-1c/ "Latest version on PyPI")\n[![codecov](https://codecov.io/gh/voronind/payroll-1c/branch/master/graph/badge.svg)](https://codecov.io/gh/voronind/payroll-1c "Coverage")\n\nParse 1C Payrolls XML file\n\nInstall\n-------\n```commandline\npip install payroll_1c\n```\n\nUsage\n-----\n\n```python\n>>> from payroll_1c import Payroll1C\n>>> payroll = Payroll1C(\'1C-payroll.xml\')\n>>> payroll = Payroll1C(fromstring=\'<СчетаПК>...</СчетаПК>\')\n>>> payroll[\'ДатаФормирования\'] == \'2022-01-01\'\n>>> for employee in payroll:\n...    print(employee[\'Фамилия\'])\n...    print(employee[\'Сумма\'])\n```\n\nDevelopment\n-----------\nWe need installed `pyenv` and `pipenv`.\n```console\ngit clone git@github.com:odoo-ru/payroll-1c.git\n\ncd payroll-1c\npipenv install --dev\n```\n\nRun tests:\n```console\npipenv run fulltest\n```\n',
    'author': 'Dmitry Voronin',
    'author_email': 'dimka665@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/odoo-ru/payroll-1c',
    'py_modules': modules,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
