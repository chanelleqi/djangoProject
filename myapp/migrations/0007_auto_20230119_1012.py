# Generated by Django 3.2.16 on 2023-01-19 15:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Names',
        ),
        migrations.DeleteModel(
            name='ZodiacSign',
        ),
    ]
