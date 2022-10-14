# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['django_router',
 'django_router.management',
 'django_router.management.commands']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'django-router',
    'version': '1.0',
    'description': 'Use simple decorators on views instead of maintaining lengthy urls.py',
    'long_description': '# Django Router\n\nMaintaining Django\'s `urls.py` can become really annoying when you have a lot of \'em(dozens in single file). Other frameworks deal with the problem in more elegant ways, like Flask\'s `@app.route` decorator. This project brings same concept to Django by adding `@router` decorator functions. No more need to deal with lengthy `urls.py`.\n\n# What you get\n\nJust use decorator in your app\'s `views.py`. Django Router uses **autodiscovery** feature, so make sure views you\'re interested in are either inside `views.py` or get imported into it.\n\n```python\n# employees/views.py\nfrom django_router import router\nfrom employees.models import Employee\nfrom django.shortcuts import render\nfrom django.views.generic.edit import CreateView\n\n# Works with function based views\n# Resulting url will be `/employees/employee_list/`\n@router.path()\ndef employee_list(request):\n    employees = Employee.objects.all()\n    return render(request, \'employee_list.html\', {\'employees\':employees})\n\n# As well as with class based views\n# Resulting url will be `/employees/employee_create/`\n@router.path()\ndef EmployeeCreate(CreateView):\n    model = Employee\n\n```\n\nAnd that\'s it!\n\n# How it works\n\nRouter has two functions `path` and `re_path` which work exactly the same as `django.urls` functions you already know. Except that you don\'t even need to specify **url** or **name**.\n\nIf no name is provided function name will be used, camel case will be turned into snake case:\n\n```python\n# same as path(\'import_employees/\', import_employees, name=\'import_employees\')\n@router.path()\ndef import_employees(request):\n    ...\n\n# same as path(\'import_employees/\', ImportEmployees.as_view(), name=\'import_employees\')\n@router.path()\nclass ImportEmployees(View):\n    ...\n```\n\nOf course you can specify path and name as usual:\n\n```python\n@router.path(\'im_emp/\', name=\'employees_import\')\ndef import_employees(request):\n    ...\n```\n\n# Settings\n\nSettings for the project are mostly to control autonaming behavior.\nThese are default settings for the project\n\n```python\nROUTER_SETTINGS={\n    "NAME_WORDS_SEPARATOR": "_"\n    "TRY_USE_MODEL_NAMES": True\n    "MODEL_NAMES_MONOLITHIC": True\n}\n```\n\n---\n\n**`NAME_WORDS_SEPARATOR`**: a separator char that\'ll be used during camel to snake case conversion in view names:\n\n```python\n@router.path()\nclass EmployeeList(ListView):\n    model = Employee\n```\n\n`NAME_WORDS_SEPARATOR = "_"`\n\n`path(\'employee_list/\', EmployeeList.as_view(), name=`**_`\'employee_list\'`_**`)`\n\n`NAME_WORDS_SEPARATOR = "-"`\n\n`path(\'employee_list/\', EmployeeList.as_view(), name=`**_`\'employee-list\'`_**`)`\n\n---\n\n**`TRY_USE_MODEL_NAMES`**: try to use model name for view naming within CBV while forming URLs\n\n```python\n@router.path()\nclass Employees(ListView):\n    model = Employee\n```\n\n`TRY_USE_MODEL_NAMES = True`\n\n`path(\'employee_list/\', Employees.as_view(), name=\'employee_list\')`\n\n`TRY_USE_MODEL_NAMES = False`\n\n`path(\'employees/\', Employees.as_view(), name=\'employees\')`\n\n---\n\n`MODEL_NAMES_MONOLITHIC`: only works when `TRY_USE_MODEL_NAMES = True`, control whether separator is used for model names consisting of multiple words\n\n```python\n@router.path()\nclass EmployeeAddressList(ListView):\n    model = EmployeeAddress\n```\n\n`MODEL_NAMES_MONOLITHIC = True`\n\n`path(\'employeeaddress/\', EmployeesAddressList.as_view(), name=\'employeeaddress_list\')`\n\n`MODEL_NAMES_MONOLITHIC` = False\n\n`path(\'employee_address/\', EmployeesAddressList.as_view(), name=\'employee_address_list\')`\n\n# Management command\n\nYou can run `python manage.py routerlist` to see list of all available routes created by the router.\n',
    'author': 'Real-Gecko',
    'author_email': 'alexandrbezenkov@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/Real-Gecko/django-router',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.4,<4.0',
}


setup(**setup_kwargs)
