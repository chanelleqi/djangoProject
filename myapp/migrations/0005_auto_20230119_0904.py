# Generated by Django 3.2.16 on 2023-01-19 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_zodiacsign'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zodiacsign',
            name='element',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='zodiacsign',
            name='planet',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='zodiacsign',
            name='quality',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='zodiacsign',
            name='sign',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='zodiacsign',
            name='symbol',
            field=models.CharField(max_length=50),
        ),
    ]
