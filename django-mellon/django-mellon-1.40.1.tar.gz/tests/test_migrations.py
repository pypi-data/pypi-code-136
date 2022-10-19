# django-mellon - SAML2 authentication for Django
# Copyright (C) 2014-2021 Entr'ouvert
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

import pytest
from django.contrib.auth.models import User

from mellon.models import Issuer, UserSAMLIdentifier


@pytest.fixture
def user_and_issuers(db):
    user1 = User.objects.create(username='user1')
    user2 = User.objects.create(username='user2')
    issuer1 = Issuer.objects.create(entity_id='https://idp1')
    issuer2 = Issuer.objects.create(entity_id='https://idp2')
    UserSAMLIdentifier.objects.create(user=user1, issuer=issuer1, name_id='xxx')
    UserSAMLIdentifier.objects.create(user=user2, issuer=issuer2, name_id='yyy')


def test_migration_0004_migrate_issuer_back_and_forward(transactional_db, user_and_issuers, migration):
    migration.before([('mellon', '0002_sessionindex')])
    new_apps = migration.apply([('mellon', '0004_migrate_issuer')])

    UserSAMLIdentifier = new_apps.get_model('mellon', 'UserSAMLIdentifier')
    Issuer = new_apps.get_model('mellon', 'Issuer')
    User = new_apps.get_model('auth', 'User')

    user1 = User.objects.get(username='user1')
    user2 = User.objects.get(username='user2')

    assert UserSAMLIdentifier.objects.count() == 2
    assert Issuer.objects.count() == 2
    assert UserSAMLIdentifier.objects.get(user=user1, issuer_fk__entity_id='https://idp1', name_id='xxx')
    assert UserSAMLIdentifier.objects.get(user=user2, issuer_fk__entity_id='https://idp2', name_id='yyy')


def test_migration_0004_migrate_issuer(transactional_db, migration):
    old_apps = migration.before([('mellon', '0003_add_issuer_model')])

    UserSAMLIdentifier = old_apps.get_model('mellon', 'UserSAMLIdentifier')
    User = old_apps.get_model('auth', 'User')

    user1 = User.objects.create(username='user1')
    user2 = User.objects.create(username='user2')

    UserSAMLIdentifier.objects.create(user=user1, issuer='https://idp1', name_id='xxx')
    UserSAMLIdentifier.objects.create(user=user2, issuer='https://idp2', name_id='yyy')

    new_apps = migration.apply([('mellon', '0004_migrate_issuer')])

    UserSAMLIdentifier = new_apps.get_model('mellon', 'UserSAMLIdentifier')
    Issuer = new_apps.get_model('mellon', 'Issuer')
    User = new_apps.get_model('auth', 'User')

    user1 = User.objects.get(username='user1')
    user2 = User.objects.get(username='user2')

    assert UserSAMLIdentifier.objects.count() == 2
    assert Issuer.objects.count() == 2
    assert UserSAMLIdentifier.objects.get(user=user1, issuer_fk__entity_id='https://idp1', name_id='xxx')
    assert UserSAMLIdentifier.objects.get(user=user2, issuer_fk__entity_id='https://idp2', name_id='yyy')
