# Generated by Django 5.0.2 on 2024-04-15 11:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0004_account'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='device',
            new_name='device_id',
        ),
    ]