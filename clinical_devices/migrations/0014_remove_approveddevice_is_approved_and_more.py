# Generated by Django 5.0.2 on 2024-03-14 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinical_devices', '0013_remove_deviceinformation_is_approved'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='approveddevice',
            name='is_approved',
        ),
        migrations.AddField(
            model_name='deviceinformation',
            name='is_approved',
            field=models.BooleanField(default=False),
        ),
    ]
