# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kalabash_admin_relaydomains', '0003_update_relaydomains'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='relaydomainalias',
            name='dates',
        ),
        migrations.RemoveField(
            model_name='relaydomainalias',
            name='target',
        ),
        migrations.DeleteModel(
            name='RelayDomainAlias',
        ),
        migrations.AlterModelOptions(
            name='relaydomain',
            options={'ordering': ['domain__name']},
        ),
        migrations.RemoveField(
            model_name='relaydomain',
            name='name',
        ),
        migrations.RemoveField(
            model_name='relaydomain',
            name='enabled',
        ),
        migrations.AlterField(
            model_name='relaydomain',
            name='domain',
            field=models.OneToOneField(to='kalabash_admin.Domain'),
            preserve_default=True,
        ),
    ]
