# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['headlight', 'headlight.drivers', 'headlight.schema']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.1.3,<9.0.0', 'tomlkit>=0.11.1,<0.12.0']

extras_require = \
{'postgresql': ['psycopg2-binary>=2.9.3,<3.0.0']}

entry_points = \
{'console_scripts': ['headlight = headlight.console:main']}

setup_kwargs = {
    'name': 'headlight',
    'version': '0.1.14',
    'description': 'A database migration toolkit.',
    'long_description': '# headlight\n\nA database migration toolkit.\n\n![PyPI](https://img.shields.io/pypi/v/headlight)\n![GitHub Workflow Status](https://img.shields.io/github/workflow/status/alex-oleshkevich/headlight/Lint)\n![GitHub](https://img.shields.io/github/license/alex-oleshkevich/headlight)\n![Libraries.io dependency status for latest release](https://img.shields.io/librariesio/release/pypi/headlight)\n![PyPI - Downloads](https://img.shields.io/pypi/dm/headlight)\n![GitHub Release Date](https://img.shields.io/github/release-date/alex-oleshkevich/headlight)\n\n## Installation\n\nInstall `headlight` using PIP or poetry:\n\n```bash\npip install headlight\n# or\npoetry add headlight\n```\n\n## Features\n\n- TODO\n\n## Usage\n\n### Create migration file\n\n```bash\n# create migration with\nheadlight new --name initial\n```\n\nIt will create a new python file in `migrations` directory\n\n### Define schema\n\n```python\n# migrations/0000_initial.py\n\nfrom headlight import Blueprint, types\n\ndate = "2022-08-21T16:19:13.465195"\nauthor = "alex"\ntransactional = True\n\n\ndef migrate(schema: Blueprint) -> None:\n    with schema.create_table(\'users\') as table:\n        table.autoincrements()\n        table.add_column(\'first_name\', types.VarCharType(256))\n        table.add_column(\'last_name\', types.VarCharType(256))\n        table.add_column(\'email\', types.VarCharType(256))\n        table.add_column(\'password\', types.VarCharType(512))\n        table.add_column(\'active\', types.BooleanType(), default=\'1\')\n        table.add_column(\'photo\', types.VarCharType(512), null=True)\n        table.add_column(\'deleted_at\', types.DateTimeType(True), null=True)\n        table.add_created_timestamp(\'joined_at\')\n        table.add_index([\'(lower(email))\'], unique=True)\n```\n\n### Execute migration\n\n```bash\nheadlight upgrade\n```\n\nAll migrations will be applied to the database\n\n### Rollback migration\n\n```bash\nheadlight downgrade\n```\n\nThe last migration will be rolled back,\n',
    'author': 'Alex Oleshkevich',
    'author_email': 'alex.oleshkevich@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/alex-oleshkevich/headlight',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.10.0,<4.0.0',
}


setup(**setup_kwargs)
