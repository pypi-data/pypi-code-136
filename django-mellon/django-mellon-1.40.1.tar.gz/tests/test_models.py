# django-mellon - SAML2 authentication for Django
# Copyright (C) 2014-2022 Entr'ouvert
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

import datetime
from importlib import import_module

import pytest
from django.utils.timezone import now

from mellon import models


@pytest.mark.parametrize(
    'session_engine_path',
    [
        'mellon.sessions_backends.db',
        'django.contrib.sessions.backends.cache',
    ],
)
def test_session_index_cleaning(session_engine_path, db, settings, django_user_model, freezer):
    settings.SESSION_ENGINE = session_engine_path
    session_engine = import_module(settings.SESSION_ENGINE)
    store = session_engine.SessionStore(None)
    user = django_user_model.objects.create(username='user')
    issuer = models.Issuer.objects.create(entity_id='https://idp.example.com/', slug='idp')
    usi = models.UserSAMLIdentifier.objects.create(user=user, issuer=issuer, name_id='1234')
    store['x'] = 1
    store.set_expiry(86400 * 31)  # expire session after one month
    store.save()
    models.SessionIndex.objects.create(
        session_index='abcd', session_key=store.session_key, saml_identifier=usi
    )
    assert models.SessionIndex.objects.count() == 1

    # check SessionIndex is only cleaned if the session is dead,
    # logout_timestamp being only used as a hint
    freezer.move_to(datetime.timedelta(days=10))
    models.SessionIndex.cleanup()
    assert models.SessionIndex.objects.count() == 1
    models.SessionIndex.objects.update(logout_timestamp=now())
    models.SessionIndex.cleanup()
    assert models.SessionIndex.objects.count() == 1

    store.flush()  # delete the session
    models.SessionIndex.cleanup()
    assert models.SessionIndex.objects.count() == 0
