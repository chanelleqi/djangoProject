# Generated by Django 3.2.16 on 2023-01-21 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0012_auto_20230120_2311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rates',
            name='x_currency',
            field=models.CharField(max_length=2),
        ),
    ]