# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-25 05:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_auto_20170425_1038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genreselect',
            name='Adventure',
            field=models.IntegerField(default=0, null=0),
        ),
        migrations.AlterField(
            model_name='genreselect',
            name='Animation',
            field=models.IntegerField(default=0, null=0),
        ),
        migrations.AlterField(
            model_name='genreselect',
            name='Children',
            field=models.IntegerField(default=0, null=0),
        ),
        migrations.AlterField(
            model_name='genreselect',
            name='Comedy',
            field=models.IntegerField(default=0, null=0),
        ),
        migrations.AlterField(
            model_name='genreselect',
            name='Crime',
            field=models.IntegerField(default=0, null=0),
        ),
        migrations.AlterField(
            model_name='genreselect',
            name='Documentary',
            field=models.IntegerField(default=0, null=0),
        ),
        migrations.AlterField(
            model_name='genreselect',
            name='Drama',
            field=models.IntegerField(default=0, null=0),
        ),
        migrations.AlterField(
            model_name='genreselect',
            name='Fantasy',
            field=models.IntegerField(default=0, null=0),
        ),
        migrations.AlterField(
            model_name='genreselect',
            name='FilmNoir',
            field=models.IntegerField(default=0, null=0),
        ),
        migrations.AlterField(
            model_name='genreselect',
            name='Horror',
            field=models.IntegerField(default=0, null=0),
        ),
        migrations.AlterField(
            model_name='genreselect',
            name='Musical',
            field=models.IntegerField(default=0, null=0),
        ),
        migrations.AlterField(
            model_name='genreselect',
            name='Mystery',
            field=models.IntegerField(default=0, null=0),
        ),
        migrations.AlterField(
            model_name='genreselect',
            name='Romance',
            field=models.IntegerField(default=0, null=0),
        ),
        migrations.AlterField(
            model_name='genreselect',
            name='SciFi',
            field=models.IntegerField(default=0, null=0),
        ),
        migrations.AlterField(
            model_name='genreselect',
            name='Thriller',
            field=models.IntegerField(default=0, null=0),
        ),
        migrations.AlterField(
            model_name='genreselect',
            name='War',
            field=models.IntegerField(default=0, null=0),
        ),
        migrations.AlterField(
            model_name='genreselect',
            name='Western',
            field=models.IntegerField(default=0, null=0),
        ),
    ]
