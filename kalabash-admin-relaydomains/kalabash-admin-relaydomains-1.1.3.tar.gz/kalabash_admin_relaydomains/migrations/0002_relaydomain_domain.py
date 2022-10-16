# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kalabash_admin', '0003_domain_type'),
        ('kalabash_admin_relaydomains', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='relaydomain',
            name='domain',
            field=models.OneToOneField(null=True, to='kalabash_admin.Domain'),
            preserve_default=True,
        ),
    ]
