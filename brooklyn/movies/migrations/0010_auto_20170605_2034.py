# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-05 15:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0009_userrating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userrating',
            name='movie_title',
            field=models.CharField(default=0, max_length=250),
        ),
    ]
