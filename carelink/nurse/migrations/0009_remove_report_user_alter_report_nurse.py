# Generated by Django 5.0.2 on 2024-04-14 19:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nurse', '0008_report_user_alter_report_nurse'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='report',
            name='user',
        ),
        migrations.AlterField(
            model_name='report',
            name='nurse',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nurse.nursebooking'),
        ),
    ]
