# Generated by Django 5.0.2 on 2024-03-22 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autherization', '0010_alter_normaluser_image_alter_nurse_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nurse',
            name='license_number',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
