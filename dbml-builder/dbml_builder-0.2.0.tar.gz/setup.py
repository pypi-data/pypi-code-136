# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['dbml_builder']

package_data = \
{'': ['*']}

install_requires = \
['SQLAlchemy==1.4.41',
 'click>=8.1,<9.0',
 'funcy>=1.17,<2.0',
 'omymodels==0.12.1',
 'pydantic==1.10.2',
 'pydbml==1.0.3']

entry_points = \
{'console_scripts': ['model-build = dbml_builder.cli:main']}

setup_kwargs = {
    'name': 'dbml-builder',
    'version': '0.2.0',
    'description': '',
    'long_description': "# dbml-builder\n\nGenerates Pydantic and SQLAlchemy from a DBML file.\n\nThis package is for users wanting to use their data model represented\nin [DBML](https://www.dbml.org/home/) in production. `dbml-builder` accomplishes this\nby:\n1. Generating Pydantic and SQLAlchemy code.\n2. Verifying existing generated code to see if it matches the specified version and\n   has not been changed since creation.\n\nCurrently, there doesn't seem to be a good solution for code generation with DBML in Python\nhence the creation of `dbml-builder`. Additionally, large software systems tend to break as\nPydantic schemas are modified which is the reason why the package includes verification\nfunctionality.\n\n`dbml-builder` is new and actively developed. If you have any feature requests or issues,\nplease submit them [here](https://github.com/jataware/dbml-builder/issues). \n\n\n## Installation\n\nInstall using pip:\n\n```\npip install dbml_builder\n```\n\n## Usage\n\nGenerate your ORM and schemas by running:\n\n```\nmodel-build generate ./project.dbml ./generated\n```\nor call `generate_models` directly in Python code.\n\n\nYou can check to if the model code is still valid by running:\n```\nmodel-build check v0.9.3 ./generated\n```\nor call `verify` directly in Python code.\n\nNote that the version is what is specified in the `note` for\na given project in DBML.\n\n### Example\n\nSuppose we have a project:\n\n```\n>> ls\nsrc/  LICENSE  poetry.lock  data-model.dbml  pyproject.toml\n```\nwhere `src` contains your code for your python project.\n\nWe can automatically generate code using:\n\n```\npip install dbml_builder\nmodel-build generate ./data-model.dbml ./src/generated\n```\n\nWe can now submit `src/generated` to version control and\nuse the generated code in a module:\n```\nfrom generated.schema import SOME_PYDANTIC_SCHEMA\nfrom generated.orm import SOME_SQLALCHEMY_TABLE\n```\n\nWe can also ensure the generated code is not changed by \nplacing a check in our code:\n```\n# src/main.py\nfrom dbml_builder import verify\n\nverify('v0.1.0', '../data-model.dbml')\n```\n",
    'author': 'Five Grant',
    'author_email': 'five@jataware.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
