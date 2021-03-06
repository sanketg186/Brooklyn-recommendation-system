# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-21 13:09
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='GenreSelect',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Action', models.BooleanField(default=False)),
                ('Adventure', models.BooleanField(default=False)),
                ('Animation', models.BooleanField(default=False)),
                ('Children', models.BooleanField(default=False)),
                ('Comedy', models.BooleanField(default=False)),
                ('Crime', models.BooleanField(default=False)),
                ('Documentary', models.BooleanField(default=False)),
                ('Drama', models.BooleanField(default=False)),
                ('Fantasy', models.BooleanField(default=False)),
                ('FilmNoir', models.BooleanField(default=False)),
                ('Horror', models.BooleanField(default=False)),
                ('Musical', models.BooleanField(default=False)),
                ('Mystery', models.BooleanField(default=False)),
                ('Romance', models.BooleanField(default=False)),
                ('SciFi', models.BooleanField(default=False)),
                ('Thriller', models.BooleanField(default=False)),
                ('War', models.BooleanField(default=False)),
                ('Western', models.BooleanField(default=False)),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
