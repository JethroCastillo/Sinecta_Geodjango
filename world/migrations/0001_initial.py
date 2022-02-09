# Generated by Django 4.0.2 on 2022-02-09 00:19

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Predio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('poly', django.contrib.gis.db.models.fields.PolygonField(srid=4326)),
                ('address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=60)),
            ],
        ),
    ]
