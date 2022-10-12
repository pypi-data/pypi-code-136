# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pghistory',
 'pghistory.admin',
 'pghistory.admin.templatetags',
 'pghistory.migrations']

package_data = \
{'': ['*'],
 'pghistory.admin': ['templates/admin/*', 'templates/pghistory_admin/*']}

install_requires = \
['django-pgtrigger>=4.5.0', 'django>=2']

extras_require = \
{':python_version >= "3.7" and python_version < "3.8"': ['importlib_metadata>=4']}

setup_kwargs = {
    'name': 'django-pghistory',
    'version': '2.5.1',
    'description': 'History tracking for Django and Postgres',
    'long_description': 'django-pghistory\n################\n\n``django-pghistory`` tracks changes to your Django models\nusing `Postgres triggers <https://www.postgresql.org/docs/current/sql-createtrigger.html>`__.\nIt offers several advantages over other apps:\n\n* No base models or managers to inherit, no signal handlers, and no custom save methods.\n  All changes are reliably tracked, including bulk methods, with miniscule code.\n* Snapshot all changes to your models, create conditional event trackers, or only\n  track the fields you care about.\n* Changes are stored in structured event tables that mirror your models. No JSON, and you\n  can easily query events in your application.\n* Changes can be grouped together with additional context attached, such as the logged-in\n  user. The middleware can do this automatically.\n\n``django-pghistory`` has a number of ways in which you can configure tracking models\nfor your application\'s needs and for performance and scale. An admin integration\nis included out of the box too.\n\n.. _quick_start:\n\nQuick Start\n===========\n\nDecorate your model with ``pghistory.track``. For example:\n\n.. code-block:: python\n\n    import pghistory\n\n    @pghistory.track(pghistory.Snapshot())\n    class TrackedModel(models.Model):\n        int_field = models.IntegerField()\n        text_field = models.TextField()\n\n\nAbove we\'ve registered a ``pghistory.Snapshot`` event tracker to ``TrackedModel``.\nThis event tracker stores every change in a dynamically-created\nmodel that mirrors fields in ``TrackedModel``.\n\nRun ``python manage.py makemigrations`` followed by ``migrate`` and\n*voila*, every change to ``TrackedModel`` is now stored. This includes bulk\nmethods and even changes that happen in raw SQL. For example:\n\n.. code-block:: python\n\n    from myapp.models import TrackedModel\n\n    # Even though we didn\'t declare TrackedModelEvent, django-pghistory\n    # creates it for us in our app\n    from myapp.models import TrackedModelEvent\n\n    m = TrackedModel.objects.create(int_field=1, text_field="hello")\n    m.int_field = 2\n    m.save()\n\n    print(TrackedModelEvent.objects.values("pgh_obj", "int_field"))\n\n    > [{\'pgh_obj\': 1, \'int_field\': 1}, {\'pgh_obj\': 1, \'int_field\': 2}]\n\nAbove we printed the ``pgh_obj`` field, which is a special foreign key to the tracked\nobject. There are a few other special ``pgh_`` fields that we\'ll discuss later.\n\n``django-pghistory`` can track a subset of fields and conditionally store events\nbased on specific field transitions. Users can also store free-form context\nfrom the application that\'s referenced by the event model, all with no additional\ndatabase queries. See the next steps below on how to dive deeper and configure it\nfor your use case.\n\nCompatibility\n=============\n\n``django-pghistory`` is compatible with Python 3.7 - 3.10, Django 2.2 - 4.1, and Postgres 10 - 14.\n\nDocumentation\n=============\n\n`View the django-pghistory docs here\n<https://django-pghistory.readthedocs.io/>`_ to learn more about:\n\n* The basics and terminology.\n* Tracking historical events on models.\n* Attaching dynamic application context to events.\n* Configuring event models.\n* Aggregating events across event models.\n* The Django admin integration.\n* Reverting models to previous versions.\n* A guide on performance and scale.\n\nThere\'s also additional help, FAQ, and troubleshooting guides.\n\nInstallation\n============\n\nInstall django-pghistory with::\n\n    pip3 install django-pghistory\n\nAfter this, add ``pghistory`` and ``pgtrigger`` to the ``INSTALLED_APPS``\nsetting of your Django project.\n\nContributing Guide\n==================\n\nFor information on setting up django-pghistory for development and\ncontributing changes, view `CONTRIBUTING.rst <CONTRIBUTING.rst>`_.\n\nPrimary Authors\n===============\n\n- @wesleykendall (Wes Kendall, wesleykendall@protonmail.com)\n\nOther Contributors\n==================\n\n- @shivananda-sahu\n- @asucrews\n- @Azurency\n- @dracos\n- @adamchainz\n- @eeriksp\n',
    'author': 'Wes Kendall',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/Opus10/django-pghistory',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.7.0,<4',
}


setup(**setup_kwargs)
