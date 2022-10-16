from django.db import models, migrations

APPLICATIONS = [
    ("admin", "kalabash_admin"),
    ("amavis", "kalabash_amavis"),
    ("limits", "kalabash_admin_limits"),
    ("postfix_autoreply", "kalabash_postfix_autoreply"),
    ("postfix_relay_domains", "kalabash_admin_relaydomains"),
    ("radicale", "kalabash_radicale"),
    ("stats", "kalabash_stats"),
    ("sievefilters", "kalabash_sievefilters"),
    ("webmail", "kalabash_webmail"),
]

def rename_app_parameters(app, model):
    """Rename all parameters for a given app."""
    qset = model.objects.filter(name__startswith=app[0])
    for param in qset:
        param.name = param.name.replace(
            "{}.".format(app[0]), "{}.".format(app[1])
        )
        param.save()


def rename_parameters(apps, schema_editor):
    """Rename old parameters."""
    Parameter = apps.get_model("lib", "Parameter")
    UserParameter = apps.get_model("lib", "UserParameter")
    for app in APPLICATIONS:
        rename_app_parameters(app, Parameter)
        rename_app_parameters(app, UserParameter)


class Migration(migrations.Migration):

    dependencies = [
        ('lib', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(rename_parameters)
    ]
