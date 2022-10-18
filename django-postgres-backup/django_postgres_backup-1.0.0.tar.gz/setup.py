# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['django_postgres_backup',
 'django_postgres_backup.management',
 'django_postgres_backup.management.commands',
 'django_postgres_backup.tests']

package_data = \
{'': ['*']}

install_requires = \
['Django>=4.1,<5.0',
 'django-extensions>=3.1.5,<4.0.0',
 'django-libsass>=0.9,<0.10',
 'psycopg2-binary>=2.9.3,<3.0.0',
 'pytest>=7.1.3,<8.0.0',
 'requests>=2.27.1,<3.0.0']

setup_kwargs = {
    'name': 'django-postgres-backup',
    'version': '1.0.0',
    'description': 'Django managed commands to back up and restore a PostgreSQL database with multiple backup generations.',
    'long_description': '[![PyPI](https://img.shields.io/pypi/v/django_postgres_backup)](https://pypi.org/project/django_postgres_backup/)\n[![Python Versions](https://img.shields.io/pypi/pyversions/django_postgres_backup.svg)](https://www.python.org/downloads/)\n[![Build Status](https://github.com/itell-solutions/django_postgres_backup/actions/workflows/build.yaml/badge.svg)](https://github.com/itell-solutions/django_postgres_backup/actions/workflows/build.yaml)\n[![Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)\n[![License](https://img.shields.io/github/license/itell-solutions/django_postgres_backup)](https://opensource.org/licenses/MIT)\n\n# Django managed commands to backup and restore PostgreSQL databases with multiple generations\n\nThe `django_postgres_backup` Django module includes managed commands to back\nup and restore a PostgreSQL database with time stamped names to provide\nmultiple backup generations.\n\n## Installation\n\nTo install, depending on your package manager, run:\n\n```bash\npip install --update django_postgres_backup\n```\n\nor\n\n```bash\npoetry add django_postgres_backup\n```\n\n## Usage\n\nTo add the backup related managed commands to your project, add it to\n`settings.INSTALLED_APPS`.\n\n```python\nINSTALLED_APPS = [\n    ...,\n    "django_postgres_backup",\n]\n```\n\nAfter this, you can backup the default database by running:\n\n```bash\npython manage.py postgres_backup\n```\n\nThe created backup can now be restored by running:\n\n```bash\npython manage.py postgres_backup\n```\n\nYou can clean and restore a whole database with all the tables and data\n\n```bash\npython manage.py postgres_restore --clean --if-exists\n```\n\n## Configuration\n\nYou can set up how many generations of backup should be saved, all other will be deleted.\n\n```python\nPOSTGRES_BACKUP_GENERATIONS = 3\n```\n\n## Limitations\n\nBackup and restore works only with postgresql.\n\n## License\n\nCopyright (c) 2022 ITELL.SOLUTIONS GmbH, Graz, Austria.\n\nDistributed under the\n[MIT license](https://en.wikipedia.org/wiki/MIT_License). For details refer to\nthe file `LICENSE`.\n\nThe source code is available from\n<https://github.com/itell-solutions/django_postgres_backup>.\n',
    'author': 'ITELL.SOLUTIONS GmbH',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/itell-solutions/django_postgres_backup',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4',
}


setup(**setup_kwargs)
