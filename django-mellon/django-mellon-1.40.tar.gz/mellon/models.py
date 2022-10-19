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


import datetime
from importlib import import_module

from django.conf import settings
from django.db import models
from django.utils.timezone import now
from django.utils.translation import gettext_lazy as _


class UserSAMLIdentifier(models.Model):
    user = models.ForeignKey(
        verbose_name=_('user'),
        to=settings.AUTH_USER_MODEL,
        related_name='saml_identifiers',
        on_delete=models.CASCADE,
    )
    name_id = models.TextField(verbose_name=_('SAML identifier'))
    created = models.DateTimeField(verbose_name=_('created'), auto_now_add=True)
    issuer = models.ForeignKey('mellon.Issuer', verbose_name=_('Issuer'), null=True, on_delete=models.CASCADE)

    nid_format = models.TextField(verbose_name=_('NameID Format'), null=True)
    nid_name_qualifier = models.TextField(verbose_name=_('NameID NameQualifier'), null=True)
    nid_sp_name_qualifier = models.TextField(verbose_name=_('NameID SPNameQualifier'), null=True)
    nid_sp_provided_id = models.TextField(verbose_name=('SAML NameID SPPRovidedID'), null=True)

    class Meta:
        verbose_name = _('user SAML identifier')
        verbose_name_plural = _('users SAML identifiers')
        unique_together = (('issuer', 'name_id'),)


class SessionIndex(models.Model):
    session_index = models.TextField(_('SAML SessionIndex'))
    session_key = models.CharField(_('Django session key'), max_length=40)
    transient_name_id = models.TextField(verbose_name=_('Transient NameID'), null=True)
    saml_identifier = models.ForeignKey(
        verbose_name=_('SAML identifier'), to=UserSAMLIdentifier, on_delete=models.CASCADE
    )
    created = models.DateTimeField(verbose_name=_('created'), auto_now_add=True)
    logout_timestamp = models.DateTimeField(verbose_name=_('Timestamp of the last logout'), null=True)

    @classmethod
    def cleanup(cls, delay_in_minutes=5, chunk_size=None):
        session_engine = import_module(settings.SESSION_ENGINE)
        store = session_engine.SessionStore()

        try:
            Session = store.model
        except AttributeError:
            Session = None

        candidates = cls.objects.filter(
            models.Q(logout_timestamp__lt=now() - datetime.timedelta(minutes=delay_in_minutes))
            | models.Q(created__lt=now() - datetime.timedelta(days=1))
        )
        if chunk_size:
            candidates = candidates[:chunk_size]
        candidates_session_keys = candidates.values_list('session_key', flat=True)
        if Session is not None:
            # fast path
            existing_session_keys = Session.objects.filter(
                session_key__in=candidates_session_keys
            ).values_list('session_key', flat=True)
            dead_session_keys = candidates_session_keys.difference(existing_session_keys)
        else:
            dead_session_keys = []
            for session_key in candidates_session_keys:
                if not store.exists(session_key):
                    dead_session_keys.append(session_key)
        cls.objects.filter(session_key__in=dead_session_keys).delete()

    class Meta:
        verbose_name = _('SAML SessionIndex')
        verbose_name_plural = _('SAML SessionIndexes')
        unique_together = (('saml_identifier', 'session_index', 'session_key'),)


class Issuer(models.Model):
    entity_id = models.TextField(verbose_name=_('IdP Entity ID'), unique=True)
    slug = models.TextField(verbose_name=_('IdP slug'), unique=True, null=True)

    class Meta:
        verbose_name = _('SAML IdP')
        verbose_name_plural = _('SAML IdPs')
