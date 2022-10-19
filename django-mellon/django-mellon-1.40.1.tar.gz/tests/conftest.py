# django-mellon - SAML2 authentication for Django
# Copyright (C) 2014-2019 Entr'ouvert
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import logging
import os

import django_webtest
import pytest
from django.core.management import call_command
from django.db import connection
from django.db.migrations.executor import MigrationExecutor


@pytest.fixture(autouse=True)
def settings(settings, tmpdir):
    settings.MEDIA_ROOT = str(tmpdir.mkdir('media'))
    return settings


@pytest.fixture
def app(request, settings):
    wtm = django_webtest.WebTestMixin()
    wtm._patch_settings()
    request.addfinalizer(wtm._unpatch_settings)
    return django_webtest.DjangoTestApp()


@pytest.fixture
def concurrency(settings):
    """Select a level of concurrency based on the db, sqlite3 is less robust
    thant postgres due to its transaction lock timeout of 5 seconds.
    """
    if 'sqlite' in settings.DATABASES['default']['ENGINE']:
        return 20
    else:
        return 100


@pytest.fixture
def private_settings(request, tmpdir):
    import django.conf
    from django.conf import UserSettingsHolder

    old = django.conf.settings._wrapped
    django.conf.settings._wrapped = UserSettingsHolder(old)

    def finalizer():
        django.conf.settings._wrapped = old

    request.addfinalizer(finalizer)
    return django.conf.settings


@pytest.fixture
def caplog(caplog):
    import py.io

    caplog.set_level(logging.INFO)
    caplog.handler.stream = py.io.TextIO()
    caplog.handler.records = []
    return caplog


@pytest.fixture(scope='session')
def metadata():
    with open(os.path.join(os.path.dirname(__file__), 'metadata.xml')) as fd:
        yield fd.read()


@pytest.fixture
def metadata_path(tmpdir, metadata):
    metadata_path = tmpdir / 'metadata.xml'
    with metadata_path.open('w') as fd:
        fd.write(metadata)
    yield str(metadata_path)


@pytest.fixture()
def migration(request, transactional_db):
    # see https://gist.github.com/asfaltboy/b3e6f9b5d95af8ba2cc46f2ba6eae5e2
    """
    This fixture returns a helper object to test Django data migrations.
    The fixture returns an object with two methods;
     - `before` to initialize db to the state before the migration under test
     - `after` to execute the migration and bring db to the state after the migration
    The methods return `old_apps` and `new_apps` respectively; these can
    be used to initiate the ORM models as in the migrations themselves.
    For example:
        def test_foo_set_to_bar(migration):
            old_apps = migration.before([('my_app', '0001_inital')])
            Foo = old_apps.get_model('my_app', 'foo')
            Foo.objects.create(bar=False)
            assert Foo.objects.count() == 1
            assert Foo.objects.filter(bar=False).count() == Foo.objects.count()
            # executing migration
            new_apps = migration.apply([('my_app', '0002_set_foo_bar')])
            Foo = new_apps.get_model('my_app', 'foo')

            assert Foo.objects.filter(bar=False).count() == 0
            assert Foo.objects.filter(bar=True).count() == Foo.objects.count()
    Based on: https://gist.github.com/blueyed/4fb0a807104551f103e6
    """

    class Migrator:
        def before(self, targets, at_end=True):
            """Specify app and starting migration names as in:
            before([('app', '0001_before')]) => app/migrations/0001_before.py
            """
            executor = MigrationExecutor(connection)
            executor.migrate(targets)
            executor.loader.build_graph()
            return executor._create_project_state(with_applied_migrations=True).apps

        def apply(self, targets):
            """Migrate forwards to the "targets" migration"""
            executor = MigrationExecutor(connection)
            executor.migrate(targets)
            executor.loader.build_graph()
            return executor._create_project_state(with_applied_migrations=True).apps

    yield Migrator()

    call_command('migrate', verbosity=0)
