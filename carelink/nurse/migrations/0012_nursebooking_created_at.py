# Generated by Django 5.0.2 on 2024-04-15 07:16

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nurse', '0011_rename_nurse_report_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='nursebooking',
            name='created_at',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
