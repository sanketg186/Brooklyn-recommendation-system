# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-05 15:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0010_auto_20170605_2034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userrating',
            name='user',
            field=models.CharField(max_length=250),
        ),
    ]
