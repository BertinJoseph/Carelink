# Generated by Django 5.0.2 on 2024-03-15 06:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Expirylist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expmedicine_name', models.CharField(max_length=200, unique=True)),
                ('expexpiry_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Medicine_Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Medicine_inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medicine_name', models.CharField(max_length=200, unique=True)),
                ('price', models.PositiveIntegerField()),
                ('manufacturer', models.CharField(max_length=200)),
                ('expiry_date', models.DateTimeField(blank=True, null=True)),
                ('quanity_availble', models.PositiveIntegerField()),
                ('image', models.ImageField(null=True, upload_to='images/')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='medicines.medicine_category')),
            ],
        ),
    ]
