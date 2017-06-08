# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-08 13:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0011_auto_20170605_2037'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movieId', models.IntegerField(default=0)),
                ('title', models.CharField(max_length=500)),
                ('genres', models.CharField(max_length=500)),
            ],
        ),
    ]
