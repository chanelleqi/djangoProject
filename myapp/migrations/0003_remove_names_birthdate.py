# Generated by Django 3.2.16 on 2023-01-18 23:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_names'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='names',
            name='birthdate',
        ),
    ]