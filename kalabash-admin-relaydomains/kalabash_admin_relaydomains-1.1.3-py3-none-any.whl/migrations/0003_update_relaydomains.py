# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.exceptions import ObjectDoesNotExist
from django.db import models, migrations
from django.db.models.signals import post_delete

from kalabash.core.models import log_object_removal


def get_content_type(apps, app_label, model):
    """Shortcut to retrieve a content type."""
    ContentType = apps.get_model("contenttypes.ContentType")
    return ContentType.objects.get(
        app_label=app_label, model=model)


def update_relay_domains(apps, schema_editor):
    """Create Domain and DomainAlias records."""
    post_delete.disconnect(log_object_removal)

    RelayDomain = apps.get_model("kalabash_admin_relaydomains.RelayDomain")
    Domain = apps.get_model("kalabash_admin.Domain")
    DomainAlias = apps.get_model("kalabash_admin.DomainAlias")
    ObjectAccess = apps.get_model("core.ObjectAccess")

    try:
        rdom_ct = get_content_type(
            apps, "kalabash_admin_relaydomains", "relaydomain")
        rdomalias_ct = get_content_type(
            apps, "kalabash_admin_relaydomains", "relaydomainalias")
        dom_ct = get_content_type(
            apps, "kalabash_admin", "domain")
        domalias_ct = get_content_type(
            apps, "kalabash_admin", "domainalias")
    except ObjectDoesNotExist:
        return

    for rdom in RelayDomain.objects.all():
        rdom.domain = Domain.objects.create(
            name=rdom.name, type="relaydomain", enabled=rdom.enabled,
            dates=rdom.dates, quota=0
        )
        rdom.save()
        for oa in ObjectAccess.objects.filter(
                content_type=rdom_ct, object_id=rdom.id):
            oa.content_type = dom_ct
            oa.object_id = rdom.domain.id
            oa.save()

        for rdomalias in rdom.relaydomainalias_set.all():
            domalias = DomainAlias.objects.create(
                name=rdomalias.name, target=rdomalias.target.domain,
                enabled=rdomalias.enabled, dates=rdomalias.dates
            )
            for oa in ObjectAccess.objects.filter(
                    content_type=rdomalias_ct, object_id=rdomalias.id):
                oa.content_type = domalias_ct
                oa.object_id = domalias.id
                oa.save()
            rdomalias.delete()


class Migration(migrations.Migration):

    dependencies = [
        ('kalabash_admin_relaydomains', '0002_relaydomain_domain'),
    ]

    operations = [
        migrations.RunPython(update_relay_domains)
    ]
