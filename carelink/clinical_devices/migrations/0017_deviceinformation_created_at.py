# Generated by Django 5.0.2 on 2024-03-14 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinical_devices', '0016_delete_approveddevice_remove_deviceinformation_uid_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='deviceinformation',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
