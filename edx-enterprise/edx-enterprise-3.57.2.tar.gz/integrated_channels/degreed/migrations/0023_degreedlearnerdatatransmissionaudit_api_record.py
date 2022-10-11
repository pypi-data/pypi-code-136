# Generated by Django 3.2.15 on 2022-09-29 17:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('integrated_channel', '0021_remove_contentmetadataitemtransmission_api_response_body'),
        ('degreed', '0022_degreedlearnerdatatransmissionaudit_friendly_status_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='degreedlearnerdatatransmissionaudit',
            name='api_record',
            field=models.OneToOneField(blank=True, help_text='Data pertaining to the transmissions API request response.', null=True, on_delete=django.db.models.deletion.CASCADE, to='integrated_channel.apiresponserecord'),
        ),
    ]
