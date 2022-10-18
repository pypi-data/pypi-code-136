# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pgactivity', 'pgactivity.management', 'pgactivity.management.commands']

package_data = \
{'': ['*']}

install_requires = \
['django>=2']

extras_require = \
{':python_version >= "3.7" and python_version < "3.8"': ['importlib_metadata>=4']}

setup_kwargs = {
    'name': 'django-pgactivity',
    'version': '1.0.0',
    'description': 'Monitor, kill, and analyze Postgres queries.',
    'long_description': 'django-pgactivity\n#################\n\n``django-pgactivity`` makes it easy to view, filter, and kill\nactive Postgres queries.\n\nSome of the features at a glance:\n\n* The ``PGActivity`` proxy model and ``pgactivity`` management command\n  for querying and filtering the ``pg_stats_activity`` table.\n* ``pgactivity.context`` and ``pgactivity.middleware.ActivityMiddleware``\n  for annotating queries with application metadata, such as the request URL.\n* ``pgactivity.cancel`` and ``pgactivity.terminate`` for cancelling\n  and terminating queries. The ``PGActivity`` model manager also has\n  these methods.\n* ``pgactivity.timeout`` for dynamically setting the statement timeout.\n\nQuick Start\n===========\n\nUse the ``pgactivity ls`` subcommand to see activity queries::\n\n    python manage.py pgactivity ls\n\nOutput looks like the following::\n\n    39225 | 0:01:32 | IDLE_IN_TRANSACTION | None | lock auth_user in access exclusiv\n    39299 | 0:00:15 | ACTIVE | None | SELECT "auth_user"."id", "auth_user"."password\n    39315 | 0:00:00 | ACTIVE | None | WITH _pgactivity_activity_cte AS ( SELECT pid\n\nThe columns are as follows:\n\n1. The process ID of the connection.\n2. The duration of the query.\n3. The state of the query (see the `Postgres docs <https://www.postgresql.org/docs/current/monitoring-stats.html#MONITORING-PG-STAT-ACTIVITY-VIEW>`__ for values).\n4. Attached context using ``pgactivity.context``.\n5. The query SQL.\n\nCancel activity with::\n\n    python manage.py pgactivity cancel <process id> <process id> ...\n\nIdle operations such as the first cannot always be cancelled. Terminate the\nconnection with::\n\n    python manage.py pgactivity terminate <process id> <process id> ...\n\nDecorate your code with ``pgactivity.context`` to attach context to SQL statements.\nInstall ``pgactivity.middleware.ActivityMiddleware`` to automatically add the\nURL and request method to every query. Then you will see values in the\ncontext column::\n\n    39299 | 0:00:15 | ACTIVE | {"url": "/admin/", "method": "GET"} | SELECT "auth_use\n\nDynamically set the SQL statement timeout of code using ``pgactivity.timeout``:\n\n.. code-block:: python\n\n    import pgactivity\n\n    @pgactivity.timeout(pgactivity.timedelta(milliseconds=500))\n    def my_operation():\n        # Any queries in this operation that take over 500 milliseconds will throw\n        # an exception\n\nCompatibility\n=============\n\n``django-pgactivity`` is compatible with Python 3.7 - 3.10, Django 2.2 - 4.1, and Postgres 10 - 15.\n\nDocumentation\n=============\n\n`View the django-pgactivity docs here\n<https://django-pgactivity.readthedocs.io/>`_ for more examples of the management command, configuration\noptions, context tracking, and the proxy model.\n\nInstallation\n============\n\nInstall django-pgactivity with::\n\n    pip3 install django-pgactivity\n\nAfter this, add ``pgactivity`` to the ``INSTALLED_APPS``\nsetting of your Django project.\n\nContributing Guide\n==================\n\nFor information on setting up django-pgactivity for development and\ncontributing changes, view `CONTRIBUTING.rst <CONTRIBUTING.rst>`_.\n\nPrimary Authors\n===============\n\n- `Wes Kendall <https://github.com/wesleykendall>`__\n- `Paul Gilmartin <https://github.com/PaulGilmartin>`__\n',
    'author': 'Opus 10 Engineering',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/Opus10/django-pgactivity',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.7.0,<4',
}


setup(**setup_kwargs)
