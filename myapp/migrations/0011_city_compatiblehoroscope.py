# Generated by Django 3.2.16 on 2023-01-20 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_remove_accountholder_currencies_visited'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('wiki_link', models.URLField()),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='CompatibleHoroscope',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('horoscope', models.CharField(max_length=50)),
                ('compatible_horoscope', models.CharField(max_length=50)),
            ],
        ),
    ]
